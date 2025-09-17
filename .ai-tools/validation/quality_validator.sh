#!/bin/bash

# =============================================================================
# AUTOMATED QUALITY VALIDATION SYSTEM v1.0.0
# Claude Code Multi-Agent Framework - Framework Health & Quality Checker
# =============================================================================

# set -eE  # Disabled to prevent issues with validation logic

# =============================================================================
# CONFIGURATION
# =============================================================================

readonly SCRIPT_VERSION="1.0.0"
readonly PROJECT_DIR="$(pwd)"
readonly AGENTS_DIR="$PROJECT_DIR/.claude/agents"
readonly PROMPTS_DIR="$PROJECT_DIR/.claude/prompts"
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
readonly ICON_CHECK="✅"
readonly ICON_WARN="⚠️"
readonly ICON_ERROR="❌"
readonly ICON_INFO="ℹ️"
readonly ICON_VALIDATE="🔍"
readonly ICON_HEALTH="💚"

# Validation results
declare -a VALIDATION_RESULTS=()
declare -i TOTAL_CHECKS=0
declare -i PASSED_CHECKS=0
declare -i WARNING_CHECKS=0
declare -i FAILED_CHECKS=0

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

print_header() {
    clear
    echo ""
    echo "${COLOR_BLUE}${COLOR_BOLD}===============================================================================${COLOR_RESET}"
    echo "${COLOR_BLUE}${COLOR_BOLD}${ICON_VALIDATE} AUTOMATED QUALITY VALIDATION SYSTEM v${SCRIPT_VERSION}${COLOR_RESET}"
    echo "${COLOR_CYAN}Framework Health & Quality Assurance${COLOR_RESET}"
    echo "${COLOR_BLUE}${COLOR_BOLD}===============================================================================${COLOR_RESET}"
    echo ""
}

print_status() {
    local status="$1"
    local message="$2"
    case "$status" in
        "pass") echo "${ICON_CHECK} ${COLOR_GREEN}${message}${COLOR_RESET}" ;;
        "warn") echo "${ICON_WARN} ${COLOR_YELLOW}${message}${COLOR_RESET}" ;;
        "fail") echo "${ICON_ERROR} ${COLOR_RED}${message}${COLOR_RESET}" ;;
        "info") echo "${ICON_INFO} ${COLOR_CYAN}${message}${COLOR_RESET}" ;;
        *)      echo "${message}" ;;
    esac
}

record_result() {
    local status="$1"
    local category="$2"
    local message="$3"

    VALIDATION_RESULTS+=("$status|$category|$message")
    ((TOTAL_CHECKS++))

    case "$status" in
        "pass") ((PASSED_CHECKS++)) ;;
        "warn") ((WARNING_CHECKS++)) ;;
        "fail") ((FAILED_CHECKS++)) ;;
    esac
}

validate_check() {
    local description="$1"
    local category="$2"
    local command="$3"

    if eval "$command" >/dev/null 2>&1; then
        print_status "pass" "$description"
        record_result "pass" "$category" "$description"
        return 0
    else
        print_status "fail" "$description"
        record_result "fail" "$category" "$description"
        return 1
    fi
}

validate_warn() {
    local description="$1"
    local category="$2"
    local command="$3"

    if eval "$command" >/dev/null 2>&1; then
        print_status "pass" "$description"
        record_result "pass" "$category" "$description"
        return 0
    else
        print_status "warn" "$description"
        record_result "warn" "$category" "$description"
        return 1
    fi
}

# =============================================================================
# VALIDATION FUNCTIONS
# =============================================================================

validate_directory_structure() {
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_VALIDATE} Validating Directory Structure${COLOR_RESET}"
    echo ""

    validate_check "Framework root directory exists" "structure" "[[ -d '$PROJECT_DIR' ]]"
    validate_check "Agents directory exists" "structure" "[[ -d '$AGENTS_DIR' ]]"
    validate_check "Prompts directory exists" "structure" "[[ -d '$PROMPTS_DIR' ]]"
    validate_check "AI Tools directory exists" "structure" "[[ -d '$PROJECT_DIR/.ai-tools' ]]"
    validate_check "Core agents directory exists" "structure" "[[ -d '$AGENTS_DIR/core' ]]"
    validate_check "Enterprise agents directory exists" "structure" "[[ -d '$AGENTS_DIR/enterprise' ]]"
    validate_check "Custom agents directory exists" "structure" "[[ -d '$AGENTS_DIR/custom' ]]"
    validate_warn "Templates directory exists" "structure" "[[ -d '$TEMPLATES_DIR' ]]"

    echo ""
}

