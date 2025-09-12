# Claude Code Agent Framework - Prompts Library

Specialized prompts library for the Claude Code Agent Framework's 11 agents, organized by function and workflow coordination.

## 📁 Directory Structure

```
.claude/prompts/
├── agents/           # Agent-specific prompts for common operations
│   ├── api/          # API Engineer prompts
│   ├── architecture/ # Software Architect prompts
│   ├── business/     # Business Analyst prompts
│   ├── data/         # Data Engineer prompts
│   ├── deployment/   # Deployment Engineer prompts
│   ├── design/       # UX Designer prompts
│   ├── frontend/     # Frontend Engineer prompts
│   ├── product/      # Product Manager prompts
│   ├── quality/      # QA Engineer prompts
│   ├── review/       # Reviewer prompts
│   └── security/     # Security Engineer prompts
├── workflows/        # Cross-agent coordination and handoff prompts
└── README.md        # This comprehensive guide
```

## 🤖 Agent-Specific Prompts

### Business Analysis (`agents/business/`)

#### **stakeholder-requirements-gathering.md**

- **Purpose:** Conduct structured stakeholder interviews and requirements workshops
- **When to use:** Starting new projects, gathering business requirements, understanding user needs
- **Key outputs:** Business Requirements Document, stakeholder analysis, success criteria
- **Agent:** business-analyst
- **Phases:** Business Discovery & Analysis, Architecture & UX Design

#### **current-state-process-analysis.md**

- **Purpose:** Analyze existing business processes to identify improvement opportunities
- **When to use:** Understanding existing workflows, identifying inefficiencies, planning process improvements
- **Key outputs:** Current state process maps, gap analysis, improvement opportunities matrix
- **Agent:** business-analyst
- **Phases:** Business Discovery & Analysis

#### **business-case-development.md**

- **Purpose:** Develop compelling business justification for proposed solutions
- **When to use:** Securing project funding, demonstrating ROI, gaining executive support
- **Key outputs:** Executive business case, financial models, risk assessments, implementation roadmap
- **Agent:** business-analyst
- **Phases:** Business Discovery & Analysis

### Product Management (`agents/product/`)

#### **feature-implementation-from-specification.md**

- **Purpose:** Implement complete application features from detailed specification documents with multi-layer coordination
- **When to use:** Feature development, specification-driven development, cross-team coordination, complete feature delivery
- **Key outputs:** Complete feature implementation (frontend + backend + database), production-ready functionality, comprehensive testing
- **Agent:** product-manager + frontend-engineer + api-engineer
- **Phases:** All phases - coordinated implementation

#### **user-story-creation-and-prioritization.md**

- **Purpose:** Transform business requirements into prioritized user stories with clear acceptance criteria
- **When to use:** Sprint planning, backlog grooming, feature definition, development prioritization
- **Key outputs:** Product backlog, user stories with acceptance criteria, prioritization matrix
- **Agent:** product-manager
- **Phases:** Business Discovery & Analysis, Architecture & UX Design

#### **mvp-scoping-and-roadmap-planning.md**

- **Purpose:** Define Minimum Viable Product scope and create strategic product roadmap
- **When to use:** Product strategy development, release planning, feature prioritization, stakeholder alignment
- **Key outputs:** MVP scope document, product roadmap, success metrics framework
- **Agent:** product-manager
- **Phases:** Business Discovery & Analysis, Architecture & UX Design

### UX Design (`agents/design/`)

#### **user-research-and-persona-development.md**

- **Purpose:** Conduct comprehensive user research and create actionable user personas
- **When to use:** Understanding target users, validating design decisions, informing product strategy
- **Key outputs:** User research report, primary personas, journey maps, design principles
- **Agent:** ux-designer
- **Phases:** Business Discovery & Analysis, Architecture & UX Design

### System Architecture (`agents/architecture/`)

#### **system-architecture-design.md**

- **Purpose:** Design scalable, maintainable system architecture aligned with business requirements
- **When to use:** Technical planning, technology stack selection, system design, scalability planning
- **Key outputs:** System architecture documentation, technology recommendations, implementation roadmap
- **Agent:** software-architect
- **Phases:** Architecture & UX Design

#### **frontend-backend-integration.md**

