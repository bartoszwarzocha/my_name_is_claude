#!/bin/bash

# =============================================================================
# AI TOOLS LAUNCHER v1.0.0
# Claude Code Multi-Agent Framework - AI-Powered Development Tools
# =============================================================================

set -e

# =============================================================================
# CORE CONFIGURATION
# =============================================================================

# Version and metadata
readonly SCRIPT_VERSION="1.0.0"
readonly FRAMEWORK_VERSION="3.1.0"
readonly SCRIPT_NAME="AI Tools Launcher"

# Paths and directories
readonly PROJECT_DIR="$(pwd)"
readonly PROJECT_NAME="$(basename "$PROJECT_DIR")"
readonly AI_TOOLS_DIR="$PROJECT_DIR/.ai-tools"
readonly AI_CORE_DIR="$AI_TOOLS_DIR/core"
readonly VENV_PATH="$AI_TOOLS_DIR/venv"
readonly PROJECT_ANALYZER="$AI_CORE_DIR/bin/project_analyzer.py"
readonly FRAMEWORK_WIZARD="$AI_TOOLS_DIR/setup/framework_wizard.sh"
readonly AGENT_DISCOVERY="$AI_TOOLS_DIR/discovery/simple_agent_browser.sh"
readonly TEMPLATE_MANAGER="$AI_TOOLS_DIR/templates/template_manager.sh"
readonly QUALITY_VALIDATOR="$AI_TOOLS_DIR/validation/quality_validator.sh"

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
readonly ICON_BRAIN="🧠"
readonly ICON_TARGET="🎯"
readonly ICON_LIGHTNING="⚡"
readonly ICON_ROBOT="🤖"
readonly ICON_MAGNIFYING="🔍"
readonly ICON_WIZARD="🧙"
readonly ICON_DISCOVER="🔍"
readonly ICON_TEMPLATES="📋"
readonly ICON_QUALITY="🔍"

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

print_header() {
    clear
    echo ""
    echo "${COLOR_BLUE}${COLOR_BOLD}===============================================================================${COLOR_RESET}"
    echo "${COLOR_BLUE}${COLOR_BOLD}${ICON_BRAIN} AI TOOLS LAUNCHER v${SCRIPT_VERSION}${COLOR_RESET}"
    echo "${COLOR_CYAN}Claude Code Multi-Agent Framework - AI-Powered Development Tools${COLOR_RESET}"
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

setup_virtual_environment() {
    print_status "info" "Setting up AI Tools virtual environment..."
    echo ""

    # Check if python3-venv is available (Ubuntu/Debian requirement)
    if ! python3 -c "import venv" 2>/dev/null; then
        print_status "error" "Python venv module not available"
        echo ""
        echo "${COLOR_YELLOW}${COLOR_BOLD}SOLUTION:${COLOR_RESET}"
        if command -v apt >/dev/null 2>&1; then
            echo "  ${COLOR_GREEN}Install python3-venv:${COLOR_RESET}"
            echo "     ${COLOR_WHITE}sudo apt update && sudo apt install python3-venv python3-pip${COLOR_RESET}"
        else
            echo "  ${COLOR_GREEN}Install Python virtual environment support for your system${COLOR_RESET}"
        fi
        return 1
    fi

    # Create virtual environment
    print_status "info" "Creating virtual environment..."
    if python3 -m venv "$VENV_PATH" --system-site-packages; then
        print_status "success" "Virtual environment created at $VENV_PATH"
    else
        print_status "error" "Failed to create virtual environment"
        echo ""
        echo "${COLOR_YELLOW}${COLOR_BOLD}TROUBLESHOOTING:${COLOR_RESET}"
        echo "  ${COLOR_GREEN}Option 1 - Install missing packages:${COLOR_RESET}"
        echo "     ${COLOR_WHITE}sudo apt update && sudo apt install python3-venv python3-pip${COLOR_RESET}"
        echo "  ${COLOR_GREEN}Option 2 - Try without system packages:${COLOR_RESET}"
        echo "     ${COLOR_WHITE}python3 -m venv $VENV_PATH${COLOR_RESET}"
        return 1
    fi

    # Ensure pip is available in virtual environment
    print_status "info" "Setting up pip in virtual environment..."
    if ! [[ -f "$VENV_PATH/bin/pip" ]]; then
        "$VENV_PATH/bin/python" -m ensurepip --upgrade 2>/dev/null || {
            print_status "warning" "ensurepip failed, trying get-pip.py..."
            curl -s https://bootstrap.pypa.io/get-pip.py | "$VENV_PATH/bin/python" || {
                print_status "error" "Failed to install pip in virtual environment"
                return 1
            }
        }
    fi

    # Verify pip installation
    if [[ -f "$VENV_PATH/bin/pip" ]]; then
        print_status "success" "Pip available in virtual environment"
    else
        print_status "error" "Pip not found in virtual environment"
        return 1
    fi

    # Install dependencies using virtual environment pip
    print_status "info" "Installing AI Tools dependencies..."
    echo "  ${COLOR_CYAN}Installing: numpy pandas scikit-learn requests scipy joblib${COLOR_RESET}"

    # Try installation with progress feedback
    if "$VENV_PATH/bin/pip" install --quiet --upgrade pip setuptools wheel; then
        print_status "success" "Updated pip and build tools"
    else
        print_status "warning" "Failed to update pip, continuing..."
    fi

    if "$VENV_PATH/bin/pip" install numpy pandas scikit-learn requests scipy joblib; then
        print_status "success" "All dependencies installed successfully"
        echo ""
        print_status "info" "Verifying installations..."

        # Quick verification
        if "$VENV_PATH/bin/python" -c "import numpy, pandas, sklearn, requests, scipy, joblib; print('✅ All imports successful')" 2>/dev/null; then
            print_status "success" "All dependencies verified working"
            return 0
        else
            print_status "warning" "Some dependencies may not be working correctly"
            return 0
        fi
    else
        print_status "error" "Failed to install some dependencies"
        echo ""
        echo "${COLOR_YELLOW}${COLOR_BOLD}ALTERNATIVE SOLUTIONS:${COLOR_RESET}"
        echo "  ${COLOR_GREEN}Option 1 - Use system packages:${COLOR_RESET}"
        echo "     ${COLOR_WHITE}sudo apt install python3-numpy python3-pandas python3-sklearn python3-scipy${COLOR_RESET}"
        echo "  ${COLOR_GREEN}Option 2 - Manual installation:${COLOR_RESET}"
        echo "     ${COLOR_WHITE}$VENV_PATH/bin/pip install --user numpy pandas scikit-learn${COLOR_RESET}"
        echo "  ${COLOR_GREEN}Option 3 - Continue without ML features:${COLOR_RESET}"
        echo "     ${COLOR_WHITE}AI Tools will work in fallback mode${COLOR_RESET}"
        return 1
    fi
}

