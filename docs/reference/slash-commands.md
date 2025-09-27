# Slash Commands - Complete Reference

**Framework Version:** 3.1.0+
**Status:** Production Ready ✅
**Total Commands:** 28

The Claude Code Framework provides a comprehensive collection of slash commands for rapid access to specialized functionality without menu navigation.

## 📋 Quick Reference

### Command Categories Overview

| Category | Commands | Purpose |
|----------|----------|---------|
| **🤖 Agent Management** | 4 commands | Agent selection, status, handoffs, expertise finding |
| **📊 Project Analysis** | 4 commands | Health checks, stack analysis, dependency validation |
| **⚡ AI-Tools Shortcuts** | 4 commands | Quick setup, validation, optimization, troubleshooting |
| **🔧 Framework Management** | 4 commands | Updates, sync, backup, restore operations |
| **📋 TodoWrite Integration** | 4 commands | Epic creation, sprint management, task coordination |
| **🚀 Workflow Commands** | 4 commands | Feature development, code review, testing, deployment |
| **🔍 Development Helpers** | 4 commands | Agent finding, documentation, examples, best practices |

## 🤖 Agent Management Commands

### `/agent-select [technology]`
**Purpose:** Automatic agent selection based on technology stack

**Usage:**
```bash
/agent-select python
/agent-select "wxpython opengl"
/agent-select cpp
/agent-select "react typescript"
```

**Output:** Ranked list of agents with relevance scores and coordination recommendations

**Integration:** Reads CLAUDE.md, analyzes tech stack, assigns agents automatically

---

### `/agent-status`
**Purpose:** Display all active agents and their current workload

**Usage:**
```bash
/agent-status
/agent-status --detailed
/agent-status --active-only
```

**Output:** Comprehensive dashboard showing agent status, tasks, collaboration patterns

**Features:** Real-time TodoWrite integration, performance metrics, workload assessment

---

### `/agent-handoff [from] [to]`
**Purpose:** Transfer tasks or context between agents

**Usage:**
```bash
/agent-handoff desktop-specialist backend-engineer
/agent-handoff current qa-engineer
/agent-handoff "frontend-engineer backend-engineer" qa-engineer
```

**Features:** Context preservation, TodoWrite task reassignment, coordination setup

---

### `/agent-expertise [domain]`
**Purpose:** Find agents with specific expertise

**Usage:**
```bash
/agent-expertise opengl
/agent-expertise "database design"
/agent-expertise security
/agent-expertise "performance optimization"
```

**Output:** Ranked experts with competency analysis and project-specific recommendations

## 📊 Project Analysis Commands

### `/health-check`
**Purpose:** Comprehensive project health analysis

**Usage:**
```bash
/health-check
/health-check --detailed
/health-check --fix-issues
```

**Analysis Areas:**
- Framework integration status
- Project configuration validity
- Development environment setup
- Agent ecosystem health
- Quality standards compliance

---

### `/stack-analysis`
**Purpose:** Technology stack compatibility and optimization analysis

**Usage:**
```bash
/stack-analysis
/stack-analysis --recommendations
/stack-analysis --compatibility
```

**Features:**
- Version compatibility matrix
- Performance characteristics analysis
- Security considerations
- Alternative technology suggestions

---

### `/dependency-check`
**Purpose:** Dependencies and security validation

**Usage:**
```bash
/dependency-check
/dependency-check --security
/dependency-check --outdated
/dependency-check --fix
```

**Checks:**
- Compatibility issues
- Security vulnerabilities
- Available updates
- License compatibility

---

### `/architecture-review`
**Purpose:** Architecture review with software-architect agent

**Usage:**
```bash
/architecture-review
/architecture-review --detailed
/architecture-review --patterns
```

**Review Areas:**
- System architecture assessment
- Design pattern analysis
- Scalability evaluation
- Refactoring recommendations

## ⚡ AI-Tools Shortcuts

### `/ai-setup`
**Purpose:** Quick AI tools setup without interactive menu

**Usage:**
```bash
/ai-setup
/ai-setup --force
/ai-setup --advanced
```

**Setup Process:**
1. Environment validation
2. Virtual environment creation
3. Dependencies installation
4. Agent discovery
5. MCP tools configuration

---

### `/ai-validate`
**Purpose:** Fast quality validation

**Usage:**
```bash
/ai-validate
/ai-validate --fix
/ai-validate --strict
```

