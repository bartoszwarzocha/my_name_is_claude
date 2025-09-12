# REST API Design and Implementation

**Agent: api-engineer**
**Purpose: Design and implement scalable, secure REST APIs following best practices**

---

## Context Analysis

The api-engineer will analyze the CLAUDE.md file to determine:
- **Primary Language**: Backend framework detection (Spring Boot, .NET Core, NestJS, FastAPI)
- **Business Domain**: Domain-specific API patterns and authentication requirements
- **Project Scale**: API complexity and enterprise vs. startup patterns
- **Integration Requirements**: External APIs, microservices, or monolithic patterns
- **Database Technology**: ORM selection and data access patterns

Based on this analysis, the engineer will select framework-specific implementation patterns and best practices.

## 🎯 Mission

Create robust, well-documented REST APIs that serve as the backbone for frontend applications and external integrations, following RESTful principles and industry standards.

## 📋 API Design Process

### Step 1: Requirements Analysis
**From architecture specifications:**
- **Functional requirements** from business logic
- **Data models** and entity relationships  
- **Integration needs** with external systems
- **Performance requirements** and expected load
- **Security requirements** and compliance needs

### Step 2: API Contract Design

**Resource Identification:**
- Identify **business entities** as API resources
- Define **resource relationships** and hierarchies
- Plan **resource URLs** following RESTful conventions
- Design **resource representations** (JSON schemas)

**HTTP Methods Mapping:**
- **GET** - Retrieve resources (safe, idempotent)
- **POST** - Create new resources
- **PUT** - Update entire resources (idempotent)
- **PATCH** - Partial resource updates
- **DELETE** - Remove resources (idempotent)

**URL Structure Design:**
```
/api/v1/users                    # Collection of users
/api/v1/users/{id}              # Specific user
/api/v1/users/{id}/orders       # User's orders (nested resource)
/api/v1/orders?status=pending   # Filtered collection
```

### Step 3: Request/Response Design

**Request Structure:**
- **Headers** - Content-Type, Authorization, Accept
- **Query Parameters** - Filtering, sorting, pagination
- **Request Body** - JSON payload with validation rules
- **Path Parameters** - Resource identifiers

**Response Structure:**
```json
{
  "data": {
    "id": "123",
    "type": "user",
    "attributes": { ... },
    "relationships": { ... }
  },
  "meta": {
    "pagination": { ... },
    "total": 150
  },
  "links": {
    "self": "/api/v1/users/123",
    "related": "/api/v1/users/123/orders"
  }
}
```

**Error Response Standards:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "code": "INVALID_FORMAT",
        "message": "Email format is invalid"
      }
    ]
  }
}
```

## Technology-Adaptive Implementation

### Java + Spring Boot REST API

**Recommended Pattern:** Controller-Service-Repository with Spring Data JPA

```java
// Entity Layer
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(unique = true)
    private String email;
    
    @Column(nullable = false)
    private String name;
    
    @Enumerated(EnumType.STRING)
    private UserStatus status;
}

// Repository Layer
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
    
    @Query("SELECT u FROM User u WHERE u.status = :status")
    Page<User> findByStatus(@Param("status") UserStatus status, Pageable pageable);
}

// Service Layer
@Service
@Transactional
public class UserService {
    private final UserRepository userRepository;
    private final UserMapper userMapper;
    
    public UserDto createUser(CreateUserRequest request) {
        if (userRepository.findByEmail(request.getEmail()).isPresent()) {
            throw new BusinessException("User with email already exists");
        }
        
        User user = userMapper.toEntity(request);
        user.setStatus(UserStatus.ACTIVE);
        User savedUser = userRepository.save(user);
        
        return userMapper.toDto(savedUser);
    }
    
    public Page<UserDto> getUsers(UserFilterCriteria criteria, Pageable pageable) {
        return userRepository.findByStatus(criteria.getStatus(), pageable)
                .map(userMapper::toDto);
    }
}

// Controller Layer
@RestController
@RequestMapping("/api/v1/users")
@Validated
public class UserController {
    private final UserService userService;
    
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public ResponseEntity<ApiResponse<UserDto>> createUser(
            @Valid @RequestBody CreateUserRequest request) {
        UserDto user = userService.createUser(request);
        return ResponseEntity.ok(ApiResponse.success(user));
    }
    
