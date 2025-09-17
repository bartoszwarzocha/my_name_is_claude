#!/bin/bash
#
# Claude Code Framework - AI-Powered Agent Selector
# Intelligent agent recommendation based on project analysis
#

set -euo pipefail

# Colors and symbols
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
BOLD='\033[1m'
NC='\033[0m'
CHECK="✅"
INFO="ℹ️"
ROBOT="🤖"
TARGET="🎯"

# Agent definitions with specializations
declare -A AGENT_SPECIALIZATIONS
AGENT_SPECIALIZATIONS[frontend-engineer]="Modern frontend development, React/Angular/Vue, responsive design, performance optimization"
AGENT_SPECIALIZATIONS[backend-engineer]="Server-side systems, business logic, API development, database integration"
AGENT_SPECIALIZATIONS[api-engineer]="REST/GraphQL APIs, microservices architecture, service integration"
AGENT_SPECIALIZATIONS[data-engineer]="Database design, ETL pipelines, data architecture, analytics"
AGENT_SPECIALIZATIONS[security-engineer]="Security architecture, threat modeling, compliance, vulnerability assessment"
AGENT_SPECIALIZATIONS[qa-engineer]="Test automation, quality assurance, performance testing, CI/CD"
AGENT_SPECIALIZATIONS[ux-designer]="User experience design, accessibility, design systems, user research"
AGENT_SPECIALIZATIONS[software-architect]="System architecture, technology selection, scalability planning"
AGENT_SPECIALIZATIONS[business-analyst]="Requirements gathering, stakeholder management, process analysis"
AGENT_SPECIALIZATIONS[product-manager]="Product strategy, user stories, MVP scoping, roadmap planning"
AGENT_SPECIALIZATIONS[deployment-engineer]="CI/CD pipelines, infrastructure automation, cloud deployment"
AGENT_SPECIALIZATIONS[mobile-developer]="Mobile applications, cross-platform development, app optimization"

# Technology-to-agent mapping
declare -A TECH_AGENT_MAP
TECH_AGENT_MAP[react]="frontend-engineer:95,ux-designer:80,qa-engineer:75"
TECH_AGENT_MAP[angular]="frontend-engineer:95,ux-designer:80,qa-engineer:75"
TECH_AGENT_MAP[vue]="frontend-engineer:95,ux-designer:80,qa-engineer:75"
TECH_AGENT_MAP[nodejs]="backend-engineer:90,api-engineer:85"
TECH_AGENT_MAP[express]="backend-engineer:85,api-engineer:90"
TECH_AGENT_MAP[nestjs]="backend-engineer:90,api-engineer:95"
TECH_AGENT_MAP[python]="backend-engineer:85,data-engineer:80"
TECH_AGENT_MAP[django]="backend-engineer:90,api-engineer:85"
TECH_AGENT_MAP[fastapi]="backend-engineer:85,api-engineer:95"
TECH_AGENT_MAP[java]="backend-engineer:90,software-architect:80"
TECH_AGENT_MAP[spring-boot]="backend-engineer:95,api-engineer:90"
TECH_AGENT_MAP[postgresql]="data-engineer:95,backend-engineer:75"
TECH_AGENT_MAP[mongodb]="data-engineer:90,backend-engineer:75"
TECH_AGENT_MAP[mysql]="data-engineer:90,backend-engineer:75"
TECH_AGENT_MAP[redis]="data-engineer:80,backend-engineer:70"
TECH_AGENT_MAP[docker]="deployment-engineer:90,backend-engineer:70"
TECH_AGENT_MAP[kubernetes]="deployment-engineer:95,software-architect:80"
TECH_AGENT_MAP[terraform]="deployment-engineer:85,software-architect:75"

# Business domain to agent mapping
declare -A DOMAIN_AGENT_MAP
DOMAIN_AGENT_MAP[fintech]="security-engineer:95,compliance-auditor:90,backend-engineer:85"
DOMAIN_AGENT_MAP[healthcare]="security-engineer:90,compliance-auditor:95,data-engineer:80"
DOMAIN_AGENT_MAP[ecommerce]="frontend-engineer:90,api-engineer:85,security-engineer:80"
DOMAIN_AGENT_MAP[enterprise]="software-architect:90,security-engineer:85,qa-engineer:85"
DOMAIN_AGENT_MAP[gaming]="frontend-engineer:85,performance-engineer:90,qa-engineer:80"
DOMAIN_AGENT_MAP[social]="api-engineer:85,data-engineer:80,security-engineer:75"

