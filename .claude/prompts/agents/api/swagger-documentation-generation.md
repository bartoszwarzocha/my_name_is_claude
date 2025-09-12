# Swagger Documentation Generation from Existing Backend Code

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

This prompt provides comprehensive guidance for generating high-quality Swagger documentation from existing backend code, ensuring complete API coverage and developer-friendly documentation.