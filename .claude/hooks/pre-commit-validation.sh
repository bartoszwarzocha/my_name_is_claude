#!/bin/bash

# Agent Validation Hook (pre-commit style)
# Validates agent prompt structure and completeness before changes are finalized
# Ensures all agent prompts follow the required structure

echo "🔍 Agent Validation Hook - Checking prompt structure..."

EXIT_CODE=0

# Check all agent prompts for required sections
find .claude/prompts/agents -name "*.md" 2>/dev/null | while read file; do
    echo "  Validating: $(basename "$file")"
    
    # Check for required sections
    REQUIRED_SECTIONS=("## Mission" "## Process" "## Deliverables")
    
    for section in "${REQUIRED_SECTIONS[@]}"; do
        if ! grep -q "$section" "$file" 2>/dev/null; then
            echo "❌ Missing section '$section' in $file"
            EXIT_CODE=1
        fi
    done
    
    # Check file is not empty
    if [[ ! -s "$file" ]]; then
        echo "❌ Empty prompt file detected: $file"
        EXIT_CODE=1
    fi
    
done

# Check agent directory structure
EXPECTED_AGENTS=(
    "api" "architecture" "business" "data" "deployment" 
    "design" "frontend" "product" "quality" "review" "security"
)

echo "🏗️ Validating agent directory structure..."
for agent in "${EXPECTED_AGENTS[@]}"; do
    if [[ ! -d ".claude/prompts/agents/$agent" ]]; then
        echo "⚠️ Missing agent directory: $agent"
    fi
done

if [[ $EXIT_CODE -eq 0 ]]; then
    echo "✅ All agent prompts validation passed"
else
    echo "❌ Agent validation failed - please fix the issues above"
fi

echo "🔍 Agent Validation Hook completed"
exit $EXIT_CODE