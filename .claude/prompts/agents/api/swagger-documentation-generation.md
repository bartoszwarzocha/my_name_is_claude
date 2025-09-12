# Swagger Documentation Generation from Existing Backend Code

**Agent: api-engineer**
**Purpose: Generate comprehensive Swagger/OpenAPI documentation from existing backend API code**

---

## Context Analysis

The api-engineer will analyze the CLAUDE.md file to determine:
- **Primary Language**: Backend framework detection for appropriate documentation generation (Spring Boot annotations, .NET XML comments, NestJS decorators, FastAPI decorators)
- **API Architecture**: RESTful vs GraphQL patterns and documentation approach
- **Business Domain**: Industry-specific documentation requirements and compliance standards
- **Project Scale**: Documentation complexity and maintenance strategy
- **Integration Requirements**: API consumption patterns and client SDK generation needs

Based on this analysis, the engineer will select framework-specific documentation generation approaches and tools.

## Mission
Generate comprehensive Swagger/OpenAPI documentation from existing backend API code, ensuring complete coverage of endpoints, models, and business logic with production-ready documentation standards.

## Process

### Phase 1: Code Analysis and Discovery

#### 1.1 Backend Code Structure Analysis
```bash
# Analyze project structure
find . -name "*.cs" -o -name "*.js" -o -name "*.ts" -o -name "*.py" | head -20
tree src/ -I "node_modules|bin|obj" -L 3
```

**Key Analysis Points:**
- **Controller/Route Files:** Identify all API controllers and route definitions
- **Model/DTO Classes:** Catalog all data transfer objects and models
- **Business Logic:** Understand service layer and business operations
- **Authentication/Authorization:** Document security implementations
- **Error Handling:** Catalog custom exceptions and error responses

#### 1.2 Existing Documentation Review
```bash
# Check for existing API documentation
find . -name "*.yml" -o -name "*.yaml" -o -name "*.json" | grep -i swagger
find . -name "*swagger*" -o -name "*openapi*"
ls -la docs/ api-docs/ swagger/
```

**Documentation Audit:**
- Existing Swagger files and their completeness
- Inline code documentation quality
- API versioning strategy
- Authentication documentation status

### Phase 2: Swagger Specification Generation

#### 2.1 OpenAPI 3.0 Structure Creation
```yaml
# swagger.yml template structure
openapi: 3.0.3
info:
  title: {Project Name} API
  description: |
    Comprehensive API documentation generated from existing backend code.
    
    ## Authentication
    [Authentication details based on code analysis]
    
    ## Error Handling
    [Standardized error response format]
  version: 1.0.0
  contact:
    name: API Support
    email: api-support@company.com
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT

servers:
  - url: https://api.production.com/v1
    description: Production server
  - url: https://api.staging.com/v1
    description: Staging server
  - url: http://localhost:5000/v1
    description: Development server

paths:
  # [Generated from controller analysis]

components:
  schemas:
    # [Generated from model analysis]
  securitySchemes:
    # [Generated from authentication analysis]

security:
  # [Applied globally based on code analysis]
```

#### 2.2 Endpoint Documentation Generation

**For Each Controller/Route:**
```yaml
# Example endpoint documentation
/api/users/{id}:
  get:
    tags:
      - Users
    summary: Get user by ID
    description: |
      Retrieves detailed user information by unique identifier.
      
      **Business Logic:**
      - Validates user ID format
      - Checks user existence
      - Applies user visibility rules
      - Returns user with related data
      
      **Permissions Required:**
      - User.Read or Admin.Users.Read
    parameters:
      - name: id
        in: path
        required: true
        description: Unique user identifier
        schema:
          type: integer
          format: int64
          minimum: 1
        example: 12345
      - name: include
        in: query
        required: false
        description: Related data to include
        schema:
          type: array
          items:
            type: string
            enum: [profile, preferences, roles]
        style: form
        explode: false
        example: ["profile", "roles"]
    responses:
      '200':
        description: User retrieved successfully
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserDetailResponse'
            examples:
              standard_user:
                summary: Standard user example
                value:
                  id: 12345
                  username: "john.doe"
                  email: "john.doe@example.com"
                  profile: {
                    firstName: "John",
                    lastName: "Doe",
                    avatar: "https://cdn.example.com/avatars/12345.jpg"
                  }
                  roles: ["user"]
                  createdAt: "2024-01-15T10:30:00Z"
              admin_user:
                summary: Admin user example
                value:
                  id: 67890
                  username: "admin"
                  email: "admin@example.com"
                  profile: {
                    firstName: "System",
                    lastName: "Administrator"
                  }
                  roles: ["admin", "user"]
                  createdAt: "2023-12-01T08:00:00Z"
      '400':
        $ref: '#/components/responses/BadRequest'
      '401':
        $ref: '#/components/responses/Unauthorized'
      '403':
        $ref: '#/components/responses/Forbidden'
      '404':
        $ref: '#/components/responses/NotFound'
      '500':
        $ref: '#/components/responses/InternalServerError'
    security:
      - bearerAuth: []
```

#### 2.3 Model Documentation Generation

**For Each Data Model:**
```yaml
# components/schemas section
UserDetailResponse:
  type: object
  description: Complete user information with related data
  required:
    - id
    - username
    - email
    - createdAt
  properties:
    id:
      type: integer
      format: int64
      description: Unique user identifier
      example: 12345
      minimum: 1
    username:
      type: string
      description: Unique username for authentication
      example: "john.doe"
      pattern: "^[a-zA-Z0-9_-]{3,30}$"
      minLength: 3
      maxLength: 30
    email:
      type: string
      format: email
      description: User's primary email address
      example: "john.doe@example.com"
    profile:
      $ref: '#/components/schemas/UserProfile'
    roles:
      type: array
      description: User's assigned roles
      items:
        type: string
        enum: [user, admin, moderator, guest]
      example: ["user"]
    preferences:
      $ref: '#/components/schemas/UserPreferences'
    createdAt:
      type: string
      format: date-time
      description: Account creation timestamp
      example: "2024-01-15T10:30:00Z"
    updatedAt:
      type: string
      format: date-time
      description: Last profile update timestamp
      example: "2024-03-20T14:45:30Z"
    isActive:
      type: boolean
      description: Account status
      example: true
      default: true
  additionalProperties: false

UserProfile:
  type: object
  description: User's profile information
  properties:
    firstName:
      type: string
      description: User's first name
      example: "John"
      maxLength: 50
    lastName:
      type: string
      description: User's last name
      example: "Doe"
      maxLength: 50
    avatar:
      type: string
      format: uri
      description: URL to user's profile picture
      example: "https://cdn.example.com/avatars/12345.jpg"
    bio:
      type: string
      description: User's biography
      example: "Software developer passionate about clean code"
      maxLength: 500
    location:
      type: string
      description: User's location
      example: "New York, NY"
      maxLength: 100
  additionalProperties: false
```

### Phase 3: Advanced Documentation Features

