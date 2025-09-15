#!/bin/bash

# Simple Conflict Resolution Hook
# Basic conflict detection for TodoWrite workflow

ACTION="${1:-detect}"
CONFLICT_TYPE="${2:-basic}"

echo "⚖️ Conflict Resolution: $ACTION ($CONFLICT_TYPE)"

detect_conflicts() {
    echo "🔍 Checking for basic workflow conflicts..."

    conflicts=0

    # Check for multiple agents working simultaneously
    if [[ -f "work/agent-activity.log" ]]; then
        active_agents=$(grep "TASK START" work/agent-activity.log | tail -5 | awk '{print $4}' | sort | uniq | wc -l)
        if [[ $active_agents -gt 2 ]]; then
            echo "⚠️ Multiple agents active - coordination needed"
            conflicts=$((conflicts + 1))
        fi
    fi

    # Check for file conflicts
    if [[ -d "work" ]]; then
        recent_changes=$(find work -name "*.md" -newer work/agent-activity.log 2>/dev/null | wc -l)
        if [[ $recent_changes -gt 3 ]]; then
            echo "⚠️ High file activity - potential conflicts"
            conflicts=$((conflicts + 1))
        fi
    fi

    echo "Found $conflicts potential conflicts"
    return $conflicts
}

resolve_conflicts() {
    echo "🔧 Simple conflict resolution:"
    echo "- Use TodoWrite to coordinate agent work"
    echo "- Ensure proper agent handoffs"
    echo "- Review work directory for conflicts"
}

# Execute action
case "$ACTION" in
    "detect")
        detect_conflicts
        ;;
    "resolve")
        resolve_conflicts
        ;;
    *)
        echo "Use: $0 [detect|resolve]"
        ;;
esac

echo "✅ Conflict resolution completed"