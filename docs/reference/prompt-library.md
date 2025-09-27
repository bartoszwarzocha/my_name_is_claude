# Prompt Library - My Name Is Claude

**Status:** Production Ready ✅

The comprehensive prompts library for the Claude Code Multi-Agent Framework, featuring specialized agent prompts, session management, project initialization, and complete workflow orchestration capabilities.

## 🎯 Framework Overview

The Claude Code Multi-Agent Framework provides:

- **Specialized AI Agents** covering complete enterprise development ecosystem
- **Professional Prompts Library** with functional design patterns and agent-prompt binding
- **Technology-Agnostic Architecture** adaptable to any development stack
- **Hierarchical TODO Management** with enterprise-grade task coordination
- **Advanced Session Management** with MCP tools integration and context analysis
- **Revolutionary Agent-Prompt Binding** with automatic agent activation system
- **Project Initialization Automation** from concept to production-ready configuration

### Core Principles

✅ **Functional Design**: Prompts describe WHAT to accomplish, not HOW to implement
✅ **Technology Agnostic**: Works across different technology stacks and project scales
✅ **CLAUDE.md Integration**: Adapts to project configuration and requirements
✅ **Measurable Criteria**: Clear, testable success conditions for all operations
✅ **Enterprise Ready**: Scalable from startup to enterprise-grade implementations

## 📁 Directory Structure

```
.claude/prompts/
├── init/                       # Project initialization system
│   ├── new-project.md          # New project framework setup
│   ├── existing-project.md     # Existing project framework integration
│   ├── claude_md_from_concept.md  # CLAUDE.md generation from concepts
│   └── prepare_instruction.md  # Development workflow generator
├── agents/                     # Agent-specific prompts with automatic binding
│   ├── api/                   # API engineering (api-engineer)
│   ├── architecture/          # System architecture (software-architect)
│   ├── automation/            # Automation engineering (automation-engineer)
│   ├── backend/               # Backend engineering (backend-engineer)
│   ├── business/              # Business analysis (business-analyst)
│   ├── capacity/              # Capacity planning (capacity-planner)
│   ├── cloud/                 # Cloud engineering (cloud-engineer)
│   ├── compliance/            # Compliance auditing (compliance-auditor)
│   ├── data/                  # Data engineering (data-engineer)
│   ├── database/              # Database administration (database-administrator)
│   ├── deployment/            # DevOps deployment (deployment-engineer)
│   ├── design/                # UX/UI design (ux-designer)
│   ├── devops/                # DevOps architecture (devops-architect)
│   ├── documentation/         # Technical writing (technical-writer)
│   ├── enterprise/            # Enterprise architecture (enterprise-architect)
│   ├── frontend/              # Frontend development (frontend-engineer)
│   ├── governance/            # Governance architecture (governance-architect)
│   ├── incident/              # Incident response (incident-responder)
│   ├── integration/           # Integration architecture (integration-architect)
│   ├── middleware/            # Middleware engineering (middleware-engineer)
│   ├── mobile/                # Mobile development (mobile-developer)
│   ├── monitoring/            # Monitoring engineering (monitoring-engineer)
│   ├── network/               # Network architecture (network-architect)
│   ├── performance/           # Performance engineering (performance-engineer)
│   ├── planner/               # Product management (product-manager)
│   ├── platform/              # Platform engineering (platform-engineer)
│   ├── project/               # Project coordination (project-coordinator)
│   ├── quality/               # Quality assurance (qa-engineer)
│   ├── reliability/           # Reliability engineering (reliability-engineer)
│   ├── risk/                  # Risk management (risk-manager)
│   ├── security/              # Security engineering (security-engineer)
│   ├── session/               # Session management (session-manager)
│   └── sre/                   # Site reliability engineering (sre-engineer)
└── workflows/                  # Multi-agent orchestration
    ├── parallel-coordination/ # Cross-team coordination
    ├── phase-transitions/     # Workflow handoffs
    └── quality-gates/         # Validation checkpoints
```

## 🔗 Agent-Prompt Binding System

### Automatic Agent Activation

The framework implements revolutionary **directory-based agent binding**:

```
.claude/prompts/agents/[category]/ → Activates corresponding agent
```

