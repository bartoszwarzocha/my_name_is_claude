# 📚 Claude Code Multi-Agent Framework - Prompts Library

**Framework Version:** 2.0.1
**Last Updated:** 2025-09-15
**Status:** Production Ready ✅

The comprehensive prompts library for the Claude Code Multi-Agent Framework, featuring specialized agent prompts, session management, project initialization, and complete workflow orchestration capabilities.

---

## 📋 Table of Contents

1. [Framework Overview](#-framework-overview)
2. [Directory Structure](#-directory-structure)
3. [How to Use Prompts in Chat](#-how-to-use-prompts-in-chat)
4. [Quick Start Guide](#-quick-start-guide)
5. [Agent-Specific Prompts](#-agent-specific-prompts)
6. [Session Management](#-session-management)
7. [Project Initialization](#-project-initialization)
8. [Project Management](#-project-management)
9. [Workflow Orchestration](#-workflow-orchestration)
10. [Creating Custom Prompts](#-creating-custom-prompts)
11. [Integration with Claude Code](#-integration-with-claude-code)
12. [Quality Standards](#-quality-standards)
13. [Best Practices](#-best-practices)

---

## 🎯 Framework Overview

The Claude Code Multi-Agent Framework provides:

- **Specialized AI Agents** covering the complete development lifecycle
- **Professional Prompts** with functional design patterns
- **Technology-Agnostic Architecture** adaptable to any development stack
- **Hierarchical TODO Management** with enterprise-grade task coordination
- **Session Management** with advanced state preservation and context analysis
- **Quality Assurance Framework** with continuous validation and improvement

### Core Principles

✅ **Functional Design**: Prompts describe WHAT to accomplish, not HOW to implement
✅ **Technology Agnostic**: Works across different technology stacks and project scales
✅ **CLAUDE.md Integration**: Adapts to project configuration and requirements
✅ **Measurable Criteria**: Clear, testable success conditions for all operations
✅ **Enterprise Ready**: Scalable from startup to enterprise-grade implementations

---

## 📁 Directory Structure

```
.claude/prompts/
├── README.md                    # This comprehensive documentation
├── PROMPT_TEMPLATE.md          # Template for creating custom prompts
├── session/                    # Session management ✅
│   ├── session-start-and-context-analysis.md
│   ├── session-continuation-from-summary.md
│   ├── session-end-and-summary-generation.md
│   ├── session-state-recovery.md
│   └── serena-sync-and-update.md
├── init/                       # Project initialization ✅
│   ├── claude_md_from_concept.md
│   ├── prepare_instruction.md
│   ├── new-project.md
│   └── existing-project.md
├── project/                    # Project management ✅
│   ├── project-health-check.md
│   ├── project-health-check-pro.md
│   ├── update-documentation-comprehensive.md
│   ├── update-changelog-and-version.md
│   ├── project-release-preparation.md
│   ├── framework-enhancement-implementation.md
│   ├── documentation-consistency-validator.md
│   └── project-structure-modernization.md
├── agents/                     # Agent-specific prompts ✅
│   ├── api/                   # API development
│   ├── architecture/          # System architecture
│   ├── automation/            # Automation engineering
│   ├── backend/               # Backend engineering
│   ├── business/              # Business analysis
│   ├── capacity/              # Capacity planning
│   ├── cloud/                 # Cloud engineering
│   ├── compliance/            # Compliance auditing
│   ├── data/                  # Data engineering
│   ├── database/              # Database administration
│   ├── deployment/            # DevOps and deployment
│   ├── design/                # UX/UI design
│   ├── devops/                # DevOps architecture
│   ├── documentation/         # Technical writing
│   ├── enterprise/            # Enterprise architecture
│   ├── frontend/              # Frontend development
│   ├── governance/            # Governance architecture
│   ├── incident/              # Incident response
│   ├── integration/           # Integration architecture
│   ├── middleware/            # Middleware engineering
│   ├── mobile/                # Mobile development
│   ├── monitoring/            # Monitoring engineering
│   ├── network/               # Network architecture
│   ├── performance/           # Performance engineering
│   ├── planner/               # Product management & review
│   ├── platform/              # Platform engineering
│   ├── project/               # Project coordination
│   ├── quality/               # Test automation
│   ├── reliability/           # Reliability engineering
│   ├── risk/                  # Risk management
│   ├── security/              # Security engineering
│   ├── session/               # Session management
│   └── sre/                   # Site reliability engineering
└── workflows/                  # Multi-agent orchestration ✅
    ├── parallel-coordination/ # Cross-team coordination
    ├── phase-transitions/     # Workflow handoffs
    ├── quality-gates/         # Validation checkpoints
    ├── scenarios/             # Development scenarios
    ├── stakeholder-communication/ # Stakeholder coordination
    └── todo-management/       # TODO orchestration
```

---

## 🎯 How to Use Prompts in Chat

### Method 1: Drag-and-Drop (Recommended)

The easiest way to use framework prompts is through drag-and-drop:

#### Step 1: Navigate to Prompt File
```bash
# In your file explorer, navigate to:
.claude/prompts/agents/[category]/[prompt-name].md

# Example paths:
.claude/prompts/agents/frontend/react-component-development.md
.claude/prompts/agents/security/security-architecture-and-threat-modeling.md
.claude/prompts/init/claude_md_from_concept.md
```

#### Step 2: Drag and Drop to Claude
1. **Select the prompt file** in your file manager
2. **Drag the file** into the Claude chat interface
3. **Drop the file** - Claude will automatically read and execute the prompt
4. **Follow the prompt instructions** - the agent will guide you through the process

#### Step 3: Provide Context (if needed)
```bash
# Some prompts may ask for additional context:
# - Project requirements
# - Technology preferences
# - Specific files or directories
# - Business objectives

# Example for initialization:
# 1. Drag claude_md_from_concept.md
# 2. Provide project description when asked
# 3. Specify technology stack preferences
# 4. Framework generates complete CLAUDE.md
```

### Method 2: Copy-Paste Content

Alternative method for manual prompt usage:

#### Step 1: Read Prompt File
```bash
# Open the prompt file in your editor
cat .claude/prompts/agents/frontend/react-component-development.md

# Or use your preferred text editor
code .claude/prompts/agents/frontend/react-component-development.md
```

#### Step 2: Copy and Paste to Chat
1. **Copy the entire prompt content** from the file
2. **Paste into Claude chat** interface
3. **Add your specific context** (project details, requirements, etc.)
4. **Submit the message** for processing

### Method 3: Reference by Path

For experienced users with Claude Code integration:

```bash
# Reference prompt by relative path
# Claude will automatically load and execute

"Use .claude/prompts/agents/frontend/react-component-development.md for this React component"

"Apply .claude/prompts/init/existing-project.md to integrate framework"

"Execute .claude/prompts/agents/security/penetration-testing-and-security-audit.md"
```

### 🔄 Prompt Execution Flow

#### Automatic Context Detection
1. **Project Analysis** - Framework detects technology stack from CLAUDE.md
2. **Environment Setup** - Configures appropriate tools and workflows
3. **Agent Coordination** - Selects optimal agent(s) for the task
4. **Execution** - Runs prompt with project-specific adaptations

#### Interactive Guidance
1. **Requirements Gathering** - Prompts ask for missing information
2. **Technology Confirmation** - Validates detected stack and preferences
3. **Progress Updates** - Shows execution progress with TodoWrite integration
4. **Quality Validation** - Ensures outputs meet defined success criteria

#### Result Delivery
1. **Primary Deliverables** - Main outputs as specified in prompt
2. **Documentation** - Comprehensive documentation and examples
3. **Next Steps** - Recommendations for follow-up actions
4. **Agent Handoffs** - Coordination points for multi-agent workflows

### 💡 Usage Tips

#### For Best Results
- **Start with project initialization** if framework not yet integrated
- **Use session management prompts** to maintain context across work sessions
- **Follow agent coordination sequences** for complex multi-component tasks
- **Leverage TODO management** for tracking progress and handoffs

#### Common Usage Patterns
```bash
# New Project Setup
1. Drag: .claude/prompts/init/claude_md_from_concept.md
2. Drag: .claude/prompts/init/prepare_instruction.md
3. Follow generated development roadmap

# Feature Development
1. Drag: .claude/prompts/agents/business/stakeholder-requirements-gathering.md
2. Drag: .claude/prompts/agents/architecture/system-architecture-design.md
3. Drag: .claude/prompts/agents/frontend/[technology-specific].md
4. Drag: .claude/prompts/agents/api/rest-api-design-and-implementation.md

# Quality Assurance
1. Drag: .claude/prompts/agents/security/security-vulnerability-assessment.md
2. Drag: .claude/prompts/agents/quality/test-automation-and-quality-assurance.md
3. Drag: .claude/prompts/agents/review/sonarqube-code-quality-analysis.md
```

#### Troubleshooting
- **If prompt doesn't execute**: Ensure file path is correct and accessible
- **If context is missing**: Check CLAUDE.md exists and is properly configured
- **If technology detection fails**: Manually specify stack in chat message
- **If agent coordination issues**: Use workflow orchestration prompts

---

## 🚀 Quick Start Guide

### 1. Using Session Management

**Start a new session:**
```bash
# Use session-start-and-context-analysis.md for project initialization
# Automatically detects technology stack and sets up context
```

**Continue from previous session:**
```bash
# Use session-continuation-from-summary.md with session summary
# Restores context and continues work seamlessly
```

### 2. Project Initialization

**For new projects:**
```bash
# Step 1: Create concept materials in init_concept/
mkdir init_concept
echo "Project description and requirements" > init_concept/project_idea.md

# Step 2: Use claude_md_from_concept.md
# Generates complete CLAUDE.md configuration from concept materials

# Step 3: Use prepare_instruction.md
# Creates custom development roadmap based on CLAUDE.md
```

**For existing projects:**
```bash
# Use existing-project.md for safe integration
# Analyzes current structure and integrates framework without disruption
```

### 3. Agent Workflows

**Business Discovery Phase:**
1. `agents/business/stakeholder-requirements-gathering.md`
2. `agents/business/current-state-process-analysis.md`
3. `agents/product/user-story-creation-and-prioritization.md`

**Architecture & Design Phase:**
1. `agents/architecture/system-architecture-design.md`
2. `agents/design/user-research-and-persona-development.md`
3. `agents/security/security-architecture-and-threat-modeling.md`

**Development Phase:**
1. `agents/frontend/[technology-specific-prompt].md`
2. `agents/api/rest-api-design-and-implementation.md`
3. `agents/data/database-design-and-etl-implementation.md`

---

## 🤖 Agent-Specific Prompts

### Business Analysis

#### `stakeholder-requirements-gathering.md`
- **Purpose**: Conduct structured stakeholder interviews and requirements workshops
- **Output**: Business Requirements Document, stakeholder analysis, success criteria
- **Technology**: Framework-agnostic business analysis
- **Usage**: Project initiation, requirements discovery, stakeholder alignment

#### `current-state-process-analysis.md`
- **Purpose**: Analyze existing business processes and identify improvement opportunities
- **Output**: Process maps, gap analysis, improvement recommendations
- **Usage**: Legacy system analysis, process optimization, change management

#### `business-case-development.md`
- **Purpose**: Develop compelling business justification for proposed solutions
- **Output**: Executive business case, ROI analysis, risk assessments
- **Usage**: Project funding, executive approval, business value demonstration

### Product Management

#### `user-story-creation-and-prioritization.md`
- **Purpose**: Transform business requirements into prioritized user stories
- **Output**: Product backlog, acceptance criteria, prioritization matrix
- **Usage**: Sprint planning, feature definition, development prioritization

#### `mvp-scoping-and-roadmap-planning.md`
- **Purpose**: Define MVP scope and create strategic product roadmap
- **Output**: MVP definition, product roadmap, success metrics
- **Usage**: Product strategy, release planning, stakeholder alignment

#### `feature-implementation-from-specification.md`
- **Purpose**: Complete feature implementation with multi-agent coordination
- **Output**: Full-stack feature implementation, testing, documentation
- **Usage**: Complex feature development, cross-team coordination

### Architecture & Design

#### `system-architecture-design.md`
- **Purpose**: Design scalable, maintainable system architecture
- **Output**: Architecture documentation, technology recommendations, implementation roadmap
- **Technologies**: Adapts to any stack (Java/Spring, .NET, Node.js, Python, desktop)
- **Usage**: Technical planning, technology selection, system design

#### `desktop-application-architecture.md`
- **Purpose**: Design cross-platform desktop application architectures
- **Output**: Desktop patterns, UI frameworks, threading implementations
- **Technologies**: Python/wxPython, C++/wxWidgets, .NET/WPF
- **Usage**: Desktop application development, cross-platform solutions

#### `user-research-and-persona-development.md`
- **Purpose**: Conduct user research and create actionable personas
- **Output**: User research reports, personas, journey maps
- **Usage**: User experience planning, design decisions, product strategy

### Frontend Development

#### Framework-Specific Development
- `react-component-development.md` - Modern React with hooks and patterns
- `react-component-development-and-testing.md` - Test-driven React development
- `angular-component-development.md` - Enterprise Angular applications
- `swagger-to-angular-generation.md` - Type-safe Angular services from OpenAPI

#### Modern Web Technologies
- `modern-javascript-and-typescript-development.md` - ES2023+ and TypeScript patterns
- `progressive-web-app-development.md` - PWA with offline functionality
- `responsive-design-and-css-architecture.md` - Modern CSS and design systems
- `web-accessibility-and-inclusive-design.md` - WCAG 2.1 compliance

#### Development Tools & Quality
- `build-tools-and-bundler-optimization.md` - Webpack/Vite optimization
- `frontend-testing-and-quality-assurance.md` - Comprehensive testing strategies
- `state-management-and-data-flow.md` - Modern state management solutions

#### Desktop Development
- `wxwidgets-desktop-development.md` - Cross-platform desktop with wxPython/C++

### API Development

#### API Design & Implementation
- `rest-api-design-and-implementation.md` - Scalable REST API development
- `graphql-api-development.md` - GraphQL with subscriptions and federation
- `microservices-architecture-patterns.md` - Microservices with proven patterns

#### Documentation & Code Generation
- `swagger-documentation-generation.md` - OpenAPI docs from existing code
- `swagger-to-endpoints-generation.md` - API endpoints from OpenAPI specs
- `frontend-backend-integration.md` - Seamless frontend-backend communication

### Data Engineering

#### Database Design & Implementation
- `database-design-and-etl-implementation.md` - Database schemas and ETL pipelines
- `database-to-entityframework-generation.md` - EF Core from database schemas
- `database-backend-integration.md` - Database-API integration patterns
- `desktop-database-integration.md` - Local and remote database integration

### Security Engineering

#### Security Architecture & Planning
- `security-architecture-and-threat-modeling.md` - Comprehensive security design
- `identity-and-access-management.md` - IAM solutions and SSO implementation

#### Security Testing & Analysis
- `penetration-testing-and-security-audit.md` - Security assessments and audits
- `secure-code-review-and-sast.md` - Code security reviews and SAST tools
- `security-vulnerability-assessment.md` - Vulnerability management

#### Compliance & Operations
- `compliance-audit-and-governance.md` - Regulatory compliance frameworks
- `incident-response-and-forensics.md` - Security incident response
- `security-controls-implementation.md` - Security controls and monitoring

### Quality & Testing

#### Quality Assurance
- `test-automation-and-quality-assurance.md` - Comprehensive testing strategies
- `application-performance-optimization.md` - Performance optimization across layers
- `sonarqube-code-quality-analysis.md` - Code quality analysis and improvement

### Deployment & Operations

#### DevOps & Infrastructure
- `ci-cd-pipeline-and-infrastructure-setup.md` - Automated deployment pipelines
- `desktop-deployment-and-packaging.md` - Cross-platform desktop deployment

---

## 🏗️ Core Framework Agents

### Backend Engineering

#### `backend-architecture-design.md`
- **Purpose**: Backend system architecture and service design
- **Output**: Service architecture, API design, database integration
- **Usage**: Backend development, microservices design, system integration

#### `backend-monitoring-logging.md`
- **Purpose**: Backend monitoring and logging infrastructure
- **Output**: Monitoring strategy, logging frameworks, performance tracking
- **Usage**: Production monitoring, debugging, performance optimization

### Database Engineering

#### `database-design-and-etl-implementation.md`
- **Purpose**: Database schema design and ETL pipeline implementation
- **Output**: Database design, data models, ETL processes
- **Usage**: Data architecture, database optimization, data pipeline development

#### `database-to-entityframework-generation.md`
- **Purpose**: Entity Framework code generation from database schema
- **Output**: Entity models, database context, repository patterns
- **Usage**: .NET development, ORM implementation, database integration

#### `database-backend-integration.md`
- **Purpose**: Database integration with backend services
- **Output**: Data access layer, connection management, transaction handling
- **Usage**: Backend development, data persistence, API integration

#### `desktop-database-integration.md`
- **Purpose**: Desktop application database integration
- **Output**: Local database setup, data synchronization, offline capabilities
- **Usage**: Desktop development, local data management, synchronization

### DevOps Architecture

#### `devops-architecture-and-automation.md`
- **Purpose**: DevOps architecture and automation frameworks
- **Output**: DevOps strategy, automation pipelines, infrastructure management
- **Usage**: Infrastructure automation, deployment optimization, operational efficiency

#### `devops-ci-cd-optimization.md`
- **Purpose**: CI/CD pipeline optimization and automation
- **Output**: Optimized pipelines, deployment strategies, quality gates
- **Usage**: DevOps improvement, deployment efficiency, automation enhancement

### Capacity Planning

#### `enterprise-capacity-planning.md`
- **Purpose**: Enterprise-scale capacity planning and resource optimization
- **Output**: Capacity models, resource forecasting, scaling strategies
- **Usage**: Infrastructure planning, cost optimization, performance scaling

#### `performance-capacity-analysis.md`
- **Purpose**: Performance analysis and capacity assessment
- **Output**: Performance metrics, capacity recommendations, optimization plans
- **Usage**: Performance tuning, capacity management, resource optimization

### Governance Architecture

#### `enterprise-governance-frameworks.md`
- **Purpose**: Enterprise governance and compliance frameworks
- **Output**: Governance strategy, compliance processes, risk management
- **Usage**: Corporate governance, regulatory compliance, risk mitigation

#### `technology-governance-and-standards.md`
- **Purpose**: Technology governance and architectural standards
- **Output**: Technology standards, governance processes, compliance frameworks
- **Usage**: Architecture governance, technology oversight, standards enforcement

### Incident Response

#### `incident-response-automation.md`
- **Purpose**: Incident response automation and orchestration
- **Output**: Response procedures, automation workflows, escalation processes
- **Usage**: Incident management, automated response, operational resilience

#### `incident-management-procedures.md`
- **Purpose**: Incident management procedures and coordination
- **Output**: Management processes, communication protocols, resolution procedures
- **Usage**: Incident handling, team coordination, service restoration

### Middleware Engineering

#### `middleware-integration-architecture.md`
- **Purpose**: Middleware architecture and integration patterns
- **Output**: Integration architecture, middleware design, communication patterns
- **Usage**: System integration, middleware implementation, service connectivity

#### `message-queue-and-middleware-optimization.md`
- **Purpose**: Message queue optimization and middleware performance
- **Output**: Optimization strategies, performance tuning, scalability improvements
- **Usage**: Middleware optimization, message processing, system performance

### Risk Management

#### `risk-assessment-and-mitigation.md`
- **Purpose**: Risk assessment and mitigation strategies
- **Output**: Risk analysis, mitigation plans, monitoring frameworks
- **Usage**: Risk management, compliance, strategic planning

#### `risk-monitoring-reporting.md`
- **Purpose**: Risk monitoring and reporting systems
- **Output**: Monitoring systems, reporting frameworks, alert mechanisms
- **Usage**: Continuous risk management, compliance reporting, risk oversight

### Site Reliability Engineering

#### `sre-reliability-engineering.md`
- **Purpose**: Site reliability engineering and operational excellence
- **Output**: SRE practices, reliability frameworks, operational procedures
- **Usage**: Production reliability, operational excellence, service availability

#### `sre-incident-response.md`
- **Purpose**: SRE incident response and postmortem analysis
- **Output**: Response procedures, postmortem processes, improvement plans
- **Usage**: Incident management, continuous improvement, operational learning

### Session Management

#### `session-start-and-context-analysis.md`
- **Purpose**: Session initialization and comprehensive context analysis
- **Output**: Session state, context analysis, project understanding
- **Usage**: Session management, context preservation, project analysis

#### `session-continuation-from-summary.md`
- **Purpose**: Session continuation from previous session summaries
- **Output**: Restored context, continued workflow, project state
- **Usage**: Session recovery, workflow continuation, context restoration

#### `session-end-and-summary-generation.md`
- **Purpose**: Session termination and comprehensive summary generation
- **Output**: Session summary, progress tracking, next steps
- **Usage**: Session closure, progress documentation, handoff preparation

#### `session-state-recovery.md`
- **Purpose**: Session state recovery and context restoration
- **Output**: Recovered state, context restoration, workflow resumption
- **Usage**: Error recovery, session restoration, continuity management

#### `serena-sync-and-update.md`
- **Purpose**: Serena MCP tool synchronization and project updates
- **Output**: Synchronized project state, updated indexing, tool coordination
- **Usage**: MCP integration, project synchronization, tool coordination

---

## 🏢 Enterprise-Scale Agents

### Enterprise Architecture

#### `enterprise-architecture-strategy.md`
- **Purpose**: Enterprise architecture strategy and governance frameworks
- **Output**: Enterprise strategy, governance processes, technology roadmaps
- **Usage**: Digital transformation, enterprise planning, architectural governance

#### `digital-transformation-planning.md`
- **Purpose**: Digital transformation planning and implementation strategies
- **Output**: Transformation roadmap, capability development, change management
- **Usage**: Organizational modernization, technology adoption, business transformation

#### `technology-governance-frameworks.md`
- **Purpose**: Technology governance and standards management
- **Output**: Governance frameworks, compliance systems, standards enforcement
- **Usage**: Technology oversight, risk management, regulatory compliance

### Cloud Engineering

#### `cloud-cost-optimization.md`
- **Purpose**: Cloud cost analysis and optimization strategies
- **Output**: Cost optimization plan, resource right-sizing, financial governance
- **Usage**: Cloud financial management, cost reduction, resource optimization

#### `cloud-migration-strategy.md`
- **Purpose**: Cloud migration planning and execution strategies
- **Output**: Migration roadmap, risk assessment, migration execution plan
- **Usage**: Cloud adoption, legacy modernization, infrastructure migration

#### `cloud-serverless-architecture.md`
- **Purpose**: Serverless architecture design and implementation
- **Output**: Serverless architecture, event-driven systems, scaling strategies
- **Usage**: Modern cloud architecture, cost-effective scaling, event processing

#### `cloud-multi-cloud-management.md`
- **Purpose**: Multi-cloud strategy and management frameworks
- **Output**: Multi-cloud architecture, vendor management, integration strategies
- **Usage**: Cloud diversification, vendor risk mitigation, hybrid cloud solutions

### Performance Engineering

#### `application-performance-optimization.md`
- **Purpose**: Application performance analysis and optimization
- **Output**: Performance optimization plan, bottleneck analysis, improvement strategies
- **Usage**: Performance tuning, scalability improvement, user experience enhancement

#### `scalability-testing-and-load-analysis.md`
- **Purpose**: Scalability testing and load analysis frameworks
- **Output**: Load testing strategy, scalability assessment, capacity planning
- **Usage**: Performance validation, capacity planning, scalability assurance

#### `system-optimization.md`
- **Purpose**: System-wide optimization and efficiency improvement
- **Output**: System optimization plan, resource efficiency, performance enhancement
- **Usage**: Infrastructure optimization, cost reduction, performance improvement

### Automation Engineering

#### `business-process-automation.md`
- **Purpose**: Business process automation and workflow optimization
- **Output**: Process automation strategy, workflow optimization, efficiency improvement
- **Usage**: Process modernization, operational efficiency, automation implementation

#### `deployment-automation-and-ci-cd.md`
- **Purpose**: Deployment automation and CI/CD pipeline implementation
- **Output**: CI/CD strategy, automation frameworks, deployment optimization
- **Usage**: DevOps implementation, deployment efficiency, quality automation

#### `infrastructure-automation.md`
- **Purpose**: Infrastructure automation and management frameworks
- **Output**: Infrastructure as code, automation strategies, operational efficiency
- **Usage**: Infrastructure management, operational automation, resource optimization

### Mobile Development

#### `mobile-app-development.md`
- **Purpose**: Mobile application development and lifecycle management
- **Output**: Mobile development strategy, platform optimization, deployment planning
- **Usage**: Mobile app development, platform-specific optimization, mobile DevOps

#### `cross-platform-development.md`
- **Purpose**: Cross-platform mobile development and optimization
- **Output**: Cross-platform strategy, code sharing optimization, platform integration
- **Usage**: Multi-platform development, development efficiency, platform consistency

### Data Science & Analytics

#### `machine-learning.md`
- **Purpose**: Machine learning implementation and model development
- **Output**: ML strategy, model development, deployment automation, performance monitoring
- **Usage**: AI implementation, predictive analytics, intelligent automation

#### `predictive-analytics.md`
- **Purpose**: Predictive analytics and forecasting systems
- **Output**: Forecasting models, analytics strategy, business intelligence frameworks
- **Usage**: Business forecasting, trend analysis, data-driven decision making

#### `data-analysis.md`
- **Purpose**: Data analysis and statistical modeling frameworks
- **Output**: Analysis strategy, statistical models, business insights
- **Usage**: Data exploration, business intelligence, analytical reporting

### Infrastructure & Operations

#### Network Architecture
- `enterprise-network-design-and-topology.md` - Enterprise network design and topology planning
- `network-infrastructure-planning.md` - Network infrastructure planning and optimization
- `network-security-architecture.md` - Network security architecture and protection strategies
- `network-performance-optimization.md` - Network performance optimization and monitoring

#### Platform Engineering
- `internal-developer-platform-design.md` - Internal developer platform design and implementation
- `developer-experience-optimization.md` - Developer experience optimization and productivity enhancement
- `platform-engineering-automation.md` - Platform automation and developer tooling

#### Reliability Engineering
- `chaos-engineering-and-resilience-testing.md` - Chaos engineering and system resilience testing
- `performance-monitoring-and-observability.md` - Performance monitoring and observability frameworks
- `system-reliability-engineering.md` - System reliability engineering and SRE practices

#### Technical Documentation
- `technical-documentation-systems.md` - Technical documentation systems and standards
- `api-documentation-and-developer-resources.md` - API documentation and developer resource management
- `knowledge-management-systems.md` - Knowledge management and documentation automation

### Monitoring & Compliance

#### Infrastructure Monitoring
- `infrastructure-monitoring.md` - Infrastructure monitoring and alerting systems
- `application-monitoring.md` - Application performance monitoring and observability
- `alerting-systems.md` - Alerting systems and incident response automation

#### Compliance & Risk Management
- `audit-preparation.md` - Audit preparation and compliance management
- `risk-assessment.md` - Risk assessment and mitigation strategies
- `regulatory-compliance.md` - Regulatory compliance and governance frameworks

### Integration & Coordination

#### Enterprise Integration
- `enterprise-integration-patterns.md` - Enterprise integration patterns and architecture design
- `system-integration.md` - System integration and connectivity management

#### Project Coordination
- `team-coordination.md` - Team coordination and collaboration management
- `project-management.md` - Project management and execution coordination

---

## 🔄 Session Management

The framework includes comprehensive session management for seamless development continuity:

### Core Session Prompts

#### `session-start-and-context-analysis.md`
- **Purpose**: Initialize development sessions with intelligent context analysis
- **Features**: Project detection, technology stack analysis, team coordination
- **Output**: Session context, development strategy, agent recommendations

#### `session-continuation-from-summary.md`
- **Purpose**: Resume work from previous session summaries
- **Features**: Context restoration, progress tracking, seamless continuation
- **Input**: Session summary from previous work
- **Output**: Restored context, updated strategy, next steps

#### `session-end-and-summary-generation.md`
- **Purpose**: Document session outcomes and prepare for future continuation
- **Features**: Progress summarization, achievement tracking, handoff preparation
- **Output**: Comprehensive session summary, continuation instructions

#### `session-state-recovery.md`
- **Purpose**: Emergency session recovery after unexpected interruptions
- **Features**: State analysis, context reconstruction, recovery procedures
- **Usage**: System crashes, network interruptions, context loss scenarios

#### `serena-sync-and-update.md`
- **Purpose**: Integration with MCP tools (Serena, Context7, Playwright)
- **Features**: Tool detection, synchronization, enhanced capabilities
- **Benefits**: Extended functionality when MCP tools are available

---

## 🎬 Project Initialization

Complete project setup automation from concept to production-ready configuration:

### Initialization Workflow

#### `claude_md_from_concept.md`
- **Purpose**: Generate complete CLAUDE.md from project concept materials
- **Input**: Files in `init_concept/` directory (ideas, requirements, preferences)
- **Process**: Technology detection, scale assessment, configuration generation
- **Output**: Production-ready CLAUDE.md with all sections populated

#### `prepare_instruction.md`
- **Purpose**: Create development roadmap from CLAUDE.md configuration
- **Input**: Existing CLAUDE.md configuration
- **Process**: Strategy generation, agent sequencing, TODO setup
- **Output**: Phase-by-phase development guide with agent coordination

#### `new-project.md`
- **Purpose**: Initialize framework for brand new projects
- **Process**: Project creation, structure setup, tool integration
- **Output**: Complete project foundation with framework integration

#### `existing-project.md`
- **Purpose**: Safely integrate framework with existing codebases
- **Process**: Analysis, safe integration, value-added enhancement
- **Guarantee**: No modification of existing source files

### Initialization Best Practices

1. **Concept Preparation**: Create clear project descriptions in `init_concept/`
2. **Technology Preferences**: Specify preferred frameworks and tools
3. **Scale Definition**: Define project complexity (startup/SME/enterprise)
4. **Team Structure**: Outline development team composition
5. **Business Context**: Provide domain and business requirements

---

## 📊 Project Management

Comprehensive project management and maintenance prompts for framework operations:

### Core Project Management

#### `project-health-check.md`
- **Purpose**: Comprehensive project health assessment and analysis
- **Features**: Code quality analysis, security scanning, documentation validation
- **Output**: Health reports, improvement recommendations, quality metrics
- **Usage**: Regular project monitoring, pre-deployment validation

#### `project-health-check-pro.md`
- **Purpose**: Advanced project health analysis with strategic assessment
- **Features**: Enterprise-grade analytics, predictive analysis, strategic recommendations
- **Output**: Executive summaries, trend analysis, strategic planning reports
- **Usage**: Executive reporting, long-term planning, enterprise governance

### Documentation Management

#### `update-documentation-comprehensive.md`
- **Purpose**: Comprehensive project documentation synchronization
- **Features**: Multi-format documentation updates, consistency validation, automated sync
- **Output**: Updated documentation, sync reports, consistency validation
- **Usage**: Documentation maintenance, release preparation, knowledge management

#### `documentation-consistency-validator.md`
- **Purpose**: Project documentation consistency validation and synchronization
- **Features**: Cross-reference validation, format consistency, content alignment
- **Output**: Consistency reports, validation results, correction recommendations
- **Usage**: Quality assurance, documentation audits, standard compliance

### Release Management

#### `update-changelog-and-version.md`
- **Purpose**: Project versioning and change documentation management
- **Features**: Automated changelog generation, semantic versioning, release notes
- **Output**: Updated changelogs, version tags, release documentation
- **Usage**: Release preparation, version control, change tracking

#### `project-release-preparation.md`
- **Purpose**: Project release preparation and deployment readiness
- **Features**: Pre-release validation, deployment checklists, quality gates
- **Output**: Release readiness reports, deployment plans, quality validation
- **Usage**: Release management, deployment planning, quality assurance

### Framework Enhancement

#### `framework-enhancement-implementation.md`
- **Purpose**: Framework enhancement and feature implementation
- **Features**: Modular enhancement development, compatibility testing, integration validation
- **Output**: Enhanced framework features, compatibility reports, integration guides
- **Usage**: Framework development, feature additions, capability expansion

#### `project-structure-modernization.md`
- **Purpose**: Project structure modernization and optimization
- **Features**: Structure analysis, modernization recommendations, migration planning
- **Output**: Modernization plans, migration guides, optimization reports
- **Usage**: Legacy modernization, structure optimization, technology updates

---

## 🔄 Workflow Orchestration

Multi-agent coordination and workflow management for complex development scenarios:

### Phase Transitions

#### `business-requirements-to-architecture-handoff.md`
- **Purpose**: Seamless handoff from business analysis to technical architecture
- **Agents**: business-analyst → software-architect
- **Output**: Technical requirements, architecture constraints, design criteria

#### `architecture-design-to-development-handoff.md`
- **Purpose**: Translation of architecture to development implementation
- **Agents**: software-architect → implementation agents
- **Output**: Implementation guidelines, technical specifications, development tasks

### Parallel Coordination

#### `cross-team-development-coordination.md`
- **Purpose**: Coordinate parallel development across multiple teams/agents
- **Features**: Dependency management, integration planning, conflict resolution
- **Usage**: Large features, multi-component development, team synchronization

### Development Scenarios

#### `new-feature-development-orchestration.md`
- **Purpose**: Complete feature development lifecycle orchestration
- **Phases**: Requirements → Design → Development → Testing → Deployment
- **Coordination**: Multi-agent workflow with quality gates

#### `critical-bug-fix-orchestration.md`
- **Purpose**: Emergency bug fix coordination with minimal disruption
- **Features**: Rapid analysis, coordinated fix, validation, deployment
- **Priority**: Critical system issues, security vulnerabilities

### TODO Management Orchestration

#### `epic-breakdown-orchestration.md`
- **Purpose**: Break down large initiatives into manageable tasks
- **Hierarchy**: Epic → Feature → Task → Subtask
- **Coordination**: Agent responsibility assignment, dependency tracking

#### `comprehensive-todo-orchestration.md`
- **Purpose**: Enterprise-grade TODO management across all agents
- **Features**: Hierarchical tracking, progress monitoring, automated handoffs
- **Integration**: TodoWrite tool coordination, CLAUDE.md configuration

### Quality Gates

#### `todo-integrated-quality-gates.md`
- **Purpose**: Quality validation checkpoints integrated with TODO management
- **Features**: Automated quality checks, gate enforcement, progression control
- **Usage**: Phase transitions, deployment readiness, quality assurance

#### `cross-agent-todo-validation.md`
- **Purpose**: Validate TODO completion and quality across agent boundaries
- **Features**: Cross-agent validation, handoff verification, quality metrics
- **Benefits**: Consistent quality, seamless transitions, accountability

---

## 📝 Creating Custom Prompts

The framework includes a comprehensive template for creating custom prompts that follow functional design principles:

### Using the Prompt Template

#### Step 1: Copy the Template
```bash
cp .claude/prompts/PROMPT_TEMPLATE.md .claude/prompts/agents/[category]/my-custom-prompt.md
```

#### Step 2: Replace Placeholders
The template uses bracket notation for easy customization:

```markdown
**Agent: [AGENT_NAME]**
**Purpose: [ONE_LINE_DESCRIPTION_OF_WHAT_THIS_PROMPT_ACCOMPLISHES]**

## 1. FUNCTIONAL REQUIREMENTS
- **Primary Objective**: [MAIN_BUSINESS_GOAL_THIS_PROMPT_SERVES]
- **Success Outcomes**: [LIST_OF_MEASURABLE_OUTCOMES]
- **Business Value**: [WHY_THIS_PROMPT_MATTERS_FOR_PROJECT]
```

#### Step 3: Follow the 4-Component Structure

**1. FUNCTIONAL REQUIREMENTS** - What needs to be accomplished
- Define business objectives and outcomes
- Focus on WHAT, not HOW
- Ensure measurable success criteria

**2. HIGH-LEVEL ALGORITHMS** - How to approach the problem
- Break down into logical phases
- Use technology-agnostic algorithms
- Provide step-by-step process framework

**3. VALIDATION CRITERIA** - What conditions must be met
- Define measurable success conditions
- Include quality gates and acceptance criteria
- Specify business validation requirements

**4. USAGE EXAMPLES** - For different scenarios
- Provide concrete examples for different technology stacks
- Show adaptability across project types and scales
- Demonstrate real-world project scenarios

### Code Inclusion Rules

Code examples are acceptable when properly labeled and structured:

#### ✅ Acceptable Code Categories

**1. Configuration Templates**
```markdown
[TEMPLATE - ADAPT TO YOUR PROJECT]
FROM node:18
WORKDIR /app
# Customize based on your project structure
```

**2. Pattern Examples**
```markdown
[PATTERN EXAMPLE - CUSTOMIZE FOR YOUR NEEDS]
const Component: React.FC = () => {
  // Your implementation here
}
```

**3. Generic Utilities**
```markdown
[UTILITY TEMPLATE - ADAPT TO YOUR STACK]
function validateEmail(email: string): boolean {
  // Universal validation logic
}
```

**4. Common Universal Templates**
```markdown
[COMMON TEMPLATE - STANDARD INDUSTRY PATTERN]
# .gitignore template
node_modules/
*.log
.env
```

**5. User-Requested Code Templates**
```markdown
[USER-REQUESTED TEMPLATE - CUSTOMIZE AS NEEDED]
// User requested authentication middleware example
const authMiddleware = (req, res, next) => {
  // Implement based on your auth strategy
}
```

#### Mandatory Conditions for Code

- **Clear labeling** as TEMPLATE/PATTERN/EXAMPLE/UTILITY/COMMON/USER-REQUESTED
- **Adaptation instructions** - how to customize for specific projects
- **Genericity** - doesn't assume specific project structure
- **Optional nature** - prompt works without the code
- **User context** - for User-Requested, must be response to explicit request

### Quality Validation Checklist

Before submitting your custom prompt:

- [ ] **Agent Assignment**: Assigned to appropriate specialized agent
- [ ] **Purpose Statement**: Clear one-line business purpose
- [ ] **4-Component Structure**: All sections completed
- [ ] **Functional Approach**: Describes WHAT, not HOW
- [ ] **Technology Agnostic**: Works across different stacks
- [ ] **CLAUDE.md Integration**: References project configuration
- [ ] **Measurable Criteria**: Clear, testable success conditions
- [ ] **No Hardcoded Paths**: No specific file/directory assumptions
- [ ] **No Technology Lock-in**: No framework assumptions without detection
- [ ] **Clear Examples**: Cross-technology adaptability demonstrated

---

## 🔧 Integration with Claude Code

### Using Prompts in Claude Code

#### 1. Session-Level Integration
```bash
# Start Claude Code in project directory
claude-code

# Session management happens automatically:
# - Context analysis and project detection
# - Technology stack identification
# - Agent coordination setup
# - TODO management initialization
```

#### 2. Agent-Specific Workflows
```bash
# Reference prompts by path
# Example: .claude/prompts/agents/frontend/react-component-development.md

# Agents automatically:
# - Read CLAUDE.md configuration
# - Adapt to detected technology stack
# - Use TodoWrite for task management
# - Coordinate with other agents
```

#### 3. TODO-Driven Workflow
```bash
# Framework provides hierarchical TODO management:
# - Session-level: TodoWrite tool for immediate tasks
# - Project-level: CLAUDE.md configuration for long-term tracking
# - Agent-level: Specialized TODO responsibilities
# - Workflow-level: Cross-agent coordination
```

### Integration with AI Tools

#### Serena (Project Navigation)
- **Use cases**: Navigating existing codebases, precise code modifications, debugging
- **Integration**: Automatic detection and enhanced capabilities when available
- **Fallback**: Framework works without Serena, with reduced navigation features

#### Context7 (Code Generation)
- **Use cases**: Generating new code, comprehensive documentation, large transformations
- **Integration**: Enhanced code generation capabilities when available
- **Fallback**: Standard Claude Code generation with manual guidance

#### Playwright (Web Automation)
- **Use cases**: End-to-end testing, web scraping, browser automation
- **Integration**: Automated testing and validation workflows
- **Fallback**: Manual testing procedures and alternative tools

---

## ✅ Quality Standards

### Framework Quality Principles

#### 1. Functional Design Compliance
- **Zero Hardcoding**: No assumptions about specific file paths or directory structures
- **Technology Agnostic**: Works across different technology stacks without modification
- **Runtime Detection**: All technology assumptions detected dynamically
- **Graceful Degradation**: Functions correctly even when external tools unavailable

#### 2. Measurable Success Criteria
- **Clear Objectives**: Every prompt defines measurable business outcomes
- **Validation Gates**: Specific criteria for task completion and quality
- **Progress Tracking**: Integrated with TodoWrite and hierarchical management
- **Quality Metrics**: Quantifiable measures of success and improvement

#### 3. Cross-Technology Compatibility
- **Stack Adaptation**: Prompts automatically adapt to detected technology stack
- **Framework Flexibility**: Works with any combination of frontend/backend/database
- **Tool Integration**: Seamless integration with existing development tools
- **Legacy Support**: Safe integration with existing codebases and workflows

#### 4. Enterprise Scalability
- **Project Scale Adaptation**: Adjusts complexity based on startup/SME/enterprise scale
- **Team Coordination**: Multi-agent workflows with clear handoff procedures
- **Quality Assurance**: Comprehensive validation and continuous improvement
- **Documentation Standards**: Complete documentation with clear examples

### Quality Assurance Process

#### 1. Prompt Validation
- **Structure Compliance**: 4-component mandatory structure verified
- **Functional Design**: No hardcoding violations detected
- **Technology Testing**: Validated across multiple technology stacks
- **Integration Testing**: Verified compatibility with other framework components

#### 2. Cross-Stack Testing
- **Technology Matrices**: Tested with various frontend/backend/database combinations
- **Scale Validation**: Verified with startup, SME, and enterprise project configurations
- **Tool Compatibility**: Tested with and without optional MCP tools
- **Performance Testing**: Validated performance impact and optimization

#### 3. Documentation Quality
- **Completeness**: All prompts fully documented with examples
- **Accuracy**: Documentation matches actual prompt behavior
- **Clarity**: Clear instructions for usage and customization
- **Maintenance**: Regular updates to reflect framework evolution

---

## 💡 Best Practices

### For Prompt Usage

#### 1. Session Management
- **Always start** with session-start-and-context-analysis.md for new work
- **Use continuation** prompts when resuming previous work
- **End sessions properly** with summary generation for future reference
- **Recover gracefully** using state recovery when needed

#### 2. Agent Coordination
- **Follow phase sequences** from business → architecture → development → deployment
- **Use handoff prompts** for seamless transitions between agents
- **Leverage parallel coordination** for complex multi-component development
- **Validate quality gates** before proceeding to next phase

#### 3. TODO Management
- **Configure hierarchy** in CLAUDE.md based on project complexity
- **Use TodoWrite tool** for session-level task tracking
- **Coordinate handoffs** through TODO status updates
- **Track progress** across all agents and workflow phases

### For Custom Prompt Development

#### 1. Design Principles
- **Start with business value** - define clear business objectives
- **Use algorithmic thinking** - break down into logical phases
- **Provide multiple examples** - show adaptability across stacks
- **Include validation criteria** - define measurable success

#### 2. Technology Adaptation
- **Detect, don't assume** - always detect technology stack dynamically
- **Provide fallbacks** - work even when preferred tools unavailable
- **Test across stacks** - validate with different technology combinations
- **Document adaptations** - show how prompt adapts to different contexts

#### 3. Integration Considerations
- **Define collaboration points** - specify how prompt works with others
- **Use shared resources** - leverage TodoWrite, CLAUDE.md, session state
- **Plan handoffs** - clear procedures for agent coordination
- **Validate integration** - test compatibility with framework workflows

### For Framework Maintenance

#### 1. Quality Monitoring
- **Regular validation** - periodic testing across technology stacks
- **Performance monitoring** - track framework efficiency and bottlenecks
- **User feedback** - incorporate feedback from development teams
- **Continuous improvement** - regular updates and enhancements

#### 2. Documentation Maintenance
- **Keep current** - update documentation with framework changes
- **Expand examples** - add new technology stack examples as needed
- **Clarify usage** - improve instructions based on user experience
- **Validate accuracy** - ensure documentation matches implementation

#### 3. Framework Evolution
- **Backward compatibility** - maintain compatibility with existing projects
- **Progressive enhancement** - add new capabilities without breaking changes
- **Standard compliance** - maintain adherence to functional design principles
- **Community feedback** - incorporate suggestions and improvements

---

## 📚 Additional Resources

### Framework Documentation
- **Main README**: `/README.md` - Project overview and getting started
- **Framework Specification**: `/CLAUDE.md` - Complete framework configuration
- **Agent Specifications**: `/.claude/agents/` - Individual agent capabilities
- **Workflow Diagrams**: `/.claude/docs/agent-sdlc-workflow.puml` - Visual workflows

### Integration Guides
- **TodoWrite Integration**: Section 8 in CLAUDE.md for configuration
- **Session Management**: Advanced state preservation and context analysis
- **MCP Tools Usage**: Serena, Context7, and Playwright integration
- **Quality Gates**: Validation procedures and quality assurance

### Development Support
- **Prompt Template**: `PROMPT_TEMPLATE.md` - Create custom prompts
- **Examples**: `/examples/` - Real-world framework implementations
- **Version History**: `/CHANGELOG.md` - Framework evolution and updates

---

**Framework Status**: Production Ready ✅
**Quality Compliance**: 100% Functional Design Adherence
**Technology Coverage**: Universal Stack Compatibility
**Enterprise Ready**: Scalable Architecture and Quality Assurance

*The Claude Code Multi-Agent Framework prompts library enables consistent, high-quality software development across diverse projects while maintaining business focus and technical excellence.*