- **Purpose:** Architecture and implementation of seamless communication between frontend and backend systems across multiple technology stacks
- **When to use:** Angular+Java/Spring Boot integration, Angular+.NET Core integration, React+Node.js communication patterns
- **Key outputs:** Service layers, HTTP client configurations, authentication flows, error handling frameworks
- **Agent:** api-engineer + frontend-engineer
- **Phases:** Development & Continuous QA
- **Technologies:** Angular+Java/Spring Boot, Angular+.NET Core, React+Node.js, CORS, JWT, OAuth

#### **desktop-application-architecture.md**

- **Purpose:** Design and implement scalable desktop application architectures using modern patterns and cross-platform technologies
- **When to use:** Desktop application development, Python+wxPython, C++/wxWidgets, .NET/WPF desktop applications
- **Key outputs:** Desktop architecture patterns, UI frameworks, data binding systems, threading implementations
- **Agent:** software-architect + frontend-engineer
- **Phases:** Architecture & UX Design, Development & Continuous QA
- **Technologies:** Python+wxPython, C++/wxWidgets, .NET/WPF, MVC/MVP/MVVM patterns

#### **desktop-database-integration.md**

- **Purpose:** Implement comprehensive database integration patterns for desktop applications with local and remote databases
- **When to use:** Desktop database applications, SQLite integration, local data management, offline-first applications
- **Key outputs:** Database connection management, ORM patterns, repository implementations, data synchronization
- **Agent:** data-engineer + frontend-engineer
- **Phases:** Architecture & UX Design, Development & Continuous QA
- **Technologies:** SQLite, PostgreSQL, Python SQLAlchemy, C++ SQLite, .NET Entity Framework

#### **desktop-deployment-and-packaging.md**

- **Purpose:** Design and implement cross-platform deployment and packaging solutions for desktop applications
- **When to use:** Desktop application distribution, cross-platform deployment, installer creation, update mechanisms
- **Key outputs:** Build scripts, installers, update systems, platform-specific packages
- **Agent:** deployment-engineer + frontend-engineer
- **Phases:** Deployment & Operations
- **Technologies:** PyInstaller, CMake/CPack, dotnet publish, Windows/macOS/Linux packaging

#### **database-backend-integration.md**

- **Purpose:** Design comprehensive database schemas and backend integration patterns with advanced ORM configurations
- **When to use:** Database-driven applications, complex data models, API data layer design, multi-technology stack integration
- **Key outputs:** Database schemas, ORM configurations, repository patterns, API service layers
- **Agent:** data-engineer + api-engineer
- **Phases:** Architecture & UX Design, Development & Continuous QA
- **Technologies:** Java/Spring Boot+JPA, .NET Core+EF, Node.js+TypeORM, Python+SQLAlchemy

#### **application-performance-optimization.md**

- **Purpose:** Implement comprehensive performance optimization strategies across frontend, backend, and database layers
- **When to use:** Performance bottlenecks, scalability requirements, optimization audits, monitoring implementation
- **Key outputs:** Performance optimizations, monitoring systems, load testing frameworks, APM configurations
- **Agent:** qa-engineer
- **Phases:** Development & Continuous QA, Deployment & Operations
- **Technologies:** Performance monitoring, caching strategies, database optimization, frontend performance

### API Engineering (`agents/api/`)

#### **swagger-documentation-generation.md**

- **Purpose:** Generate comprehensive Swagger/OpenAPI documentation from existing backend API code
- **When to use:** API documentation, backend code analysis, documentation maintenance
- **Key outputs:** Complete OpenAPI 3.0 specification, interactive Swagger UI, integration examples
- **Agent:** api-engineer
- **Phases:** Development & Continuous QA

#### **swagger-to-endpoints-generation.md**

- **Purpose:** Generate complete, production-ready API endpoints from Swagger/OpenAPI specifications
- **When to use:** API development from documentation, ensuring consistency between spec and implementation
- **Key outputs:** Complete API controllers, models/DTOs, error handling, service layer integration
- **Agent:** api-engineer
- **Phases:** Development & Continuous QA

#### **rest-api-design-and-implementation.md**