#### 3.1 Security Documentation
```yaml
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: |
        JWT Bearer token authentication.
        
        **Token Structure:**
        - Header: Algorithm and token type
        - Payload: User claims and permissions
        - Signature: Token verification
        
        **Token Lifecycle:**
        - Expires after 24 hours
        - Refresh token available for renewal
        - Automatic logout on token expiration
        
        **Required Claims:**
        - sub: User ID
        - roles: User roles array
        - exp: Expiration timestamp
    
    apiKey:
      type: apiKey
      in: header
      name: X-API-Key
      description: |
        API Key for service-to-service authentication.
        Contact API administrator for key provisioning.
        
        **Usage Guidelines:**
        - Include in all requests
        - Rotate keys quarterly
        - Monitor usage via API dashboard
        
    oauth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://auth.company.com/oauth2/authorize
          tokenUrl: https://auth.company.com/oauth2/token
          scopes:
            read: Read access to user data
            write: Write access to user data
            admin: Administrative access
          description: |
            OAuth 2.0 Authorization Code flow for third-party integrations.
            
            **Setup Process:**
            1. Register application in developer portal
            2. Implement authorization flow
            3. Handle token refresh
            4. Respect rate limits
```

#### 3.2 Error Response Documentation
```yaml
components:
  responses:
    BadRequest:
      description: Invalid request parameters or body
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          examples:
            validation_error:
              summary: Validation error example
              value:
                error: "VALIDATION_ERROR"
                message: "Request validation failed"
                details: [
                  {
                    field: "email",
                    message: "Must be a valid email address",
                    code: "INVALID_FORMAT"
                  },
                  {
                    field: "age",
                    message: "Must be between 18 and 120",
                    code: "OUT_OF_RANGE"
                  }
                ]
                timestamp: "2024-03-20T14:45:30Z"
                requestId: "req_12345"
    
    Unauthorized:
      description: Authentication required or invalid
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          examples:
            missing_token:
              summary: Missing authentication token
              value:
                error: "UNAUTHORIZED"
                message: "Authentication token required"
                details: null
                timestamp: "2024-03-20T14:45:30Z"
                requestId: "req_12346"
            invalid_token:
              summary: Invalid or expired token
              value:
                error: "UNAUTHORIZED"
                message: "Invalid or expired authentication token"
                details: null
                timestamp: "2024-03-20T14:45:30Z"
                requestId: "req_12347"

  schemas:
    ErrorResponse:
      type: object
      description: Standardized error response format
      required:
        - error
        - message
        - timestamp
        - requestId
      properties:
        error:
          type: string
          description: Error code for programmatic handling
          enum: 
            - VALIDATION_ERROR
            - UNAUTHORIZED
            - FORBIDDEN
            - NOT_FOUND
            - CONFLICT
            - RATE_LIMIT_EXCEEDED
            - INTERNAL_ERROR
          example: "VALIDATION_ERROR"
        message:
          type: string
          description: Human-readable error message
          example: "Request validation failed"
        details:
          oneOf:
            - type: array
              items:
                $ref: '#/components/schemas/ValidationError'
            - type: "null"
          description: Additional error details (validation errors, etc.)
        timestamp:
          type: string
          format: date-time
          description: Error occurrence timestamp
          example: "2024-03-20T14:45:30Z"
        requestId:
          type: string
          description: Unique request identifier for debugging
          example: "req_12345"
    
    ValidationError:
      type: object
      required:
        - field
        - message
        - code
      properties:
        field:
          type: string
          description: Field name that failed validation
          example: "email"
        message:
          type: string
          description: Validation error message
          example: "Must be a valid email address"
        code:
          type: string
          description: Validation error code
          enum:
            - REQUIRED
            - INVALID_FORMAT
            - OUT_OF_RANGE
            - TOO_SHORT
            - TOO_LONG
            - DUPLICATE_VALUE
          example: "INVALID_FORMAT"
```

### Phase 4: Documentation Enhancement and Validation

#### 4.1 Code Examples Generation
```yaml
# Add realistic code examples for each endpoint
paths:
  /api/users:
    post:
      # ... endpoint definition
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
            examples:
              standard_user:
                summary: Create standard user
                description: Creates a new user with basic information
                value:
                  username: "jane.smith"
                  email: "jane.smith@example.com"
                  password: "SecurePass123!"
                  profile: {
                    firstName: "Jane",
                    lastName: "Smith",
                    bio: "Product manager with 5 years experience"
                  }
              admin_user:
                summary: Create admin user
                description: Creates a new administrative user
                value:
                  username: "admin.new"
                  email: "admin@company.com"
                  password: "AdminSecurePass456!"
                  roles: ["admin", "user"]
                  profile: {
                    firstName: "Admin",
                    lastName: "User"
                  }
```

#### 4.2 Interactive Documentation Features
```yaml
# Add tags for better organization
tags:
  - name: Users
    description: |
      User management operations
      
      **Key Features:**
      - User registration and authentication
      - Profile management
      - Role-based access control
      - Account preferences
      
      **Business Rules:**
      - Usernames must be unique
      - Email verification required
      - Password complexity enforced
      - Inactive accounts auto-deleted after 2 years
  
  - name: Authentication
    description: |
      Authentication and authorization endpoints
      
      **Supported Methods:**
      - JWT Bearer tokens
      - API Key authentication
      - OAuth 2.0 flows
      
      **Security Features:**
      - Token refresh capability
      - Role-based permissions
      - Rate limiting
      - Audit logging

externalDocs:
  description: Complete API Developer Guide
  url: https://docs.company.com/api/guide
```

## Deliverables

### 1. Complete Swagger/OpenAPI 3.0 Specification
- **File:** `swagger.yml` or `openapi.json`
- **Coverage:** All endpoints, models, and business logic
- **Quality:** Production-ready with examples and validation

### 2. Interactive Documentation
- **Swagger UI** setup for testing and exploration
- **ReDoc** alternative for documentation consumption
- **Postman Collection** export for API testing

### 3. Code Integration
```csharp
// .NET Core integration example
services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new OpenApiInfo 
    { 
        Title = "Company API", 
        Version = "v1",
        Description = "Generated from existing backend code",
        Contact = new OpenApiContact
        {
            Name = "API Support",
            Email = "api-support@company.com"
        }
    });
    
    // Include XML comments
    var xmlFile = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
    var xmlPath = Path.Combine(AppContext.BaseDirectory, xmlFile);
    c.IncludeXmlComments(xmlPath);
    
    // Add JWT authentication
    c.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
    {
        Description = "JWT Authorization header using the Bearer scheme",
        Name = "Authorization",
        In = ParameterLocation.Header,
        Type = SecuritySchemeType.ApiKey,
        Scheme = "Bearer"
    });
});
```

### 4. Documentation Maintenance Plan
- **Automated Generation:** CI/CD integration for documentation updates
- **Versioning Strategy:** API version management and documentation
- **Review Process:** Regular documentation quality audits
- **Developer Onboarding:** Documentation usage guidelines

## Implementation Strategy

### 1. Technology Detection

Analyze CLAUDE.md configuration to determine:
- **Backend framework** from primary_language field for appropriate annotation/decorator selection
- **API patterns** to understand RESTful vs GraphQL documentation requirements
- **Business domain** for industry-specific documentation standards and compliance
- **Integration needs** for client SDK generation and API consumption patterns

