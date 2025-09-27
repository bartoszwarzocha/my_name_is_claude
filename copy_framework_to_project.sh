#!/bin/bash

# =============================================================================
# CLAUDE CODE MULTI-AGENT FRAMEWORK - PROJECT COPY SCRIPT
# =============================================================================
#
# Copies essential framework files to a target project directory.
# Handles both new and existing projects with safety checks.
#
# Version: 1.0.0
# Framework: Claude Code Multi-Agent Framework v3.1.0
# =============================================================================

set -e

# =============================================================================
# CONFIGURATION
# =============================================================================

readonly SCRIPT_VERSION="1.1.0"
readonly FRAMEWORK_VERSION="3.2.0"
readonly SCRIPT_NAME="Framework Copy Script"

# Colors for output
readonly COLOR_RED=$(tput setaf 1)
readonly COLOR_GREEN=$(tput setaf 2)
readonly COLOR_YELLOW=$(tput setaf 3)
readonly COLOR_BLUE=$(tput setaf 4)
readonly COLOR_CYAN=$(tput setaf 6)
readonly COLOR_WHITE=$(tput setaf 7)
readonly COLOR_BOLD=$(tput bold)
readonly COLOR_RESET=$(tput sgr0)

# Icons
readonly ICON_CHECK="✅"
readonly ICON_WARN="⚠️"
readonly ICON_ERROR="❌"
readonly ICON_INFO="ℹ️"
readonly ICON_COPY="📋"

# Framework source directory (current directory)
readonly SOURCE_DIR="$(pwd)"
readonly TARGET_DIR="${1:-}"

# Essential framework files and directories to copy
readonly ESSENTIAL_DIRS=(
    ".ai-tools"
    ".claude"
    ".mcp-tools"
    "init_concept"
)

readonly ESSENTIAL_FILES=(
    "ai-tools.sh"
    "mcp-tools.sh"
    "VERSION"
    "CLAUDE_template.md"
    "copy_framework_to_project.sh"
)

# Special files with name changes
readonly SPECIAL_FILES=(
    "LICENSE:FRAMEWORK_LICENSE"
    "README.md:FRAMEWORK_README.md"
    "CHANGELOG.md:FRAMEWORK_CHANGELOG.md"
    "FRAMEWORK_ROADMAP.md:FRAMEWORK_ROADMAP.md"
)

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

print_status() {
    local status="$1"
    local message="$2"
    case "$status" in
        "success") echo "${ICON_CHECK} ${COLOR_GREEN}${message}${COLOR_RESET}" ;;
        "warning") echo "${ICON_WARN} ${COLOR_YELLOW}${message}${COLOR_RESET}" ;;
        "error")   echo "${ICON_ERROR} ${COLOR_RED}${message}${COLOR_RESET}" ;;
        "info")    echo "${ICON_INFO} ${COLOR_CYAN}${message}${COLOR_RESET}" ;;
        "copy")    echo "${ICON_COPY} ${COLOR_WHITE}${message}${COLOR_RESET}" ;;
        *)         echo "${message}" ;;
    esac
}

print_header() {
    echo ""
    echo "${COLOR_BLUE}${COLOR_BOLD}===============================================================================${COLOR_RESET}"
    echo "${COLOR_BLUE}${COLOR_BOLD}${ICON_COPY} CLAUDE CODE MULTI-AGENT FRAMEWORK - COPY SCRIPT${COLOR_RESET}"
    echo "${COLOR_CYAN}Copy Essential Framework Files to Target Project${COLOR_RESET}"
    echo "${COLOR_BLUE}${COLOR_BOLD}===============================================================================${COLOR_RESET}"
    echo ""
    echo "${COLOR_GREEN}Framework:${COLOR_RESET} Claude Code Multi-Agent Framework v${FRAMEWORK_VERSION}"
    echo "${COLOR_GREEN}Script:${COLOR_RESET} ${SCRIPT_NAME} v${SCRIPT_VERSION}"
    echo "${COLOR_GREEN}Source:${COLOR_RESET} ${SOURCE_DIR}"
    echo "${COLOR_GREEN}Target:${COLOR_RESET} ${TARGET_DIR:-Not specified}"
    echo ""
}

