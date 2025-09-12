# Agent Prompts Library

This directory contains specialized prompts for the Claude Code Agent Framework's 11 agents, organized by function and workflow coordination.

## 📁 Directory Structure

```
.claude/prompts/
├── agents/           # Agent-specific prompts for common operations
├── workflows/        # Cross-agent coordination and handoff prompts
└── README.md        # This comprehensive guide
```

## 🤖 Agent-Specific Prompts

### Business Analysis (`agents/business/`)

**stakeholder-requirements-gathering.md**

- **Purpose:** Conduct structured stakeholder interviews and requirements workshops
- **When to use:** Starting new projects, gathering business requirements, understanding user needs
- **Key outputs:** Business Requirements Document, stakeholder analysis, success criteria
- **Agent:** business-analyst

**current-state-process-analysis.md**

- **Purpose:** Analyze existing business processes to identify improvement opportunities
- **When to use:** Understanding existing workflows, identifying inefficiencies, planning process improvements
- **Key outputs:** Current state process maps, gap analysis, improvement opportunities matrix
- **Agent:** business-analyst

**business-case-development.md**

- **Purpose:** Develop compelling business justification for proposed solutions
- **When to use:** Securing project funding, demonstrating ROI, gaining executive support
- **Key outputs:** Executive business case, financial models, risk assessments, implementation roadmap
- **Agent:** business-analyst

### Product Management (`agents/product/`)

**user-story-creation-and-prioritization.md**

- **Purpose:** Transform business requirements into prioritized user stories with clear acceptance criteria
- **When to use:** Sprint planning, backlog grooming, feature definition, development prioritization
- **Key outputs:** Product backlog, user stories with acceptance criteria, prioritization matrix
- **Agent:** product-manager

**mvp-scoping-and-roadmap-planning.md**

- **Purpose:** Define Minimum Viable Product scope and create strategic product roadmap
- **When to use:** Product strategy development, release planning, feature prioritization, stakeholder alignment
- **Key outputs:** MVP scope document, product roadmap, success metrics framework
- **Agent:** product-manager

### UX Design (`agents/design/`)

**user-research-and-persona-development.md**

- **Purpose:** Conduct comprehensive user research and create actionable user personas
- **When to use:** Understanding target users, validating design decisions, informing product strategy
- **Key outputs:** User research report, primary personas, journey maps, design principles
- **Agent:** ux-designer

### System Architecture (`agents/architecture/`)

**system-architecture-design.md**

- **Purpose:** Design scalable, maintainable system architecture aligned with business requirements
- **When to use:** Technical planning, technology stack selection, system design, scalability planning
- **Key outputs:** System architecture documentation, technology recommendations, implementation roadmap
- **Agent:** software-architect

### API Engineering (`agents/api/`)

**rest-api-design-and-implementation.md**

- **Purpose:** Design and implement scalable, secure REST APIs following best practices
- **When to use:** API development, microservices architecture, backend integration design
- **Key outputs:** API specifications (OpenAPI/Swagger), implementation code, integration guides
- **Agent:** api-engineer

**microservices-architecture-patterns.md**

- **Purpose:** Design and implement scalable microservices architecture with proven patterns and best practices
- **When to use:** System decomposition, service mesh architecture, distributed systems design
- **Key outputs:** Service boundary definitions, communication patterns, resilience implementations
- **Agent:** api-engineer

**graphql-api-development.md**

- **Purpose:** Design and implement efficient GraphQL APIs with advanced features like subscriptions and federation
- **When to use:** Flexible data fetching requirements, real-time features, API federation scenarios
- **Key outputs:** GraphQL schemas, resolver implementations, subscription systems, federation setup
- **Agent:** api-engineer

### Data Engineering (`agents/data/`)

**database-design-and-etl-implementation.md**

- **Purpose:** Design efficient database schemas and implement robust ETL pipelines for data processing
- **When to use:** Database design, data warehouse implementation, ETL pipeline development
- **Key outputs:** Database schemas, migration scripts, ETL pipeline code, data quality frameworks
- **Agent:** data-engineer

### Security Engineering (`agents/security/`)

**security-architecture-and-threat-modeling.md**

- **Purpose:** Design comprehensive security architecture and conduct thorough threat modeling
- **When to use:** Security planning, threat assessment, compliance implementation, incident response
- **Key outputs:** Security architecture, threat models, incident response plans, compliance frameworks
- **Agent:** security-engineer

### Quality Assurance (`agents/quality/`)

**test-automation-and-quality-assurance.md**

- **Purpose:** Design comprehensive testing strategies and implement automated quality assurance processes
- **When to use:** Test planning, automation framework setup, quality gate implementation
- **Key outputs:** Test strategies, automated test suites, quality dashboards, CI/CD integration
- **Agent:** qa-engineer

### Deployment Engineering (`agents/deployment/`)

**ci-cd-pipeline-and-infrastructure-setup.md**

- **Purpose:** Design and implement automated deployment pipelines and scalable infrastructure
- **When to use:** Infrastructure planning, CI/CD setup, deployment automation, monitoring implementation
- **Key outputs:** Infrastructure code, CI/CD pipelines, monitoring setup, deployment documentation
- **Agent:** deployment-engineer

### Review and Validation (`agents/review/`)

**sonarqube-code-quality-analysis.md**

