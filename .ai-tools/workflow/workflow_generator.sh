#!/bin/bash
#
# Claude Code Framework - Intelligent Project Workflow Generator
# Revolutionary workflow intelligence with AI-powered optimization
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
WIZARD="🧙"
GEAR="⚙️"
ROCKET="🚀"

# Global variables
WORKFLOW_DIR="$(dirname "$(realpath "$0")")"
PROJECT_DIR=""
WORKFLOW_OUTPUT=""
PROJECT_PROFILE=""
SELECTED_WORKFLOW=""

# Initialize workflow generator
init_workflow_generator() {
    echo -e "${WIZARD} ${BOLD}INTELLIGENT PROJECT WORKFLOW GENERATION${NC}"
    echo "================================================================================"
    echo -e "${INFO} Analyzing project characteristics for optimal workflow orchestration..."
    echo
}

# Enhanced project analysis building on existing detection
analyze_project_intelligence() {
    local project_dir="$1"

    echo -e "${BRAIN} ${BOLD}ENHANCED PROJECT ANALYSIS${NC}"
    echo "================================================================================"
    echo -e "${INFO} Building comprehensive project intelligence profile..."

    # Integration with existing technology detection
    local setup_detector="$WORKFLOW_DIR/../setup/project_detector.sh"
    local basic_analysis=""

    if [[ -f "$setup_detector" ]]; then
        echo -e "${CHECK} Integrating with existing technology detection..."
        basic_analysis=$("$setup_detector" "$project_dir" --json 2>/dev/null || echo "{}")
    else
        echo -e "${YELLOW}Warning: Setup detector not found, using fallback analysis${NC}"
        basic_analysis=$(fallback_technology_detection "$project_dir")
    fi

    # Advanced complexity analysis
    echo -e "${INFO} Analyzing project complexity and architecture patterns..."
    local codebase_analysis=$(analyze_codebase_complexity "$project_dir")
    local dependency_analysis=$(analyze_dependency_complexity "$project_dir")
    local architecture_analysis=$(analyze_architecture_patterns "$project_dir")

    # Risk and constraint assessment
    echo -e "${INFO} Assessing development risks and business constraints..."
    local risk_profile=$(assess_project_risks "$project_dir")
    local business_constraints=$(assess_business_requirements "$project_dir")

    # Generate comprehensive project profile
    PROJECT_PROFILE=$(generate_project_profile "$basic_analysis" "$codebase_analysis" "$dependency_analysis" "$architecture_analysis" "$risk_profile" "$business_constraints")

    echo -e "${CHECK} Project intelligence analysis complete!"
    echo
}

# Analyze codebase complexity
analyze_codebase_complexity() {
    local project_dir="$1"
    local file_count=0
    local line_count=0
    local complexity_score=0

    if [[ -d "$project_dir" ]]; then
        # Count files and lines of code
        file_count=$(find "$project_dir" -type f \( -name "*.js" -o -name "*.ts" -o -name "*.jsx" -o -name "*.tsx" -o -name "*.py" -o -name "*.java" -o -name "*.cs" -o -name "*.cpp" -o -name "*.c" \) 2>/dev/null | wc -l)

        if [[ $file_count -gt 0 ]]; then
            line_count=$(find "$project_dir" -type f \( -name "*.js" -o -name "*.ts" -o -name "*.jsx" -o -name "*.tsx" -o -name "*.py" -o -name "*.java" -o -name "*.cs" -o -name "*.cpp" -o -name "*.c" \) -exec wc -l {} + 2>/dev/null | tail -1 | awk '{print $1}' || echo "0")
        fi

        # Calculate complexity score
        if [[ $file_count -lt 50 && $line_count -lt 5000 ]]; then
            complexity_score=1  # Simple
        elif [[ $file_count -lt 200 && $line_count -lt 25000 ]]; then
            complexity_score=2  # Medium
        elif [[ $file_count -lt 500 && $line_count -lt 100000 ]]; then
            complexity_score=3  # Complex
        else
            complexity_score=4  # Very Complex
        fi
    fi

    echo "{\"file_count\":$file_count,\"line_count\":$line_count,\"complexity_score\":$complexity_score}"
}