validate_agent_files() {
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_VALIDATE} Validating Agent Files${COLOR_RESET}"
    echo ""

    local agent_count=0
    local valid_agents=0
    local invalid_agents=0

    while IFS= read -r -d '' agent_file; do
        ((agent_count++))
        local agent_name=$(basename "$agent_file" .md)

        # Check YAML header (handle both Unix and Windows line endings)
        if grep -q "^---" "$agent_file" && grep -q "^name:" "$agent_file" && grep -q "^description:" "$agent_file"; then
            ((valid_agents++))
        else
            print_status "fail" "Agent $agent_name missing YAML header"
            record_result "fail" "agents" "Agent $agent_name missing YAML header"
            ((invalid_agents++))
        fi

        # Check for TODO Management section
        if grep -q "## .*TODO.*Management" "$agent_file"; then
            # Valid TODO section found
            :
        else
            print_status "warn" "Agent $agent_name missing TODO Management section"
            record_result "warn" "agents" "Agent $agent_name missing TODO Management section"
        fi

        # Check for CLAUDE.md adaptation
        if grep -q "CLAUDE.md" "$agent_file"; then
            # Valid CLAUDE.md reference found
            :
        else
            print_status "warn" "Agent $agent_name missing CLAUDE.md adaptation"
            record_result "warn" "agents" "Agent $agent_name missing CLAUDE.md adaptation"
        fi

    done < <(find "$AGENTS_DIR" -name "*.md" -type f -print0)

    print_status "info" "Found $agent_count total agents"
    print_status "info" "Valid agents: $valid_agents, Invalid agents: $invalid_agents"
    record_result "pass" "agents" "Agent inventory: $agent_count total, $valid_agents valid"

    echo ""
}

validate_claude_md() {
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_VALIDATE} Validating CLAUDE.md Configuration${COLOR_RESET}"
    echo ""

    local claude_file="$PROJECT_DIR/CLAUDE.md"

    validate_check "CLAUDE.md exists" "config" "[[ -f '$claude_file' ]]"

    if [[ -f "$claude_file" ]]; then
        validate_check "Contains Project Metadata section" "config" "grep -q '## Project Metadata' '$claude_file'"
        validate_check "Contains project_name field" "config" "grep -q 'project_name' '$claude_file'"
        validate_check "Contains Technologies section" "config" "grep -q '## Technologies' '$claude_file'"
        validate_check "Contains Agents and Roles section" "config" "grep -q '## Agents and Roles' '$claude_file'"
        validate_warn "Contains TODO Management section" "config" "grep -q '## TODO Management' '$claude_file'"
        validate_warn "Contains Framework Guidelines section" "config" "grep -q '## Framework Guidelines' '$claude_file'"
    fi

    echo ""
}

validate_ai_tools() {
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_VALIDATE} Validating AI Tools Components${COLOR_RESET}"
    echo ""

    validate_check "AI Tools core directory exists" "ai_tools" "[[ -d '$PROJECT_DIR/.ai-tools/core' ]]"
    validate_check "Project analyzer exists" "ai_tools" "[[ -f '$PROJECT_DIR/.ai-tools/core/bin/project_analyzer.py' ]]"
    validate_check "Agent selector exists" "ai_tools" "[[ -f '$PROJECT_DIR/.ai-tools/core/integration/ai_agent_selector.py' ]]"
    validate_check "Framework wizard exists" "ai_tools" "[[ -f '$PROJECT_DIR/.ai-tools/setup/framework_wizard.sh' ]]"
    validate_check "Agent discovery exists" "ai_tools" "[[ -f '$PROJECT_DIR/.ai-tools/discovery/simple_agent_browser.sh' ]]"
    validate_check "Template manager exists" "ai_tools" "[[ -f '$PROJECT_DIR/.ai-tools/templates/template_manager.sh' ]]"
    validate_check "Main launcher exists" "ai_tools" "[[ -f '$PROJECT_DIR/ai-tools.sh' ]]"

    # Check executability
    validate_check "Framework wizard is executable" "ai_tools" "[[ -x '$PROJECT_DIR/.ai-tools/setup/framework_wizard.sh' ]]"
    validate_check "Agent discovery is executable" "ai_tools" "[[ -x '$PROJECT_DIR/.ai-tools/discovery/simple_agent_browser.sh' ]]"
    validate_check "Template manager is executable" "ai_tools" "[[ -x '$PROJECT_DIR/.ai-tools/templates/template_manager.sh' ]]"
    validate_check "Main launcher is executable" "ai_tools" "[[ -x '$PROJECT_DIR/ai-tools.sh' ]]"

    echo ""
}