### 2. Documentation Tool Selection

Select framework-specific documentation tools:
- **Java/Spring Boot**: SpringDoc OpenAPI with comprehensive annotations
- **.NET Core**: Swashbuckle.AspNetCore with XML comments and attributes
- **Node.js/NestJS**: @nestjs/swagger with decorators and DTOs
- **Python/FastAPI**: Built-in OpenAPI with Pydantic models and comprehensive examples
- **Generic**: Standard OpenAPI 3.0 specification with manual endpoint documentation

### 3. Documentation Generation Approach

Apply technology-specific documentation patterns:
- **Code annotations**: Framework-appropriate decorators and attributes for automatic generation
- **Model documentation**: Comprehensive schema definitions with examples and validation rules
- **Security documentation**: Authentication schemes and authorization requirements
- **Example generation**: Realistic request/response examples for all endpoints

### 4. Success Criteria

API documentation validation checklist:
- **Technology alignment**: Documentation tools and patterns match backend framework
- **Completeness**: All endpoints, models, and business logic documented
- **Accuracy**: Documentation matches actual implementation and behavior
- **Usability**: Interactive documentation works for API testing and exploration
- **Maintainability**: Automated generation integrated with CI/CD pipeline

## Quality Gates

### ✅ Completeness Check
- [ ] All controllers/routes documented
- [ ] All models and DTOs included
- [ ] Authentication methods covered
- [ ] Error responses documented
- [ ] Business logic explained

### ✅ Accuracy Validation
- [ ] Endpoint URLs match implementation
- [ ] Request/response models accurate
- [ ] Status codes correct
- [ ] Authentication requirements verified
- [ ] Examples tested and working

### ✅ Usability Testing
- [ ] Swagger UI renders correctly
- [ ] API testing through documentation works
- [ ] Examples are realistic and helpful
- [ ] Documentation is developer-friendly
- [ ] Search and navigation function properly

## Best Practices

### Documentation Standards
- **Descriptive Summaries:** Clear, concise endpoint descriptions
- **Business Context:** Explain why endpoints exist and their purpose
- **Complete Examples:** Realistic request/response examples
- **Error Scenarios:** Document common error cases
- **Security Clarity:** Clear authentication and authorization requirements

### Maintenance Guidelines
- **Code Comments:** Ensure inline documentation supports generation
- **Automated Updates:** CI/CD pipeline integration
- **Version Control:** Track documentation changes with code changes
- **Regular Reviews:** Monthly documentation quality audits
- **Developer Feedback:** Collect and implement user feedback

## Technology-Adaptive Implementation

### Java + Spring Boot + Swagger/OpenAPI

**Recommended Pattern:** SpringDoc OpenAPI with annotations and automated generation

