#!/bin/bash

set -e

##############################################
# Shared setup
##############################################

# Paths
PROJECT_DIR="$(pwd)"
PROJECT_NAME="$(basename "$PROJECT_DIR")"

# Colors
green=$(tput setaf 2)
yellow=$(tput setaf 3)
red=$(tput setaf 1)
blue=$(tput setaf 4)
reset=$(tput sgr0)

function echo_info()    { echo "${blue}$*${reset}"; }
function echo_success() { echo "${green}$*${reset}"; }
function echo_warn()    { echo "${yellow}$*${reset}"; }
function echo_error()   { echo "${red}$*${reset}"; }

function require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo_error "Missing command: $1"
    exit 1
  fi
}

##############################################
# Context7 MCP section (Docker-based)
##############################################

C7_IMAGE_NAME="context7-mcp"
C7_DOCKERFILE_NAME="Dockerfile.context7"
C7_CONTAINER_NAME="context7-container"
C7_PROJECT_PATH="$PROJECT_DIR"

function c7_create_dockerfile() {
  if [ ! -f "$C7_DOCKERFILE_NAME" ]; then
    echo_info "Creating $C7_DOCKERFILE_NAME..."
    cat > "$C7_DOCKERFILE_NAME" <<'EOF'
FROM node:18-alpine
WORKDIR /app
RUN npm install -g @upstash/context7-mcp
CMD ["context7-mcp"]
EOF
  else
    echo_success "$C7_DOCKERFILE_NAME already exists – skipping"
  fi
}

function c7_build_image() {
  require_cmd docker
  echo_info "Building Docker image: $C7_IMAGE_NAME"
  docker build -f "$C7_DOCKERFILE_NAME" -t "$C7_IMAGE_NAME" .
}

function c7_run_container() {
  require_cmd docker
  echo_info "Starting container: $C7_IMAGE_NAME"
  docker run -it --rm \
    -v "$C7_PROJECT_PATH:/app" \
    --name "$C7_CONTAINER_NAME" \
    "$C7_IMAGE_NAME"
}

function c7_test_image_exists() {
  require_cmd docker
  if docker image inspect "$C7_IMAGE_NAME" &>/dev/null; then
    echo_success "Docker image '$C7_IMAGE_NAME' exists."
  else
    echo_warn "Docker image '$C7_IMAGE_NAME' not found."
  fi
}

function c7_remove_image() {
  require_cmd docker
  echo_info "Removing Docker image: $C7_IMAGE_NAME"
  docker rmi "$C7_IMAGE_NAME" || echo_warn "Failed to remove image."
}

function c7_register_mcp() {
  require_cmd claude
  require_cmd docker
  if ! docker image inspect "$C7_IMAGE_NAME" &>/dev/null; then
    echo_info "Docker image '$C7_IMAGE_NAME' not found – building first..."
    c7_build_image
  fi
  echo_info "Registering Context7 MCP with Claude Code"
  claude mcp add context7 -- docker run --rm -i -v "$C7_PROJECT_PATH:/app" "$C7_IMAGE_NAME"
  echo_success "Registered MCP 'context7'."
}

function c7_unregister_mcp() {
  require_cmd claude
  echo_info "Removing MCP 'context7' from Claude Code"
  claude mcp remove context7 && echo_success "Unregistered 'context7'." || echo_warn "Nothing to remove."
}

function context7_menu() {
  while true; do
    echo ""
    echo "===== Context7 MCP Options ====="
    echo "Project path: ${C7_PROJECT_PATH}"
    echo "================================"
    echo "1. Create Dockerfile (if missing)"
    echo "2. Build Docker image"
    echo "3. Run Context7 container"
    echo "4. Test if image exists"
    echo "5. Remove Docker image"
    echo "6. Register Context7 MCP with Claude Code"
    echo "7. Unregister Context7 MCP from Claude Code"
    echo "8. Back"
    echo "================================"
    read -rp "Choose option [1-8]: " opt
    case $opt in
      1) c7_create_dockerfile ;;
      2) c7_build_image ;;
      3) c7_run_container ;;
      4) c7_test_image_exists ;;
      5) c7_remove_image ;;
      6) c7_register_mcp ;;
      7) c7_unregister_mcp ;;
      8) break ;;
      *) echo_warn "Invalid option. Try again." ;;
    esac
  done
}

