#!/bin/bash

# =============================================================================
# SIMPLE AGENT BROWSER v1.0.0
# Claude Code Multi-Agent Framework - Agent Explorer
# =============================================================================

set -e

# =============================================================================
# CONFIGURATION
# =============================================================================

readonly PROJECT_DIR="$(pwd)"
readonly AGENTS_DIR="$PROJECT_DIR/.claude/agents"

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
readonly ICON_SEARCH="🔍"
readonly ICON_AGENT="🤖"
readonly ICON_CATEGORY="📁"
readonly ICON_INFO="ℹ️"
readonly ICON_SUCCESS="✅"

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

print_header() {
    clear
    echo ""
    echo "${COLOR_BLUE}${COLOR_BOLD}===============================================================================${COLOR_RESET}"
    echo "${COLOR_BLUE}${COLOR_BOLD}${ICON_SEARCH} AGENT DISCOVERY SYSTEM${COLOR_RESET}"
    echo "${COLOR_CYAN}Browse and Explore Available Agents${COLOR_RESET}"
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

show_agent_details() {
    local agent_file="$1"
    local agent_name=$(basename "$agent_file" .md)

    clear
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_AGENT} Agent: $agent_name${COLOR_RESET}"
    echo "${COLOR_YELLOW}Category:${COLOR_RESET} $(dirname "$agent_file" | sed "s|$AGENTS_DIR/||")"
    echo ""

    # Show description from YAML header
    if grep -q "^description:" "$agent_file"; then
        echo "${COLOR_GREEN}Description:${COLOR_RESET}"
        grep "^description:" "$agent_file" | sed 's/^description: //' | fold -s -w 80
        echo ""
    fi

    # Show first few lines of competencies
    if grep -q "## .*Competencies\|## .*Skills\|## .*Capabilities" "$agent_file"; then
        echo "${COLOR_GREEN}Key Competencies:${COLOR_RESET}"
        sed -n '/## .*Competencies\|## .*Skills\|## .*Capabilities/,/^##[^#]/p' "$agent_file" | head -10 | tail -n +2 | head -n -1 | sed 's/^- /• /'
        echo ""
    fi

    # Show technologies if available
    if grep -q -i "technology\|stack\|framework" "$agent_file"; then
        echo "${COLOR_GREEN}Technologies:${COLOR_RESET}"
        grep -i "technology\|stack\|framework" "$agent_file" | head -3 | sed 's/[*#-]//' | sed 's/^  */• /'
        echo ""
    fi
}

