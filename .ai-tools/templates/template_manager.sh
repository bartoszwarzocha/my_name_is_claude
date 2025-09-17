#!/bin/bash

# =============================================================================
# QUICK START TEMPLATE MANAGER v1.0.0
# Claude Code Multi-Agent Framework - Project Template Generator
# =============================================================================

set -e

# =============================================================================
# CONFIGURATION
# =============================================================================

readonly SCRIPT_VERSION="1.0.0"
readonly PROJECT_DIR="$(pwd)"
readonly TEMPLATES_DIR="$PROJECT_DIR/.ai-tools/templates"

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

# Icons
readonly ICON_TEMPLATE="📋"
readonly ICON_ROCKET="🚀"
readonly ICON_SUCCESS="✅"
readonly ICON_INFO="ℹ️"
readonly ICON_WIZARD="🧙"

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

print_header() {
    clear
    echo ""
    echo "${COLOR_BLUE}${COLOR_BOLD}===============================================================================${COLOR_RESET}"
    echo "${COLOR_BLUE}${COLOR_BOLD}${ICON_TEMPLATE} QUICK START TEMPLATE MANAGER v${SCRIPT_VERSION}${COLOR_RESET}"
    echo "${COLOR_CYAN}Generate Project Templates for Popular Tech Stacks${COLOR_RESET}"
    echo "${COLOR_BLUE}${COLOR_BOLD}===============================================================================${COLOR_RESET}"
    echo ""
}

print_status() {
    local status="$1"
    local message="$2"
    case "$status" in
        "success") echo "${ICON_SUCCESS} ${COLOR_GREEN}${message}${COLOR_RESET}" ;;
        "error")   echo "❌ ${COLOR_RED}${message}${COLOR_RESET}" ;;
        "warning") echo "⚠️ ${COLOR_YELLOW}${message}${COLOR_RESET}" ;;
        "info")    echo "${ICON_INFO} ${COLOR_CYAN}${message}${COLOR_RESET}" ;;
        *)         echo "${message}" ;;
    esac
}

ask_question() {
    local question="$1"
    local default="$2"

    echo -n "${COLOR_CYAN}${question}${COLOR_RESET}"
    if [[ -n "$default" ]]; then
        echo -n " ${COLOR_YELLOW}[${default}]${COLOR_RESET}"
    fi
    echo -n ": "

    read -r response
    echo "${response:-$default}"
}

# =============================================================================
# TEMPLATE DEFINITIONS
# =============================================================================

declare -A TEMPLATES=(
    ["react-app"]="React Application with TypeScript"
    ["python-app"]="Python Application with FastAPI/Django"
    ["node-api"]="Node.js API with TypeScript"
    ["angular-app"]="Angular Application with TypeScript"
    ["fullstack-mern"]="MERN Stack (MongoDB, Express, React, Node.js)"
    ["ai-rag-system"]="AI RAG System with Python & LangChain"
    ["arduino-iot"]="Arduino IoT Project with C++"
    ["python-desktop-database"]="Python Desktop App with wxPython & SQLite"
    ["wxwidgets-cpp"]="wxWidgets C++ Desktop Application"
    ["enterprise-rest-api"]="Enterprise REST API (Java/C#/.NET)"
)

declare -A TEMPLATE_DESCRIPTIONS=(
    ["react-app"]="Modern React application with TypeScript, hooks, and comprehensive testing. Perfect for SPAs and frontend-focused projects."
    ["python-app"]="Python application with clean architecture, FastAPI/Django, and production-ready deployment. Ideal for backend services and APIs."
    ["node-api"]="High-performance Node.js API with TypeScript, Express.js, and comprehensive validation. Great for RESTful APIs and microservices."
    ["angular-app"]="Enterprise-grade Angular application with NgRx, Material Design, and scalable architecture. Perfect for large-scale applications."
    ["fullstack-mern"]="Complete MERN stack application with TypeScript, authentication, and real-time features. Ideal for full-stack web applications."
    ["ai-rag-system"]="Advanced RAG system with Python, LangChain, vector databases, and LLM integration. Perfect for AI-powered knowledge systems."
    ["arduino-iot"]="Arduino-based IoT project with sensor integration, WiFi connectivity, and cloud data transmission. Ideal for embedded IoT solutions."
    ["python-desktop-database"]="Professional desktop application with wxPython GUI and SQLite database. Perfect for cross-platform desktop tools."
    ["wxwidgets-cpp"]="Native C++ desktop application with wxWidgets framework. Ideal for high-performance cross-platform desktop software."
    ["enterprise-rest-api"]="Enterprise-grade REST API with comprehensive security, monitoring, and compliance. Perfect for mission-critical business systems."
)

