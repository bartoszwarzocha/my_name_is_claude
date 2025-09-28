#!/bin/bash

# =============================================================================
# MCP TOOLS MANAGER v2.0.0
# Claude Code Multi-Agent Framework - Professional MCP Management System
# =============================================================================

set -e

# =============================================================================
# CORE CONFIGURATION
# =============================================================================

# Version and metadata
readonly SCRIPT_VERSION="2.0.0"
readonly FRAMEWORK_VERSION="2.1.0"
readonly SCRIPT_NAME="MCP Tools Manager"

# Paths and directories
readonly PROJECT_DIR="$(pwd)"
readonly PROJECT_NAME="$(basename "$PROJECT_DIR")"
readonly HOME_MCP_DIR="$HOME/.mcp-tools"
readonly PROJECT_MCP_DIR="$PROJECT_DIR/.mcp-tools"
readonly MCP_REGISTRY="$HOME_MCP_DIR/registry"
readonly CONFIG_FILE="$HOME_MCP_DIR/config.json"
readonly PROJECT_CONFIG="$PROJECT_MCP_DIR/config.json"

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
readonly ICON_GEAR="⚙️"
readonly ICON_LIGHTNING="⚡"
readonly ICON_TARGET="🎯"
readonly ICON_WRENCH="🔧"
readonly ICON_HEALTH="🏥"

# Performance cache variables
declare -a CACHED_PROJECT_TECH=()
declare CACHE_TIMESTAMP=0
declare CACHE_PROJECT_DIR=""

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

function log_info()    { echo "${COLOR_BLUE}${ICON_INFO} $*${COLOR_RESET}"; }
function log_success() { echo "${COLOR_GREEN}${ICON_SUCCESS} $*${COLOR_RESET}"; }
function log_warn()    { echo "${COLOR_YELLOW}${ICON_WARNING} $*${COLOR_RESET}"; }
function log_error()   { echo "${COLOR_RED}${ICON_ERROR} $*${COLOR_RESET}"; }
function log_header()  { echo "${COLOR_BOLD}${COLOR_CYAN}$*${COLOR_RESET}"; }

function require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    log_error "Missing required command: $1"
    log_info "Please install $1 and try again."
    exit 1
  fi
}

function read_option() {
  local option
  read -r option 2>/dev/null || option=""
  echo "$option"
}

function wait_for_enter() {
  echo ""
  echo "Naciśnij Enter, aby kontynuować..."
  read -r
}

function setup_directories() {
  mkdir -p "$HOME_MCP_DIR" "$HOME_MCP_DIR/logs" "$MCP_REGISTRY"
  [[ -d "$PROJECT_MCP_DIR" ]] || mkdir -p "$PROJECT_MCP_DIR"
}

# =============================================================================
# PROJECT ANALYSIS & SMART DETECTION
# =============================================================================

function detect_project_technology() {
  # Cache validation - check if cache is valid (same directory and recent)
  local current_time=$(date +%s)
  local cache_validity=300  # 5 minutes cache

  if [[ "$CACHE_PROJECT_DIR" == "$PROJECT_DIR" ]] &&
     [[ $((current_time - CACHE_TIMESTAMP)) -lt $cache_validity ]] &&
     [[ ${#CACHED_PROJECT_TECH[@]} -gt 0 ]]; then
    # Return cached results
    printf '%s\n' "${CACHED_PROJECT_TECH[@]}"
    return 0
  fi

  # Cache miss - perform actual detection
  local tech_stack=()

  # Frontend Technologies
  [[ -f "package.json" ]] && tech_stack+=("nodejs")
  [[ -f "angular.json" ]] && tech_stack+=("angular")
  [[ -f "next.config.js" || -f "next.config.ts" ]] && tech_stack+=("nextjs")
  [[ -d "src" && -f "package.json" ]] && grep -q "react" package.json 2>/dev/null && tech_stack+=("react")
  [[ -f "vue.config.js" || -f "vite.config.js" ]] && tech_stack+=("vue")

  # Backend Technologies
  [[ -f "requirements.txt" || -f "pyproject.toml" || -f "setup.py" ]] && tech_stack+=("python")
  [[ -f "pom.xml" || -f "build.gradle" ]] && tech_stack+=("java")
  [[ -f "*.csproj" || -f "*.sln" ]] && tech_stack+=("dotnet")
  [[ -f "go.mod" ]] && tech_stack+=("golang")
  [[ -f "Cargo.toml" ]] && tech_stack+=("rust")
  [[ -f "composer.json" ]] && tech_stack+=("php")
  [[ -f "Gemfile" ]] && tech_stack+=("ruby")

  # Database Technologies - optimize multiple greps on same file
  if [[ -f "docker-compose.yml" ]]; then
    local compose_content
    compose_content=$(cat docker-compose.yml 2>/dev/null || echo "")
    [[ "$compose_content" =~ postgres ]] && tech_stack+=("postgresql")
    [[ "$compose_content" =~ mysql ]] && tech_stack+=("mysql")
    [[ "$compose_content" =~ redis ]] && tech_stack+=("redis")
  fi

  # Infrastructure
  [[ -f "Dockerfile" ]] && tech_stack+=("docker")
  [[ -d ".github/workflows" || -f ".gitlab-ci.yml" ]] && tech_stack+=("cicd")
  [[ -f "terraform.tf" || -d "terraform" ]] && tech_stack+=("terraform")
  [[ -d "k8s" || -f "kubernetes.yml" ]] && tech_stack+=("kubernetes")

  # Testing
  [[ -f "cypress.config.js" || -d "cypress" ]] && tech_stack+=("cypress")
  [[ -f "jest.config.js" || -f "jest.config.ts" ]] && tech_stack+=("jest")
  [[ -f "playwright.config.js" || -f "playwright.config.ts" ]] && tech_stack+=("playwright")

  # Update cache
  CACHED_PROJECT_TECH=("${tech_stack[@]}")
  CACHE_TIMESTAMP=$current_time
  CACHE_PROJECT_DIR="$PROJECT_DIR"

  printf '%s\n' "${tech_stack[@]}"
}

function get_smart_mcp_recommendations() {
  local detected_tech=()
  mapfile -t detected_tech < <(detect_project_technology)

  local recommendations=()

  # Always recommend core tools
  recommendations+=("serena" "context7")

  # Technology-specific recommendations
  for tech in "${detected_tech[@]}"; do
    case "$tech" in
      "nodejs"|"react"|"angular"|"vue"|"nextjs")
        recommendations+=("playwright" "jest" "github")
        ;;
      "python")
        recommendations+=("github" "postgresql" "rest-api")
        ;;
      "java")
        recommendations+=("github" "postgresql" "rest-api" "sonarqube")
        ;;
      "docker")
        recommendations+=("docker" "kubernetes")
        ;;
      "cicd")
        recommendations+=("github" "gitlab")
        ;;
      "postgresql"|"mysql")
        recommendations+=("postgresql" "mysql")
        ;;
    esac
  done

  # Remove duplicates and print
  printf '%s\n' "${recommendations[@]}" | sort -u
}

