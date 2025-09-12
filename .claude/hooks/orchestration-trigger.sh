#!/bin/bash

# Orchestration Trigger Engine
# Automatically detects project context and triggers appropriate orchestration scenario
# Provides intelligent scenario selection based on project characteristics

echo "🎯 Orchestration Trigger Engine - Starting analysis..."

# Ensure work directory exists
mkdir -p work/orchestration

# Configuration and parameters
PROJECT_ROOT="${1:-$(pwd)}"
FORCE_SCENARIO="${2:-}"  # Optional: force specific scenario
ANALYSIS_MODE="${3:-auto}"  # auto, manual, interactive

TRIGGER_LOG="work/orchestration/trigger-analysis-$(date +%Y%m%d_%H%M%S).log"

cat > "$TRIGGER_LOG" << EOF
# Orchestration Trigger Analysis

**Started:** $(date)
**Project Root:** $PROJECT_ROOT
**Forced Scenario:** ${FORCE_SCENARIO:-"None - Auto-detection"}
**Analysis Mode:** $ANALYSIS_MODE

## Project Analysis Results

EOF

echo "$(date): Orchestration trigger analysis started" >> "$TRIGGER_LOG"

# Function to analyze project characteristics
analyze_project_context() {
    local analysis_score=0
    local security_indicators=0
    local data_indicators=0
    local mvp_indicators=0
    local enterprise_indicators=0
    
    echo "🔍 Analyzing project context and characteristics..."
    echo "### Project Context Analysis" >> "$TRIGGER_LOG"
    
    # Check for security-related indicators
    if [[ -f "package.json" ]] && grep -q -i "security\|auth\|jwt\|passport\|bcrypt" "package.json"; then
        security_indicators=$((security_indicators + 2))
        echo "- 🔒 Security dependencies detected in package.json" >> "$TRIGGER_LOG"
    fi
    
    if find "$PROJECT_ROOT" -name "*.md" -exec grep -l -i "gdpr\|sox\|hipaa\|compliance\|security" {} \; | head -1 > /dev/null; then
        security_indicators=$((security_indicators + 3))
        echo "- 📋 Compliance/security documentation found" >> "$TRIGGER_LOG"
    fi
    
    if [[ -f "CLAUDE.md" ]] && grep -q -i "fintech\|healthcare\|banking\|finance\|regulated" "CLAUDE.md"; then
        security_indicators=$((security_indicators + 4))
        enterprise_indicators=$((enterprise_indicators + 2))
        echo "- 🏛️ Regulated industry indicators in CLAUDE.md" >> "$TRIGGER_LOG"
    fi
    
    # Check for data-related indicators  
    if [[ -f "package.json" ]] && grep -q -i "analytics\|dashboard\|chart\|d3\|plotly\|data\|ml\|ai" "package.json"; then
        data_indicators=$((data_indicators + 3))
        echo "- 📊 Data/analytics dependencies detected" >> "$TRIGGER_LOG"
    fi
    
    if find "$PROJECT_ROOT" -name "*.py" -exec grep -l "pandas\|numpy\|sklearn\|tensorflow\|pytorch" {} \; | head -1 > /dev/null; then
        data_indicators=$((data_indicators + 4))
        echo "- 🤖 Machine learning/data science libraries found" >> "$TRIGGER_LOG"
    fi
    
    if [[ -d "data" ]] || [[ -d "datasets" ]] || [[ -d "analytics" ]] || [[ -d "reports" ]]; then
        data_indicators=$((data_indicators + 2))
        echo "- 📈 Data-related directory structure found" >> "$TRIGGER_LOG"
    fi
    
    # Check for MVP/startup indicators
    if [[ -f "CLAUDE.md" ]] && grep -q -i "mvp\|prototype\|startup\|proof.*concept\|poc" "CLAUDE.md"; then
        mvp_indicators=$((mvp_indicators + 4))
        echo "- 🚀 MVP/startup indicators in CLAUDE.md" >> "$TRIGGER_LOG"
    fi
    
    if [[ -f "package.json" ]] && jq -e '.version | test("^0\\.")' package.json > /dev/null 2>&1; then
        mvp_indicators=$((mvp_indicators + 2))
        echo "- 🆕 Early version number detected (0.x.x)" >> "$TRIGGER_LOG"
    fi
    
    # Check for enterprise indicators
    if [[ -f "CLAUDE.md" ]] && grep -q -i "enterprise\|corporation\|large.*scale\|production" "CLAUDE.md"; then
        enterprise_indicators=$((enterprise_indicators + 3))
        echo "- 🏢 Enterprise scale indicators in CLAUDE.md" >> "$TRIGGER_LOG"
    fi
    
    if [[ -f "docker-compose.yml" ]] || [[ -f "Dockerfile" ]] || [[ -d ".github/workflows" ]]; then
        enterprise_indicators=$((enterprise_indicators + 2))
        echo "- 🐳 Enterprise deployment infrastructure found" >> "$TRIGGER_LOG"
    fi
    
    # Calculate scores and determine recommendation
    echo "### Analysis Scoring" >> "$TRIGGER_LOG"
    echo "- Security Indicators: $security_indicators" >> "$TRIGGER_LOG"
    echo "- Data Indicators: $data_indicators" >> "$TRIGGER_LOG"
    echo "- MVP Indicators: $mvp_indicators" >> "$TRIGGER_LOG"
    echo "- Enterprise Indicators: $enterprise_indicators" >> "$TRIGGER_LOG"
    
    # Scenario recommendation logic
    local recommended_scenario=""
    local confidence="medium"
    
    if [[ $security_indicators -ge 6 ]] || [[ $enterprise_indicators -ge 4 ]]; then
        recommended_scenario="enterprise-security-first"
        if [[ $security_indicators -ge 8 ]]; then
            confidence="high"
        fi
    elif [[ $data_indicators -ge 6 ]]; then
        recommended_scenario="data-driven"
        if [[ $data_indicators -ge 8 ]]; then
            confidence="high"
        fi
    elif [[ $mvp_indicators -ge 4 ]] || [[ $security_indicators -le 2 && $data_indicators -le 2 ]]; then
        recommended_scenario="rapid-mvp"
        if [[ $mvp_indicators -ge 6 ]]; then
            confidence="high"
        fi
    else
        recommended_scenario="rapid-mvp"  # Default fallback
        confidence="low"
    fi
    
    echo "### Recommendation" >> "$TRIGGER_LOG"
    echo "- **Recommended Scenario:** $recommended_scenario" >> "$TRIGGER_LOG"
    echo "- **Confidence Level:** $confidence" >> "$TRIGGER_LOG"
    echo ""
    
    echo "$recommended_scenario:$confidence"
}

