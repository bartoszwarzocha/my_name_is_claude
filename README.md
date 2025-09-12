# My Name Is Claude

## Claude Code Multi-Agent Framework & Comprehensive Prompts Library

A comprehensive workspace template for Claude Code projects, optimized for efficient multi-agent collaboration, parallel work execution, and production-ready development workflows. This framework includes an extensive library of 33 specialized agent prompts with comprehensive coverage for security and frontend engineering.

**🔗 Repository:** [https://github.com/your-username/my_claude](https://github.com/your-username/my_claude)

Inspired by: [Claude AI](https://claude.ai), [Serena](https://serena.ai), [Context7](https://context7.ai), https://github.com/coleam00/context-engineering-intro.git and https://github.com/lausena/my_awesome_crm.git

## 📑 Table of Contents

- [📋 Project Description](#-project-description)
- [🎯 Main Goals](#-main-goals)
- [🏗️ Project Structure](#️-project-structure)
- [🤖 Available Agents & Specializations](#-available-agents--specializations)
  - [📋 Phase 1: Business Discovery & Analysis](#-phase-1-business-discovery--analysis)
  - [🏗️ Phase 2: Architecture & UX Design](#️-phase-2-architecture--ux-design)
  - [💻 Phase 3: Development & Continuous QA](#-phase-3-development--continuous-qa)
  - [🚀 Phase 4: Deployment & Operations](#-phase-4-deployment--operations)
- [📊 Prompts Library Overview](#-prompts-library-overview)
- [🛠️ Framework Features](#️-framework-features)
  - [⚡ Advanced Multi-Agent Orchestration](#-advanced-multi-agent-orchestration)
  - [🔄 Production-Ready Prompts](#-production-ready-prompts)
  - [🌐 Technology Stack Flexibility](#-technology-stack-flexibility)
  - [🔧 Comprehensive Automation Hooks](#-comprehensive-automation-hooks)
  - [🗃️ Enterprise Database Management](#️-enterprise-database-management)
- [🚀 Getting Started](#-getting-started)
- [📝 Usage Examples & Scenarios](#-usage-examples--scenarios)
- [⚙️ Advanced Configuration](#️-advanced-configuration)
- [🤝 Best Practices](#-best-practices)
- [🔧 Troubleshooting & Support](#-troubleshooting--support)
- [📚 Documentation & Resources](#-documentation--resources)
- [🤝 Contributing and Development](#-contributing-and-development)
- [📄 License & Usage](#-license--usage)
- [🎉 Summary & Impact](#-summary--impact)

## 📋 Project Description

This repository contains a production-ready Claude Code Agent Framework with a comprehensive prompts library, configuration templates, and multi-agent orchestration system. The framework transforms software development through systematic agent collaboration, implementing enterprise-grade development lifecycle management with specialized expertise in each domain.

**Key Innovation:** Comprehensive prompt library featuring complete security-engineer (7 prompts) and frontend-engineer (11 prompts) coverage, plus advanced workflow orchestration scenarios.

## 🎯 Main Goals

- **Agent-Driven Development:** Revolutionary approach using 11 specialized AI agents for complete software lifecycle
- **Production Readiness:** Enterprise-grade prompts with real working code examples and advanced patterns
- **Systematic Workflows:** Orchestrated multi-agent collaboration with quality gates and phase transitions
- **Technology Excellence:** Deep expertise in modern technology stacks (Angular, wxWidgets, security, infrastructure)
- **Scalable Architecture:** Adaptable framework supporting projects from startups to enterprise scale

## 🏗️ Project Structure

```text
my_claude/
├── .claude/                                    # Claude Code configuration
│   ├── agents/                                 # 11 specialized agent definitions
│   │   ├── api/                               # API engineer agent
│   │   ├── architecture/                      # Software architect agent
│   │   ├── business/                          # Business analyst agent
│   │   ├── data/                             # Data engineer agent
│   │   ├── deployment/                        # Deployment engineer agent
│   │   ├── design/                           # UX/UI designer agent
│   │   ├── frontend/                         # Frontend engineer agent
│   │   ├── planner/                          # Product manager agent
│   │   ├── quality/                          # QA engineer agent
│   │   ├── review/                           # Reviewer agent
│   │   └── security/                         # Security engineer agent
│   │
│   ├── prompts/                              # ⭐ Comprehensive Prompts Library
│   │   ├── agents/                           # 33 specialized agent prompts
│   │   │   ├── api/                         # 3 API engineering prompts
│   │   │   ├── architecture/                # 1 system architecture prompt
│   │   │   ├── business/                    # 3 business analysis prompts
│   │   │   ├── data/                        # 1 data engineering prompt
│   │   │   ├── deployment/                  # 1 deployment engineering prompt
│   │   │   ├── design/                      # 1 UX design prompt
│   │   │   ├── frontend/                    # ✅ 11 frontend prompts
│   │   │   ├── product/                     # 2 product management prompts
│   │   │   ├── quality/                     # 1 QA engineering prompt
│   │   │   ├── review/                      # 2 review & validation prompts
│   │   │   └── security/                    # ✅ 7 complete security prompts
│   │   ├── workflows/                       # Multi-agent orchestration prompts
│   │   └── README.md                        # Complete prompts documentation
│   │
│   ├── templates/                           # Reusable templates and patterns
│   ├── hooks/                              # 🔧 Automation hooks (11 hooks)
│   └── docs/                               # Framework documentation
│
├── CLAUDE.md                               # Main project configuration
├── DATABASE_CONNECTIONS.md                 # Database configurations
└── README.md                              # This comprehensive guide
```

## 🤖 Available Agents & Specializations

### 📋 Phase 1: Business Discovery & Analysis

#### **Business Analyst**

- **Role:** Requirements analysis and process optimization
- **Competencies:** Stakeholder management, process modeling, requirements documentation, business case development
- **Focus:** Business process excellence and stakeholder alignment
- **Available Prompts:** 3 prompts (stakeholder-requirements-gathering, current-state-process-analysis, business-case-development)

#### **Product Manager**

- **Role:** Product strategy and user-centric solutions
- **Competencies:** Market analysis, UX research, roadmaps, user story creation, MVP scoping
- **Focus:** Business value delivery and product strategy
- **Available Prompts:** 2 prompts (user-story-creation-and-prioritization, mvp-scoping-and-roadmap-planning)

#### **Reviewer**

- **Role:** Quality assurance and validation
- **Competencies:** Requirements validation, code quality analysis, security vulnerability assessment
- **Focus:** Completeness, quality, and business alignment
- **Available Prompts:** 2 prompts (sonarqube-code-quality-analysis, security-vulnerability-assessment)

### 🏗️ Phase 2: Architecture & UX Design

#### **Software Architect**

- **Role:** System architecture design and technology selection
- **Competencies:** Scalable solutions, architectural patterns, technology stack selection, system design
- **Focus:** Long-term maintainability, performance, and scalability
- **Available Prompts:** 1 prompt (system-architecture-design)

#### **UX/UI Designer**

- **Role:** User experience and interface design
- **Competencies:** User research, persona development, design systems, accessibility, prototyping
- **Focus:** User-centered design and inclusive experiences
- **Available Prompts:** 1 prompt (user-research-and-persona-development)

#### **Security Engineer**

- **Role:** Security architecture and compliance
- **Competencies:** Threat modeling, penetration testing, compliance audits, incident response, IAM, secure code review
- **Focus:** Security-first development and regulatory compliance
- **Available Prompts:** 7 prompts (security-architecture-and-threat-modeling, penetration-testing-and-security-audit, compliance-audit-and-governance, incident-response-and-forensics, security-controls-implementation, identity-and-access-management, secure-code-review-and-sast)

### 💻 Phase 3: Development & Continuous QA

#### **Frontend Engineer**

- **Role:** User interface development with modern frameworks
- **Competencies:** Angular 17+ development, wxWidgets desktop apps, responsive design, TypeScript mastery, PWA development, accessibility compliance, state management, build optimization, comprehensive testing
- **Focus:** User experience excellence, accessibility, and technical excellence
- **Available Prompts:** 11 prompts (angular-component-development, wxwidgets-desktop-development, responsive-design-and-css-architecture, modern-javascript-and-typescript-development, progressive-web-app-development, web-accessibility-and-inclusive-design, state-management-and-data-flow, build-tools-and-bundler-optimization, frontend-testing-and-quality-assurance, react-component-development, react-component-development-and-testing)
- **Technologies:** Angular 17+, React, wxPython, TypeScript, RxJS, CSS Architecture, PWA, WCAG 2.1

#### **API Engineer**

- **Role:** API and microservices development
- **Competencies:** RESTful APIs, GraphQL development, microservices architecture, service integration, API security
- **Focus:** API excellence, service reliability, and integration quality
- **Available Prompts:** 3 prompts (rest-api-design-and-implementation, microservices-architecture-patterns, graphql-api-development)

#### **Data Engineer**

- **Role:** Data architecture and analytics
- **Competencies:** Database design, ETL pipelines, data processing, business intelligence, data quality frameworks
- **Focus:** Data reliability, performance optimization, and analytics excellence
- **Available Prompts:** 1 prompt (database-design-and-etl-implementation)

#### **QA Engineer**

- **Role:** Quality assurance and test automation
- **Competencies:** Test automation, performance testing, quality processes, comprehensive testing strategies
- **Focus:** Quality-first development and continuous improvement
- **Available Prompts:** 1 prompt (test-automation-and-quality-assurance)

### 🚀 Phase 4: Deployment & Operations

#### **Deployment Engineer**

- **Role:** DevOps and infrastructure management
- **Competencies:** CI/CD pipelines, cloud infrastructure, monitoring, automation, scalable infrastructure
- **Focus:** Zero-downtime deployments and enterprise reliability
- **Available Prompts:** 1 prompt (ci-cd-pipeline-and-infrastructure-setup)

## 📊 Prompts Library Overview

### Available Prompts by Agent

| Phase | Agent | Available Prompts | Specializations |
|-------|-------|-------------------|-----------------|
| **Phase 1** | business-analyst | 3 prompts | Stakeholder requirements, process analysis, business cases |
| **Phase 1** | product-manager | 2 prompts | User story creation, MVP scoping and roadmaps |
| **Phase 1** | reviewer | 2 prompts | Code quality analysis, security vulnerability assessment |
| **Phase 2** | software-architect | 1 prompt | System architecture design |
| **Phase 2** | ux-designer | 1 prompt | User research and persona development |
| **Phase 2** | security-engineer | 7 prompts | Complete security coverage: threat modeling, penetration testing, compliance |
| **Phase 3** | frontend-engineer | 11 prompts | Complete frontend coverage: Angular, React, wxWidgets, PWA, accessibility |
| **Phase 3** | api-engineer | 3 prompts | REST API design, microservices, GraphQL development |
| **Phase 3** | data-engineer | 1 prompt | Database design and ETL implementation |
| **Phase 3** | qa-engineer | 1 prompt | Test automation and quality assurance |
| **Phase 4** | deployment-engineer | 1 prompt | CI/CD pipeline and infrastructure setup |

**📈 Total Available:** 33 specialized prompts

**🌟 Comprehensive Coverage Areas:**
- **Security Engineering:** Complete enterprise security workflow coverage
- **Frontend Development:** Full-stack frontend development with modern frameworks
- **Business Analysis:** Core business discovery and requirements processes

## 🛠️ Framework Features

### ⚡ Advanced Multi-Agent Orchestration

- **Phase-Based Workflow:** 5-phase software development lifecycle with systematic transitions
- **Parallel Execution:** Optimized for concurrent agent work with minimal conflicts
- **Quality Gates:** Built-in validation checkpoints between phases
- **Agent Coordination:** Sophisticated handoff protocols and collaboration patterns

### 🔄 Production-Ready Prompts

- **Expert-Level Content:** Each prompt contains actual working code examples
- **Enterprise Patterns:** Advanced architectural patterns and best practices
- **Technology Mastery:** Deep specialization in modern technology stacks
- **Comprehensive Coverage:** Complete workflows from analysis to deployment

### 🌐 Technology Stack Flexibility

- **Frontend Excellence:** Complete Angular 17+ and wxWidgets desktop development
- **Security Focus:** Comprehensive security engineering with 7 specialized prompts
- **Modern JavaScript/TypeScript:** ES2023+ features and advanced patterns
- **Cross-Platform:** Web applications, desktop applications, and mobile PWAs

### 🔧 Comprehensive Automation Hooks

- **11 Specialized Hooks:** Complete automation for multi-agent workflows
- **Quality Assurance:** Automated validation for prompts, dependencies, and compliance
- **Performance Monitoring:** Real-time tracking of agent execution and bottleneck identification
- **Conflict Resolution:** Proactive detection and resolution of agent conflicts
- **Compliance Automation:** WCAG 2.1, GDPR, and SOX compliance validation

### 🗃️ Enterprise Database Management

- **Multiple Environments:** WSL, Docker, cloud configurations
- **Connection Patterns:** Standardized database connection templates
- **Migration Support:** Database schema evolution and ETL pipelines

## 🚀 Getting Started

### 1. Repository Setup

```bash
# Clone the repository
git clone https://github.com/your-username/my_name_is_claude.git
cd my_name_is_claude

# Or copy template for new project
cp -r my_name_is_claude/ my_new_project/
cd my_new_project/
```

### 2. Project Configuration

#### Configure Main Project File

Edit `CLAUDE.md` to match your project requirements:

```markdown
# Update these sections:
- Technology stack (Angular, wxWidgets, etc.)
- Business domain and goals
- Agent specializations needed
- Project-specific requirements
```

#### Setup Database Connections (if needed)

Customize `DATABASE_CONNECTIONS.md` 

### 3. Launch Claude Code

```bash
# Navigate to project directory
cd /path/to/your/project

# Launch Claude Code
claude-code
```

### 4. Using the Prompts Library

#### For Individual Agent Work:
1. Navigate to `.claude/prompts/agents/[agent-name]/`
2. Select appropriate prompt based on your task
3. Follow the structured approach in the prompt
4. Use collaboration points to coordinate with other agents

#### For Multi-Agent Workflows:
1. Start with business analysis prompts (Phase 1)
2. Use phase transition coordination
3. Execute parallel development work (Phase 3)
4. Apply quality gates for validation

## 📝 Usage Examples & Scenarios

### Enterprise Web Application Development

```
Phase 1: Business Discovery
├── business-analyst → stakeholder-requirements-gathering.md
├── product-manager → user-story-creation-and-prioritization.md
└── reviewer → requirements validation

Phase 2: Architecture & Design
├── software-architect → system-architecture-design.md
├── security-engineer → security-architecture-and-threat-modeling.md
├── ux-designer → user-research-and-persona-development.md
└── api-engineer → microservices-architecture-patterns.md

Phase 3: Development & QA (Parallel)
├── frontend-engineer → angular-component-development.md
├── api-engineer → rest-api-design-and-implementation.md
├── security-engineer → secure-code-review-and-sast.md
└── qa-engineer → test-automation-and-quality-assurance.md

Phase 4: Deployment
└── deployment-engineer → ci-cd-pipeline-and-infrastructure-setup.md
```

### Desktop Application Development

```
Specialized Focus:
├── frontend-engineer → wxwidgets-desktop-development.md
├── security-engineer → identity-and-access-management.md
├── data-engineer → database-design-and-etl-implementation.md
└── deployment-engineer → infrastructure setup for desktop distribution
```

### Security-Critical Application

```
Security-First Approach:
├── security-engineer → security-architecture-and-threat-modeling.md
├── security-engineer → penetration-testing-and-security-audit.md
├── security-engineer → compliance-audit-and-governance.md
└── reviewer → security-vulnerability-assessment.md
```

### Automated Multi-Agent Workflow with Hooks

```
Complete Automation Pipeline:
├── agent-handoff.sh → Seamless phase transitions
├── cross-agent-dependency-tracker.sh → Workflow validation  
├── compliance-automation.sh → WCAG/GDPR/SOX validation
├── agent-performance-monitor.sh → Bottleneck identification
└── agent-conflict-resolution.sh → Proactive conflict management
```

**Example Hook Usage:**
```bash
# Start performance monitoring
./.claude/hooks/agent-performance-monitor.sh "start" "frontend-engineer"

# Validate dependencies before starting work
./.claude/hooks/cross-agent-dependency-tracker.sh "validate" "frontend-engineer"

# Check compliance during development
./.claude/hooks/compliance-automation.sh "wcag" "frontend-engineer"

# Detect and resolve conflicts
./.claude/hooks/agent-conflict-resolution.sh "detect"
```

## ⚙️ Advanced Configuration

### Multi-Agent Coordination

Each agent can be customized by editing files in the `.claude/agents/` directory. The prompts library in `.claude/prompts/agents/` provides specialized workflows for each agent.

### CI/CD System Integration

The framework supports integration with:

- **GitHub Actions** - Complete CI/CD workflows
- **GitLab CI** - Enterprise DevOps pipelines  
- **Azure DevOps** - Microsoft ecosystem integration
- **Jenkins** - Traditional CI/CD environments

### Technology Stack Adaptation

The template supports diverse technology combinations:

**Frontend:**
- ✅ Angular 17+ (Complete coverage - 9 prompts)
- ✅ wxWidgets Desktop (Complete coverage)
- Modern CSS Architecture & Responsive Design
- Progressive Web Applications (PWA)

**Backend & APIs:**
- RESTful APIs with OpenAPI/Swagger
- GraphQL with subscriptions and federation
- Microservices architecture patterns

**Security:**
- ✅ Complete security coverage (7 prompts)
- Threat modeling and penetration testing
- Identity and Access Management (IAM)
- Compliance frameworks (GDPR, SOX, HIPAA)

**Infrastructure:**
- AWS/Azure/GCP cloud platforms
- Docker/Kubernetes containerization
- Infrastructure as Code (IaC)

## 🤝 Best Practices

### Workflow Organization

- **Use Phase-Based Approach:** Follow the 5-phase development lifecycle
- **Leverage Parallel Execution:** Run compatible agents concurrently
- **Implement Quality Gates:** Validate deliverables before phase transitions
- **Maintain Agent Coordination:** Use handoff protocols between agents

### Code and Documentation Management

- **Version Control Integration:** Git workflow with agent-specific branches
- **Documentation Standards:** Maintain living documentation with each deliverable
- **Code Review Process:** Multi-agent review with security and quality focus
- **Continuous Integration:** Automated testing and quality gates

### Project Scaling

- **Modular Prompt Library:** Add custom prompts as needed
- **Agent Specialization:** Customize agents for domain-specific requirements
- **Workflow Orchestration:** Create project-specific coordination patterns
- **Knowledge Management:** Maintain project memory across agent interactions

## 🔧 Troubleshooting & Support

### Common Issues

**Database Connection Problems:**
- Check `DATABASE_CONNECTIONS.md` configuration
- Verify environment-specific settings (WSL, Docker, cloud)
- Use `DATABASE_CONNECTIONS_TEMPLATE.md` for reference

**Agent Coordination Conflicts:**
- Use `reviewer` agent for conflict resolution
- Follow phase-based workflow to minimize conflicts
- Leverage quality gates for validation

**Performance Optimization:**
- Execute compatible tasks in parallel
- Use agent-specific prompts for efficiency
- Implement caching strategies for repeated operations

### WSL and File Synchronization

If working in WSL environment and files are not synchronized between Windows and WSL:

```bash
# Check if files are synchronized
ls -la /mnt/e/AI/my_claude/

# Force synchronization (if needed)
cd /mnt/e/AI/my_claude/
git status
git pull origin main

# Or reset to latest state
git fetch origin
git reset --hard origin/main
```

## 📚 Documentation & Resources

### Core Documentation

- **[Prompts Library Guide](.claude/prompts/README.md)** - Complete documentation of all 33 available prompts
- **[Automation Hooks Guide](.claude/hooks/README.md)** - Complete documentation of all 11 automation hooks
- **[Agent Specifications](.claude/agents/)** - Detailed agent capabilities and configurations
- **[Project Configuration](CLAUDE.md)** - Main project setup and customization guide
- **[Database Connections](DATABASE_CONNECTIONS.md)** - Database configuration examples

### External Resources

- **[Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)** - Official Claude Code guide
- **[Agent Development Lifecycle](.claude/docs/agent-sdlc-workflow.puml)** - Visual workflow diagrams
- **[Technology Integration Guides](.claude/docs/)** - Serena and Context7 usage patterns

### Community & Support

- **Issues & Feature Requests:** [GitHub Issues](https://github.com/your-username/my_claude/issues)
- **Discussions:** [GitHub Discussions](https://github.com/your-username/my_claude/discussions)
- **Contributing:** See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines

## 🤝 Contributing and Development

This framework thrives on community contributions and real-world usage feedback.

### How to Contribute

1. **Fork the repository** and create a feature branch
2. **Add new prompts** following existing structure and patterns
3. **Test with real projects** and document results
4. **Submit Pull Request** with detailed description
5. **Participate in reviews** and community discussions

### Development Priorities

**Immediate Next Steps:**
1. 🎯 Complete **api-engineer** prompts (2 remaining)
2. 🎯 Complete **business-analyst** prompts (2 remaining)  
3. 🎯 Complete **reviewer** prompts (3 remaining)
4. 🚀 Create workflow orchestration scenarios
5. 📋 Develop quality gate validation prompts

### Quality Standards

- **Expert-Level Content:** Each prompt must contain production-ready examples
- **Technology Depth:** Demonstrate mastery of modern development practices
- **Enterprise Focus:** Address real business needs and scalability requirements
- **Documentation Excellence:** Clear, comprehensive, and actionable guidance

## 📄 License & Usage

**MIT License** - You are free to use, modify, and distribute this framework for any purpose, including commercial projects.

This template serves as a foundation for building sophisticated software solutions using AI-driven development approaches. The comprehensive prompts library and multi-agent framework represent months of expert knowledge distillation and real-world application.

## 🎉 Summary & Impact

This Claude Code Multi-Agent Framework represents a paradigm shift in software development:

**🚀 Revolutionary Approach:** Transform development through systematic AI agent collaboration
**📚 Knowledge Repository:** 31+ expert-level prompts with complete security and frontend coverage  
**🏗️ Production Ready:** Enterprise-grade patterns with real working code examples
**🌍 Technology Excellence:** Deep specialization in Angular, wxWidgets, security, and modern development
**⚡ Scalable Framework:** Adaptable from startup MVPs to enterprise-scale applications

**Ready to revolutionize your development workflow?** Start with the comprehensive prompts library and experience the future of AI-driven software development.

**Happy coding with Claude Code!** 🚀