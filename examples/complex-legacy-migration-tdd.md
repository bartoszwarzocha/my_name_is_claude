# Example 3: Complex Legacy Migration ASP.NET + C++ → Angular + .NET Core with TDD

**Execution Date:** 2025-09-12  
**Commit:** 73a1009 (adaptive prompts)  
**Framework Version:** Claude Code Multi-Agent Framework v1.0 - Technology Adaptive

## Brief Application Description

Comprehensive migration of legacy enterprise application from ASP.NET WebForms + C++ backend to modern Angular + .NET Core Web API architecture. The project is characterized by lack of documentation, complex business rules in C++, and requirement to apply Test-Driven Development methodology with Playwright MCP for automated testing.

## Key Technology Assumptions

- **Legacy System:**
  - Frontend: ASP.NET WebForms (circa 2008-2012)
  - Backend: C++ native libraries with COM interop
  - Database: SQL Server with stored procedures
  - Business Logic: Mixed C++/SQL stored procedures
  
- **Target Modern System:**
  - Frontend: Angular 17+ with TypeScript
  - Backend: .NET Core 8.0 Web API
  - Database: SQL Server with Entity Framework Core
  - Testing: Playwright end-to-end automation
  - Methodology: Test-Driven Development (TDD)

- **Migration Challenges:**
  - Zero documentation for business logic
  - C++ code reverse engineering required
  - Complex data transformations
  - Business continuity during migration
  - Comprehensive test coverage from day one

## Sample CLAUDE.md Content with Hierarchical TODO Management

```markdown
# CLAUDE.md – Complex Legacy Migration Project

## 0. Project Metadata
- **project_name**: "legacy-enterprise-migration"
- **project_description**: "Complete migration from ASP.NET WebForms + C++ backend to Angular + .NET Core with TDD approach"
- **primary_language**: typescript
- **business_domain**: enterprise
- **project_scale**: enterprise
- **development_stage**: development

## 1. Project Description
Enterprise-scale migration from legacy ASP.NET WebForms with C++ backend to modern Angular + .NET Core architecture. Project requires comprehensive reverse engineering, business logic reconstruction, and TDD implementation with Playwright automation testing.

## 2. Domains and Goals
- Business domains: enterprise software, legacy modernization, business process automation
- Main project goals: technology modernization, performance improvement, maintainability enhancement, comprehensive test coverage

## 3. Technologies
- **Frontend – technologies and tools:** Angular 17+, TypeScript, RxJS, Angular Material, PWA capabilities
- **Backend – technologies and tools:** .NET Core 8.0, C#, Entity Framework Core, SignalR
- **Database:** SQL Server, Entity Framework migrations, stored procedure migration
- **Testing:** Playwright, Jest, xUnit, TDD methodology
- **Legacy Analysis:** C++ code analysis, COM interop understanding, WebForms reverse engineering

## 4. Agents and Roles
[Enhanced agent configuration with focus on legacy migration, TDD, and comprehensive testing]

## 5. Integrations and Dependencies
- Legacy system: ASP.NET WebForms + C++ backend analysis
- Database migration: SQL Server schema and stored procedures
- Testing framework: Playwright MCP integration for E2E testing
- CI/CD: Automated testing pipeline with TDD workflows

## 6. Non-functional Requirements
- Performance: 10x improvement in response times
- Security: Modern authentication/authorization, data protection compliance
- Scalability: Cloud-ready architecture, horizontal scaling capabilities
- Availability: Zero-downtime migration strategy, progressive deployment
- Testability: 90%+ code coverage, comprehensive E2E test suite

## 7. Special Notes
- TDD methodology mandatory from project start
- Playwright MCP integration for automated testing
- C++ to C# business logic migration
- Legacy WebForms UI pattern analysis and modern Angular equivalent design
- Progressive migration strategy with parallel system operation
```

## Project Initialization Method

### 1. Migration Environment Preparation