##############################################
# Serena MCP section
##############################################

SERENA_DIR="$HOME/tools/serena"
SUPPORTED_LANGS=("python" "typescript" "java" "csharp" "rust" "go" "ruby" "cpp" "php")
SERENA_PROJECT_CONFIG="$PROJECT_DIR/.serena/project.yml"
SERENA_DEPENDENCIES_FILE="$PROJECT_DIR/.serena/dependencies.txt"

function serena_check_installed() {
  if [[ -d "$SERENA_DIR" && -f "$SERENA_DIR/pyproject.toml" ]]; then
    echo_success "Serena is installed in $SERENA_DIR"
  else
    echo_error "Serena is NOT installed in $SERENA_DIR"
    exit 1
  fi
}

function serena_install() {
  require_cmd git
  echo_info "Installing Serena into $SERENA_DIR"
  mkdir -p "$HOME/tools"
  cd "$HOME/tools"
  if [ ! -d "$SERENA_DIR" ]; then
    git clone https://github.com/oraios/serena serena
  fi
  cd "$SERENA_DIR"

  if ! command -v uv &> /dev/null; then
    echo_info "Installing uv..."
    curl -Ls https://astral.sh/uv/install.sh | bash
    if [ -f "$HOME/.bashrc" ]; then
      # shellcheck disable=SC1090
      source "$HOME/.bashrc"
    fi
  fi

  echo_info "Creating uv virtual environment..."
  uv venv

  echo_info "Installing Serena with all extras..."
  uv pip install -e .[all-extras]

  echo_success "Serena installed successfully in $SERENA_DIR"
}

function serena_check_git_repo() {
  if ! git rev-parse --is-inside-work-tree &>/dev/null; then
    echo_warn "This is not a Git repository. MCP features may be limited."
  fi
}

function serena_ensure_project_config() {
  local has_source=false
  for ext in py ts java cs rs go rb cpp c php; do
    if find "$PROJECT_DIR" -type f -name "*.${ext}" | grep -q .; then
      has_source=true
      break
    fi
  done

  if [[ "$has_source" = false && ! -f "$SERENA_PROJECT_CONFIG" ]]; then
    echo_warn "No source files or project config found."
    echo_info "Creating .serena/project.yml"
    echo_info "Choose language:"
    select lang in "${SUPPORTED_LANGS[@]}"; do
      if [[ -n "$lang" ]]; then
        mkdir -p "$PROJECT_DIR/.serena"
        cat > "$SERENA_PROJECT_CONFIG" <<EOF
project_name: $PROJECT_NAME
language: $lang
EOF
        echo_success "Created $SERENA_PROJECT_CONFIG"
        break
      else
        echo_warn "Invalid selection. Try again."
      fi
    done
  fi
}

function serena_start() {
  serena_ensure_project_config
  serena_check_git_repo
  echo_info "Starting Serena MCP server for: $PROJECT_NAME"
  require_cmd uv
  uv run --directory "$SERENA_DIR" serena-mcp-server --context ide-assistant --project "$PROJECT_DIR"
}

function serena_start_with_index() {
  serena_ensure_project_config
  serena_check_git_repo
  echo_info "Starting Serena MCP server for: $PROJECT_NAME"
  require_cmd uv
  uv run --directory "$SERENA_DIR" serena-mcp-server --context ide-assistant --project "$PROJECT_DIR" &
  sleep 3
  echo_info "Triggering auto-indexing..."
  if command -v claude >/dev/null 2>&1; then
    claude mcp call serena index-project || echo_warn "Indexing failed or MCP not ready"
  else
    echo_warn "Claude CLI not found, skipping indexing call"
  fi
}