    @GetMapping
    public ResponseEntity<ApiResponse<PagedResult<UserDto>>> getUsers(
            UserFilterCriteria criteria,
            @PageableDefault(size = 20, sort = "name") Pageable pageable) {
        Page<UserDto> users = userService.getUsers(criteria, pageable);
        return ResponseEntity.ok(ApiResponse.success(PagedResult.of(users)));
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<ApiResponse<UserDto>> getUser(@PathVariable Long id) {
        return userService.findById(id)
                .map(user -> ResponseEntity.ok(ApiResponse.success(user)))
                .orElse(ResponseEntity.notFound().build());
    }
}

// Exception Handler
@ControllerAdvice
public class ApiExceptionHandler {
    @ExceptionHandler(BusinessException.class)
    public ResponseEntity<ApiResponse<Void>> handleBusinessException(BusinessException ex) {
        return ResponseEntity.badRequest()
                .body(ApiResponse.error(ex.getMessage()));
    }
    
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ApiResponse<Void>> handleValidationException(
            MethodArgumentNotValidException ex) {
        List<ValidationError> errors = ex.getBindingResult().getFieldErrors()
                .stream()
                .map(error -> new ValidationError(error.getField(), error.getDefaultMessage()))
                .collect(Collectors.toList());
        
        return ResponseEntity.badRequest()
                .body(ApiResponse.validationError(errors));
    }
}
```

### .NET Core Web API

**Recommended Pattern:** Clean Architecture with MediatR and CQRS

```csharp
// Domain Entity
public class User : BaseEntity
{
    public string Email { get; private set; }
    public string Name { get; private set; }
    public UserStatus Status { get; private set; }
    
    public User(string email, string name)
    {
        Email = email;
        Name = name;
        Status = UserStatus.Active;
    }
}

// Application Commands/Queries
public class CreateUserCommand : IRequest<ApiResult<UserDto>>
{
    public string Email { get; set; }
    public string Name { get; set; }
}

public class GetUsersQuery : IRequest<ApiResult<PagedResult<UserDto>>>
{
    public UserFilterCriteria Criteria { get; set; }
    public int Page { get; set; } = 1;
    public int PageSize { get; set; } = 20;
}

// Command Handler
public class CreateUserHandler : IRequestHandler<CreateUserCommand, ApiResult<UserDto>>
{
    private readonly IUserRepository _repository;
    private readonly IMapper _mapper;
    
    public async Task<ApiResult<UserDto>> Handle(CreateUserCommand request, CancellationToken cancellationToken)
    {
        // Validation
        if (await _repository.ExistsByEmailAsync(request.Email))
        {
            return ApiResult<UserDto>.Failure("User with email already exists");
        }
        
        var user = new User(request.Email, request.Name);
        await _repository.AddAsync(user);
        await _repository.SaveChangesAsync(cancellationToken);
        
        return ApiResult<UserDto>.Success(_mapper.Map<UserDto>(user));
    }
}

// API Controller
[ApiController]
[Route("api/v1/[controller]")]
public class UsersController : ControllerBase
{
    private readonly IMediator _mediator;
    
    public UsersController(IMediator mediator)
    {
        _mediator = mediator;
    }
    
    [HttpPost]
    [ProducesResponseType(typeof(ApiResponse<UserDto>), 201)]
    [ProducesResponseType(typeof(ApiResponse<object>), 400)]
    public async Task<ActionResult<ApiResponse<UserDto>>> CreateUser([FromBody] CreateUserCommand command)
    {
        var result = await _mediator.Send(command);
        
        if (result.IsSuccess)
        {
            return CreatedAtAction(nameof(GetUser), new { id = result.Data.Id }, 
                ApiResponse<UserDto>.Success(result.Data));
        }
        
        return BadRequest(ApiResponse<object>.Error(result.ErrorMessage));
    }
    
