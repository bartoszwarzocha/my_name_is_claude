#!/bin/bash
#
# Claude Code Framework - Intelligent Agent Selection Optimizer
# Advanced agent coordination and workload optimization
#

set -euo pipefail

# Colors and symbols
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
WHITE='\033[1;37m'
BOLD='\033[1m'
NC='\033[0m'
CHECK="✅"
INFO="ℹ️"
BRAIN="🧠"
TARGET="🎯"
GEAR="⚙️"
CHART="📊"

# Agent capability matrix - maps agents to their primary capabilities
declare -A AGENT_CAPABILITIES
AGENT_CAPABILITIES[business-analyst]="requirements:95,stakeholder:90,process:85,documentation:80"
AGENT_CAPABILITIES[product-manager]="strategy:95,roadmap:90,features:85,prioritization:90"
AGENT_CAPABILITIES[software-architect]="architecture:95,patterns:90,scalability:85,integration:80"
AGENT_CAPABILITIES[ux-designer]="design:95,usability:90,accessibility:85,research:80"
AGENT_CAPABILITIES[frontend-engineer]="ui:95,javascript:90,frameworks:85,responsive:80"
AGENT_CAPABILITIES[backend-engineer]="api:90,database:85,performance:80,security:75"
AGENT_CAPABILITIES[api-engineer]="api:95,microservices:90,integration:85,documentation:80"
AGENT_CAPABILITIES[data-engineer]="database:95,etl:90,analytics:85,optimization:80"
AGENT_CAPABILITIES[qa-engineer]="testing:95,automation:90,quality:85,performance:80"
AGENT_CAPABILITIES[security-engineer]="security:95,compliance:90,audit:85,threats:90"
AGENT_CAPABILITIES[deployment-engineer]="devops:95,cicd:90,infrastructure:85,monitoring:80"
AGENT_CAPABILITIES[reviewer]="review:95,quality:90,validation:85,compliance:80"

# Agent workload capacity (relative effort units)
declare -A AGENT_CAPACITY
AGENT_CAPACITY[business-analyst]=8
AGENT_CAPACITY[product-manager]=10
AGENT_CAPACITY[software-architect]=12
AGENT_CAPACITY[ux-designer]=8
AGENT_CAPACITY[frontend-engineer]=15
AGENT_CAPACITY[backend-engineer]=15
AGENT_CAPACITY[api-engineer]=12
AGENT_CAPACITY[data-engineer]=10
AGENT_CAPACITY[qa-engineer]=12
AGENT_CAPACITY[security-engineer]=8
AGENT_CAPACITY[deployment-engineer]=10
AGENT_CAPACITY[reviewer]=6

# Initialize agent optimizer
init_agent_optimizer() {
    echo -e "${GEAR} ${BOLD}INTELLIGENT AGENT SELECTION OPTIMIZATION${NC}"
    echo "================================================================================"
    echo -e "${INFO} Analyzing project requirements for optimal agent coordination..."
    echo
}

# Analyze project requirements for agent optimization
analyze_project_requirements() {
    local project_profile="$1"

    echo -e "${BRAIN} ${BOLD}PROJECT REQUIREMENT ANALYSIS${NC}"
    echo "================================================================================"

    # Extract key project characteristics
    local complexity_score=$(echo "$project_profile" | grep -o '"complexity_score":[0-9]*' | cut -d':' -f2 || echo "2")
    local dependency_score=$(echo "$project_profile" | grep -o '"dependency_score":[0-9]*' | cut -d':' -f2 || echo "2")
    local risk_score=$(echo "$project_profile" | grep -o '"risk_score":[0-9]*' | cut -d':' -f2 || echo "1")
    local business_type=$(echo "$project_profile" | grep -o '"business_type":"[^"]*"' | cut -d'"' -f4 || echo "general")
    local scale=$(echo "$project_profile" | grep -o '"scale":"[^"]*"' | cut -d'"' -f4 || echo "sme")

    echo -e "${INFO} Project Complexity: ${CYAN}$complexity_score/4${NC}"
    echo -e "${INFO} Dependency Complexity: ${CYAN}$dependency_score/4${NC}"
    echo -e "${INFO} Risk Level: ${CYAN}$risk_score/10${NC}"
    echo -e "${INFO} Business Domain: ${CYAN}$business_type${NC}"
    echo -e "${INFO} Project Scale: ${CYAN}$scale${NC}"

    # Calculate requirement weights
    local requirements=$(calculate_requirement_weights "$complexity_score" "$dependency_score" "$risk_score" "$business_type" "$scale")

    echo -e "${CHECK} Project requirements analyzed!"
    echo "$requirements"
}

