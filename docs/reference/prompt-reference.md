# Prompt Reference - Claude Code Framework

**Status:** Production Ready ✅

Complete reference catalog of all prompts in the Claude Code Multi-Agent Framework with agent-prompt binding documentation.

## 🎯 Overview

The Claude Code Framework provides a comprehensive library of professional-grade prompts that automatically activate corresponding specialized agents. All prompts follow functional design principles and adapt to project-specific requirements.

## 🔗 Agent-Prompt Binding System

### Automatic Agent Activation

The framework implements revolutionary directory-based agent binding:

```
.claude/prompts/agents/[category]/ → Activates corresponding agent
```

**Binding Examples:**
- `.claude/prompts/agents/api/` → Activates `api-engineer` agent
- `.claude/prompts/agents/frontend/` → Activates `frontend-engineer` agent
- `.claude/prompts/agents/security/` → Activates `security-engineer` agent
- `.claude/prompts/agents/planner/` → Activates `product-manager` agent

## 📁 Prompt Library Structure

### Session Management Prompts

#### Core Session Operations
- **`session-start-and-context-analysis.md`**
  - **Purpose**: Initialize new work session with comprehensive context analysis
  - **Agent**: `session-manager`
  - **Capabilities**: Project analysis, technology detection, context establishment

- **`session-continuation-from-summary.md`**
  - **Purpose**: Resume previous session with state restoration
  - **Agent**: `session-manager`
  - **Capabilities**: Context recovery, state validation, seamless continuation

- **`session-end-and-summary-generation.md`**
  - **Purpose**: Close session with intelligent summarization
  - **Agent**: `session-manager`
  - **Capabilities**: Work summarization, context preservation, handoff preparation

- **`session-state-recovery.md`**
  - **Purpose**: Recover from interrupted or corrupted sessions
  - **Agent**: `session-manager`
  - **Capabilities**: State validation, corruption detection, recovery protocols

#### MCP Integration
- **`serena-sync-and-update.md`**
  - **Purpose**: Synchronize with Serena MCP tools and update project index
  - **Agent**: `session-manager`
  - **Capabilities**: MCP integration, project indexing, knowledge base updates

- **`session-context-validation.md`**
  - **Purpose**: Validate session context integrity and detect corruption
  - **Agent**: `session-manager`
  - **Capabilities**: Context validation, integrity checking, corruption recovery

- **`session-handoff-management.md`**
  - **Purpose**: Manage team transitions and collaborative session handoffs
  - **Agent**: `session-manager`
  - **Capabilities**: Team coordination, context transfer, collaborative workflows

### Agent-Specific Prompts

#### API Engineering (`/agents/api/`)
- **`rest-api-design-and-implementation.md`**
  - **Agent**: `api-engineer`
  - **Purpose**: Design and implement RESTful APIs with best practices
  - **Capabilities**: API architecture, endpoint design, documentation generation

- **`graphql-api-development.md`**
  - **Agent**: `api-engineer`
  - **Purpose**: Develop GraphQL APIs with schema design and optimization
  - **Capabilities**: Schema design, resolver implementation, performance optimization

- **`microservices-architecture-patterns.md`**
  - **Agent**: `api-engineer`
  - **Purpose**: Design and implement microservices architecture
  - **Capabilities**: Service decomposition, communication patterns, deployment strategies

#### Frontend Engineering (`/agents/frontend/`)
- **`modern-web-component-development.md`**
  - **Agent**: `frontend-engineer`
  - **Purpose**: Develop modern, reusable web components
  - **Capabilities**: Component architecture, state management, performance optimization

- **`responsive-web-design-implementation.md`**
  - **Agent**: `frontend-engineer`
  - **Purpose**: Implement responsive and accessible web designs
  - **Capabilities**: Responsive layouts, accessibility compliance, cross-browser compatibility

- **`frontend-performance-optimization.md`**
  - **Agent**: `frontend-engineer`
  - **Purpose**: Optimize frontend application performance
  - **Capabilities**: Bundle optimization, lazy loading, performance monitoring

#### Backend Engineering (`/agents/backend/`)
- **`scalable-backend-architecture.md`**
  - **Agent**: `backend-engineer`
  - **Purpose**: Design scalable backend systems and services
  - **Capabilities**: Architecture design, database optimization, caching strategies

- **`server-side-security-implementation.md`**
  - **Agent**: `backend-engineer`
  - **Purpose**: Implement comprehensive server-side security
  - **Capabilities**: Authentication, authorization, data protection, security monitoring

- **`backend-performance-optimization.md`**
  - **Agent**: `backend-engineer`
  - **Purpose**: Optimize backend system performance and scalability
  - **Capabilities**: Database optimization, caching, load balancing, monitoring

