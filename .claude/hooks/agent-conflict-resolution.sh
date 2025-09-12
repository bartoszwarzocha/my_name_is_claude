#!/bin/bash

# Agent Conflict Resolution Hook
# Detects and resolves conflicts between agents
# Handles overlapping responsibilities and resource contention

ACTION="${1:-detect}"  # detect, resolve, report, escalate
CONFLICT_TYPE="${2:-all}"  # requirements, resources, responsibilities, timeline, all
AGENTS_INVOLVED="${3:-}"

echo "⚖️ Agent Conflict Resolution Hook - Action: $ACTION, Type: $CONFLICT_TYPE..."

# Ensure work directory exists
mkdir -p work/conflicts

EXIT_CODE=0

detect_requirement_conflicts() {
    echo "📋 Detecting requirement conflicts..."
    
    local conflicts_found=0
    
    # Check for conflicting business requirements
    if [[ -d "work/handoffs" ]]; then
        # Look for conflicting specifications between agents
        BUSINESS_REQS=$(find work/handoffs -name "*business-analyst*" -o -name "*product-manager*" 2>/dev/null)
        ARCH_REQS=$(find work/handoffs -name "*software-architect*" 2>/dev/null)
        SECURITY_REQS=$(find work/handoffs -name "*security-engineer*" 2>/dev/null)
        
        # Check for security vs performance conflicts
        if [[ -n "$SECURITY_REQS" && -n "$ARCH_REQS" ]]; then
            # Simple conflict detection based on keywords
            if grep -qi "performance\|speed\|fast" $ARCH_REQS 2>/dev/null && \
               grep -qi "encryption\|security.*slow\|performance.*impact" $SECURITY_REQS 2>/dev/null; then
                create_conflict_record "requirements" "security-engineer,software-architect" \
                    "Potential conflict: Security requirements may impact performance goals" \
                    "medium"
                conflicts_found=$((conflicts_found + 1))
            fi
        fi
        
        # Check for UX vs Business requirement conflicts
        UX_REQS=$(find work/handoffs -name "*ux-designer*" 2>/dev/null)
        if [[ -n "$BUSINESS_REQS" && -n "$UX_REQS" ]]; then
            if grep -qi "complex\|advanced.*feature" $BUSINESS_REQS 2>/dev/null && \
               grep -qi "simple\|minimal\|user.*friendly" $UX_REQS 2>/dev/null; then
                create_conflict_record "requirements" "business-analyst,ux-designer" \
                    "Potential conflict: Complex business requirements vs simple UX design" \
                    "high"
                conflicts_found=$((conflicts_found + 1))
            fi
        fi
    fi
    
    echo "  Found $conflicts_found requirement conflicts"
    return $conflicts_found
}

detect_resource_conflicts() {
    echo "🔧 Detecting resource conflicts..."
    
    local conflicts_found=0
    
    # Check for concurrent resource usage
    if [[ -f "work/agent-activity.log" ]]; then
        # Look for overlapping active sessions
        ACTIVE_SESSIONS=$(grep "TASK START" work/agent-activity.log | tail -10)
        
        # Check for concurrent frontend and API development
        if echo "$ACTIVE_SESSIONS" | grep -q "frontend-engineer" && \
           echo "$ACTIVE_SESSIONS" | grep -q "api-engineer"; then
            # Check if they're working on the same integration
            if grep -qi "integration\|api.*call\|endpoint" work/agent-activity.log 2>/dev/null; then
                create_conflict_record "resources" "frontend-engineer,api-engineer" \
                    "Potential resource conflict: Concurrent API integration work" \
                    "medium"
                conflicts_found=$((conflicts_found + 1))
            fi
        fi
        
        # Check for testing resource conflicts
        if echo "$ACTIVE_SESSIONS" | grep -q "qa-engineer" && \
           (echo "$ACTIVE_SESSIONS" | grep -q "frontend-engineer" || echo "$ACTIVE_SESSIONS" | grep -q "api-engineer"); then
            create_conflict_record "resources" "qa-engineer,frontend-engineer,api-engineer" \
                "Testing resources may be in contention during concurrent development" \
                "low"
            conflicts_found=$((conflicts_found + 1))
        fi
    fi
    
    # Check for file system conflicts
    if [[ -d "work" ]]; then
        # Look for concurrent file modifications
        RECENT_FILES=$(find work -name "*.md" -newer work/agent-activity.log 2>/dev/null | head -5)
        if [[ $(echo "$RECENT_FILES" | wc -l) -gt 3 ]]; then
            create_conflict_record "resources" "multiple" \
                "High concurrent file activity detected - potential merge conflicts" \
                "medium"
            conflicts_found=$((conflicts_found + 1))
        fi
    fi
    
    echo "  Found $conflicts_found resource conflicts"
    return $conflicts_found
}

