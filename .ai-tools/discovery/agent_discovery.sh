#!/bin/bash

# =============================================================================
# AGENT DISCOVERY SYSTEM v1.0.0
# Claude Code Multi-Agent Framework - Intelligent Agent Explorer
# =============================================================================

set -e

# =============================================================================
# CONFIGURATION
# =============================================================================

readonly SCRIPT_VERSION="1.0.0"
readonly PROJECT_DIR="$(pwd)"
readonly AGENTS_DIR="$PROJECT_DIR/.claude/agents"
readonly CACHE_DIR="$PROJECT_DIR/.ai-tools/discovery/cache"
readonly AGENT_INDEX="$CACHE_DIR/agent_index.json"

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
readonly ICON_SKILL="💡"
readonly ICON_INFO="ℹ️"
readonly ICON_SUCCESS="✅"
readonly ICON_BACK="↩️"

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

print_header() {
    clear
    echo ""
    echo "${COLOR_BLUE}${COLOR_BOLD}===============================================================================${COLOR_RESET}"
    echo "${COLOR_BLUE}${COLOR_BOLD}${ICON_SEARCH} AGENT DISCOVERY SYSTEM v${SCRIPT_VERSION}${COLOR_RESET}"
    echo "${COLOR_CYAN}Intelligent Agent Explorer - Claude Code Multi-Agent Framework${COLOR_RESET}"
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

# =============================================================================
# AGENT ANALYSIS FUNCTIONS
# =============================================================================

build_agent_index() {
    print_status "info" "Building agent index..."

    mkdir -p "$CACHE_DIR"
    echo "{" > "$AGENT_INDEX"
    echo "  \"agents\": [" >> "$AGENT_INDEX"

    local first_agent=true

    find "$AGENTS_DIR" -name "*.md" -type f | while read -r agent_file; do
        local agent_name=$(basename "$agent_file" .md)
        local category_path=$(dirname "$agent_file" | sed "s|$AGENTS_DIR/||")
        local category=$(echo "$category_path" | tr '/' '-')

        # Extract description from YAML header and clean it
        local description=""
        if grep -q "^description:" "$agent_file"; then
            description=$(grep "^description:" "$agent_file" | sed 's/^description: //' | tr '"' "'" | tr '\n\r\t' ' ' | sed 's/[[:cntrl:]]//g' | cut -c1-200)
        fi

        # Extract main technologies/skills and clean
        local technologies=""
        if grep -q "technologies\|tech\|stack" "$agent_file"; then
            technologies=$(grep -i "technologies\|tech\|stack" "$agent_file" | head -3 | sed 's/[*#-]//g' | tr '\n\r\t' ' ' | sed 's/[[:cntrl:]]//g' | cut -c1-100)
        fi

        # Extract primary specializations and clean
        local specializations=""
        if grep -q "specializ\|expert\|focus" "$agent_file"; then
            specializations=$(grep -i "specializ\|expert\|focus" "$agent_file" | head -3 | sed 's/[*#-]//g' | tr '\n\r\t' ' ' | sed 's/[[:cntrl:]]//g' | cut -c1-100)
        fi

        if [ "$first_agent" = false ]; then
            echo "," >> "$AGENT_INDEX"
        fi
        first_agent=false

        cat >> "$AGENT_INDEX" << EOF
    {
      "name": "$agent_name",
      "category": "$category",
      "description": "$description",
      "technologies": "$technologies",
      "specializations": "$specializations",
      "file_path": "$agent_file"
    }
EOF
    done

    echo "" >> "$AGENT_INDEX"
    echo "  ]" >> "$AGENT_INDEX"
    echo "}" >> "$AGENT_INDEX"

    print_status "success" "Agent index built successfully"
}

get_agent_categories() {
    if [[ ! -f "$AGENT_INDEX" ]]; then
        build_agent_index
    fi

    python3 -c "
import json
with open('$AGENT_INDEX', 'r') as f:
    data = json.load(f)
categories = sorted(set(agent['category'] for agent in data['agents']))
for cat in categories:
    print(cat)
"
}

get_agents_by_category() {
    local category="$1"

    python3 -c "
import json
with open('$AGENT_INDEX', 'r') as f:
    data = json.load(f)
agents = [agent for agent in data['agents'] if agent['category'] == '$category']
for agent in sorted(agents, key=lambda x: x['name']):
    print(f\"{agent['name']}|{agent['description'][:100]}...\")
"
}

search_agents() {
    local query="$1"

    python3 -c "
import json
query = '$query'.lower()
with open('$AGENT_INDEX', 'r') as f:
    data = json.load(f)

matches = []
for agent in data['agents']:
    score = 0
    # Check name match
    if query in agent['name'].lower():
        score += 10
    # Check description match
    if query in agent['description'].lower():
        score += 5
    # Check technologies match
    if query in agent['technologies'].lower():
        score += 3
    # Check specializations match
    if query in agent['specializations'].lower():
        score += 2

    if score > 0:
        matches.append((agent, score))

# Sort by score descending
matches.sort(key=lambda x: x[1], reverse=True)

for agent, score in matches[:10]:  # Top 10 matches
    print(f\"{agent['name']}|{agent['category']}|{score}|{agent['description'][:80]}...\")
"
}

show_agent_details() {
    local agent_name="$1"

    local agent_file=$(python3 -c "
import json
with open('$AGENT_INDEX', 'r') as f:
    data = json.load(f)
for agent in data['agents']:
    if agent['name'] == '$agent_name':
        print(agent['file_path'])
        break
")

    if [[ -f "$agent_file" ]]; then
        clear
        echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_AGENT} Agent: $agent_name${COLOR_RESET}"
        echo "${COLOR_YELLOW}Category:${COLOR_RESET} $(dirname "$agent_file" | sed "s|$AGENTS_DIR/||")"
        echo "${COLOR_YELLOW}File:${COLOR_RESET} $agent_file"
        echo ""

        # Show description from YAML header
        if grep -q "^description:" "$agent_file"; then
            echo "${COLOR_GREEN}Description:${COLOR_RESET}"
            grep "^description:" "$agent_file" | sed 's/^description: //' | fold -s -w 80
            echo ""
        fi

        # Show main competencies
        echo "${COLOR_GREEN}Core Competencies:${COLOR_RESET}"
        if grep -q "## .*Competencies" "$agent_file"; then
            sed -n '/## .*Competencies/,/^##[^#]/p' "$agent_file" | head -10 | tail -n +2 | head -n -1
        else
            echo "See full agent file for detailed competencies"
        fi
        echo ""

        # Show specializations if available
        if grep -q "## .*Specializations\|## .*Domain" "$agent_file"; then
            echo "${COLOR_GREEN}Specializations:${COLOR_RESET}"
            sed -n '/## .*Specializations\|## .*Domain/,/^##[^#]/p' "$agent_file" | head -8 | tail -n +2 | head -n -1
            echo ""
        fi

    else
        print_status "error" "Agent file not found: $agent_file"
    fi
}

# =============================================================================
# INTERACTIVE MENUS
# =============================================================================

show_main_menu() {
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_SEARCH} Agent Discovery Options:${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}[1]${COLOR_RESET} Browse by Category      ${COLOR_WHITE}- Explore agents by domain${COLOR_RESET}"
    echo "${COLOR_YELLOW}[2]${COLOR_RESET} Search Agents           ${COLOR_WHITE}- Find agents by technology/skill${COLOR_RESET}"
    echo "${COLOR_YELLOW}[3]${COLOR_RESET} Show All Agents         ${COLOR_WHITE}- List all available agents${COLOR_RESET}"
    echo "${COLOR_YELLOW}[4]${COLOR_RESET} Agent Statistics        ${COLOR_WHITE}- Framework agent overview${COLOR_RESET}"
    echo "${COLOR_YELLOW}[5]${COLOR_RESET} Rebuild Index           ${COLOR_WHITE}- Refresh agent database${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}[b]${COLOR_RESET} Back to AI Tools        ${COLOR_WHITE}- Return to main menu${COLOR_RESET}"
    echo "${COLOR_YELLOW}[q]${COLOR_RESET} Quit                    ${COLOR_WHITE}- Exit discovery system${COLOR_RESET}"
    echo ""
}

browse_by_category() {
    while true; do
        clear
        echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_CATEGORY} Available Categories:${COLOR_RESET}"
        echo ""

        local categories=($(get_agent_categories))
        local i=1
        for category in "${categories[@]}"; do
            local agent_count=$(python3 -c "
import json
with open('$AGENT_INDEX', 'r') as f:
    data = json.load(f)
count = len([a for a in data['agents'] if a['category'] == '$category'])
print(count)
")
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

        local agents_info=$(get_agents_by_category "$category")
        local agents=()
        local i=1

        while IFS='|' read -r agent_name agent_desc; do
            if [[ -n "$agent_name" ]]; then
                agents+=("$agent_name")
                echo "${COLOR_YELLOW}[$i]${COLOR_RESET} ${COLOR_GREEN}$agent_name${COLOR_RESET}"
                echo "    ${COLOR_WHITE}$agent_desc${COLOR_RESET}"
                echo ""
                ((i++))
            fi
        done <<< "$agents_info"

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
            echo "${COLOR_CYAN}${COLOR_BOLD}Search Results for: '$query'${COLOR_RESET}"
            echo ""

            local search_results=$(search_agents "$query")
            if [[ -n "$search_results" ]]; then
                local agents=()
                local i=1

                while IFS='|' read -r agent_name category score description; do
                    if [[ -n "$agent_name" ]]; then
                        agents+=("$agent_name")
                        echo "${COLOR_YELLOW}[$i]${COLOR_RESET} ${COLOR_GREEN}$agent_name${COLOR_RESET} ${COLOR_BLUE}($category)${COLOR_RESET} ${COLOR_MAGENTA}[score: $score]${COLOR_RESET}"
                        echo "    ${COLOR_WHITE}$description${COLOR_RESET}"
                        echo ""
                        ((i++))
                    fi
                done <<< "$search_results"

                echo "${COLOR_YELLOW}[s]${COLOR_RESET} New search"
                echo "${COLOR_YELLOW}[b]${COLOR_RESET} Back to main menu"
                echo ""

                echo -n "${COLOR_BOLD}Select agent (1-${#agents[@]}, s, b): ${COLOR_RESET}"
                read -r choice

                if [[ "$choice" == "s" ]]; then
                    continue
                elif [[ "$choice" == "b" ]]; then
                    break
                elif [[ "$choice" =~ ^[0-9]+$ ]] && [[ "$choice" -ge 1 ]] && [[ "$choice" -le "${#agents[@]}" ]]; then
                    echo ""
                    show_agent_details "${agents[$((choice-1))]}"
                    echo ""
                    echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                    read -r
                fi
            else
                print_status "warning" "No agents found matching '$query'"
                echo ""
            fi
        fi
    done
}

show_all_agents() {
    clear
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_AGENT} All Available Agents${COLOR_RESET}"
    echo ""

    local categories=($(get_agent_categories))
    for category in "${categories[@]}"; do
        echo "${COLOR_BLUE}${COLOR_BOLD}${ICON_CATEGORY} $category${COLOR_RESET}"

        local agents_info=$(get_agents_by_category "$category")
        while IFS='|' read -r agent_name agent_desc; do
            if [[ -n "$agent_name" ]]; then
                echo "  ${COLOR_GREEN}$agent_name${COLOR_RESET} - ${COLOR_WHITE}$agent_desc${COLOR_RESET}"
            fi
        done <<< "$agents_info"
        echo ""
    done

    echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
    read -r
}

show_statistics() {
    clear
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_INFO} Agent Framework Statistics${COLOR_RESET}"
    echo ""

    local total_agents=$(python3 -c "
import json
with open('$AGENT_INDEX', 'r') as f:
    data = json.load(f)
print(len(data['agents']))
")

    echo "${COLOR_GREEN}Total Agents:${COLOR_RESET} $total_agents"
    echo ""

    echo "${COLOR_GREEN}Agents by Category:${COLOR_RESET}"
    local categories=($(get_agent_categories))
    for category in "${categories[@]}"; do
        local count=$(python3 -c "
import json
with open('$AGENT_INDEX', 'r') as f:
    data = json.load(f)
count = len([a for a in data['agents'] if a['category'] == '$category'])
print(count)
")
        printf "  %-20s %s\n" "$category:" "$count agents"
    done

    echo ""
    echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
    read -r
}

# =============================================================================
# MAIN EXECUTION
# =============================================================================

main() {
    # Build initial index if needed
    if [[ ! -f "$AGENT_INDEX" ]]; then
        build_agent_index
    fi

    while true; do
        print_header
        show_statistics
        echo ""
        show_main_menu

        echo -n "${COLOR_BOLD}${ICON_SEARCH} Select option: ${COLOR_RESET}"
        read -r choice
        echo ""

        case "$choice" in
            "1") browse_by_category ;;
            "2") interactive_search ;;
            "3") show_all_agents ;;
            "4") show_statistics ;;
            "5") build_agent_index ;;
            "b") exit 0 ;;
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