validate_template_library() {
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_VALIDATE} Validating Template Library${COLOR_RESET}"
    echo ""

    if [[ -d "$TEMPLATES_DIR" ]]; then
        local template_count=$(find "$TEMPLATES_DIR" -name "*.md" -type f | wc -l)

        if [[ $template_count -gt 0 ]]; then
            print_status "pass" "Template library contains $template_count templates"
            record_result "pass" "templates" "Template library has $template_count templates"

            # Check specific templates
            validate_warn "React template exists" "templates" "[[ -f '$TEMPLATES_DIR/react-app.md' ]]"
            validate_warn "Python template exists" "templates" "[[ -f '$TEMPLATES_DIR/python-app.md' ]]"
            validate_warn "Node.js template exists" "templates" "[[ -f '$TEMPLATES_DIR/node-api.md' ]]"
            validate_warn "Angular template exists" "templates" "[[ -f '$TEMPLATES_DIR/angular-app.md' ]]"
            validate_warn "MERN template exists" "templates" "[[ -f '$TEMPLATES_DIR/fullstack-mern.md' ]]"
        else
            print_status "warn" "Template library is empty"
            record_result "warn" "templates" "Template library is empty"
        fi
    else
        print_status "warn" "Template directory does not exist"
        record_result "warn" "templates" "Template directory missing"
    fi

    echo ""
}