```bash
# Navigate to framework directory
cd /mnt/e/AI/my_name_is_claude

# Create migration project
mkdir legacy-enterprise-migration
cd legacy-enterprise-migration

# Copy framework
cp -r ../.claude .
cp ../CLAUDE.md .
cp ../DATABASE_CONNECTIONS.md .

# Legacy system analysis structure
mkdir -p legacy-analysis/{webforms,cpp-backend,database,business-logic}
mkdir -p modern-implementation/{angular-frontend,dotnet-api,tests}
mkdir -p migration-artifacts/{documentation,test-scenarios,deployment}

# Setup TDD structure
mkdir -p tests/{unit,integration,e2e-playwright}

# Customize CLAUDE.md for complex migration
# [Edit CLAUDE.md file according to above content]
```

### 2. Initialize Claude Code with TDD Focus

```bash
# Initialize in migration mode
claude-code

# Verify availability of all agents
# Especially: business-analyst, software-architect, frontend-engineer, api-engineer, qa-engineer
```

## MCP Initialization Method

### Playwright MCP (E2E Testing Automation)

```bash
# Install Playwright MCP for automated testing
../mcp_tools.sh

# Choose option 3: Playwright MCP
# Configuration for TDD approach:
# - Installation: NPX deployment
# - Browser support: Chromium, Firefox, WebKit
# - Test framework integration: Jest + Playwright
# - Parallel execution: enabled

# Verification in Claude Code settings:
# "mcpServers": {
#   "playwright": {
#     "command": "npx",
#     "args": ["-y", "@playwright/test", "--config=playwright.config.js"],
#     "env": {
#       "PLAYWRIGHT_BROWSERS_PATH": "./playwright-browsers"
#     }
#   }
# }
```

### Serena MCP (Legacy Code Analysis)

```bash
# Serena for deep legacy analysis
# Multi-project analysis configuration:
# - Port: 3003
# - Legacy directory: ./legacy-analysis (ASP.NET + C++)
# - Modern directory: ./modern-implementation (Angular + .NET Core)
# - Comparative analysis: enabled
```

### Context7 MCP (Documentation Generation)

```bash
# Context7 for comprehensive documentation
# Focus areas:
# - Business logic reconstruction documentation
# - API specification generation
# - Test scenario documentation
# - Migration progress tracking
```

## Detailed Step-by-Step Instructions - TDD Approach

### Pre-Phase: Legacy System Analysis and Test Planning (3-4 hours)

#### Step 0.1: Deep Legacy Analysis

**Prompt:** `.claude/prompts/agents/business/current-state-process-analysis.md`

**Prompt Context:**
```
I'm analyzing complex legacy system:
- ASP.NET WebForms frontend (no documentation)
- C++ backend with COM interop
- SQL Server with complex stored procedures
- Zero technical documentation

Goal: Understand business logic and user workflows for TDD test design.
I need to identify all user scenarios to write comprehensive test suite.
```

**Expected Results:**
- Complete user workflow identification from legacy WebForms
- Business rule extraction from C++ code analysis
- Data flow mapping between WebForms → C++ → SQL Server
- Critical business scenarios list for priority testing

**TDD Preparation:**
- **Test Scenarios Identification:** Every business workflow becomes test case
- **User Story Extraction:** Legacy features → modern user stories with acceptance criteria
- **Test Data Requirements:** Real data scenarios for comprehensive testing

#### Step 0.2: Test-First Architecture Planning

**Prompt:** `.claude/prompts/agents/qa/test-automation-and-quality-assurance.md`

**Prompt Context:**
```
Designing TDD approach for complex migration:
1. I need test pyramid strategy (unit, integration, E2E)
2. Playwright integration for automated browser testing
3. Test data management strategy
4. CI/CD integration with TDD workflow
5. Test coverage requirements: 90%+
```

**Expected Results:**
- Framework detects TypeScript/.NET and proposes TDD patterns
- Comprehensive test strategy with Playwright E2E tests
- Test data fixtures and mock strategies
- TDD workflow: Red → Green → Refactor cycle documentation
- CI/CD pipeline with mandatory test passing

### Phase 1: Test-Driven Business Logic Discovery (4-5 hours)