# Analyze dependency complexity
analyze_dependency_complexity() {
    local project_dir="$1"
    local dependency_score=0
    local package_files=0

    # Check for package management files
    if [[ -f "$project_dir/package.json" ]]; then
        package_files=$((package_files + 1))
        local deps=$(grep -o '"[^"]*"' "$project_dir/package.json" 2>/dev/null | wc -l || echo 0)
        dependency_score=$((dependency_score + deps / 10))
    fi

    if [[ -f "$project_dir/requirements.txt" ]]; then
        package_files=$((package_files + 1))
        local deps=$(wc -l < "$project_dir/requirements.txt" 2>/dev/null || echo 0)
        dependency_score=$((dependency_score + deps / 5))
    fi

    if [[ -f "$project_dir/pom.xml" ]]; then
        package_files=$((package_files + 1))
        local deps=$(grep -c "<dependency>" "$project_dir/pom.xml" 2>/dev/null || echo 0)
        dependency_score=$((dependency_score + deps / 3))
    fi

    # Normalize dependency score
    if [[ $dependency_score -lt 5 ]]; then
        dependency_score=1  # Low
    elif [[ $dependency_score -lt 15 ]]; then
        dependency_score=2  # Medium
    elif [[ $dependency_score -lt 30 ]]; then
        dependency_score=3  # High
    else
        dependency_score=4  # Very High
    fi

    echo "{\"package_files\":$package_files,\"dependency_score\":$dependency_score}"
}

# Analyze architecture patterns
analyze_architecture_patterns() {
    local project_dir="$1"
    local patterns=()
    local architecture_complexity=0

    # Detect common architecture patterns
    if [[ -d "$project_dir/src/components" ]] || [[ -d "$project_dir/components" ]]; then
        patterns+=("\"component_based\"")
        architecture_complexity=$((architecture_complexity + 1))
    fi

    if [[ -f "$project_dir/docker-compose.yml" ]] || [[ -f "$project_dir/Dockerfile" ]]; then
        patterns+=("\"containerized\"")
        architecture_complexity=$((architecture_complexity + 2))
    fi

    if [[ -d "$project_dir/microservices" ]] || grep -q "microservice" "$project_dir"/**/*.md 2>/dev/null; then
        patterns+=("\"microservices\"")
        architecture_complexity=$((architecture_complexity + 3))
    fi

    if [[ -d "$project_dir/api" ]] || [[ -d "$project_dir/src/api" ]] || [[ -f "$project_dir/openapi.yaml" ]]; then
        patterns+=("\"api_driven\"")
        architecture_complexity=$((architecture_complexity + 1))
    fi

    local patterns_json=$(IFS=','; echo "[${patterns[*]}]")
    echo "{\"patterns\":$patterns_json,\"architecture_complexity\":$architecture_complexity}"
}

# Assess project risks
assess_project_risks() {
    local project_dir="$1"
    local risk_factors=()
    local risk_score=0

    # Legacy code indicators
    if find "$project_dir" -name "*.js" -exec grep -l "var " {} \; 2>/dev/null | head -1 > /dev/null; then
        risk_factors+=("\"legacy_javascript\"")
        risk_score=$((risk_score + 2))
    fi

    # Security risk indicators
    if [[ -f "$project_dir/package.json" ]] && grep -q "\"jquery\"" "$project_dir/package.json" 2>/dev/null; then
        risk_factors+=("\"jquery_dependency\"")
        risk_score=$((risk_score + 1))
    fi

    # Compliance indicators
    if grep -r -i "gdpr\|hipaa\|sox\|pci" "$project_dir" 2>/dev/null | head -1 > /dev/null; then
        risk_factors+=("\"compliance_requirements\"")
        risk_score=$((risk_score + 3))
    fi

    # No tests indicator
    if ! find "$project_dir" -name "*test*" -type f 2>/dev/null | head -1 > /dev/null; then
        risk_factors+=("\"no_tests\"")
        risk_score=$((risk_score + 3))
    fi

    local risk_factors_json=$(IFS=','; echo "[${risk_factors[*]}]")
    echo "{\"risk_factors\":$risk_factors_json,\"risk_score\":$risk_score}"
}