validate_file_consistency() {
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_VALIDATE} Validating File Consistency${COLOR_RESET}"
    echo ""

    # Check for broken symlinks or missing files
    local broken_links=0
    while IFS= read -r -d '' file; do
        if [[ -L "$file" ]] && [[ ! -e "$file" ]]; then
            print_status "fail" "Broken symlink: $file"
            record_result "fail" "consistency" "Broken symlink: $file"
            ((broken_links++))
        fi
    done < <(find "$PROJECT_DIR" -type l -print0 2>/dev/null)

    if [[ $broken_links -eq 0 ]]; then
        print_status "pass" "No broken symlinks found"
        record_result "pass" "consistency" "No broken symlinks found"
    fi

    # Check for duplicate agent names
    local agent_names=($(find "$AGENTS_DIR" -name "*.md" -type f -exec basename {} .md \;))
    local unique_names=($(printf '%s\n' "${agent_names[@]}" | sort -u))

    if [[ ${#agent_names[@]} -eq ${#unique_names[@]} ]]; then
        print_status "pass" "No duplicate agent names found"
        record_result "pass" "consistency" "No duplicate agent names"
    else
        print_status "fail" "Duplicate agent names detected"
        record_result "fail" "consistency" "Duplicate agent names detected"
    fi

    echo ""
}

validate_security() {
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_VALIDATE} Validating Security & Best Practices${COLOR_RESET}"
    echo ""

    # Check for potential security issues
    local security_issues=0

    # Check for hardcoded secrets or API keys (exclude documentation, placeholders, and validation scripts)
    local secret_matches=$(grep -r -i "api[_-]key.*=\|secret.*=\|password.*=\|token.*=" "$PROJECT_DIR" --include="*.md" --include="*.sh" --include="*.py" 2>/dev/null | \
        grep -v "example\|test\|demo\|documentation\|comment\|\$secret\|README\|\.md:" | \
        grep -v "password.*=.*password\|username.*=.*username\|token.*=.*token\|key.*=.*key" | \
        grep -v "placeholder\|sample\|template\|your_\|YOUR_\|<.*>" | \
        grep -v "quality_validator\|validation\|grep.*api\|grep.*secret\|grep.*password" | head -5)

    if [[ -n "$secret_matches" ]]; then
        print_status "warn" "Potential hardcoded secrets found (review manually)"
        record_result "warn" "security" "Potential hardcoded secrets detected"
        echo ""
        echo "${COLOR_YELLOW}Found potential secrets in:${COLOR_RESET}"

        # Use a safer approach to iterate through matches
        while IFS= read -r line; do
            [[ -n "$line" ]] && echo "  ${COLOR_YELLOW}→${COLOR_RESET} $line"
        done <<< "$secret_matches"

        echo ""
        echo "${COLOR_CYAN}${ICON_INFO} Please review these matches to ensure they are not actual secrets${COLOR_RESET}"
        echo ""
        ((security_issues++))
    else
        print_status "pass" "No obvious hardcoded secrets found"
        record_result "pass" "security" "No hardcoded secrets detected"
    fi

    # Check for executable permissions on non-script files (excluding common executable files)
    local wrong_permissions=0
    local wrong_files=()
    while IFS= read -r -d '' file; do
        # Skip script files and common executable extensions
        if [[ -f "$file" ]] && [[ -x "$file" ]] && \
           [[ ! "$file" =~ \\.sh$ ]] && [[ ! "$file" =~ \\.py$ ]] && \
           [[ ! "$file" =~ \\.pl$ ]] && [[ ! "$file" =~ \\.rb$ ]] && \
           [[ ! "$file" =~ \\.js$ ]] && [[ ! "$file" =~ \\.(exe|bin|out)$ ]] && \
           [[ ! "$file" =~ /bin/ ]] && [[ ! "$file" =~ /scripts/ ]]; then
            ((wrong_permissions++))
            wrong_files+=("$file")
        fi
    done < <(find "$PROJECT_DIR" -type f -print0 2>/dev/null)

    if [[ $wrong_permissions -eq 0 ]]; then
        print_status "pass" "File permissions are appropriate"
        record_result "pass" "security" "Appropriate file permissions"
    else
        print_status "warn" "$wrong_permissions files have unexpected executable permissions"
        record_result "warn" "security" "$wrong_permissions files with wrong permissions"
        echo ""
        echo "${COLOR_YELLOW}Files with unexpected executable permissions:${COLOR_RESET}"
        for file in "${wrong_files[@]:0:5}"; do  # Show max 5 files
            echo "  ${COLOR_YELLOW}→${COLOR_RESET} $file"
        done
        [[ ${#wrong_files[@]} -gt 5 ]] && echo "  ${COLOR_YELLOW}→${COLOR_RESET} ... and $((${#wrong_files[@]} - 5)) more files"
        echo ""
        echo "${COLOR_CYAN}${ICON_INFO} Note: On WSL2/Windows systems, file permission warnings are normal due to filesystem differences and do not indicate security issues.${COLOR_RESET}"
        echo ""
    fi

    echo ""
}

# =============================================================================
# REPORTING FUNCTIONS
# =============================================================================

reset_validation_counters() {
    VALIDATION_RESULTS=()
    TOTAL_CHECKS=0
    PASSED_CHECKS=0
    WARNING_CHECKS=0
    FAILED_CHECKS=0
}

generate_summary_report() {
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_HEALTH} VALIDATION SUMMARY REPORT${COLOR_RESET}"
    echo "${COLOR_BLUE}===============================================================================${COLOR_RESET}"
    echo ""

    # Overall health score - prevent division by zero
    local health_score=0
    if [[ $TOTAL_CHECKS -gt 0 ]]; then
        health_score=$((PASSED_CHECKS * 100 / TOTAL_CHECKS))
    fi
    local health_status=""
    local health_color=""

    if [[ $health_score -ge 90 ]]; then
        health_status="EXCELLENT"
        health_color="$COLOR_GREEN"
    elif [[ $health_score -ge 75 ]]; then
        health_status="GOOD"
        health_color="$COLOR_YELLOW"
    elif [[ $health_score -ge 60 ]]; then
        health_status="FAIR"
        health_color="$COLOR_YELLOW"
    else
        health_status="NEEDS ATTENTION"
        health_color="$COLOR_RED"
    fi

    echo "${COLOR_BOLD}Framework Health Score: ${health_color}${health_score}% - ${health_status}${COLOR_RESET}"
    echo ""

    # Statistics
    echo "${COLOR_GREEN}✅ Passed:${COLOR_RESET} $PASSED_CHECKS/$TOTAL_CHECKS checks"
    echo "${COLOR_YELLOW}⚠️ Warnings:${COLOR_RESET} $WARNING_CHECKS/$TOTAL_CHECKS checks"
    echo "${COLOR_RED}❌ Failed:${COLOR_RESET} $FAILED_CHECKS/$TOTAL_CHECKS checks"
    echo ""

    # Category breakdown
    echo "${COLOR_CYAN}${COLOR_BOLD}Results by Category:${COLOR_RESET}"
    echo ""

    local categories=($(printf '%s\n' "${VALIDATION_RESULTS[@]}" | cut -d'|' -f2 | sort -u))

    for category in "${categories[@]}"; do
        local cat_total=0
        local cat_passed=0
        local cat_warned=0
        local cat_failed=0

        for result in "${VALIDATION_RESULTS[@]}"; do
            IFS='|' read -r status cat message <<< "$result"
            if [[ "$cat" == "$category" ]]; then
                ((cat_total++))
                case "$status" in
                    "pass") ((cat_passed++)) ;;
                    "warn") ((cat_warned++)) ;;
                    "fail") ((cat_failed++)) ;;
                esac
            fi
        done

        local cat_score=$((cat_passed * 100 / cat_total))
        printf "  %-15s %3d%% (%d/%d) " "$category" "$cat_score" "$cat_passed" "$cat_total"

        if [[ $cat_failed -gt 0 ]]; then
            echo "${COLOR_RED}${cat_failed} failed${COLOR_RESET}"
        elif [[ $cat_warned -gt 0 ]]; then
            echo "${COLOR_YELLOW}${cat_warned} warnings${COLOR_RESET}"
        else
            echo "${COLOR_GREEN}all passed${COLOR_RESET}"
        fi
    done

    echo ""

    # Recommendations
    echo "${COLOR_CYAN}${COLOR_BOLD}Recommendations:${COLOR_RESET}"
    echo ""

    if [[ $FAILED_CHECKS -gt 0 ]]; then
        echo "• ${COLOR_RED}Address critical failures first${COLOR_RESET}"
        echo "• Review framework structure and ensure all components are properly installed"
    fi

    if [[ $WARNING_CHECKS -gt 0 ]]; then
        echo "• ${COLOR_YELLOW}Review warnings for potential improvements${COLOR_RESET}"
        echo "• Consider implementing recommended best practices"
    fi

    if [[ $health_score -ge 90 ]]; then
        echo "• ${COLOR_GREEN}Framework is in excellent condition${COLOR_RESET}"
        echo "• Continue monitoring with regular validation runs"
    fi

    echo ""
}