# =============================================================================
# MCP TOOLS REGISTRY & DEFINITIONS
# =============================================================================

function init_mcp_registry() {
  # Check if extended registry exists, otherwise create core registry
  if [[ ! -f "$MCP_REGISTRY/extended.json" ]]; then
    # Create the extended registry if it doesn't exist
    mkdir -p "$MCP_REGISTRY"
    # The extended.json file should already be created, but if not, use core as fallback
    if [[ ! -f "$MCP_REGISTRY/core.json" ]]; then
      cat > "$MCP_REGISTRY/core.json" <<'EOF'
{
  "serena": {
    "name": "Serena",
    "category": "development",
    "description": "Code Navigation & Project Analysis",
    "install_method": "git_uv",
    "repository": "https://github.com/oraios/serena",
    "install_dir": "$HOME/tools/serena",
    "dependencies": ["git", "uv"],
    "technologies": ["python", "typescript", "java", "rust", "go"],
    "register_cmd": "uv run --directory $HOME/tools/serena serena-mcp-server --context ide-assistant --project $PROJECT_DIR",
    "priority": 1
  },
  "context7": {
    "name": "Context7",
    "category": "development",
    "description": "Advanced Code Generation",
    "install_method": "docker",
    "npm_package": "@upstash/context7-mcp",
    "dependencies": ["docker"],
    "technologies": ["nodejs", "typescript", "python", "java"],
    "register_cmd": "docker run --rm -i -v $PROJECT_DIR:/app context7-mcp",
    "priority": 1
  }
}
EOF
    fi
  fi
}

function get_mcp_list() {
  local category="${1:-all}"
  local registry_file="$MCP_REGISTRY/extended.json"

  # Fallback to core.json if extended doesn't exist
  if [[ ! -f "$registry_file" ]]; then
    registry_file="$MCP_REGISTRY/core.json"
    if [[ ! -f "$registry_file" ]]; then
      init_mcp_registry
      registry_file="$MCP_REGISTRY/core.json"
    fi
  fi

  if [[ "$MCP_LIMITED_MODE" == "true" ]]; then
    # Limited mode - basic hardcoded list
    if [[ "$category" == "all" || "$category" == "development" ]]; then
      echo "serena"
      echo "context7"
      echo "github"
    fi
    if [[ "$category" == "all" || "$category" == "testing" ]]; then
      echo "playwright"
    fi
    if [[ "$category" == "all" || "$category" == "database" ]]; then
      echo "postgresql"
    fi
    return 0
  fi

  if [[ "$category" == "all" ]]; then
    jq -r 'keys[]' "$registry_file" 2>/dev/null | sort
  else
    jq -r --arg cat "$category" 'to_entries[] | select(.value.category == $cat) | .key' "$registry_file" 2>/dev/null | sort
  fi
}