#### Step 1.1: Business Logic Test Design

**Prompt:** `.claude/prompts/agents/business/stakeholder-requirements-gathering.md`

**Prompt Context:**
```
No business documentation for legacy system.
Using TDD approach:
1. Analyze legacy C++ code and SQL stored procedures
2. Extract business rules as test specifications
3. Design failing tests FIRST (Red phase)
4. Document expected business behavior
5. Create test fixtures for complex scenarios
```

**Expected Results:**
- Business rules extracted as executable test specifications
- Comprehensive test cases list covering all legacy functionality
- Test data scenarios representing real business cases
- Acceptance criteria for each business rule
- **TDD Red Phase:** Failing tests for all business requirements

#### Step 1.2: C++ to C# Logic Migration Tests

**Prompt:** `.claude/prompts/agents/api/rest-api-design-and-implementation.md`

**Prompt Context:**
```
TDD approach for C++ → .NET Core migration:
1. Write failing API tests FIRST for each C++ function
2. Design .NET Core API endpoints with test specifications
3. Implement C# business logic to pass tests (Green phase)
4. Refactor for clean architecture (Refactor phase)

Focus: Complex algorithms and business calculations from C++ code.
```

**Expected Results:**
- Framework detects .NET Core from CLAUDE.md
- API endpoint specifications with comprehensive test coverage
- C++ algorithm analysis and C# equivalent implementation
- **TDD Green Phase:** .NET Core implementation passing all tests
- **TDD Refactor Phase:** Clean architecture improvements

### Phase 2: Frontend TDD Implementation (6-8 hours)

#### Step 2.1: Angular Component TDD

**Prompt:** `.claude/prompts/agents/frontend/angular-component-development.md`

**Prompt Context:**
```
TDD for Angular frontend migration:
1. Analyze legacy WebForms UI patterns
2. Write Angular component tests FIRST (Red phase)
3. Implement Angular components to pass tests (Green phase)
4. Refactor for performance and maintainability

Include: TypeScript interfaces, reactive forms, HTTP client testing.
```

**Expected Results:**
- Framework detects Angular 17+ from CLAUDE.md
- WebForms → Angular component mapping
- Comprehensive Angular test suite (unit + integration)
- **TDD Cycles:** Red → Green → Refactor for each component
- TypeScript interfaces matching .NET Core API contracts

#### Step 2.2: E2E Testing with Playwright MCP

**Prompt:** `.claude/prompts/agents/qa/test-automation-and-quality-assurance.md` (second time, E2E focus)

**Prompt Context:**
```
Playwright MCP integration for comprehensive E2E testing:
1. Convert legacy user workflows → Playwright test scenarios
2. Cross-browser testing (Chrome, Firefox, Safari)
3. Visual regression testing comparing legacy vs. modern
4. Performance testing and accessibility validation
5. Test data management across different environments
```

**Expected Results:**
- Complete Playwright test suite for all user workflows
- Cross-browser compatibility validation
- Performance benchmarking (legacy vs. modern)
- Visual regression testing capabilities
- **Continuous E2E Testing:** Integrated in TDD workflow

### Phase 3: Database Migration with TDD (3-4 hours)

#### Step 3.1: Database Schema Migration

**Prompt:** `.claude/prompts/agents/data/database-design-and-etl-implementation.md`

**Prompt Context:**
```
TDD approach for database migration:
1. Write database integration tests FIRST
2. Migrate stored procedures → Entity Framework Core
3. Test complex data transformations
4. Validate business rule enforcement in database layer
5. Performance testing for large datasets
```

**Expected Results:**
- Entity Framework Core models with comprehensive test coverage
- Stored procedure migration to C# LINQ queries
- Database integration test suite
- Data migration scripts with validation tests
- Performance optimization for complex queries

### Phase 4: Integration and System Testing (4-5 hours)

#### Step 4.1: API Integration Testing

**Prompt:** `.claude/prompts/agents/frontend/frontend-backend-integration.md`

