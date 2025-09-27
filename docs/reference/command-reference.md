# Command Reference - Claude Code Framework

**Status:** Production Ready ✅

Comprehensive reference for all Claude Code Framework commands with intelligent command recognition and multi-language support.

## 🎯 Overview

The Claude Code Framework provides intelligent command recognition that automatically maps user inputs to appropriate agent-prompt combinations. Commands work in both Polish and English with fuzzy matching and intent recognition.

## 🔗 Command-Agent Mapping System

### Intelligent Recognition Features

- **Multi-Language Support** - Polish and English commands
- **Fuzzy Matching** - Recognizes partial and abbreviated commands
- **Intent Recognition** - Understands user intent beyond exact syntax
- **Context Awareness** - Adapts to current project and session context
- **Automatic Agent Activation** - Maps commands to appropriate agents and prompts

## 📋 Session Management Commands

### Core Session Operations

```bash
# Polish Commands
"zapisz sesję"              # Save current session state
"przywróć sesję"            # Restore previous session state
"odzyskaj sesję"            # Recover interrupted session
"rozpocznij sesję"          # Start new session with context analysis
"kontynuuj sesję"           # Continue previous session
"analiza kontekstu"         # Analyze current project context

# English Commands
"save session"              # Save current session state
"restore session"           # Restore previous session state
"recover session"           # Recover from interruption
"start session"             # Initialize new work session
"continue session"          # Resume previous session
"context analysis"          # Analyze project context
```

**Agent Activation:** All session commands automatically activate `session-manager` agent

### Session Management Integration

```bash
# Advanced Session Operations
"session state validation"  # Validate session integrity
"session handoff"          # Team transition management
"session context recovery" # Context corruption recovery
```

## 🔧 Serena MCP Integration Commands

### MCP Tools Synchronization

```bash
# Polish Commands
"serena sync"               # Synchronize with Serena index
"serena update"             # Update project index
"przeindeksuj projekt"      # Reindex project knowledge base
"zaktualizuj indeks"        # Update index with recent changes
"status serena"             # Check Serena integration status
"sprawdź serena"            # Verify Serena availability

# English Commands
"serena sync"               # Synchronize project index
"serena update"             # Update knowledge base
"reindex project"           # Rebuild project index
"update index"              # Refresh index
"serena status"             # Check integration status
"check serena"              # Verify Serena availability
```

**Agent Activation:** Serena commands activate `session-manager` with MCP integration

**Automatic Detection:** Framework automatically detects `.serena` directory for enhanced capabilities

## 🏗️ Project Management Commands

### Project Operations

```bash
# Polish Commands
"sprawdź projekt"           # Check project health and status
"health check"              # Comprehensive project health assessment
"zdrowie projektu"          # Project health analysis
"nowy projekt"              # Initialize new project with framework
"istniejący projekt"        # Add framework to existing project
"przygotuj release"         # Prepare project for release
"modernizuj strukturę"      # Modernize project structure
"automatyzacja projektu"    # Setup project automation
"inicjalizacja"             # Project initialization

# English Commands
"check project"             # Project health assessment
"health check"              # Comprehensive project analysis
"new project"               # Initialize new project
"existing project"          # Integrate with existing project
"prepare release"           # Release preparation workflow
"modernize structure"       # Structure modernization
"project automation"        # Automation setup
"initialization"            # Framework initialization
```

**Agent Activation:** Project commands activate `project-owner` agent

## 📊 Business Analysis Commands

### Requirements and Analysis

```bash
# Polish Commands
"analiza biznesowa"         # Business analysis and requirements
"wymagania"                 # Requirements gathering
"case study"                # Business case development
"studium przypadku"         # Business case analysis
"stakeholder"               # Stakeholder management
"interesariusze"            # Stakeholder analysis
"proces biznesowy"          # Business process analysis

# English Commands
"business analysis"         # Business requirements analysis
"requirements"              # Requirements gathering
"case study"                # Business case development
"stakeholder"               # Stakeholder management
"business process"          # Process analysis
"requirements gathering"    # Detailed requirements collection
```

