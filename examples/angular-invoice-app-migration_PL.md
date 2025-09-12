# Przykład 2: Migracja Aplikacji Web do Wystawiania Faktur - Angular/.NET API

**Data wykonania:** 2025-09-12  
**Commit:** 73a1009 (adaptative prompts)  
**Framework Version:** Claude Code Multi-Agent Framework v1.0 - Technology Adaptive

## Krótki Opis Aplikacji

Modernizacja istniejącej aplikacji web do wystawiania faktur z przestarzałą dokumentacją API. Projekt obejmuje analizę istniejącego systemu, aktualizację dokumentacji Swagger, oraz optymalizację funkcjonalności biznesowej na podstawie reverse engineering i analizy kodu.

## Kluczowe Założenia Technologiczne

- **Frontend:** Angular 17+ (istniejący, wymaga aktualizacji)
- **Backend API:** .NET Core Web API (istniejący C# kod)
- **Database:** SQL Server/PostgreSQL (analiza istniejących połączeń)
- **Documentation:** Swagger/OpenAPI 3.0 (regeneracja z kodu)
- **Challenge:** Przestarzała dokumentacja Swagger nie odzwierciedla rzeczywistych endpointów
- **Approach:** Reverse engineering + code analysis + documentation rebuild

## Przykładowa Zawartość CLAUDE.md

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

## Sposób Zainicjowania Pracy z Projektem

### 1. Przygotowanie Środowiska Analizy

```bash
# Nawigacja do katalogu frameworku
cd /mnt/e/AI/my_name_is_claude

# Utworzenie katalogu analizy projektu
mkdir invoice-app-migration
cd invoice-app-migration

# Skopiowanie frameworku
cp -r ../.claude .
cp ../CLAUDE.md .
cp ../DATABASE_CONNECTIONS.md .

# Przygotowanie struktury analizy
mkdir -p analysis/{api,frontend,database,documentation}
mkdir -p existing-code/{backend,frontend}

# Dostosowanie CLAUDE.md do projektu migracji
# [Edytuj plik CLAUDE.md zgodnie z powyższą zawartością]
```

### 2. Analiza Istniejącego Kodu

```bash
# Symulacja skopiowania istniejącego kodu do analizy
# W rzeczywistym projekcie:
# cp -r /path/to/existing/backend/* ./existing-code/backend/
# cp -r /path/to/existing/frontend/* ./existing-code/frontend/

# Inicjalizacja Claude Code z kontekstem istniejącego projektu
claude-code
```

## Sposób Zainicjowania MCP

### Serena MCP (Analiza Istniejącego Kodu)

```bash
# Konfiguracja Serena dla analizy istniejącego kodu
../mcp_tools.sh

# Wybór opcji 2: Serena MCP
# Konfiguracja specjalna dla code analysis:
# - Port: 3002
# - Directory: ./existing-code (dla analizy legacy code)
# - Auto-indexing: enabled
# - Development mode: enabled

# Dodatkowa konfiguracja dla multi-directory analysis:
# Directory 1: ./existing-code/backend (.NET API)
# Directory 2: ./existing-code/frontend (Angular app)
```

### Context7 MCP (Dokumentacja i Regeneracja)

```bash
# Context7 MCP dla dokumentacji rebuild
# Opcja 1: Context7 MCP
# Specjalna konfiguracja dla documentation generation:
# - Focus: API documentation regeneration
# - Template: OpenAPI 3.0 specification
# - Output: Swagger documentation
```

## Szczegółowa Instrukcja Krok po Kroku

### Faza 1: Analiza Istniejącego Systemu (2-3 godziny)

#### Krok 1.1: Analiza API Endpoints przez Reverse Engineering

**Prompt:** `.claude/prompts/agents/api/rest-api-design-and-implementation.md`

**Kontekst dla promptu:**
```
Mam istniejącą aplikację .NET Core Web API do fakturowania. 
Stara dokumentacja Swagger jest nieaktualna i wskazuje błędne endpointy.
Potrzebuję przeanalizować kod źródłowy kontrollerów i zregenerować dokładną dokumentację API.

Skopiuj controllers z existing-code/backend/Controllers/ i przeanalizuj rzeczywiste endpointy.
```

**Oczekiwane efekty:**
- Framework automatycznie wykryje .NET Core z CLAUDE.md
- Otrzymasz analizę Controllers ze wszystkimi rzeczywistymi endpointami
- Lista działających vs. dokumentowanych endpointów
- Propozycje poprawek i modernizacji API
- Nowa struktura dokumentacji OpenAPI 3.0

**Jak reagować na opcje:**
- **Deprecated endpoints:** Zaplanuj migration path
- **Missing documentation:** Prioritize critical business endpoints
- **API versioning:** Implement if multiple versions detected

#### Krok 1.2: Regeneracja Dokumentacji Swagger

**Prompt:** `.claude/prompts/agents/api/swagger-documentation-generation.md`

**Oczekiwane efekty:**
- Automatyczne generowanie OpenAPI spec z kodu .NET
- Kompletna dokumentacja wszystkich działających endpointów
- Request/Response schemas z przykładami
- Authentication/Authorization schemas
- API testing capabilities w Swagger UI

#### Krok 1.3: Analiza Frontendu Angular

**Prompt:** `.claude/prompts/agents/frontend/angular-component-development.md`

**Kontekst dla promptu:**
```
Analizuję istniejącą aplikację Angular do fakturowania.
Potrzebuję zidentyfikować:
- Które komponenty wywołują które API endpoints
- Jakie services są używane do komunikacji z API
- Które części frontend są nieaktywne/nieużywane
- Stan TypeScript definitions dla API responses
```

**Oczekiwane efekty:**
- Mapowanie Angular services → API endpoints
- Identyfikacja nieistniejących API calls (404 errors)
- Propozycje modernizacji Angular do wersji 17+
- TypeScript interfaces alignment z rzeczywistym API

### Faza 2: Dokumentacja i Specyfikacja (2-3 godziny)

#### Krok 2.1: Rekonstrukcja Procesów Biznesowych

**Prompt:** `.claude/prompts/agents/business/current-state-process-analysis.md`

**Kontekst dla promptu:**
```
Na podstawie analizy kodu backend i frontend, zrekonstruuj rzeczywiste procesy biznesowe:
- Jak wygląda flow tworzenia faktury?
- Jakie są wymagane pola i walidacje?
- Które procesy są zautomatyzowane?
- Gdzie występują bottlenecki w UX?
```

**Oczekiwane efekty:**
- Kompletna mapa procesów biznesowych invoice workflow
- Identyfikacja luk w funkcjonalności vs. code implementation
- Propozycje optymalizacji user experience
- Requirements dla missing functionality

#### Krok 2.2: Analiza Bezpieczeństwa

**Prompt:** `.claude/prompts/agents/security/secure-code-review-and-sast.md`

**Oczekiwane efekty:**
- Framework wykryje .NET Core i zaproponuje security analysis
- Code review dla authentication/authorization
- Identyfikacja potential security vulnerabilities
- Compliance check dla financial application standards

#### Krok 2.3: Audyt Bazy Danych

**Prompt:** `.claude/prompts/agents/data/database-design-and-etl-implementation.md`

**Oczekiwane efekty:**
- Analiza istniejącego database schema
- Entity Framework model validation
- Performance bottlenecks identification
- Data migration strategies proposal

### Faza 3: Modernizacja i Optymalizacja (4-6 godzin)

#### Krok 3.1: Modernizacja API

**Prompt:** `.claude/prompts/agents/api/rest-api-design-and-implementation.md` (drugi raz, z focus na improvements)

**Kontekst dla promptu:**
```
Na podstawie analizy, zmodernizuj API:
- Dodaj missing endpoints identified w frontend analysis
- Implement proper error handling i status codes
- Add API versioning strategy
- Optimize performance dla bulk operations
```

**Oczekiwane efekty:**
- Updated .NET Controllers z best practices
- Proper HTTP status codes i error handling
- API versioning implementation
- Performance optimizations (caching, pagination)
- Updated OpenAPI documentation

#### Krok 3.2: Frontend Optimization

**Prompt:** `.claude/prompts/agents/frontend/frontend-backend-integration.md`

**Oczekiwane efekty:**
- Angular services updated dla new API structure
- Proper error handling w frontend
- TypeScript interfaces generated z OpenAPI spec
- RxJS patterns dla async operations
- Loading states i user feedback

#### Krok 3.3: Performance Optimization

**Prompt:** `.claude/prompts/agents/frontend/application-performance-optimization.md`

**Oczekiwane efekty:**
- Angular performance optimizations (OnPush, lazy loading)
- API response optimization strategies
- Database query performance improvements
- Frontend bundle size optimization

### Faza 4: Testing i Validation (3-4 godziny)

#### Krok 4.1: API Testing

**Prompt:** `.claude/prompts/agents/qa/test-automation-and-quality-assurance.md`

**Oczekiwane efekty:**
- Comprehensive API testing strategy
- Integration tests dla critical invoice workflows
- Performance testing dla concurrent users
- Regression testing dla existing functionality

#### Krok 4.2: Frontend Testing

**Prompt:** `.claude/prompts/agents/frontend/frontend-testing-and-quality-assurance.md`

**Oczekiwane efekty:**
- Angular unit tests dla updated components
- E2E tests dla complete invoice workflows  
- User acceptance testing scenarios
- Cross-browser compatibility validation

### Faza 5: Deployment i Migration (2-3 godziny)

#### Krok 5.1: Migration Strategy

**Prompt:** `.claude/prompts/agents/deployment/ci-cd-pipeline-and-infrastructure-setup.md`

**Oczekiwane efekty:**
- Zero-downtime deployment strategy
- Database migration plan
- Rollback procedures
- Monitoring i alerting setup

## Wykorzystanie Orkiestracji i Hooks

### Orkiestracja dla Legacy Code Analysis

```bash
# Specjalny scenariusz dla legacy migration
./.claude/hooks/orchestration-trigger.sh "$(pwd)" "migration"

# Lub automatyczna detekcja:
./.claude/hooks/orchestration-trigger.sh

# Advanced conditional workflow dla complex migration
./.claude/hooks/orchestration/conditional-workflow-engine.sh "$(pwd)" "fintech" "migration"
```

**Oczekiwane zachowanie orkiestracji:**
1. **Legacy Analysis Phase:** business-analyst → api-engineer (code analysis) → frontend-engineer
2. **Documentation Rebuild:** api-engineer (swagger generation) → reviewer (validation)
3. **Modernization Phase:** api-engineer → frontend-engineer → qa-engineer (parallel)
4. **Deployment Preparation:** deployment-engineer → security-engineer (final review)

### Wykorzystanie Hooks dla Migration

#### Code Analysis Monitoring

```bash
# Monitoring analizy legacy code
./.claude/hooks/agent-performance-monitor.sh "start" "api-engineer"
./.claude/hooks/agent-performance-monitor.sh "start" "frontend-engineer"

# Tracking progress w reverse engineering
./.claude/hooks/agent-performance-monitor.sh "analyze" "migration"
```

#### Dependency Validation

```bash
# Walidacja zależności między frontend a API changes
./.claude/hooks/cross-agent-dependency-tracker.sh "validate" "frontend-backend"

# Check compatibility przed deployment
./.claude/hooks/cross-agent-dependency-tracker.sh "check" "migration-readiness"
```

#### Quality Gates

```bash
# Compliance dla financial applications
./.claude/hooks/compliance-automation.sh "fintech" "api-engineer"

# Security validation dla financial data
./.claude/hooks/compliance-automation.sh "security" "financial-data"
```

## Wykorzystanie MCP Tools dla Legacy Analysis

### Serena MCP - Advanced Code Navigation

```bash
# Deep code analysis dla controller discovery
# W Claude Code, użyj Serena commands:

# Analiza kontrollerów:
serena search "public class.*Controller" --type cs

# Discovery API endpoints:
serena search "\[Http(Get|Post|Put|Delete)\]" --type cs

# Database model analysis:
serena search "public class.*: IEntity" --type cs

# Angular service analysis:
serena search "@Injectable" --type ts --path frontend
```

### Context7 MCP - Documentation Generation

```bash
# Automatyczne generowanie dokumentacji:
# Użyj Context7 dla:

# 1. API Documentation rebuild
# 2. Frontend component documentation
# 3. Database schema documentation  
# 4. Migration guide generation
```

## Realny Przypadek Użycia - Problem-Solving Approach

### Challenge 1: Inconsistent API Documentation

**Problem:** Swagger documentation wskazuje /api/v1/invoices/create, ale rzeczywisty endpoint to /api/invoices/generate

**Solution Process:**
1. **Code Analysis:** Serena search dla wszystkich API routes
2. **Documentation Rebuild:** Swagger generation z rzeczywistego kodu
3. **Frontend Alignment:** Update Angular services dla correct endpoints
4. **Testing:** Comprehensive API testing dla all discovered endpoints

### Challenge 2: Missing Business Logic

**Problem:** Frontend ma komponenty dla "recurring invoices" ale API nie ma podpory

**Solution Process:**
1. **Business Analysis:** Determine if feature was planned but never implemented
2. **API Extension:** Add missing endpoints w .NET API
3. **Database Migration:** Add required tables/columns
4. **Frontend Integration:** Connect existing UI do new API

### Challenge 3: Performance Issues

**Problem:** Invoice listing page loading >5 seconds dla 1000+ invoices

**Solution Process:**
1. **API Analysis:** Database query optimization
2. **Pagination Implementation:** Server-side paging
3. **Frontend Optimization:** Virtual scrolling w Angular
4. **Caching Strategy:** Redis/memory caching dla frequent queries

## Oczekiwane Rezultaty Końcowe

### Deliverables Techniczne

- ✅ **Accurate API Documentation** - OpenAPI 3.0 spec reflecting actual endpoints
- ✅ **Modernized Angular Frontend** - Updated to latest patterns and performance optimizations
- ✅ **Optimized .NET API** - Performance improvements and proper error handling
- ✅ **Comprehensive Testing** - API and E2E tests for critical workflows
- ✅ **Migration Documentation** - Complete guide for deployment and rollback

### Deliverables Biznesowe

- ✅ **Restored System Reliability** - Eliminated 404 errors and API mismatches
- ✅ **Improved User Experience** - Faster loading times and better error messaging
- ✅ **Complete Business Process Documentation** - Clear understanding of all invoice workflows
- ✅ **Future-Proof Architecture** - Modern patterns enabling easier future enhancements

### Metrics Sukcesu

- **API Accuracy:** 100% documentation-code alignment (vs. previous ~60%)
- **Performance:** <2s page loading (vs. previous 5+s)
- **Error Reduction:** 95% reduction w frontend API errors
- **Development Velocity:** 50% faster future feature development
- **Maintenance Cost:** 60% reduction w debugging time dla API issues

### Migration Timeline

#### Tydzień 1: Analysis & Documentation
1. **Day 1-2:** Legacy code analysis i API discovery
2. **Day 3-4:** Documentation rebuild i business process mapping
3. **Day 5:** Security audit i performance baseline

#### Tydzień 2: Modernization & Testing
1. **Day 1-3:** API improvements i frontend optimization
2. **Day 4-5:** Comprehensive testing i validation

#### Tydzień 3: Deployment & Validation
1. **Day 1-2:** Staging deployment i user acceptance testing
2. **Day 3:** Production migration
3. **Day 4-5:** Post-migration monitoring i optimization

---

**Status:** Ready for legacy system analysis and modernization - Complete methodology dla handling problematic existing codebases using Claude Code Multi-Agent Framework with reverse engineering capabilities.

This example demonstrates practical approach do real-world migration challenges, including code analysis, documentation rebuild, i systematic modernization process using comprehensive multi-agent coordination.