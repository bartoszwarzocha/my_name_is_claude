#!/bin/bash

# Cross-Agent Dependency Tracker Hook
# Tracks dependencies between agents and validates workflow dependencies
# Ensures security-engineer requirements → frontend-engineer implementation coordination

ACTION="${1:-track}"  # track, validate, report
AGENT_TYPE="${2:-}"
DEPENDENCY_DATA="${3:-}"

echo "🔗 Cross-Agent Dependency Tracker Hook - Action: $ACTION..."

# Ensure work directory exists
mkdir -p work/dependencies

# Define agent dependencies matrix
declare -A DEPENDENCIES
# Format: "dependent_agent:required_agent:description"
DEPENDENCIES=(
    ["frontend-engineer:security-engineer"]="Security requirements and compliance standards"
    ["frontend-engineer:ux-designer"]="User interface designs and user experience specifications"
    ["frontend-engineer:api-engineer"]="API contracts and integration specifications"
    ["api-engineer:software-architect"]="System architecture and service design patterns"
    ["api-engineer:security-engineer"]="API security standards and authentication requirements"
    ["data-engineer:software-architect"]="Data architecture and system integration patterns"
    ["qa-engineer:frontend-engineer"]="Frontend components and testing requirements"
    ["qa-engineer:api-engineer"]="API endpoints and integration testing requirements"
    ["qa-engineer:security-engineer"]="Security testing requirements and compliance validation"
    ["deployment-engineer:frontend-engineer"]="Frontend build artifacts and deployment requirements"
    ["deployment-engineer:api-engineer"]="Backend services and deployment configurations"
    ["deployment-engineer:security-engineer"]="Security controls and infrastructure hardening"
    ["reviewer:security-engineer"]="Security review criteria and vulnerability assessment"
    ["reviewer:qa-engineer"]="Quality metrics and testing coverage requirements"
    ["software-architect:business-analyst"]="Business requirements and technical constraints"
    ["ux-designer:business-analyst"]="User requirements and business process understanding"
    ["security-engineer:business-analyst"]="Business security requirements and compliance needs"
)

track_dependency() {
    local dependent="$1"
    local required="$2"
    local description="$3"
    
    echo "📋 Tracking dependency: $dependent depends on $required"
    
    DEPENDENCY_ID="$(date +%Y%m%d_%H%M%S)_${dependent}_requires_${required}"
    DEPENDENCY_FILE="work/dependencies/${DEPENDENCY_ID}.json"
    
    cat > "$DEPENDENCY_FILE" << EOF
{
  "dependency_id": "$DEPENDENCY_ID",
  "timestamp": "$(date -Iseconds)",
  "dependent_agent": "$dependent",
  "required_agent": "$required",
  "description": "$description",
  "status": "tracked",
  "blocking_issues": [],
  "resolution_notes": "",
  "last_updated": "$(date -Iseconds)"
}
EOF
    
    echo "📄 Dependency tracked: $DEPENDENCY_FILE"
}

validate_dependencies() {
    local target_agent="${1:-all}"
    echo "🔍 Validating dependencies for: $target_agent"
    
    local validation_issues=0
    
    # Check if target agent has all required dependencies met
    for dep_key in "${!DEPENDENCIES[@]}"; do
        IFS=':' read -r dependent required <<< "$dep_key"
        
        if [[ "$target_agent" == "all" || "$target_agent" == "$dependent" ]]; then
            echo "  Checking: $dependent requires $required"
            
            # Check if required agent has delivered outputs
            REQUIRED_OUTPUT_EXISTS=false
            
            # Look for handoff records or deliverables
            if [[ -d "work/handoffs" ]]; then
                if find work/handoffs -name "*${required}*" | grep -q .; then
                    REQUIRED_OUTPUT_EXISTS=true
                    echo "    ✅ $required has handoff records"
                fi
            fi
            
            # Look for agent-specific deliverables
            case "$required" in
                "security-engineer")
                    if [[ -f "work/security-requirements.md" || -f "work/threat-model.md" ]]; then
                        REQUIRED_OUTPUT_EXISTS=true
                    fi
                    ;;
                "ux-designer")
                    if [[ -f "work/ui-designs.md" || -f "work/user-personas.md" ]]; then
                        REQUIRED_OUTPUT_EXISTS=true
                    fi
                    ;;
                "api-engineer")
                    if [[ -f "work/api-specs.yml" || -f "work/api-documentation.md" ]]; then
                        REQUIRED_OUTPUT_EXISTS=true
                    fi
                    ;;
                "software-architect")
                    if [[ -f "work/system-architecture.md" || -f "work/tech-specs.md" ]]; then
                        REQUIRED_OUTPUT_EXISTS=true
                    fi
                    ;;
            esac
            
            if [[ "$REQUIRED_OUTPUT_EXISTS" == false ]]; then
                echo "    ⚠️  Dependency not satisfied: $dependent waiting for $required"
                validation_issues=$((validation_issues + 1))
                
                # Create blocking issue record
                BLOCKING_FILE="work/dependencies/blocking_${dependent}_waiting_for_${required}.json"
                cat > "$BLOCKING_FILE" << EOF
{
  "blocking_issue_id": "blocking_${dependent}_waiting_for_${required}",
  "timestamp": "$(date -Iseconds)",
  "dependent_agent": "$dependent",
  "required_agent": "$required",
  "description": "${DEPENDENCIES[$dep_key]}",
  "status": "blocked",
  "impact": "medium",
  "escalation_needed": false,
  "created": "$(date -Iseconds)"
}
EOF
            else
                echo "    ✅ Dependency satisfied"
            fi
        fi
    done
    
    echo "📊 Validation completed: $validation_issues blocking issues found"
    return $validation_issues
}

