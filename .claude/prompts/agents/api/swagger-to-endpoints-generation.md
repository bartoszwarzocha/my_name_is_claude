# API Endpoint Generation from Swagger Documentation

## Mission
Generate complete, production-ready API endpoints from Swagger/OpenAPI specifications, ensuring consistency between documentation and implementation while maintaining best practices for security, validation, and error handling. **Adapt implementation to the technology stack defined in CLAUDE.md.**

## Pre-Implementation Analysis

### Step 1: Project Technology Detection
**CRITICAL: Always analyze CLAUDE.md first to determine the backend technology stack:**
```bash
# Read project configuration
cat CLAUDE.md | grep -A 5 "primary_language\|Backend"
```

**Technology-specific project analysis:**
```bash
# For .NET/C#
find . -name "*.csproj" -o -name "*.sln" | head -5
ls -la Controllers/ Models/ Services/ 2>/dev/null

# For Java/Spring
find . -name "pom.xml" -o -name "build.gradle" -o -name "*Application.java" | head -5
ls -la src/main/java/ 2>/dev/null

# For Node.js/TypeScript
find . -name "package.json" -o -name "*.js" -o -name "*.ts" | head -5
ls -la routes/ controllers/ src/ 2>/dev/null

# For Python (FastAPI/Django/Flask)
find . -name "requirements.txt" -o -name "*.py" -o -name "pyproject.toml" | head -5
ls -la api/ views/ models/ 2>/dev/null

# For Go
find . -name "go.mod" -o -name "*.go" | head -5
ls -la cmd/ internal/ api/ 2>/dev/null

# For C++ (RESTinio/Crow/etc.)
find . -name "CMakeLists.txt" -o -name "*.cpp" -o -name "*.h" | head -5
ls -la src/ include/ 2>/dev/null
```

### Step 2: Swagger Specification Analysis
**Validate and analyze Swagger specification:**
```bash
# Technology-agnostic validation
if command -v swagger-codegen-cli &> /dev/null; then
    swagger-codegen-cli validate -i swagger.yml
elif command -v swagger-codegen &> /dev/null; then
    swagger-codegen validate -i swagger.yml
elif command -v npx &> /dev/null; then
    npx swagger-codegen validate -i swagger.yml
else
    echo "Using manual validation - check JSON/YAML syntax"
fi

# Analyze Swagger structure
if command -v yq &> /dev/null; then
    yq eval '.paths | keys' swagger.yml | head -20
    yq eval '.components.schemas | keys' swagger.yml | head -10
elif command -v jq &> /dev/null; then
    jq -r '.paths | keys[]' swagger.json | head -20
    jq -r '.components.schemas | keys[]' swagger.json | head -10
else
    echo "Manual analysis required - check paths and schemas sections"
fi
```

**Key Analysis Points:**
- **Endpoint Coverage:** All paths, methods, and parameters
- **Model Definitions:** Complete component schemas
- **Security Schemes:** Authentication and authorization setup
- **Response Definitions:** Status codes and response models
- **Business Rules:** Extract business logic from descriptions

### Step 3: Existing Project Structure Analysis

```bash
# Universal project structure analysis
tree . -I "node_modules|bin|obj|target|dist|build|__pycache__" -L 3
find . -type f -name "*.md" | grep -i readme | head -3
```

## Technology-Specific Implementation Templates

**⚠️ IMPORTANT: Select implementation template based on CLAUDE.md backend technology configuration**

### C# / .NET Core Implementation

**Use when CLAUDE.md specifies: C#, .NET, ASP.NET Core**