# Assess business requirements
assess_business_requirements() {
    local project_dir="$1"
    local business_type="general"
    local scale="sme"
    local priority="standard"

    # Business domain detection
    if grep -r -i "ecommerce\|shop\|cart\|payment" "$project_dir" 2>/dev/null | head -1 > /dev/null; then
        business_type="ecommerce"
    elif grep -r -i "fintech\|banking\|finance\|trading" "$project_dir" 2>/dev/null | head -1 > /dev/null; then
        business_type="fintech"
    elif grep -r -i "health\|medical\|patient\|clinical" "$project_dir" 2>/dev/null | head -1 > /dev/null; then
        business_type="healthcare"
    fi

    # Scale detection
    local file_count=$(find "$project_dir" -type f -name "*.js" -o -name "*.ts" -o -name "*.py" 2>/dev/null | wc -l)
    if [[ $file_count -gt 500 ]]; then
        scale="enterprise"
    elif [[ $file_count -lt 50 ]]; then
        scale="startup"
    fi

    # Priority detection
    if [[ -f "$project_dir/README.md" ]] && grep -i -E "urgent|asap|deadline|critical" "$project_dir/README.md" 2>/dev/null | head -1 > /dev/null; then
        priority="high"
    fi

    echo "{\"business_type\":\"$business_type\",\"scale\":\"$scale\",\"priority\":\"$priority\"}"
}