function get_mcp_info() {
  local mcp_name="$1"
  local field="${2:-all}"
  local registry_file="$MCP_REGISTRY/extended.json"

  if [[ "$MCP_LIMITED_MODE" == "true" ]]; then
    # Limited mode - basic hardcoded info
    case "$mcp_name" in
      "serena")
        case "$field" in
          "name") echo "Serena" ;;
          "description") echo "Code Navigation & Project Analysis" ;;
          "category") echo "development" ;;
          "install_method") echo "git_uv" ;;
          "register_cmd") echo "uv run --directory $HOME/tools/serena serena-mcp-server --context ide-assistant --project $PROJECT_DIR" ;;
          *) echo '{"name":"Serena","category":"development","description":"Code Navigation & Project Analysis"}' ;;
        esac ;;
      "context7")
        case "$field" in
          "name") echo "Context7" ;;
          "description") echo "Advanced Code Generation" ;;
          "category") echo "development" ;;
          "install_method") echo "docker" ;;
          "register_cmd") echo "docker run --rm -i -v $PROJECT_DIR:/app context7-mcp" ;;
          *) echo '{"name":"Context7","category":"development","description":"Advanced Code Generation"}' ;;
        esac ;;
      "github")
        case "$field" in
          "name") echo "GitHub" ;;
          "description") echo "Repository Management" ;;
          "category") echo "development" ;;
          "install_method") echo "npm" ;;
          "register_cmd") echo "npx @modelcontextprotocol/server-github" ;;
          *) echo '{"name":"GitHub","category":"development","description":"Repository Management"}' ;;
        esac ;;
      "playwright")
        case "$field" in
          "name") echo "Playwright" ;;
          "description") echo "Web Automation & Testing" ;;
          "category") echo "testing" ;;
          "install_method") echo "npm" ;;
          "register_cmd") echo "npx playwright" ;;
          *) echo '{"name":"Playwright","category":"testing","description":"Web Automation & Testing"}' ;;
        esac ;;
      "postgresql")
        case "$field" in
          "name") echo "PostgreSQL" ;;
          "description") echo "Database Operations" ;;
          "category") echo "database" ;;
          "install_method") echo "npm" ;;
          "register_cmd") echo "npx @modelcontextprotocol/server-postgres" ;;
          *) echo '{"name":"PostgreSQL","category":"database","description":"Database Operations"}' ;;
        esac ;;
      *) echo "" ;;
    esac
    return 0
  fi

  # Fallback to core.json if extended doesn't exist
  if [[ ! -f "$registry_file" ]]; then
    registry_file="$MCP_REGISTRY/core.json"
    if [[ ! -f "$registry_file" ]]; then
      init_mcp_registry
      registry_file="$MCP_REGISTRY/core.json"
    fi
  fi

  if [[ "$field" == "all" ]]; then
    jq -r --arg name "$mcp_name" '.[$name]' "$registry_file" 2>/dev/null
  else
    jq -r --arg name "$mcp_name" --arg field "$field" '.[$name][$field] // empty' "$registry_file" 2>/dev/null
  fi
}

# =============================================================================
# MCP STATUS & HEALTH MONITORING
# =============================================================================

function check_mcp_installed() {
  local mcp_name="$1"
  local fast_mode="${2:-false}"
  local install_method
  install_method=$(get_mcp_info "$mcp_name" "install_method")

  case "$install_method" in
    "git_uv")
      local install_dir
      install_dir=$(get_mcp_info "$mcp_name" "install_dir")
      install_dir="${install_dir//\$HOME/$HOME}"
      [[ -d "$install_dir" ]] && return 0
      ;;
    "docker")
      local image_name="${mcp_name}-mcp"
      if [[ "$fast_mode" == "true" ]]; then
        # Fast check: just look for image name in docker images output (much faster)
        docker images --format "table {{.Repository}}" 2>/dev/null | grep -q "^$image_name$" && return 0
      else
        # Thorough check
        docker image inspect "$image_name" &>/dev/null && return 0
      fi
      ;;
    "npm")
      local npm_package
      npm_package=$(get_mcp_info "$mcp_name" "npm_package")
      if [[ "$fast_mode" == "true" ]]; then
        # Fast check: look for package in npm global directory
        [[ -d "$(npm root -g)/$npm_package" ]] 2>/dev/null && return 0
      else
        # Thorough check
        npm list -g "$npm_package" &>/dev/null && return 0
      fi
      ;;
  esac

  return 1
}

function check_mcp_registered() {
  local mcp_name="$1"
  require_cmd claude
  claude mcp list 2>/dev/null | grep -q "^$mcp_name:" && return 0
  return 1
}

function get_mcp_status() {
  local mcp_name="$1"
  local fast_mode="${2:-false}"
  local installed="❌"
  local registered="❌"

  check_mcp_installed "$mcp_name" "$fast_mode" && installed="✅"
  check_mcp_registered "$mcp_name" && registered="✅"

  echo "$installed $registered"
}