- **Purpose:** Design and implement scalable, secure REST APIs following best practices
- **When to use:** API development, microservices architecture, backend integration design
- **Key outputs:** API specifications (OpenAPI/Swagger), implementation code, integration guides
- **Agent:** api-engineer
- **Phases:** Development & Continuous QA

#### **microservices-architecture-patterns.md**

- **Purpose:** Design and implement scalable microservices architecture with proven patterns and best practices
- **When to use:** System decomposition, service mesh architecture, distributed systems design
- **Key outputs:** Service boundary definitions, communication patterns, resilience implementations
- **Agent:** api-engineer
- **Phases:** Architecture & UX Design, Development & Continuous QA

#### **graphql-api-development.md**

- **Purpose:** Design and implement efficient GraphQL APIs with advanced features like subscriptions and federation
- **When to use:** Flexible data fetching requirements, real-time features, API federation scenarios
- **Key outputs:** GraphQL schemas, resolver implementations, subscription systems, federation setup
- **Agent:** api-engineer
- **Phases:** Development & Continuous QA

### Data Engineering (`agents/data/`)

#### **database-to-entityframework-generation.md**

- **Purpose:** Generate comprehensive Entity Framework Core models, contexts, and API endpoints from database schemas
- **When to use:** Database-first development, stored procedures integration, complete CRUD operations generation
- **Key outputs:** EF Core entities, DbContext, repositories, API controllers, stored procedure integration
- **Agent:** data-engineer + api-engineer
- **Phases:** Architecture & UX Design, Development & Continuous QA

#### **database-design-and-etl-implementation.md**

- **Purpose:** Design efficient database schemas and implement robust ETL pipelines for data processing
- **When to use:** Database design, data warehouse implementation, ETL pipeline development
- **Key outputs:** Database schemas, migration scripts, ETL pipeline code, data quality frameworks
- **Agent:** data-engineer
- **Phases:** Architecture & UX Design, Development & Continuous QA

### Security Engineering (`agents/security/`)

#### **security-architecture-and-threat-modeling.md**

- **Purpose:** Design comprehensive security architecture and conduct thorough threat modeling
- **When to use:** Security planning, threat assessment, compliance implementation, incident response
- **Key outputs:** Security architecture, threat models, incident response plans, compliance frameworks
- **Agent:** security-engineer
- **Phases:** Architecture & UX Design, Development & Continuous QA

#### **penetration-testing-and-security-audit.md**

- **Purpose:** Conduct comprehensive penetration testing and security audits of applications and infrastructure
- **When to use:** Security assessments, control validation, pre-deployment testing, compliance audits
- **Key outputs:** Penetration testing reports, vulnerability matrices, remediation plans
- **Agent:** security-engineer
- **Phases:** Development & Continuous QA, Deployment & Operations

#### **compliance-audit-and-governance.md**

- **Purpose:** Implement compliance frameworks and conduct regulatory compliance audits
- **When to use:** Audit preparation, compliance implementation, regulatory risk management
- **Key outputs:** Compliance documentation, audit results, remediation plans, governance frameworks
- **Agent:** security-engineer
- **Phases:** All phases (continuous monitoring)

#### **incident-response-and-forensics.md**

- **Purpose:** Develop incident response plans and conduct digital forensics analysis of security incidents
- **When to use:** Incident preparedness, breach response, post-incident analysis
- **Key outputs:** Incident response plans, playbooks, forensic reports, preventive measures
- **Agent:** security-engineer
- **Phases:** Deployment & Operations, Monitoring & Continuous Improvement

#### **security-controls-implementation.md**

- **Purpose:** Implement comprehensive security controls and security monitoring systems
- **When to use:** Security hardening, monitoring setup, access control implementation
- **Key outputs:** Security control configurations, monitoring dashboards, response procedures
- **Agent:** security-engineer
- **Phases:** Development & Continuous QA, Deployment & Operations

#### **identity-and-access-management.md**

- **Purpose:** Design and implement comprehensive identity and access management solutions
- **When to use:** SSO projects, RBAC implementation, IAM migrations, federation integrations
- **Key outputs:** IAM architecture, SSO configurations, access policies, audit procedures
- **Agent:** security-engineer
- **Phases:** Architecture & UX Design, Development & Continuous QA