    [HttpGet]
    [ProducesResponseType(typeof(ApiResponse<PagedResult<UserDto>>), 200)]
    public async Task<ActionResult<ApiResponse<PagedResult<UserDto>>>> GetUsers([FromQuery] GetUsersQuery query)
    {
        var result = await _mediator.Send(query);
        return Ok(ApiResponse<PagedResult<UserDto>>.Success(result.Data));
    }
    
    [HttpGet("{id:int}")]
    [ProducesResponseType(typeof(ApiResponse<UserDto>), 200)]
    [ProducesResponseType(404)]
    public async Task<ActionResult<ApiResponse<UserDto>>> GetUser(int id)
    {
        var query = new GetUserByIdQuery { Id = id };
        var result = await _mediator.Send(query);
        
        if (result.IsSuccess)
        {
            return Ok(ApiResponse<UserDto>.Success(result.Data));
        }
        
        return NotFound();
    }
}

// Startup Configuration
public void ConfigureServices(IServiceCollection services)
{
    services.AddControllers();
    services.AddMediatR(typeof(CreateUserHandler));
    services.AddAutoMapper(typeof(UserProfile));
    services.AddSwaggerGen();
    services.AddDbContext<ApplicationDbContext>();
}
```

### Node.js + NestJS API

**Recommended Pattern:** Module-based architecture with TypeORM and decorators

```typescript
// Entity
@Entity('users')
export class User {
  @PrimaryGeneratedColumn()
  id: number;
  
  @Column({ unique: true })
  email: string;
  
  @Column()
  name: string;
  
  @Column({
    type: 'enum',
    enum: UserStatus,
    default: UserStatus.ACTIVE
  })
  status: UserStatus;
  
  @CreateDateColumn()
  createdAt: Date;
  
  @UpdateDateColumn()
  updatedAt: Date;
}

// DTO Classes
export class CreateUserDto {
  @IsEmail()
  @IsNotEmpty()
  email: string;
  
  @IsString()
  @Length(2, 50)
  name: string;
}

export class UserDto {
  id: number;
  email: string;
  name: string;
  status: UserStatus;
  createdAt: Date;
}

// Service
@Injectable()
export class UserService {
  constructor(
    @InjectRepository(User)
    private userRepository: Repository<User>,
  ) {}
  
  async createUser(createUserDto: CreateUserDto): Promise<UserDto> {
    const existingUser = await this.userRepository.findOne({
      where: { email: createUserDto.email }
    });
    
    if (existingUser) {
      throw new ConflictException('User with this email already exists');
    }
    
    const user = this.userRepository.create(createUserDto);
    const savedUser = await this.userRepository.save(user);
    
    return this.mapToDto(savedUser);
  }
  
  async findUsers(criteria: UserFilterCriteria, paginationDto: PaginationDto): Promise<PagedResult<UserDto>> {
    const [users, total] = await this.userRepository.findAndCount({
      where: criteria,
      skip: (paginationDto.page - 1) * paginationDto.limit,
      take: paginationDto.limit,
      order: { [paginationDto.sortBy]: paginationDto.sortOrder }
    });
    
    return {
      data: users.map(user => this.mapToDto(user)),
      meta: {
        page: paginationDto.page,
        limit: paginationDto.limit,
        total,
        totalPages: Math.ceil(total / paginationDto.limit)
      }
    };
  }
  
  private mapToDto(user: User): UserDto {
    return {
      id: user.id,
      email: user.email,
      name: user.name,
      status: user.status,
      createdAt: user.createdAt
    };
  }
}

// Controller
@ApiTags('users')
@Controller('api/v1/users')
export class UserController {
  constructor(private readonly userService: UserService) {}
  
  @Post()
  @ApiOperation({ summary: 'Create a new user' })
  @ApiResponse({ status: 201, description: 'User created successfully', type: ApiResponse<UserDto> })
  @ApiResponse({ status: 400, description: 'Bad Request' })
  @UsePipes(new ValidationPipe())
  async createUser(@Body() createUserDto: CreateUserDto): Promise<ApiResponse<UserDto>> {
    const user = await this.userService.createUser(createUserDto);
    return ApiResponse.success(user);
  }
  