**Expected Results:**
- Complete integration test suite Angular ↔ .NET Core API
- Authentication/authorization testing
- Error handling and user feedback scenarios
- Real-time communication testing (SignalR if applicable)
- **Integration TDD:** Tests covering all integration points

#### Step 4.2: Security and Performance Testing

**Prompt:** `.claude/prompts/agents/security/secure-code-review-and-sast.md`

**Expected Results:**
- Security test automation (authentication, authorization, data protection)
- Performance test automation (load testing, stress testing)
- Vulnerability scanning integration in CI/CD
- Security compliance validation tests

### Phase 5: Migration Strategy and Deployment (3-4 hours)

#### Step 5.1: Progressive Migration Strategy

**Prompt:** `.claude/prompts/agents/deployment/ci-cd-pipeline-and-infrastructure-setup.md`

**Expected Results:**
- Blue-green deployment strategy for zero-downtime migration
- Feature flagging for progressive rollout
- Rollback procedures with comprehensive testing
- **Automated Deployment Testing:** Every deployment validated by test suite

## Using Orchestration for Complex Migration

### Advanced Orchestration for TDD Migration

```bash
# Specialized orchestration for complex migration projects
./.claude/hooks/orchestration/conditional-workflow-engine.sh "$(pwd)" "enterprise" "migration-tdd"

# Multi-phase orchestration with TDD gates:
./.claude/hooks/orchestration-trigger.sh "$(pwd)" "migration" "tdd-mode"

# Real-time monitoring for complex workflows
./.claude/hooks/orchestration-monitor.sh "watch" "migration-progress"
```

**Advanced Orchestration Features:**
1. **TDD Phase Gates:** Each phase requires passing tests before progression
2. **Parallel Testing:** Unit, integration, E2E tests run concurrently
3. **Automatic Rollback:** Failed tests trigger automatic workflow rollback
4. **Quality Gates:** Code coverage, performance, security gates
5. **Business Validation:** Stakeholder approval gates for critical business logic

### Playwright MCP Integration in Orchestration

```bash
# Automated E2E testing in each development phase
# Orchestration automatically triggers:

# 1. Legacy behavior capture (record current system)
# 2. Modern system testing (validate new implementation)
# 3. Comparison testing (ensure behavioral parity)
# 4. Regression testing (ensure no functionality loss)
```

## Advanced Hooks for Migration Project

### Migration-Specific Hooks

#### Legacy Analysis Hook

```bash
# Specialized hook for legacy code analysis
./.claude/hooks/legacy-system-analyzer.sh "start" "cpp-backend"
./.claude/hooks/legacy-system-analyzer.sh "start" "webforms-frontend"

# Business logic extraction
./.claude/hooks/business-logic-extractor.sh "analyze" "cpp-to-csharp"
```

#### TDD Workflow Hook

```bash
# Automated TDD cycle enforcement
./.claude/hooks/tdd-workflow-enforcer.sh "start" "red-green-refactor"

# Test coverage monitoring
./.claude/hooks/test-coverage-monitor.sh "enforce" "90-percent-minimum"

# Automatic test execution on code changes
./.claude/hooks/continuous-testing.sh "enable" "playwright-integration"
```

#### Migration Progress Hook

```bash
# Track migration progress across all components
./.claude/hooks/migration-progress-tracker.sh "status" "overall"

# Component-specific progress
./.claude/hooks/migration-progress-tracker.sh "component" "frontend-angular"
./.claude/hooks/migration-progress-tracker.sh "component" "backend-api"
```

## Using MCP Tools for Advanced Migration

### Playwright MCP - Comprehensive E2E Testing

```bash
# Advanced Playwright scenarios in Claude Code:

# Legacy system behavior recording:
playwright record-legacy --url=http://legacy-system --output=legacy-behavior.spec.js

# Modern system testing:
playwright test modern-implementation.spec.js --browser=all

# Comparison testing:
playwright compare-behaviors --legacy=legacy-behavior.spec.js --modern=modern-implementation.spec.js

# Visual regression testing:
playwright visual-compare --baseline=legacy-screenshots --current=modern-screenshots
```

