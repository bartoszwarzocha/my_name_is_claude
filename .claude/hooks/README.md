# Claude Code Hooks - Multi-Agent Framework

Automated hooks for the Claude Code Multi-Agent Framework to enhance workflow automation, quality assurance, and coordination between agents.

## 📁 Available Hooks

## Basic Framework Hooks

### 1. **user-prompt-submit-hook.sh**

- **Purpose:** Automatically tracks documentation changes and updates prompt statistics
- **Triggers:** When user submits prompts that might affect documentation
- **What it does:**
  - Detects changes in `.md` and `.puml` files
  - Counts current prompts and updates statistics
  - Logs documentation updates to `work/documentation-updates.log`
  - Maintains documentation consistency

**Usage in Claude Code settings:**
```json
{
  "hooks": {
    "user-prompt-submit": ".claude/hooks/user-prompt-submit-hook.sh"
  }
}
```

### 2. **pre-commit-validation.sh**

- **Purpose:** Validates agent prompt structure and framework integrity
- **Triggers:** Before committing changes (manual execution or git pre-commit)
- **What it does:**
  - Checks all agent prompts for required sections (Mission, Process, Deliverables)
  - Validates agent directory structure
  - Ensures no empty prompt files
  - Prevents broken framework commits

**Manual Usage:**
```bash
./.claude/hooks/pre-commit-validation.sh
```

### 3. **post-commit-sync.sh**

- **Purpose:** Synchronizes prompt counts and framework statistics after changes
- **Triggers:** After successful commits (manual or automated)
- **What it does:**
  - Counts prompts per agent type
  - Updates `work/current-stats.md` with latest statistics
  - Maintains `work/sync-activity.log`
  - Keeps documentation aligned with actual state

**Manual Usage:**
```bash
./.claude/hooks/post-commit-sync.sh
```

### 4. **task-start-logger.sh**

- **Purpose:** Logs multi-agent task coordination and prevents conflicts
- **Triggers:** When starting agent-specific tasks
- **What it does:**
  - Logs task initiation to `work/agent-activity.log`
  - Tracks active agents and potential coordination needs
  - Maintains task timeline for workflow analysis
  - Provides conflict detection between agent types

**Usage:**
```bash
./.claude/hooks/task-start-logger.sh "frontend-engineer" "Angular component development"
```

### 5. **quality-gate-checker.sh**

- **Purpose:** Runs specialized quality checks based on agent type
- **Triggers:** During code review or quality validation phases  
- **What it does:**
  - Security-specific validation for security-engineer
  - Frontend standards checking for frontend-engineer
  - Review completeness validation for reviewer
  - Logs quality gate results to `work/quality-gates.log`

**Usage:**
```bash
./.claude/hooks/quality-gate-checker.sh "security-engineer" "threat-modeling"
```

## Advanced Multi-Agent Hooks

### 6. **agent-handoff.sh**

- **Purpose:** Automates work handoff between agents in different workflow phases
- **Triggers:** When transitioning work from one agent to another
- **What it does:**
  - Validates proper phase transitions (Discovery → Architecture → Development → Deployment)
  - Creates structured handoff records with required actions for receiving agent
  - Tracks collaboration points and coordination needs
  - Identifies potential workflow issues and blocking dependencies

**Usage:**
```bash
./.claude/hooks/agent-handoff.sh "business-analyst" "software-architect" "Business requirements and user stories completed"
```

### 7. **prompt-quality-validator.sh**

- **Purpose:** Validates quality and completeness of agent prompts
- **Triggers:** When creating or modifying agent prompts
- **What it does:**
  - Checks markdown structure and required sections (Mission, Process, Deliverables)
  - Validates content completeness and technical accuracy
  - Generates quality reports with scoring and recommendations
  - Ensures agent prompts follow framework standards

**Usage:**
```bash
# Validate specific prompt
./.claude/hooks/prompt-quality-validator.sh ".claude/prompts/agents/security/threat-modeling.md"

# Validate all prompts comprehensively
./.claude/hooks/prompt-quality-validator.sh "" "comprehensive"
```

### 8. **cross-agent-dependency-tracker.sh**

- **Purpose:** Tracks and validates dependencies between agents
- **Triggers:** Throughout multi-agent workflow execution
- **What it does:**
  - Maps dependencies between agents (e.g., frontend needs security requirements)
  - Validates that required agent outputs are available before dependent work starts
  - Generates dependency reports and identifies blocking issues
  - Provides workflow optimization recommendations