# Project scale to agent mapping
declare -A SCALE_AGENT_MAP
SCALE_AGENT_MAP[startup]="frontend-engineer:90,backend-engineer:90,qa-engineer:80"
SCALE_AGENT_MAP[sme]="frontend-engineer:85,backend-engineer:85,qa-engineer:85,security-engineer:80"
SCALE_AGENT_MAP[enterprise]="software-architect:95,security-engineer:90,qa-engineer:90,deployment-engineer:85"

# Agent recommendations with confidence scores
declare -A AGENT_RECOMMENDATIONS
RECOMMENDED_AGENTS=()

# Initialize agent selector
init_selector() {
    echo -e "${ROBOT} ${BOLD}AI-POWERED AGENT SELECTION${NC}"
    echo "================================================================================"
    echo -e "${INFO} Analyzing project requirements for optimal agent recommendations..."
}

# Parse technology stack and calculate agent scores
analyze_technologies() {
    local tech_stack="$1"

    echo -e "${INFO} Analyzing technology stack: ${CYAN}$tech_stack${NC}"

    # Split technologies by comma
    IFS=',' read -ra TECHS <<< "$tech_stack"

    for tech in "${TECHS[@]}"; do
        tech=$(echo "$tech" | xargs) # trim whitespace

        if [[ -n "${TECH_AGENT_MAP[$tech]:-}" ]]; then
            # Parse agent:confidence pairs
            IFS=',' read -ra MAPPINGS <<< "${TECH_AGENT_MAP[$tech]}"

            for mapping in "${MAPPINGS[@]}"; do
                IFS=':' read -ra PAIR <<< "$mapping"
                local agent="${PAIR[0]}"
                local score="${PAIR[1]}"

                # Add to or update agent score
                if [[ -n "${AGENT_RECOMMENDATIONS[$agent]:-}" ]]; then
                    local current_score="${AGENT_RECOMMENDATIONS[$agent]}"
                    local new_score=$((current_score + score))
                    # Cap at 100
                    if [[ $new_score -gt 100 ]]; then
                        new_score=100
                    fi
                    AGENT_RECOMMENDATIONS[$agent]="$new_score"
                else
                    AGENT_RECOMMENDATIONS[$agent]="$score"
                fi
            done
        fi
    done
}

# Apply business domain scoring
analyze_business_domain() {
    local domain="$1"

    echo -e "${INFO} Applying business domain analysis: ${CYAN}$domain${NC}"

    if [[ -n "${DOMAIN_AGENT_MAP[$domain]:-}" ]]; then
        IFS=',' read -ra MAPPINGS <<< "${DOMAIN_AGENT_MAP[$domain]}"

        for mapping in "${MAPPINGS[@]}"; do
            IFS=':' read -ra PAIR <<< "$mapping"
            local agent="${PAIR[0]}"
            local score="${PAIR[1]}"

            # Boost score for domain-specific agents
            if [[ -n "${AGENT_RECOMMENDATIONS[$agent]:-}" ]]; then
                local current_score="${AGENT_RECOMMENDATIONS[$agent]}"
                local boost=$((score / 4)) # 25% boost
                local new_score=$((current_score + boost))
                if [[ $new_score -gt 100 ]]; then
                    new_score=100
                fi
                AGENT_RECOMMENDATIONS[$agent]="$new_score"
            else
                # Add domain-specific agent even if not tech-detected
                AGENT_RECOMMENDATIONS[$agent]="$((score / 2))"
            fi
        done
    fi
}

# Apply project scale considerations
analyze_project_scale() {
    local scale="$1"

    echo -e "${INFO} Applying project scale considerations: ${CYAN}$scale${NC}"

    if [[ -n "${SCALE_AGENT_MAP[$scale]:-}" ]]; then
        IFS=',' read -ra MAPPINGS <<< "${SCALE_AGENT_MAP[$scale]}"

        for mapping in "${MAPPINGS[@]}"; do
            IFS=':' read -ra PAIR <<< "$mapping"
            local agent="${PAIR[0]}"
            local score="${PAIR[1]}"

            # Apply scale-based adjustments
            if [[ -n "${AGENT_RECOMMENDATIONS[$agent]:-}" ]]; then
                local current_score="${AGENT_RECOMMENDATIONS[$agent]}"
                local adjustment=$((score / 10)) # 10% adjustment
                local new_score=$((current_score + adjustment))
                if [[ $new_score -gt 100 ]]; then
                    new_score=100
                fi
                AGENT_RECOMMENDATIONS[$agent]="$new_score"
            else
                # Add scale-important agents
                if [[ $score -gt 80 ]]; then
                    AGENT_RECOMMENDATIONS[$agent]="$((score / 3))"
                fi
            fi
        done
    fi
}