#### Security Engineering (`/agents/security/`)
- **`security-architecture-and-threat-modeling.md`**
  - **Agent**: `security-engineer`
  - **Purpose**: Design security architecture and perform threat modeling
  - **Capabilities**: Security design, threat analysis, risk assessment

- **`penetration-testing-and-security-audit.md`**
  - **Agent**: `security-engineer`
  - **Purpose**: Conduct penetration testing and security audits
  - **Capabilities**: Vulnerability assessment, security testing, audit procedures

- **`secure-code-review-and-sast.md`**
  - **Agent**: `security-engineer`
  - **Purpose**: Perform secure code reviews and static analysis
  - **Capabilities**: Code security analysis, vulnerability detection, remediation guidance

#### Quality Assurance (`/agents/quality/`)
- **`test-automation-and-quality-assurance.md`**
  - **Agent**: `qa-engineer`
  - **Purpose**: Implement comprehensive test automation and QA processes
  - **Capabilities**: Test strategy, automation frameworks, quality metrics

- **`application-performance-optimization.md`**
  - **Agent**: `qa-engineer`
  - **Purpose**: Optimize application performance and user experience
  - **Capabilities**: Performance testing, optimization strategies, monitoring

- **`quality-process-improvement.md`**
  - **Agent**: `qa-engineer`
  - **Purpose**: Improve quality processes and development workflows
  - **Capabilities**: Process analysis, quality metrics, continuous improvement

#### Business Analysis (`/agents/business/`)
- **`stakeholder-requirements-gathering.md`**
  - **Agent**: `business-analyst`
  - **Purpose**: Gather and analyze stakeholder requirements
  - **Capabilities**: Requirements elicitation, stakeholder management, documentation

- **`business-case-development.md`**
  - **Agent**: `business-analyst`
  - **Purpose**: Develop comprehensive business cases for projects
  - **Capabilities**: Business analysis, cost-benefit analysis, ROI calculation

- **`current-state-process-analysis.md`**
  - **Agent**: `business-analyst`
  - **Purpose**: Analyze current business processes and identify improvements
  - **Capabilities**: Process mapping, gap analysis, improvement recommendations

#### Product Management (`/agents/planner/`)
- **`user-story-creation-and-prioritization.md`**
  - **Agent**: `product-manager`
  - **Purpose**: Create and prioritize user stories for development
  - **Capabilities**: User story development, prioritization frameworks, backlog management

- **`mvp-scoping-and-roadmap-planning.md`**
  - **Agent**: `product-manager`
  - **Purpose**: Define MVP scope and develop product roadmaps
  - **Capabilities**: MVP definition, roadmap planning, feature prioritization

- **`feature-implementation-from-specification.md`**
  - **Agent**: `product-manager`
  - **Purpose**: Guide feature implementation from specification to delivery
  - **Capabilities**: Feature specification, implementation planning, delivery coordination

#### Architecture (`/agents/architecture/`)
- **`system-architecture-design.md`**
  - **Agent**: `software-architect`
  - **Purpose**: Design comprehensive system architecture
  - **Capabilities**: Architecture patterns, technology selection, scalability planning

- **`technology-stack-evaluation-and-selection.md`**
  - **Agent**: `software-architect`
  - **Purpose**: Evaluate and select optimal technology stacks
  - **Capabilities**: Technology assessment, stack comparison, decision frameworks

- **`architectural-decision-records.md`**
  - **Agent**: `software-architect`
  - **Purpose**: Document architectural decisions and rationale
  - **Capabilities**: Decision documentation, rationale recording, impact analysis

#### UX Design (`/agents/design/`)
- **`user-research-and-persona-development.md`**
  - **Agent**: `ux-designer`
  - **Purpose**: Conduct user research and develop user personas
  - **Capabilities**: User research, persona development, insight generation

- **`web-accessibility-and-inclusive-design.md`**
  - **Agent**: `ux-designer`
  - **Purpose**: Design accessible and inclusive user experiences
  - **Capabilities**: Accessibility compliance, inclusive design, usability testing

- **`design-system-development-and-maintenance.md`**
  - **Agent**: `ux-designer`
  - **Purpose**: Develop and maintain comprehensive design systems
  - **Capabilities**: Design system architecture, component libraries, style guides

#### Data Engineering (`/agents/data/`)
- **`database-design-and-etl-implementation.md`**
  - **Agent**: `data-engineer`
  - **Purpose**: Design databases and implement ETL pipelines
  - **Capabilities**: Database architecture, ETL processes, data modeling