**Agent Activation:** Business commands activate `business-analyst` agent

## 🎨 Product Management Commands

### Product Strategy and Planning

```bash
# Polish Commands
"planowanie produktu"       # Product planning and strategy
"user stories"              # User story creation
"historie użytkownika"      # User story development
"roadmap"                   # Product roadmap planning
"mapa drogowa"              # Roadmap development
"MVP"                       # MVP scoping and planning
"feature"                   # Feature implementation
"funkcjonalność"            # Feature development

# English Commands
"product planning"          # Product strategy and planning
"user stories"              # User story creation and prioritization
"roadmap"                   # Product roadmap development
"MVP"                       # MVP scoping and planning
"feature"                   # Feature implementation planning
"product strategy"          # Strategic product planning
```

**Agent Activation:** Product commands activate `product-manager` agent

## 💻 Development Commands

### Frontend Development

```bash
# Polish/English Commands
"frontend"                  # Frontend development tasks
"front-end"                 # Frontend engineering
"React"                     # React-specific development
"Angular"                   # Angular-specific development
"Vue"                       # Vue.js-specific development
"component"                 # Component development
"UI"                        # User interface development
"responsive design"         # Responsive web design
```

**Agent Activation:** Frontend commands activate `frontend-engineer` agent

### Backend Development

```bash
# Polish/English Commands
"backend"                   # Backend development tasks
"back-end"                  # Backend engineering
"server"                    # Server-side development
"database"                  # Database operations
"baza danych"               # Database management
"ETL"                       # Data pipeline development
"data processing"           # Data processing tasks
```

**Agent Activation:** Backend commands activate `backend-engineer` agent

### API Development

```bash
# Polish/English Commands
"API"                       # API development
"interfejs API"             # API interface development
"REST API"                  # REST API design and implementation
"GraphQL"                   # GraphQL API development
"microservices"             # Microservices architecture
"mikroserwisy"              # Microservices development
"service integration"      # Service integration tasks
```

**Agent Activation:** API commands activate `api-engineer` agent

## 🔍 Quality & Security Commands

### Testing and Quality Assurance

```bash
# Polish Commands
"testy"                     # Testing and quality assurance
"testing"                   # Test automation
"quality"                   # Quality assurance
"jakość"                    # Quality management
"performance"               # Performance optimization
"wydajność"                 # Performance testing
"test automation"           # Automated testing

# English Commands
"tests"                     # Testing tasks
"testing"                   # Quality assurance testing
"quality"                   # Quality management
"performance"               # Performance optimization
"load testing"              # Performance testing
"test automation"           # Automated testing frameworks
```

**Agent Activation:** Quality commands activate `qa-engineer` agent

### Security Operations

```bash
# Polish Commands
"security"                  # Security engineering
"bezpieczeństwo"            # Security implementation
"threat modeling"           # Threat modeling and analysis
"modelowanie zagrożeń"      # Threat analysis
"penetration test"          # Security testing
"test penetracyjny"         # Penetration testing
"code review"               # Security code review
"przegląd kodu"             # Code security analysis

# English Commands
"security"                  # Security engineering
"threat modeling"           # Security threat analysis
"penetration test"          # Security testing
"security audit"            # Security assessment
"code review"               # Security code review
"vulnerability assessment"  # Security vulnerability analysis
```

**Agent Activation:** Security commands activate `security-engineer` agent

## 🏗️ Architecture & Design Commands

### System Architecture

```bash
# Polish/English Commands
"architektura"              # System architecture design
"architecture"              # Architecture planning
"system design"             # System architecture
"scalability"               # Scalability planning
"enterprise architecture"   # Enterprise-level architecture
"design patterns"           # Architectural patterns
```