# Generate comprehensive project profile
generate_project_profile() {
    local basic_analysis="$1"
    local codebase_analysis="$2"
    local dependency_analysis="$3"
    local architecture_analysis="$4"
    local risk_profile="$5"
    local business_constraints="$6"

    # Combine all analyses into comprehensive profile
    cat <<EOF
{
    "basic_analysis": $basic_analysis,
    "codebase_analysis": $codebase_analysis,
    "dependency_analysis": $dependency_analysis,
    "architecture_analysis": $architecture_analysis,
    "risk_profile": $risk_profile,
    "business_constraints": $business_constraints,
    "generated_timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
EOF
}

# Fallback technology detection
fallback_technology_detection() {
    local project_dir="$1"
    local technologies=()

    if [[ -f "$project_dir/package.json" ]]; then
        technologies+=("\"nodejs\"")
        if grep -q "\"react\"" "$project_dir/package.json" 2>/dev/null; then
            technologies+=("\"react\"")
        fi
        if grep -q "\"angular\"" "$project_dir/package.json" 2>/dev/null; then
            technologies+=("\"angular\"")
        fi
    fi

    if [[ -f "$project_dir/requirements.txt" ]] || find "$project_dir" -name "*.py" 2>/dev/null | head -1 > /dev/null; then
        technologies+=("\"python\"")
    fi

    local tech_json=$(IFS=','; echo "[${technologies[*]}]")
    echo "{\"technologies\":$tech_json,\"confidence\":0.7}"
}

# Select optimal workflow template
select_optimal_workflow() {
    echo -e "${TARGET} ${BOLD}WORKFLOW INTELLIGENCE GENERATION${NC}"
    echo "================================================================================"
    echo -e "${INFO} Analyzing project profile for optimal workflow selection..."

    # Parse project profile for key characteristics
    local business_type=$(echo "$PROJECT_PROFILE" | grep -o '"business_type":"[^"]*"' | cut -d'"' -f4)
    local scale=$(echo "$PROJECT_PROFILE" | grep -o '"scale":"[^"]*"' | cut -d'"' -f4)
    local complexity_score=$(echo "$PROJECT_PROFILE" | grep -o '"complexity_score":[0-9]*' | cut -d':' -f2)
    local risk_score=$(echo "$PROJECT_PROFILE" | grep -o '"risk_score":[0-9]*' | cut -d':' -f2)

    # Workflow selection logic
    local workflow_type="standard"
    local methodology="agile"
    local security_focus="standard"

    # Determine workflow type based on complexity
    if [[ ${complexity_score:-1} -ge 3 ]]; then
        workflow_type="enterprise"
        methodology="phased"
    elif [[ ${complexity_score:-1} -le 1 ]]; then
        workflow_type="rapid"
        methodology="iterative"
    fi

    # Adjust for business domain
    case "$business_type" in
        "fintech"|"healthcare")
            security_focus="high"
            methodology="compliance-first"
            ;;
        "ecommerce")
            workflow_type="market-driven"
            methodology="mvp-first"
            ;;
    esac

    # Adjust for risk profile
    if [[ ${risk_score:-0} -ge 5 ]]; then
        security_focus="critical"
        methodology="risk-managed"
    fi

    # Generate workflow recommendation
    SELECTED_WORKFLOW=$(cat <<EOF
{
    "workflow_type": "$workflow_type",
    "methodology": "$methodology",
    "security_focus": "$security_focus",
    "business_type": "$business_type",
    "scale": "$scale",
    "complexity_score": ${complexity_score:-1},
    "risk_score": ${risk_score:-0}
}
EOF
)

    echo -e "${CHECK} Optimal workflow profile generated!"
    echo -e "${INFO} Workflow Type: ${CYAN}$workflow_type${NC}"
    echo -e "${INFO} Methodology: ${CYAN}$methodology${NC}"
    echo -e "${INFO} Security Focus: ${CYAN}$security_focus${NC}"
    echo
}

# Generate agent coordination plan
generate_agent_coordination() {
    echo -e "${GEAR} ${BOLD}AGENT COORDINATION OPTIMIZATION${NC}"
    echo "================================================================================"
    echo -e "${INFO} Optimizing agent sequences and coordination patterns..."

    # Extract workflow characteristics
    local workflow_type=$(echo "$SELECTED_WORKFLOW" | grep -o '"workflow_type":"[^"]*"' | cut -d'"' -f4)
    local methodology=$(echo "$SELECTED_WORKFLOW" | grep -o '"methodology":"[^"]*"' | cut -d'"' -f4)
    local security_focus=$(echo "$SELECTED_WORKFLOW" | grep -o '"security_focus":"[^"]*"' | cut -d'"' -f4)
    local scale=$(echo "$SELECTED_WORKFLOW" | grep -o '"scale":"[^"]*"' | cut -d'"' -f4)

    # Generate agent sequences based on workflow type
    local agent_sequences=""
    local quality_gates=""
    local milestones=""

    case "$workflow_type" in
        "rapid")
            agent_sequences=$(generate_rapid_workflow_agents "$methodology" "$scale")
            quality_gates=$(generate_rapid_quality_gates "$security_focus")
            milestones=$(generate_rapid_milestones)
            ;;
        "enterprise")
            agent_sequences=$(generate_enterprise_workflow_agents "$methodology" "$scale")
            quality_gates=$(generate_enterprise_quality_gates "$security_focus")
            milestones=$(generate_enterprise_milestones)
            ;;
        "market-driven")
            agent_sequences=$(generate_market_driven_agents "$methodology" "$scale")
            quality_gates=$(generate_market_driven_quality_gates "$security_focus")
            milestones=$(generate_market_driven_milestones)
            ;;
        *)
            agent_sequences=$(generate_standard_workflow_agents "$methodology" "$scale")
            quality_gates=$(generate_standard_quality_gates "$security_focus")
            milestones=$(generate_standard_milestones)
            ;;
    esac

    echo -e "${CHECK} Agent coordination plan optimized!"
    echo -e "${INFO} Primary Agents: ${CYAN}$(echo "$agent_sequences" | grep -o 'primary.*' | head -1)${NC}"
    echo -e "${INFO} Quality Gates: ${CYAN}$(echo "$quality_gates" | wc -l) checkpoints${NC}"
    echo -e "${INFO} Milestones: ${CYAN}$(echo "$milestones" | wc -l) deliverables${NC}"
    echo

    # Store coordination plan
    cat > /tmp/coordination_plan.json <<EOF
{
    "agent_sequences": $agent_sequences,
    "quality_gates": $quality_gates,
    "milestones": $milestones,
    "workflow_type": "$workflow_type",
    "methodology": "$methodology"
}
EOF
}