**Examples:**
- `.claude/prompts/agents/api/rest-api-design.md` → **Automatically activates** `api-engineer`
- `.claude/prompts/agents/frontend/react-component.md` → **Automatically activates** `frontend-engineer`
- `.claude/prompts/agents/security/threat-modeling.md` → **Automatically activates** `security-engineer`

### Prompt Header Requirements

Every agent-specific prompt includes:

```markdown
**🤖 AGENT ACTIVATION:** This prompt automatically activates the `[agent-name]` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.
```

## 🚀 How to Use Prompts

### 1. Direct File Usage

Copy prompt content directly into Claude Code chat:

```bash
# Copy prompt to clipboard
cat .claude/prompts/agents/api/rest-api-design.md | clip
```

### 2. Agent Activation via Directory Structure

When using any prompt from `.claude/prompts/agents/[category]/`:
1. **Agent automatically activates** based on directory
2. **Context loads** from CLAUDE.md configuration
3. **TODO integration** manages task workflow
4. **Quality assurance** applies enterprise standards

### 3. Session Integration

For session management prompts:

```bash
# Session commands
"zapisz sesję" / "save session"
"przywróć sesję" / "restore session"
"rozpocznij sesję" / "start session"
```

## 📋 Prompt Categories

### **Project Initialization**
- **new-project.md** - New project framework setup
- **existing-project.md** - Add framework to existing project
- **claude_md_from_concept.md** - Generate CLAUDE.md from project concept

### **Session Management**
- **session-start-and-context-analysis.md** - Initialize new work session
- **session-continuation-from-summary.md** - Resume previous session
- **session-end-and-summary-generation.md** - Close and summarize session
- **serena-sync-and-update.md** - MCP tools integration

### **Agent-Specific Prompts**
All agent categories have specialized prompts that:
- **Automatically activate** the corresponding agent
- **Adapt to project technology stack** via CLAUDE.md
- **Integrate with TODO workflow** for task coordination
- **Follow functional design principles** (WHAT not HOW)

## 🎯 Creating Custom Prompts

### Template Structure

Use `PROMPT_TEMPLATE.md` as starting point:

```markdown
# [Prompt Title]

**🤖 AGENT ACTIVATION:** [If agent-specific]
**📋 FUNCTIONAL REQUIREMENTS:** What needs to be accomplished
**🔄 HIGH-LEVEL ALGORITHMS:** How to approach the problem
**✅ VALIDATION CRITERIA:** Success conditions
**💡 USAGE EXAMPLES:** Cross-technology scenarios
```

### Quality Standards

✅ **Functional Requirements** - Clear WHAT description
✅ **Technology Agnostic** - Works across different stacks
✅ **CLAUDE.md Integration** - Adapts to project configuration
✅ **Validation Criteria** - Measurable success conditions
✅ **Usage Examples** - Multiple technology scenarios

## 🔧 Integration with Claude Code

### Framework Configuration

Prompts automatically adapt based on CLAUDE.md:

```yaml
# Project configuration influences prompt behavior
primary_language: "typescript"  # Affects code examples
business_domain: "fintech"      # Affects compliance focus
project_scale: "enterprise"    # Affects complexity handling
```

### TodoWrite Integration

All prompts integrate with TodoWrite workflow:
- **Automatic task creation** based on prompt complexity
- **Hierarchical task management** (Epic→Feature→Task→Subtask)
- **Cross-agent coordination** for complex workflows
- **Progress tracking** with real-time status updates

## 📚 Best Practices

### For Prompt Usage
1. **Read CLAUDE.md first** - Understand project context
2. **Use appropriate agent prompts** - Let automatic activation work
3. **Follow functional patterns** - Focus on outcomes not implementation
4. **Validate results** - Check against prompt success criteria

### For Prompt Development
1. **Start with template** - Use established structure
2. **Test across technologies** - Ensure technology agnostic design
3. **Validate quality gates** - Meet all framework standards
4. **Document integration points** - Clear agent coordination

---

**See also:**
- [Agent System](agent-system.md) - Complete agent documentation
- [TODO Management](todo-management.md) - Hierarchical task system
- [Session Management](session-management.md) - State and context management