```java
// Maven Dependencies
/*
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
    <version>2.2.0</version>
</dependency>
*/

// OpenAPI Configuration
@Configuration
@EnableOpenApi
public class OpenApiConfig {
    
    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
            .info(new Info()
                .title("Company API")
                .version("v1.0")
                .description("Comprehensive API documentation generated from Spring Boot code")
                .contact(new Contact()
                    .name("API Support Team")
                    .email("api-support@company.com")
                    .url("https://company.com/support"))
                .license(new License()
                    .name("Apache 2.0")
                    .url("https://www.apache.org/licenses/LICENSE-2.0.html")))
            .servers(Arrays.asList(
                new Server().url("https://api.company.com/v1").description("Production server"),
                new Server().url("https://staging-api.company.com/v1").description("Staging server"),
                new Server().url("http://localhost:8080/v1").description("Development server")
            ))
            .addSecurityItem(new SecurityRequirement().addList("bearerAuth"))
            .components(new Components()
                .addSecuritySchemes("bearerAuth",
                    new SecurityScheme()
                        .type(SecurityScheme.Type.HTTP)
                        .scheme("bearer")
                        .bearerFormat("JWT")
                        .description("JWT Bearer token authentication")));
    }
}

// Controller with comprehensive documentation
@RestController
@RequestMapping("/api/users")
@Tag(name = "Users", description = "User management operations")
@SecurityRequirement(name = "bearerAuth")
public class UserController {
    
    private final UserService userService;
    
    @GetMapping("/{id}")
    @Operation(
        summary = "Get user by ID",
        description = "Retrieves detailed user information by unique identifier. " +
                     "Requires appropriate permissions to access user data."
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "User retrieved successfully",
            content = @Content(
                mediaType = "application/json",
                schema = @Schema(implementation = UserDetailResponse.class),
                examples = {
                    @ExampleObject(
                        name = "Standard User",
                        summary = "Example of standard user response",
                        value = """{"id":12345,"username":"john.doe","email":"john.doe@example.com","profile":{"firstName":"John","lastName":"Doe"},"roles":["user"],"createdAt":"2024-01-15T10:30:00Z"}"""
                    ),
                    @ExampleObject(
                        name = "Admin User",
                        summary = "Example of admin user response",
                        value = """{"id":67890,"username":"admin","email":"admin@company.com","profile":{"firstName":"System","lastName":"Administrator"},"roles":["admin","user"],"createdAt":"2023-12-01T08:00:00Z"}"""
                    )
                }
            )
        ),
        @ApiResponse(
            responseCode = "400",
            description = "Invalid user ID format",
            content = @Content(
                mediaType = "application/json",
                schema = @Schema(implementation = ErrorResponse.class)
            )
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Authentication required",
            content = @Content(
                mediaType = "application/json",
                schema = @Schema(implementation = ErrorResponse.class)
            )
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Insufficient permissions",
            content = @Content(
                mediaType = "application/json",
                schema = @Schema(implementation = ErrorResponse.class)
            )
        ),
        @ApiResponse(
            responseCode = "404",
            description = "User not found",
            content = @Content(
                mediaType = "application/json",
                schema = @Schema(implementation = ErrorResponse.class)
            )
        )
    })
    public ResponseEntity<UserDetailResponse> getUserById(
            @Parameter(
                description = "Unique user identifier",
                required = true,
                example = "12345",
                schema = @Schema(type = "integer", format = "int64", minimum = "1")
            )
            @PathVariable Long id,
            
            @Parameter(
                description = "Related data to include in response",
                required = false,
                example = "profile,roles",
                schema = @Schema(
                    type = "array",
                    allowableValues = {"profile", "preferences", "roles"}
                )
            )
            @RequestParam(required = false) List<String> include
    ) {
        UserDetailResponse user = userService.getUserById(id, include);
        return ResponseEntity.ok(user);
    }
    
    @PostMapping
    @Operation(
        summary = "Create new user",
        description = "Creates a new user account with the provided information. " +
                     "Email must be unique and password must meet complexity requirements."
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "201",
            description = "User created successfully",
            content = @Content(
                mediaType = "application/json",
                schema = @Schema(implementation = UserDetailResponse.class)
            )
        ),
        @ApiResponse(
            responseCode = "400",
            description = "Validation errors in request data",
            content = @Content(
                mediaType = "application/json",
                schema = @Schema(implementation = ValidationErrorResponse.class),
                examples = @ExampleObject(
                    value = """{"error":"VALIDATION_ERROR","message":"Request validation failed","details":[{"field":"email","message":"Must be a valid email address","code":"INVALID_FORMAT"}],"timestamp":"2024-03-20T14:45:30Z","requestId":"req_12345"}"""
                )
            )
        ),
        @ApiResponse(
            responseCode = "409",
            description = "User with email already exists",
            content = @Content(
                mediaType = "application/json",
                schema = @Schema(implementation = ErrorResponse.class)
            )
        )
    })
    public ResponseEntity<UserDetailResponse> createUser(
            @io.swagger.v3.oas.annotations.parameters.RequestBody(
                description = "User creation data",
                required = true,
                content = @Content(
                    mediaType = "application/json",
                    schema = @Schema(implementation = CreateUserRequest.class),
                    examples = {
                        @ExampleObject(
                            name = "Standard User Creation",
                            summary = "Create a standard user account",
                            value = """{"username":"jane.smith","email":"jane.smith@example.com","password":"SecurePass123!","profile":{"firstName":"Jane","lastName":"Smith","bio":"Product manager with 5 years experience"}}"""
                        )
                    }
                )
            )
            @Valid @RequestBody CreateUserRequest request
    ) {
        UserDetailResponse user = userService.createUser(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }
}

// Model Documentation with Schema annotations
@Schema(description = "Complete user information with related data")
public class UserDetailResponse {
    
    @Schema(
        description = "Unique user identifier",
        example = "12345",
        minimum = "1",
        requiredMode = Schema.RequiredMode.REQUIRED
    )
    private Long id;
    
    @Schema(
        description = "Unique username for authentication",
        example = "john.doe",
        pattern = "^[a-zA-Z0-9_-]{3,30}$",
        minLength = 3,
        maxLength = 30,
        requiredMode = Schema.RequiredMode.REQUIRED
    )
    private String username;
    
    @Schema(
        description = "User's primary email address",
        example = "john.doe@example.com",
        format = "email",
        requiredMode = Schema.RequiredMode.REQUIRED
    )
    private String email;
    
    @Schema(
        description = "User's profile information",
        implementation = UserProfile.class
    )
    private UserProfile profile;
    
    @Schema(
        description = "User's assigned roles",
        example = "[\"user\"]",
        allowableValues = {"user", "admin", "moderator", "guest"}
    )
    private List<String> roles;
    
    @Schema(
        description = "Account creation timestamp",
        example = "2024-01-15T10:30:00Z",
        format = "date-time",
        requiredMode = Schema.RequiredMode.REQUIRED
    )
    private Instant createdAt;
    
    @Schema(
        description = "Last profile update timestamp",
        example = "2024-03-20T14:45:30Z",
        format = "date-time"
    )
    private Instant updatedAt;
    
    @Schema(
        description = "Account status",
        example = "true",
        defaultValue = "true",
        requiredMode = Schema.RequiredMode.REQUIRED
    )
    private Boolean isActive;
    
    // Constructors, getters, setters...
}

// Error Response Documentation
@Schema(description = "Standardized error response format")
public class ErrorResponse {
    
    @Schema(
        description = "Error code for programmatic handling",
        example = "VALIDATION_ERROR",
        allowableValues = {
            "VALIDATION_ERROR", "UNAUTHORIZED", "FORBIDDEN", 
            "NOT_FOUND", "CONFLICT", "RATE_LIMIT_EXCEEDED", "INTERNAL_ERROR"
        },
        requiredMode = Schema.RequiredMode.REQUIRED
    )
    private String error;
    
    @Schema(
        description = "Human-readable error message",
        example = "Request validation failed",
        requiredMode = Schema.RequiredMode.REQUIRED
    )
    private String message;
    
    @Schema(
        description = "Additional error details (validation errors, etc.)",
        oneOf = {ValidationError[].class, Object.class}
    )
    private Object details;
    
    @Schema(
        description = "Error occurrence timestamp",
        example = "2024-03-20T14:45:30Z",
        format = "date-time",
        requiredMode = Schema.RequiredMode.REQUIRED
    )
    private Instant timestamp;
    
    @Schema(
        description = "Unique request identifier for debugging",
        example = "req_12345",
        requiredMode = Schema.RequiredMode.REQUIRED
    )
    private String requestId;
    
    // Constructors, getters, setters...
}

// Application Properties for Swagger UI customization
# application.yml
springdoc:
  api-docs:
    path: /api-docs
  swagger-ui:
    path: /swagger-ui.html
    tryItOutEnabled: true
    operationsSorter: method
    tagsSorter: alpha
    displayRequestDuration: true
    docExpansion: none
  show-actuator: false
  writer-with-default-pretty-printer: true
```

### .NET Core + Swashbuckle + XML Documentation

**Recommended Pattern:** Swashbuckle.AspNetCore with XML comments and attributes