  @Get()
  @ApiOperation({ summary: 'Get users with filtering and pagination' })
  @ApiResponse({ status: 200, description: 'Users retrieved successfully' })
  async getUsers(
    @Query() filterDto: UserFilterDto,
    @Query() paginationDto: PaginationDto
  ): Promise<ApiResponse<PagedResult<UserDto>>> {
    const result = await this.userService.findUsers(filterDto, paginationDto);
    return ApiResponse.success(result);
  }
  
  @Get(':id')
  @ApiParam({ name: 'id', description: 'User ID' })
  @ApiResponse({ status: 200, description: 'User found' })
  @ApiResponse({ status: 404, description: 'User not found' })
  async getUser(@Param('id', ParseIntPipe) id: number): Promise<ApiResponse<UserDto>> {
    const user = await this.userService.findById(id);
    return ApiResponse.success(user);
  }
}

// Exception Filter
@Catch()
export class AllExceptionsFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse<Response>();
    const request = ctx.getRequest<Request>();
    
    let status = 500;
    let message = 'Internal server error';
    
    if (exception instanceof HttpException) {
      status = exception.getStatus();
      message = exception.message;
    }
    
    response.status(status).json({
      statusCode: status,
      timestamp: new Date().toISOString(),
      path: request.url,
      error: message
    });
  }
}
```

### Python + FastAPI

**Recommended Pattern:** Clean Architecture with dependency injection and async support

```python
# Models
from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum as PyEnum

Base = declarative_base()

class UserStatus(PyEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    status = Column(Enum(UserStatus), default=UserStatus.ACTIVE)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Schemas (Pydantic)
from pydantic import BaseModel, EmailStr, validator
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    
    @validator('name')
    def validate_name(cls, v):
        if not v or len(v.strip()) < 2:
            raise ValueError('Name must be at least 2 characters long')
        return v.strip()

class UserDto(BaseModel):
    id: int
    email: str
    name: str
    status: UserStatus
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserFilter(BaseModel):
    status: Optional[UserStatus] = None
    search: Optional[str] = None

class PaginationParams(BaseModel):
    page: int = 1
    limit: int = 20
    
    @validator('page')
    def validate_page(cls, v):
        if v < 1:
            raise ValueError('Page must be >= 1')
        return v
    
    @validator('limit')
    def validate_limit(cls, v):
        if v < 1 or v > 100:
            raise ValueError('Limit must be between 1 and 100')
        return v

# Repository
from typing import Protocol, Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

class UserRepository(Protocol):
    async def create_user(self, user_data: UserCreate) -> User: ...
    async def get_by_email(self, email: str) -> Optional[User]: ...
    async def get_by_id(self, user_id: int) -> Optional[User]: ...
    async def get_users(self, filters: UserFilter, pagination: PaginationParams) -> tuple[List[User], int]: ...

class SQLUserRepository:
    def __init__(self, session: Session):
        self.session = session
    
    async def create_user(self, user_data: UserCreate) -> User:
        db_user = User(**user_data.dict())
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user
    
    async def get_by_email(self, email: str) -> Optional[User]:
        return self.session.query(User).filter(User.email == email).first()
    
    async def get_by_id(self, user_id: int) -> Optional[User]:
        return self.session.query(User).filter(User.id == user_id).first()
    
    async def get_users(self, filters: UserFilter, pagination: PaginationParams) -> tuple[List[User], int]:
        query = self.session.query(User)
        
        # Apply filters
        if filters.status:
            query = query.filter(User.status == filters.status)
        if filters.search:
            search_term = f"%{filters.search}%"
            query = query.filter(or_(User.name.ilike(search_term), User.email.ilike(search_term)))
        
        total = query.count()
        
        # Apply pagination
        offset = (pagination.page - 1) * pagination.limit
        users = query.offset(offset).limit(pagination.limit).all()
        
        return users, total

# Service
from fastapi import HTTPException, status

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    async def create_user(self, user_data: UserCreate) -> UserDto:
        # Check if user exists
        existing_user = await self.repository.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists"
            )
        
        user = await self.repository.create_user(user_data)
        return UserDto.from_orm(user)
    
    async def get_users(self, filters: UserFilter, pagination: PaginationParams) -> dict:
        users, total = await self.repository.get_users(filters, pagination)
        
        return {
            "data": [UserDto.from_orm(user) for user in users],
            "meta": {
                "page": pagination.page,
                "limit": pagination.limit,
                "total": total,
                "total_pages": (total + pagination.limit - 1) // pagination.limit
            }
        }