```csharp
// Controllers/{EntityName}Controller.cs - Generated from Swagger
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Authorization;
using AutoMapper;

[ApiController]
[Route("api/[controller]")]
[Produces("application/json")]
[ProducesResponseType(typeof(ErrorResponse), 500)]
public class {EntityName}Controller : ControllerBase
{
    private readonly I{EntityName}Service _{entityName}Service;
    private readonly IMapper _mapper;
    private readonly ILogger<{EntityName}Controller> _logger;

    public {EntityName}Controller(
        I{EntityName}Service {entityName}Service, 
        IMapper mapper, 
        ILogger<{EntityName}Controller> logger)
    {
        _{entityName}Service = {entityName}Service;
        _mapper = mapper;
        _logger = logger;
    }

    /// <summary>
    /// Get {entityName} by ID - Generated from Swagger
    /// </summary>
    [HttpGet("{id}")]
    [Authorize(Policy = "{EntityName}Read")]
    [ProducesResponseType(typeof({EntityName}Response), 200)]
    [ProducesResponseType(typeof(ErrorResponse), 400)]
    [ProducesResponseType(typeof(ErrorResponse), 404)]
    public async Task<ActionResult<{EntityName}Response>> Get{EntityName}ById(
        [FromRoute] long id,
        [FromQuery] string[]? include = null)
    {
        try
        {
            // Implementation based on Swagger specification
            var entity = await _{entityName}Service.GetByIdAsync(id, include);
            if (entity == null)
                return NotFound(CreateErrorResponse("NOT_FOUND", $"{EntityName} not found"));

            var response = _mapper.Map<{EntityName}Response>(entity);
            return Ok(response);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error retrieving {EntityName} {Id}", id);
            return StatusCode(500, CreateErrorResponse("INTERNAL_ERROR", "An unexpected error occurred"));
        }
    }

    /// <summary>
    /// Create new {entityName} - Generated from Swagger
    /// </summary>
    [HttpPost]
    [Authorize(Policy = "{EntityName}Write")]
    [ProducesResponseType(typeof({EntityName}Response), 201)]
    [ProducesResponseType(typeof(ErrorResponse), 400)]
    public async Task<ActionResult<{EntityName}Response>> Create{EntityName}([FromBody] Create{EntityName}Request request)
    {
        if (!ModelState.IsValid)
            return BadRequest(CreateValidationErrorResponse());

        try
        {
            var entity = await _{entityName}Service.CreateAsync(request);
            var response = _mapper.Map<{EntityName}Response>(entity);
            
            return CreatedAtAction(nameof(Get{EntityName}ById), new { id = entity.Id }, response);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error creating {EntityName}");
            return StatusCode(500, CreateErrorResponse("INTERNAL_ERROR", "An unexpected error occurred"));
        }
    }

    private ErrorResponse CreateErrorResponse(string error, string message) => new()
    {
        Error = error,
        Message = message,
        Timestamp = DateTime.UtcNow,
        RequestId = HttpContext.TraceIdentifier
    };
}
```

### Java / Spring Boot Implementation

**Use when CLAUDE.md specifies: Java, Spring Boot, Spring Web**

```java
// src/main/java/controllers/{EntityName}Controller.java - Generated from Swagger
@RestController
@RequestMapping("/api/{entityNameLowerCase}")
@Validated
@RequiredArgsConstructor
@Slf4j
public class {EntityName}Controller {

    private final {EntityName}Service {entityName}Service;
    private final {EntityName}Mapper {entityName}Mapper;

    /**
     * Get {entityName} by ID - Generated from Swagger
     */
    @GetMapping("/{id}")
    @PreAuthorize("hasAuthority('{ENTITY_NAME}_READ')")
    public ResponseEntity<{EntityName}Response> get{EntityName}ById(
            @PathVariable @Valid @Positive Long id,
            @RequestParam(required = false) List<String> include) {
        
        try {
            Optional<{EntityName}> entity = {entityName}Service.findById(id, include);
            return entity.map(e -> ResponseEntity.ok({entityName}Mapper.toResponse(e)))
                    .orElse(ResponseEntity.notFound().build());
        } catch (Exception e) {
            log.error("Error retrieving {EntityName} {}", id, e);
            throw new InternalServerException("Error retrieving {entityName}");
        }
    }

    /**
     * Create new {entityName} - Generated from Swagger
     */
    @PostMapping
    @PreAuthorize("hasAuthority('{ENTITY_NAME}_WRITE')")
    public ResponseEntity<{EntityName}Response> create{EntityName}(@Valid @RequestBody Create{EntityName}Request request) {
        try {
            {EntityName} created = {entityName}Service.create(request);
            {EntityName}Response response = {entityName}Mapper.toResponse(created);
            
            return ResponseEntity.status(HttpStatus.CREATED)
                    .location(URI.create("/api/{entityNameLowerCase}/" + created.getId()))
                    .body(response);
        } catch (Exception e) {
            log.error("Error creating {EntityName}", e);
            throw new InternalServerException("Error creating {entityName}");
        }
    }
}
```

### Node.js / TypeScript Implementation

**Use when CLAUDE.md specifies: Node.js, TypeScript, Express**