**Validation Areas:**
- Code quality standards
- Agent configuration compliance
- Framework integration health
- Testing coverage
- Security compliance

---

### `/ai-optimize`
**Purpose:** Performance optimization suggestions

**Usage:**
```bash
/ai-optimize
/ai-optimize --performance
/ai-optimize --memory
/ai-optimize --agents
```

**Optimization Focus:**
- Code performance analysis
- Memory usage optimization
- Agent coordination efficiency
- Framework resource utilization

---

### `/ai-troubleshoot`
**Purpose:** Debug AI tools issues

**Usage:**
```bash
/ai-troubleshoot
/ai-troubleshoot --verbose
/ai-troubleshoot --fix-common
```

**Diagnostic Coverage:**
- Virtual environment problems
- Agent configuration errors
- MCP tools connectivity
- Performance issues

## 🔧 Framework Management Commands

### `/framework-update`
**Purpose:** Update framework in current project

**Usage:**
```bash
/framework-update
/framework-update --check-only
/framework-update --force
/framework-update --backup
```

**Update Process:**
1. Version compatibility check
2. Automatic backup creation
3. Selective component updates
4. Configuration migration
5. Validation and verification

---

### `/framework-sync`
**Purpose:** Sync with main framework repository

**Usage:**
```bash
/framework-sync
/framework-sync --pull-only
/framework-sync --agents-only
```

**Sync Components:**
- Agent definitions updates
- Prompt library enhancements
- Framework tools improvements
- Documentation updates

---

### `/framework-backup`
**Purpose:** Backup current framework configuration

**Usage:**
```bash
/framework-backup
/framework-backup --name="pre-update-backup"
/framework-backup --compress
```

**Backup Contents:**
- Framework configuration files
- Agent definitions and assignments
- Custom prompts and hooks
- Project-specific overrides

---

### `/framework-restore [backup-id]`
**Purpose:** Restore from framework backup

**Usage:**
```bash
/framework-restore fw-backup-a7f8d9e2
/framework-restore --latest
/framework-restore --preview fw-backup-a7f8d9e2
```

**Restoration Features:**
- Selective component restoration
- Conflict resolution
- Safety backup creation
- Validation verification

## 📋 TodoWrite Integration Commands

### `/todo-epic [name]`
**Purpose:** Create new epic with automatic task breakdown

**Usage:**
```bash
/todo-epic "User Authentication System"
/todo-epic "Advanced Export Features" --template=feature
/todo-epic "Performance Optimization" --priority=high
```

**Epic Structure:**
- Automatic feature breakdown
- Agent assignment suggestions
- Timeline estimation
- Success criteria definition

---

### `/todo-sprint`
**Purpose:** Display current sprint status and progress

**Usage:**
```bash
/todo-sprint
/todo-sprint --planning
/todo-sprint --review
```

**Sprint Management:**
- Task progress tracking
- Agent workload distribution
- Sprint metrics analysis
- Velocity calculation

---

### `/todo-agent-tasks [agent]`
**Purpose:** Show tasks assigned to specific agent

**Usage:**
```bash
/todo-agent-tasks backend-engineer
/todo-agent-tasks desktop-specialist --status=active
/todo-agent-tasks qa-engineer --timeline
```

**Task Information:**
- Active task status
- Progress tracking
- Collaboration status
- Performance metrics

---

### `/todo-dependencies`
**Purpose:** Analyze task dependencies and critical paths

**Usage:**
```bash
/todo-dependencies
/todo-dependencies --critical-path
/todo-dependencies --blocking
```

**Analysis Features:**
- Dependency graph visualization
- Critical path identification
- Bottleneck detection
- Optimization recommendations

## 🚀 Workflow Commands

### `/start-feature [name]`
**Purpose:** Initialize new feature with agent team

**Usage:**
```bash
/start-feature "Real-time Collaboration"
/start-feature "Advanced Search" --template=search
/start-feature "User Preferences" --agents="desktop-specialist,backend-engineer"
```

**Initialization Process:**
1. Feature analysis and scoping
2. Automatic agent team formation
3. Task breakdown and assignment
4. Workflow coordination setup
5. Quality gates configuration

---

### `/code-review`
**Purpose:** Multi-agent code review

**Usage:**
```bash
/code-review
/code-review --files="src/export/*.py"
/code-review --security-focus
/code-review --performance-focus
```