# Function to get scenario parameters based on analysis
get_scenario_parameters() {
    local scenario="$1"
    local confidence="$2"
    
    case "$scenario" in
        "rapid-mvp")
            if [[ -f "CLAUDE.md" ]] && grep -q -i "startup" "CLAUDE.md"; then
                echo "startup minimal"
            elif [[ -f "CLAUDE.md" ]] && grep -q -i "prototype\|poc" "CLAUDE.md"; then
                echo "prototype minimal"
            else
                echo "startup extended"
            fi
            ;;
        "enterprise-security-first")
            local compliance="gdpr"
            local security_level="high"
            
            if [[ -f "CLAUDE.md" ]] && grep -q -i "sox" "CLAUDE.md"; then
                compliance="sox"
            elif [[ -f "CLAUDE.md" ]] && grep -q -i "hipaa" "CLAUDE.md"; then
                compliance="hipaa"
            elif [[ -f "CLAUDE.md" ]] && grep -q -i "pci" "CLAUDE.md"; then
                compliance="pci"
            fi
            
            if [[ "$confidence" == "high" ]]; then
                security_level="critical"
            fi
            
            echo "$compliance $security_level enterprise"
            ;;
        "data-driven")
            local data_type="analytics"
            local scale="enterprise"
            local analytics="advanced"
            
            if find "$PROJECT_ROOT" -name "*.py" -exec grep -l "sklearn\|tensorflow\|pytorch" {} \; | head -1 > /dev/null; then
                data_type="ml"
                analytics="ai-ml"
            elif [[ -f "package.json" ]] && grep -q -i "realtime\|streaming\|socket" "package.json"; then
                data_type="realtime"
                analytics="advanced"
            elif find "$PROJECT_ROOT" -name "*.md" -exec grep -l -i "report\|dashboard" {} \; | head -1 > /dev/null; then
                data_type="reporting"
                analytics="basic"
            fi
            
            echo "$data_type $scale $analytics"
            ;;
        *)
            echo "startup minimal"  # Safe default
            ;;
    esac
}