search_agents() {
    local query="$1"
    local matches=()

    echo "${COLOR_CYAN}${COLOR_BOLD}Search Results for: '$query'${COLOR_RESET}"
    echo ""

    # Search through all agent files
    while IFS= read -r -d '' file; do
        if grep -q -i "$query" "$file"; then
            matches+=("$file")
        fi
    done < <(find "$AGENTS_DIR" -name "*.md" -type f -print0)

    if [[ ${#matches[@]} -eq 0 ]]; then
        print_status "warning" "No agents found matching '$query'"
        return
    fi

    local i=1
    for match in "${matches[@]}"; do
        local agent_name=$(basename "$match" .md)
        local category=$(dirname "$match" | sed "s|$AGENTS_DIR/||")
        echo "${COLOR_YELLOW}[$i]${COLOR_RESET} ${COLOR_GREEN}$agent_name${COLOR_RESET} ${COLOR_BLUE}($category)${COLOR_RESET}"

        # Show brief description
        if grep -q "^description:" "$match"; then
            local desc=$(grep "^description:" "$match" | sed 's/^description: //' | cut -c1-80)
            echo "    ${COLOR_WHITE}$desc...${COLOR_RESET}"
        fi
        echo ""
        ((i++))
    done

    echo "${COLOR_YELLOW}[s]${COLOR_RESET} New search"
    echo "${COLOR_YELLOW}[b]${COLOR_RESET} Back to main menu"
    echo ""

    echo -n "${COLOR_BOLD}Select agent (1-${#matches[@]}, s, b): ${COLOR_RESET}"
    read -r choice

    if [[ "$choice" == "s" ]]; then
        return
    elif [[ "$choice" == "b" ]]; then
        return
    elif [[ "$choice" =~ ^[0-9]+$ ]] && [[ "$choice" -ge 1 ]] && [[ "$choice" -le "${#matches[@]}" ]]; then
        echo ""
        show_agent_details "${matches[$((choice-1))]}"
        echo ""
        echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
        read -r
    fi
}

browse_by_category() {
    while true; do
        clear
        echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_CATEGORY} Available Categories:${COLOR_RESET}"
        echo ""

        # Get categories
        local categories=($(find "$AGENTS_DIR" -mindepth 1 -type d | sed "s|$AGENTS_DIR/||" | sort))
        local i=1

        for category in "${categories[@]}"; do
            local agent_count=$(find "$AGENTS_DIR/$category" -name "*.md" -type f | wc -l)
            echo "${COLOR_YELLOW}[$i]${COLOR_RESET} $category ${COLOR_WHITE}($agent_count agents)${COLOR_RESET}"
            ((i++))
        done

        echo ""
        echo "${COLOR_YELLOW}[b]${COLOR_RESET} Back to main menu"
        echo ""

        echo -n "${COLOR_BOLD}Select category (1-${#categories[@]}, b): ${COLOR_RESET}"
        read -r choice

        if [[ "$choice" == "b" ]]; then
            break
        elif [[ "$choice" =~ ^[0-9]+$ ]] && [[ "$choice" -ge 1 ]] && [[ "$choice" -le "${#categories[@]}" ]]; then
            show_category_agents "${categories[$((choice-1))]}"
        else
            print_status "error" "Invalid selection"
        fi
        echo ""
    done
}

show_category_agents() {
    local category="$1"

    while true; do
        clear
        echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_CATEGORY} Category: $category${COLOR_RESET}"
        echo ""

        # Get agents in category
        local agents=($(find "$AGENTS_DIR/$category" -name "*.md" -type f | sort))
        local i=1

        for agent_file in "${agents[@]}"; do
            local agent_name=$(basename "$agent_file" .md)
            echo "${COLOR_YELLOW}[$i]${COLOR_RESET} ${COLOR_GREEN}$agent_name${COLOR_RESET}"

            # Show brief description
            if grep -q "^description:" "$agent_file"; then
                local desc=$(grep "^description:" "$agent_file" | sed 's/^description: //' | cut -c1-80)
                echo "    ${COLOR_WHITE}$desc...${COLOR_RESET}"
            fi
            echo ""
            ((i++))
        done

        echo "${COLOR_YELLOW}[b]${COLOR_RESET} Back to categories"
        echo ""

        echo -n "${COLOR_BOLD}Select agent (1-${#agents[@]}, b): ${COLOR_RESET}"
        read -r choice

        if [[ "$choice" == "b" ]]; then
            break
        elif [[ "$choice" =~ ^[0-9]+$ ]] && [[ "$choice" -ge 1 ]] && [[ "$choice" -le "${#agents[@]}" ]]; then
            echo ""
            show_agent_details "${agents[$((choice-1))]}"
            echo ""
            echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
            read -r
        else
            print_status "error" "Invalid selection"
        fi
        echo ""
    done
}

show_all_agents() {
    clear
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_AGENT} All Available Agents${COLOR_RESET}"
    echo ""

    local categories=($(find "$AGENTS_DIR" -mindepth 1 -type d 2>/dev/null | sed "s|$AGENTS_DIR/||" | sort))

    for category in "${categories[@]}"; do
        echo "${COLOR_BLUE}${COLOR_BOLD}${ICON_CATEGORY} $category${COLOR_RESET}"

        local agents=($(find "$AGENTS_DIR/$category" -name "*.md" -type f | sort))
        for agent_file in "${agents[@]}"; do
            local agent_name=$(basename "$agent_file" .md)
            echo "  ${COLOR_GREEN}$agent_name${COLOR_RESET}"
        done
        echo ""
    done

    echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
    read -r
}

