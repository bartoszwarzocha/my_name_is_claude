#!/bin/bash

# Multi-Agent Coordination Hook (task-start)
# Logs agent interactions and task initiation for workflow tracking
# Helps maintain coordination between multiple agents

AGENT_TYPE="${1:-unknown}"
TASK_DESCRIPTION="${2:-No description provided}"

echo "🤖 Multi-Agent Coordination Hook - Logging task start..."

# Ensure work directory exists
mkdir -p work

# Create agent activity log entry
cat >> work/agent-activity.log << EOF
=====================================
TASK START: $(date)
Agent: $AGENT_TYPE
Description: $TASK_DESCRIPTION
Session ID: $$
=====================================

EOF

# Track active agents
if [[ ! -f "work/active-agents.json" ]]; then
    echo '{}' > work/active-agents.json
fi

# Log task initiation
echo "📋 Task initiated by agent: $AGENT_TYPE"
echo "📝 Task description: $TASK_DESCRIPTION"

# Check for potential conflicts with other active agents
if [[ -f "work/active-agents.json" ]]; then
    echo "🔄 Checking for agent coordination needs..."
    
    # Simple conflict detection based on agent types
    case "$AGENT_TYPE" in
        "frontend-engineer"|"security-engineer"|"qa-engineer")
            echo "⚠️ Development phase agent active - consider coordination with related agents"
            ;;
        "business-analyst"|"product-manager"|"reviewer")
            echo "📋 Discovery phase agent active - ensure requirements alignment"
            ;;
        "software-architect"|"deployment-engineer")
            echo "🏗️ Architecture phase agent active - validate with business requirements"
            ;;
    esac
fi

# Update agent status tracking
echo "$(date): $AGENT_TYPE started task: $TASK_DESCRIPTION" >> work/task-timeline.log

echo "✅ Multi-Agent Coordination Hook completed"