# CLAUDE.md – Project Description Template for Claude Code

## 0. Project Metadata

- **project_name**: [project name, e.g., "task-manager-app"]
- **project_description**: [brief description, e.g., "Web application supporting team task management"]
- **project_version**: [current version, e.g., "1.0.0"]
- **framework_version**: [Claude Code Multi-Agent Framework version, e.g., "2.0.0"]
- **last_updated**: [last update date, e.g., "2025-09-14"]
- **primary_language**: [main language: csharp, python, rust, java, typescript, go, cpp, ruby]
- **business_domain**: [domain: ecommerce, fintech, healthcare, saas, enterprise, iot, etc.]
- **project_scale**: [scale: startup, sme, enterprise]
- **development_stage**: [stage: concept, mvp, development, production, maintenance]

## 1. Project Description

[Fill in the general project description, e.g., "Web application supporting team task management."]

---

## 2. Domains and Goals

- Business domains: [e.g., project management, team communication, data analysis]
- Main project goals: [e.g., improve collaboration, process automation, reporting]

---

## 3. Technologies

- **Frontend – technologies and tools:** [fill in, e.g., React, Vue, TypeScript]
- **Backend – technologies and tools:** [fill in, e.g., Python, Node.js, FastAPI]
- **Deployment – infrastructure and tools:** [fill in, e.g., Docker, Kubernetes, AWS]
- **Database:** [e.g., PostgreSQL, MySQL, MongoDB]
- **Other:** [e.g., deployment automation, external service integrations]

---

## 4. Agents and Roles

The list of available agents and their competency scope is defined in files:

### Core Strategy and Planning

- **product-manager** - Product strategy, requirements gathering, stakeholder management
- **business-analyst** - Business process analysis, requirements documentation, stakeholder communication
- **reviewer** - Quality assurance, requirements validation, risk assessment

### Project and Session Management

- **session-manager** - Session lifecycle management, context preservation, state recovery, MCP tools coordination
- **project-owner** - Project initialization, health monitoring, governance, framework configuration

### Architecture and Design

- **software-architect** - System architecture, technology selection, scalability planning

### Agent-Prompt Integration

**🔗 Automatic Agent Activation System:**
- Prompts in `.claude/prompts/agents/[category]/` automatically activate corresponding agents
- Directory structure determines agent binding: `api/` → `api-engineer`, `frontend/` → `frontend-engineer`
- Agents read CLAUDE.md and adapt to project requirements automatically
- All tasks managed through agent's TodoWrite workflow integration

**Usage Pattern:**
```
Prompt Location: .claude/prompts/agents/api/rest-api-design.md
→ Activates: api-engineer agent (.claude/agents/api/api-engineer.md)
→ Agent Context: Reads this CLAUDE.md for project adaptation
→ Agent Execution: Applies specialized competencies + TodoWrite management
```
- **ux-designer** - User experience design, design systems, accessibility, user research

### Development

- **frontend-engineer** - User interface development, responsive design, performance optimization
- **api-engineer** - API design, microservices, service integration, distributed systems
- **data-engineer** - Data architecture, ETL pipelines, analytics, database optimization

### Quality and Security

- **qa-engineer** - Test automation, quality processes, performance testing, continuous improvement
- **security-engineer** - Application security, threat modeling, compliance, security architecture

### Operations

- **deployment-engineer** - DevOps, CI/CD pipelines, infrastructure automation, monitoring

Each agent's competency scope is located in the corresponding file in the `.claude/agents` directory. If you want to add a new agent or modify a role, edit the appropriate agent file.

---

## 5. Integrations and Dependencies

- External APIs: [e.g., integration with external services]
- Services: [e.g., notification systems, authorization]
- Other dependencies: [e.g., libraries, supporting tools]

---

## 6. Non-functional Requirements

- Performance: [e.g., fast application operation]
- Security: [e.g., user data protection]
- Scalability: [e.g., system expansion capability]
- Availability: [e.g., high service availability]

---

## 7. Special Notes

- Technological constraints: [e.g., preferred open-source solutions]
- Coding style preferences: [e.g., readability, standards compliance]
- Special guidelines for agents: [e.g., communication language preferences]
- Work directory usage: The `/work/` directory is the ONLY location for temporary files, scripts, and working documents - excluded from git via .gitignore