detect_responsibility_overlaps() {
    echo "👥 Detecting responsibility overlaps..."
    
    local conflicts_found=0
    
    # Define agent responsibility boundaries
    declare -A PRIMARY_RESPONSIBILITIES
    PRIMARY_RESPONSIBILITIES["business-analyst"]="requirements,processes,stakeholders"
    PRIMARY_RESPONSIBILITIES["product-manager"]="features,roadmap,prioritization"
    PRIMARY_RESPONSIBILITIES["ux-designer"]="user_experience,interfaces,usability"
    PRIMARY_RESPONSIBILITIES["software-architect"]="architecture,patterns,technology_stack"
    PRIMARY_RESPONSIBILITIES["security-engineer"]="security,compliance,threats"
    PRIMARY_RESPONSIBILITIES["frontend-engineer"]="ui_implementation,client_code,user_interactions"
    PRIMARY_RESPONSIBILITIES["api-engineer"]="services,apis,integration"
    PRIMARY_RESPONSIBILITIES["data-engineer"]="data_models,etl,analytics"
    PRIMARY_RESPONSIBILITIES["qa-engineer"]="testing,quality,validation"
    PRIMARY_RESPONSIBILITIES["deployment-engineer"]="infrastructure,deployment,operations"
    PRIMARY_RESPONSIBILITIES["reviewer"]="quality_review,validation,approval"
    
    # Check for overlapping work based on handoff records
    if [[ -d "work/handoffs" ]]; then
        # Look for multiple agents working on similar deliverables
        for area in "security" "ui" "api" "testing" "architecture"; do
            AGENTS_IN_AREA=$(find work/handoffs -name "*.md" -exec grep -l "$area" {} \; 2>/dev/null | \
                           sed 's/.*_\([^_]*\)_to_.*/\1/' | sort | uniq -c | awk '$1 > 1 {print $2}')
            
            if [[ -n "$AGENTS_IN_AREA" ]]; then
                create_conflict_record "responsibilities" "$AGENTS_IN_AREA" \
                    "Multiple agents working in overlapping area: $area" \
                    "low"
                conflicts_found=$((conflicts_found + 1))
            fi
        done
    fi
    
    # Check for boundary violations in prompts
    for agent_dir in .claude/prompts/agents/*/; do
        if [[ -d "$agent_dir" ]]; then
            agent_name=$(basename "$agent_dir")
            other_responsibilities=""
            
            # Check if agent prompts mention other agents' primary responsibilities
            for other_agent in "${!PRIMARY_RESPONSIBILITIES[@]}"; do
                if [[ "$agent_name" != "$other_agent" ]]; then
                    other_resp="${PRIMARY_RESPONSIBILITIES[$other_agent]}"
                    IFS=',' read -ra RESP_ARRAY <<< "$other_resp"
                    for resp in "${RESP_ARRAY[@]}"; do
                        if grep -ri "$resp" "$agent_dir" >/dev/null 2>&1; then
                            other_responsibilities="$other_responsibilities,$other_agent($resp)"
                        fi
                    done
                fi
            done
            
            if [[ -n "$other_responsibilities" ]]; then
                create_conflict_record "responsibilities" "$agent_name,overlap" \
                    "Agent $agent_name may have overlapping responsibilities: $other_responsibilities" \
                    "low"
                conflicts_found=$((conflicts_found + 1))
            fi
        fi
    done
    
    echo "  Found $conflicts_found responsibility overlaps"
    return $conflicts_found
}

create_conflict_record() {
    local conflict_type="$1"
    local agents_involved="$2"
    local description="$3"
    local severity="$4"
    
    local conflict_id="conflict_$(date +%Y%m%d_%H%M%S)_${conflict_type}"
    local conflict_file="work/conflicts/${conflict_id}.json"
    
    cat > "$conflict_file" << EOF
{
  "conflict_id": "$conflict_id",
  "timestamp": "$(date -Iseconds)",
  "type": "$conflict_type",
  "severity": "$severity",
  "agents_involved": "$agents_involved",
  "description": "$description",
  "status": "detected",
  "resolution_strategy": null,
  "resolution_notes": "",
  "escalated": false,
  "resolved_timestamp": null
}
EOF
    
    echo "🚨 Conflict detected: $conflict_id ($severity severity)"
}

resolve_conflicts() {
    local target_type="$1"
    
    echo "🔧 Attempting to resolve conflicts of type: $target_type"
    
    local resolved_count=0
    
    # Find unresolved conflicts
    for conflict_file in work/conflicts/conflict_*.json; do
        if [[ -f "$conflict_file" ]]; then
            CONFLICT_TYPE=$(jq -r '.type' "$conflict_file" 2>/dev/null)
            CONFLICT_STATUS=$(jq -r '.status' "$conflict_file" 2>/dev/null)
            SEVERITY=$(jq -r '.severity' "$conflict_file" 2>/dev/null)
            
            if [[ "$CONFLICT_STATUS" == "detected" && ("$target_type" == "all" || "$target_type" == "$CONFLICT_TYPE") ]]; then
                echo "  Resolving conflict: $(basename "$conflict_file")"
                
                # Apply resolution strategy based on conflict type
                case "$CONFLICT_TYPE" in
                    "requirements")
                        resolve_requirement_conflict "$conflict_file"
                        ;;
                    "resources")
                        resolve_resource_conflict "$conflict_file"
                        ;;
                    "responsibilities")
                        resolve_responsibility_conflict "$conflict_file"
                        ;;
                esac
                
                resolved_count=$((resolved_count + 1))
            fi
        fi
    done
    
    echo "  Resolved $resolved_count conflicts"
    return $resolved_count
}

resolve_requirement_conflict() {
    local conflict_file="$1"
    
    AGENTS=$(jq -r '.agents_involved' "$conflict_file")
    DESCRIPTION=$(jq -r '.description' "$conflict_file")
    
    # Create resolution strategy
    RESOLUTION_STRATEGY=""
    if echo "$DESCRIPTION" | grep -qi "security.*performance"; then
        RESOLUTION_STRATEGY="Prioritize security requirements; implement performance optimizations in later iterations"
    elif echo "$DESCRIPTION" | grep -qi "complex.*simple"; then
        RESOLUTION_STRATEGY="Create progressive disclosure UI; implement complex features with simple initial interface"
    else
        RESOLUTION_STRATEGY="Schedule conflict resolution meeting between involved agents"
    fi
    
    # Update conflict record
    tmp_file=$(mktemp)
    jq --arg strategy "$RESOLUTION_STRATEGY" --arg timestamp "$(date -Iseconds)" '
        .resolution_strategy = $strategy |
        .status = "in_resolution" |
        .resolution_notes = "Automatic resolution strategy applied" |
        .resolved_timestamp = $timestamp
    ' "$conflict_file" > "$tmp_file" && mv "$tmp_file" "$conflict_file"
    
    echo "    Applied resolution strategy: $RESOLUTION_STRATEGY"
}

resolve_resource_conflict() {
    local conflict_file="$1"
    
    RESOLUTION_STRATEGY="Implement resource scheduling and coordination protocols"
    
    # Create coordination plan
    COORDINATION_FILE="work/conflicts/coordination_plan_$(basename "$conflict_file" .json).md"
    
    cat > "$COORDINATION_FILE" << EOF
# Resource Conflict Coordination Plan

**Generated:** $(date)
**Conflict:** $(jq -r '.conflict_id' "$conflict_file")

## Coordination Strategy

### Resource Scheduling
- Implement time-boxed development windows
- Establish shared resource booking system
- Create handoff checkpoints between agents

### Communication Protocol
- Daily stand-up meetings for overlapping work
- Shared documentation updates
- Real-time conflict notification system

### Technical Solutions
- Branch-based development workflows
- Automated merge conflict detection
- Shared development environment management

## Implementation Plan

1. **Immediate (24 hours)**
   - Notify affected agents
   - Implement temporary coordination measures
   - Schedule conflict resolution meeting

2. **Short-term (1 week)**
   - Establish formal coordination protocols
   - Implement technical solutions
   - Create monitoring dashboard

3. **Long-term (1 month)**
   - Evaluate effectiveness
   - Optimize coordination processes
   - Update agent workflows

EOF

    # Update conflict record
    tmp_file=$(mktemp)
    jq --arg strategy "$RESOLUTION_STRATEGY" --arg timestamp "$(date -Iseconds)" '
        .resolution_strategy = $strategy |
        .status = "coordinated" |
        .resolution_notes = "Coordination plan created" |
        .resolved_timestamp = $timestamp
    ' "$conflict_file" > "$tmp_file" && mv "$tmp_file" "$conflict_file"
    
    echo "    Created coordination plan: $COORDINATION_FILE"
}

resolve_responsibility_conflict() {
    local conflict_file="$1"
    
    RESOLUTION_STRATEGY="Clarify agent boundaries and establish collaboration protocols"
    
    # Update conflict record with boundary clarification
    tmp_file=$(mktemp)
    jq --arg strategy "$RESOLUTION_STRATEGY" --arg timestamp "$(date -Iseconds)" '
        .resolution_strategy = $strategy |
        .status = "clarified" |
        .resolution_notes = "Agent boundaries clarified, collaboration protocols established" |
        .resolved_timestamp = $timestamp
    ' "$conflict_file" > "$tmp_file" && mv "$tmp_file" "$conflict_file"
    
    echo "    Applied boundary clarification strategy"
}

generate_conflict_report() {
    echo "📋 Generating conflict resolution report..."
    
    REPORT_FILE="work/conflicts/conflict_report_$(date +%Y%m%d_%H%M%S).md"
    
    cat > "$REPORT_FILE" << EOF
# Agent Conflict Resolution Report

**Generated:** $(date)

## Executive Summary

$(
TOTAL_CONFLICTS=$(find work/conflicts -name "conflict_*.json" 2>/dev/null | wc -l)
RESOLVED_CONFLICTS=$(find work/conflicts -name "conflict_*.json" -exec jq -r 'select(.status != "detected") | .conflict_id' {} \; 2>/dev/null | wc -l)
ACTIVE_CONFLICTS=$((TOTAL_CONFLICTS - RESOLVED_CONFLICTS))

echo "- **Total Conflicts Detected:** $TOTAL_CONFLICTS"
echo "- **Resolved Conflicts:** $RESOLVED_CONFLICTS"  
echo "- **Active Conflicts:** $ACTIVE_CONFLICTS"

if [[ $ACTIVE_CONFLICTS -eq 0 ]]; then
    echo "- **Status:** 🟢 All conflicts resolved or managed"
elif [[ $ACTIVE_CONFLICTS -le 2 ]]; then
    echo "- **Status:** 🟡 Minor conflicts require attention"
else
    echo "- **Status:** 🔴 Multiple conflicts need resolution"
fi
)

## Conflict Analysis by Type

### Requirement Conflicts
$(
REQ_CONFLICTS=$(find work/conflicts -name "conflict_*.json" -exec jq -r 'select(.type == "requirements") | .conflict_id' {} \; 2>/dev/null | wc -l)
echo "**Count:** $REQ_CONFLICTS conflicts"

if [[ $REQ_CONFLICTS -gt 0 ]]; then
    echo ""
    echo "**Recent Requirements Conflicts:**"
    find work/conflicts -name "conflict_*.json" -exec jq -r 'select(.type == "requirements") | "- " + .description + " (" + .severity + ")"' {} \; 2>/dev/null | head -3
fi
)

### Resource Conflicts
$(
RES_CONFLICTS=$(find work/conflicts -name "conflict_*.json" -exec jq -r 'select(.type == "resources") | .conflict_id' {} \; 2>/dev/null | wc -l)
echo "**Count:** $RES_CONFLICTS conflicts"

if [[ $RES_CONFLICTS -gt 0 ]]; then
    echo ""
    echo "**Recent Resource Conflicts:**"
    find work/conflicts -name "conflict_*.json" -exec jq -r 'select(.type == "resources") | "- " + .description + " (" + .severity + ")"' {} \; 2>/dev/null | head -3
fi
)

### Responsibility Overlaps
$(
RESP_CONFLICTS=$(find work/conflicts -name "conflict_*.json" -exec jq -r 'select(.type == "responsibilities") | .conflict_id' {} \; 2>/dev/null | wc -l)
echo "**Count:** $RESP_CONFLICTS overlaps"

if [[ $RESP_CONFLICTS -gt 0 ]]; then
    echo ""
    echo "**Recent Responsibility Overlaps:**"
    find work/conflicts -name "conflict_*.json" -exec jq -r 'select(.type == "responsibilities") | "- " + .description + " (" + .severity + ")"' {} \; 2>/dev/null | head -3
fi
)

## Resolution Status

| Conflict ID | Type | Severity | Status | Resolution Strategy |
|-------------|------|----------|--------|-------------------|
$(
find work/conflicts -name "conflict_*.json" 2>/dev/null | while read conflict_file; do
    if [[ -f "$conflict_file" ]]; then
        ID=$(jq -r '.conflict_id' "$conflict_file" 2>/dev/null)
        TYPE=$(jq -r '.type' "$conflict_file" 2>/dev/null)
        SEVERITY=$(jq -r '.severity' "$conflict_file" 2>/dev/null)
        STATUS=$(jq -r '.status' "$conflict_file" 2>/dev/null)
        STRATEGY=$(jq -r '.resolution_strategy // "None"' "$conflict_file" 2>/dev/null)
        echo "| $(basename "$ID") | $TYPE | $SEVERITY | $STATUS | $STRATEGY |"
    fi
done
)

## Recommendations

### Immediate Actions (24 hours)
$(
find work/conflicts -name "conflict_*.json" -exec jq -r 'select(.status == "detected" and .severity == "high") | "- Address high-severity conflict: " + .description' {} \; 2>/dev/null
if [[ $? -ne 0 ]] || [[ -z "$(find work/conflicts -name "conflict_*.json" -exec jq -r 'select(.status == "detected" and .severity == "high") | .description' {} \; 2>/dev/null)" ]]; then
    echo "- No high-severity conflicts requiring immediate attention"
fi
)

### Short-term Improvements (1 week)
- Implement proactive conflict detection mechanisms
- Establish regular conflict review meetings
- Create agent coordination protocols
- Develop conflict resolution playbooks

### Long-term Prevention (1 month)
- Enhance agent boundary definitions
- Implement automated resource scheduling
- Create conflict prediction models
- Establish performance metrics for conflict resolution

## Conflict Trends

$(
if [[ $TOTAL_CONFLICTS -gt 0 ]]; then
    echo "### Weekly Conflict Volume"
    echo "- Current week conflicts: $(find work/conflicts -name "conflict_*.json" -newer $(date -d '7 days ago' '+%Y-%m-%d' 2>/dev/null && echo "$(date -d '7 days ago' '+%Y%m%d')" || echo "20230101") 2>/dev/null | wc -l)"
    echo "- Resolution rate: $((RESOLVED_CONFLICTS * 100 / TOTAL_CONFLICTS))%"
    echo "- Average resolution time: $(if [[ $RESOLVED_CONFLICTS -gt 0 ]]; then echo "~24 hours (estimated)"; else echo "N/A"; fi)"
else
    echo "### Baseline Established"
    echo "- This is the initial conflict assessment"
    echo "- Future reports will show trend analysis"
fi
)

EOF
    
    echo "📄 Conflict resolution report: $REPORT_FILE"
}

# Main execution logic
case "$ACTION" in
    "detect")
        echo "🔍 Detecting all types of conflicts..."
        
        total_conflicts=0
        
        if [[ "$CONFLICT_TYPE" == "all" || "$CONFLICT_TYPE" == "requirements" ]]; then
            detect_requirement_conflicts
            total_conflicts=$((total_conflicts + $?))
        fi
        
        if [[ "$CONFLICT_TYPE" == "all" || "$CONFLICT_TYPE" == "resources" ]]; then
            detect_resource_conflicts
            total_conflicts=$((total_conflicts + $?))
        fi
        
        if [[ "$CONFLICT_TYPE" == "all" || "$CONFLICT_TYPE" == "responsibilities" ]]; then
            detect_responsibility_overlaps
            total_conflicts=$((total_conflicts + $?))
        fi
        
        EXIT_CODE=$total_conflicts
        ;;
        
    "resolve")
        resolve_conflicts "$CONFLICT_TYPE"
        EXIT_CODE=$?
        ;;
        
    "report")
        generate_conflict_report
        ;;
        
    "escalate")
        echo "📢 Escalating unresolved conflicts..."
        
        # Find high-severity unresolved conflicts
        HIGH_SEVERITY_CONFLICTS=$(find work/conflicts -name "conflict_*.json" -exec jq -r 'select(.status == "detected" and .severity == "high") | .conflict_id' {} \; 2>/dev/null)
        
        if [[ -n "$HIGH_SEVERITY_CONFLICTS" ]]; then
            ESCALATION_FILE="work/conflicts/escalation_$(date +%Y%m%d_%H%M%S).md"
            
            cat > "$ESCALATION_FILE" << EOF
# Conflict Escalation Notice

**Generated:** $(date)
**Priority:** HIGH

## Escalated Conflicts

$(echo "$HIGH_SEVERITY_CONFLICTS" | while read conflict_id; do
    conflict_file="work/conflicts/${conflict_id}.json"
    if [[ -f "$conflict_file" ]]; then
        echo "### $conflict_id"
        echo "- **Type:** $(jq -r '.type' "$conflict_file")"
        echo "- **Agents:** $(jq -r '.agents_involved' "$conflict_file")"
        echo "- **Description:** $(jq -r '.description' "$conflict_file")"
        echo ""
    fi
done)

## Required Actions

1. **Immediate Management Review** - High-severity conflicts require management intervention
2. **Agent Coordination Meeting** - Schedule meeting with involved agents
3. **Process Review** - Evaluate current conflict resolution processes
4. **Timeline Impact Assessment** - Assess impact on project timelines

## Next Steps

- [ ] Schedule management review meeting
- [ ] Notify affected stakeholders
- [ ] Implement temporary mitigation measures
- [ ] Update conflict resolution procedures

EOF
            
            echo "📢 Escalation notice created: $ESCALATION_FILE"
            EXIT_CODE=1
        else
            echo "📋 No high-severity conflicts require escalation"
            EXIT_CODE=0
        fi
        ;;
        
    *)
        echo "❌ Unknown action: $ACTION"
        echo "Available actions: detect, resolve, report, escalate"
        exit 1
        ;;
esac

# Log conflict resolution activity
echo "$(date): Conflict resolution $ACTION completed - Type: $CONFLICT_TYPE, Exit: $EXIT_CODE" >> work/conflict-resolution.log

if [[ $EXIT_CODE -eq 0 ]]; then
    echo "✅ Conflict resolution completed successfully"
else
    echo "⚠️ Conflicts detected or unresolved ($EXIT_CODE) - review conflict reports"
fi

echo "⚖️ Agent Conflict Resolution Hook completed"
exit $EXIT_CODE