show_usage() {
    echo "${COLOR_CYAN}${COLOR_BOLD}Usage:${COLOR_RESET}"
    echo "  $0 <target_directory> [options]"
    echo ""
    echo "${COLOR_CYAN}${COLOR_BOLD}Options:${COLOR_RESET}"
    echo "  --dry-run     Show what would be copied without actually copying"
    echo "  --force       Skip confirmation prompts"
    echo "  --backup      Create backups of existing files before overwriting"
    echo "  --help        Show this help message"
    echo ""
    echo "${COLOR_CYAN}${COLOR_BOLD}Examples:${COLOR_RESET}"
    echo "  $0 /path/to/my-project"
    echo "  $0 ../new-project --dry-run"
    echo "  $0 /existing/project --backup --force"
    echo ""
}

validate_source() {
    print_status "info" "Validating source framework directory..."

    local missing_items=()

    # Check essential directories
    for dir in "${ESSENTIAL_DIRS[@]}"; do
        if [[ ! -d "$SOURCE_DIR/$dir" ]]; then
            missing_items+=("Directory: $dir")
        fi
    done

    # Check essential files
    for file in "${ESSENTIAL_FILES[@]}"; do
        if [[ ! -f "$SOURCE_DIR/$file" ]]; then
            missing_items+=("File: $file")
        fi
    done

    # Check special files
    for item in "${SPECIAL_FILES[@]}"; do
        local source_file="${item%%:*}"
        if [[ ! -f "$SOURCE_DIR/$source_file" ]]; then
            missing_items+=("File: $source_file")
        fi
    done

    if [[ ${#missing_items[@]} -gt 0 ]]; then
        print_status "error" "Missing essential framework components:"
        for item in "${missing_items[@]}"; do
            echo "  ${ICON_ERROR} $item"
        done
        return 1
    fi

    print_status "success" "Source framework validation passed"
    return 0
}

validate_target() {
    local target="$1"

    if [[ -z "$target" ]]; then
        print_status "error" "Target directory not specified"
        show_usage
        return 1
    fi

    # Convert to absolute path
    target="$(cd "$(dirname "$target")" 2>/dev/null && pwd)/$(basename "$target")" || return 1

    if [[ ! -d "$target" ]]; then
        print_status "warning" "Target directory does not exist: $target"
        read -p "Create target directory? (y/N): " -r
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            mkdir -p "$target" || {
                print_status "error" "Failed to create target directory"
                return 1
            }
            print_status "success" "Created target directory: $target"
        else
            print_status "error" "Cannot proceed without target directory"
            return 1
        fi
    fi

    print_status "success" "Target directory validated: $target"
    return 0
}

check_conflicts() {
    local target="$1"
    local conflicts=()

    print_status "info" "Checking for potential conflicts in target directory..."

    # Check directories
    for dir in "${ESSENTIAL_DIRS[@]}"; do
        if [[ -d "$target/$dir" ]]; then
            conflicts+=("Directory: $dir")
        fi
    done

    # Check files
    for file in "${ESSENTIAL_FILES[@]}"; do
        if [[ -f "$target/$file" ]]; then
            conflicts+=("File: $file")
        fi
    done

    # Check special files (target names)
    for item in "${SPECIAL_FILES[@]}"; do
        local target_file="${item##*:}"
        if [[ -f "$target/$target_file" ]]; then
            conflicts+=("File: $target_file")
        fi
    done

    if [[ ${#conflicts[@]} -gt 0 ]]; then
        print_status "warning" "Found existing files that will be overwritten:"
        for conflict in "${conflicts[@]}"; do
            echo "  ${ICON_WARN} $conflict"
        done
        echo ""
        return 1
    fi

    print_status "success" "No conflicts detected"
    return 0
}

create_backup() {
    local file="$1"
    local backup_file="${file}.backup.$(date +%Y%m%d_%H%M%S)"

    if [[ -e "$file" ]]; then
        cp -r "$file" "$backup_file"
        print_status "info" "Backed up: $(basename "$file") → $(basename "$backup_file")"
        return 0
    fi
    return 1
}

copy_item() {
    local source="$1"
    local target="$2"
    local item_type="$3"
    local backup_mode="$4"

    if [[ "$backup_mode" == "true" ]] && [[ -e "$target" ]]; then
        create_backup "$target"
    fi

    if [[ "$item_type" == "directory" ]]; then
        # Special handling for different directories
        local dir_name="$(basename "$source")"

        if [[ "$dir_name" == ".ai-tools" ]]; then
            print_status "copy" "Copying .ai-tools directory (excluding virtual environment)..."
            mkdir -p "$target"

            # Copy all subdirectories except venv/
            for item in "$source"/*; do
                if [[ -e "$item" ]]; then
                    local item_name="$(basename "$item")"
                    if [[ "$item_name" != "venv" ]]; then
                        cp -r "$item" "$target/"
                        print_status "copy" "  ✓ $(basename "$item")"
                    else
                        print_status "info" "  ⏭ Skipping virtual environment (venv/)"
                    fi
                fi
            done
            print_status "success" "Completed .ai-tools directory copy"

        elif [[ "$dir_name" == ".claude" ]]; then
            print_status "copy" "Copying .claude directory (excluding monitoring and sensitive files)..."
            mkdir -p "$target"

            # Copy specific subdirectories only
            local claude_dirs=("agents" "prompts" "commands" "hooks" "templates" "assets" "docs")
            for subdir in "${claude_dirs[@]}"; do
                if [[ -d "$source/$subdir" ]]; then
                    cp -r "$source/$subdir" "$target/"
                    print_status "copy" "  ✓ $subdir"
                fi
            done

            # Copy settings.local.json if it exists
            if [[ -f "$source/settings.local.json" ]]; then
                cp "$source/settings.local.json" "$target/"
                print_status "copy" "  ✓ settings.local.json"
            fi

            print_status "info" "  ⏭ Skipping monitoring/ (enterprise internal)"
            print_status "info" "  ⏭ Skipping docs/ (framework internal)"
            print_status "success" "Completed .claude directory copy"

        else
            cp -r "$source" "$target"
            print_status "copy" "Copied directory: $(basename "$source")"
        fi
    else
        cp "$source" "$target"
        print_status "copy" "Copied file: $(basename "$source") → $(basename "$target")"
    fi
}

update_gitignore() {
    local target="$1"
    local gitignore_path="$target/.gitignore"

    print_status "info" "Updating .gitignore in target project..."

    # Check if .gitignore exists, create if not
    if [[ ! -f "$gitignore_path" ]]; then
        print_status "info" "Creating .gitignore file in target project"
        touch "$gitignore_path"
    fi

    # Check if framework section already exists
    if grep -q "# My Name Is Claude Framework Files" "$gitignore_path" 2>/dev/null; then
        print_status "warning" "Framework section already exists in .gitignore, skipping update"
        return 0
    fi

    # Add framework section to .gitignore
    cat >> "$gitignore_path" << 'EOF'

# =============================================================================
# My Name Is Claude Framework Files
# =============================================================================
# These files are copied from the My Name Is Claude framework and should not
# be tracked in this project's git repository. They are managed separately.

# Framework directories
.ai-tools/
.claude/
.mcp-tools/
init_concept/

# Framework scripts and files
ai-tools.sh
mcp-tools.sh
VERSION
CLAUDE_template.md
copy_framework_to_project.sh

# Framework documentation
FRAMEWORK_LICENSE
FRAMEWORK_README.md
FRAMEWORK_CHANGELOG.md
FRAMEWORK_ROADMAP.md

# End My Name Is Claude Framework Files
# =============================================================================
EOF

    print_status "success" "Added framework files to .gitignore"
    return 0
}

perform_copy() {
    local target="$1"
    local dry_run="$2"
    local backup_mode="$3"

    print_status "info" "Starting framework copy operation..."
    echo ""

    if [[ "$dry_run" == "true" ]]; then
        print_status "info" "${COLOR_YELLOW}DRY RUN MODE - No files will be actually copied${COLOR_RESET}"
        echo ""
    fi

    # Copy directories
    print_status "info" "Copying essential directories..."
    for dir in "${ESSENTIAL_DIRS[@]}"; do
        local source="$SOURCE_DIR/$dir"
        local target_path="$target/$dir"

        if [[ "$dry_run" == "true" ]]; then
            print_status "copy" "[DRY RUN] Would copy directory: $dir"
        else
            copy_item "$source" "$target_path" "directory" "$backup_mode"
        fi
    done

    echo ""

    # Copy files
    print_status "info" "Copying essential files..."
    for file in "${ESSENTIAL_FILES[@]}"; do
        local source="$SOURCE_DIR/$file"
        local target_path="$target/$file"

        if [[ "$dry_run" == "true" ]]; then
            print_status "copy" "[DRY RUN] Would copy file: $file"
        else
            copy_item "$source" "$target_path" "file" "$backup_mode"
        fi
    done

    echo ""

    # Copy special files with name changes
    print_status "info" "Copying special files with name changes..."
    for item in "${SPECIAL_FILES[@]}"; do
        local source_file="${item%%:*}"
        local target_file="${item##*:}"
        local source="$SOURCE_DIR/$source_file"
        local target_path="$target/$target_file"

        if [[ "$dry_run" == "true" ]]; then
            print_status "copy" "[DRY RUN] Would copy: $source_file → $target_file"
        else
            copy_item "$source" "$target_path" "file" "$backup_mode"
        fi
    done

    echo ""

    if [[ "$dry_run" == "true" ]]; then
        print_status "info" "Dry run completed. Use without --dry-run to perform actual copy."
        print_status "info" "Note: .gitignore would also be updated to exclude framework files."
    else
        print_status "success" "Framework copy completed successfully!"

        # Update .gitignore to exclude copied framework files
        echo ""
        update_gitignore "$target"

        echo ""
        print_status "info" "Next steps:"
        echo "  1. Navigate to: $target"
        echo "  2. Review CLAUDE_template.md and customize as CLAUDE.md for your project"
        echo "  3. Run: ./ai-tools.sh to start using the framework"
        echo "  4. Setup MCP tools: ./mcp-tools.sh"
        echo "  5. Check FRAMEWORK_LICENSE for framework licensing terms"
        echo "  6. Read FRAMEWORK_README.md for complete framework documentation"
        echo "  7. Framework files have been added to .gitignore automatically"
    fi
}

# =============================================================================
# MAIN SCRIPT
# =============================================================================

main() {
    local dry_run="false"
    local force_mode="false"
    local backup_mode="false"
    local target_dir=""

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --dry-run)
                dry_run="true"
                shift
                ;;
            --force)
                force_mode="true"
                shift
                ;;
            --backup)
                backup_mode="true"
                shift
                ;;
            --help)
                print_header
                show_usage
                exit 0
                ;;
            -*)
                print_status "error" "Unknown option: $1"
                show_usage
                exit 1
                ;;
            *)
                if [[ -z "$target_dir" ]]; then
                    target_dir="$1"
                else
                    print_status "error" "Multiple target directories specified"
                    show_usage
                    exit 1
                fi
                shift
                ;;
        esac
    done

    print_header

    # Validate inputs
    if ! validate_source; then
        print_status "error" "Source validation failed"
        exit 1
    fi

    if ! validate_target "$target_dir"; then
        print_status "error" "Target validation failed"
        exit 1
    fi

    # Convert target to absolute path
    target_dir="$(cd "$target_dir" && pwd)"

    # Check for conflicts
    local has_conflicts="false"
    if ! check_conflicts "$target_dir"; then
        has_conflicts="true"
    fi

    # Get confirmation if not in force mode
    if [[ "$force_mode" != "true" ]] && [[ "$dry_run" != "true" ]]; then
        echo ""
        if [[ "$has_conflicts" == "true" ]]; then
            if [[ "$backup_mode" == "true" ]]; then
                print_status "warning" "Existing files will be backed up before overwriting."
            else
                print_status "warning" "Existing files will be OVERWRITTEN without backup."
            fi
        fi

        echo ""
        read -p "Proceed with copying framework to $target_dir? (y/N): " -r
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_status "info" "Operation cancelled by user"
            exit 0
        fi
    fi

    # Perform the copy
    perform_copy "$target_dir" "$dry_run" "$backup_mode"
}

# Run main function with all arguments
main "$@"