show_manual_setup_guide() {
    clear
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_INFO} AI Tools Manual Setup Guide${COLOR_RESET}"
    echo "=========================================="
    echo ""
    echo "${COLOR_GREEN}${COLOR_BOLD}Quick Setup (Recommended):${COLOR_RESET}"
    echo "  ${COLOR_WHITE}1. Run: ./ai-tools.sh${COLOR_RESET}"
    echo "  ${COLOR_WHITE}2. Answer 'y' when asked to create virtual environment${COLOR_RESET}"
    echo "  ${COLOR_WHITE}3. Wait for automatic installation to complete${COLOR_RESET}"
    echo ""
    echo "${COLOR_GREEN}${COLOR_BOLD}Manual Setup Steps:${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}Step 1: Install system requirements (Ubuntu/WSL)${COLOR_RESET}"
    echo "  ${COLOR_WHITE}sudo apt update${COLOR_RESET}"
    echo "  ${COLOR_WHITE}sudo apt install python3-venv python3-pip python3-dev${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}Step 2: Create virtual environment${COLOR_RESET}"
    echo "  ${COLOR_WHITE}python3 -m venv $VENV_PATH${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}Step 3: Activate virtual environment${COLOR_RESET}"
    echo "  ${COLOR_WHITE}source $VENV_PATH/bin/activate${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}Step 4: Install AI Tools dependencies${COLOR_RESET}"
    echo "  ${COLOR_WHITE}pip install numpy pandas scikit-learn requests scipy joblib${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}Step 5: Test installation${COLOR_RESET}"
    echo "  ${COLOR_WHITE}./ai-tools.sh${COLOR_RESET}"
    echo ""
    echo "${COLOR_GREEN}${COLOR_BOLD}Alternative: System packages (faster but less isolated)${COLOR_RESET}"
    echo "  ${COLOR_WHITE}sudo apt install python3-numpy python3-pandas python3-sklearn python3-scipy${COLOR_RESET}"
    echo ""
    echo "${COLOR_GREEN}${COLOR_BOLD}Troubleshooting:${COLOR_RESET}"
    echo "  ${COLOR_CYAN}• If 'externally-managed-environment' error:${COLOR_RESET}"
    echo "    ${COLOR_WHITE}Always use virtual environment or system packages${COLOR_RESET}"
    echo "  ${COLOR_CYAN}• If pip missing in venv:${COLOR_RESET}"
    echo "    ${COLOR_WHITE}$VENV_PATH/bin/python -m ensurepip --upgrade${COLOR_RESET}"
    echo "  ${COLOR_CYAN}• If WSL performance issues:${COLOR_RESET}"
    echo "    ${COLOR_WHITE}Consider using system packages for faster startup${COLOR_RESET}"
    echo ""
}