**Review Process:**
- Parallel multi-agent analysis
- Security assessment
- Performance evaluation
- Architecture validation
- Consolidated recommendations

---

### `/testing-strategy`
**Purpose:** Setup comprehensive testing strategy

**Usage:**
```bash
/testing-strategy
/testing-strategy --feature="export-system"
/testing-strategy --performance
/testing-strategy --security
```

**Strategy Components:**
- Testing pyramid design
- Framework integration
- Performance benchmarks
- Security testing protocols
- CI/CD integration

---

### `/deployment-prep`
**Purpose:** Deployment preparation and validation

**Usage:**
```bash
/deployment-prep
/deployment-prep --environment=production
/deployment-prep --platform=windows
/deployment-prep --checklist
```

**Preparation Areas:**
- Code quality validation
- Build and packaging
- Documentation completeness
- Environment configuration
- Risk assessment

## 🔍 Development Helpers

### `/find-agent [skill]`
**Purpose:** Find agent with specific skill or expertise

**Usage:**
```bash
/find-agent opengl
/find-agent "database optimization"
/find-agent testing
/find-agent "user interface design"
```

**Search Features:**
- Multi-domain skill matching
- Experience level filtering
- Project context integration
- Collaboration recommendations

---

### `/quick-docs [topic]`
**Purpose:** Instant access to documentation

**Usage:**
```bash
/quick-docs wxpython
/quick-docs "sqlite optimization"
/quick-docs framework
/quick-docs agents
```

**Documentation Sources:**
- Framework documentation
- Agent usage guides
- Technology references
- Code examples
- Best practices

---

### `/example-code [pattern]`
**Purpose:** Code examples for specific patterns

**Usage:**
```bash
/example-code "mvc pattern"
/example-code "database connection"
/example-code "export functionality"
/example-code "error handling"
```

**Example Features:**
- Technology-specific implementations
- Complete working examples
- Best practices integration
- Testing strategies
- Performance considerations

---

### `/best-practices [area]`
**Purpose:** Best practices for development areas

**Usage:**
```bash
/best-practices python
/best-practices "gui development"
/best-practices security
/best-practices "database design"
```

**Practice Categories:**
- Language-specific guidelines
- Framework best practices
- Security recommendations
- Performance optimization
- Testing methodologies

## 🎯 Command Features

### Intelligent Integration
- **Auto-completion:** Smart suggestions based on project context
- **Agent Routing:** Automatic agent assignment for each command
- **Context Awareness:** Commands adapt to current project state
- **TodoWrite Sync:** Automatic task creation and progress tracking
- **Multi-Agent Coordination:** Seamless agent collaboration

### Usage Patterns

**Quick Development Cycle:**
```bash
# Health check and setup
/health-check
/ai-setup

# Feature development
/start-feature "New Export Format"
/find-agent "file format expertise"
/example-code "file export pattern"

# Quality assurance
/code-review
/testing-strategy
/ai-validate

# Deployment
/deployment-prep
```

**Troubleshooting Workflow:**
```bash
# Diagnose issues
/health-check --detailed
/dependency-check --security
/ai-troubleshoot

# Get help
/quick-docs troubleshooting
/find-agent "debugging expertise"
/best-practices "error handling"
```

**Project Management:**
```bash
# Epic and sprint management
/todo-epic "Performance Optimization"
/todo-sprint --planning
/todo-dependencies --critical-path

# Agent coordination
/agent-status
/agent-handoff current qa-engineer
/todo-agent-tasks backend-engineer
```

## 🔧 Implementation Details

### Command Storage
All slash commands are stored in `.claude/commands/` directory with complete documentation including:
- Detailed functionality descriptions
- Usage examples and options
- Integration patterns
- Output format specifications

### Framework Integration
- Commands integrate with existing agent system
- TodoWrite automatic synchronization
- Session state preservation
- Quality gate enforcement
- Performance monitoring

### Extensibility
The command system is designed for easy extension:
- Add new commands by creating `.md` files in `.claude/commands/`
- Follow established documentation patterns
- Integrate with agent system for functionality
- Maintain consistency with existing command structure

---

**Related Documentation:**
- [Command Reference](command-reference.md) - Complete command system overview
- [Agent Reference](agent-reference.md) - Agent system documentation
- [TodoWrite Management](todo-management.md) - Task management integration
- [Framework Customization](../advanced/framework-customization.md) - Extending the framework