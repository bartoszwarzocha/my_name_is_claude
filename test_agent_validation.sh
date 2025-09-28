#!/bin/bash

# Simple script to test agent validation without interactive interface

echo "🔍 Testing Agent Validation..."
echo ""

AGENTS_DIR=".claude/agents"
TOTAL_AGENTS=0
VALID_AGENTS=0
INVALID_AGENTS=0

echo "Testing individual agents:"
echo ""

while IFS= read -r -d '' agent_file; do
    ((TOTAL_AGENTS++))
    agent_name=$(basename "$agent_file" .md)

    # Check YAML header
    if grep -q "^---" "$agent_file" && grep -q "^name:" "$agent_file" && grep -q "^description:" "$agent_file"; then
        yaml_status="✅"
        ((VALID_AGENTS++))
    else
        yaml_status="❌"
        ((INVALID_AGENTS++))
    fi

    # Check TodoWrite Integration
    if grep -q "TodoWrite Integration" "$agent_file"; then
        todo_status="✅"
    else
        todo_status="⚠️"
    fi

    echo "[$yaml_status/$todo_status] $agent_name"

done < <(find "$AGENTS_DIR" -name "*.md" -type f -print0)

echo ""
echo "📊 Results Summary:"
echo "   Total agents: $TOTAL_AGENTS"
echo "   Valid YAML headers: $VALID_AGENTS"
echo "   Invalid YAML headers: $INVALID_AGENTS"
echo ""

if [ $INVALID_AGENTS -eq 0 ]; then
    echo "🎉 All agents have valid YAML headers!"
else
    echo "⚠️ $INVALID_AGENTS agents missing YAML headers"
fi