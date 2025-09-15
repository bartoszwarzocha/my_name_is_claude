# Claude Code Hooks - Simplified TodoWrite Integration

Automated hooks for the Claude Code Multi-Agent Framework optimized for TodoWrite workflow coordination and simplified agent management.

## 📁 Available Hooks

## Basic Framework Hooks

### 1. **user-prompt-submit-hook.sh**

- **Purpose:** Tracks documentation changes and updates prompt statistics
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
  - Checks all agent prompts for required sections
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

- **Purpose:** Logs multi-agent task coordination for TodoWrite integration
- **Triggers:** When starting agent-specific tasks
- **What it does:**
  - Logs task initiation to `work/agent-activity.log`
  - Tracks active agents for coordination
  - Provides simple conflict detection
  - Integrates with TodoWrite workflow

**Usage:**
```bash
./.claude/hooks/task-start-logger.sh "frontend-engineer" "Angular component development"
```

### 5. **quality-gate-checker.sh**

- **Purpose:** Runs basic quality checks based on agent type
- **Triggers:** During code review or quality validation phases
- **What it does:**
  - Security validation for security-engineer
  - Frontend standards checking for frontend-engineer
  - Review completeness validation for reviewer
  - Logs results to `work/quality-gates.log`

**Usage:**
```bash
./.claude/hooks/quality-gate-checker.sh "security-engineer" "threat-modeling"
```

## Simplified Multi-Agent Hooks

### 6. **agent-handoff.sh** ✨ Simplified

- **Purpose:** Simple TodoWrite patterns for agent transitions
- **Triggers:** When transitioning work from one agent to another
- **What it does:**
  - Validates agent transition
  - Generates TodoWrite task patterns
  - Provides simple handoff coordination
  - Minimal logging and overhead

**Usage:**
```bash
./.claude/hooks/agent-handoff.sh "business-analyst" "software-architect"
```

**Output Example:**
```
🔄 Agent Handoff: business-analyst → software-architect
✅ Agent transition validated

📝 TodoWrite patterns for software-architect:

TodoWrite({
  content: "Process handoff from business-analyst",
  status: "in_progress",
  activeForm: "Processing business-analyst handoff"
});

✅ Use TodoWrite to track handoff progress
```

### 7. **cross-agent-dependency-tracker.sh** ✨ Simplified

- **Purpose:** Basic dependency checking for TodoWrite coordination
- **Triggers:** When checking agent dependencies
- **What it does:**
  - Shows simple dependency relationships
  - Provides guidance for TodoWrite coordination
  - Minimal complexity and overhead
  - Focus on TodoWrite integration

**Usage:**
```bash
# Check dependencies for specific agent
./.claude/hooks/cross-agent-dependency-tracker.sh "check" "frontend-engineer"
```

**Output Example:**
```
🔗 Dependency Check: check for frontend-engineer
Depends on: ux-designer, api-engineer, security-engineer
📋 Basic dependency status for frontend-engineer
Use TodoWrite to coordinate agent dependencies
✅ Dependency check completed
```

### 8. **agent-conflict-resolution.sh** ✨ Simplified

- **Purpose:** Basic conflict detection for TodoWrite workflow
- **Triggers:** When checking for workflow conflicts
- **What it does:**
  - Detects basic workflow conflicts
  - Checks for multiple active agents
  - Monitors file activity conflicts
  - Provides simple resolution guidance

**Usage:**
```bash
# Detect conflicts
./.claude/hooks/agent-conflict-resolution.sh "detect"

# Get resolution guidance
./.claude/hooks/agent-conflict-resolution.sh "resolve"
```

**Output Example:**
```
⚖️ Conflict Resolution: detect (basic)
🔍 Checking for basic workflow conflicts...
⚠️ Multiple agents active - coordination needed
Found 1 potential conflicts
✅ Conflict resolution completed
```

### 9. **prompt-quality-validator.sh**

- **Purpose:** Validates quality and completeness of agent prompts
- **Triggers:** When creating or modifying agent prompts
- **What it does:**
  - Checks markdown structure and required sections
  - Validates content completeness
  - Generates quality reports with scoring
  - Ensures prompts follow framework standards

**Usage:**
```bash
# Validate specific prompt
./.claude/hooks/prompt-quality-validator.sh ".claude/prompts/agents/security/threat-modeling.md"

# Validate all prompts
./.claude/hooks/prompt-quality-validator.sh "" "comprehensive"
```

### 10. **agent-performance-monitor.sh**

- **Purpose:** Monitors agent performance and execution metrics
- **Triggers:** At start and end of agent tasks
- **What it does:**
  - Tracks task execution time and resource usage
  - Calculates performance scores
  - Generates performance reports
  - Identifies optimization opportunities