# Generate standard workflow agents
generate_standard_workflow_agents() {
    local methodology="$1"
    local scale="$2"

    cat <<EOF
{
    "phases": [
        {
            "phase": "Planning & Analysis",
            "duration": "1-2 weeks",
            "agents": ["business-analyst", "product-manager"],
            "parallel": false,
            "handoff_to": "architecture"
        },
        {
            "phase": "Architecture & Design",
            "duration": "1 week",
            "agents": ["software-architect", "ux-designer"],
            "parallel": true,
            "handoff_to": "development"
        },
        {
            "phase": "Core Development",
            "duration": "3-4 weeks",
            "agents": ["frontend-engineer", "backend-engineer", "api-engineer"],
            "parallel": true,
            "handoff_to": "quality"
        },
        {
            "phase": "Quality & Security",
            "duration": "1-2 weeks",
            "agents": ["qa-engineer", "security-engineer"],
            "parallel": false,
            "handoff_to": "deployment"
        },
        {
            "phase": "Deployment & Launch",
            "duration": "1 week",
            "agents": ["deployment-engineer"],
            "parallel": false,
            "handoff_to": "complete"
        }
    ]
}
EOF
}

# Generate standard quality gates
generate_standard_quality_gates() {
    local security_focus="$1"

    cat <<EOF
[
    {
        "gate": "Requirements Validation",
        "phase": "Planning & Analysis",
        "criteria": ["Stakeholder approval", "Business requirements documented", "Success metrics defined"],
        "blocking": true
    },
    {
        "gate": "Architecture Review",
        "phase": "Architecture & Design",
        "criteria": ["Technical architecture approved", "Security considerations documented", "Scalability validated"],
        "blocking": true
    },
    {
        "gate": "Code Quality Check",
        "phase": "Core Development",
        "criteria": ["Code review completed", "Unit tests passing", "Documentation updated"],
        "blocking": false
    },
    {
        "gate": "Security & Performance Validation",
        "phase": "Quality & Security",
        "criteria": ["Security scan passed", "Performance benchmarks met", "Integration tests successful"],
        "blocking": true
    },
    {
        "gate": "Production Readiness",
        "phase": "Deployment & Launch",
        "criteria": ["Deployment validated", "Monitoring configured", "Rollback plan verified"],
        "blocking": true
    }
]
EOF
}

# Generate standard milestones
generate_standard_milestones() {
    cat <<EOF
[
    {
        "milestone": "Project Kickoff",
        "deliverables": ["Project charter", "Team assignments", "Communication plan"],
        "success_criteria": "All stakeholders aligned and project officially started"
    },
    {
        "milestone": "Architecture Baseline",
        "deliverables": ["Technical architecture document", "UI/UX mockups", "API specifications"],
        "success_criteria": "Development can begin with clear technical direction"
    },
    {
        "milestone": "MVP Delivery",
        "deliverables": ["Core functionality implemented", "Basic testing completed", "Documentation updated"],
        "success_criteria": "Minimum viable product ready for stakeholder review"
    },
    {
        "milestone": "Quality Gate Passed",
        "deliverables": ["Full test suite passing", "Security validation completed", "Performance benchmarks met"],
        "success_criteria": "Application ready for production deployment"
    },
    {
        "milestone": "Production Launch",
        "deliverables": ["Application deployed", "Monitoring active", "Support procedures documented"],
        "success_criteria": "Application successfully running in production environment"
    }
]
EOF
}