generate_dependency_report() {
    echo "📋 Generating dependency report..."
    
    REPORT_FILE="work/dependencies/dependency_report_$(date +%Y%m%d_%H%M%S).md"
    
    cat > "$REPORT_FILE" << EOF
# Cross-Agent Dependency Report

**Generated:** $(date)

## Dependency Matrix

| Dependent Agent | Required Agent | Description | Status |
|----------------|----------------|-------------|---------|
EOF

    # Add dependency matrix to report
    for dep_key in "${!DEPENDENCIES[@]}"; do
        IFS=':' read -r dependent required <<< "$dep_key"
        description="${DEPENDENCIES[$dep_key]}"
        
        # Check status
        status="⚠️ Unknown"
        if [[ -d "work/handoffs" ]] && find work/handoffs -name "*${required}*" | grep -q .; then
            status="✅ Satisfied"
        elif [[ -f "work/dependencies/blocking_${dependent}_waiting_for_${required}.json" ]]; then
            status="🔴 Blocked"
        fi
        
        echo "| $dependent | $required | $description | $status |" >> "$REPORT_FILE"
    done
    
    cat >> "$REPORT_FILE" << EOF

## Blocking Issues

$(if [[ -n "$(find work/dependencies -name "blocking_*.json" 2>/dev/null)" ]]; then
    echo "### Current Blocking Issues"
    for blocking_file in work/dependencies/blocking_*.json; do
        if [[ -f "$blocking_file" ]]; then
            echo ""
            echo "**$(basename "$blocking_file" .json)**"
            echo "- Created: $(jq -r '.created' "$blocking_file" 2>/dev/null || echo "Unknown")"
            echo "- Issue: $(jq -r '.dependent_agent + " waiting for " + .required_agent' "$blocking_file" 2>/dev/null || echo "Parse error")"
            echo ""
        fi
    done
else
    echo "No blocking issues currently identified."
fi)

## Recommendations

### Immediate Actions
$(find work/dependencies -name "blocking_*.json" 2>/dev/null | head -3 | while read blocking_file; do
    if [[ -f "$blocking_file" ]]; then
        echo "- Prioritize $(jq -r '.required_agent' "$blocking_file" 2>/dev/null) deliverables for $(jq -r '.dependent_agent' "$blocking_file" 2>/dev/null)"
    fi
done)

### Workflow Optimization
- Consider parallel work where dependencies allow
- Establish regular dependency check meetings
- Create standardized handoff procedures
- Implement dependency status dashboards

## Dependency Health Score

$(
total_deps=${#DEPENDENCIES[@]}
satisfied_deps=$(find work/handoffs -name "*.md" 2>/dev/null | wc -l)
blocking_deps=$(find work/dependencies -name "blocking_*.json" 2>/dev/null | wc -l)

if [[ $total_deps -gt 0 ]]; then
    health_score=$(( (satisfied_deps * 100) / total_deps ))
    echo "**Overall Health:** $health_score% ($satisfied_deps/$total_deps dependencies satisfied)"
    
    if [[ $health_score -ge 80 ]]; then
        echo "**Status:** 🟢 Healthy workflow"
    elif [[ $health_score -ge 60 ]]; then
        echo "**Status:** 🟡 Monitor closely"
    else
        echo "**Status:** 🔴 Intervention needed"
    fi
else
    echo "**Status:** 📊 No dependencies tracked yet"
fi
)

EOF

    echo "📄 Dependency report generated: $REPORT_FILE"
}

# Main execution logic
case "$ACTION" in
    "track")
        if [[ -n "$AGENT_TYPE" && -n "$DEPENDENCY_DATA" ]]; then
            # Manual dependency tracking
            IFS=':' read -r dependent required description <<< "$DEPENDENCY_DATA"
            track_dependency "$dependent" "$required" "$description"
        else
            # Track all predefined dependencies
            echo "📋 Tracking all predefined dependencies..."
            for dep_key in "${!DEPENDENCIES[@]}"; do
                IFS=':' read -r dependent required <<< "$dep_key"
                description="${DEPENDENCIES[$dep_key]}"
                track_dependency "$dependent" "$required" "$description"
            done
        fi
        ;;
        
    "validate")
        validate_dependencies "$AGENT_TYPE"
        VALIDATION_EXIT=$?
        ;;
        
    "report")
        generate_dependency_report
        ;;
        
    *)
        echo "❌ Unknown action: $ACTION"
        echo "Available actions: track, validate, report"
        exit 1
        ;;
esac

# Log activity
echo "$(date): Cross-agent dependency $ACTION completed" >> work/dependency-activity.log

echo "✅ Cross-Agent Dependency Tracker Hook completed"
exit ${VALIDATION_EXIT:-0}