- **`data-pipeline-architecture-and-optimization.md`**
  - **Agent**: `data-engineer`
  - **Purpose**: Design and optimize data processing pipelines
  - **Capabilities**: Pipeline architecture, stream processing, batch processing

- **`data-quality-and-governance.md`**
  - **Agent**: `data-engineer`
  - **Purpose**: Implement data quality and governance frameworks
  - **Capabilities**: Data validation, quality monitoring, governance policies

#### Deployment Engineering (`/agents/deployment/`)
- **`ci-cd-pipeline-and-infrastructure-setup.md`**
  - **Agent**: `deployment-engineer`
  - **Purpose**: Setup CI/CD pipelines and deployment infrastructure
  - **Capabilities**: Pipeline design, infrastructure automation, deployment strategies

- **`container-orchestration-and-kubernetes.md`**
  - **Agent**: `deployment-engineer`
  - **Purpose**: Implement container orchestration with Kubernetes
  - **Capabilities**: Container design, Kubernetes configuration, orchestration patterns

- **`cloud-infrastructure-automation.md`**
  - **Agent**: `deployment-engineer`
  - **Purpose**: Automate cloud infrastructure provisioning and management
  - **Capabilities**: Infrastructure as code, cloud automation, resource optimization

### Project Initialization Prompts (`/init/`)

- **`new-project.md`**
  - **Agent**: `project-owner`
  - **Purpose**: Initialize new project with framework integration
  - **Capabilities**: Project setup, CLAUDE.md creation, framework configuration

- **`existing-project.md`**
  - **Agent**: `project-owner`
  - **Purpose**: Integrate framework with existing projects
  - **Capabilities**: Project analysis, framework adaptation, integration planning

- **`claude_md_from_concept.md`**
  - **Agent**: `project-owner`
  - **Purpose**: Generate CLAUDE.md from project concept documentation
  - **Capabilities**: Concept analysis, configuration generation, requirements mapping

- **`prepare_instruction.md`**
  - **Agent**: `project-owner`
  - **Purpose**: Generate development instructions and workflow
  - **Capabilities**: Workflow planning, agent coordination, implementation strategy

### Workflow Orchestration Prompts (`/workflows/`)

#### Parallel Coordination (`/workflows/parallel-coordination/`)
- Cross-team coordination patterns
- Simultaneous agent workflows
- Resource conflict resolution

#### Phase Transitions (`/workflows/phase-transitions/`)
- Agent handoff protocols
- Phase transition management
- Context preservation patterns

#### Quality Gates (`/workflows/quality-gates/`)
- Quality validation checkpoints
- Multi-agent validation workflows
- Quality assurance coordination

## 🎯 Prompt Quality Standards

### Mandatory Structure

Every prompt MUST contain these sections:

1. **FUNCTIONAL REQUIREMENTS** - What needs to be accomplished
2. **HIGH-LEVEL ALGORITHMS** - How to approach the problem
3. **VALIDATION CRITERIA** - What conditions must be met
4. **USAGE EXAMPLES** - For different scenarios

### Quality Compliance

All prompts ensure:

- ✅ **Functional Design** - Describes WHAT, not HOW
- ✅ **Technology Agnostic** - Works across different stacks
- ✅ **CLAUDE.md Integration** - Adapts to project configuration
- ✅ **Professional Standards** - Enterprise-grade content
- ✅ **Agent Integration** - Seamless agent activation

### Validation Criteria

Prompts are validated for:

- **Structural Compliance** - Required sections present
- **Functional Approach** - No hardcoding violations
- **Technology Adaptation** - Cross-stack compatibility
- **Integration Quality** - Framework component compatibility

## 🔧 Usage Guidelines

### Direct Prompt Usage

1. **Copy prompt content** from `.claude/prompts/` directory
2. **Paste into Claude Code** - Agent automatically activates
3. **Framework adapts** to CLAUDE.md configuration
4. **TodoWrite integration** manages workflow

### Agent-Prompt Coordination

When using prompts:
- **Agent automatically activates** based on directory structure
- **Context loads** from CLAUDE.md project configuration
- **TODO integration** coordinates with other agents
- **Quality standards** ensure enterprise-grade results

### Best Practices

1. **Read CLAUDE.md first** - Understand project context
2. **Use appropriate category** - Let automatic activation work
3. **Follow functional patterns** - Focus on outcomes
4. **Validate results** - Check against success criteria

---

**See also:**
- [Agent Reference](agent-reference.md) - Complete agent documentation
- [Command Reference](command-reference.md) - Command-agent mapping
- [Prompt Library](../core-features/prompt-library.md) - Detailed prompt system documentation