activate_venv_if_available() {
    # Check if virtual environment exists and is properly configured
    if [[ -f "$VENV_PATH/bin/activate" ]] && [[ -f "$VENV_PATH/bin/pip" ]]; then
        print_status "info" "Activating AI Tools virtual environment..."
        source "$VENV_PATH/bin/activate"
        print_status "success" "Virtual environment activated: $(python --version)"
        return 0
    elif [[ -f "$VENV_PATH/bin/activate" ]] && [[ ! -f "$VENV_PATH/bin/pip" ]]; then
        print_status "warning" "Virtual environment exists but is incomplete (missing pip)"
        echo ""
        echo "${COLOR_BOLD}${COLOR_YELLOW}Repair Options:${COLOR_RESET}"
        echo "  ${COLOR_GREEN}[y]${COLOR_RESET} Recreate virtual environment (recommended)"
        echo "  ${COLOR_GREEN}[r]${COLOR_RESET} Try to repair existing environment"
        echo "  ${COLOR_GREEN}[m]${COLOR_RESET} Show manual setup guide"
        echo "  ${COLOR_GREEN}[s]${COLOR_RESET} Skip and continue in fallback mode"
        echo "  ${COLOR_GREEN}[q]${COLOR_RESET} Quit"
        echo ""
        read -p "Choose option (y/r/m/s/q): " -r

        case "$REPLY" in
            [Yy]*)
                print_status "info" "Removing broken virtual environment..."
                rm -rf "$VENV_PATH"
                setup_virtual_environment
                return $?
                ;;
            [Rr]*)
                print_status "info" "Attempting to repair virtual environment..."
                "$VENV_PATH/bin/python" -m ensurepip --upgrade || {
                    print_status "error" "Repair failed. Recreating environment..."
                    rm -rf "$VENV_PATH"
                    setup_virtual_environment
                    return $?
                }
                if [[ -f "$VENV_PATH/bin/pip" ]]; then
                    print_status "success" "Virtual environment repaired"
                    source "$VENV_PATH/bin/activate"
                    return 0
                else
                    print_status "error" "Repair failed. Please recreate environment."
                    return 1
                fi
                ;;
            [Mm]*)
                show_manual_setup_guide
                echo ""
                read -p "Press Enter to return to main menu..." -r
                return 1
                ;;
            [Ss]*)
                print_status "info" "Continuing in fallback mode (limited AI features)"
                return 1
                ;;
            [Qq]*)
                print_status "info" "Exiting AI Tools"
                exit 0
                ;;
            *)
                print_status "info" "Invalid option. Continuing in fallback mode."
                return 1
                ;;
        esac
    else
        print_status "warning" "Virtual environment not found at $VENV_PATH"
        echo ""
        echo "${COLOR_BOLD}${COLOR_YELLOW}Setup Options:${COLOR_RESET}"
        echo "  ${COLOR_GREEN}[y]${COLOR_RESET} Automatic setup (recommended)"
        echo "  ${COLOR_GREEN}[m]${COLOR_RESET} Show manual setup guide"
        echo "  ${COLOR_GREEN}[s]${COLOR_RESET} Skip and continue in fallback mode"
        echo "  ${COLOR_GREEN}[q]${COLOR_RESET} Quit"
        echo ""
        read -p "Choose option (y/m/s/q): " -r

        case "$REPLY" in
            [Yy]*)
                setup_virtual_environment
                return $?
                ;;
            [Mm]*)
                show_manual_setup_guide
                echo ""
                read -p "Press Enter to return to main menu..." -r
                return 1
                ;;
            [Ss]*)
                print_status "info" "Continuing in fallback mode (limited AI features)"
                return 1
                ;;
            [Qq]*)
                print_status "info" "Exiting AI Tools"
                exit 0
                ;;
            *)
                print_status "info" "Invalid option. Continuing in fallback mode."
                return 1
                ;;
        esac
    fi
}