```csharp
// NuGet Packages
/*
<PackageReference Include="Swashbuckle.AspNetCore" Version="6.5.0" />
<PackageReference Include="Swashbuckle.AspNetCore.Annotations" Version="6.5.0" />
*/

// Startup Configuration
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddControllers();
        
        services.AddSwaggerGen(c =>
        {
            c.SwaggerDoc("v1", new OpenApiInfo
            {
                Title = "Company API",
                Version = "v1",
                Description = "Comprehensive API documentation generated from .NET Core code",
                Contact = new OpenApiContact
                {
                    Name = "API Support Team",
                    Email = "api-support@company.com",
                    Url = new Uri("https://company.com/support")
                },
                License = new OpenApiLicense
                {
                    Name = "MIT License",
                    Url = new Uri("https://opensource.org/licenses/MIT")
                }
            });
            
            // Add JWT authentication
            c.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
            {
                Description = "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\"",
                Name = "Authorization",
                In = ParameterLocation.Header,
                Type = SecuritySchemeType.ApiKey,
                Scheme = "Bearer"
            });
            
            c.AddSecurityRequirement(new OpenApiSecurityRequirement
            {
                {
                    new OpenApiSecurityScheme
                    {
                        Reference = new OpenApiReference
                        {
                            Type = ReferenceType.SecurityScheme,
                            Id = "Bearer"
                        }
                    },
                    Array.Empty<string>()
                }
            });
            
            // Include XML comments
            var xmlFilename = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
            var xmlPath = Path.Combine(AppContext.BaseDirectory, xmlFilename);
            c.IncludeXmlComments(xmlPath);
            
            // Enable annotations
            c.EnableAnnotations();
            
            // Add examples
            c.SchemaFilter<ExampleSchemaFilter>();
            c.OperationFilter<ExampleOperationFilter>();
        });
    }
    
    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        if (env.IsDevelopment())
        {
            app.UseSwagger();
            app.UseSwaggerUI(c =>
            {
                c.SwaggerEndpoint("/swagger/v1/swagger.json", "Company API V1");
                c.RoutePrefix = "swagger";
                c.DisplayRequestDuration();
                c.DocExpansion(DocExpansion.None);
                c.DefaultModelsExpandDepth(-1);
            });
        }
    }
}

// Controller with comprehensive documentation
/// <summary>
/// User management operations
/// </summary>
/// <remarks>
/// Provides endpoints for user creation, retrieval, updating, and management.
/// All operations require appropriate authentication and authorization.
/// </remarks>
[ApiController]
[Route("api/[controller]")]
[SwaggerTag("User management operations including registration, authentication, and profile management")]
[Authorize]
public class UsersController : ControllerBase
{
    private readonly IUserService _userService;
    
    public UsersController(IUserService userService)
    {
        _userService = userService;
    }
    
    /// <summary>
    /// Retrieves detailed user information by unique identifier
    /// </summary>
    /// <param name="id">Unique user identifier</param>
    /// <param name="include">Related data to include in response (profile, roles, preferences)</param>
    /// <returns>User details with requested related data</returns>
    /// <remarks>
    /// Sample request:
    /// 
    ///     GET /api/users/12345?include=profile,roles
    /// 
    /// Business Logic:
    /// - Validates user ID format
    /// - Checks user existence
    /// - Applies user visibility rules
    /// - Returns user with related data
    /// 
    /// Permissions Required:
    /// - User.Read or Admin.Users.Read
    /// </remarks>
    /// <response code="200">User retrieved successfully</response>
    /// <response code="400">Invalid user ID format</response>
    /// <response code="401">Authentication required</response>
    /// <response code="403">Insufficient permissions</response>
    /// <response code="404">User not found</response>
    [HttpGet("{id:long}")]
    [SwaggerOperation(
        Summary = "Get user by ID",
        Description = "Retrieves detailed user information by unique identifier. Requires appropriate permissions to access user data.",
        OperationId = "GetUserById",
        Tags = new[] { "Users" }
    )]
    [SwaggerResponse(200, "User retrieved successfully", typeof(UserDetailResponse))]
    [SwaggerResponse(400, "Invalid user ID format", typeof(ErrorResponse))]
    [SwaggerResponse(401, "Authentication required", typeof(ErrorResponse))]
    [SwaggerResponse(403, "Insufficient permissions", typeof(ErrorResponse))]
    [SwaggerResponse(404, "User not found", typeof(ErrorResponse))]
    public async Task<ActionResult<UserDetailResponse>> GetUserById(
        [FromRoute] long id,
        [FromQuery] string[] include = null)
    {
        var user = await _userService.GetUserByIdAsync(id, include);
        return Ok(user);
    }
    
    /// <summary>
    /// Creates a new user account
    /// </summary>
    /// <param name="request">User creation data</param>
    /// <returns>Created user details</returns>
    /// <remarks>
    /// Sample request:
    /// 
    ///     POST /api/users
    ///     {
    ///         "username": "jane.smith",
    ///         "email": "jane.smith@example.com",
    ///         "password": "SecurePass123!",
    ///         "profile": {
    ///             "firstName": "Jane",
    ///             "lastName": "Smith",
    ///             "bio": "Product manager with 5 years experience"
    ///         }
    ///     }
    /// 
    /// Business Rules:
    /// - Username must be unique
    /// - Email must be unique and valid format
    /// - Password must meet complexity requirements
    /// - Email verification will be required
    /// </remarks>
    /// <response code="201">User created successfully</response>
    /// <response code="400">Validation errors in request data</response>
    /// <response code="409">User with email already exists</response>
    [HttpPost]
    [SwaggerOperation(
        Summary = "Create new user",
        Description = "Creates a new user account with the provided information. Email must be unique and password must meet complexity requirements.",
        OperationId = "CreateUser",
        Tags = new[] { "Users" }
    )]
    [SwaggerResponse(201, "User created successfully", typeof(UserDetailResponse))]
    [SwaggerResponse(400, "Validation errors in request data", typeof(ValidationErrorResponse))]
    [SwaggerResponse(409, "User with email already exists", typeof(ErrorResponse))]
    public async Task<ActionResult<UserDetailResponse>> CreateUser(
        [FromBody, SwaggerRequestBody("User creation data", Required = true)] CreateUserRequest request)
    {
        var user = await _userService.CreateUserAsync(request);
        return CreatedAtAction(nameof(GetUserById), new { id = user.Id }, user);
    }
}

// Model with comprehensive documentation
/// <summary>
/// Complete user information with related data
/// </summary>
/// <example>
/// {
///   "id": 12345,
///   "username": "john.doe",
///   "email": "john.doe@example.com",
///   "profile": {
///     "firstName": "John",
///     "lastName": "Doe"
///   },
///   "roles": ["user"],
///   "createdAt": "2024-01-15T10:30:00Z",
///   "isActive": true
/// }
/// </example>
[SwaggerSchema("Complete user information with related data")]
public class UserDetailResponse
{
    /// <summary>
    /// Unique user identifier
    /// </summary>
    /// <example>12345</example>
    [SwaggerSchema("Unique user identifier", Format = "int64")]
    [Required]
    public long Id { get; set; }
    
    /// <summary>
    /// Unique username for authentication
    /// </summary>
    /// <example>john.doe</example>
    [SwaggerSchema("Unique username for authentication", Pattern = "^[a-zA-Z0-9_-]{3,30}$")]
    [Required]
    [StringLength(30, MinimumLength = 3)]
    public string Username { get; set; }
    
    /// <summary>
    /// User's primary email address
    /// </summary>
    /// <example>john.doe@example.com</example>
    [SwaggerSchema("User's primary email address", Format = "email")]
    [Required]
    [EmailAddress]
    public string Email { get; set; }
    
    /// <summary>
    /// User's profile information
    /// </summary>
    [SwaggerSchema("User's profile information")]
    public UserProfile Profile { get; set; }
    
    /// <summary>
    /// User's assigned roles
    /// </summary>
    /// <example>["user"]</example>
    [SwaggerSchema("User's assigned roles")]
    public List<string> Roles { get; set; } = new List<string>();
    
    /// <summary>
    /// Account creation timestamp
    /// </summary>
    /// <example>2024-01-15T10:30:00Z</example>
    [SwaggerSchema("Account creation timestamp", Format = "date-time")]
    [Required]
    public DateTime CreatedAt { get; set; }
    
    /// <summary>
    /// Last profile update timestamp
    /// </summary>
    /// <example>2024-03-20T14:45:30Z</example>
    [SwaggerSchema("Last profile update timestamp", Format = "date-time")]
    public DateTime? UpdatedAt { get; set; }
    
    /// <summary>
    /// Account status
    /// </summary>
    /// <example>true</example>
    [SwaggerSchema("Account status", Default = true)]
    [Required]
    public bool IsActive { get; set; } = true;
}

// Project file configuration for XML documentation
/*
<Project Sdk="Microsoft.NET.Sdk.Web">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <GenerateDocumentationFile>true</GenerateDocumentationFile>
    <NoWarn>$(NoWarn);1591</NoWarn>
  </PropertyGroup>
</Project>
*/
```

### Node.js + NestJS + Swagger

**Recommended Pattern:** @nestjs/swagger with decorators and DTOs