# Calculate requirement weights based on project characteristics
calculate_requirement_weights() {
    local complexity_score="$1"
    local dependency_score="$2"
    local risk_score="$3"
    local business_type="$4"
    local scale="$5"

    # Base requirement weights
    local requirements_weight=70
    local architecture_weight=60
    local development_weight=80
    local security_weight=50
    local testing_weight=60
    local deployment_weight=40

    # Adjust weights based on complexity
    if [[ $complexity_score -ge 3 ]]; then
        architecture_weight=$((architecture_weight + 20))
        testing_weight=$((testing_weight + 15))
        deployment_weight=$((deployment_weight + 15))
    fi

    # Adjust weights based on dependencies
    if [[ $dependency_score -ge 3 ]]; then
        architecture_weight=$((architecture_weight + 15))
        deployment_weight=$((deployment_weight + 20))
    fi

    # Adjust weights based on risk
    if [[ $risk_score -ge 5 ]]; then
        security_weight=$((security_weight + 30))
        testing_weight=$((testing_weight + 20))
    fi

    # Adjust weights based on business domain
    case "$business_type" in
        "fintech"|"healthcare")
            security_weight=$((security_weight + 40))
            testing_weight=$((testing_weight + 25))
            requirements_weight=$((requirements_weight + 15))
            ;;
        "ecommerce")
            development_weight=$((development_weight + 20))
            security_weight=$((security_weight + 20))
            ;;
        "enterprise")
            architecture_weight=$((architecture_weight + 25))
            security_weight=$((security_weight + 20))
            deployment_weight=$((deployment_weight + 25))
            ;;
    esac

    # Adjust weights based on scale
    case "$scale" in
        "startup")
            development_weight=$((development_weight + 20))
            deployment_weight=$((deployment_weight - 10))
            ;;
        "enterprise")
            architecture_weight=$((architecture_weight + 30))
            security_weight=$((security_weight + 25))
            testing_weight=$((testing_weight + 20))
            deployment_weight=$((deployment_weight + 30))
            ;;
    esac

    # Generate requirements JSON
    cat <<EOF
{
    "requirements": $requirements_weight,
    "architecture": $architecture_weight,
    "development": $development_weight,
    "security": $security_weight,
    "testing": $testing_weight,
    "deployment": $deployment_weight
}
EOF
}

# Optimize agent selection based on requirements
optimize_agent_selection() {
    local project_requirements="$1"

    echo -e "${TARGET} ${BOLD}AGENT SELECTION OPTIMIZATION${NC}"
    echo "================================================================================"
    echo -e "${INFO} Computing optimal agent combinations..."

    # Extract requirement weights
    local req_requirements=$(echo "$project_requirements" | grep -o '"requirements":[0-9]*' | cut -d':' -f2)
    local req_architecture=$(echo "$project_requirements" | grep -o '"architecture":[0-9]*' | cut -d':' -f2)
    local req_development=$(echo "$project_requirements" | grep -o '"development":[0-9]*' | cut -d':' -f2)
    local req_security=$(echo "$project_requirements" | grep -o '"security":[0-9]*' | cut -d':' -f2)
    local req_testing=$(echo "$project_requirements" | grep -o '"testing":[0-9]*' | cut -d':' -f2)
    local req_deployment=$(echo "$project_requirements" | grep -o '"deployment":[0-9]*' | cut -d':' -f2)

    # Calculate agent scores
    local agent_scores=""
    agent_scores=$(calculate_agent_scores "$req_requirements" "$req_architecture" "$req_development" "$req_security" "$req_testing" "$req_deployment")

    # Select optimal agent combination
    local optimal_agents=$(select_optimal_agent_combination "$agent_scores")

    echo -e "${CHECK} Agent selection optimized!"
    echo "$optimal_agents"
}