**Agent Activation:** Architecture commands activate `software-architect` agent

### User Experience Design

```bash
# Polish/English Commands
"UX"                        # User experience design
"user experience"           # UX design and research
"design system"             # Design system development
"system projektowania"      # Design system creation
"accessibility"             # Accessibility design
"dostępność"                # Accessible design
"user research"             # User research and analysis
```

**Agent Activation:** UX commands activate `ux-designer` agent

## 🚀 Deployment & Operations Commands

### Deployment and Infrastructure

```bash
# Polish/English Commands
"deployment"                # Deployment operations
"wdrożenie"                 # Deployment management
"CI/CD"                     # CI/CD pipeline operations
"infrastructure"            # Infrastructure management
"infrastruktura"            # Infrastructure setup
"container"                 # Containerization
"Docker"                    # Docker operations
"Kubernetes"                # Kubernetes orchestration
```

**Agent Activation:** Deployment commands activate `deployment-engineer` agent

## 🔍 Review & Validation Commands

### Code Review and Validation

```bash
# Polish/English Commands
"review"                    # Code and architecture review
"przegląd"                  # Review operations
"validate"                  # Validation tasks
"walidacja"                 # Validation processes
"audit"                     # Audit operations
"audyt"                     # Audit procedures
"compliance"                # Compliance validation
"zgodność"                  # Compliance checking
"quality gate"              # Quality gate validation
"brama jakości"             # Quality assurance gates
```

**Agent Activation:** Review commands activate `reviewer` agent

## 🎯 Command Recognition Rules

### Language Support

- **Polish Commands** - Native Polish language support with technical terms
- **English Commands** - Standard English command recognition
- **Mixed Language** - Handles code-switching between Polish and English
- **Technical Terms** - Recognizes technical terms in both languages

### Context Awareness

- **Project Context** - Commands adapt to current project type and technology stack
- **Session Context** - Understands ongoing work and previous agent interactions
- **Task Context** - Maps commands to appropriate complexity level of prompts
- **User Preference** - Adapts to user's preferred communication style
- **MCP Tools Detection** - Automatically enhances commands when Serena MCP is active

### Fuzzy Matching

- **Partial Commands** - Recognizes incomplete or abbreviated commands
- **Synonyms** - Handles multiple ways of expressing the same intent
- **Technical Variations** - Maps technical variations to standard commands
- **Intent Recognition** - Understands user intent with non-standard phrasing

### Multi-Command Handling

- **Compound Commands** - Processes multiple commands in single request
- **Sequential Processing** - Executes complex workflows with multiple agents
- **Dependency Resolution** - Understands command dependencies and execution order
- **Batch Operations** - Groups related commands for efficient execution

## 🔧 Advanced Command Features

### Automatic Agent Coordination

```bash
# Example: Complex workflow commands
"full project setup"        # Activates project-owner → business-analyst → software-architect
"security audit"            # Activates security-engineer → compliance-auditor → reviewer
"performance optimization"  # Activates performance-engineer → qa-engineer → monitoring-engineer
```

### Context-Sensitive Recommendations

The framework provides intelligent command suggestions based on:
- Current project state and configuration
- Previous command history and patterns
- Detected technology stack and requirements
- Active session context and ongoing work

### Error Handling and Recovery

- **Command Not Recognized** - Provides similar command suggestions
- **Missing Context** - Requests necessary context for command execution
- **Agent Unavailable** - Suggests alternative agents or approaches
- **Integration Failure** - Provides fallback commands and recovery options

## ⚡ Slash Commands

**New in Framework v3.1.0:** Complete collection of specialized slash commands for rapid development workflows.

The framework provides 28 specialized slash commands organized in 7 categories for instant access to specific functionality without menu navigation.