# FastAPI Routes
from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import Annotated

router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.post("/", response_model=UserDto, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    service: Annotated[UserService, Depends(get_user_service)]
) -> UserDto:
    """Create a new user"""
    return await service.create_user(user_data)

@router.get("/", response_model=dict)
async def get_users(
    service: Annotated[UserService, Depends(get_user_service)],
    status_filter: Optional[UserStatus] = Query(None, alias="status"),
    search: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100)
) -> dict:
    """Get users with filtering and pagination"""
    filters = UserFilter(status=status_filter, search=search)
    pagination = PaginationParams(page=page, limit=limit)
    
    return await service.get_users(filters, pagination)

@router.get("/{user_id}", response_model=UserDto)
async def get_user(
    user_id: int,
    service: Annotated[UserService, Depends(get_user_service)]
) -> UserDto:
    """Get user by ID"""
    user = await service.repository.get_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return UserDto.from_orm(user)

# Exception Handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.status_code,
                "message": exc.detail,
                "timestamp": datetime.utcnow().isoformat()
            }
        }
    )
```

### Generic/Fallback Implementation

For unsupported technologies, provide generic REST API patterns:

```yaml
# Generic REST API Configuration
api:
  base_path: "/api/v1"
  versioning: "path"  # or "header", "query"
  
resource_patterns:
  collections: "/resources"           # GET, POST
  individual: "/resources/{id}"       # GET, PUT, PATCH, DELETE
  nested: "/resources/{id}/subitems" # Nested resources
  
response_format:
  success:
    data: "<resource_data>"
    meta: "<pagination_info>"
    links: "<hypermedia_links>"
  error:
    error:
      code: "ERROR_CODE"
      message: "Human readable message"
      details: ["<validation_errors>"]
      
http_status_codes:
  200: "OK - Successful GET, PUT, PATCH"
  201: "Created - Successful POST"
  204: "No Content - Successful DELETE"
  400: "Bad Request - Validation errors"
  401: "Unauthorized - Authentication required"
  403: "Forbidden - Authorization failed"
  404: "Not Found - Resource doesn't exist"
  409: "Conflict - Resource already exists"
  422: "Unprocessable Entity - Semantic errors"
  500: "Internal Server Error - Server errors"
```

## 🔧 Implementation Guidelines

### Step 4: Database Integration
- **Data Access Layer** with repository patterns
- **Query optimization** and efficient data fetching
- **Transaction management** for data consistency
- **Connection pooling** and database performance
- **Migration scripts** for schema changes

### Step 5: Security Implementation
- **Authentication** - JWT, OAuth2, or session-based
- **Authorization** - Role-based or attribute-based access control
- **Input validation** and sanitization
- **Rate limiting** and throttling
- **HTTPS enforcement** and security headers

### Step 6: Error Handling and Validation
- **Input validation** with detailed error messages
- **Business rule validation** with appropriate HTTP status codes
- **Exception handling** with consistent error responses
- **Logging** for debugging and monitoring
- **Graceful degradation** for external service failures

## 📊 API Quality Standards

### Performance Requirements
- **Response time** targets (e.g., < 200ms for simple queries)
- **Throughput** handling (requests per second)
- **Caching strategies** (Redis, CDN, HTTP caching)
- **Database optimization** (indexing, query tuning)

### Documentation Standards
- **OpenAPI/Swagger** specification
- **Interactive API documentation** with examples
- **Authentication guide** and setup instructions
- **Error code reference** with explanations
- **SDK/client library** generation support

### Testing Strategy
- **Unit tests** for business logic and validations
- **Integration tests** for database interactions
- **Contract tests** for API compatibility
- **Load tests** for performance validation
- **Security tests** for vulnerability assessment

## 🔄 Common API Patterns

### CRUD Operations
```javascript
// Create
POST /api/v1/users
Content-Type: application/json
{ "name": "John Doe", "email": "john@example.com" }

// Read
GET /api/v1/users/123
GET /api/v1/users?page=1&limit=20&sort=name

