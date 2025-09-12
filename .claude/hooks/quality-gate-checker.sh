#!/bin/bash

# Quality Gate Hook (specialized validation)
# Ensures security and frontend standards are met during code review
# Runs agent-specific quality checks based on the type of work being done

AGENT_TYPE="${1:-unknown}"
WORK_TYPE="${2:-general}"

echo "🛡️ Quality Gate Hook - Running specialized checks..."

EXIT_CODE=0

case "$AGENT_TYPE" in
    "security-engineer")
        echo "🔐 Running security-specific quality checks..."
        
        # Check for security prompt completeness
        SECURITY_PROMPTS=(
            "security-architecture-and-threat-modeling"
            "penetration-testing-and-security-audit"
            "compliance-audit-and-governance"
            "incident-response-and-forensics"
            "security-controls-implementation"
            "identity-and-access-management"
            "secure-code-review-and-sast"
        )
        
        for prompt in "${SECURITY_PROMPTS[@]}"; do
            if [[ ! -f ".claude/prompts/agents/security/$prompt.md" ]]; then
                echo "❌ Missing critical security prompt: $prompt"
                EXIT_CODE=1
            fi
        done
        
        echo "🔍 Security checklist validation completed"
        ;;
        
    "frontend-engineer")
        echo "🎨 Running frontend-specific quality checks..."
        
        # Check for frontend prompt categories
        FRONTEND_CATEGORIES=(
            "angular-component-development"
            "wxwidgets-desktop-development"
            "responsive-design-and-css-architecture"
            "modern-javascript-and-typescript-development"
            "progressive-web-app-development"
            "web-accessibility-and-inclusive-design"
            "state-management-and-data-flow"
            "build-tools-and-bundler-optimization"
            "frontend-testing-and-quality-assurance"
        )
        
        for prompt in "${FRONTEND_CATEGORIES[@]}"; do
            if [[ ! -f ".claude/prompts/agents/frontend/$prompt.md" ]]; then
                echo "⚠️ Frontend prompt missing: $prompt"
            fi
        done
        
        echo "🎯 Frontend standards validation completed"
        ;;
        
    "reviewer")
        echo "👀 Running review-specific quality checks..."
        
        # Check for review completeness
        if [[ ! -f ".claude/prompts/agents/review/sonarqube-code-quality-analysis.md" ]]; then
            echo "⚠️ Missing code quality analysis prompt"
        fi
        
        if [[ ! -f ".claude/prompts/agents/review/security-vulnerability-assessment.md" ]]; then
            echo "⚠️ Missing security vulnerability assessment prompt"
        fi
        
        echo "📋 Review standards validation completed"
        ;;
        
    *)
        echo "ℹ️ General quality checks for agent: $AGENT_TYPE"
        
        # Check basic prompt structure for any agent
        AGENT_DIR=".claude/prompts/agents/$AGENT_TYPE"
        if [[ -d "$AGENT_DIR" ]]; then
            PROMPT_COUNT=$(find "$AGENT_DIR" -name "*.md" | wc -l)
            echo "📊 Agent $AGENT_TYPE has $PROMPT_COUNT prompts"
        fi
        ;;
esac

# Log quality gate execution
echo "$(date): Quality gate check for $AGENT_TYPE (type: $WORK_TYPE) - Exit code: $EXIT_CODE" >> work/quality-gates.log

if [[ $EXIT_CODE -eq 0 ]]; then
    echo "✅ Quality gate passed for $AGENT_TYPE"
else
    echo "❌ Quality gate failed for $AGENT_TYPE"
fi

echo "🛡️ Quality Gate Hook completed"
exit $EXIT_CODE