# Apply baseline essential agents
apply_baseline_agents() {
    echo -e "${INFO} Ensuring essential agent coverage..."

    # Essential agents for any project
    local essential_agents=("frontend-engineer:70" "backend-engineer:70" "qa-engineer:65")

    for agent_score in "${essential_agents[@]}"; do
        IFS=':' read -ra PAIR <<< "$agent_score"
        local agent="${PAIR[0]}"
        local min_score="${PAIR[1]}"

        if [[ -z "${AGENT_RECOMMENDATIONS[$agent]:-}" ]] || [[ "${AGENT_RECOMMENDATIONS[$agent]}" -lt "$min_score" ]]; then
            AGENT_RECOMMENDATIONS[$agent]="$min_score"
        fi
    done
}

# Integrate with existing AI system if available
integrate_ai_recommendations() {
    local project_dir="$1"

    echo -e "${INFO} Integrating with AI-powered analysis system..."

    local analyzer_path="$(dirname "$0")/../../ai_tools/bin/project_analyzer.py"

    if [[ -f "$analyzer_path" ]]; then
        echo -e "${INFO} Running advanced AI analysis..."

        # Run AI analyzer and extract agent recommendations
        local ai_output
        if ai_output=$(python3 "$analyzer_path" "$project_dir" 2>/dev/null); then
            echo -e "${CHECK} AI analysis completed successfully"

            # Parse AI recommendations and boost scores
            while IFS= read -r line; do
                if [[ $line =~ (frontend-engineer|backend-engineer|api-engineer|data-engineer|security-engineer|qa-engineer) ]]; then
                    local agent=$(echo "$line" | grep -o '[a-z]*-engineer' | head -1)
                    if [[ -n "$agent" ]]; then
                        # Boost AI-recommended agents
                        if [[ -n "${AGENT_RECOMMENDATIONS[$agent]:-}" ]]; then
                            local current_score="${AGENT_RECOMMENDATIONS[$agent]}"
                            local boosted_score=$((current_score + 15))
                            if [[ $boosted_score -gt 100 ]]; then
                                boosted_score=100
                            fi
                            AGENT_RECOMMENDATIONS[$agent]="$boosted_score"
                        else
                            AGENT_RECOMMENDATIONS[$agent]="75"
                        fi
                    fi
                fi
            done <<< "$ai_output"
        else
            echo -e "${YELLOW}Warning: AI analysis not available, using heuristic recommendations${NC}"
        fi
    else
        echo -e "${YELLOW}Warning: AI analyzer not found, using heuristic recommendations${NC}"
    fi
}