check_dependencies() {
    local missing_system_deps=()
    local missing_python_deps=()
    local needs_sudo=false
    local has_problems=false

    print_status "info" "Checking AI Tools dependencies..."

    # Try to activate venv first
    activate_venv_if_available

    # Check Python
    if ! command -v python3 >/dev/null 2>&1; then
        missing_system_deps+=("python3")
    fi

    # Check pip
    if ! command -v pip3 >/dev/null 2>&1; then
        missing_system_deps+=("python3-pip")
    fi

    # Check AI Tools directory
    if [[ ! -d "$AI_TOOLS_DIR" ]]; then
        print_status "error" "AI Tools directory not found: $AI_TOOLS_DIR"
        echo "Please ensure you're running this from the framework root directory."
        has_problems=true
    fi

    # Check core components
    if [[ ! -f "$PROJECT_ANALYZER" ]]; then
        print_status "error" "Project analyzer not found: $PROJECT_ANALYZER"
        has_problems=true
    fi

    # Check Python ML dependencies with loading message
    print_status "info" "Please wait... Testing Python ML dependencies..."
    local ml_deps=("numpy" "pandas" "scikit-learn" "scipy" "joblib")
    for dep in "${ml_deps[@]}"; do
        # Handle special case for scikit-learn (imports as sklearn)
        local import_name="$dep"
        if [[ "$dep" == "scikit-learn" ]]; then
            import_name="sklearn"
        else
            import_name="${dep//-/_}"
        fi

        if ! python3 -c "import ${import_name}" 2>/dev/null; then
            missing_python_deps+=("$dep")
        fi
    done

    # Report status
    if [[ ${#missing_system_deps[@]} -gt 0 ]]; then
        print_status "error" "Missing system dependencies: ${missing_system_deps[*]}"

        # Suggest installation based on system
        if command -v apt >/dev/null 2>&1; then
            echo "${COLOR_YELLOW}Suggested fix:${COLOR_RESET} sudo apt update && sudo apt install ${missing_system_deps[*]}"
            needs_sudo=true
        elif command -v yum >/dev/null 2>&1; then
            echo "${COLOR_YELLOW}Suggested fix:${COLOR_RESET} sudo yum install ${missing_system_deps[*]}"
            needs_sudo=true
        elif command -v brew >/dev/null 2>&1; then
            echo "${COLOR_YELLOW}Suggested fix:${COLOR_RESET} brew install python3"
        fi
        echo ""
        has_problems=true
    fi

    if [[ ${#missing_python_deps[@]} -gt 0 ]]; then
        print_status "warning" "Missing Python ML dependencies: ${missing_python_deps[*]}"
        echo "${COLOR_YELLOW}AI Tools will run in fallback mode without these dependencies.${COLOR_RESET}"
        echo ""
        echo "${COLOR_CYAN}${COLOR_BOLD}RECOMMENDED: Use AI Tools virtual environment${COLOR_RESET}"
        if [[ -f "$VENV_PATH/bin/activate" ]]; then
            echo "  ${COLOR_GREEN}1. Activate virtual environment:${COLOR_RESET}"
            echo "     ${COLOR_WHITE}source $VENV_PATH/bin/activate${COLOR_RESET}"
            echo "  ${COLOR_GREEN}2. Install dependencies:${COLOR_RESET}"
            echo "     ${COLOR_WHITE}pip install ${missing_python_deps[*]}${COLOR_RESET}"
            echo "  ${COLOR_GREEN}3. Run AI Tools again:${COLOR_RESET}"
            echo "     ${COLOR_WHITE}./ai-tools.sh${COLOR_RESET}"
        else
            echo "  ${COLOR_GREEN}1. Create virtual environment:${COLOR_RESET}"
            echo "     ${COLOR_WHITE}python3 -m venv $VENV_PATH${COLOR_RESET}"
            echo "  ${COLOR_GREEN}2. Activate and install:${COLOR_RESET}"
            echo "     ${COLOR_WHITE}source $VENV_PATH/bin/activate && pip install ${missing_python_deps[*]}${COLOR_RESET}"
        fi
        echo ""
        echo "${COLOR_YELLOW}${COLOR_BOLD}ALTERNATIVE METHODS:${COLOR_RESET}"
        echo "  ${COLOR_CYAN}System packages (Ubuntu/Debian):${COLOR_RESET}"
        echo "     ${COLOR_WHITE}sudo apt update && sudo apt install python3-numpy python3-pandas python3-sklearn python3-scipy${COLOR_RESET}"
        echo "  ${COLOR_CYAN}User installation (if allowed):${COLOR_RESET}"
        echo "     ${COLOR_WHITE}pip3 install --user ${missing_python_deps[*]}${COLOR_RESET}"
        echo "  ${COLOR_CYAN}Force installation (not recommended):${COLOR_RESET}"
        echo "     ${COLOR_WHITE}pip3 install --break-system-packages ${missing_python_deps[*]}${COLOR_RESET}"

        echo ""
        print_status "info" "Continuing with rule-based AI (fallback mode)..."
        has_problems=true
    fi

    # If critical problems detected, require user acknowledgment
    if [[ "$has_problems" == true ]]; then
        echo ""
        echo "${COLOR_BOLD}${COLOR_YELLOW}Options:${COLOR_RESET}"
        echo "  ${COLOR_GREEN}[Enter]${COLOR_RESET} Continue to main menu"
        echo "  ${COLOR_RED}[Esc]${COLOR_RESET}   Exit AI Tools"
        echo ""
        echo -n "${COLOR_BOLD}${COLOR_YELLOW}Choose action: ${COLOR_RESET}"

        # Read single character without waiting for Enter
        read -rsn1 key

        # Handle escape sequence (Esc key sends ^[ which is \x1b)
        if [[ "$key" == $'\x1b' ]]; then
            echo ""
            echo "${COLOR_RED}${ICON_ERROR} Exiting due to dependency issues...${COLOR_RESET}"
            exit 1
        elif [[ "$key" == "" ]]; then
            # Enter key was pressed
            echo ""
            echo "${COLOR_GREEN}${ICON_SUCCESS} Continuing to main menu...${COLOR_RESET}"
        else
            # Any other key - treat as Enter
            echo ""
            echo "${COLOR_GREEN}${ICON_SUCCESS} Continuing to main menu...${COLOR_RESET}"
        fi
    fi

    if [[ ${#missing_system_deps[@]} -eq 0 && ${#missing_python_deps[@]} -eq 0 ]]; then
        print_status "success" "All dependencies found - Full AI capabilities enabled!"
    fi
}

detect_project_type() {
    local project_path="${1:-$PROJECT_DIR}"

    # Quick technology detection
    local frontend=""
    local backend=""

    if [[ -f "$project_path/package.json" ]]; then
        if grep -q "react" "$project_path/package.json" 2>/dev/null; then
            frontend="React"
        elif grep -q "angular" "$project_path/package.json" 2>/dev/null; then
            frontend="Angular"
        elif grep -q "vue" "$project_path/package.json" 2>/dev/null; then
            frontend="Vue.js"
        fi
        backend="Node.js"
    fi

    if [[ -f "$project_path/requirements.txt" || -f "$project_path/pyproject.toml" ]]; then
        backend="Python"
    fi

    if [[ -f "$project_path/pom.xml" ]]; then
        backend="Java"
    fi

    if [[ -f "$project_path/Cargo.toml" ]]; then
        backend="Rust"
    fi

    echo "$frontend${frontend:+/}$backend"
}

# =============================================================================
# CORE AI TOOLS FUNCTIONS
# =============================================================================

run_project_analysis() {
    local target_path="${1:-$PROJECT_DIR}"

    clear
    print_status "info" "Analyzing project: $target_path"
    echo ""

    # Add AI tools to Python path and run analyzer
    export PYTHONPATH="$AI_TOOLS_DIR:$PYTHONPATH"

    if python3 "$PROJECT_ANALYZER" "$target_path"; then
        print_status "success" "Project analysis completed"
    else
        print_status "error" "Project analysis failed"
        return 1
    fi
}

run_technology_detection() {
    local target_path="${1:-$PROJECT_DIR}"

    clear
    print_status "info" "Detecting technologies in: $target_path"
    echo ""

    export PYTHONPATH="$AI_TOOLS_DIR:$PYTHONPATH"

    python3 -c "
import sys
sys.path.insert(0, '$AI_TOOLS_DIR')
from core.core.simple_technology_detector import SimpleTechnologyDetector

detector = SimpleTechnologyDetector()
tech_stack = detector.detect_technology_stack('$target_path')

print('${COLOR_CYAN}Technology Stack Detection Results:${COLOR_RESET}')
print('=' * 50)
print(f'${COLOR_GREEN}Frontend:${COLOR_RESET} {tech_stack.frontend[:5]}')  # Show first 5
print(f'${COLOR_GREEN}Backend:${COLOR_RESET} {tech_stack.backend[:5]}')
print(f'${COLOR_GREEN}Database:${COLOR_RESET} {tech_stack.database[:3]}')
print(f'${COLOR_GREEN}Infrastructure:${COLOR_RESET} {tech_stack.infrastructure[:3]}')
print(f'${COLOR_GREEN}Confidence:${COLOR_RESET} {tech_stack.confidence_score:.2f}')
"

    if [[ $? -eq 0 ]]; then
        print_status "success" "Technology detection completed"
    else
        print_status "error" "Technology detection failed"
        return 1
    fi
}

run_agent_recommendations() {
    local target_path="${1:-$PROJECT_DIR}"

    clear
    print_status "info" "Generating agent recommendations for: $target_path"
    echo ""

    export PYTHONPATH="$AI_TOOLS_DIR:$PYTHONPATH"

    python3 -c "
import sys
sys.path.insert(0, '$AI_TOOLS_DIR')
from core.integration.simple_agent_selector import SimpleAgentSelector as AgentSelectionEngine, AgentSelectionRequest

try:
    selector = AgentSelectionEngine('$target_path')
    request = AgentSelectionRequest(project_path='$target_path', max_agents=8)
    response = selector.select_agents(request)

    print('${COLOR_CYAN}AI Agent Recommendations:${COLOR_RESET}')
    print('=' * 50)

    for i, agent in enumerate(response.recommended_agents, 1):
        print(f'${COLOR_GREEN}{i}.${COLOR_RESET} {agent}')

    if hasattr(response, 'reasoning'):
        print(f'\\n${COLOR_YELLOW}Selection Method:${COLOR_RESET} Rule-based (fallback)')

except Exception as e:
    print(f'${COLOR_RED}Error: {e}${COLOR_RESET}')
"

    if [[ $? -eq 0 ]]; then
        print_status "success" "Agent recommendations completed"
    else
        print_status "error" "Agent recommendations failed"
        return 1
    fi
}

run_tutorial() {
    clear
    print_status "info" "Running AI Tools tutorial"
    echo ""

    if [[ -f "$AI_CORE_DIR/demo/tutorial_basic.py" ]]; then
        python3 "$AI_CORE_DIR/demo/tutorial_basic.py"
        print_status "success" "Tutorial completed"
    else
        print_status "error" "Tutorial not found"
        return 1
    fi
}

run_framework_setup() {
    clear
    print_status "info" "Starting Interactive Framework Setup Wizard"
    echo ""

    if [[ -f "$FRAMEWORK_WIZARD" ]]; then
        if bash "$FRAMEWORK_WIZARD"; then
            print_status "success" "Framework setup completed"
        else
            print_status "error" "Framework setup failed"
            return 1
        fi
    else
        print_status "error" "Framework setup wizard not found: $FRAMEWORK_WIZARD"
        return 1
    fi
}

run_agent_discovery() {
    clear
    print_status "info" "Starting Agent Discovery System"
    echo ""

    if [[ -f "$AGENT_DISCOVERY" ]]; then
        if bash "$AGENT_DISCOVERY"; then
            print_status "success" "Agent discovery completed"
        else
            print_status "error" "Agent discovery failed"
            return 1
        fi
    else
        print_status "error" "Agent discovery system not found: $AGENT_DISCOVERY"
        return 1
    fi
}

run_template_manager() {
    clear
    print_status "info" "Starting Quick Start Template Manager"
    echo ""

    if [[ -f "$TEMPLATE_MANAGER" ]]; then
        if bash "$TEMPLATE_MANAGER"; then
            print_status "success" "Template generation completed"
        else
            print_status "error" "Template generation failed"
            return 1
        fi
    else
        print_status "error" "Template manager not found: $TEMPLATE_MANAGER"
        return 1
    fi
}

run_quality_validation() {
    clear
    print_status "info" "Starting Automated Quality Validation"
    echo ""

    if [[ -f "$QUALITY_VALIDATOR" ]]; then
        # Launch interactive validation menu
        bash "$QUALITY_VALIDATOR"
        print_status "success" "Quality validation completed"
    else
        print_status "error" "Quality validator not found: $QUALITY_VALIDATOR"
        return 1
    fi
}

show_system_status() {
    clear
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_TARGET} AI Tools System Status${COLOR_RESET}"
    echo "================================"
    echo ""

    # Framework info
    echo "${COLOR_GREEN}Framework:${COLOR_RESET} Claude Code Multi-Agent Framework v$FRAMEWORK_VERSION"
    echo "${COLOR_GREEN}AI Tools:${COLOR_RESET} v$SCRIPT_VERSION"
    echo "${COLOR_GREEN}Project:${COLOR_RESET} $PROJECT_NAME"

    # Quick project detection
    local project_type=$(detect_project_type)
    if [[ -n "$project_type" ]]; then
        echo "${COLOR_GREEN}Detected:${COLOR_RESET} $project_type"
    fi

    echo ""

    # Check components
    local status_ok=true

    if [[ -d "$AI_TOOLS_DIR" ]]; then
        print_status "success" "AI Tools directory found"
    else
        print_status "error" "AI Tools directory missing"
        status_ok=false
    fi

    if [[ -f "$PROJECT_ANALYZER" ]]; then
        print_status "success" "Project analyzer available"
    else
        print_status "error" "Project analyzer missing"
        status_ok=false
    fi

    if [[ -f "$FRAMEWORK_WIZARD" ]]; then
        print_status "success" "Framework setup wizard available"
    else
        print_status "error" "Framework setup wizard missing"
        status_ok=false
    fi

    if [[ -f "$AGENT_DISCOVERY" ]]; then
        print_status "success" "Agent discovery system available"
    else
        print_status "error" "Agent discovery system missing"
        status_ok=false
    fi

    if [[ -f "$TEMPLATE_MANAGER" ]]; then
        print_status "success" "Template manager available"
    else
        print_status "error" "Template manager missing"
        status_ok=false
    fi

    if [[ -f "$QUALITY_VALIDATOR" ]]; then
        print_status "success" "Quality validator available"
    else
        print_status "error" "Quality validator missing"
        status_ok=false
    fi

    if command -v python3 >/dev/null 2>&1; then
        print_status "success" "Python 3 available"
    else
        print_status "error" "Python 3 missing"
        status_ok=false
    fi

    echo ""
    if $status_ok; then
        print_status "success" "All systems operational"
    else
        print_status "warning" "Some components need attention"
    fi
}

# =============================================================================
# INTERACTIVE MENU SYSTEM
# =============================================================================

show_main_menu() {
    echo "${COLOR_CYAN}${COLOR_BOLD}FRAMEWORK OPTIONS${COLOR_RESET}"
    echo "${COLOR_CYAN}${COLOR_BOLD}────────────────────────────────────────────────────────────────${COLOR_RESET}"
    echo "${COLOR_YELLOW}[d]${COLOR_RESET} Agent Discovery System  ${COLOR_WHITE}- Browse and explore available agents${COLOR_RESET}"
    echo "${COLOR_YELLOW}[v]${COLOR_RESET} Quality Validation      ${COLOR_WHITE}- Framework health & quality checks${COLOR_RESET}"
    echo ""
    echo "${COLOR_MAGENTA}${COLOR_BOLD}PROJECT OPTIONS${COLOR_RESET}"
    echo "${COLOR_MAGENTA}${COLOR_BOLD}────────────────────────────────────────────────────────────────${COLOR_RESET}"
    echo "${COLOR_YELLOW}[w]${COLOR_RESET} Project Setup Wizard    ${COLOR_WHITE}- Interactive project setup${COLOR_RESET}"
    echo "${COLOR_YELLOW}[p]${COLOR_RESET} Project Templates       ${COLOR_WHITE}- Generate CLAUDE.md from tech stack templates${COLOR_RESET}"
    echo "${COLOR_YELLOW}[a]${COLOR_RESET} Project Analysis        ${COLOR_WHITE}- Comprehensive project analysis${COLOR_RESET}"
    echo "${COLOR_YELLOW}[c]${COLOR_RESET} Custom Path Analysis    ${COLOR_WHITE}- Analyze specific directory${COLOR_RESET}"
    echo "${COLOR_YELLOW}[t]${COLOR_RESET} Technology Detection    ${COLOR_WHITE}- Detect technology stack${COLOR_RESET}"
    echo "${COLOR_YELLOW}[r]${COLOR_RESET} Agent Recommendations   ${COLOR_WHITE}- Get AI agent suggestions${COLOR_RESET}"
    echo ""
    echo "${COLOR_WHITE}${COLOR_BOLD}OTHER${COLOR_RESET}"
    echo "${COLOR_WHITE}${COLOR_BOLD}────────────────────────────────────────────────────────────────${COLOR_RESET}"
    echo "${COLOR_YELLOW}[s]${COLOR_RESET} System Status          ${COLOR_WHITE}- Check AI tools status${COLOR_RESET}"
    echo "${COLOR_YELLOW}[u]${COLOR_RESET} Tutorial               ${COLOR_WHITE}- Basic usage tutorial${COLOR_RESET}"
    echo "${COLOR_YELLOW}[m]${COLOR_RESET} Manual Setup Guide     ${COLOR_WHITE}- Step-by-step installation help${COLOR_RESET}"
    echo "${COLOR_YELLOW}[h]${COLOR_RESET} Help                   ${COLOR_WHITE}- Show detailed help${COLOR_RESET}"
    echo "${COLOR_YELLOW}[q]${COLOR_RESET} Quit                   ${COLOR_WHITE}- Exit AI tools${COLOR_RESET}"
    echo ""
}

show_help() {
    clear
    echo "${COLOR_CYAN}${COLOR_BOLD}${ICON_INFO} AI Tools Help${COLOR_RESET}"
    echo "===================="
    echo ""
    echo "${COLOR_GREEN}About AI Tools:${COLOR_RESET}"
    echo "The AI Tools system provides intelligent project analysis and agent recommendations"
    echo "for the Claude Code Multi-Agent Framework."
    echo ""
    echo "${COLOR_GREEN}Key Features:${COLOR_RESET}"
    echo "• Technology stack detection (90+ technologies)"
    echo "• Project complexity analysis"
    echo "• Business domain classification"
    echo "• Intelligent agent recommendations"
    echo "• Interactive framework setup wizard"
    echo "• Agent discovery and exploration system"
    echo "• Quick start templates for popular tech stacks"
    echo "• Automated quality validation and health checks"
    echo "• Integration with framework agents"
    echo ""
    echo "${COLOR_GREEN}Usage:${COLOR_RESET}"
    echo "Run './ai-tools.sh' and select options from the menu."
    echo "For command-line usage: python3 .ai-tools/core/bin/project_analyzer.py [path]"
    echo ""
    echo "${COLOR_GREEN}Dependencies:${COLOR_RESET}"
    echo "• Python 3.6+"
    echo "• AI Tools components (.ai-tools/)"
    echo ""
}

run_interactive_menu() {
    while true; do
        print_header
        show_system_status
        echo ""
        show_main_menu

        echo -n "${COLOR_BOLD}${ICON_LIGHTNING} Select option: ${COLOR_RESET}"
        read -r choice
        echo ""

        case "$choice" in
            "a"|"A")
                run_project_analysis
                echo ""
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "t"|"T")
                run_technology_detection
                echo ""
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "r"|"R")
                run_agent_recommendations
                echo ""
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "u"|"U")
                run_tutorial
                echo ""
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "w"|"W") run_framework_setup ;;  # Interactive - no additional prompt
            "p"|"P") run_template_manager ;;  # Interactive - no additional prompt
            "d"|"D") run_agent_discovery ;;  # Interactive - no additional prompt
            "v"|"V") run_quality_validation ;;  # Interactive - no additional prompt
            "c"|"C")
                echo -n "${COLOR_CYAN}Enter path to analyze: ${COLOR_RESET}"
                read -r custom_path
                if [[ -d "$custom_path" ]]; then
                    run_project_analysis "$custom_path"
                else
                    print_status "error" "Directory not found: $custom_path"
                fi
                echo ""
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "s"|"S")
                show_system_status
                echo ""
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "m"|"M")
                show_manual_setup_guide
                echo ""
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "h"|"H")
                show_help
                echo ""
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
            "q"|"Q"|"quit"|"exit")
                echo "${ICON_SUCCESS} ${COLOR_GREEN}Thank you for using AI Tools!${COLOR_RESET}"
                exit 0
                ;;
            *)
                print_status "error" "Invalid option: $choice"
                echo ""
                echo -n "${COLOR_YELLOW}Press Enter to continue...${COLOR_RESET}"
                read -r
                ;;
        esac
    done
}