**Usage:**
```bash
# Track all predefined dependencies
./.claude/hooks/cross-agent-dependency-tracker.sh "track"

# Validate dependencies for specific agent
./.claude/hooks/cross-agent-dependency-tracker.sh "validate" "frontend-engineer"

# Generate comprehensive dependency report
./.claude/hooks/cross-agent-dependency-tracker.sh "report"
```

### 9. **agent-performance-monitor.sh**

- **Purpose:** Monitors agent performance and execution metrics
- **Triggers:** At start and end of agent tasks
- **What it does:**
  - Tracks task execution time and system resource usage
  - Calculates performance scores based on deliverables and duration
  - Generates performance reports with trends and recommendations
  - Identifies workflow bottlenecks and optimization opportunities

**Usage:**
```bash
# Start monitoring
TASK_ID=$(./.claude/hooks/agent-performance-monitor.sh "start" "frontend-engineer")

# Stop monitoring (use returned TASK_ID)
./.claude/hooks/agent-performance-monitor.sh "stop" "frontend-engineer" "$TASK_ID"

# Generate performance report
./.claude/hooks/agent-performance-monitor.sh "report"
```

### 10. **compliance-automation.sh**

- **Purpose:** Automated compliance checking for WCAG, GDPR, SOX standards
- **Triggers:** During quality validation and before deployment
- **What it does:**
  - Validates WCAG 2.1 accessibility compliance for frontend work
  - Checks GDPR data protection compliance for security implementations
  - Verifies SOX internal controls for audit and review processes
  - Generates comprehensive compliance reports with remediation plans

**Usage:**
```bash
# Check WCAG compliance for frontend
./.claude/hooks/compliance-automation.sh "wcag" "frontend-engineer"

# Check GDPR compliance for security
./.claude/hooks/compliance-automation.sh "gdpr" "security-engineer"

# Run comprehensive compliance check
./.claude/hooks/compliance-automation.sh "all" "frontend-engineer"
```

### 11. **agent-conflict-resolution.sh**

- **Purpose:** Detects and resolves conflicts between agents
- **Triggers:** Throughout multi-agent workflow execution
- **What it does:**
  - Detects requirement conflicts between agents (security vs performance)
  - Identifies resource contention and overlapping responsibilities
  - Provides automated resolution strategies for common conflicts
  - Escalates high-severity conflicts for management review

**Usage:**
```bash
# Detect all types of conflicts
./.claude/hooks/agent-conflict-resolution.sh "detect"

# Resolve specific conflict types
./.claude/hooks/agent-conflict-resolution.sh "resolve" "requirements"

# Generate conflict resolution report
./.claude/hooks/agent-conflict-resolution.sh "report"

# Escalate unresolved high-severity conflicts
./.claude/hooks/agent-conflict-resolution.sh "escalate"
```

## 🚀 Quick Setup

### 1. Configure in Claude Code Settings

Add to your `.claude/settings.local.json`:

```json
{
  "hooks": {
    "user-prompt-submit": ".claude/hooks/user-prompt-submit-hook.sh"
  }
}
```

### 2. Git Integration (Optional)

For git integration, create symbolic links:

```bash
# In your git repository
ln -s ../../.claude/hooks/pre-commit-validation.sh .git/hooks/pre-commit
ln -s ../../.claude/hooks/post-commit-sync.sh .git/hooks/post-commit
```

### 3. Manual Execution

All hooks can be run manually for testing:

```bash
# Test basic framework hooks
./.claude/hooks/user-prompt-submit-hook.sh
./.claude/hooks/pre-commit-validation.sh
./.claude/hooks/post-commit-sync.sh
./.claude/hooks/task-start-logger.sh "test-agent" "testing"
./.claude/hooks/quality-gate-checker.sh "frontend-engineer"

# Test advanced multi-agent hooks
./.claude/hooks/agent-handoff.sh "test-from" "test-to" "test handoff"
./.claude/hooks/prompt-quality-validator.sh "" "comprehensive"
./.claude/hooks/cross-agent-dependency-tracker.sh "track"
./.claude/hooks/agent-performance-monitor.sh "analyze"
./.claude/hooks/compliance-automation.sh "all"
./.claude/hooks/agent-conflict-resolution.sh "detect"
```

## 📊 Hook Outputs and Logs

### Work Directory Files Created

#### Basic Framework Logs