```typescript
// src/controllers/{entityName}Controller.ts - Generated from Swagger
import { Request, Response, NextFunction } from 'express';
import { validationResult } from 'express-validator';
import { {EntityName}Service } from '../services/{EntityName}Service';
import { auth, requirePermission } from '../middleware/auth';
import { validate{EntityName}Id, validateCreate{EntityName} } from '../validators/{entityName}Validators';

export class {EntityName}Controller {
    constructor(private {entityName}Service: {EntityName}Service) {}

    /**
     * Get {entityName} by ID - Generated from Swagger
     */
    public get{EntityName}ById = [
        auth.authenticate,
        requirePermission('{entityName}:read'),
        validate{EntityName}Id,
        async (req: Request, res: Response, next: NextFunction) => {
            try {
                const errors = validationResult(req);
                if (!errors.isEmpty()) {
                    return res.status(400).json({
                        error: 'VALIDATION_ERROR',
                        message: 'Request validation failed',
                        details: errors.array(),
                        timestamp: new Date().toISOString(),
                        requestId: req.id
                    });
                }

                const id = parseInt(req.params.id);
                const include = req.query.include as string[] | undefined;

                const entity = await this.{entityName}Service.findById(id, include);
                if (!entity) {
                    return res.status(404).json({
                        error: 'NOT_FOUND',
                        message: `{EntityName} not found`,
                        timestamp: new Date().toISOString(),
                        requestId: req.id
                    });
                }

                res.json(entity);
            } catch (error) {
                next(error);
            }
        }
    ];

    /**
     * Create new {entityName} - Generated from Swagger
     */
    public create{EntityName} = [
        auth.authenticate,
        requirePermission('{entityName}:write'),
        validateCreate{EntityName},
        async (req: Request, res: Response, next: NextFunction) => {
            try {
                const errors = validationResult(req);
                if (!errors.isEmpty()) {
                    return res.status(400).json({
                        error: 'VALIDATION_ERROR',
                        message: 'Request validation failed',
                        details: errors.array(),
                        timestamp: new Date().toISOString(),
                        requestId: req.id
                    });
                }

                const created = await this.{entityName}Service.create(req.body);
                
                res.status(201)
                   .location(`/api/{entityNameLowerCase}/${created.id}`)
                   .json(created);
            } catch (error) {
                next(error);
            }
        }
    ];
}
```

### Python / FastAPI Implementation

**Use when CLAUDE.md specifies: Python, FastAPI**

```python
# app/controllers/{entity_name}_controller.py - Generated from Swagger
from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from ..services.{entity_name}_service import {EntityName}Service
from ..schemas.{entity_name}_schemas import {EntityName}Response, Create{EntityName}Request
from ..dependencies.auth import get_current_user, require_permission
from ..dependencies.common import get_{entity_name}_service
from ..models.user import User
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/{entity_name_plural}", tags=["{entity_name}"])

@router.get(
    "/{{{entity_name}_id}}",
    response_model={EntityName}Response,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(require_permission("{entity_name}:read"))]
)
async def get_{entity_name}_by_id(
    {entity_name}_id: int,
    include: Optional[List[str]] = Query(None),
    current_user: User = Depends(get_current_user),
    {entity_name}_service: {EntityName}Service = Depends(get_{entity_name}_service)
):
    """Get {entityName} by ID - Generated from Swagger"""
    try:
        entity = await {entity_name}_service.get_by_id({entity_name}_id, include)
        if not entity:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{EntityName} not found"
            )
        return entity
    except Exception as e:
        logger.error(f"Error retrieving {EntityName} {{entity_name}_id}: {{e}}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.post(
    "/",
    response_model={EntityName}Response,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission("{entity_name}:write"))]
)
async def create_{entity_name}(
    request: Create{EntityName}Request,
    current_user: User = Depends(get_current_user),
    {entity_name}_service: {EntityName}Service = Depends(get_{entity_name}_service)
):
    """Create new {entityName} - Generated from Swagger"""
    try:
        created = await {entity_name}_service.create(request)
        return created
    except Exception as e:
        logger.error(f"Error creating {EntityName}: {{e}}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
```

### Go Implementation

**Use when CLAUDE.md specifies: Go, Golang**