# =============================================================================
# COMMAND LINE INTERFACE
# =============================================================================

show_cli_help() {
    echo "Usage: $0 [OPTION] [PATH]"
    echo ""
    echo "Options:"
    echo "  -a, --analyze [PATH]     Run project analysis"
    echo "  -t, --tech [PATH]        Detect technology stack"
    echo "  -r, --recommend [PATH]   Get agent recommendations"
    echo "  -u, --tutorial           Run basic tutorial"
    echo "  -w, --wizard             Run framework setup wizard"
    echo "  -d, --discover           Run agent discovery system"
    echo "  -p, --templates          Run template manager"
    echo "  -v, --validate           Run quality validation"
    echo "  -s, --status             Show system status"
    echo "  -h, --help               Show this help"
    echo ""
    echo "If no options are provided, interactive menu will be shown."
    echo ""
    echo "Examples:"
    echo "  $0                       # Interactive menu"
    echo "  $0 -a                    # Analyze current project"
    echo "  $0 -a /path/to/project   # Analyze specific project"
    echo "  $0 -t                    # Technology detection"
    echo "  $0 -r                    # Agent recommendations"
    echo "  $0 -w                    # Framework setup wizard"
    echo "  $0 -d                    # Agent discovery system"
    echo "  $0 -p                    # Quick start templates"
    echo "  $0 -v                    # Quality validation"
}

# =============================================================================
# MAIN EXECUTION
# =============================================================================

main() {
    # Check dependencies first
    check_dependencies

    # Parse command line arguments
    case "${1:-}" in
        "-a"|"--analyze")
            shift
            run_project_analysis "${1:-$PROJECT_DIR}"
            ;;
        "-t"|"--tech")
            shift
            run_technology_detection "${1:-$PROJECT_DIR}"
            ;;
        "-r"|"--recommend")
            shift
            run_agent_recommendations "${1:-$PROJECT_DIR}"
            ;;
        "-u"|"--tutorial")
            run_tutorial
            ;;
        "-w"|"--wizard")
            run_framework_setup
            ;;
        "-d"|"--discover")
            run_agent_discovery
            ;;
        "-p"|"--templates")
            run_template_manager
            ;;
        "-v"|"--validate")
            run_quality_validation
            ;;
        "-s"|"--status")
            print_header
            show_system_status
            ;;
        "-h"|"--help")
            print_header
            show_cli_help
            ;;
        "")
            # No arguments - run interactive menu
            run_interactive_menu
            ;;
        *)
            print_status "error" "Unknown option: $1"
            echo ""
            show_cli_help
            exit 1
            ;;
    esac
}

# Run main function
main "$@"