function show_system_health() {
  log_header "═══════════════ SYSTEM HEALTH CHECK ═══════════════"
  echo ""

  log_info "Checking core dependencies..."
  local deps=("claude" "docker" "node" "npm" "git" "jq")
  for dep in "${deps[@]}"; do
    if command -v "$dep" >/dev/null 2>&1; then
      echo "  ✅ $dep: $(command -v "$dep")"
    else
      echo "  ❌ $dep: Not found"
    fi
  done

  echo ""
  log_info "MCP Tools Status:"
  printf "%-15s %-12s %-10s %s\n" "Tool" "Installed" "Registered" "Description"
  printf "%-15s %-12s %-10s %s\n" "----" "---------" "----------" "-----------"

  while IFS= read -r mcp_name; do
    local status
    status=$(get_mcp_status "$mcp_name")
    local desc
    desc=$(get_mcp_info "$mcp_name" "description")
    printf "%-15s %-12s %s\n" "$mcp_name" "$status" "$desc"
  done < <(get_mcp_list)

  echo ""
  log_info "Project Analysis:"
  echo "  📁 Project: $PROJECT_NAME"
  echo "  📍 Path: $PROJECT_DIR"
  echo "  🔧 Detected Technologies:"
  while IFS= read -r tech; do
    [[ -n "$tech" ]] && echo "     • $tech"
  done < <(detect_project_technology)

  echo ""
  log_info "Recommended MCP Tools:"
  while IFS= read -r mcp; do
    [[ -n "$mcp" ]] && echo "     • $mcp"
  done < <(get_smart_mcp_recommendations)
}

# =============================================================================
# MCP INSTALLATION FUNCTIONS
# =============================================================================

function install_mcp_serena() {
  log_info "Installing Serena MCP..."
  require_cmd git

  local install_dir="$HOME/tools/serena"
  mkdir -p "$HOME/tools"

  if [[ ! -d "$install_dir" ]]; then
    cd "$HOME/tools"
    git clone https://github.com/oraios/serena serena
  fi

  cd "$install_dir"

  if ! command -v uv &>/dev/null; then
    log_info "Installing uv package manager..."
    curl -Ls https://astral.sh/uv/install.sh | bash
    # shellcheck disable=SC1090
    source "$HOME/.bashrc" 2>/dev/null || true
  fi

  log_info "Setting up Python environment and installing..."
  uv venv
  uv pip install -e .[all-extras]

  log_success "Serena installed successfully!"
}

function install_mcp_context7() {
  log_info "Installing Context7 MCP..."
  require_cmd docker

  local dockerfile_path="$PROJECT_DIR/Dockerfile.context7"

  if [[ ! -f "$dockerfile_path" ]]; then
    log_info "Creating Context7 Dockerfile..."
    cat > "$dockerfile_path" <<'EOF'
FROM node:18-alpine
WORKDIR /app
RUN npm install -g @upstash/context7-mcp
CMD ["context7-mcp"]
EOF
  fi

  log_info "Building Context7 Docker image..."
  docker build -f "$dockerfile_path" -t "context7-mcp" "$PROJECT_DIR"

  log_success "Context7 installed successfully!"
}

function install_mcp_generic_npm() {
  local mcp_name="$1"
  local npm_package
  npm_package=$(get_mcp_info "$mcp_name" "npm_package")

  if [[ -z "$npm_package" ]]; then
    log_error "No npm package defined for $mcp_name"
    return 1
  fi

  log_info "Installing $mcp_name via npm..."
  require_cmd npm

  npm install -g "$npm_package"
  log_success "$mcp_name installed successfully!"
}

function install_mcp() {
  local mcp_name="$1"
  local install_method
  install_method=$(get_mcp_info "$mcp_name" "install_method")

  case "$install_method" in
    "git_uv") install_mcp_serena ;;
    "docker") install_mcp_context7 ;;
    "npm") install_mcp_generic_npm "$mcp_name" ;;
    *)
      log_error "Unknown installation method: $install_method"
      return 1
      ;;
  esac
}

# =============================================================================
# MCP REGISTRATION FUNCTIONS
# =============================================================================

function register_mcp_global() {
  local mcp_name="$1"
  require_cmd claude

  local register_cmd
  register_cmd=$(get_mcp_info "$mcp_name" "register_cmd")

  if [[ -z "$register_cmd" ]]; then
    log_error "No registration command defined for $mcp_name"
    return 1
  fi

  # Expand variables in the command
  register_cmd="${register_cmd//\$PROJECT_DIR/$PROJECT_DIR}"
  register_cmd="${register_cmd//\$HOME/$HOME}"

  log_info "Registering $mcp_name globally with Claude Code..."

  # Use bash to properly handle the command expansion
  eval "claude mcp add \"$mcp_name\" -- $register_cmd"

  log_success "$mcp_name registered globally!"
}

function register_mcp_project() {
  local mcp_name="$1"
  require_cmd claude

  local register_cmd
  register_cmd=$(get_mcp_info "$mcp_name" "register_cmd")

  if [[ -z "$register_cmd" ]]; then
    log_error "No registration command defined for $mcp_name"
    return 1
  fi

  # Expand variables in the command
  register_cmd="${register_cmd//\\$PROJECT_DIR/$PROJECT_DIR}"
  register_cmd="${register_cmd//\\$HOME/$HOME}"

  log_info "Registering $mcp_name for current project..."

  # Create project MCP config directory if it doesn't exist
  mkdir -p "$PROJECT_MCP_DIR"

  # For now, use same registration as global but note it's project-specific
  # TODO: Implement true project-specific registration when Claude Code supports it
  eval "claude mcp add \"$mcp_name\" -- $register_cmd"

  # Create a marker file to track project-specific registrations
  echo "$mcp_name" >> "$PROJECT_MCP_DIR/registered_mcps.txt"

  log_success "$mcp_name registered for project $PROJECT_NAME!"
}

