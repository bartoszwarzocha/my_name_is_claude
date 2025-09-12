#!/bin/bash

# Documentation Update Hook (user-prompt-submit-hook)
# Automatically updates documentation when prompts or markdown files are modified
# Triggers: When user submits a prompt that might affect documentation

echo "📝 Documentation Update Hook - Checking for documentation changes..."

# Check if any markdown files or PlantUML files have been modified
if git diff --name-only HEAD~1 2>/dev/null | grep -E "\.(md|puml)$" > /dev/null; then
    echo "📄 Documentation changes detected in recent commits"
    
    # Count current prompts
    TOTAL_PROMPTS=$(find .claude/prompts/agents -name "*.md" 2>/dev/null | wc -l)
    echo "📊 Current prompt count: $TOTAL_PROMPTS"
    
    # Log the change
    echo "$(date): Documentation update detected - $TOTAL_PROMPTS total prompts" >> work/documentation-updates.log
    
    echo "✅ Documentation tracking updated"
else
    echo "ℹ️ No documentation changes detected"
fi

# Check if work directory documentation needs update
if [[ -f "work/project-knowledge-base.md" ]]; then
    echo "🔄 Work directory documentation exists - ready for updates"
fi

echo "📝 Documentation Update Hook completed"