# Sort and categorize recommendations
categorize_recommendations() {
    echo -e "\n${TARGET} ${BOLD}AGENT RECOMMENDATION ANALYSIS${NC}"
    echo "================================================================================"

    # Sort agents by confidence score
    local sorted_agents=()
    for agent in "${!AGENT_RECOMMENDATIONS[@]}"; do
        sorted_agents+=("${AGENT_RECOMMENDATIONS[$agent]}:$agent")
    done

    # Sort by score (descending)
    IFS=$'\n' sorted_agents=($(sort -rn <<< "${sorted_agents[*]}"))

    # Categorize by confidence level
    local high_confidence=()
    local medium_confidence=()
    local low_confidence=()

    for item in "${sorted_agents[@]}"; do
        IFS=':' read -ra PARTS <<< "$item"
        local score="${PARTS[0]}"
        local agent="${PARTS[1]}"

        if [[ $score -ge 80 ]]; then
            high_confidence+=("$agent:$score")
        elif [[ $score -ge 65 ]]; then
            medium_confidence+=("$agent:$score")
        else
            low_confidence+=("$agent:$score")
        fi
    done

    # Display categorized recommendations
    if [[ ${#high_confidence[@]} -gt 0 ]]; then
        echo -e "\n${GREEN}${BOLD}🟢 HIGH PRIORITY AGENTS (Confidence ≥ 80%):${NC}"
        for item in "${high_confidence[@]}"; do
            IFS=':' read -ra PARTS <<< "$item"
            local agent="${PARTS[0]}"
            local score="${PARTS[1]}"
            echo -e "   ${CHECK} ${GREEN}$agent${NC} (confidence: $score%) - ${AGENT_SPECIALIZATIONS[$agent]:-Agent specialization}"
            RECOMMENDED_AGENTS+=("$agent")
        done
    fi

    if [[ ${#medium_confidence[@]} -gt 0 ]]; then
        echo -e "\n${YELLOW}${BOLD}🟡 SUPPORTING AGENTS (Confidence 65-79%):${NC}"
        for item in "${medium_confidence[@]}"; do
            IFS=':' read -ra PARTS <<< "$item"
            local agent="${PARTS[0]}"
            local score="${PARTS[1]}"
            echo -e "   ◯ ${YELLOW}$agent${NC} (confidence: $score%) - ${AGENT_SPECIALIZATIONS[$agent]:-Agent specialization}"
        done
    fi

    if [[ ${#low_confidence[@]} -gt 0 ]]; then
        echo -e "\n${BLUE}${BOLD}🔵 OPTIONAL AGENTS (Confidence < 65%):${NC}"
        for item in "${low_confidence[@]}"; do
            IFS=':' read -ra PARTS <<< "$item"
            local agent="${PARTS[0]}"
            local score="${PARTS[1]}"
            echo -e "   ◯ ${BLUE}$agent${NC} (confidence: $score%) - ${AGENT_SPECIALIZATIONS[$agent]:-Agent specialization}"
        done
    fi
}

# Generate workflow recommendation
generate_workflow_recommendation() {
    echo -e "\n${TARGET} ${BOLD}RECOMMENDED DEVELOPMENT WORKFLOW:${NC}"
    echo "================================================================================"

    # Create workflow based on recommended agents
    local workflow_phases=()

    # Check for planning agents
    if [[ " ${RECOMMENDED_AGENTS[@]} " =~ " business-analyst " ]] || [[ " ${RECOMMENDED_AGENTS[@]} " =~ " product-manager " ]]; then
        workflow_phases+=("${BLUE}1. Planning:${NC} business-analyst → product-manager")
    fi

    # Architecture phase
    if [[ " ${RECOMMENDED_AGENTS[@]} " =~ " software-architect " ]]; then
        workflow_phases+=("${BLUE}2. Architecture:${NC} software-architect → ux-designer")
    fi

    # Development phase
    local dev_agents=()
    for agent in "${RECOMMENDED_AGENTS[@]}"; do
        if [[ "$agent" =~ engineer$ ]] && [[ "$agent" != "software-architect" ]]; then
            dev_agents+=("$agent")
        fi
    done

    if [[ ${#dev_agents[@]} -gt 0 ]]; then
        local dev_phase="Development: $(IFS=' → '; echo "${dev_agents[*]}")"
        workflow_phases+=("${BLUE}3. ${dev_phase}${NC}")
    fi

    # Quality phase
    if [[ " ${RECOMMENDED_AGENTS[@]} " =~ " qa-engineer " ]]; then
        workflow_phases+=("${BLUE}4. Quality:${NC} qa-engineer → security-engineer")
    fi

    # Deployment phase
    if [[ " ${RECOMMENDED_AGENTS[@]} " =~ " deployment-engineer " ]]; then
        workflow_phases+=("${BLUE}5. Deployment:${NC} deployment-engineer")
    fi

    # Display workflow
    for phase in "${workflow_phases[@]}"; do
        echo -e "   $phase"
    done

    if [[ ${#workflow_phases[@]} -eq 0 ]]; then
        echo -e "   ${YELLOW}Standard workflow: frontend-engineer → backend-engineer → qa-engineer${NC}"
    fi
}

# Main agent selection function
select_optimal_agents() {
    local project_dir="$1"
    local tech_stack="$2"
    local business_domain="$3"
    local project_scale="$4"

    init_selector

    # Clear previous recommendations
    AGENT_RECOMMENDATIONS=()
    RECOMMENDED_AGENTS=()

    # Run analysis phases
    analyze_technologies "$tech_stack"
    analyze_business_domain "$business_domain"
    analyze_project_scale "$project_scale"
    apply_baseline_agents
    integrate_ai_recommendations "$project_dir"

    # Generate recommendations
    categorize_recommendations
    generate_workflow_recommendation

    echo -e "\n${CHECK} Agent selection analysis complete!"

    # Return recommended agents for external use
    echo "RECOMMENDED_AGENTS_START"
    for agent in "${RECOMMENDED_AGENTS[@]}"; do
        echo "$agent"
    done
    echo "RECOMMENDED_AGENTS_END"
}

# Execute if run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    if [[ $# -lt 4 ]]; then
        echo "Usage: $0 <project_directory> <tech_stack> <business_domain> <project_scale>"
        echo "Example: $0 /path/to/project react,nodejs ecommerce sme"
        exit 1
    fi

    select_optimal_agents "$1" "$2" "$3" "$4"
fi