function unregister_mcp() {
  local mcp_name="$1"
  require_cmd claude

  log_info "Unregistering $mcp_name from Claude Code..."
  claude mcp remove "$mcp_name" && log_success "$mcp_name unregistered successfully!" || log_warn "Nothing to remove."
}

# =============================================================================
# MCP-SPECIFIC MENUS
# =============================================================================

function show_mcp_menu() {
  local mcp_name="$1"
  local mcp_info
  mcp_info=$(get_mcp_info "$mcp_name")

  if [[ -z "$mcp_info" || "$mcp_info" == "null" ]]; then
    log_error "MCP '$mcp_name' not found in registry"
    return 1
  fi

  local name desc category status
  name=$(echo "$mcp_info" | jq -r '.name')
  desc=$(echo "$mcp_info" | jq -r '.description')
  category=$(echo "$mcp_info" | jq -r '.category')
  status=$(get_mcp_status "$mcp_name")

  clear
  log_header "════════════ $name MANAGEMENT ════════════"
  echo "Status: $status | Category: $category"
  echo "Project: $PROJECT_NAME"
  log_header "════════════════════════════════════════════"
  echo ""
  echo "${COLOR_BOLD}QUICK ACTIONS:${COLOR_RESET}"
  echo " [${COLOR_GREEN}q${COLOR_RESET}] ${ICON_LIGHTNING} Quick Setup (Install + Register + Start)"
  echo " [${COLOR_BLUE}s${COLOR_RESET}] ${ICON_TARGET} Smart Configuration (Auto-detect optimal setup)"
  echo ""
  echo "${COLOR_BOLD}INSTALLATION:${COLOR_RESET}               ${COLOR_BOLD}REGISTRATION:${COLOR_RESET}"
  echo " [${COLOR_YELLOW}i${COLOR_RESET}] Install $name                [${COLOR_MAGENTA}r${COLOR_RESET}] Register Global"
  echo " [${COLOR_YELLOW}u${COLOR_RESET}] Update to Latest            [${COLOR_MAGENTA}p${COLOR_RESET}] Register Project-specific"
  echo " [${COLOR_YELLOW}x${COLOR_RESET}] Remove/Uninstall            [${COLOR_MAGENTA}d${COLOR_RESET}] Unregister"
  echo ""
  echo "${COLOR_BOLD}OPERATIONS:${COLOR_RESET}                ${COLOR_BOLD}CONFIGURATION:${COLOR_RESET}"
  echo " [${COLOR_CYAN}1${COLOR_RESET}] Start Service              [${COLOR_WHITE}c${COLOR_RESET}] Configure Settings"
  echo " [${COLOR_CYAN}2${COLOR_RESET}] Start with Advanced         [${COLOR_WHITE}v${COLOR_RESET}] View Configuration"
  echo " [${COLOR_CYAN}3${COLOR_RESET}] Stop Service               [${COLOR_WHITE}z${COLOR_RESET}] Reset to Defaults"
  echo " [${COLOR_CYAN}4${COLOR_RESET}] Restart Service"
  echo ""
  echo "${COLOR_BOLD}DIAGNOSTICS:${COLOR_RESET}"
  echo " [${COLOR_GREEN}t${COLOR_RESET}] Test Connection             [${COLOR_GREEN}l${COLOR_RESET}] View Logs                [${COLOR_GREEN}h${COLOR_RESET}] Health Check"
  echo ""
  echo " [${COLOR_RED}0${COLOR_RESET}] ← Back to Main Menu"
  log_header "════════════════════════════════════════════"
  echo ""
}

