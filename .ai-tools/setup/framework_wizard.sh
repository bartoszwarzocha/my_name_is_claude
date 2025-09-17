#!/bin/bash

# =============================================================================
# INTERACTIVE FRAMEWORK SETUP WIZARD v1.0.0
# Claude Code Multi-Agent Framework - Zero-Configuration Project Setup
# =============================================================================

set -e

# =============================================================================
# CORE CONFIGURATION
# =============================================================================

readonly SCRIPT_VERSION="1.0.0"
readonly FRAMEWORK_VERSION="2.2.0"
readonly WIZARD_NAME="Framework Setup Wizard"

# Paths and directories
readonly PROJECT_DIR="$(pwd)"
readonly PROJECT_NAME="$(basename "$PROJECT_DIR")"
readonly FRAMEWORK_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
readonly SETUP_DIR="$FRAMEWORK_ROOT/.ai-tools/setup"
readonly TEMPLATES_DIR="$SETUP_DIR/templates"
readonly AI_CORE_DIR="$FRAMEWORK_ROOT/.ai-tools/core"

# Target files
readonly TARGET_CLAUDE_MD="$PROJECT_DIR/CLAUDE.md"
readonly TARGET_GITIGNORE="$PROJECT_DIR/.gitignore"
readonly TARGET_README="$PROJECT_DIR/README.md"

# Colors and formatting
readonly COLOR_RED=$(tput setaf 1)
readonly COLOR_GREEN=$(tput setaf 2)
readonly COLOR_YELLOW=$(tput setaf 3)
readonly COLOR_BLUE=$(tput setaf 4)
readonly COLOR_MAGENTA=$(tput setaf 5)
readonly COLOR_CYAN=$(tput setaf 6)
readonly COLOR_WHITE=$(tput setaf 7)
readonly COLOR_BOLD=$(tput bold)
readonly COLOR_RESET=$(tput sgr0)

# Icons and symbols
readonly ICON_SUCCESS="✅"
readonly ICON_ERROR="❌"
readonly ICON_WARNING="⚠️"
readonly ICON_INFO="ℹ️"
readonly ICON_ROCKET="🚀"
readonly ICON_WIZARD="🧙"
readonly ICON_TARGET="🎯"
readonly ICON_LIGHTNING="⚡"
readonly ICON_GEAR="⚙️"
readonly ICON_STAR="⭐"

# Setup state
declare -A PROJECT_CONFIG
declare -a RECOMMENDED_AGENTS
declare -a DETECTED_TECHNOLOGIES

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

print_header() {
    clear
    echo ""
    echo "${COLOR_BLUE}${COLOR_BOLD}===============================================================================${COLOR_RESET}"
    echo "${COLOR_BLUE}${COLOR_BOLD}${ICON_WIZARD} INTERACTIVE FRAMEWORK SETUP WIZARD v${SCRIPT_VERSION}${COLOR_RESET}"
    echo "${COLOR_CYAN}Claude Code Multi-Agent Framework - Zero-Configuration Project Setup${COLOR_RESET}"
    echo "${COLOR_BLUE}${COLOR_BOLD}===============================================================================${COLOR_RESET}"
    echo ""
}

print_status() {
    local status="$1"
    local message="$2"
    case "$status" in
        "success") echo "${ICON_SUCCESS} ${COLOR_GREEN}${message}${COLOR_RESET}" ;;
        "error")   echo "${ICON_ERROR} ${COLOR_RED}${message}${COLOR_RESET}" ;;
        "warning") echo "${ICON_WARNING} ${COLOR_YELLOW}${message}${COLOR_RESET}" ;;
        "info")    echo "${ICON_INFO} ${COLOR_CYAN}${message}${COLOR_RESET}" ;;
        *)         echo "${message}" ;;
    esac
}

print_step() {
    local step="$1"
    local title="$2"
    echo ""
    echo "${COLOR_MAGENTA}${COLOR_BOLD}${ICON_TARGET} PHASE ${step}: ${title}${COLOR_RESET}"
    echo "${COLOR_MAGENTA}$(printf '=%.0s' {1..60})${COLOR_RESET}"
    echo ""
}

ask_question() {
    local question="$1"
    local default="$2"
    local response

    echo -n "${COLOR_CYAN}${question}${COLOR_RESET}"
    if [[ -n "$default" ]]; then
        echo -n " ${COLOR_YELLOW}[${default}]${COLOR_RESET}"
    fi
    echo -n ": "

    read -r response
    echo "${response:-$default}"
}