# Calculate agent scores based on requirements
calculate_agent_scores() {
    local req_requirements="$1"
    local req_architecture="$2"
    local req_development="$3"
    local req_security="$4"
    local req_testing="$5"
    local req_deployment="$6"

    local scores_json="{"
    local first=true

    for agent in "${!AGENT_CAPABILITIES[@]}"; do
        local capabilities="${AGENT_CAPABILITIES[$agent]}"
        local score=0

        # Parse agent capabilities
        local requirements_cap=$(echo "$capabilities" | grep -o 'requirements:[0-9]*' | cut -d':' -f2 || echo "0")
        local architecture_cap=$(echo "$capabilities" | grep -o 'architecture:[0-9]*' | cut -d':' -f2 || echo "0")
        local api_cap=$(echo "$capabilities" | grep -o 'api:[0-9]*' | cut -d':' -f2 || echo "0")
        local ui_cap=$(echo "$capabilities" | grep -o 'ui:[0-9]*' | cut -d':' -f2 || echo "0")
        local database_cap=$(echo "$capabilities" | grep -o 'database:[0-9]*' | cut -d':' -f2 || echo "0")
        local security_cap=$(echo "$capabilities" | grep -o 'security:[0-9]*' | cut -d':' -f2 || echo "0")
        local testing_cap=$(echo "$capabilities" | grep -o 'testing:[0-9]*' | cut -d':' -f2 || echo "0")
        local devops_cap=$(echo "$capabilities" | grep -o 'devops:[0-9]*' | cut -d':' -f2 || echo "0")

        # Calculate weighted score
        score=$((
            (requirements_cap * req_requirements / 100) +
            (architecture_cap * req_architecture / 100) +
            ((api_cap + ui_cap + database_cap) * req_development / 300) +
            (security_cap * req_security / 100) +
            (testing_cap * req_testing / 100) +
            (devops_cap * req_deployment / 100)
        ))

        # Add to scores JSON
        if [[ "$first" = true ]]; then
            first=false
        else
            scores_json+=","
        fi
        scores_json+="\"$agent\":$score"
    done

    scores_json+="}"
    echo "$scores_json"
}

# Select optimal agent combination
select_optimal_agent_combination() {
    local agent_scores="$1"

    echo -e "${CHART} ${BOLD}AGENT COMBINATION OPTIMIZATION${NC}"
    echo "================================================================================"

    # Sort agents by score
    local sorted_agents=()
    for agent in "${!AGENT_CAPABILITIES[@]}"; do
        local score=$(echo "$agent_scores" | grep -o "\"$agent\":[0-9]*" | cut -d':' -f2)
        sorted_agents+=("$score:$agent")
    done

    # Sort by score (descending)
    IFS=$'\n' sorted_agents=($(sort -rn <<< "${sorted_agents[*]}"))

    # Select agents based on scores and capacity constraints
    local selected_agents=()
    local total_workload=0
    local max_workload=100  # Maximum project workload units

    echo -e "${INFO} Agent Selection Process:"

    for item in "${sorted_agents[@]}"; do
        IFS=':' read -ra PARTS <<< "$item"
        local score="${PARTS[0]}"
        local agent="${PARTS[1]}"
        local capacity="${AGENT_CAPACITY[$agent]}"

        if [[ $score -gt 50 && $((total_workload + capacity)) -le $max_workload ]]; then
            selected_agents+=("$agent")
            total_workload=$((total_workload + capacity))
            echo -e "   ${CHECK} ${GREEN}$agent${NC} (score: $score, capacity: $capacity)"
        elif [[ $score -le 50 ]]; then
            echo -e "   ⚪ ${YELLOW}$agent${NC} (score: $score - below threshold)"
        else
            echo -e "   ❌ ${CYAN}$agent${NC} (score: $score - capacity exceeded)"
        fi
    done

    echo -e "${INFO} Total Workload: ${CYAN}$total_workload/$max_workload units${NC}"

    # Generate agent combination JSON
    local agents_json=$(printf '%s\n' "${selected_agents[@]}" | jq -R . | jq -s .)
    cat <<EOF
{
    "selected_agents": $agents_json,
    "total_workload": $total_workload,
    "max_workload": $max_workload,
    "utilization": $((total_workload * 100 / max_workload))
}
EOF
}

# Optimize agent coordination patterns
optimize_agent_coordination() {
    local selected_agents="$1"
    local project_requirements="$2"

    echo -e "${GEAR} ${BOLD}AGENT COORDINATION OPTIMIZATION${NC}"
    echo "================================================================================"
    echo -e "${INFO} Optimizing agent coordination patterns and handoffs..."

    # Extract selected agents
    local agents_array=$(echo "$selected_agents" | grep -o '"selected_agents":\[[^]]*\]' | cut -d'[' -f2 | cut -d']' -f1 | tr ',' '\n' | tr -d '"')

    # Analyze agent dependencies
    local coordination_plan=$(analyze_agent_dependencies "$agents_array")

    # Optimize parallel vs sequential execution
    local execution_plan=$(optimize_execution_patterns "$agents_array" "$coordination_plan")

    # Generate handoff protocols
    local handoff_protocols=$(generate_handoff_protocols "$agents_array" "$execution_plan")

    echo -e "${CHECK} Agent coordination optimized!"

    # Combine coordination data
    cat <<EOF
{
    "coordination_plan": $coordination_plan,
    "execution_plan": $execution_plan,
    "handoff_protocols": $handoff_protocols
}
EOF
}