function handle_mcp_menu() {
  local mcp_name="$1"

  while true; do
    show_mcp_menu "$mcp_name"
    echo -n "Wybierz opcję: "
    local key
    key=$(read_option)

    case "$key" in
      # Quick Actions
      q|Q)
        log_info "Executing Quick Setup for $mcp_name..."
        if ! check_mcp_installed "$mcp_name"; then
          install_mcp "$mcp_name"
        fi
        if ! check_mcp_registered "$mcp_name"; then
          register_mcp_global "$mcp_name"
        fi
        log_success "Quick setup completed!"
        wait_for_enter
        ;;

      s|S)
        log_info "Smart Configuration for $mcp_name..."
        # TODO: Implement smart configuration logic
        log_info "Analyzing project and optimizing $mcp_name configuration..."
        wait_for_enter
        ;;

      # Installation
      i|I)
        if check_mcp_installed "$mcp_name"; then
          log_warn "$mcp_name is already installed."
        else
          install_mcp "$mcp_name"
        fi
        wait_for_enter
        ;;

      u|U)
        log_info "Updating $mcp_name to latest version..."
        # TODO: Implement update logic
        wait_for_enter
        ;;

      x|X)
        log_warn "Removing $mcp_name..."
        # TODO: Implement removal logic
        wait_for_enter
        ;;

      # Registration
      r|R)
        if check_mcp_registered "$mcp_name"; then
          log_warn "$mcp_name is already registered globally."
        else
          if ! check_mcp_installed "$mcp_name"; then
            log_error "$mcp_name is not installed. Install it first."\n            sleep 1
          else
            register_mcp_global "$mcp_name"
          fi
        fi
        wait_for_enter
        ;;

      p|P)
        register_mcp_project "$mcp_name"
        wait_for_enter
        ;;

      d|D)
        unregister_mcp "$mcp_name"
        wait_for_enter
        ;;

      # Operations
      1)
        log_info "Starting $mcp_name service..."
        # TODO: Implement service start logic
        wait_for_enter
        ;;

      2)
        log_info "Starting $mcp_name with advanced options..."
        # TODO: Implement advanced start logic
        wait_for_enter
        ;;

      3)
        log_info "Stopping $mcp_name service..."
        # TODO: Implement service stop logic
        wait_for_enter
        ;;

      4)
        log_info "Restarting $mcp_name service..."
        # TODO: Implement service restart logic
        wait_for_enter
        ;;

      # Configuration
      c|C)
        log_info "Opening $mcp_name configuration..."
        # TODO: Implement configuration menu
        wait_for_enter
        ;;

      v|V)
        log_info "Current $mcp_name configuration:"
        get_mcp_info "$mcp_name" | jq '.'
        wait_for_enter
        ;;

      z|Z)
        log_info "Resetting $mcp_name to default configuration..."
        # TODO: Implement reset logic
        wait_for_enter
        ;;

      # Diagnostics
      t|T)
        log_info "Testing $mcp_name connection..."
        if check_mcp_registered "$mcp_name"; then
          claude mcp call "$mcp_name" health 2>/dev/null && log_success "Connection OK" || log_warn "Connection failed"
        else
          log_error "$mcp_name is not registered"
          sleep 1
        fi
        wait_for_enter
        ;;

      l|L)
        log_info "Viewing $mcp_name logs..."
        # TODO: Implement log viewing
        wait_for_enter
        ;;

      h|H)
        log_info "$mcp_name Health Check:"
        local status
        status=$(get_mcp_status "$mcp_name")
        echo "  Status: $status"
        echo "  Configuration: $(get_mcp_info "$mcp_name" | jq -r '.name')"
        wait_for_enter
        ;;

      # Exit
      0|b|B)
        break
        ;;

      *)
        log_warn "Invalid option: '$key'. Try again."
        sleep 1
        ;;
    esac
  done
}

# =============================================================================
# MAIN MENU & NAVIGATION
# =============================================================================

function show_main_menu() {
  local detected_tech
  mapfile -t detected_tech < <(detect_project_technology)

  clear
  log_header "════════════ MCP TOOLS MANAGER ════════════"
  echo "Version: $SCRIPT_VERSION | Framework: Claude Code Multi-Agent v$FRAMEWORK_VERSION"
  if [[ "$MCP_LIMITED_MODE" == "true" ]]; then
    echo "Mode: ${COLOR_YELLOW}LIMITED${COLOR_RESET} (jq not available - install jq for full functionality)"
  else
    echo "Mode: ${COLOR_GREEN}FULL${COLOR_RESET} (All features available)"
  fi
  echo "Project: $PROJECT_NAME"
  echo "Path: $PROJECT_DIR"
  log_header "═══════════════════════════════════════════"
  echo ""
  echo "${COLOR_BOLD}CONFIGURATION MANAGEMENT:${COLOR_RESET}"
  echo " [${COLOR_CYAN}g${COLOR_RESET}] ${ICON_GEAR} Global MCP Configuration"
  echo " [${COLOR_CYAN}p${COLOR_RESET}] ${ICON_WRENCH} Project-specific MCP Configuration"
  echo " [${COLOR_CYAN}a${COLOR_RESET}] ${ICON_HEALTH} View Active MCP Status"
  echo ""
  echo "${COLOR_BOLD}SMART RECOMMENDATIONS${COLOR_RESET} (Based on detected: ${detected_tech[*]}):"
  local recs=()
  mapfile -t recs < <(get_smart_mcp_recommendations)
  for rec in "${recs[@]:0:3}"; do
    [[ -n "$rec" ]] && echo " [${COLOR_GREEN}${rec:0:1}${COLOR_RESET}] $(get_mcp_info "$rec" "name") - $(get_mcp_info "$rec" "description")"
  done
  echo ""
  echo "${COLOR_BOLD}MCP TOOLS BY CATEGORY:${COLOR_RESET}"
  echo " [${COLOR_YELLOW}1${COLOR_RESET}] ${ICON_ROCKET} Development & Code"
  echo " [${COLOR_YELLOW}2${COLOR_RESET}] ${ICON_TARGET} Testing & Quality"
  echo " [${COLOR_YELLOW}3${COLOR_RESET}] ${ICON_GEAR} Database & APIs"
  echo " [${COLOR_YELLOW}4${COLOR_RESET}] ${ICON_WRENCH} Cloud & Infrastructure"
  echo " [${COLOR_YELLOW}5${COLOR_RESET}] ${ICON_LIGHTNING} AI & Machine Learning"
  echo " [${COLOR_YELLOW}6${COLOR_RESET}] ${ICON_HEALTH} Productivity & System Tools"
  echo ""
  echo "${COLOR_BOLD}SYSTEM OPERATIONS:${COLOR_RESET}"
  echo " [${COLOR_MAGENTA}h${COLOR_RESET}] ${ICON_HEALTH} System Health Check"
  echo " [${COLOR_MAGENTA}u${COLOR_RESET}] ${ICON_ROCKET} Update All MCP Tools"
  echo " [${COLOR_RED}0${COLOR_RESET}] Exit"
  log_header "═══════════════════════════════════════════"
  echo ""
}