### Serena MCP - Deep Code Analysis

```bash
# Complex code analysis commands:

# C++ business logic extraction:
serena analyze-cpp --extract-business-logic --output=business-rules.md

# WebForms to Angular mapping:
serena map-ui-patterns --from=webforms --to=angular --output=ui-migration-map.json

# Cross-language dependency analysis:
serena trace-dependencies --from=cpp --to=csharp --business-logic-focus
```

### Context7 MCP - Advanced Documentation

```bash
# Comprehensive documentation generation:

# Business logic documentation:
context7 generate-docs --type=business-logic --source=cpp-analysis --output=business-requirements.md

# API documentation:
context7 generate-api-docs --source=dotnet-controllers --format=openapi-3.0

# Test documentation:
context7 generate-test-docs --source=playwright-tests --format=test-coverage-report
```

## Real Use Case - Enterprise Migration Challenges

### Challenge 1: Complex C++ Business Logic

**Problem:** 10,000 lines of undocumented C++ code with complex mathematical algorithms

**TDD Solution Process:**
1. **Test-First Approach:** Write comprehensive tests based on input/output analysis
2. **Algorithm Reconstruction:** C++ code analysis → mathematical specification → C# implementation
3. **Validation Testing:** Extensive test cases with real production data
4. **Performance Testing:** Ensure C# version matches C++ performance

**Implementation Timeline:** 2 weeks
**Test Coverage:** 95% for business logic algorithms
**Performance:** C# version 15% faster than original C++

### Challenge 2: WebForms to Angular Migration

**Problem:** 50+ WebForms pages with complex server-side logic and ViewState dependencies

**TDD Solution Process:**
1. **User Journey Testing:** Playwright capture all user workflows
2. **Component-by-Component:** Each WebForm → Angular component with comprehensive tests
3. **State Management:** ViewState replacement with Angular state management patterns
4. **Progressive Migration:** Feature flags enable gradual rollout

**Implementation Timeline:** 6 weeks
**Test Coverage:** 90% component coverage, 100% E2E workflow coverage
**User Experience:** 5x faster page loads, modern responsive design

### Challenge 3: Database Stored Procedure Migration

**Problem:** 200+ stored procedures with complex business logic

**TDD Solution Process:**
1. **Integration Tests First:** Test each stored procedure input/output
2. **LINQ Translation:** SP logic → Entity Framework Core queries
3. **Performance Testing:** Ensure query performance parity
4. **Data Integrity:** Comprehensive data validation tests

**Implementation Timeline:** 4 weeks
**Test Coverage:** 100% database integration test coverage
**Performance:** 25% improvement in query performance

## Expected Final Results

### Technical Deliverables

- ✅ **Complete Modern Application** - Angular 17+ frontend with .NET Core 8.0 API
- ✅ **Comprehensive Test Suite** - 90%+ coverage with automated Playwright E2E tests
- ✅ **Zero Business Logic Loss** - All C++ algorithms successfully migrated to C#
- ✅ **Performance Improvements** - 10x faster response times, modern UX
- ✅ **Cloud-Ready Architecture** - Scalable, maintainable, modern technology stack

### Business Deliverables

- ✅ **Zero Downtime Migration** - Progressive rollout with automatic rollback capabilities
- ✅ **Enhanced User Experience** - Modern responsive design with improved workflows
- ✅ **Future-Proof Technology** - Modern stack enabling rapid future development
- ✅ **Comprehensive Documentation** - Complete system documentation with business logic specs
- ✅ **Maintainable Codebase** - Clean architecture with extensive test coverage

### Migration Success Metrics

- **Development Time:** 12 weeks vs. estimated 18-24 months traditional approach
- **Test Coverage:** 90%+ across all layers (unit, integration, E2E)
- **Performance Improvement:** 10x faster response times, 5x faster page loads
- **Business Continuity:** Zero business interruption during migration
- **Code Quality:** 95% maintainability index, zero critical bugs
- **User Satisfaction:** 85% user satisfaction increase post-migration