# Generate rapid workflow variants (placeholder functions)
generate_rapid_workflow_agents() { generate_standard_workflow_agents "$@"; }
generate_rapid_quality_gates() { generate_standard_quality_gates "$@"; }
generate_rapid_milestones() { generate_standard_milestones; }

# Generate enterprise workflow variants (placeholder functions)
generate_enterprise_workflow_agents() { generate_standard_workflow_agents "$@"; }
generate_enterprise_quality_gates() { generate_standard_quality_gates "$@"; }
generate_enterprise_milestones() { generate_standard_milestones; }

# Generate market-driven workflow variants (placeholder functions)
generate_market_driven_agents() { generate_standard_workflow_agents "$@"; }
generate_market_driven_quality_gates() { generate_standard_quality_gates "$@"; }
generate_market_driven_milestones() { generate_standard_milestones; }

# Generate workflow documentation
generate_workflow_documentation() {
    echo -e "${ROCKET} ${BOLD}WORKFLOW DOCUMENTATION GENERATION${NC}"
    echo "================================================================================"
    echo -e "${INFO} Creating comprehensive workflow documentation..."

    local output_dir="${PROJECT_DIR}/workflow_generated"
    mkdir -p "$output_dir"

    # Generate main workflow guide
    cat > "$output_dir/PROJECT_WORKFLOW.md" <<EOF
# Intelligent Project Workflow

**Generated**: $(date)
**Project**: $(basename "$PROJECT_DIR")
**Workflow Type**: $(echo "$SELECTED_WORKFLOW" | grep -o '"workflow_type":"[^"]*"' | cut -d'"' -f4)

## Project Profile

$(echo "$PROJECT_PROFILE" | jq . 2>/dev/null || echo "Project profile data")

## Recommended Workflow

$(echo "$SELECTED_WORKFLOW" | jq . 2>/dev/null || echo "Workflow configuration")

## Agent Coordination Plan

$(cat /tmp/coordination_plan.json 2>/dev/null | jq . || echo "Agent coordination details")

## Implementation Guidelines

### Phase Execution
1. Follow the defined phase sequence
2. Complete quality gates before progression
3. Maintain agent coordination protocols
4. Monitor milestone achievement

### Success Criteria
- All quality gates passed
- Milestone deliverables completed
- Agent handoffs executed successfully
- Project objectives achieved

---
*Generated by Claude Code Framework - Intelligent Workflow Generator*
EOF

    # Generate agent sequences documentation
    cat > "$output_dir/AGENT_SEQUENCES.md" <<EOF
# Agent Coordination Sequences

**Generated**: $(date)

## Agent Execution Plan

$(cat /tmp/coordination_plan.json 2>/dev/null | jq '.agent_sequences // {}' || echo "Agent sequences will be detailed here")

## Handoff Protocols

### Standard Handoff Process
1. Completing agent creates handoff summary
2. Quality gate validation (if applicable)
3. Next agent receives context and begins work
4. Progress tracking updated

### Agent Dependencies
- Sequential phases must complete before next phase begins
- Parallel agents coordinate through shared TodoWrite workflow
- Quality gates serve as synchronization points

---
*Agent coordination optimized by Intelligent Workflow Generator*
EOF

    # Generate quality gates documentation
    cat > "$output_dir/QUALITY_GATES.md" <<EOF
# Quality Gates and Validation

**Generated**: $(date)

## Quality Gate Framework

$(cat /tmp/coordination_plan.json 2>/dev/null | jq '.quality_gates // []' || echo "Quality gates will be detailed here")

## Validation Procedures

### Gate Execution Process
1. Automated validation where possible
2. Manual review for subjective criteria
3. Stakeholder approval for business decisions
4. Documentation of gate passage

### Quality Standards
- All blocking gates must pass
- Non-blocking gates logged for continuous improvement
- Quality metrics tracked throughout project

---
*Quality framework generated by Intelligent Workflow Generator*
EOF

    # Generate progress monitoring documentation
    cat > "$output_dir/PROGRESS_MONITORING.md" <<EOF
# Progress Monitoring and Metrics

**Generated**: $(date)

## Milestone Tracking

$(cat /tmp/coordination_plan.json 2>/dev/null | jq '.milestones // []' || echo "Milestones will be detailed here")

## Progress Metrics

### Key Performance Indicators
- Phase completion percentage
- Quality gate pass rate
- Agent coordination efficiency
- Milestone delivery accuracy

### Monitoring Process
1. Daily progress updates via TodoWrite
2. Weekly milestone assessment
3. Quality gate tracking
4. Agent performance monitoring

---
*Progress monitoring framework by Intelligent Workflow Generator*
EOF

    WORKFLOW_OUTPUT="$output_dir"
    echo -e "${CHECK} Workflow documentation generated!"
    echo -e "${INFO} Output Directory: ${CYAN}$output_dir${NC}"
    echo
}