function show_category_menu() {
  local category="$1"
  local category_name="$2"
  local show_status="${3:-false}"  # Fast mode by default

  clear
  log_header "════════════ $category_name MCP TOOLS ════════════"
  echo ""

  local tools=()
  mapfile -t tools < <(get_mcp_list "$category")

  local i=1
  for tool in "${tools[@]}"; do
    local name desc status
    name=$(get_mcp_info "$tool" "name")
    desc=$(get_mcp_info "$tool" "description")

    if [[ "$show_status" == "true" ]]; then
      status=$(get_mcp_status "$tool" "true")  # Use fast mode for better performance
    else
      status="⏱️  ⏱️"  # Placeholder for fast mode
    fi

    printf " [%s] %-15s %s - %s\n" "$i" "$status" "$name" "$desc"
    ((i++))
  done

  echo ""
  if [[ "$show_status" == "false" ]]; then
    echo " [${COLOR_CYAN}s${COLOR_RESET}] 📊 Show Status (checks installation/registration)"
  fi
  echo " [0] ← Back to Main Menu"
  echo ""
  log_header "════════════════════════════════════════════"
}

function handle_category_menu() {
  local category="$1"
  local category_name="$2"
  local show_status="false"

  while true; do
    show_category_menu "$category" "$category_name" "$show_status"
    if [[ "$show_status" == "false" ]]; then
      echo -n "Wybierz narzędzie MCP [0-9] lub [s] dla statusów: "
    else
      echo -n "Wybierz narzędzie MCP [0-9]: "
    fi
    local key
    key=$(read_option)

    if [[ "$key" == "0" ]]; then
      break
    elif [[ "$key" == "s" || "$key" == "S" ]] && [[ "$show_status" == "false" ]]; then
      show_status="true"
      log_info "Sprawdzanie statusów MCP tools..."
      sleep 1
    elif [[ "$key" =~ ^[1-9]$ ]]; then
      local tools=()
      mapfile -t tools < <(get_mcp_list "$category")
      local index=$((key - 1))

      if [[ $index -lt ${#tools[@]} ]]; then
        handle_mcp_menu "${tools[$index]}"
      else
        log_warn "Invalid selection: $key"
        sleep 1
      fi
    else
      log_warn "Invalid option: '$key'. Try again."
      sleep 1
    fi
  done
}

function main_menu() {
  setup_directories

  # Initialize MCP registry if it doesn't exist
  [[ ! -f "$MCP_REGISTRY/core.json" ]] && init_mcp_registry

  while true; do
    show_main_menu
    echo -n "Wybierz opcję: "
    local key
    key=$(read_option)

    case "$key" in
      # Configuration Management
      g|G)
        log_info "Global MCP Configuration"
        # TODO: Implement global configuration menu
        wait_for_enter
        ;;

      p|P)
        log_info "Project-specific MCP Configuration"
        # TODO: Implement project configuration menu
        wait_for_enter
        ;;

      a|A)
        show_system_health
        wait_for_enter
        ;;

      # Smart Recommendations (first 3 letters)
      s|S)
        handle_mcp_menu "serena"
        ;;

      c|C)
        handle_mcp_menu "context7"
        ;;

      # Categories
      1)
        handle_category_menu "development" "DEVELOPMENT & CODE"
        ;;

      2)
        handle_category_menu "testing" "TESTING & QUALITY"
        ;;

      3)
        # Combine database and api categories
        clear
        log_header "════════════ DATABASE & APIs MCP TOOLS ════════════"
        echo ""
        echo "${COLOR_BOLD}Database Tools:${COLOR_RESET}"
        while IFS= read -r tool; do
          [[ -n "$tool" ]] && echo " • $(get_mcp_info "$tool" "name") - $(get_mcp_info "$tool" "description")"
        done < <(get_mcp_list "database")
        echo ""
        echo "${COLOR_BOLD}API Tools:${COLOR_RESET}"
        while IFS= read -r tool; do
          [[ -n "$tool" ]] && echo " • $(get_mcp_info "$tool" "name") - $(get_mcp_info "$tool" "description")"
        done < <(get_mcp_list "api")
        wait_for_enter
        ;;

      4)
        # Combine cloud and infrastructure categories
        clear
        log_header "════════════ CLOUD & INFRASTRUCTURE MCP TOOLS ════════════"
        echo ""
        echo "${COLOR_BOLD}Cloud Platforms:${COLOR_RESET}"
        while IFS= read -r tool; do
          [[ -n "$tool" ]] && echo " • $(get_mcp_info "$tool" "name") - $(get_mcp_info "$tool" "description")"
        done < <(get_mcp_list "cloud")
        echo ""
        echo "${COLOR_BOLD}Infrastructure Tools:${COLOR_RESET}"
        while IFS= read -r tool; do
          [[ -n "$tool" ]] && echo " • $(get_mcp_info "$tool" "name") - $(get_mcp_info "$tool" "description")"
        done < <(get_mcp_list "infrastructure")
        wait_for_enter
        ;;

      5)
        handle_category_menu "ai" "AI & MACHINE LEARNING"
        ;;

      6)
        # Combine productivity and system categories
        clear
        log_header "════════════ PRODUCTIVITY & SYSTEM TOOLS ════════════"
        echo ""
        echo "${COLOR_BOLD}Productivity Tools:${COLOR_RESET}"
        while IFS= read -r tool; do
          [[ -n "$tool" ]] && echo " • $(get_mcp_info "$tool" "name") - $(get_mcp_info "$tool" "description")"
        done < <(get_mcp_list "productivity")
        echo ""
        echo "${COLOR_BOLD}System Tools:${COLOR_RESET}"
        while IFS= read -r tool; do
          [[ -n "$tool" ]] && echo " • $(get_mcp_info "$tool" "name") - $(get_mcp_info "$tool" "description")"
        done < <(get_mcp_list "system")
        wait_for_enter
        ;;

      # System Operations
      h|H)
        show_system_health
        wait_for_enter
        ;;

      u|U)
        log_info "Updating all MCP tools..."
        # TODO: Implement update all logic
        wait_for_enter
        ;;

      # Exit
      0)
        log_info "Thank you for using MCP Tools Manager!"
        exit 0
        ;;

      *)
        log_warn "Invalid option: '$key'. Try again."
        sleep 1
        ;;
    esac
  done
}