# Function to execute orchestration with proper parameters
execute_orchestration() {
    local scenario="$1"
    local parameters="$2"
    
    local script_path=".claude/hooks/orchestration/${scenario}-scenario.sh"
    
    if [[ ! -f "$script_path" ]]; then
        echo "❌ Orchestration scenario script not found: $script_path"
        echo "$(date): ERROR - Script not found: $script_path" >> "$TRIGGER_LOG"
        return 1
    fi
    
    echo "🚀 Executing orchestration: $scenario with parameters: $parameters"
    echo "$(date): Executing $scenario with parameters: $parameters" >> "$TRIGGER_LOG"
    
    # Execute the orchestration scenario
    bash "$script_path" $parameters
    local exit_code=$?
    
    echo "$(date): Orchestration completed with exit code: $exit_code" >> "$TRIGGER_LOG"
    
    return $exit_code
}

# Main trigger logic
main() {
    echo "🎯 Orchestration Trigger Engine Analysis"
    
    # If scenario is forced, skip analysis
    if [[ -n "$FORCE_SCENARIO" ]]; then
        echo "🎭 Forced scenario mode: $FORCE_SCENARIO"
        echo "$(date): Forced scenario execution: $FORCE_SCENARIO" >> "$TRIGGER_LOG"
        
        case "$FORCE_SCENARIO" in
            "mvp"|"rapid-mvp")
                execute_orchestration "rapid-mvp" "startup minimal"
                ;;
            "security"|"enterprise-security-first"|"enterprise")
                execute_orchestration "enterprise-security-first" "gdpr high enterprise"
                ;;
            "data"|"data-driven"|"analytics")
                execute_orchestration "data-driven" "analytics enterprise advanced"
                ;;
            *)
                echo "❌ Unknown forced scenario: $FORCE_SCENARIO"
                echo "Available scenarios: mvp, security, data"
                exit 1
                ;;
        esac
        return $?
    fi
    
    # Automatic analysis and recommendation
    local analysis_result
    analysis_result=$(analyze_project_context)
    
    local scenario
    local confidence
    IFS=':' read -r scenario confidence <<< "$analysis_result"
    
    echo "📊 Analysis Complete:"
    echo "   Recommended Scenario: $scenario"
    echo "   Confidence Level: $confidence"
    
    # Get appropriate parameters for the scenario
    local parameters
    parameters=$(get_scenario_parameters "$scenario" "$confidence")
    
    echo "   Parameters: $parameters"
    
    # Interactive mode - ask for confirmation
    if [[ "$ANALYSIS_MODE" == "interactive" ]]; then
        echo ""
        echo "🤔 Recommended orchestration scenario: $scenario"
        echo "   Parameters: $parameters"
        echo "   Confidence: $confidence"
        echo ""
        read -p "Proceed with this scenario? (y/n/custom): " -n 1 -r
        echo ""
        
        case $REPLY in
            [Yy])
                echo "✅ Proceeding with recommended scenario"
                ;;
            [Nn])
                echo "🛑 Orchestration cancelled by user"
                exit 0
                ;;
            [Cc])
                echo "Available scenarios: rapid-mvp, enterprise-security-first, data-driven"
                read -p "Enter custom scenario: " custom_scenario
                read -p "Enter parameters: " custom_parameters
                scenario="$custom_scenario"
                parameters="$custom_parameters"
                ;;
            *)
                echo "❌ Invalid response. Exiting."
                exit 1
                ;;
        esac
    fi
    
    # Execute the orchestration
    execute_orchestration "$scenario" "$parameters"
    local orchestration_result=$?
    
    # Generate trigger summary report
    local trigger_report="work/orchestration/trigger-report-$(date +%Y%m%d_%H%M%S).md"
    
    cat > "$trigger_report" << EOF