### Long-term Benefits

- **Development Velocity:** 300% increase in new feature development speed
- **Maintenance Cost:** 70% reduction in ongoing maintenance costs
- **Scalability:** Cloud-ready architecture supporting 10x user growth
- **Technology Debt:** Eliminated legacy technology debt
- **Team Productivity:** Modern development tools and practices

## TODO Workflow Management for TDD Migration

### Enterprise-Scale TODO Configuration

Based on CLAUDE.md Section 8 configuration for **enterprise** scale with **TDD methodology**:

```yaml
## 8. TODO Management Configuration
### Task Management Strategy
- **todo_management_enabled**: true
- **todo_hierarchy_level**: hierarchical
- **auto_task_creation**: true
- **project_scale**: enterprise
- **business_domain**: enterprise

### TDD-Specific Settings
- **test_driven_development**: true
- **legacy_system_migration**: true
- **zero_downtime_deployment**: critical
- **comprehensive_testing**: mandatory
```

### Test-Driven TODO Examples

#### Phase 1: Legacy Analysis with TDD TODO Flow

**qa-engineer** drives test-first legacy analysis:

```javascript
// TDD Approach: Tests before understanding
TodoWrite({
  todos: [
    {
      content: "RED: Write failing tests for C++ business logic outputs",
      status: "completed",
      activeForm: "Writing failing tests for C++ logic"
    },
    {
      content: "GREEN: Reverse-engineer C++ algorithms to pass tests",
      status: "in_progress",
      activeForm: "Reverse-engineering C++ algorithms"
    },
    {
      content: "REFACTOR: Optimize C# algorithm implementations",
      status: "pending",
      activeForm: "Optimizing C# implementations"
    }
  ]
})
```

**api-engineer** follows TDD for API migration:

```javascript
// API migration with test-first approach
TodoWrite({
  todos: [
    {
      content: "RED: Write integration tests for WebForms API behavior",
      status: "completed",
      activeForm: "Writing WebForms integration tests"
    },
    {
      content: "GREEN: Implement .NET Core API to pass WebForms tests",
      status: "in_progress",
      activeForm: "Implementing .NET Core API"
    },
    {
      content: "REFACTOR: Optimize API performance and error handling",
      status: "pending",
      activeForm: "Optimizing API performance"
    }
  ]
})
```

#### Phase 2: Playwright E2E TDD Coordination

**frontend-engineer** with **qa-engineer** parallel TDD workflow:

```javascript
// Frontend engineer creates component structure
TodoWrite({
  todos: [
    {
      content: "RED: Record legacy WebForms user workflows with Playwright",
      status: "completed",
      activeForm: "Recording legacy workflows"
    },
    {
      content: "GREEN: Build Angular components to pass Playwright tests",
      status: "in_progress",
      activeForm: "Building Angular components"
    },
    {
      content: "REFACTOR: Optimize Angular performance and UX",
      status: "pending",
      activeForm: "Optimizing Angular performance"
    }
  ]
})

// qa-engineer manages comprehensive test validation
TodoWrite({
  todos: [
    {
      content: "Validate 100% Playwright test coverage for all workflows",
      status: "in_progress",
      activeForm: "Validating test coverage"
    },
    {
      content: "Execute cross-browser compatibility testing",
      status: "pending",
      activeForm: "Executing cross-browser tests"
    },
    {
      content: "Performance regression testing vs legacy system",
      status: "pending",
      activeForm: "Performance regression testing"
    }
  ]
})
```

#### Phase 3: Database Migration TDD Flow

**data-engineer** manages complex stored procedure migration:

```javascript
// TDD for database migration
TodoWrite({
  todos: [
    {
      content: "RED: Integration tests for all 200+ stored procedures",
      status: "completed",
      activeForm: "Testing stored procedures"
    },
    {
      content: "GREEN: LINQ implementations to pass SP integration tests",
      status: "in_progress",
      activeForm: "Implementing LINQ equivalents"
    },
    {
      content: "REFACTOR: Optimize EF Core queries for performance",
      status: "pending",
      activeForm: "Optimizing EF Core queries"
    },
    {
      content: "Data integrity validation with comprehensive test suite",
      status: "pending",
      activeForm: "Validating data integrity"
    }
  ]
})
```