# =============================================================================
# SCRIPT ENTRY POINT
# =============================================================================

# Smart dependency management for jq
function check_and_install_jq() {
  if command -v jq >/dev/null 2>&1; then
    return 0
  fi

  log_warn "jq JSON processor not found - required for full functionality"
  log_info "Attempting automatic installation..."

  # Try different installation methods
  if command -v apt >/dev/null 2>&1; then
    log_info "Detected apt package manager"
    echo "Installing jq via apt (requires sudo)..."
    if sudo apt update && sudo apt install -y jq; then
      log_success "jq installed successfully via apt!"
      return 0
    else
      log_warn "Could not install via apt (installation failed)"
    fi
  fi

  if command -v yum >/dev/null 2>&1; then
    log_info "Detected yum package manager"
    if sudo yum install -y jq; then
      log_success "jq installed successfully via yum!"
      return 0
    fi
  fi

  if command -v brew >/dev/null 2>&1; then
    log_info "Detected Homebrew package manager"
    if brew install jq 2>/dev/null; then
      log_success "jq installed successfully via Homebrew!"
      return 0
    fi
  fi

  # Manual installation fallback
  log_info "Automatic installation failed. Offering manual installation..."
  echo ""
  echo "${COLOR_BOLD}Manual Installation Options:${COLOR_RESET}"
  echo ""
  echo "Ubuntu/Debian:"
  echo "  ${COLOR_CYAN}sudo apt update && sudo apt install -y jq${COLOR_RESET}"
  echo ""
  echo "CentOS/RHEL/Fedora:"
  echo "  ${COLOR_CYAN}sudo yum install -y jq${COLOR_RESET}"
  echo "  ${COLOR_CYAN}sudo dnf install -y jq${COLOR_RESET}"
  echo ""
  echo "macOS:"
  echo "  ${COLOR_CYAN}brew install jq${COLOR_RESET}"
  echo ""
  echo "Or download binary from: ${COLOR_BLUE}https://jqlang.github.io/jq/download/${COLOR_RESET}"
  echo ""

  read -p "Try installation manually now? Press Enter when done, or 'q' to continue in limited mode: " response

  if [[ "$response" == "q" || "$response" == "Q" ]]; then
    log_warn "Continuing in limited mode - some features unavailable"
    return 1
  fi

  # Check again after manual installation
  if command -v jq >/dev/null 2>&1; then
    log_success "jq detected! Full functionality enabled."
    return 0
  else
    log_warn "jq still not found. Continuing in limited mode."
    return 1
  fi
}

# Check for required dependencies
if ! check_and_install_jq; then
  log_warn "Running in LIMITED MODE - some features may not work correctly"
  export MCP_LIMITED_MODE=true
else
  export MCP_LIMITED_MODE=false
fi

# Ensure we have a proper terminal
if [[ ! -t 0 ]]; then
  log_error "This script requires an interactive terminal"
  exit 1
fi

# Start the main menu
main_menu