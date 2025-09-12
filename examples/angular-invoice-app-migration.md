# Example 2: Web Invoice Application Migration - Angular/.NET API

**Execution Date:** 2025-09-12  
**Commit:** 73a1009 (adaptive prompts)  
**Framework Version:** Claude Code Multi-Agent Framework v1.0 - Technology Adaptive

## Brief Application Description

Modernization of existing web invoice application with outdated API documentation. The project involves analysis of existing system, Swagger documentation update, and business functionality optimization based on reverse engineering and code analysis.

## Key Technology Assumptions

- **Frontend:** Angular 17+ (existing, requires updates)
- **Backend API:** .NET Core Web API (existing C# code)
- **Database:** SQL Server/PostgreSQL (analysis of existing connections)
- **Documentation:** Swagger/OpenAPI 3.0 (regeneration from code)
- **Challenge:** Outdated Swagger documentation doesn't reflect actual endpoints
- **Approach:** Reverse engineering + code analysis + documentation rebuild

## Sample CLAUDE.md Content

```markdown
# CLAUDE.md – Invoice Application Migration Project

## 0. Project Metadata
- **project_name**: "invoice-app-migration"
- **project_description**: "Migration and modernization of existing Angular/NET invoice application with API documentation rebuild"
- **primary_language**: typescript
- **business_domain**: fintech
- **project_scale**: sme
- **development_stage**: production

## 1. Project Description
Modernization of existing invoice web application with focus on API documentation accuracy, frontend optimization, and business process improvement. Legacy system requires reverse engineering and comprehensive documentation rebuild.

## 2. Domains and Goals
- Business domains: financial services, invoice management, business accounting
- Main project goals: API documentation accuracy, system modernization, business process optimization

## 3. Technologies
- **Frontend – technologies and tools:** Angular 17+, TypeScript, RxJS, Angular Material
- **Backend – technologies and tools:** .NET Core Web API, C#, Entity Framework Core
- **Database:** SQL Server, Entity Framework migrations
- **Other:** Swagger/OpenAPI, automated API documentation, reverse engineering tools

## 4. Agents and Roles
[Standard agent configuration with focus on API analysis and documentation rebuild]

## 5. Integrations and Dependencies
- Existing API endpoints: .NET Core Web API
- Database: SQL Server with existing schema
- Frontend framework: Angular with existing component structure
- Documentation: Swagger UI regeneration

## 6. Non-functional Requirements
- Performance: API response optimization, frontend loading improvements
- Security: Authentication/authorization validation, data protection compliance
- Scalability: Multi-tenant support, concurrent user handling
- Availability: Zero-downtime migration, rollback capabilities

## 7. Special Notes
- Existing codebase analysis required
- API endpoint discovery through code inspection
- Backward compatibility maintenance
- Business process validation essential
```

## Project Initialization Method

### 1. Analysis Environment Preparation

```bash
# Navigate to framework directory
cd /mnt/e/AI/my_name_is_claude

# Create project analysis directory
mkdir invoice-app-migration
cd invoice-app-migration

# Copy framework
cp -r ../.claude .
cp ../CLAUDE.md .
cp ../DATABASE_CONNECTIONS.md .

# Prepare analysis structure
mkdir -p analysis/{api,frontend,database,documentation}
mkdir -p existing-code/{backend,frontend}

# Customize CLAUDE.md for migration project
# [Edit CLAUDE.md file according to above content]
```

### 2. Existing Code Analysis

```bash
# Simulation of copying existing code for analysis
# In real project:
# cp -r /path/to/existing/backend/* ./existing-code/backend/
# cp -r /path/to/existing/frontend/* ./existing-code/frontend/

# Initialize Claude Code with existing project context
claude-code
```

## MCP Initialization Method

### Serena MCP (Existing Code Analysis)

```bash
# Serena configuration for existing code analysis
../mcp_tools.sh

# Choose option 2: Serena MCP
# Special configuration for code analysis:
# - Port: 3002
# - Directory: ./existing-code (for legacy code analysis)
# - Auto-indexing: enabled
# - Development mode: enabled

# Additional configuration for multi-directory analysis:
# Directory 1: ./existing-code/backend (.NET API)
# Directory 2: ./existing-code/frontend (Angular app)
```

### Context7 MCP (Documentation and Regeneration)

```bash
# Context7 MCP for documentation rebuild
# Option 1: Context7 MCP
# Special configuration for documentation generation:
# - Focus: API documentation regeneration
# - Template: OpenAPI 3.0 specification
# - Output: Swagger documentation
```

## Detailed Step-by-Step Instructions

### Phase 1: Existing System Analysis (2-3 hours)

#### Step 1.1: API Endpoints Analysis through Reverse Engineering

**Prompt:** `.claude/prompts/agents/api/rest-api-design-and-implementation.md`

**Prompt Context:**
```
I have an existing .NET Core Web API for invoicing.
Old Swagger documentation is outdated and points to wrong endpoints.
I need to analyze source code controllers and regenerate accurate API documentation.

Copy controllers from existing-code/backend/Controllers/ and analyze actual endpoints.
```

**Expected Results:**
- Framework automatically detects .NET Core from CLAUDE.md
- You'll receive Controllers analysis with all actual endpoints
- List of working vs. documented endpoints
- Correction and modernization proposals for API
- New OpenAPI 3.0 documentation structure

**How to React to Options:**
- **Deprecated endpoints:** Plan migration path
- **Missing documentation:** Prioritize critical business endpoints
- **API versioning:** Implement if multiple versions detected

#### Step 1.2: Swagger Documentation Regeneration

**Prompt:** `.claude/prompts/agents/api/swagger-documentation-generation.md`

**Expected Results:**
- Automatic OpenAPI spec generation from .NET code
- Complete documentation of all working endpoints
- Request/Response schemas with examples
- Authentication/Authorization schemas
- API testing capabilities in Swagger UI

#### Step 1.3: Angular Frontend Analysis

**Prompt:** `.claude/prompts/agents/frontend/angular-component-development.md`

**Prompt Context:**
```
I'm analyzing existing Angular invoice application.
I need to identify:
- Which components call which API endpoints
- What services are used for API communication
- Which frontend parts are inactive/unused
- Status of TypeScript definitions for API responses
```

**Expected Results:**
- Mapping Angular services → API endpoints
- Identification of non-existent API calls (404 errors)
- Angular modernization proposals to version 17+
- TypeScript interfaces alignment with actual API

### Phase 2: Documentation and Specification (2-3 hours)

#### Step 2.1: Business Process Reconstruction

**Prompt:** `.claude/prompts/agents/business/current-state-process-analysis.md`

**Prompt Context:**
```
Based on backend and frontend code analysis, reconstruct actual business processes:
- How does invoice creation flow look?
- What are required fields and validations?
- Which processes are automated?
- Where do UX bottlenecks occur?
```

**Expected Results:**
- Complete business process map of invoice workflow
- Identification of gaps in functionality vs. code implementation
- User experience optimization proposals
- Requirements for missing functionality

#### Step 2.2: Security Analysis

**Prompt:** `.claude/prompts/agents/security/secure-code-review-and-sast.md`

**Expected Results:**
- Framework detects .NET Core and proposes security analysis
- Code review for authentication/authorization
- Identification of potential security vulnerabilities
- Compliance check for financial application standards

#### Step 2.3: Database Audit

**Prompt:** `.claude/prompts/agents/data/database-design-and-etl-implementation.md`

**Expected Results:**
- Analysis of existing database schema
- Entity Framework model validation
- Performance bottlenecks identification
- Data migration strategies proposal

### Phase 3: Modernization and Optimization (4-6 hours)

#### Step 3.1: API Modernization

**Prompt:** `.claude/prompts/agents/api/rest-api-design-and-implementation.md` (second time, with focus on improvements)

**Prompt Context:**
```
Based on analysis, modernize API:
- Add missing endpoints identified in frontend analysis
- Implement proper error handling and status codes
- Add API versioning strategy
- Optimize performance for bulk operations
```

**Expected Results:**
- Updated .NET Controllers with best practices
- Proper HTTP status codes and error handling
- API versioning implementation
- Performance optimizations (caching, pagination)
- Updated OpenAPI documentation

#### Step 3.2: Frontend Optimization

**Prompt:** `.claude/prompts/agents/frontend/frontend-backend-integration.md`

**Expected Results:**
- Angular services updated for new API structure
- Proper error handling in frontend
- TypeScript interfaces generated from OpenAPI spec
- RxJS patterns for async operations
- Loading states and user feedback

#### Step 3.3: Performance Optimization

**Prompt:** `.claude/prompts/agents/frontend/application-performance-optimization.md`

**Expected Results:**
- Angular performance optimizations (OnPush, lazy loading)
- API response optimization strategies
- Database query performance improvements
- Frontend bundle size optimization

### Phase 4: Testing and Validation (3-4 hours)

#### Step 4.1: API Testing

**Prompt:** `.claude/prompts/agents/qa/test-automation-and-quality-assurance.md`

**Expected Results:**
- Comprehensive API testing strategy
- Integration tests for critical invoice workflows
- Performance testing for concurrent users
- Regression testing for existing functionality

#### Step 4.2: Frontend Testing

**Prompt:** `.claude/prompts/agents/frontend/frontend-testing-and-quality-assurance.md`

**Expected Results:**
- Angular unit tests for updated components
- E2E tests for complete invoice workflows
- User acceptance testing scenarios
- Cross-browser compatibility validation

### Phase 5: Deployment and Migration (2-3 hours)

#### Step 5.1: Migration Strategy

**Prompt:** `.claude/prompts/agents/deployment/ci-cd-pipeline-and-infrastructure-setup.md`

**Expected Results:**
- Zero-downtime deployment strategy
- Database migration plan
- Rollback procedures
- Monitoring and alerting setup

## Using Orchestration and Hooks

### Orchestration for Legacy Code Analysis

```bash
# Special scenario for legacy migration
./.claude/hooks/orchestration-trigger.sh "$(pwd)" "migration"

# Or automatic detection:
./.claude/hooks/orchestration-trigger.sh

# Advanced conditional workflow for complex migration
./.claude/hooks/orchestration/conditional-workflow-engine.sh "$(pwd)" "fintech" "migration"
```

**Expected Orchestration Behavior:**
1. **Legacy Analysis Phase:** business-analyst → api-engineer (code analysis) → frontend-engineer
2. **Documentation Rebuild:** api-engineer (swagger generation) → reviewer (validation)
3. **Modernization Phase:** api-engineer → frontend-engineer → qa-engineer (parallel)
4. **Deployment Preparation:** deployment-engineer → security-engineer (final review)

### Using Hooks for Migration

#### Code Analysis Monitoring

```bash
# Legacy code analysis monitoring
./.claude/hooks/agent-performance-monitor.sh "start" "api-engineer"
./.claude/hooks/agent-performance-monitor.sh "start" "frontend-engineer"

# Reverse engineering progress tracking
./.claude/hooks/agent-performance-monitor.sh "analyze" "migration"
```

#### Dependency Validation

```bash
# Frontend and API changes dependency validation
./.claude/hooks/cross-agent-dependency-tracker.sh "validate" "frontend-backend"

# Compatibility check before deployment
./.claude/hooks/cross-agent-dependency-tracker.sh "check" "migration-readiness"
```

#### Quality Gates

```bash
# Financial applications compliance
./.claude/hooks/compliance-automation.sh "fintech" "api-engineer"

# Financial data security validation
./.claude/hooks/compliance-automation.sh "security" "financial-data"
```

## Using MCP Tools for Legacy Analysis

### Serena MCP - Advanced Code Navigation

```bash
# Deep code analysis for controller discovery
# In Claude Code, use Serena commands:

# Controller analysis:
serena search "public class.*Controller" --type cs

# API endpoints discovery:
serena search "\[Http(Get|Post|Put|Delete)\]" --type cs

# Database model analysis:
serena search "public class.*: IEntity" --type cs

# Angular service analysis:
serena search "@Injectable" --type ts --path frontend
```

### Context7 MCP - Documentation Generation

```bash
# Automatic documentation generation:
# Use Context7 for:

# 1. API Documentation rebuild
# 2. Frontend component documentation
# 3. Database schema documentation
# 4. Migration guide generation
```

## Real Use Case - Problem-Solving Approach

### Challenge 1: Inconsistent API Documentation

**Problem:** Swagger documentation points to /api/v1/invoices/create, but actual endpoint is /api/invoices/generate

**Solution Process:**
1. **Code Analysis:** Serena search for all API routes
2. **Documentation Rebuild:** Swagger generation from actual code
3. **Frontend Alignment:** Update Angular services for correct endpoints
4. **Testing:** Comprehensive API testing for all discovered endpoints

### Challenge 2: Missing Business Logic

**Problem:** Frontend has components for "recurring invoices" but API has no support

**Solution Process:**
1. **Business Analysis:** Determine if feature was planned but never implemented
2. **API Extension:** Add missing endpoints in .NET API
3. **Database Migration:** Add required tables/columns
4. **Frontend Integration:** Connect existing UI to new API

### Challenge 3: Performance Issues

**Problem:** Invoice listing page loading >5 seconds for 1000+ invoices

**Solution Process:**
1. **API Analysis:** Database query optimization
2. **Pagination Implementation:** Server-side paging
3. **Frontend Optimization:** Virtual scrolling in Angular
4. **Caching Strategy:** Redis/memory caching for frequent queries

## Expected Final Results

### Technical Deliverables

- ✅ **Accurate API Documentation** - OpenAPI 3.0 spec reflecting actual endpoints
- ✅ **Modernized Angular Frontend** - Updated to latest patterns and performance optimizations
- ✅ **Optimized .NET API** - Performance improvements and proper error handling
- ✅ **Comprehensive Testing** - API and E2E tests for critical workflows
- ✅ **Migration Documentation** - Complete guide for deployment and rollback

### Business Deliverables

- ✅ **Restored System Reliability** - Eliminated 404 errors and API mismatches
- ✅ **Improved User Experience** - Faster loading times and better error messaging
- ✅ **Complete Business Process Documentation** - Clear understanding of all invoice workflows
- ✅ **Future-Proof Architecture** - Modern patterns enabling easier future enhancements

### Success Metrics

- **API Accuracy:** 100% documentation-code alignment (vs. previous ~60%)
- **Performance:** <2s page loading (vs. previous 5+s)
- **Error Reduction:** 95% reduction in frontend API errors
- **Development Velocity:** 50% faster future feature development
- **Maintenance Cost:** 60% reduction in debugging time for API issues

### Migration Timeline

#### Week 1: Analysis & Documentation
1. **Day 1-2:** Legacy code analysis and API discovery
2. **Day 3-4:** Documentation rebuild and business process mapping
3. **Day 5:** Security audit and performance baseline

#### Week 2: Modernization & Testing
1. **Day 1-3:** API improvements and frontend optimization
2. **Day 4-5:** Comprehensive testing and validation

#### Week 3: Deployment & Validation
1. **Day 1-2:** Staging deployment and user acceptance testing
2. **Day 3:** Production migration
3. **Day 4-5:** Post-migration monitoring and optimization

---

**Status:** Ready for legacy system analysis and modernization - Complete methodology for handling problematic existing codebases using Claude Code Multi-Agent Framework with reverse engineering capabilities.

This example demonstrates practical approach to real-world migration challenges, including code analysis, documentation rebuild, and systematic modernization process using comprehensive multi-agent coordination.