```go
// internal/handlers/{entity_name}_handler.go - Generated from Swagger
package handlers

import (
    "encoding/json"
    "net/http"
    "strconv"
    "strings"
    
    "github.com/gorilla/mux"
    "github.com/your-project/internal/services"
    "github.com/your-project/internal/models"
    "github.com/your-project/internal/middleware"
)

type {EntityName}Handler struct {
    service services.{EntityName}Service
    logger  Logger
}

func New{EntityName}Handler(service services.{EntityName}Service, logger Logger) *{EntityName}Handler {
    return &{EntityName}Handler{
        service: service,
        logger:  logger,
    }
}

// Get{EntityName}ByID handles GET /api/{entity_name_plural}/{id} - Generated from Swagger
func (h *{EntityName}Handler) Get{EntityName}ByID(w http.ResponseWriter, r *http.Request) {
    vars := mux.Vars(r)
    idStr := vars["id"]
    
    id, err := strconv.ParseInt(idStr, 10, 64)
    if err != nil {
        http.Error(w, "Invalid ID format", http.StatusBadRequest)
        return
    }
    
    // Parse include query parameter
    includeStr := r.URL.Query().Get("include")
    var include []string
    if includeStr != "" {
        include = strings.Split(includeStr, ",")
    }
    
    entity, err := h.service.GetByID(r.Context(), id, include)
    if err != nil {
        h.logger.Error("Error retrieving {EntityName}", "id", id, "error", err)
        http.Error(w, "Internal server error", http.StatusInternalServerError)
        return
    }
    
    if entity == nil {
        http.Error(w, "{EntityName} not found", http.StatusNotFound)
        return
    }
    
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(entity)
}

// Create{EntityName} handles POST /api/{entity_name_plural} - Generated from Swagger
func (h *{EntityName}Handler) Create{EntityName}(w http.ResponseWriter, r *http.Request) {
    var req models.Create{EntityName}Request
    
    if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
        http.Error(w, "Invalid request body", http.StatusBadRequest)
        return
    }
    
    if err := req.Validate(); err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }
    
    created, err := h.service.Create(r.Context(), &req)
    if err != nil {
        h.logger.Error("Error creating {EntityName}", "error", err)
        http.Error(w, "Internal server error", http.StatusInternalServerError)
        return
    }
    
    w.Header().Set("Content-Type", "application/json")
    w.Header().Set("Location", fmt.Sprintf("/api/{entity_name_plural}/%d", created.ID))
    w.WriteStatus(http.StatusCreated)
    json.NewEncoder(w).Encode(created)
}

// RegisterRoutes registers all {EntityName} routes
func (h *{EntityName}Handler) RegisterRoutes(r *mux.Router) {
    // Apply authentication and authorization middleware
    {entity_name}Router := r.PathPrefix("/api/{entity_name_plural}").Subrouter()
    {entity_name}Router.Use(middleware.Authenticate)
    
    {entity_name}Router.HandleFunc("/{id}", 
        middleware.RequirePermission("{entity_name}:read")(h.Get{EntityName}ByID)).
        Methods("GET")
        
    {entity_name}Router.HandleFunc("", 
        middleware.RequirePermission("{entity_name}:write")(h.Create{EntityName})).
        Methods("POST")
}
```

### C++ Implementation

**Use when CLAUDE.md specifies: C++, RESTinio, Crow**