function serena_start_dev() {
  serena_ensure_project_config
  serena_check_git_repo
  echo_info "Starting Serena MCP in dev mode with dashboard + SSE"
  require_cmd uv
  uv run --directory "$SERENA_DIR" serena-mcp-server \
    --context ide-assistant \
    --project "$PROJECT_DIR" \
    --dev --sse --dashboard
}

function serena_start_dev_with_index() {
  serena_ensure_project_config
  serena_check_git_repo
  echo_info "Starting Serena MCP in dev mode with dashboard + SSE"
  require_cmd uv
  uv run --directory "$SERENA_DIR" serena-mcp-server \
    --context ide-assistant \
    --project "$PROJECT_DIR" \
    --dev --sse --dashboard &
  sleep 3
  echo_info "Triggering auto-indexing..."
  if command -v claude >/dev/null 2>&1; then
    claude mcp call serena index-project || echo_warn "Indexing failed or MCP not ready"
  else
    echo_warn "Claude CLI not found, skipping indexing call"
  fi
}

function serena_start_with_extra_projects() {
  serena_ensure_project_config
  serena_check_git_repo

  echo_info "Looking for additional project dependencies..."

  local EXTRA_PROJECTS=()
  if [[ -f "$SERENA_DEPENDENCIES_FILE" ]]; then
    mapfile -t EXTRA_PROJECTS < "$SERENA_DEPENDENCIES_FILE"
    echo_info "Using saved dependencies:"
    for p in "${EXTRA_PROJECTS[@]}"; do echo " - $p"; done
  else
    echo_info "Enter extra project paths (space-separated):"
    read -r -a EXTRA_PROJECTS
    mkdir -p "$(dirname "$SERENA_DEPENDENCIES_FILE")"
    printf "%s\n" "${EXTRA_PROJECTS[@]}" > "$SERENA_DEPENDENCIES_FILE"
    echo_success "Saved to $SERENA_DEPENDENCIES_FILE"
  fi

  echo_info "Starting MCP with extra projects..."
  require_cmd uv
  uv run --directory "$SERENA_DIR" serena-mcp-server \
    --context ide-assistant \
    --project "$PROJECT_DIR" \
    --extra-projects "${EXTRA_PROJECTS[@]}"
}

function serena_register_mcp() {
  require_cmd claude
  require_cmd uv
  echo_info "Registering Serena MCP with Claude Code"
  claude mcp add serena -- uv run --directory "$SERENA_DIR" serena-mcp-server --context ide-assistant --project "$PROJECT_DIR"
  echo_success "Registered successfully."
}

function serena_unregister_mcp() {
  require_cmd claude
  echo_info "Removing MCP 'serena' from Claude"
  claude mcp remove serena && echo_success "Unregistered successfully" || echo_warn "Nothing to remove"
}

function serena_menu() {
  while true; do
    echo ""
    echo "===== Serena MCP Options ====="
    echo "Project: ${PROJECT_NAME}"
    echo "Path:    ${PROJECT_DIR}"
    echo "================================"
    echo "1. Install Serena in WSL ($SERENA_DIR)"
    echo "2. Check if Serena is installed"
    echo "3. Register Serena MCP with Claude Code"
    echo "4. Unregister Serena MCP from Claude Code"
    echo "5. Start Serena MCP"
    echo "6. Start Serena MCP + index"
    echo "7. Start Serena MCP in dev mode"
    echo "8. Start Serena MCP in dev mode + index"
    echo "9. Start Serena MCP with extra projects"
    echo "0. Back"
    echo "================================"
    read -rp "Choose option [0-9]: " opt
    case $opt in
      1) serena_install ;;
      2) serena_check_installed ;;
      3) serena_register_mcp ;;
      4) serena_unregister_mcp ;;
      5) serena_start ;;
      6) serena_start_with_index ;;
      7) serena_start_dev ;;
      8) serena_start_dev_with_index ;;
      9) serena_start_with_extra_projects ;;
      0) break ;;
      *) echo_warn "Invalid option. Try again." ;;
    esac
  done
}

##############################################
# Playwright MCP section
##############################################