#### **secure-code-review-and-sast.md**

- **Purpose:** Conduct advanced security code reviews and implement SAST tools
- **When to use:** Code reviews, security pipeline implementation, vulnerability analysis
- **Key outputs:** Security review reports, SAST configurations, secure coding guides
- **Agent:** security-engineer
- **Phases:** Development & Continuous QA

### Frontend Engineering (`agents/frontend/`)

#### **swagger-to-angular-generation.md**

- **Purpose:** Generate complete, type-safe Angular services and data models from Swagger/OpenAPI specifications
- **When to use:** Frontend API integration, Angular development from backend documentation, type-safe service generation
- **Key outputs:** TypeScript interfaces, Angular HTTP services, error handling, reactive patterns, form integration
- **Agent:** frontend-engineer
- **Phases:** Development & Continuous QA
- **Technologies:** Angular, TypeScript, RxJS, HTTP Client

#### **angular-component-development.md**

- **Purpose:** Architect and implement advanced Angular applications with enterprise-grade component architecture
- **When to use:** Angular app development, standalone components implementation, reactive programming
- **Key outputs:** Angular component library, RxJS state management, performance optimization frameworks
- **Agent:** frontend-engineer
- **Phases:** Development & Continuous QA
- **Technologies:** Angular 17+, TypeScript, RxJS, Angular Material

#### **wxwidgets-desktop-development.md**

- **Purpose:** Develop cross-platform desktop applications using wxWidgets with Python (wxPython) or C++
- **When to use:** Desktop applications, system tools, cross-platform applications
- **Key outputs:** Desktop application framework, advanced UI patterns, threading system
- **Agent:** frontend-engineer
- **Phases:** Development & Continuous QA
- **Technologies:** wxPython, wxWidgets C++, threading, SQLite

#### **responsive-design-and-css-architecture.md**

- **Purpose:** Implementation of modern CSS methodologies and responsive design patterns with design systems
- **When to use:** Responsive design, design systems, CSS optimization, accessibility
- **Key outputs:** CSS frameworks, design systems, responsive components, performance optimizations
- **Agent:** frontend-engineer
- **Phases:** Development & Continuous QA

#### **modern-javascript-and-typescript-development.md**

- **Purpose:** Mastery of modern JavaScript ES2023+ features and advanced TypeScript patterns
- **When to use:** Modern JavaScript/TypeScript development, code optimization, functional patterns
- **Key outputs:** Utility libraries, pattern frameworks, TypeScript configurations
- **Agent:** frontend-engineer
- **Phases:** Development & Continuous QA

#### **progressive-web-app-development.md**

- **Purpose:** Create comprehensive Progressive Web Applications with offline functionality and native integration
- **When to use:** PWA development, offline functionality, device feature integration
- **Key outputs:** Service workers, cache strategies, manifest, push notifications
- **Agent:** frontend-engineer
- **Phases:** Development & Continuous QA

#### **web-accessibility-and-inclusive-design.md**

- **Purpose:** Implement WCAG 2.1 compliance and create inclusive digital experiences
- **When to use:** Accessibility audits, WCAG implementation, inclusive design
- **Key outputs:** Accessibility frameworks, audit tools, ARIA components
- **Agent:** frontend-engineer
- **Phases:** Development & Continuous QA

#### **state-management-and-data-flow.md**

- **Purpose:** Architecture and implementation of comprehensive state management solutions for complex frontend applications
- **When to use:** Global state management, server state synchronization, performance optimization
- **Key outputs:** State management frameworks, reactive patterns, performance optimizations
- **Agent:** frontend-engineer
- **Phases:** Development & Continuous QA

#### **build-tools-and-bundler-optimization.md**

- **Purpose:** Architecture and optimization of advanced build pipelines for modern frontend applications
- **When to use:** Build optimization, bundle analysis, CI/CD configuration, performance optimization
- **Key outputs:** Webpack/Vite configurations, bundle analysis frameworks, CI/CD pipelines
- **Agent:** frontend-engineer
- **Phases:** Development & Continuous QA, Deployment & Operations

#### **frontend-testing-and-quality-assurance.md**