declare -A TEMPLATE_AGENTS=(
    ["react-app"]="frontend-engineer, ux-designer, qa-engineer"
    ["python-app"]="backend-engineer, api-engineer, database-administrator"
    ["node-api"]="api-engineer, backend-engineer, security-engineer"
    ["angular-app"]="frontend-engineer, ux-designer, software-architect"
    ["fullstack-mern"]="frontend-engineer, backend-engineer, api-engineer, data-engineer"
    ["ai-rag-system"]="data-engineer, backend-engineer, api-engineer"
    ["arduino-iot"]="embedded-engineer, electronics-engineer, backend-engineer"
    ["python-desktop-database"]="desktop-specialist, data-engineer, ux-designer"
    ["wxwidgets-cpp"]="desktop-specialist, graphics-2d-engineer, software-architect"
    ["enterprise-rest-api"]="enterprise-architect, api-engineer, security-engineer"
)

# =============================================================================
# TEMPLATE GENERATION FUNCTIONS
# =============================================================================

show_available_templates() {
    clear
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_TEMPLATE} Available Project Templates:${COLOR_RESET}"
    echo ""

    local i=1
    for template_key in "${!TEMPLATES[@]}"; do
        local template_name="${TEMPLATES[$template_key]}"
        local template_desc="${TEMPLATE_DESCRIPTIONS[$template_key]}"

        echo "${COLOR_YELLOW}[$i]${COLOR_RESET} ${COLOR_GREEN}$template_name${COLOR_RESET}"
        echo "    ${COLOR_WHITE}$template_desc${COLOR_RESET}"
        echo ""
        ((i++))
    done
}

show_template_details() {
    local template_key="$1"
    local template_name="${TEMPLATES[$template_key]}"
    local template_desc="${TEMPLATE_DESCRIPTIONS[$template_key]}"
    local template_agents="${TEMPLATE_AGENTS[$template_key]}"

    echo "${COLOR_CYAN}${COLOR_BOLD}Template: $template_name${COLOR_RESET}"
    echo ""
    echo "${COLOR_GREEN}Description:${COLOR_RESET}"
    echo "$template_desc"
    echo ""
    echo "${COLOR_GREEN}Recommended Agents:${COLOR_RESET}"
    echo "$template_agents"
    echo ""
}

collect_project_info() {
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_WIZARD} Project Configuration${COLOR_RESET}"
    echo ""

    PROJECT_NAME=$(ask_question "Project name" "my-awesome-project")
    PROJECT_DESCRIPTION=$(ask_question "Project description" "A modern application built with best practices")

    echo ""
    echo "${COLOR_GREEN}Business Domain Options:${COLOR_RESET}"
    echo "1. E-commerce    2. Healthcare    3. Finance    4. Education"
    echo "5. Social Media  6. Productivity  7. Gaming     8. Other"
    echo ""

    local domain_choice=$(ask_question "Select business domain (1-8)" "8")
    case "$domain_choice" in
        "1") BUSINESS_DOMAIN="ecommerce" ;;
        "2") BUSINESS_DOMAIN="healthcare" ;;
        "3") BUSINESS_DOMAIN="finance" ;;
        "4") BUSINESS_DOMAIN="education" ;;
        "5") BUSINESS_DOMAIN="social_media" ;;
        "6") BUSINESS_DOMAIN="productivity" ;;
        "7") BUSINESS_DOMAIN="gaming" ;;
        *) BUSINESS_DOMAIN="general" ;;
    esac

    echo ""
    echo "${COLOR_GREEN}Project Scale Options:${COLOR_RESET}"
    echo "1. Startup (MVP)  2. SME (Small-Medium)  3. Enterprise (Large-scale)"
    echo ""

    local scale_choice=$(ask_question "Select project scale (1-3)" "2")
    case "$scale_choice" in
        "1") PROJECT_SCALE="startup" ;;
        "2") PROJECT_SCALE="sme" ;;
        "3") PROJECT_SCALE="enterprise" ;;
        *) PROJECT_SCALE="sme" ;;
    esac
}

