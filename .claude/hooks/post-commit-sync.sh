#!/bin/bash

# Prompt Count Sync Hook (post-commit)
# Automatically syncs prompt counts and updates statistics after commits
# Maintains accurate documentation of current framework state

echo "📊 Prompt Count Sync Hook - Updating statistics..."

# Count prompts by agent
declare -A AGENT_COUNTS
TOTAL_PROMPTS=0

for agent_dir in .claude/prompts/agents/*/; do
    if [[ -d "$agent_dir" ]]; then
        agent_name=$(basename "$agent_dir")
        count=$(find "$agent_dir" -name "*.md" 2>/dev/null | wc -l)
        AGENT_COUNTS[$agent_name]=$count
        TOTAL_PROMPTS=$((TOTAL_PROMPTS + count))
    fi
done

echo "📈 Current Prompt Statistics:"
echo "  Total Prompts: $TOTAL_PROMPTS"

# Display counts by agent
for agent in "${!AGENT_COUNTS[@]}"; do
    printf "  %-20s %d prompts\n" "$agent:" "${AGENT_COUNTS[$agent]}"
done

# Update work directory statistics
if [[ -d "work" ]]; then
    cat > work/current-stats.md << EOF
# Current Framework Statistics

**Updated:** $(date)
**Total Prompts:** $TOTAL_PROMPTS

## Prompts by Agent

$(for agent in $(printf '%s\n' "${!AGENT_COUNTS[@]}" | sort); do
    printf "- **%s:** %d prompts\n" "$agent" "${AGENT_COUNTS[$agent]}"
done)

## Recent Activity

- Last sync: $(date)
- Repository state: Active development
- Framework version: Multi-agent v1.0
EOF

    echo "📁 Updated work/current-stats.md"
fi

# Log the sync activity
echo "$(date): Prompt sync completed - $TOTAL_PROMPTS total prompts" >> work/sync-activity.log

echo "✅ Prompt Count Sync Hook completed"