```cpp
// src/controllers/{entity_name}_controller.hpp - Generated from Swagger
#pragma once

#include <restinio/all.hpp>
#include <json/json.h>
#include "../services/{entity_name}_service.hpp"
#include "../middleware/auth_middleware.hpp"

namespace api::controllers {

class {EntityName}Controller {
private:
    std::shared_ptr<services::{EntityName}Service> service_;
    std::shared_ptr<spdlog::logger> logger_;

public:
    {EntityName}Controller(
        std::shared_ptr<services::{EntityName}Service> service,
        std::shared_ptr<spdlog::logger> logger)
        : service_(service), logger_(logger) {}

    // GET /api/{entity_name_plural}/{id} - Generated from Swagger
    restinio::request_handling_status_t get_{entity_name}_by_id(
        const restinio::request_handle_t& req) {
        
        try {
            auto id_str = req->header().path_params()["id"];
            int64_t id = std::stoll(id_str);
            
            // Parse include query parameter
            std::vector<std::string> include;
            auto include_param = req->header().get_field("include");
            if (!include_param.empty()) {
                // Parse comma-separated values
                std::stringstream ss(include_param);
                std::string item;
                while (std::getline(ss, item, ',')) {
                    include.push_back(item);
                }
            }
            
            auto entity = service_->get_by_id(id, include);
            if (!entity) {
                return req->create_response(restinio::status_not_found())
                    .set_body(R"({"error": "NOT_FOUND", "message": "{EntityName} not found"})")
                    .done();
            }
            
            Json::Value response;
            entity->to_json(response);
            
            Json::StreamWriterBuilder builder;
            std::string json_string = Json::writeString(builder, response);
            
            return req->create_response(restinio::status_ok())
                .set_body(json_string)
                .set_header(restinio::http_field::content_type, "application/json")
                .done();
                
        } catch (const std::exception& e) {
            logger_->error("Error retrieving {EntityName}: {}", e.what());
            return req->create_response(restinio::status_internal_server_error())
                .set_body(R"({"error": "INTERNAL_ERROR", "message": "Internal server error"})")
                .done();
        }
    }

    // POST /api/{entity_name_plural} - Generated from Swagger
    restinio::request_handling_status_t create_{entity_name}(
        const restinio::request_handle_t& req) {
        
        try {
            Json::Value request_json;
            Json::CharReaderBuilder builder;
            std::string errors;
            
            std::istringstream request_body(req->body());
            if (!Json::parseFromStream(builder, request_body, &request_json, &errors)) {
                return req->create_response(restinio::status_bad_request())
                    .set_body(R"({"error": "VALIDATION_ERROR", "message": "Invalid JSON"})")
                    .done();
            }
            
            models::Create{EntityName}Request create_request;
            create_request.from_json(request_json);
            
            if (!create_request.validate()) {
                return req->create_response(restinio::status_bad_request())
                    .set_body(R"({"error": "VALIDATION_ERROR", "message": "Request validation failed"})")
                    .done();
            }
            
            auto created = service_->create(create_request);
            
            Json::Value response;
            created->to_json(response);
            
            Json::StreamWriterBuilder json_builder;
            std::string json_string = Json::writeString(json_builder, response);
            
            return req->create_response(restinio::status_created())
                .set_body(json_string)
                .set_header(restinio::http_field::content_type, "application/json")
                .set_header(restinio::http_field::location, 
                    fmt::format("/api/{entity_name_plural}/{}", created->get_id()))
                .done();
                
        } catch (const std::exception& e) {
            logger_->error("Error creating {EntityName}: {}", e.what());
            return req->create_response(restinio::status_internal_server_error())
                .set_body(R"({"error": "INTERNAL_ERROR", "message": "Internal server error"})")
                .done();
        }
    }
};

} // namespace api::controllers
```

## Implementation Process

### Phase 1: Technology-Specific Setup

1. **Read CLAUDE.md** to determine the exact backend technology
2. **Analyze existing project structure** for patterns and conventions
3. **Select appropriate implementation template** from the above options
4. **Adapt template** to match existing codebase conventions


### Phase 2: Swagger-to-Code Mapping

1. **Parse Swagger paths** → Generate route definitions
2. **Parse Swagger schemas** → Generate model/DTO classes
3. **Parse Swagger responses** → Generate response handling
4. **Parse Swagger security** → Generate authentication/authorization


### Phase 3: Code Generation

1. **Generate controllers/handlers** using technology-specific patterns
2. **Generate request/response models** with validation
3. **Generate service interfaces** for business logic
4. **Generate error handling** consistent with existing patterns


### Phase 4: Integration and Testing

1. **Integrate with existing middleware** (auth, logging, validation)
2. **Update dependency injection** configuration
3. **Generate integration tests** for new endpoints
4. **Update API documentation** with implementation details

## Quality Gates


### ✅ Technology Compliance

- [ ] Implementation matches CLAUDE.md backend technology
- [ ] Code follows existing project patterns and conventions
- [ ] Integration with existing middleware and services
- [ ] Proper dependency injection configuration


### ✅ Swagger Accuracy

- [ ] All endpoints from Swagger implemented
- [ ] Request/response models match specification exactly
- [ ] Status codes match documentation
- [ ] Authentication requirements implemented correctly


### ✅ Production Readiness

- [ ] Comprehensive error handling
- [ ] Input validation and sanitization
- [ ] Proper logging and monitoring
- [ ] Security best practices applied
- [ ] Performance considerations addressed

**This prompt ensures API endpoints are generated using the exact technology stack specified in CLAUDE.md, maintaining consistency with existing project architecture.**