- **Purpose:** Implementation of comprehensive testing strategies and quality assurance frameworks for modern frontend applications
- **When to use:** Testing pyramid, E2E testing, accessibility testing, performance testing
- **Key outputs:** Testing frameworks, automated tests, visual regression testing
- **Agent:** frontend-engineer
- **Phases:** Development & Continuous QA

#### **react-component-development.md**

- **Purpose:** Architect and implement modern React applications with advanced component patterns and hooks
- **When to use:** React app development, component library creation, state management implementation
- **Key outputs:** React component library, custom hooks, performance optimization frameworks
- **Agent:** frontend-engineer
- **Phases:** Development & Continuous QA
- **Technologies:** React 18+, TypeScript, React Query, Zustand

#### **react-component-development-and-testing.md**

- **Purpose:** Comprehensive React component development with integrated testing strategies and quality assurance
- **When to use:** Test-driven React development, component testing, integration testing setup
- **Key outputs:** Tested React components, testing frameworks, CI/CD integration
- **Agent:** frontend-engineer
- **Phases:** Development & Continuous QA
- **Technologies:** React 18+, Jest, React Testing Library, Cypress

### Quality Assurance (`agents/quality/`)

#### **test-automation-and-quality-assurance.md**

- **Purpose:** Design comprehensive testing strategies and implement automated quality assurance processes
- **When to use:** Test planning, automation framework setup, quality gate implementation
- **Key outputs:** Test strategies, automated test suites, quality dashboards, CI/CD integration
- **Agent:** qa-engineer
- **Phases:** Development & Continuous QA

### Deployment Engineering (`agents/deployment/`)

#### **ci-cd-pipeline-and-infrastructure-setup.md**

- **Purpose:** Design and implement automated deployment pipelines and scalable infrastructure
- **When to use:** Infrastructure planning, CI/CD setup, deployment automation, monitoring implementation
- **Key outputs:** Infrastructure code, CI/CD pipelines, monitoring setup, deployment documentation
- **Agent:** deployment-engineer
- **Phases:** Deployment & Operations

### Review and Validation (`agents/review/`)

#### **sonarqube-code-quality-analysis.md**

- **Purpose:** Conduct comprehensive code quality analysis using SonarQube and establish quality gates
- **When to use:** Code quality assessment, technical debt analysis, quality gate enforcement
- **Key outputs:** Quality reports, remediation plans, automated quality gates, team coaching materials
- **Agent:** reviewer
- **Phases:** Development & Continuous QA

#### **security-vulnerability-assessment.md**

- **Purpose:** Conduct comprehensive security vulnerability assessments using automated tools and manual analysis
- **When to use:** Security audits, vulnerability management, compliance validation, penetration testing
- **Key outputs:** Vulnerability reports, risk assessments, remediation priorities, security dashboards
- **Agent:** reviewer
- **Phases:** Development & Continuous QA, Deployment & Operations

## 🔄 Workflow Coordination Prompts

### Phase Transitions (`workflows/phase-transitions/`)

*Section to be expanded - prompts will be created systematically*

### Orchestration Scenarios (`workflows/scenarios/`)

*Section to be expanded - scenarios will be created based on common use cases*

### Parallel Coordination (`workflows/parallel-coordination/`)

*Section to be expanded - prompts for parallel team work*

### Quality Gates (`workflows/quality-gates/`)

*Section to be expanded - prompts for validation checkpoints between phases*

### Stakeholder Communication (`workflows/stakeholder-communication/`)

*Section to be expanded - prompts for stakeholder updates and approval processes*

## 📊 Prompts Library Statistics

### Available Prompts Overview

| Agent | Available Prompts | Specialization Areas |
|-------|-------------------|----------------------|
| **business-analyst** | Available | Stakeholder requirements, process analysis, business cases |
| **product-manager** | Available | User story creation, MVP scoping, feature implementation |
| **ux-designer** | Available | User research and persona development |
| **software-architect** | Available | System architecture design |
| **api-engineer** | Available | REST API, microservices, GraphQL, Swagger generation |
| **data-engineer** | Available | Database design, ETL, EntityFramework generation |
| **frontend-engineer** | Complete coverage | Angular, React, wxWidgets, PWA, accessibility, modern JS/TS |
| **security-engineer** | Complete coverage | Threat modeling, pentesting, compliance, IAM, forensics |
| **qa-engineer** | Available | Test automation and quality assurance |
| **deployment-engineer** | Available | CI/CD pipeline and infrastructure setup |
| **reviewer** | Available | Code quality analysis, security vulnerability assessment |

