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
readonly FRAMEWORK_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
readonly TEMPLATES_DIR="$FRAMEWORK_ROOT/.ai-tools/templates"

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

# Timeout wrapper for read operations to prevent hanging
safe_read() {
    local timeout_duration=${1:-30}  # Default 30 second timeout
    local prompt_var="$2"
    local result_var="$3"

    # Use timeout with read
    if timeout "$timeout_duration" bash -c "read -r response; echo \"\$response\"" 2>/dev/null; then
        return 0
    else
        echo ""  # Return empty on timeout
        return 1
    fi
}

# Enhanced read function with timeout protection
safe_read_with_retry() {
    local timeout_duration=${1:-30}
    local max_retries=${2:-2}
    local attempt=1

    while [[ $attempt -le $max_retries ]]; do
        if [[ $attempt -gt 1 ]]; then
            print_status "warning" "Input timeout, retrying (attempt $attempt/$max_retries)..."
        fi

        local result
        if result=$(timeout "$timeout_duration" bash -c "read -r response; echo \"\$response\"" 2>/dev/null); then
            echo "$result"
            return 0
        fi

        ((attempt++))
        sleep 1
    done

    print_status "warning" "Input timeout after $max_retries attempts, using default"
    echo ""
    return 1
}

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

    local response
    read -r response
    echo "${response:-$default}"
}

# =============================================================================
# DYNAMIC TEMPLATE DISCOVERY
# =============================================================================

# Dynamic arrays populated by scan_templates()
declare -A TEMPLATES
declare -A TEMPLATE_DESCRIPTIONS
declare -A TEMPLATE_AGENTS

# Technology-based agent mapping for automatic agent recommendations
declare -A TECH_AGENT_MAP=(
    ["react"]="frontend-engineer, ux-designer"
    ["angular"]="frontend-engineer, ux-designer, software-architect"
    ["python"]="backend-engineer, data-engineer"
    ["fastapi"]="api-engineer, backend-engineer"
    ["django"]="backend-engineer, data-engineer"
    ["node.js"]="api-engineer, backend-engineer"
    ["typescript"]="frontend-engineer, backend-engineer"
    ["javascript"]="frontend-engineer, backend-engineer"
    ["cpp"]="desktop-specialist, software-architect"
    ["c++"]="desktop-specialist, software-architect"
    ["wxwidgets"]="desktop-specialist, graphics-2d-engineer"
    ["mern"]="frontend-engineer, backend-engineer, api-engineer, data-engineer"
    ["arduino"]="embedded-engineer, electronics-engineer"
    ["iot"]="embedded-engineer, electronics-engineer, backend-engineer"
    ["rag"]="data-engineer, backend-engineer, api-engineer"
    ["langchain"]="data-engineer, backend-engineer"
    ["enterprise"]="enterprise-architect, security-engineer"
    ["api"]="api-engineer, backend-engineer"
    ["desktop"]="desktop-specialist, ux-designer"
    ["database"]="data-engineer, database-administrator"
)