**Usage:**
```bash
# Start monitoring
TASK_ID=$(./.claude/hooks/agent-performance-monitor.sh "start" "frontend-engineer")

# Stop monitoring
./.claude/hooks/agent-performance-monitor.sh "stop" "frontend-engineer" "$TASK_ID"

# Generate report
./.claude/hooks/agent-performance-monitor.sh "report"
```

### 11. **compliance-automation.sh**

- **Purpose:** Automated compliance checking for WCAG, GDPR, SOX standards
- **Triggers:** During quality validation and before deployment
- **What it does:**
  - Validates WCAG 2.1 accessibility compliance
  - Checks GDPR data protection compliance
  - Verifies SOX internal controls
  - Generates compliance reports

**Usage:**
```bash
# Check WCAG compliance
./.claude/hooks/compliance-automation.sh "wcag" "frontend-engineer"

# Check GDPR compliance
./.claude/hooks/compliance-automation.sh "gdpr" "security-engineer"

# Run comprehensive check
./.claude/hooks/compliance-automation.sh "all" "frontend-engineer"
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

# Test simplified multi-agent hooks
./.claude/hooks/agent-handoff.sh "test-from" "test-to"
./.claude/hooks/cross-agent-dependency-tracker.sh "check" "frontend-engineer"
./.claude/hooks/agent-conflict-resolution.sh "detect"

# Test advanced hooks
./.claude/hooks/prompt-quality-validator.sh "" "comprehensive"
./.claude/hooks/agent-performance-monitor.sh "analyze"
./.claude/hooks/compliance-automation.sh "all"
```

## 📊 Hook Outputs and Logs

### Work Directory Files Created

#### Basic Framework Logs

- `work/documentation-updates.log` - Documentation change tracking
- `work/agent-activity.log` - Multi-agent task coordination log
- `work/current-stats.md` - Current framework statistics
- `work/sync-activity.log` - Prompt synchronization history
- `work/quality-gates.log` - Quality validation results

#### Advanced Multi-Agent Logs

- `work/quality-reports/` - Prompt quality validation reports
- `work/performance/` - Agent performance metrics and reports
- `work/compliance/` - Compliance audit reports (WCAG, GDPR, SOX)

### Log File Formats

**agent-activity.log:**
```text
=====================================
TASK START: 2025-09-15 09:30:00
Agent: frontend-engineer
Description: Angular component development
Session ID: 12345
=====================================
```

**quality-gates.log:**
```text
2025-09-15 09:30:00: Quality gate check for security-engineer (type: threat-modeling) - Exit code: 0
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
# Keep it simple and TodoWrite-compatible

# Log the activity (optional)
echo "$(date): Custom hook executed" >> work/custom-hook.log

echo "✅ Your Custom Hook completed"
```

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

1. **TodoWrite Integration:** Use hooks to generate TodoWrite patterns for coordination
2. **Keep Simple:** Simplified hooks focus on essential functionality
3. **Fast Execution:** Hooks complete in < 2 seconds for smooth workflow
4. **Minimal Logging:** Only essential logs to avoid clutter
5. **Testing:** Test hooks manually before automated workflows

## 🔄 Integration with TodoWrite Workflow

### Recommended Hook Usage for TodoWrite Coordination

**Starting New Work:**
1. Use `task-start-logger.sh` to log agent activation
2. Use `agent-handoff.sh` for TodoWrite patterns when receiving work
3. Use `cross-agent-dependency-tracker.sh` to check prerequisites

**During Development:**
1. Use `quality-gate-checker.sh` for validation checkpoints
2. Use `agent-conflict-resolution.sh` if coordination issues arise
3. Use `prompt-quality-validator.sh` for maintaining standards

**Completing Work:**
1. Use `post-commit-sync.sh` to update framework statistics
2. Use `compliance-automation.sh` for final validation
3. Use `agent-handoff.sh` when passing work to next agent

### TodoWrite Pattern Examples

All simplified hooks generate TodoWrite-compatible patterns:

```javascript
// Generated by agent-handoff.sh
TodoWrite({
  content: "Process handoff from business-analyst",
  status: "in_progress",
  activeForm: "Processing business-analyst handoff"
});

// Manual coordination based on dependency-tracker.sh
TodoWrite({
  content: "Coordinate with security-engineer for requirements",
  status: "pending",
  activeForm: "Waiting for security requirements"
});

// Conflict resolution guidance
TodoWrite({
  content: "Resolve workflow conflict detected by hooks",
  status: "pending",
  activeForm: "Resolving agent coordination conflict"
});
```

---

**Note:** These simplified hooks are optimized for TodoWrite workflow integration while maintaining essential multi-agent coordination capabilities. Complex orchestration features have been removed in favor of TodoWrite-driven coordination.