- **Purpose:** Conduct comprehensive code quality analysis using SonarQube and establish quality gates
- **When to use:** Code quality assessment, technical debt analysis, quality gate enforcement
- **Key outputs:** Quality reports, remediation plans, automated quality gates, team coaching materials
- **Agent:** reviewer

**security-vulnerability-assessment.md**

- **Purpose:** Conduct comprehensive security vulnerability assessments using automated tools and manual analysis
- **When to use:** Security audits, vulnerability management, compliance validation, penetration testing
- **Key outputs:** Vulnerability reports, risk assessments, remediation priorities, security dashboards
- **Agent:** reviewer

## 🔄 Workflow Coordination Prompts

### Phase Transitions (`workflows/phase-transitions/`)

**business-requirements-to-architecture-handoff.md**

- **Purpose:** Seamlessly transfer validated business requirements to architecture and design teams
- **When to use:** Transitioning from Phase 1 (Business Discovery) to Phase 2 (Architecture & Design)
- **Key activities:** Requirements validation, team briefings, handoff coordination meeting
- **Participants:** business-analyst, product-manager, ux-designer, reviewer → software-architect, security-engineer, data-engineer
- **Outputs:** Complete requirements package, architecture briefing documents, team alignment confirmation

**architecture-design-to-development-handoff.md**

- **Purpose:** Transfer validated architecture and design specifications to development teams
- **When to use:** Transitioning from Phase 2 (Architecture & Design) to Phase 3 (Development & QA)
- **Key activities:** Architecture documentation validation, design system handoff, development team briefings
- **Participants:** software-architect, ux-designer, security-engineer, data-engineer → frontend-engineer, api-engineer, qa-engineer
- **Outputs:** Technical specifications, design system package, implementation guidance

*[Additional phase transition prompts to be created]*

### Orchestration Scenarios (`workflows/scenarios/`)

**new-feature-development-orchestration.md**

- **Purpose:** Orchestrate multi-agent collaboration for developing new features from conception to production
- **When to use:** Complete feature development lifecycle, major functionality additions, MVP development
- **Key phases:** Business Discovery → Architecture & Design → Development & QA → Deployment & Validation
- **Participants:** All 11 agents coordinated through systematic workflow
- **Outputs:** Production-ready features with complete documentation and validation

**critical-bug-fix-orchestration.md**

- **Purpose:** Coordinate rapid response for critical production issues with minimal disruption
- **When to use:** Emergency incidents, critical bugs, system outages, security breaches
- **Key phases:** Emergency Response → Priority Fix → Standard Resolution → Post-Incident Analysis
- **Participants:** Specialized response teams based on incident type and severity
- **Outputs:** System restoration, incident reports, prevention measures, process improvements

### Parallel Coordination (`workflows/parallel-coordination/`)

**cross-team-development-coordination.md**

- **Purpose:** Coordinate frontend, API, data, security, and QA teams during concurrent development
- **When to use:** During Phase 3 (Development & QA) when multiple specialized teams work in parallel
- **Key activities:** Daily standups, integration coordination, quality gate management
- **Participants:** frontend-engineer, api-engineer, data-engineer, security-engineer, qa-engineer
- **Outputs:** Coordination notes, integration status, quality metrics, risk assessments

### Quality Gates (`workflows/quality-gates/`)

*[Prompts to be created for quality validation checkpoints between phases]*

### Stakeholder Communication (`workflows/stakeholder-communication/`)

*[Prompts to be created for stakeholder updates, approval processes, feedback integration]*

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

## 📊 Success Metrics

### Individual Agent Effectiveness

- **Task completion rate** within estimated timeframes
- **Quality of deliverables** meeting defined standards
- **Stakeholder satisfaction** with agent outputs
- **Collaboration effectiveness** with other agents

### Workflow Coordination Success

- **Phase transition smoothness** without information loss
- **Cross-team coordination** effectiveness and communication
- **Quality gate passage** rates and issue resolution speed
- **Overall project timeline** adherence and delivery quality

## 🔧 Integration with AI Tools

### Serena Integration

- Use Serena for **navigating existing codebases** when analyzing current state
- Leverage Serena for **precise code modifications** during implementation
- Apply Serena for **debugging and troubleshooting** during development phases

### Context7 Integration

- Use Context7 for **generating new code** based on specifications
- Leverage Context7 for **creating comprehensive documentation** and templates
- Apply Context7 for **large-scale transformations** and migrations

### Combined AI-Agent Workflows

- **Analysis phase:** Serena + business-analyst for current state analysis
- **Design phase:** Context7 + software-architect for architecture generation
- **Development phase:** Context7 + Serena + development agents for implementation
- **Documentation phase:** Context7 + all agents for comprehensive documentation

## 📚 Additional Resources

- **Agent Specifications:** `.claude/agents/` directory for detailed agent capabilities
- **Workflow Diagrams:** `.claude/docs/agent-sdlc-workflow.puml` for visual process overview
- **Project Configuration:** `CLAUDE.md` for project-specific agent guidance
- **AI Tools Guide:** `.claude/docs/ai-tools-usage-guide.md` for Serena and Context7 usage

---

**Note:** This prompt library is continuously evolving. Prompts marked with *[Additional prompts to be created]* indicate areas for future expansion based on project needs and user feedback.

*Each prompt is designed to work independently while supporting the overall Agent-Driven Development Lifecycle for maximum productivity and quality.*