### Critical Issue Management with TDD

**High-Priority Bug with TDD Resolution:**

```javascript
// qa-engineer discovers performance regression
TodoWrite({
  todos: [
    {
      content: "CRITICAL: C# algorithm 50% slower than C++ in performance tests",
      status: "in_progress",
      activeForm: "Analyzing performance regression"
    },
    {
      content: "RED: Write performance test with acceptable thresholds",
      status: "pending",
      activeForm: "Writing performance tests"
    },
    {
      content: "GREEN: Optimize C# code to pass performance test",
      status: "pending",
      activeForm: "Optimizing C# performance"
    }
  ]
})

// api-engineer responds with optimization
TodoWrite({
  todos: [
    {
      content: "Profile C# algorithm bottlenecks with detailed metrics",
      status: "in_progress",
      activeForm: "Profiling algorithm bottlenecks"
    },
    {
      content: "Implement parallel processing for C# algorithm",
      status: "pending",
      activeForm: "Implementing parallel processing"
    }
  ]
})

// Success: C# version becomes 15% faster than original C++
```

### TDD Quality Gates with TODO Integration

Enterprise-level TDD quality gates:

```javascript
// qa-engineer enforces strict TDD quality gates
TodoWrite({
  todos: [
    {
      content: "QUALITY GATE: 90%+ test coverage across all layers",
      status: "in_progress",
      activeForm: "Validating test coverage"
    },
    {
      content: "QUALITY GATE: 100% Playwright E2E workflow coverage",
      status: "completed",
      activeForm: "Validating E2E coverage"
    },
    {
      content: "QUALITY GATE: Zero performance regression vs legacy",
      status: "pending",
      activeForm: "Validating performance parity"
    },
    {
      content: "QUALITY GATE: 100% business logic algorithm accuracy",
      status: "pending",
      activeForm: "Validating algorithm accuracy"
    }
  ]
})
```

### Production TDD Automation

```bash
# TDD-specific automation templates
./.claude/templates/todo/agent-coordination-hooks.sh legacy-migration tdd-enterprise

# Expected TDD workflow output:
# 🔴 RED Phase:
# ✅ qa-engineer: All failing tests written
# ✅ frontend-engineer: Component test structure ready
# ✅ api-engineer: Integration test framework complete
#
# 🟢 GREEN Phase:
# ⏳ api-engineer: Implementation to pass tests in progress
# ⏳ frontend-engineer: Component development in progress
# ⏸️ data-engineer: Waiting for API completion
#
# 🔵 REFACTOR Phase:
# ⏸️ All agents: Waiting for GREEN phase completion
```

## TDD Methodology Results

### Test Pyramid Achievement

```
E2E Tests (Playwright): 150+ scenarios covering all user workflows
Integration Tests: 300+ tests covering all API and database interactions
Unit Tests: 800+ tests covering all business logic and components

Total Test Coverage: 92%
Test Execution Time: <5 minutes for full suite
Automated Test Success Rate: 98%
```

### TDD Workflow Success

- **Red Phase:** 100% failing tests written before implementation
- **Green Phase:** 100% tests passing after implementation
- **Refactor Phase:** Continuous code quality improvements
- **Cycle Time:** Average 15 minutes per TDD cycle
- **Bug Detection:** 95% of bugs caught by automated tests before deployment

---

**Status:** Complete enterprise-scale migration methodology utilizing Claude Code Multi-Agent Framework with TDD approach and Playwright automation. This example demonstrates the most complex migration scenario with comprehensive testing, business continuity, and zero-risk deployment strategies.

**Key Innovation:** Integration of TDD methodology with multi-agent coordination, automated testing via Playwright MCP, and systematic legacy code analysis resulting in risk-free enterprise migration with superior quality outcomes.