ask_yes_no() {
    local question="$1"
    local default="${2:-y}"
    local response

    while true; do
        echo -n "${COLOR_CYAN}${question} (y/n)${COLOR_RESET}"
        if [[ -n "$default" ]]; then
            echo -n " ${COLOR_YELLOW}[${default}]${COLOR_RESET}"
        fi
        echo -n ": "

        read -r response
        response="${response:-$default}"

        case "$response" in
            [Yy]|[Yy][Ee][Ss]) return 0 ;;
            [Nn]|[Nn][Oo]) return 1 ;;
            *) echo "${COLOR_RED}Please enter 'y' or 'n'${COLOR_RESET}" ;;
        esac
    done
}

select_from_list() {
    local title="$1"
    shift
    local options=("$@")
    local choice

    echo "${COLOR_CYAN}${title}:${COLOR_RESET}"
    echo ""

    for i in "${!options[@]}"; do
        echo "  ${COLOR_YELLOW}[$((i+1))]${COLOR_RESET} ${options[$i]}"
    done
    echo ""

    while true; do
        choice=$(ask_question "Select option (1-${#options[@]})" "1")
        if [[ "$choice" =~ ^[0-9]+$ ]] && [[ "$choice" -ge 1 ]] && [[ "$choice" -le "${#options[@]}" ]]; then
            echo "${options[$((choice-1))]}"
            return 0
        else
            echo "${COLOR_RED}Invalid selection. Please choose 1-${#options[@]}${COLOR_RESET}"
        fi
    done
}

# =============================================================================
# PROJECT ANALYSIS FUNCTIONS
# =============================================================================