- `work/documentation-updates.log` - Documentation change tracking
- `work/agent-activity.log` - Multi-agent task coordination log
- `work/current-stats.md` - Current framework statistics
- `work/sync-activity.log` - Prompt synchronization history
- `work/task-timeline.log` - Timeline of agent tasks
- `work/quality-gates.log` - Quality validation results

#### Advanced Multi-Agent Logs

- `work/handoffs/` - Agent handoff records and coordination plans
- `work/quality-reports/` - Prompt quality validation reports
- `work/dependencies/` - Agent dependency tracking and blocking issues
- `work/performance/` - Agent performance metrics and reports
- `work/compliance/` - Compliance audit reports (WCAG, GDPR, SOX)
- `work/conflicts/` - Agent conflict detection and resolution records

### Log File Formats

**agent-activity.log:**

```text
=====================================
TASK START: 2025-09-12 10:30:00
Agent: frontend-engineer
Description: Angular component development
Session ID: 12345
=====================================
```

**quality-gates.log:**

```text
2025-09-12 10:30:00: Quality gate check for security-engineer (type: threat-modeling) - Exit code: 0
```

## 🔧 Customization

### Adding New Hooks

1. Create new shell script in `.claude/hooks/`
2. Make it executable: `chmod +x .claude/hooks/your-hook.sh`
3. Add appropriate logging to `work/` directory
4. Update this README with documentation

### Hook Template

```bash
#!/bin/bash

# Your Custom Hook
# Description of what this hook does
# Triggers: When this hook should run

echo "🔧 Your Custom Hook - Starting..."

# Your hook logic here
# ...

# Log the activity
echo "$(date): Custom hook executed" >> work/custom-hook.log

echo "✅ Your Custom Hook completed"
```

### Environment Variables

Hooks can use these environment variables:

- `CLAUDE_PROJECT_ROOT` - Project root directory
- `CLAUDE_AGENT_TYPE` - Current agent type (if available)
- `CLAUDE_TASK_ID` - Unique task identifier (if available)

## 🛠️ Troubleshooting

### Common Issues

**Permission Denied:**
```bash
chmod +x .claude/hooks/*.sh
```

**Work Directory Missing:**
```bash
mkdir -p work
```

**Hook Not Triggering:**
- Check Claude Code settings configuration
- Verify hook script has executable permissions
- Review Claude Code logs for error messages

### Debug Mode

Run hooks with debug output:
```bash
bash -x ./.claude/hooks/hook-name.sh
```

## 📈 Best Practices

1. **Regular Monitoring:** Check `work/` logs regularly for coordination issues
2. **Hook Performance:** Keep hooks fast (< 5 seconds) to avoid workflow interruption
3. **Error Handling:** All hooks include proper exit codes for CI/CD integration
4. **Documentation:** Update this README when adding custom hooks
5. **Testing:** Test hooks manually before adding to automated workflows

## 🔄 Integration with Multi-Agent Workflow

### Phase-Based Hook Usage

**Phase 1 (Discovery):**

- Use `task-start-logger.sh` for business-analyst and product-manager coordination
- Run `quality-gate-checker.sh` for requirements validation
- Deploy `cross-agent-dependency-tracker.sh` to establish workflow dependencies
- Use `agent-conflict-resolution.sh` to detect early requirement conflicts

**Phase 2 (Architecture):**

- Deploy `quality-gate-checker.sh` for security-engineer validation
- Use `agent-handoff.sh` for business-analyst → software-architect transitions
- Run `compliance-automation.sh` for early security and accessibility planning
- Monitor with `agent-performance-monitor.sh` for architecture definition tasks

**Phase 3 (Development):**

- Heavy usage of `task-start-logger.sh` for parallel development coordination
- Continuous `quality-gate-checker.sh` for frontend and security validation
- Active `cross-agent-dependency-tracker.sh` validation for integration readiness
- Use `prompt-quality-validator.sh` for maintaining development standard quality
- Deploy `agent-conflict-resolution.sh` for resource contention management

**Phase 4 (Deployment):**

- Pre-deployment validation with all quality gates
- Comprehensive `compliance-automation.sh` validation (WCAG, GDPR, SOX)
- `agent-performance-monitor.sh` for deployment task optimization
- Post-deployment synchronization with `post-commit-sync.sh`

---

**Note:** These hooks are designed to work seamlessly with the 11-agent Claude Code framework while maintaining flexibility for custom workflows and project-specific requirements.