# Analyze agent dependencies
analyze_agent_dependencies() {
    local agents_array="$1"

    # Define dependency matrix
    declare -A DEPENDENCIES
    DEPENDENCIES[business-analyst]=""
    DEPENDENCIES[product-manager]="business-analyst"
    DEPENDENCIES[software-architect]="product-manager"
    DEPENDENCIES[ux-designer]="product-manager"
    DEPENDENCIES[frontend-engineer]="ux-designer,software-architect"
    DEPENDENCIES[backend-engineer]="software-architect"
    DEPENDENCIES[api-engineer]="software-architect"
    DEPENDENCIES[data-engineer]="software-architect"
    DEPENDENCIES[qa-engineer]="frontend-engineer,backend-engineer,api-engineer"
    DEPENDENCIES[security-engineer]="software-architect"
    DEPENDENCIES[deployment-engineer]="qa-engineer,security-engineer"
    DEPENDENCIES[reviewer]="*"

    local dependencies_json="{"
    local first=true

    while IFS= read -r agent; do
        [[ -z "$agent" ]] && continue

        if [[ "$first" = true ]]; then
            first=false
        else
            dependencies_json+=","
        fi

        local deps="${DEPENDENCIES[$agent]:-}"
        if [[ -n "$deps" ]]; then
            local deps_array=$(echo "$deps" | tr ',' '\n' | jq -R . | jq -s .)
            dependencies_json+="\"$agent\":$deps_array"
        else
            dependencies_json+="\"$agent\":[]"
        fi
    done <<< "$agents_array"

    dependencies_json+="}"
    echo "$dependencies_json"
}