detect_project_technologies() {
    print_status "info" "Analyzing project structure and technologies..."

    export PYTHONPATH="$AI_CORE_DIR:$PYTHONPATH"

    # Run technology detection
    local tech_output
    tech_output=$(python3 -c "
import sys
import json
sys.path.insert(0, '$AI_CORE_DIR')
from core.data_collection_system import TechnologyDetector

try:
    detector = TechnologyDetector()
    tech_stack = detector.detect_technology_stack('$PROJECT_DIR')

    result = {
        'frontend': tech_stack.frontend[:5],
        'backend': tech_stack.backend[:5],
        'database': tech_stack.database[:3],
        'infrastructure': tech_stack.infrastructure[:3],
        'testing': tech_stack.testing[:3],
        'confidence': tech_stack.confidence_score
    }
    print(json.dumps(result))
except Exception as e:
    print('{}')
" 2>/dev/null)

    if [[ -n "$tech_output" && "$tech_output" != "{}" ]]; then
        DETECTED_TECHNOLOGIES=($(echo "$tech_output" | python3 -c "
import json, sys
data = json.load(sys.stdin)
all_techs = []
for category in ['frontend', 'backend', 'database', 'infrastructure', 'testing']:
    all_techs.extend(data.get(category, []))
print(' '.join(all_techs[:10]))
"))

        local confidence
        confidence=$(echo "$tech_output" | python3 -c "
import json, sys
data = json.load(sys.stdin)
print(f\"{data.get('confidence', 0):.2f}\")
")

        print_status "success" "Technology detection completed (confidence: $confidence)"

        if [[ ${#DETECTED_TECHNOLOGIES[@]} -gt 0 ]]; then
            echo "${COLOR_GREEN}Detected technologies:${COLOR_RESET} ${DETECTED_TECHNOLOGIES[*]}"
        fi
    else
        print_status "warning" "Technology detection failed - will use manual input"
        DETECTED_TECHNOLOGIES=()
    fi
}

get_agent_recommendations() {
    print_status "info" "Generating intelligent agent recommendations..."

    export PYTHONPATH="$AI_CORE_DIR:$PYTHONPATH"

    local agents_output
    agents_output=$(python3 -c "
import sys
import json
sys.path.insert(0, '$AI_CORE_DIR')
from integration.ai_agent_selector import AgentSelectionEngine, AgentSelectionRequest

try:
    selector = AgentSelectionEngine('$PROJECT_DIR')
    request = AgentSelectionRequest(project_path='$PROJECT_DIR', max_agents=8)
    response = selector.select_agents(request)

    print(json.dumps(response.recommended_agents))
except Exception as e:
    print('[]')
" 2>/dev/null)

    if [[ -n "$agents_output" && "$agents_output" != "[]" ]]; then
        readarray -t RECOMMENDED_AGENTS < <(echo "$agents_output" | python3 -c "
import json, sys
agents = json.load(sys.stdin)
for agent in agents:
    print(agent)
")
        print_status "success" "Generated ${#RECOMMENDED_AGENTS[@]} agent recommendations"
    else
        # Fallback recommendations
        RECOMMENDED_AGENTS=("project-owner" "session-manager" "software-architect" "frontend-engineer" "backend-engineer" "qa-engineer")
        print_status "warning" "Using fallback agent recommendations"
    fi
}

# =============================================================================
# SETUP PHASES
# =============================================================================

phase_1_welcome() {
    print_step "1" "Welcome & Project Detection"

    echo "${COLOR_CYAN}Welcome to the Claude Code Multi-Agent Framework Setup Wizard!${COLOR_RESET}"
    echo ""
    echo "This wizard will help you:"
    echo "• ${ICON_GEAR} Detect your project's technology stack"
    echo "• ${ICON_TARGET} Recommend optimal agents for your project"
    echo "• ${ICON_LIGHTNING} Generate custom CLAUDE.md configuration"
    echo "• ${ICON_ROCKET} Set up the framework for immediate use"
    echo ""

    print_status "info" "Current project: ${COLOR_BOLD}$PROJECT_NAME${COLOR_RESET}"
    print_status "info" "Project path: ${COLOR_BOLD}$PROJECT_DIR${COLOR_RESET}"

    echo ""

    if [[ -f "$TARGET_CLAUDE_MD" ]]; then
        echo "${COLOR_YELLOW}${ICON_WARNING} CLAUDE.md already exists in this project.${COLOR_RESET}"
        echo ""
        if ask_yes_no "Continue with setup? (This will create backup of existing CLAUDE.md)"; then
            cp "$TARGET_CLAUDE_MD" "${TARGET_CLAUDE_MD}.backup.$(date +%Y%m%d_%H%M%S)"
            print_status "success" "Backup created"
        else
            print_status "info" "Setup cancelled by user"
            exit 0
        fi
    fi

    echo ""
    ask_yes_no "Ready to begin intelligent project analysis?" || {
        print_status "info" "Setup cancelled by user"
        exit 0
    }
}

phase_2_project_analysis() {
    print_step "2" "Intelligent Project Analysis"

    detect_project_technologies
    echo ""
    get_agent_recommendations
    echo ""

    # Get project basic info
    PROJECT_CONFIG[project_name]=$(ask_question "Project name" "$PROJECT_NAME")
    PROJECT_CONFIG[project_description]=$(ask_question "Project description" "AI-powered development project")
    PROJECT_CONFIG[project_version]=$(ask_question "Initial version" "1.0.0")

    echo ""
    PROJECT_CONFIG[primary_language]=$(select_from_list "Primary programming language" \
        "TypeScript" "JavaScript" "Python" "Java" "C#" "Go" "Rust" "PHP" "Other")

    PROJECT_CONFIG[business_domain]=$(select_from_list "Business domain" \
        "web_development" "mobile_development" "data_science" "fintech" "healthcare" \
        "ecommerce" "education" "gaming" "enterprise" "api_services" "other")

    PROJECT_CONFIG[project_scale]=$(select_from_list "Project scale" \
        "startup" "sme" "enterprise")

    PROJECT_CONFIG[development_stage]=$(select_from_list "Development stage" \
        "planning" "development" "testing" "production" "maintenance")
}

phase_3_technology_configuration() {
    print_step "3" "Technology Stack Configuration"

    echo "Based on analysis, we detected these technologies:"
    if [[ ${#DETECTED_TECHNOLOGIES[@]} -gt 0 ]]; then
        for tech in "${DETECTED_TECHNOLOGIES[@]}"; do
            echo "  ${ICON_SUCCESS} $tech"
        done
    else
        echo "  ${COLOR_YELLOW}No technologies auto-detected${COLOR_RESET}"
    fi

    echo ""

    if ask_yes_no "Add additional technologies manually?"; then
        echo ""
        echo "Enter additional technologies (comma-separated):"
        local additional_techs
        additional_techs=$(ask_question "Additional technologies" "")

        if [[ -n "$additional_techs" ]]; then
            IFS=',' read -ra ADDR <<< "$additional_techs"
            for tech in "${ADDR[@]}"; do
                DETECTED_TECHNOLOGIES+=("$(echo "$tech" | xargs)")
            done
        fi
    fi

    PROJECT_CONFIG[technologies]=$(IFS=','; echo "${DETECTED_TECHNOLOGIES[*]}")
}

phase_4_agent_selection() {
    print_step "4" "Agent Selection & Customization"

    echo "Recommended agents for your project:"
    echo ""

    for i in "${!RECOMMENDED_AGENTS[@]}"; do
        echo "  ${COLOR_GREEN}$((i+1)).${COLOR_RESET} ${RECOMMENDED_AGENTS[$i]}"
    done

    echo ""

    if ask_yes_no "Customize agent selection?"; then
        echo ""
        echo "Additional agents you might want to consider:"
        echo "  ${COLOR_CYAN}• security-engineer${COLOR_RESET} - For security-critical applications"
        echo "  ${COLOR_CYAN}• data-engineer${COLOR_RESET} - For data-intensive applications"
        echo "  ${COLOR_CYAN}• mobile-developer${COLOR_RESET} - For mobile app development"
        echo "  ${COLOR_CYAN}• devops-architect${COLOR_RESET} - For complex deployment needs"
        echo ""

        local additional_agents
        additional_agents=$(ask_question "Add agents (comma-separated)" "")

        if [[ -n "$additional_agents" ]]; then
            IFS=',' read -ra ADDR <<< "$additional_agents"
            for agent in "${ADDR[@]}"; do
                RECOMMENDED_AGENTS+=("$(echo "$agent" | xargs)")
            done
        fi
    fi

    PROJECT_CONFIG[agents]=$(IFS=','; echo "${RECOMMENDED_AGENTS[*]}")
}

phase_5_framework_features() {
    print_step "5" "Framework Features Configuration"

    echo "Configure framework features:"
    echo ""

    # MCP Tools
    if ask_yes_no "Enable MCP Tools integration? (Serena, Context7, Playwright)"; then
        PROJECT_CONFIG[mcp_tools_enabled]="true"
    else
        PROJECT_CONFIG[mcp_tools_enabled]="false"
    fi

    # AI Tools
    if ask_yes_no "Enable AI-powered agent selection?"; then
        PROJECT_CONFIG[ai_tools_enabled]="true"
    else
        PROJECT_CONFIG[ai_tools_enabled]="false"
    fi

    # Session Management
    if ask_yes_no "Enable advanced session management?"; then
        PROJECT_CONFIG[session_management]="true"
    else
        PROJECT_CONFIG[session_management]="false"
    fi

    # Quality Gates
    if ask_yes_no "Enable automated quality gates?"; then
        PROJECT_CONFIG[quality_gates]="true"
    else
        PROJECT_CONFIG[quality_gates]="false"
    fi
}

phase_6_claude_md_generation() {
    print_step "6" "CLAUDE.md Generation"

    print_status "info" "Generating customized CLAUDE.md configuration..."

    # Generate CLAUDE.md content
    cat > "$TARGET_CLAUDE_MD" << EOF
# CLAUDE.md – ${PROJECT_CONFIG[project_name]} Configuration

## Project Metadata
- **project_name**: "${PROJECT_CONFIG[project_name]}"
- **project_description**: "${PROJECT_CONFIG[project_description]}"
- **project_version**: "${PROJECT_CONFIG[project_version]}"
- **primary_language**: "${PROJECT_CONFIG[primary_language]}"
- **business_domain**: "${PROJECT_CONFIG[business_domain]}"
- **project_scale**: "${PROJECT_CONFIG[project_scale]}"
- **development_stage**: "${PROJECT_CONFIG[development_stage]}"

## Project Overview
${PROJECT_CONFIG[project_description]}

**Technologies**: ${PROJECT_CONFIG[technologies]}

**Goals**: Accelerate development, improve code quality, enhance collaboration, standardize processes.

## Technologies
**Framework**: Claude Code Multi-Agent Framework v${FRAMEWORK_VERSION}

**Stack**: ${PROJECT_CONFIG[technologies]}

## Agents and Roles
**Recommended Agents**: ${PROJECT_CONFIG[agents]}

## Integrations
**MCP Tools**: ${PROJECT_CONFIG[mcp_tools_enabled]}
**AI Tools**: ${PROJECT_CONFIG[ai_tools_enabled]}
**Development**: Git, code quality tools, testing frameworks

## Requirements
**Performance**: <2s prompt response, parallel execution
**Scalability**: Multi-project support, agent extensibility
**Reliability**: 99.9% session recovery, graceful degradation
**Security**: No hardcoded secrets, safe code generation

## Framework Guidelines
**Style**: Readability first, functional design, consistent naming
**Agent Rules**: Clear communication, specific error handling, enterprise quality

## Version History
**Current**: ${PROJECT_CONFIG[project_version]}
**Created**: $(date +%Y-%m-%d)
**Status**: Initial framework setup completed

---

*Generated by Claude Code Multi-Agent Framework Setup Wizard v${SCRIPT_VERSION}*
EOF

    print_status "success" "CLAUDE.md generated successfully"

    # Generate basic .gitignore if it doesn't exist
    if [[ ! -f "$TARGET_GITIGNORE" ]]; then
        cat > "$TARGET_GITIGNORE" << EOF
# Dependencies
node_modules/
venv/
.env

# Build outputs
dist/
build/
*.o
*.so

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Framework
/work/
Session_*.md
*.session

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
EOF
        print_status "success" "Basic .gitignore created"
    fi
}

phase_7_completion() {
    print_step "7" "Setup Completion & Next Steps"

    print_status "success" "Framework setup completed successfully!"
    echo ""

    echo "${COLOR_GREEN}${COLOR_BOLD}${ICON_STAR} What was configured:${COLOR_RESET}"
    echo "• ${ICON_SUCCESS} Project analyzed and configured"
    echo "• ${ICON_SUCCESS} ${#RECOMMENDED_AGENTS[@]} agents recommended"
    echo "• ${ICON_SUCCESS} CLAUDE.md generated with your settings"
    echo "• ${ICON_SUCCESS} Framework ready for immediate use"

    if [[ ${#DETECTED_TECHNOLOGIES[@]} -gt 0 ]]; then
        echo "• ${ICON_SUCCESS} ${#DETECTED_TECHNOLOGIES[@]} technologies detected"
    fi

    echo ""
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_ROCKET} Next Steps:${COLOR_RESET}"
    echo "1. Review generated CLAUDE.md file"
    echo "2. Run: ${COLOR_YELLOW}./ai-tools.sh${COLOR_RESET} to access AI tools"
    echo "3. Run: ${COLOR_YELLOW}./mcp-tools.sh${COLOR_RESET} to set up MCP tools"
    echo "4. Start using framework agents for development"
    echo ""

    echo "${COLOR_GREEN}${COLOR_BOLD}${ICON_LIGHTNING} Quick Commands:${COLOR_RESET}"
    echo "• ${COLOR_CYAN}./ai-tools.sh --analyze${COLOR_RESET}     # Analyze your project"
    echo "• ${COLOR_CYAN}./ai-tools.sh --recommend${COLOR_RESET}   # Get agent recommendations"
    echo "• ${COLOR_CYAN}./mcp-tools.sh${COLOR_RESET}              # Set up MCP tools"
    echo ""

    if ask_yes_no "Open CLAUDE.md for review?"; then
        if command -v code >/dev/null 2>&1; then
            code "$TARGET_CLAUDE_MD"
        elif command -v nano >/dev/null 2>&1; then
            nano "$TARGET_CLAUDE_MD"
        else
            echo "${COLOR_CYAN}Generated CLAUDE.md:${COLOR_RESET}"
            echo "Path: $TARGET_CLAUDE_MD"
        fi
    fi

    echo ""
    print_status "success" "Welcome to the Claude Code Multi-Agent Framework! ${ICON_ROCKET}"
}

# =============================================================================
# MAIN EXECUTION
# =============================================================================

main() {
    # Check if we're in the right place
    if [[ ! -f "$FRAMEWORK_ROOT/ai-tools.sh" || ! -d "$AI_CORE_DIR" ]]; then
        echo "${COLOR_RED}${ICON_ERROR} Error: This script must be run from a Claude Code Framework directory${COLOR_RESET}"
        echo "Please ensure you're in the framework root directory."
        exit 1
    fi

    # Check Python availability
    if ! command -v python3 >/dev/null 2>&1; then
        echo "${COLOR_RED}${ICON_ERROR} Error: Python 3 is required but not found${COLOR_RESET}"
        echo "Please install Python 3 and try again."
        exit 1
    fi

    # Run setup phases
    phase_1_welcome
    phase_2_project_analysis
    phase_3_technology_configuration
    phase_4_agent_selection
    phase_5_framework_features
    phase_6_claude_md_generation
    phase_7_completion
}

# Execute main function
main "$@"