### 🤖 Agent Management Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/agent-select [technology]` | Automatic agent selection based on tech stack | `/agent-select "python wxpython"` |
| `/agent-status` | Display all active agents and their workload | `/agent-status --detailed` |
| `/agent-handoff [from] [to]` | Transfer tasks between agents | `/agent-handoff desktop-specialist backend-engineer` |
| `/agent-expertise [domain]` | Find agents with specific expertise | `/agent-expertise "database optimization"` |

### 📊 Project Analysis Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/health-check` | Comprehensive project health analysis | `/health-check --detailed` |
| `/stack-analysis` | Technology stack compatibility analysis | `/stack-analysis --recommendations` |
| `/dependency-check` | Dependencies and security validation | `/dependency-check --security` |
| `/architecture-review` | Architecture review with software-architect | `/architecture-review --patterns` |

### ⚡ AI-Tools Shortcuts

| Command | Description | Example |
|---------|-------------|---------|
| `/ai-setup` | Quick AI tools setup without menu | `/ai-setup --advanced` |
| `/ai-validate` | Fast quality validation | `/ai-validate --fix` |
| `/ai-optimize` | Performance optimization suggestions | `/ai-optimize --performance` |
| `/ai-troubleshoot` | Debug AI tools issues | `/ai-troubleshoot --verbose` |

### 🔧 Framework Management Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/framework-update` | Update framework in project | `/framework-update --backup` |
| `/framework-sync` | Sync with main framework repo | `/framework-sync --agents-only` |
| `/framework-backup` | Backup current configuration | `/framework-backup --compress` |
| `/framework-restore [backup]` | Restore from backup | `/framework-restore fw-backup-a7f8d9e2` |

### 📋 TodoWrite Integration Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/todo-epic [name]` | Create new epic with task breakdown | `/todo-epic "User Authentication System"` |
| `/todo-sprint` | Display current sprint status | `/todo-sprint --planning` |
| `/todo-agent-tasks [agent]` | Tasks assigned to specific agent | `/todo-agent-tasks backend-engineer` |
| `/todo-dependencies` | Analyze task dependencies | `/todo-dependencies --critical-path` |

### 🚀 Workflow Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/start-feature [name]` | Initialize feature with agent team | `/start-feature "Real-time Collaboration"` |
| `/code-review` | Multi-agent code review | `/code-review --security-focus` |
| `/testing-strategy` | Setup comprehensive testing | `/testing-strategy --performance` |
| `/deployment-prep` | Deployment preparation | `/deployment-prep --environment=production` |

### 🔍 Development Helpers

| Command | Description | Example |
|---------|-------------|---------|
| `/find-agent [skill]` | Find agent with specific skill | `/find-agent "opengl programming"` |
| `/quick-docs [topic]` | Instant documentation access | `/quick-docs wxpython` |
| `/example-code [pattern]` | Code examples for patterns | `/example-code "mvc pattern"` |
| `/best-practices [area]` | Best practices for development area | `/best-practices python` |

### Command Features

**Intelligent Integration:**
- **Auto-completion** - Smart suggestions based on project context
- **Agent Routing** - Automatic agent assignment for each command
- **Context Awareness** - Commands adapt to current project state
- **TodoWrite Sync** - Automatic task creation and progress tracking
- **Multi-Agent Coordination** - Seamless agent collaboration

**Usage Patterns:**
```bash
# Quick project health check
/health-check

# Start new feature development
/start-feature "Export System"

# Get help with specific technology
/quick-docs "sqlite optimization"

# Find expert for specific domain
/find-agent "performance optimization"

# Setup comprehensive testing
/testing-strategy --feature="export-system"
```

**Command Documentation:**
Each slash command has complete documentation in `.claude/commands/` directory with detailed usage examples, options, and integration patterns.

---

**See also:**
- [Slash Commands](slash-commands.md) - Complete slash commands reference and guide
- [Agent Reference](agent-reference.md) - Complete agent documentation
- [Prompt Reference](prompt-reference.md) - Agent-specific prompts
- [Session Management](session-management.md) - Session commands detailed usage