**Status:** Comprehensive prompts library with complete coverage for security and frontend engineering

**Comprehensive Coverage Areas:**
- **Security Engineering:** Complete enterprise security workflow coverage
- **Frontend Development:** Full-stack modern frontend development
- **Business Analysis:** Core business discovery and requirements processes

## 🎯 How to Use These Prompts

### For Individual Agent Work

1. **Select appropriate agent prompt** based on your current role and task
2. **Read the mission and process** sections carefully
3. **Follow the structured approach** provided in the prompt
4. **Use the collaboration points** to coordinate with other agents
5. **Deliver the specified outputs** with quality standards

### For Workflow Coordination

1. **Identify the workflow transition** or coordination need
2. **Select appropriate workflow prompt** for your situation
3. **Gather required participants** as specified in the prompt
4. **Follow the process framework** and agenda templates
5. **Validate success criteria** before proceeding to next phase

### For Project Planning

1. **Start with Phase 1 business analysis** prompts
2. **Use workflow transition prompts** to move between phases
3. **Apply parallel coordination prompts** during development phases
4. **Leverage quality gate prompts** for validation checkpoints
5. **Use stakeholder communication prompts** for updates and approvals

## 🛠️ Customization Guidelines

### Adapting Prompts for Your Project

- **Replace placeholders** with project-specific information
- **Adjust timelines** based on your project schedule
- **Modify deliverables** to match your documentation standards
- **Customize success criteria** for your business context
- **Add domain-specific requirements** as needed

### Creating New Prompts

- **Follow existing prompt structure** for consistency
- **Include clear mission statement** and purpose
- **Provide step-by-step process** framework
- **Specify collaboration points** with other agents
- **Define clear deliverables** and success criteria
- **Add examples** and templates where helpful

## 🔧 Integration with Claude Code

### Using Prompts in Claude Code

1. **Open Claude Code** in the project directory
2. **Select appropriate agent** for the task
3. **Reference the prompt** using path (e.g., `agents/frontend/angular-component-development.md`)
4. **Customize the prompt** for specific project requirements
5. **Execute the task** following prompt guidelines
6. **Coordinate with other agents** as needed

### Integration with AI Tools

#### Serena Integration

- Use Serena for **navigating existing codebases** when analyzing current state
- Leverage Serena for **precise code modifications** during implementation
- Apply Serena for **debugging and troubleshooting** during development phases

#### Context7 Integration

- Use Context7 for **generating new code** based on specifications
- Leverage Context7 for **creating comprehensive documentation** and templates
- Apply Context7 for **large-scale transformations** and migrations

## 📚 Additional Resources

- **Agent Specifications:** `.claude/agents/` directory for detailed agent capabilities
- **Workflow Diagrams:** `.claude/docs/agent-sdlc-workflow.puml` for visual process overview
- **Project Configuration:** `CLAUDE.md` for project-specific agent guidance
- **AI Tools Guide:** `.claude/docs/ai-tools-usage-guide.md` for Serena and Context7 usage
- **Main README:** `README.md` for general project overview and configuration

## 🚀 Next Development Steps

### Planned Expansion

1. **Continue developing agent prompts** based on project needs and domain expertise
2. **Workflow scenarios** - create complete orchestration scenarios  
3. **Quality gates** - prompts for validation checkpoints between phases
4. **Stakeholder communication** - frameworks for updates and approvals
5. **Documentation templates** - standard formats for deliverables

### Development Approach

- Focus on **real project needs** rather than predetermined targets
- Develop prompts based on **actual workflow requirements**
- Prioritize **quality and completeness** over quantity
- Create prompts that address **specific domain expertise areas**

---

**Note:** This prompts library is continuously evolving. Prompts marked with *[To be created]* indicate areas for future expansion based on project needs and user feedback.

*Each prompt is designed to work independently while supporting the overall Agent-Driven Development Lifecycle for maximum productivity and quality.*