generate_claude_md() {
    local template_key="$1"
    local template_file="$TEMPLATES_DIR/${template_key}.md"
    local output_file="$PROJECT_DIR/CLAUDE.md"

    if [[ ! -f "$template_file" ]]; then
        print_status "error" "Template file not found: $template_file"
        return 1
    fi

    print_status "info" "Generating CLAUDE.md from $template_key template..."

    # Read template and substitute variables
    local content=$(cat "$template_file")
    content=${content//\{\{PROJECT_NAME\}\}/$PROJECT_NAME}
    content=${content//\{\{PROJECT_DESCRIPTION\}\}/$PROJECT_DESCRIPTION}
    content=${content//\{\{BUSINESS_DOMAIN\}\}/$BUSINESS_DOMAIN}
    content=${content//\{\{PROJECT_SCALE\}\}/$PROJECT_SCALE}

    # Write to CLAUDE.md
    echo "$content" > "$output_file"

    print_status "success" "CLAUDE.md generated successfully!"
    echo ""
    echo "${COLOR_YELLOW}Generated Configuration:${COLOR_RESET}"
    echo "• Project: $PROJECT_NAME"
    echo "• Description: $PROJECT_DESCRIPTION"
    echo "• Domain: $BUSINESS_DOMAIN"
    echo "• Scale: $PROJECT_SCALE"
    echo "• Template: ${TEMPLATES[$template_key]}"
    echo ""
    echo "${COLOR_GREEN}Next Steps:${COLOR_RESET}"
    echo "1. Review the generated CLAUDE.md file"
    echo "2. Run './ai-tools.sh -r' for agent recommendations"
    echo "3. Use './ai-tools.sh -w' to set up the framework"
    echo "4. Start developing with the recommended agents"
}

select_template() {
    while true; do
        show_available_templates

        echo "${COLOR_YELLOW}[b]${COLOR_RESET} Back to main menu"
        echo "${COLOR_YELLOW}[q]${COLOR_RESET} Quit"
        echo ""

        local template_keys=($(printf '%s\n' "${!TEMPLATES[@]}" | sort))
        echo -n "${COLOR_BOLD}Select template (1-${#template_keys[@]}, b, q): ${COLOR_RESET}"
        read -r choice
        echo ""

        if [[ "$choice" == "b" ]]; then
            return 0
        elif [[ "$choice" == "q" ]]; then
            exit 0
        elif [[ "$choice" =~ ^[0-9]+$ ]] && [[ "$choice" -ge 1 ]] && [[ "$choice" -le "${#template_keys[@]}" ]]; then
            local selected_template="${template_keys[$((choice-1))]}"

            show_template_details "$selected_template"

            echo -n "${COLOR_BOLD}Use this template? (y/n): ${COLOR_RESET}"
            read -r confirm

            if [[ "$confirm" =~ ^[Yy] ]]; then
                collect_project_info
                generate_claude_md "$selected_template"
                return 0
            fi
        else
            print_status "error" "Invalid selection"
        fi
        echo ""
    done
}

show_existing_templates() {
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_INFO} Template Library Status${COLOR_RESET}"
    echo ""

    print_status "info" "Scanning template directory: $TEMPLATES_DIR"
    echo ""

    # Check each template dynamically from TEMPLATES array
    local available_count=0
    local missing_count=0

    # Explicit template list for reliable iteration
    local template_list="ai-rag-system angular-app arduino-iot enterprise-rest-api fullstack-mern node-api python-app python-desktop-database react-app wxwidgets-cpp"

    for template_key in $template_list; do
        local template_name="${TEMPLATES[$template_key]}"
        local template_file="$TEMPLATES_DIR/${template_key}.md"

        if [[ -f "$template_file" ]]; then
            echo "${ICON_SUCCESS} ${COLOR_GREEN}$template_name${COLOR_RESET} - ${template_key}.md"
            available_count=$((available_count + 1))
        else
            echo "❌ ${COLOR_RED}$template_name${COLOR_RESET} - Missing: ${template_key}.md"
            missing_count=$((missing_count + 1))
        fi
    done

    echo ""
    if [[ $missing_count -eq 0 ]]; then
        print_status "success" "Template library contains $available_count templates - All templates available!"
    else
        print_status "warning" "Template library: $available_count available, $missing_count missing"
    fi
    echo ""
    echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
    read -r
}

check_existing_claude_md() {
    if [[ -f "$PROJECT_DIR/CLAUDE.md" ]]; then
        echo "${COLOR_YELLOW}⚠️ CLAUDE.md already exists in this directory.${COLOR_RESET}"
        echo ""
        echo -n "${COLOR_BOLD}Overwrite existing CLAUDE.md? (y/n): ${COLOR_RESET}"
        read -r overwrite

        if [[ ! "$overwrite" =~ ^[Yy] ]]; then
            print_status "info" "Template generation cancelled"
            return 1
        fi

        # Create backup
        cp "$PROJECT_DIR/CLAUDE.md" "$PROJECT_DIR/CLAUDE.md.backup.$(date +%Y%m%d_%H%M%S)"
        print_status "info" "Created backup of existing CLAUDE.md"
        echo ""
    fi
    return 0
}

show_main_menu() {
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_ROCKET} Template Manager Options:${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}[1]${COLOR_RESET} Generate Project Template  ${COLOR_WHITE}- Create CLAUDE.md from template${COLOR_RESET}"
    echo "${COLOR_YELLOW}[2]${COLOR_RESET} Browse Templates           ${COLOR_WHITE}- View available templates${COLOR_RESET}"
    echo "${COLOR_YELLOW}[3]${COLOR_RESET} Template Library Status    ${COLOR_WHITE}- Check template availability${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}[b]${COLOR_RESET} Back to AI Tools           ${COLOR_WHITE}- Return to main menu${COLOR_RESET}"
    echo "${COLOR_YELLOW}[q]${COLOR_RESET} Quit                       ${COLOR_WHITE}- Exit template manager${COLOR_RESET}"
    echo ""
}

# =============================================================================
# MAIN EXECUTION
# =============================================================================

main() {
    while true; do
        print_header

        # Show quick stats
        local available_templates=$(find "$TEMPLATES_DIR" -name "*.md" -not -name "template_manager.sh" -type f | wc -l)
        echo "${COLOR_GREEN}Available Templates:${COLOR_RESET} $available_templates"
        echo "${COLOR_GREEN}Current Directory:${COLOR_RESET} $PROJECT_DIR"
        echo ""

        show_main_menu

        echo -n "${COLOR_BOLD}${ICON_TEMPLATE} Select option: ${COLOR_RESET}"
        read -r choice
        echo ""

        case "$choice" in
            "1")
                if check_existing_claude_md; then
                    select_template
                fi
                ;;
            "2") show_available_templates; echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"; read -r ;;
            "3") show_existing_templates ;;
            "b")
                echo "${ICON_SUCCESS} ${COLOR_GREEN}Returning to AI Tools...${COLOR_RESET}"
                exit 0
                ;;
            "q")
                echo "${ICON_SUCCESS} ${COLOR_GREEN}Thank you for using Template Manager!${COLOR_RESET}"
                exit 0
                ;;
            *) print_status "error" "Invalid option: $choice" ;;
        esac

        echo ""
    done
}

# Run main function
main "$@"