# Optimize execution patterns
optimize_execution_patterns() {
    local agents_array="$1"
    local coordination_plan="$2"

    # Create execution phases based on dependencies
    local phases="["
    local phase_num=1

    # Phase 1: Requirements and Planning
    local phase1_agents=()
    while IFS= read -r agent; do
        [[ -z "$agent" ]] && continue
        if [[ "$agent" == "business-analyst" || "$agent" == "product-manager" ]]; then
            phase1_agents+=("\"$agent\"")
        fi
    done <<< "$agents_array"

    if [[ ${#phase1_agents[@]} -gt 0 ]]; then
        local phase1_json=$(IFS=','; echo "[${phase1_agents[*]}]")
        phases+="{\"phase\":$phase_num,\"name\":\"Requirements & Planning\",\"agents\":$phase1_json,\"parallel\":false},"
        phase_num=$((phase_num + 1))
    fi

    # Phase 2: Architecture and Design
    local phase2_agents=()
    while IFS= read -r agent; do
        [[ -z "$agent" ]] && continue
        if [[ "$agent" == "software-architect" || "$agent" == "ux-designer" ]]; then
            phase2_agents+=("\"$agent\"")
        fi
    done <<< "$agents_array"

    if [[ ${#phase2_agents[@]} -gt 0 ]]; then
        local phase2_json=$(IFS=','; echo "[${phase2_agents[*]}]")
        phases+="{\"phase\":$phase_num,\"name\":\"Architecture & Design\",\"agents\":$phase2_json,\"parallel\":true},"
        phase_num=$((phase_num + 1))
    fi

    # Phase 3: Development
    local phase3_agents=()
    while IFS= read -r agent; do
        [[ -z "$agent" ]] && continue
        if [[ "$agent" == "frontend-engineer" || "$agent" == "backend-engineer" || "$agent" == "api-engineer" || "$agent" == "data-engineer" ]]; then
            phase3_agents+=("\"$agent\"")
        fi
    done <<< "$agents_array"

    if [[ ${#phase3_agents[@]} -gt 0 ]]; then
        local phase3_json=$(IFS=','; echo "[${phase3_agents[*]}]")
        phases+="{\"phase\":$phase_num,\"name\":\"Core Development\",\"agents\":$phase3_json,\"parallel\":true},"
        phase_num=$((phase_num + 1))
    fi

    # Phase 4: Quality and Security
    local phase4_agents=()
    while IFS= read -r agent; do
        [[ -z "$agent" ]] && continue
        if [[ "$agent" == "qa-engineer" || "$agent" == "security-engineer" ]]; then
            phase4_agents+=("\"$agent\"")
        fi
    done <<< "$agents_array"

    if [[ ${#phase4_agents[@]} -gt 0 ]]; then
        local phase4_json=$(IFS=','; echo "[${phase4_agents[*]}]")
        phases+="{\"phase\":$phase_num,\"name\":\"Quality & Security\",\"agents\":$phase4_json,\"parallel\":false},"
        phase_num=$((phase_num + 1))
    fi

    # Phase 5: Deployment
    local phase5_agents=()
    while IFS= read -r agent; do
        [[ -z "$agent" ]] && continue
        if [[ "$agent" == "deployment-engineer" ]]; then
            phase5_agents+=("\"$agent\"")
        fi
    done <<< "$agents_array"

    if [[ ${#phase5_agents[@]} -gt 0 ]]; then
        local phase5_json=$(IFS=','; echo "[${phase5_agents[*]}]")
        phases+="{\"phase\":$phase_num,\"name\":\"Deployment & Launch\",\"agents\":$phase5_json,\"parallel\":false},"
        phase_num=$((phase_num + 1))
    fi

    # Review Phase (if reviewer is selected)
    while IFS= read -r agent; do
        [[ -z "$agent" ]] && continue
        if [[ "$agent" == "reviewer" ]]; then
            phases+="{\"phase\":\"continuous\",\"name\":\"Quality Review\",\"agents\":[\"reviewer\"],\"parallel\":false},"
            break
        fi
    done <<< "$agents_array"

    # Remove trailing comma and close array
    phases="${phases%,}"
    phases+="]"

    echo "$phases"
}

# Generate handoff protocols
generate_handoff_protocols() {
    local agents_array="$1"
    local execution_plan="$2"

    local protocols="["
    local first=true

    # Standard handoff protocols
    local handoffs=(
        "business-analyst→product-manager:Requirements to Strategy"
        "product-manager→software-architect:Strategy to Architecture"
        "product-manager→ux-designer:Strategy to Design"
        "software-architect→backend-engineer:Architecture to Implementation"
        "software-architect→api-engineer:Architecture to API Development"
        "ux-designer→frontend-engineer:Design to UI Implementation"
        "frontend-engineer→qa-engineer:UI to Testing"
        "backend-engineer→qa-engineer:Backend to Testing"
        "api-engineer→qa-engineer:API to Testing"
        "qa-engineer→deployment-engineer:Testing to Deployment"
        "security-engineer→deployment-engineer:Security to Deployment"
    )

    for handoff in "${handoffs[@]}"; do
        IFS='→' read -ra HANDOFF_PARTS <<< "$handoff"
        IFS=':' read -ra DESC_PARTS <<< "${HANDOFF_PARTS[1]}"
        local from_agent="${HANDOFF_PARTS[0]}"
        local to_agent="${DESC_PARTS[0]}"
        local description="${DESC_PARTS[1]}"

        # Check if both agents are in selected agents
        if grep -q "$from_agent" <<< "$agents_array" && grep -q "$to_agent" <<< "$agents_array"; then
            if [[ "$first" = true ]]; then
                first=false
            else
                protocols+=","
            fi

            protocols+="{\"from\":\"$from_agent\",\"to\":\"$to_agent\",\"description\":\"$description\",\"requirements\":[\"Complete deliverables\",\"Update documentation\",\"Notify next agent\"]}"
        fi
    done

    protocols+="]"
    echo "$protocols"
}

# Main optimization function
optimize_project_agents() {
    local project_profile="$1"

    init_agent_optimizer

    local requirements=$(analyze_project_requirements "$project_profile")
    local selection=$(optimize_agent_selection "$requirements")
    local coordination=$(optimize_agent_coordination "$selection" "$requirements")

    # Generate final optimization report
    cat <<EOF
{
    "project_requirements": $requirements,
    "agent_selection": $selection,
    "coordination_optimization": $coordination,
    "optimization_timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
EOF
}

# Execute if run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    if [[ $# -lt 1 ]]; then
        echo "Usage: $0 <project_profile_json>"
        echo "Example: $0 '{\"complexity_score\":2,\"business_type\":\"ecommerce\"}'"
        exit 1
    fi

    optimize_project_agents "$1"
fi