# Hooks & Automation - My Name Is Claude

**Status:** Production Ready ✅

Automated hooks for the Claude Code Multi-Agent Framework optimized for TodoWrite workflow coordination and simplified agent management.

## 📁 Available Hooks

### Basic Framework Hooks

#### 1. **user-prompt-submit-hook.sh**

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
    "user-prompt-submit-hook": {
      "command": ".claude/hooks/user-prompt-submit-hook.sh"
    }
  }
}
```

#### 2. **agent-handoff.sh**

- **Purpose:** Coordinates seamless transitions between agents during multi-agent workflows
- **Triggers:** When one agent completes work and needs to hand off to another agent
- **What it does:**
  - Generates TodoWrite tasks for the next agent in the workflow
  - Preserves context and relevant information for handoff
  - Logs agent transitions for workflow tracking
  - Ensures no work is lost during agent transitions

**Usage in Claude Code settings:**
```json
{
  "hooks": {
    "agent-handoff": {
      "command": ".claude/hooks/agent-handoff.sh",
      "triggers": ["agent-completion", "workflow-transition"]
    }
  }
}
```

#### 3. **cross-agent-dependency-tracker.sh**

- **Purpose:** Tracks dependencies between different agents and their tasks
- **Triggers:** When TodoWrite tasks are created or updated across multiple agents
- **What it does:**
  - Identifies task dependencies between different agents
  - Prevents conflicts in parallel agent work
  - Creates dependency graphs for complex workflows
  - Alerts when blocking dependencies are detected

**Usage in Claude Code settings:**
```json
{
  "hooks": {
    "cross-agent-dependency-tracker": {
      "command": ".claude/hooks/cross-agent-dependency-tracker.sh",
      "triggers": ["task-creation", "task-update"]
    }
  }
}
```

#### 4. **agent-conflict-resolution.sh**

- **Purpose:** Detects and resolves conflicts when multiple agents work on related tasks
- **Triggers:** When potential conflicts are detected in agent workflows
- **What it does:**
  - Analyzes task overlaps between different agents
  - Suggests conflict resolution strategies
  - Implements simple conflict resolution automatically
  - Escalates complex conflicts for manual resolution

**Usage in Claude Code settings:**
```json
{
  "hooks": {
    "agent-conflict-resolution": {
      "command": ".claude/hooks/agent-conflict-resolution.sh",
      "triggers": ["conflict-detection", "parallel-agent-work"]
    }
  }
}
```

## 🔧 Hook Configuration

### Setting Up Hooks in Claude Code

1. **Enable Hooks in Settings:**
   ```json
   {
     "hooks": {
       "user-prompt-submit-hook": {
         "command": ".claude/hooks/user-prompt-submit-hook.sh",
         "enabled": true,
         "async": false
       }
     }
   }
   ```

2. **Configure Hook Permissions:**
   ```bash
   chmod +x .claude/hooks/*.sh
   ```

3. **Test Hook Functionality:**
   ```bash
   # Test a hook manually
   ./.claude/hooks/user-prompt-submit-hook.sh
   ```

### Hook Environment Variables

Hooks have access to these environment variables:

- `CLAUDE_PROJECT_ROOT` - Root directory of the current project
- `CLAUDE_AGENT_ACTIVE` - Currently active agent (if any)
- `CLAUDE_SESSION_ID` - Current session identifier
- `CLAUDE_WORK_DIR` - Working directory for temporary files (`/work/`)

### Global Hook Configuration

Create `.claude/hooks/config.sh` for shared configuration:

```bash
#!/bin/bash
# Global hook configuration

# Logging settings
HOOK_LOG_LEVEL="INFO"
HOOK_LOG_FILE="work/hooks.log"

# TodoWrite integration
TODOWRITE_ENABLED=true
TODOWRITE_AUTO_CREATE=true

# Agent coordination
AGENT_HANDOFF_ENABLED=true
CONFLICT_RESOLUTION_AUTO=true

# Export all settings
export HOOK_LOG_LEVEL HOOK_LOG_FILE TODOWRITE_ENABLED TODOWRITE_AUTO_CREATE
export AGENT_HANDOFF_ENABLED CONFLICT_RESOLUTION_AUTO
```

## 🔄 Hook Workflows

### TodoWrite Integration Workflow

1. **Task Creation Hook**
   ```bash
   # Automatically triggered when TODO items are created
   .claude/hooks/cross-agent-dependency-tracker.sh
   ```

2. **Agent Handoff Hook**
   ```bash
   # Triggered when agent completes major milestone
   .claude/hooks/agent-handoff.sh "frontend-engineer" "backend-engineer"
   ```

3. **Conflict Detection Hook**
   ```bash
   # Triggered when potential conflicts detected
   .claude/hooks/agent-conflict-resolution.sh
   ```

### Session Management Integration

Hooks integrate with [Session Management](../../core-features/session-management.md):

- **Session Start:** Initialize hook logging and state tracking
- **Session Continue:** Restore hook state and continue monitoring
- **Session End:** Generate hook activity summary

### Multi-Agent Coordination

Hooks enable seamless multi-agent workflows:

```bash
# Example: Frontend → Backend → Deployment workflow
1. Frontend-engineer completes component development
   → agent-handoff.sh triggers
   → Creates TODO for backend-engineer

2. Backend-engineer starts API development
   → cross-agent-dependency-tracker.sh monitors
   → Identifies API-component dependencies

3. Both agents work in parallel
   → agent-conflict-resolution.sh prevents conflicts
   → Coordinates shared resource access
```

## 📋 Custom Hook Development

### Hook Template

Create new hooks using this template:

```bash
#!/bin/bash
# .claude/hooks/my-custom-hook.sh

# Source global configuration
source "$(dirname "$0")/config.sh" 2>/dev/null || true

# Hook metadata
HOOK_NAME="my-custom-hook"
HOOK_VERSION="1.0.0"

# Main hook logic
main() {
    local trigger_event="$1"
    local context="$2"

    # Log hook execution
    echo "[$(date)] $HOOK_NAME triggered: $trigger_event" >> "$HOOK_LOG_FILE"

    # Your custom logic here
    case "$trigger_event" in
        "my-event")
            handle_my_event "$context"
            ;;
        *)
            echo "Unknown trigger: $trigger_event"
            exit 1
            ;;
    esac
}

handle_my_event() {
    local context="$1"
    # Implement your custom logic
    echo "Handling my event with context: $context"
}

# Execute main function with all arguments
main "$@"
```

### Hook Best Practices

1. **Error Handling**
   ```bash
   # Always include error handling
   set -euo pipefail

   # Use proper exit codes
   exit 0  # Success
   exit 1  # Error
   ```

2. **Logging**
   ```bash
   # Log all significant actions
   echo "[$(date)] Hook action performed" >> "$HOOK_LOG_FILE"
   ```

3. **Performance**
   ```bash
   # Keep hooks fast and efficient
   # Use background processing for long operations
   long_operation &
   ```

4. **Integration**
   ```bash
   # Integrate with TodoWrite when appropriate
   if [[ "$TODOWRITE_ENABLED" == "true" ]]; then
       create_todo_item "Hook-generated task"
   fi
   ```

## 🎯 Integration Examples

### Example 1: Custom Project Setup Hook

```bash
#!/bin/bash
# .claude/hooks/project-setup-complete.sh

# Triggered when project setup is complete
main() {
    local project_type="$1"

    case "$project_type" in
        "react")
            setup_react_specific_automation
            ;;
        "nodejs")
            setup_nodejs_specific_automation
            ;;
        *)
            setup_generic_automation
            ;;
    esac
}

setup_react_specific_automation() {
    # Create TODO for React-specific setup tasks
    echo "TODO: Configure ESLint for React project" >> work/react-setup-todos.md
    echo "TODO: Setup React testing environment" >> work/react-setup-todos.md
}
```

### Example 2: Code Quality Hook

```bash
#!/bin/bash
# .claude/hooks/code-quality-check.sh

# Triggered when code is modified
main() {
    local file_changed="$1"

    # Run quality checks based on file type
    case "$file_changed" in
        *.js|*.ts|*.jsx|*.tsx)
            run_javascript_quality_checks "$file_changed"
            ;;
        *.py)
            run_python_quality_checks "$file_changed"
            ;;
    esac
}
```

## 🔍 Troubleshooting

### Common Issues

1. **Hook Not Executing**
   ```bash
   # Check permissions
   ls -la .claude/hooks/
   # Should show -rwxr-xr-x permissions

   # Fix permissions if needed
   chmod +x .claude/hooks/*.sh
   ```

2. **Environment Variables Not Available**
   ```bash
   # Check if config.sh is sourced
   source .claude/hooks/config.sh
   echo $HOOK_LOG_LEVEL
   ```

3. **Hook Execution Errors**
   ```bash
   # Check hook logs
   tail -f work/hooks.log

   # Test hook manually
   ./.claude/hooks/user-prompt-submit-hook.sh
   ```

### Debug Mode

Enable debug mode for verbose hook logging:

```bash
# Set debug mode
export HOOK_DEBUG=true

# Run hook with debug output
./.claude/hooks/agent-handoff.sh
```

---

**See also:**
- [Session Management](../../core-features/session-management.md) - State and context management
- [TODO Management](../../core-features/todo-management.md) - Task coordination system
- [Agent System](../../core-features/agent-system.md) - Multi-agent coordination