---

## 8. TODO Management Configuration

### Task Management Strategy

- **todo_management_enabled**: [true/false - enable active TODO management system]
- **todo_hierarchy_level**: [simple/hierarchical - choose management complexity]
- **auto_task_creation**: [true/false - enable automatic task breakdown by agents]
- **progress_tracking**: [session/project/enterprise - choose tracking scope]

### TodoWrite Integration

- **session_todos**: [true/false - use TodoWrite for immediate session tasks]
- **agent_coordination**: [true/false - agents coordinate via shared todos]
- **task_handoffs**: [true/false - enable automatic task handoffs between agents]

### Hierarchical TODO System (if enabled)

- **epic_management**: [true/false - use Epic level (4-12 weeks) for major initiatives]
- **feature_breakdown**: [true/false - break Epics into Features (1-3 weeks)]
- **task_granularity**: [detailed/standard/minimal - level of task breakdown]
- **subtask_tracking**: [true/false - track individual subtasks (2-8 hours)]

### Agent TODO Responsibilities

**Epic Level (Business Strategy):**
- **epic_owners**: [business-analyst, product-manager] - responsible for Epic creation and management
- **epic_validation**: [reviewer] - validates Epic definitions and business value

**Feature Level (Architecture):**
- **feature_owners**: [software-architect, ux-designer, security-engineer] - break Epics into Features
- **feature_coordination**: [true/false] - coordinate Feature dependencies across agents

**Task Level (Implementation):**
- **task_owners**: [frontend-engineer, api-engineer, data-engineer, qa-engineer] - execute Tasks
- **task_estimation**: [true/false] - agents provide time estimates for Tasks
- **task_dependencies**: [true/false] - track dependencies between Tasks

**Subtask Level (Execution):**
- **subtask_auto_creation**: [true/false] - agents automatically break Tasks into Subtasks
- **subtask_completion_tracking**: [true/false] - track individual Subtask completion

### Progress Reporting

- **daily_standups**: [true/false] - generate daily progress reports
- **weekly_summaries**: [true/false] - weekly progress and velocity reports
- **milestone_tracking**: [true/false] - track major project milestones
- **burndown_charts**: [true/false] - generate burndown and velocity metrics

### Integration Settings

- **external_tools**: [none/jira/asana/trello/other] - integrate with external project management
- **notification_system**: [true/false] - enable TODO status change notifications
- **automation_hooks**: [true/false] - use .claude/hooks for TODO automation
- **api_integration**: [true/false] - expose TODO data via API for external tools

### TODO Management Templates

**For Startup Projects (project_scale: startup):**
```yaml
todo_management_enabled: true
todo_hierarchy_level: simple
auto_task_creation: true
progress_tracking: session
session_todos: true
agent_coordination: true
epic_management: false
feature_breakdown: true
task_granularity: standard
```

**For SME Projects (project_scale: sme):**
```yaml
todo_management_enabled: true
todo_hierarchy_level: hierarchical
auto_task_creation: true
progress_tracking: project
session_todos: true
agent_coordination: true
epic_management: true
feature_breakdown: true
task_granularity: detailed
milestone_tracking: true
```

**For Enterprise Projects (project_scale: enterprise):**
```yaml
todo_management_enabled: true
todo_hierarchy_level: hierarchical
auto_task_creation: true
progress_tracking: enterprise
session_todos: true
agent_coordination: true
epic_management: true
feature_breakdown: true
task_granularity: detailed
subtask_tracking: true
daily_standups: true
weekly_summaries: true
burndown_charts: true
external_tools: jira
api_integration: true
```

---

## 9. Command-Agent Mapping

### 🎯 **INTELLIGENT COMMAND RECOGNITION**

**Claude agents MUST recognize user commands and automatically select appropriate agent-prompt combinations:**