scan_templates() {
    print_status "info" "Scanning template directory for available templates..."

    # Clear existing arrays
    for key in "${!TEMPLATES[@]}"; do
        unset TEMPLATES["$key"]
        unset TEMPLATE_DESCRIPTIONS["$key"]
        unset TEMPLATE_AGENTS["$key"]
    done

    # Find all .md files in templates directory
    local template_files=()
    while IFS= read -r -d '' file; do
        template_files+=("$file")
    done < <(find "$TEMPLATES_DIR" -name "*.md" -type f -print0 2>/dev/null)

    local template_count=0

    for template_file in "${template_files[@]}"; do
        local template_key=$(basename "$template_file" .md)

        # Skip if it's the template_manager.sh itself
        if [[ "$template_key" == "template_manager" ]]; then
            continue
        fi

        # Extract template name from first line (# CLAUDE.md – Template Name)
        local template_name=""
        local first_line=$(head -n 1 "$template_file" 2>/dev/null)
        if [[ "$first_line" =~ ^#[[:space:]]*CLAUDE\.md[[:space:]]*–[[:space:]]*(.+)$ ]]; then
            template_name="${BASH_REMATCH[1]}"
        else
            # Fallback: use filename with spaces
            template_name=$(echo "$template_key" | sed 's/-/ /g' | sed 's/\b\w/\U&/g')
        fi

        # Extract description from Project Overview section
        local description=""
        local in_overview=false
        local overview_content=""

        while IFS= read -r line; do
            if [[ "$line" =~ ^##[[:space:]]*Project[[:space:]]*Overview[[:space:]]*$ ]]; then
                in_overview=true
                continue
            elif [[ "$line" =~ ^##[[:space:]]*.*$ ]] && [[ "$in_overview" == true ]]; then
                break
            elif [[ "$in_overview" == true ]] && [[ "$line" =~ ^[A-Z].*\.[[:space:]]*$ ]]; then
                overview_content="$line"
                break
            fi
        done < "$template_file"

        if [[ -n "$overview_content" ]]; then
            description="$overview_content"
        else
            description="Template for $template_name development."
        fi

        # Generate recommended agents based on template key and name
        local recommended_agents="qa-engineer"
        local template_lower=$(echo "$template_key $template_name" | tr '[:upper:]' '[:lower:]')

        for tech in "${!TECH_AGENT_MAP[@]}"; do
            if [[ "$template_lower" =~ $tech ]]; then
                recommended_agents="$recommended_agents, ${TECH_AGENT_MAP[$tech]}"
            fi
        done

        # Remove duplicates and clean up
        recommended_agents=$(echo "$recommended_agents" | tr ',' '\n' | sort -u | tr '\n' ',' | sed 's/,$//' | sed 's/^,//')

        # Populate arrays
        TEMPLATES["$template_key"]="$template_name"
        TEMPLATE_DESCRIPTIONS["$template_key"]="$description"
        TEMPLATE_AGENTS["$template_key"]="$recommended_agents"

        ((template_count++))
    done

    print_status "success" "Discovered $template_count templates"

    if [[ $template_count -eq 0 ]]; then
        print_status "warning" "No templates found in $TEMPLATES_DIR"
        return 1
    fi

    return 0
}

# =============================================================================
# TEMPLATE GENERATION FUNCTIONS
# =============================================================================

show_available_templates() {
    clear
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_TEMPLATE} Available Project Templates:${COLOR_RESET}"
    echo ""

    local i=1
    local template_keys=($(printf '%s\n' "${!TEMPLATES[@]}" | sort))
    for template_key in "${template_keys[@]}"; do
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

    # Read template and substitute variables with error handling
    local content
    if ! content=$(cat "$template_file" 2>/dev/null); then
        print_status "error" "Failed to read template file: $template_file"
        return 1
    fi

    # Validate required variables are set
    if [[ -z "$PROJECT_NAME" || -z "$PROJECT_DESCRIPTION" || -z "$BUSINESS_DOMAIN" || -z "$PROJECT_SCALE" ]]; then
        print_status "error" "Missing required project configuration variables"
        return 1
    fi

    # Variable substitution
    content=${content//\{\{PROJECT_NAME\}\}/$PROJECT_NAME}
    content=${content//\{\{PROJECT_DESCRIPTION\}\}/$PROJECT_DESCRIPTION}
    content=${content//\{\{BUSINESS_DOMAIN\}\}/$BUSINESS_DOMAIN}
    content=${content//\{\{PROJECT_SCALE\}\}/$PROJECT_SCALE}

    # Write to CLAUDE.md with error handling
    if ! echo "$content" > "$output_file" 2>/dev/null; then
        print_status "error" "Failed to write CLAUDE.md file: $output_file"
        return 1
    fi

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

        local choice
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

            local confirm
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

    # Check each template dynamically from scanned TEMPLATES array
    local available_count=0
    local missing_count=0

    # Use sorted template keys for consistent display
    local template_keys=($(printf '%s\n' "${!TEMPLATES[@]}" | sort))

    for template_key in "${template_keys[@]}"; do
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

        local overwrite
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
    echo "${COLOR_YELLOW}[r]${COLOR_RESET} Rescan Templates           ${COLOR_WHITE}- Refresh template list${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}[b]${COLOR_RESET} Back to AI Tools           ${COLOR_WHITE}- Return to main menu${COLOR_RESET}"
    echo "${COLOR_YELLOW}[q]${COLOR_RESET} Quit                       ${COLOR_WHITE}- Exit template manager${COLOR_RESET}"
    echo ""
    echo "${COLOR_CYAN}💡 Tip: Add custom templates by placing .md files in:${COLOR_RESET}"
    echo "   ${COLOR_WHITE}$TEMPLATES_DIR/${COLOR_RESET}"
    echo ""
}

# =============================================================================
# MAIN EXECUTION
# =============================================================================

main() {
    # Initialize templates by scanning directory
    if ! scan_templates; then
        print_status "error" "Failed to scan templates directory"
        exit 1
    fi

    while true; do
        print_header

        # Show dynamic stats
        echo "${COLOR_GREEN}Available Templates:${COLOR_RESET} ${#TEMPLATES[@]}"
        echo "${COLOR_GREEN}Current Directory:${COLOR_RESET} $PROJECT_DIR"
        echo ""

        show_main_menu

        echo -n "${COLOR_BOLD}${ICON_TEMPLATE} Select option: ${COLOR_RESET}"

        local choice
        read -r choice
        echo ""

        case "$choice" in
            "1")
                if check_existing_claude_md; then
                    select_template
                fi
                ;;
            "2")
                show_available_templates
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "3") show_existing_templates ;;
            "r")
                print_status "info" "Rescanning templates directory..."
                scan_templates
                ;;
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