# Orchestration Trigger Report

**Generated:** $(date)
**Project Root:** $PROJECT_ROOT
**Analysis Mode:** $ANALYSIS_MODE

## Analysis Summary

### Scenario Selection
- **Recommended Scenario:** $scenario
- **Confidence Level:** $confidence
- **Parameters Used:** $parameters
- **Execution Result:** $(if [[ $orchestration_result -eq 0 ]]; then echo "✅ Successful"; else echo "❌ Failed (Exit Code: $orchestration_result)"; fi)

### Decision Factors

The orchestration trigger engine analyzed the following project characteristics:

1. **Security Requirements:** Detected compliance frameworks, security dependencies, and regulated industry indicators
2. **Data Processing Needs:** Identified analytics libraries, data directories, and visualization requirements
3. **Project Maturity:** Assessed version numbers, documentation maturity, and scale indicators
4. **Enterprise Features:** Found deployment infrastructure, enterprise patterns, and scale indicators

### Automated Trigger Benefits

- ⚡ **Reduced Setup Time:** Automatic scenario selection eliminates manual configuration
- 🎯 **Improved Accuracy:** Context-aware analysis ensures optimal workflow selection
- 🔄 **Consistent Execution:** Standardized trigger logic ensures repeatable results
- 📊 **Data-Driven Decisions:** Objective analysis reduces subjective scenario selection bias

### Next Steps

1. **Review Generated Reports:** Check orchestration reports in \`work/orchestration/\` directory
2. **Validate Deliverables:** Ensure all agent outputs meet project requirements
3. **Iterate as Needed:** Use insights for subsequent development iterations
4. **Optimize Triggers:** Provide feedback to improve future automatic selections

## Trigger Configuration Recommendations

### For Future Projects

Based on this analysis, consider:

$(case "$scenario" in
    "rapid-mvp")
        echo "- **MVP Projects:** Use explicit MVP indicators in CLAUDE.md for accurate detection"
        echo "- **Speed Optimization:** Consider parallel agent execution for faster delivery"
        echo "- **Quality Balance:** Implement essential quality gates without over-engineering"
        ;;
    "enterprise-security-first")
        echo "- **Compliance Projects:** Clearly document regulatory requirements in CLAUDE.md"
        echo "- **Security Integration:** Implement security-by-design from project inception"
        echo "- **Enterprise Scale:** Plan for enterprise-grade infrastructure and processes"
        ;;
    "data-driven")
        echo "- **Data Projects:** Document data sources and analytics requirements clearly"
        echo "- **Performance Planning:** Consider data processing and storage requirements early"
        echo "- **User Experience:** Plan for data visualization and user interaction patterns"
        ;;
esac)

### Trigger Optimization

- **Documentation:** Ensure CLAUDE.md contains clear project indicators
- **Dependencies:** Use descriptive package names that reflect project purpose
- **Structure:** Organize directories to reflect project focus areas
- **Configuration:** Add project metadata to improve automatic detection

EOF
    
    echo "📊 Trigger analysis report: $trigger_report"
    echo "📄 Detailed analysis log: $TRIGGER_LOG"
    
    # Log the trigger completion
    echo "$(date): Orchestration trigger completed - Scenario: $scenario, Result: $orchestration_result" >> work/orchestration-activity.log
    
    if [[ $orchestration_result -eq 0 ]]; then
        echo "🎉 Orchestration trigger completed successfully!"
    else
        echo "⚠️ Orchestration encountered issues - check reports for details"
    fi
    
    exit $orchestration_result
}

# Execute main function
main "$@"