```typescript
// Package Dependencies
/*
npm install @nestjs/swagger swagger-ui-express
*/

// Main Application Setup
import { NestFactory } from '@nestjs/core';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';
import { ValidationPipe } from '@nestjs/common';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  
  // Global validation pipe
  app.useGlobalPipes(new ValidationPipe({
    transform: true,
    whitelist: true,
    forbidNonWhitelisted: true,
  }));
  
  // Swagger configuration
  const config = new DocumentBuilder()
    .setTitle('Company API')
    .setDescription('Comprehensive API documentation generated from NestJS code')
    .setVersion('1.0')
    .setContact('API Support Team', 'https://company.com/support', 'api-support@company.com')
    .setLicense('MIT License', 'https://opensource.org/licenses/MIT')
    .addServer('https://api.company.com/v1', 'Production server')
    .addServer('https://staging-api.company.com/v1', 'Staging server')
    .addServer('http://localhost:3000/v1', 'Development server')
    .addBearerAuth(
      {
        type: 'http',
        scheme: 'bearer',
        bearerFormat: 'JWT',
        name: 'JWT',
        description: 'Enter JWT token',
        in: 'header',
      },
      'JWT-auth'
    )
    .addApiKey(
      {
        type: 'apiKey',
        name: 'X-API-Key',
        in: 'header',
        description: 'API Key for service-to-service authentication',
      },
      'api-key'
    )
    .addTag('Users', 'User management operations')
    .addTag('Authentication', 'Authentication and authorization endpoints')
    .build();
    
  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('swagger', app, document, {
    swaggerOptions: {
      persistAuthorization: true,
      displayRequestDuration: true,
      docExpansion: 'none',
      operationsSorter: 'method',
      tagsSorter: 'alpha',
      tryItOutEnabled: true,
    },
    customSiteTitle: 'Company API Documentation',
  });
  
  await app.listen(3000);
}
bootstrap();

// DTOs with comprehensive documentation
import { ApiProperty, ApiPropertyOptional } from '@nestjs/swagger';
import { IsEmail, IsString, IsOptional, Length, IsArray, IsBoolean, IsDateString } from 'class-validator';
import { Transform } from 'class-transformer';

export class CreateUserRequest {
  @ApiProperty({
    description: 'Unique username for authentication',
    example: 'jane.smith',
    minLength: 3,
    maxLength: 30,
    pattern: '^[a-zA-Z0-9_-]{3,30}$',
  })
  @IsString()
  @Length(3, 30)
  username: string;
  
  @ApiProperty({
    description: "User's primary email address",
    example: 'jane.smith@example.com',
    format: 'email',
  })
  @IsEmail()
  email: string;
  
  @ApiProperty({
    description: 'Account password - must meet complexity requirements',
    example: 'SecurePass123!',
    minLength: 8,
    maxLength: 128,
    writeOnly: true,
  })
  @IsString()
  @Length(8, 128)
  password: string;
  
  @ApiPropertyOptional({
    description: "User's profile information",
    type: () => UserProfileRequest,
  })
  @IsOptional()
  profile?: UserProfileRequest;
  
  @ApiPropertyOptional({
    description: "User's initial roles",
    example: ['user'],
    enum: ['user', 'admin', 'moderator', 'guest'],
    isArray: true,
  })
  @IsOptional()
  @IsArray()
  @IsString({ each: true })
  roles?: string[];
}

export class UserDetailResponse {
  @ApiProperty({
    description: 'Unique user identifier',
    example: 12345,
    type: 'integer',
    format: 'int64',
    minimum: 1,
  })
  id: number;
  
  @ApiProperty({
    description: 'Unique username for authentication',
    example: 'john.doe',
    minLength: 3,
    maxLength: 30,
    pattern: '^[a-zA-Z0-9_-]{3,30}$',
  })
  username: string;
  
  @ApiProperty({
    description: "User's primary email address",
    example: 'john.doe@example.com',
    format: 'email',
  })
  email: string;
  
  @ApiPropertyOptional({
    description: "User's profile information",
    type: () => UserProfile,
  })
  profile?: UserProfile;
  
  @ApiProperty({
    description: "User's assigned roles",
    example: ['user'],
    enum: ['user', 'admin', 'moderator', 'guest'],
    isArray: true,
  })
  roles: string[];
  
  @ApiProperty({
    description: 'Account creation timestamp',
    example: '2024-01-15T10:30:00Z',
    format: 'date-time',
  })
  createdAt: string;
  
  @ApiPropertyOptional({
    description: 'Last profile update timestamp',
    example: '2024-03-20T14:45:30Z',
    format: 'date-time',
  })
  updatedAt?: string;
  
  @ApiProperty({
    description: 'Account status',
    example: true,
    default: true,
  })
  isActive: boolean;
}

// Controller with comprehensive documentation
@ApiTags('Users')
@ApiBearerAuth('JWT-auth')
@Controller('api/users')
@UseGuards(JwtAuthGuard)
export class UsersController {
  constructor(private readonly usersService: UsersService) {}
  
  @Get(':id')
  @ApiOperation({
    summary: 'Get user by ID',
    description: `
      Retrieves detailed user information by unique identifier.
      Requires appropriate permissions to access user data.
      
      **Business Logic:**
      - Validates user ID format
      - Checks user existence
      - Applies user visibility rules
      - Returns user with related data
      
      **Permissions Required:**
      - User.Read or Admin.Users.Read
    `,
    operationId: 'getUserById',
  })
  @ApiParam({
    name: 'id',
    description: 'Unique user identifier',
    example: 12345,
    type: 'integer',
    format: 'int64',
  })
  @ApiQuery({
    name: 'include',
    description: 'Related data to include in response',
    required: false,
    example: ['profile', 'roles'],
    enum: ['profile', 'preferences', 'roles'],
    isArray: true,
    explode: false,
  })
  @ApiResponse({
    status: 200,
    description: 'User retrieved successfully',
    type: UserDetailResponse,
    examples: {
      'Standard User': {
        summary: 'Example of standard user response',
        value: {
          id: 12345,
          username: 'john.doe',
          email: 'john.doe@example.com',
          profile: {
            firstName: 'John',
            lastName: 'Doe',
          },
          roles: ['user'],
          createdAt: '2024-01-15T10:30:00Z',
          isActive: true,
        },
      },
      'Admin User': {
        summary: 'Example of admin user response',
        value: {
          id: 67890,
          username: 'admin',
          email: 'admin@company.com',
          profile: {
            firstName: 'System',
            lastName: 'Administrator',
          },
          roles: ['admin', 'user'],
          createdAt: '2023-12-01T08:00:00Z',
          isActive: true,
        },
      },
    },
  })
  @ApiResponse({
    status: 400,
    description: 'Invalid user ID format',
    type: ErrorResponse,
  })
  @ApiResponse({
    status: 401,
    description: 'Authentication required',
    type: ErrorResponse,
  })
  @ApiResponse({
    status: 403,
    description: 'Insufficient permissions',
    type: ErrorResponse,
  })
  @ApiResponse({
    status: 404,
    description: 'User not found',
    type: ErrorResponse,
  })
  async getUserById(
    @Param('id', ParseIntPipe) id: number,
    @Query('include') include?: string[],
  ): Promise<UserDetailResponse> {
    return this.usersService.findById(id, include);
  }
  
  @Post()
  @ApiOperation({
    summary: 'Create new user',
    description: `
      Creates a new user account with the provided information.
      Email must be unique and password must meet complexity requirements.
      
      **Business Rules:**
      - Username must be unique
      - Email must be unique and valid format
      - Password must meet complexity requirements
      - Email verification will be required
    `,
    operationId: 'createUser',
  })
  @ApiBody({
    description: 'User creation data',
    type: CreateUserRequest,
    examples: {
      'Standard User Creation': {
        summary: 'Create a standard user account',
        value: {
          username: 'jane.smith',
          email: 'jane.smith@example.com',
          password: 'SecurePass123!',
          profile: {
            firstName: 'Jane',
            lastName: 'Smith',
            bio: 'Product manager with 5 years experience',
          },
        },
      },
    },
  })
  @ApiResponse({
    status: 201,
    description: 'User created successfully',
    type: UserDetailResponse,
  })
  @ApiResponse({
    status: 400,
    description: 'Validation errors in request data',
    type: ValidationErrorResponse,
  })
  @ApiResponse({
    status: 409,
    description: 'User with email already exists',
    type: ErrorResponse,
  })
  async createUser(
    @Body() createUserDto: CreateUserRequest,
  ): Promise<UserDetailResponse> {
    return this.usersService.create(createUserDto);
  }
}

// Error Response Models
export class ErrorResponse {
  @ApiProperty({
    description: 'Error code for programmatic handling',
    example: 'VALIDATION_ERROR',
    enum: [
      'VALIDATION_ERROR',
      'UNAUTHORIZED', 
      'FORBIDDEN',
      'NOT_FOUND',
      'CONFLICT',
      'RATE_LIMIT_EXCEEDED',
      'INTERNAL_ERROR'
    ],
  })
  error: string;
  
  @ApiProperty({
    description: 'Human-readable error message',
    example: 'Request validation failed',
  })
  message: string;
  
  @ApiPropertyOptional({
    description: 'Additional error details (validation errors, etc.)',
    oneOf: [
      { type: 'array', items: { $ref: '#/components/schemas/ValidationError' } },
      { type: 'null' }
    ],
  })
  details?: any;
  
  @ApiProperty({
    description: 'Error occurrence timestamp',
    example: '2024-03-20T14:45:30Z',
    format: 'date-time',
  })
  timestamp: string;
  
  @ApiProperty({
    description: 'Unique request identifier for debugging',
    example: 'req_12345',
  })
  requestId: string;
}
```