#### **Session Management Commands**
```
User Input → Agent + Prompt
"zapisz sesję" / "save session" → session-manager + session-end-and-summary-generation.md (+ serena-sync if .serena exists)
"przywróć sesję" / "restore session" → session-manager + session-continuation-from-summary.md (+ serena-sync if .serena exists)
"odzyskaj sesję" / "recover session" → session-manager + session-state-recovery.md (+ serena-sync if .serena exists)
"rozpocznij sesję" / "start session" → session-manager + session-start-and-context-analysis.md (+ serena-sync if .serena exists)
"kontynuuj sesję" / "continue session" → session-manager + session-continuation-from-summary.md (+ serena-sync if .serena exists)
"analiza kontekstu" / "context analysis" → session-manager + session-start-and-context-analysis.md (+ serena-sync if .serena exists)
```

#### **Serena MCP Integration Commands**
```
"serena sync" / "synchronizuj serena" → session-manager + serena-sync-and-update.md
"serena update" / "aktualizuj serena" → session-manager + serena-sync-and-update.md
"reindex project" / "przeindeksuj projekt" → session-manager + serena-sync-and-update.md
"update index" / "zaktualizuj indeks" → session-manager + serena-sync-and-update.md
"serena status" / "status serena" → session-manager + serena-sync-and-update.md
"check serena" / "sprawdź serena" → session-manager + serena-sync-and-update.md
```

#### **Project Management Commands**
```
"sprawdź projekt" / "check project" → project-owner + project-health-check-pro.md
"health check" / "zdrowie projektu" → project-owner + project-health-check-pro.md
"nowy projekt" / "new project" → project-owner + new-project.md
"istniejący projekt" / "existing project" → project-owner + existing-project.md
"przygotuj release" / "prepare release" → project-owner + project-release-preparation.md
"modernizuj strukturę" / "modernize structure" → project-owner + project-structure-modernization.md
"automatyzacja projektu" / "project automation" → project-owner + project-maintenance-automation.md
"inicjalizacja" / "initialization" → project-owner + new-project.md
```

#### **Business Analysis Commands**
```
"analiza biznesowa" / "business analysis" → business-analyst + business-case-development.md
"wymagania" / "requirements" → business-analyst + stakeholder-requirements-gathering.md
"case study" / "studium przypadku" → business-analyst + business-case-development.md
"stakeholder" / "interesariusze" → business-analyst + stakeholder-requirements-gathering.md
"proces biznesowy" / "business process" → business-analyst + current-state-process-analysis.md
```

#### **Product Management Commands**
```
"planowanie produktu" / "product planning" → product-manager + mvp-scoping-and-roadmap-planning.md
"user stories" / "historie użytkownika" → product-manager + user-story-creation-and-prioritization.md
"roadmap" / "mapa drogowa" → product-manager + mvp-scoping-and-roadmap-planning.md
"MVP" → product-manager + mvp-scoping-and-roadmap-planning.md
"feature" / "funkcjonalność" → product-manager + feature-implementation-from-specification.md
```

#### **Development Commands**
```
"frontend" / "front-end" → frontend-engineer + (context-appropriate frontend prompt)
"backend" / "back-end" → backend-engineer + (context-appropriate backend prompt)
"API" / "interfejs API" → api-engineer + rest-api-design-and-implementation.md
"REST API" → api-engineer + rest-api-design-and-implementation.md
"GraphQL" → api-engineer + graphql-api-development.md
"microservices" / "mikroserwisy" → api-engineer + microservices-architecture-patterns.md
"baza danych" / "database" → data-engineer + database-design-and-etl-implementation.md
"ETL" → data-engineer + database-design-and-etl-implementation.md
```

#### **Quality & Security Commands**
```
"testy" / "tests" / "testing" → qa-engineer + test-automation-and-quality-assurance.md
"quality" / "jakość" → qa-engineer + test-automation-and-quality-assurance.md
"performance" / "wydajność" → qa-engineer + application-performance-optimization.md
"security" / "bezpieczeństwo" → security-engineer + (context-appropriate security prompt)
"threat modeling" / "modelowanie zagrożeń" → security-engineer + security-architecture-and-threat-modeling.md
"penetration test" / "test penetracyjny" → security-engineer + penetration-testing-and-security-audit.md
"code review" / "przegląd kodu" → security-engineer + secure-code-review-and-sast.md
```