show_detailed_report() {
    clear
    echo "${COLOR_CYAN}${COLOR_BOLD}DETAILED VALIDATION RESULTS${COLOR_RESET}"
    echo "${COLOR_BLUE}===============================================================================${COLOR_RESET}"
    echo ""

    local current_category=""

    for result in "${VALIDATION_RESULTS[@]}"; do
        IFS='|' read -r status category message <<< "$result"

        if [[ "$category" != "$current_category" ]]; then
            echo "${COLOR_CYAN}${COLOR_BOLD}$category:${COLOR_RESET}"
            current_category="$category"
        fi

        case "$status" in
            "pass") echo "  ${ICON_CHECK} ${COLOR_GREEN}$message${COLOR_RESET}" ;;
            "warn") echo "  ${ICON_WARN} ${COLOR_YELLOW}$message${COLOR_RESET}" ;;
            "fail") echo "  ${ICON_ERROR} ${COLOR_RED}$message${COLOR_RESET}" ;;
        esac
    done

    echo ""
}

# =============================================================================
# MAIN MENU FUNCTIONS
# =============================================================================

run_full_validation() {
    clear
    print_status "info" "Starting comprehensive framework validation..."
    echo ""

    reset_validation_counters
    validate_directory_structure
    validate_agent_files
    validate_claude_md
    validate_ai_tools
    validate_template_library
    validate_file_consistency
    validate_security

    generate_summary_report
}