### Python + FastAPI + Automatic Documentation

**Recommended Pattern:** FastAPI built-in OpenAPI with Pydantic models

```python
# FastAPI with comprehensive documentation
from fastapi import FastAPI, HTTPException, Depends, Query, Path, Body, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional, List, Union
from datetime import datetime
from enum import Enum
import uvicorn

# Initialize FastAPI with comprehensive metadata
app = FastAPI(
    title="Company API",
    description="""
    Comprehensive API documentation generated from FastAPI code.
    
    ## Authentication
    
    This API uses JWT Bearer token authentication. Include the token in the Authorization header:
    ```
    Authorization: Bearer <your_jwt_token>
    ```
    
    ## Error Handling
    
    All errors follow a standardized format with appropriate HTTP status codes.
    Validation errors include detailed field-level information.
    
    ## Rate Limiting
    
    API requests are rate-limited to prevent abuse. Current limits:
    - 100 requests per minute for authenticated users
    - 20 requests per minute for unauthenticated requests
    """,
    version="1.0.0",
    contact={
        "name": "API Support Team",
        "url": "https://company.com/support",
        "email": "api-support@company.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    servers=[
        {"url": "https://api.company.com/v1", "description": "Production server"},
        {"url": "https://staging-api.company.com/v1", "description": "Staging server"},
        {"url": "http://localhost:8000/v1", "description": "Development server"},
    ],
    openapi_tags=[
        {
            "name": "users",
            "description": "User management operations",
            "externalDocs": {
                "description": "User Management Guide",
                "url": "https://docs.company.com/users",
            },
        },
        {
            "name": "authentication",
            "description": "Authentication and authorization endpoints",
        },
    ],
)

# Security scheme
security = HTTPBearer()

# Pydantic models with comprehensive documentation
class UserRole(str, Enum):
    """Available user roles in the system"""
    USER = "user"
    ADMIN = "admin"
    MODERATOR = "moderator"
    GUEST = "guest"

class UserProfile(BaseModel):
    """User profile information"""
    first_name: Optional[str] = Field(
        None,
        title="First Name",
        description="User's first name",
        example="John",
        max_length=50
    )
    last_name: Optional[str] = Field(
        None,
        title="Last Name", 
        description="User's last name",
        example="Doe",
        max_length=50
    )
    avatar: Optional[str] = Field(
        None,
        title="Avatar URL",
        description="URL to user's profile picture",
        example="https://cdn.example.com/avatars/12345.jpg",
        regex=r"^https?://.*\.(jpg|jpeg|png|gif)$"
    )
    bio: Optional[str] = Field(
        None,
        title="Biography",
        description="User's biography",
        example="Software developer passionate about clean code",
        max_length=500
    )
    location: Optional[str] = Field(
        None,
        title="Location",
        description="User's location",
        example="New York, NY",
        max_length=100
    )
    
    class Config:
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "avatar": "https://cdn.example.com/avatars/12345.jpg",
                "bio": "Software developer passionate about clean code",
                "location": "New York, NY"
            }
        }

class CreateUserRequest(BaseModel):
    """Request model for creating a new user"""
    username: str = Field(
        ...,
        title="Username",
        description="Unique username for authentication",
        example="jane.smith",
        min_length=3,
        max_length=30,
        regex=r"^[a-zA-Z0-9_-]{3,30}$"
    )
    email: EmailStr = Field(
        ...,
        title="Email Address",
        description="User's primary email address",
        example="jane.smith@example.com"
    )
    password: str = Field(
        ...,
        title="Password",
        description="Account password - must meet complexity requirements",
        example="SecurePass123!",
        min_length=8,
        max_length=128
    )
    profile: Optional[UserProfile] = Field(
        None,
        title="Profile Information",
        description="User's profile information"
    )
    roles: Optional[List[UserRole]] = Field(
        [UserRole.USER],
        title="User Roles",
        description="User's initial roles",
        example=["user"]
    )
    
    @validator('password')
    def validate_password_complexity(cls, v):
        """Validate password meets complexity requirements"""
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one digit')
        if not any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in v):
            raise ValueError('Password must contain at least one special character')
        return v
    
    class Config:
        schema_extra = {
            "example": {
                "username": "jane.smith",
                "email": "jane.smith@example.com",
                "password": "SecurePass123!",
                "profile": {
                    "first_name": "Jane",
                    "last_name": "Smith",
                    "bio": "Product manager with 5 years experience"
                },
                "roles": ["user"]
            }
        }

class UserDetailResponse(BaseModel):
    """Complete user information with related data"""
    id: int = Field(
        ...,
        title="User ID",
        description="Unique user identifier",
        example=12345,
        ge=1
    )
    username: str = Field(
        ...,
        title="Username",
        description="Unique username for authentication",
        example="john.doe"
    )
    email: EmailStr = Field(
        ...,
        title="Email Address",
        description="User's primary email address",
        example="john.doe@example.com"
    )
    profile: Optional[UserProfile] = Field(
        None,
        title="Profile Information",
        description="User's profile information"
    )
    roles: List[UserRole] = Field(
        ...,
        title="User Roles",
        description="User's assigned roles",
        example=["user"]
    )
    created_at: datetime = Field(
        ...,
        title="Creation Date",
        description="Account creation timestamp",
        example="2024-01-15T10:30:00Z"
    )
    updated_at: Optional[datetime] = Field(
        None,
        title="Update Date", 
        description="Last profile update timestamp",
        example="2024-03-20T14:45:30Z"
    )
    is_active: bool = Field(
        True,
        title="Account Status",
        description="Account status",
        example=True
    )
    
    class Config:
        schema_extra = {
            "examples": {
                "Standard User": {
                    "summary": "Example of standard user response",
                    "value": {
                        "id": 12345,
                        "username": "john.doe",
                        "email": "john.doe@example.com",
                        "profile": {
                            "first_name": "John",
                            "last_name": "Doe"
                        },
                        "roles": ["user"],
                        "created_at": "2024-01-15T10:30:00Z",
                        "is_active": True
                    }
                },
                "Admin User": {
                    "summary": "Example of admin user response",
                    "value": {
                        "id": 67890,
                        "username": "admin",
                        "email": "admin@company.com",
                        "profile": {
                            "first_name": "System",
                            "last_name": "Administrator"
                        },
                        "roles": ["admin", "user"],
                        "created_at": "2023-12-01T08:00:00Z",
                        "is_active": True
                    }
                }
            }
        }

# Error Response Models
class ValidationError(BaseModel):
    """Individual validation error details"""
    field: str = Field(..., description="Field name that failed validation", example="email")
    message: str = Field(..., description="Validation error message", example="Must be a valid email address")
    code: str = Field(..., description="Validation error code", example="INVALID_FORMAT")

class ErrorResponse(BaseModel):
    """Standardized error response format"""
    error: str = Field(
        ...,
        description="Error code for programmatic handling",
        example="VALIDATION_ERROR"
    )
    message: str = Field(
        ...,
        description="Human-readable error message",
        example="Request validation failed"
    )
    details: Optional[Union[List[ValidationError], None]] = Field(
        None,
        description="Additional error details (validation errors, etc.)"
    )
    timestamp: datetime = Field(
        ...,
        description="Error occurrence timestamp",
        example="2024-03-20T14:45:30Z"
    )
    request_id: str = Field(
        ...,
        description="Unique request identifier for debugging",
        example="req_12345"
    )

# API Endpoints with comprehensive documentation
@app.get(
    "/api/users/{user_id}",
    response_model=UserDetailResponse,
    status_code=status.HTTP_200_OK,
    tags=["users"],
    summary="Get user by ID",
    description="""
    Retrieves detailed user information by unique identifier.
    Requires appropriate permissions to access user data.
    
    **Business Logic:**
    - Validates user ID format
    - Checks user existence
    - Applies user visibility rules
    - Returns user with related data
    
    **Permissions Required:**
    - User.Read or Admin.Users.Read
    """,
    responses={
        200: {
            "description": "User retrieved successfully",
            "content": {
                "application/json": {
                    "examples": {
                        "Standard User": {
                            "summary": "Example of standard user response",
                            "value": {
                                "id": 12345,
                                "username": "john.doe",
                                "email": "john.doe@example.com",
                                "profile": {"first_name": "John", "last_name": "Doe"},
                                "roles": ["user"],
                                "created_at": "2024-01-15T10:30:00Z",
                                "is_active": True
                            }
                        }
                    }
                }
            }
        },
        400: {"model": ErrorResponse, "description": "Invalid user ID format"},
        401: {"model": ErrorResponse, "description": "Authentication required"},
        403: {"model": ErrorResponse, "description": "Insufficient permissions"},
        404: {"model": ErrorResponse, "description": "User not found"},
    }
)
async def get_user_by_id(
    user_id: int = Path(
        ...,
        title="User ID",
        description="Unique user identifier",
        example=12345,
        ge=1
    ),
    include: Optional[List[str]] = Query(
        None,
        title="Include Related Data",
        description="Related data to include in response",
        example=["profile", "roles"],
        regex=r"^(profile|preferences|roles)$"
    ),
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Get user by ID endpoint implementation"""
    # Implementation logic here
    pass

@app.post(
    "/api/users",
    response_model=UserDetailResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["users"],
    summary="Create new user",
    description="""
    Creates a new user account with the provided information.
    Email must be unique and password must meet complexity requirements.
    
    **Business Rules:**
    - Username must be unique
    - Email must be unique and valid format
    - Password must meet complexity requirements
    - Email verification will be required
    """,
    responses={
        201: {"description": "User created successfully"},
        400: {"model": ErrorResponse, "description": "Validation errors in request data"},
        409: {"model": ErrorResponse, "description": "User with email already exists"},
    }
)
async def create_user(
    user_data: CreateUserRequest = Body(
        ...,
        title="User Creation Data",
        description="Complete user information for account creation",
        example={
            "username": "jane.smith",
            "email": "jane.smith@example.com",
            "password": "SecurePass123!",
            "profile": {
                "first_name": "Jane",
                "last_name": "Smith",
                "bio": "Product manager with 5 years experience"
            },
            "roles": ["user"]
        }
    )
):
    """Create user endpoint implementation"""
    # Implementation logic here
    pass

# Custom OpenAPI schema modifications
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Company API",
        version="1.0.0",
        description="Comprehensive API documentation generated from FastAPI code",
        routes=app.routes,
    )
    
    # Add custom security schemes
    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "JWT Bearer token authentication"
        }
    }
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )
```