#### **Architecture & Design Commands**
```
"architektura" / "architecture" → software-architect + system-architecture-design.md
"design system" / "system projektowania" → ux-designer + user-research-and-persona-development.md
"UX" / "user experience" → ux-designer + user-research-and-persona-development.md
"accessibility" / "dostępność" → ux-designer + web-accessibility-and-inclusive-design.md
"deployment" / "wdrożenie" → deployment-engineer + ci-cd-pipeline-and-infrastructure-setup.md
"CI/CD" → deployment-engineer + ci-cd-pipeline-and-infrastructure-setup.md
"infrastructure" / "infrastruktura" → deployment-engineer + ci-cd-pipeline-and-infrastructure-setup.md
```

#### **Review & Validation Commands**
```
"review" / "przegląd" → reviewer + (context-appropriate review prompt)
"validate" / "walidacja" → reviewer + (context-appropriate validation prompt)
"audit" / "audyt" → reviewer + security-vulnerability-assessment.md
"compliance" / "zgodność" → reviewer + compliance-audit-and-governance.md
"quality gate" / "brama jakości" → reviewer + (quality assessment prompt)
```

### ✅ **COMMAND RECOGNITION RULES**

#### **Language Support**
- **Polish Commands** - Recognize Polish language commands and map to appropriate agents
- **English Commands** - Standard English command recognition
- **Mixed Language** - Handle code-switching between Polish and English
- **Technical Terms** - Recognize technical terms in both languages

#### **Context Awareness**
- **Project Context** - Consider current project type and technology stack
- **Session Context** - Understand ongoing work and previous agent interactions
- **Task Context** - Map commands to appropriate complexity level of prompts
- **User Preference** - Adapt to user's preferred communication style
- **MCP Tools Detection** - Automatically detect if Serena MCP is active (check for .serena directory)
- **Serena Integration** - Enhance session commands with Serena sync when MCP tools are available

#### **Fuzzy Matching**
- **Partial Commands** - Recognize incomplete or abbreviated commands
- **Synonyms** - Handle multiple ways of expressing the same intent
- **Technical Variations** - Map technical variations to standard commands
- **Intent Recognition** - Understand user intent even with non-standard phrasing

#### **Multi-Command Handling**
- **Compound Commands** - Handle multiple commands in single request
- **Sequential Processing** - Execute complex workflows involving multiple agents
- **Dependency Resolution** - Understand command dependencies and execution order
- **Batch Operations** - Group related commands for efficient execution

#### **Serena MCP Integration Logic**
- **Automatic Detection** - Check for .serena directory existence to determine if Serena MCP is active
- **Session Memory Strategy** - When Serena is active: prioritize Serena's project knowledge base for session context
- **Hybrid Approach** - Use both Serena project indexing and framework's session summaries for comprehensive context
- **Index Synchronization** - Automatically trigger Serena reindexing after significant project changes
- **Fallback Mechanism** - Gracefully fallback to standard session management when Serena is unavailable

---

## 10. Contact and Project Owners

- Main contact: [e.g., email, Slack, Teams]
- Business/technical owners: [e.g., name and surname, role]

---

## 11. Change History

### Version History

- **Project Creation Date**: [e.g., 2025-09-11]
- **Current Version**: [project_version from metadata]
- **Last Updated**: [last_updated from metadata]

### Version Control Integration

- **Repository**: [git repository URL]
- **Branch Strategy**: [e.g., main, develop, feature branches]
- **Version Tags**: [e.g., semantic versioning: v1.0.0, v1.1.0]

### Change Log Template

```markdown
## [Version] - YYYY-MM-DD

### Added
- New features or capabilities

### Changed
- Changes to existing functionality

### Deprecated
- Features marked for removal in future versions

### Removed
- Features removed in this version

### Fixed
- Bug fixes and issue resolutions

### Security
- Security improvements and fixes
```

### Major Updates History

- **Initial Setup**: [Creation date] - Project initialized with Claude Code Multi-Agent Framework
- **TODO Management Integration**: [Date] - Added hierarchical TODO management system
- **Workflow Orchestration**: [Date] - Implemented cross-agent coordination workflows
- **Quality Gates**: [Date] - Added quality validation and monitoring systems
- **[Custom Updates]**: [Date] - [Description of project-specific changes]

---

*Fill in the above sections according to project requirements. Claude Code agents will automatically adapt their competencies based on this file.*