# Display workflow summary
show_workflow_summary() {
    echo -e "${ROCKET} ${BOLD}INTELLIGENT WORKFLOW GENERATION COMPLETE${NC}"
    echo "================================================================================"
    echo -e "${TARGET} ${BOLD}Generated Workflow Summary:${NC}"

    local workflow_type=$(echo "$SELECTED_WORKFLOW" | grep -o '"workflow_type":"[^"]*"' | cut -d'"' -f4)
    local methodology=$(echo "$SELECTED_WORKFLOW" | grep -o '"methodology":"[^"]*"' | cut -d'"' -f4)
    local scale=$(echo "$SELECTED_WORKFLOW" | grep -o '"scale":"[^"]*"' | cut -d'"' -f4)

    echo -e "   ${CHECK} Workflow Type: ${GREEN}$workflow_type${NC}"
    echo -e "   ${CHECK} Methodology: ${GREEN}$methodology${NC}"
    echo -e "   ${CHECK} Project Scale: ${GREEN}$scale${NC}"
    echo -e "   ${CHECK} Documentation: ${GREEN}$WORKFLOW_OUTPUT${NC}"
    echo
    echo -e "${INFO} ${BOLD}Next Steps:${NC}"
    echo -e "   1. Review generated workflow documentation"
    echo -e "   2. Customize agent sequences if needed"
    echo -e "   3. Begin development following workflow phases"
    echo -e "   4. Monitor progress through quality gates"
    echo
    echo -e "${CHECK} Intelligent workflow generation completed in $(date)!"
}

# Main workflow generation function
generate_project_workflow() {
    local project_dir="$1"

    if [[ ! -d "$project_dir" ]]; then
        echo -e "${YELLOW}Error: Project directory not found: $project_dir${NC}"
        exit 1
    fi

    PROJECT_DIR="$project_dir"

    init_workflow_generator
    analyze_project_intelligence "$project_dir"
    select_optimal_workflow
    generate_agent_coordination
    generate_workflow_documentation
    show_workflow_summary

    # Clean up temporary files
    rm -f /tmp/coordination_plan.json
}

# Execute if run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    if [[ $# -lt 1 ]]; then
        echo "Usage: $0 <project_directory>"
        echo "Example: $0 /path/to/project"
        exit 1
    fi

    generate_project_workflow "$1"
fi