### Generic/Fallback Implementation

For unsupported technologies, provide generic OpenAPI patterns:

```yaml
# Generic OpenAPI 3.0 Template
openapi: 3.0.3
info:
  title: "API Documentation"
  description: "Generated from existing backend code"
  version: "1.0.0"
  contact:
    name: "API Support"
    email: "support@company.com"
    
servers:
  - url: "https://api.company.com/v1"
    description: "Production server"
  - url: "http://localhost:PORT/v1"
    description: "Development server"
    
security:
  - bearerAuth: []
  
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: "JWT Bearer token authentication"
      
  schemas:
    ErrorResponse:
      type: object
      required: [error, message, timestamp, requestId]
      properties:
        error:
          type: string
          description: "Error code for programmatic handling"
        message:
          type: string
          description: "Human-readable error message"
        timestamp:
          type: string
          format: date-time
          description: "Error occurrence timestamp"
        requestId:
          type: string
          description: "Unique request identifier"
          
  responses:
    BadRequest:
      description: "Invalid request parameters or body"
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Unauthorized:
      description: "Authentication required or invalid"
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Forbidden:
      description: "Insufficient permissions"
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    NotFound:
      description: "Resource not found"
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
            
tags:
  - name: "API"
    description: "API operations"
    
paths: {}
  # Populate with discovered endpoints
```

This prompt provides comprehensive guidance for generating high-quality Swagger documentation from existing backend code, ensuring complete API coverage and developer-friendly documentation.