# Docker-based (analogous to Context7)
PW_IMAGE_NAME="playwright-mcp"
PW_DOCKERFILE_NAME="Dockerfile.playwright"
PW_CONTAINER_NAME="playwright-container"

function pw_create_dockerfile() {
  if [ ! -f "$PW_DOCKERFILE_NAME" ]; then
    echo_info "Creating $PW_DOCKERFILE_NAME..."
    cat > "$PW_DOCKERFILE_NAME" <<'EOF'
FROM node:20-bullseye
WORKDIR /app
# Install Playwright MCP + browsers
RUN npm i -g @playwright/mcp playwright && npx playwright install --with-deps
# Start the MCP server (stdio)
CMD ["npx","@playwright/mcp"]
EOF
  else
    echo_success "$PW_DOCKERFILE_NAME already exists – skipping"
  fi
}

function pw_build_image() {
  require_cmd docker
  echo_info "Building Docker image: $PW_IMAGE_NAME"
  docker build -f "$PW_DOCKERFILE_NAME" -t "$PW_IMAGE_NAME" .
}

function pw_run_container() {
  require_cmd docker
  echo_info "Starting container: $PW_IMAGE_NAME"
  docker run -it --rm \
    --shm-size=2g \
    --name "$PW_CONTAINER_NAME" \
    "$PW_IMAGE_NAME"
}

# Registration via NPX (simplest)
function pw_register_mcp_npx() {
  require_cmd claude
  require_cmd node
  echo_info "Registering Playwright MCP (NPX)"
  claude mcp add playwright -- npx '@playwright/mcp@latest'
  echo_success "Registered MCP 'playwright' via NPX."
}

# Registration via Docker (analogous to Context7)
function pw_register_mcp_docker() {
  require_cmd claude
  require_cmd docker
  if ! docker image inspect "$PW_IMAGE_NAME" &>/dev/null; then
    echo_info "Docker image '$PW_IMAGE_NAME' not found – building first..."
    pw_build_image
  fi
  echo_info "Registering Playwright MCP (Docker)"
  claude mcp add playwright -- docker run --rm -i --shm-size=2g "$PW_IMAGE_NAME"
  echo_success "Registered MCP 'playwright' via Docker."
}

function pw_unregister_mcp() {
  require_cmd claude
  echo_info "Removing MCP 'playwright' from Claude Code"
  claude mcp remove playwright && echo_success "Unregistered 'playwright'." || echo_warn "Nothing to remove."
}

function playwright_menu() {
  while true; do
    echo ""
    echo "===== Playwright MCP Options ====="
    echo "=================================="
    echo "1. Create Dockerfile (if missing)"
    echo "2. Build Docker image"
    echo "3. Run Playwright container"
    echo "4. Register Playwright MCP via NPX"
    echo "5. Register Playwright MCP via Docker"
    echo "6. Unregister Playwright MCP"
    echo "7. Back"
    echo "=================================="
    read -rp "Choose option [1-7]: " opt
    case $opt in
      1) pw_create_dockerfile ;;
      2) pw_build_image ;;
      3) pw_run_container ;;
      4) pw_register_mcp_npx ;;
      5) pw_register_mcp_docker ;;
      6) pw_unregister_mcp ;;
      7) break ;;
      *) echo_warn "Invalid option. Try again." ;;
    esac
  done
}

##############################################
# Top-level menu
##############################################

function main_menu() {
  while true; do
    echo ""
    echo "=========== MCP MANAGER ==========="
    echo "Version: 1.0.0"
    echo "Project: ${PROJECT_NAME}"
    echo "Path:    ${PROJECT_DIR}"
    echo "==================================="
    echo "1. Context7 MCP options"
    echo "2. Serena MCP options"
    echo "3. Playwright MCP options"
    echo "4. Exit"
    echo "==================================="
    read -rp "Choose option [1-4]: " opt
    case $opt in
      1) context7_menu ;;
      2) serena_menu ;;
      3) playwright_menu ;;
      4) echo_info "Bye"; exit 0 ;;
      *) echo_warn "Invalid option. Try again." ;;
    esac
  done
}

main_menu