show_statistics() {
    clear
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_INFO} Agent Framework Statistics${COLOR_RESET}"
    echo ""

    local total_agents=$(find "$AGENTS_DIR" -name "*.md" -type f | wc -l)
    echo "${COLOR_GREEN}Total Agents:${COLOR_RESET} $total_agents"
    echo ""

    echo "${COLOR_GREEN}Agents by Category:${COLOR_RESET}"
    local categories=($(find "$AGENTS_DIR" -mindepth 1 -type d 2>/dev/null | sed "s|$AGENTS_DIR/||" | sort))

    for category in "${categories[@]}"; do
        local count=$(find "$AGENTS_DIR/$category" -name "*.md" -type f | wc -l)
        printf "  %-20s %s\n" "$category:" "$count agents"
    done

    echo ""
}

interactive_search() {
    while true; do
        clear
        echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_SEARCH} Agent Search${COLOR_RESET}"
        echo ""
        echo "Search by: technology, skill, domain, or agent name"
        echo "Examples: 'react', 'frontend', 'security', 'deployment'"
        echo ""

        echo -n "${COLOR_BOLD}Enter search term (or 'b' to go back): ${COLOR_RESET}"
        read -r query

        if [[ "$query" == "b" ]]; then
            break
        elif [[ -n "$query" ]]; then
            echo ""
            search_agents "$query"
        fi
    done
}

show_main_menu() {
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_SEARCH} Agent Discovery Options:${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}[1]${COLOR_RESET} Browse by Category      ${COLOR_WHITE}- Explore agents by domain${COLOR_RESET}"
    echo "${COLOR_YELLOW}[2]${COLOR_RESET} Search Agents           ${COLOR_WHITE}- Find agents by technology/skill${COLOR_RESET}"
    echo "${COLOR_YELLOW}[3]${COLOR_RESET} Show All Agents         ${COLOR_WHITE}- List all available agents${COLOR_RESET}"
    echo "${COLOR_YELLOW}[4]${COLOR_RESET} Agent Statistics        ${COLOR_WHITE}- Framework agent overview${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}[b]${COLOR_RESET} Back to AI Tools        ${COLOR_WHITE}- Return to main menu${COLOR_RESET}"
    echo "${COLOR_YELLOW}[q]${COLOR_RESET} Quit                    ${COLOR_WHITE}- Exit discovery system${COLOR_RESET}"
    echo ""
}

# =============================================================================
# MAIN EXECUTION
# =============================================================================

main() {
    while true; do
        print_header

        # Show brief framework status
        local total_agents=$(find "$AGENTS_DIR" -name "*.md" -type f 2>/dev/null | wc -l)
        echo "${COLOR_GREEN}Framework Status:${COLOR_RESET}"
        echo "• Agents: $total_agents"
        echo "• Location: $(basename "$AGENTS_DIR")"
        echo ""

        show_main_menu

        echo -n "${COLOR_BOLD}${ICON_SEARCH} Select option: ${COLOR_RESET}"
        read -r choice
        echo ""

        case "$choice" in
            "1") browse_by_category ;;
            "2") interactive_search ;;
            "3") show_all_agents ;;
            "4")
                show_statistics
                echo ""
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "b")
                echo "${ICON_SUCCESS} ${COLOR_GREEN}Returning to AI Tools...${COLOR_RESET}"
                exit 0
                ;;
            "q")
                echo "${ICON_SUCCESS} ${COLOR_GREEN}Thank you for using Agent Discovery!${COLOR_RESET}"
                exit 0
                ;;
            *) print_status "error" "Invalid option: $choice" ;;
        esac

        echo ""
    done
}

# Run main function
main "$@"