// Update
PUT /api/v1/users/123
PATCH /api/v1/users/123

// Delete  
DELETE /api/v1/users/123
```

### Pagination Pattern
```javascript
GET /api/v1/users?page=2&limit=20

Response:
{
  "data": [...],
  "meta": {
    "page": 2,
    "limit": 20, 
    "total": 150,
    "totalPages": 8
  },
  "links": {
    "first": "/api/v1/users?page=1&limit=20",
    "prev": "/api/v1/users?page=1&limit=20", 
    "next": "/api/v1/users?page=3&limit=20",
    "last": "/api/v1/users?page=8&limit=20"
  }
}
```

### Filtering and Searching
```javascript
// Simple filtering
GET /api/v1/users?status=active&role=admin

// Text search
GET /api/v1/users?search=john

// Advanced filtering
GET /api/v1/orders?created_after=2023-01-01&amount_min=100
```

## 🚀 Deployment and Monitoring

### API Deployment
- **Environment configuration** (dev, staging, production)
- **Health check endpoints** for load balancers
- **Graceful shutdown** handling
- **Blue-green deployment** support
- **Feature flags** for gradual rollouts

### Monitoring and Observability
- **Metrics collection** (response time, error rates, throughput)
- **Structured logging** with correlation IDs
- **Distributed tracing** for request flow
- **Alerting** on performance degradation or errors
- **API analytics** for usage patterns and optimization

## 🤝 Integration Points

### Frontend Integration
- **CORS configuration** for browser requests
- **API versioning** strategy for backward compatibility
- **Real-time updates** via WebSockets or Server-Sent Events
- **File upload** handling with progress tracking

### External System Integration
- **Third-party API** integration with retry logic
- **Webhook** handling for event-driven architectures
- **Queue integration** for asynchronous processing
- **Circuit breaker** patterns for service resilience

## 📤 Deliverables

- **API Specification** (OpenAPI/Swagger documentation)
- **Implementation Code** with comprehensive test coverage
- **Database Migration Scripts** for schema changes
- **Deployment Configuration** and environment setup
- **Monitoring Setup** with dashboards and alerts
- **Integration Guide** for frontend and external consumers

## 🤝 Collaboration Points

**With frontend-engineer:** API contract validation and integration testing
**With data-engineer:** Database optimization and data access patterns
**With security-engineer:** Authentication, authorization, and security controls
**With qa-engineer:** API testing strategy and automated test suites
**With deployment-engineer:** Deployment pipeline and monitoring setup

## Implementation Strategy

### 1. Technology Detection

Analyze CLAUDE.md configuration to determine:
- **Backend framework** from primary_language field (Java/Spring, .NET Core, Node.js/NestJS, Python/FastAPI)
- **Database technology** for ORM selection and data access patterns
- **Authentication requirements** based on business domain and security needs
- **Integration patterns** for microservices vs. monolithic architectures

### 2. Framework-Specific Implementation

Select implementation patterns based on detected technology:
- **Java/Spring Boot**: Controller-Service-Repository with Spring Data JPA
- **.NET Core**: Clean Architecture with MediatR and CQRS patterns
- **Node.js/NestJS**: Module-based architecture with TypeORM and decorators
- **Python/FastAPI**: Clean Architecture with async support and dependency injection
- **Generic**: Standard REST patterns with appropriate HTTP status codes

### 3. API Design Principles

Apply framework-appropriate patterns:
- **Resource modeling**: RESTful resource identification and URL design
- **Request/Response**: Consistent data structures and error handling
- **Validation**: Input validation and business rule enforcement
- **Security**: Authentication, authorization, and data protection
- **Performance**: Caching, pagination, and query optimization

### 4. Success Criteria

API quality validation checklist:
- **Technology alignment**: Implementation follows framework best practices
- **Performance**: Response times meet SLA requirements
- **Security**: Authentication and authorization properly implemented
- **Documentation**: OpenAPI/Swagger spec with examples and integration guides
- **Testing**: Comprehensive test coverage including contract and load tests

---
*Well-designed APIs provide the foundation for scalable, maintainable applications and enable seamless integration across systems.*