run_quick_validation() {
    clear
    print_status "info" "Running quick validation checks..."
    echo ""

    reset_validation_counters
    validate_directory_structure
    validate_claude_md
    validate_ai_tools

    generate_summary_report
}

show_main_menu() {
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_VALIDATE} Validation Options:${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}[1]${COLOR_RESET} Full Validation         ${COLOR_WHITE}- Comprehensive framework health check${COLOR_RESET}"
    echo "${COLOR_YELLOW}[2]${COLOR_RESET} Quick Validation        ${COLOR_WHITE}- Essential components check${COLOR_RESET}"
    echo "${COLOR_YELLOW}[3]${COLOR_RESET} Agent Files Only        ${COLOR_WHITE}- Validate agent definitions${COLOR_RESET}"
    echo "${COLOR_YELLOW}[4]${COLOR_RESET} AI Tools Only           ${COLOR_WHITE}- Validate AI tools components${COLOR_RESET}"
    echo "${COLOR_YELLOW}[5]${COLOR_RESET} Security Check          ${COLOR_WHITE}- Security and best practices audit${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}[r]${COLOR_RESET} Show Detailed Report    ${COLOR_WHITE}- View last validation results${COLOR_RESET}"
    echo "${COLOR_YELLOW}[b]${COLOR_RESET} Back to AI Tools        ${COLOR_WHITE}- Return to main menu${COLOR_RESET}"
    echo "${COLOR_YELLOW}[q]${COLOR_RESET} Quit                    ${COLOR_WHITE}- Exit validation system${COLOR_RESET}"
    echo ""
}

# =============================================================================
# MAIN EXECUTION
# =============================================================================

main() {
    while true; do
        print_header

        # Show framework status
        local total_agents=$(find "$AGENTS_DIR" -name "*.md" -type f 2>/dev/null | wc -l)
        echo "${COLOR_GREEN}Framework Status:${COLOR_RESET}"
        echo "• Agents: $total_agents"
        echo "• Location: $PROJECT_DIR"
        echo ""

        show_main_menu

        echo -n "${COLOR_BOLD}${ICON_VALIDATE} Select option: ${COLOR_RESET}"
        read -r choice
        echo ""

        case "$choice" in
            "1")
                run_full_validation
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "2")
                run_quick_validation
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "3")
                clear
                echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_VALIDATE} Validating Agent Files Only${COLOR_RESET}"
                echo ""
                reset_validation_counters
                validate_agent_files
                generate_summary_report
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "4")
                clear
                echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_VALIDATE} Validating AI Tools Only${COLOR_RESET}"
                echo ""
                reset_validation_counters
                validate_ai_tools
                generate_summary_report
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "5")
                clear
                echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_VALIDATE} Security & Best Practices Check${COLOR_RESET}"
                echo ""
                reset_validation_counters
                validate_security
                generate_summary_report
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "r")
                if [[ ${#VALIDATION_RESULTS[@]} -gt 0 ]]; then
                    show_detailed_report
                    echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                    read -r
                else
                    print_status "warn" "No validation results available. Run a validation first."
                    echo ""
                fi
                ;;
            "b")
                echo "${ICON_CHECK} ${COLOR_GREEN}Returning to AI Tools...${COLOR_RESET}"
                exit 0
                ;;
            "q")
                echo "${ICON_CHECK} ${COLOR_GREEN}Thank you for using Quality Validation!${COLOR_RESET}"
                exit 0
                ;;
            *) print_status "fail" "Invalid option: $choice" ;;
        esac

        echo ""
    done
}

# Check if running in automated mode
if [[ "$1" == "--auto" ]] || [[ "$1" == "-a" ]]; then
    # Run automated validation (non-interactive)
    print_header
    print_status "info" "Running automated framework validation..."
    echo ""

    reset_validation_counters
    validate_directory_structure
    validate_claude_md
    validate_ai_tools

    generate_summary_report

    # Add pause to allow user to read results
    echo ""
    echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
    read -r

    # Exit with proper code based on results
    if [[ $FAILED_CHECKS -gt 0 ]]; then
        exit 1  # Failed checks - error
    elif [[ $WARNING_CHECKS -gt 0 ]]; then
        exit 0  # Only warnings - success
    else
        exit 0  # All passed - success
    fi
else
    # Run main interactive function
    main "$@"
fi