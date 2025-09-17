#!/bin/bash
#
# Claude Code Framework - Project Technology Detector
# Advanced technology stack detection and analysis
#

set -euo pipefail

# Colors and symbols
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'
CHECK="✅"
INFO="ℹ️"

# Detection results
declare -A DETECTED_TECH
CONFIDENCE_SCORES=()
PROJECT_INDICATORS=()

# Initialize detection system
init_detector() {
    local project_dir="$1"

    if [[ ! -d "$project_dir" ]]; then
        echo "Error: Project directory does not exist: $project_dir"
        exit 1
    fi

    echo -e "${INFO} Initializing technology detection for: ${CYAN}$project_dir${NC}"
}

# Frontend framework detection
detect_frontend() {
    local project_dir="$1"
    local confidence=0
    local frameworks=()

    # React detection
    if [[ -f "$project_dir/package.json" ]]; then
        if grep -q '"react"' "$project_dir/package.json"; then
            frameworks+=("react")
            confidence=$((confidence + 40))

            # React version detection
            local react_version=$(grep '"react"' "$project_dir/package.json" | sed 's/.*"react": *"[^0-9]*\([0-9]*\).*/\1/')
            if [[ "$react_version" -ge 18 ]]; then
                confidence=$((confidence + 10))
                DETECTED_TECH["react_version"]="$react_version+"
            fi

            # TypeScript with React
            if grep -q '"@types/react"' "$project_dir/package.json" || [[ -f "$project_dir/tsconfig.json" ]]; then
                confidence=$((confidence + 15))
                frameworks+=("typescript")
            fi
        fi
    fi

    # Angular detection
    if [[ -f "$project_dir/angular.json" ]]; then
        frameworks+=("angular")
        confidence=$((confidence + 50))

        # Angular version detection
        if [[ -f "$project_dir/package.json" ]] && grep -q '"@angular/core"' "$project_dir/package.json"; then
            local ng_version=$(grep '"@angular/core"' "$project_dir/package.json" | sed 's/.*"[^0-9]*\([0-9]*\).*/\1/')
            DETECTED_TECH["angular_version"]="$ng_version+"
            confidence=$((confidence + 10))
        fi
    fi

    # Vue.js detection
    if [[ -f "$project_dir/package.json" ]] && grep -q '"vue"' "$project_dir/package.json"; then
        frameworks+=("vue")
        confidence=$((confidence + 40))

        # Vue 3 detection
        local vue_version=$(grep '"vue"' "$project_dir/package.json" | sed 's/.*"vue": *"[^0-9]*\([0-9]*\).*/\1/')
        if [[ "$vue_version" -ge 3 ]]; then
            confidence=$((confidence + 10))
            DETECTED_TECH["vue_version"]="3+"
        fi
    fi

    # Svelte detection
    if [[ -f "$project_dir/package.json" ]] && grep -q '"svelte"' "$project_dir/package.json"; then
        frameworks+=("svelte")
        confidence=$((confidence + 35))
    fi

    # Next.js detection
    if [[ -f "$project_dir/package.json" ]] && grep -q '"next"' "$project_dir/package.json"; then
        frameworks+=("nextjs")
        confidence=$((confidence + 20))
    fi

    # Static site detection
    if [[ -f "$project_dir/index.html" ]] && [[ ! -f "$project_dir/package.json" ]]; then
        frameworks+=("static")
        confidence=$((confidence + 20))
    fi

    # CSS framework detection
    if [[ -f "$project_dir/package.json" ]]; then
        if grep -q '"tailwindcss"' "$project_dir/package.json"; then
            frameworks+=("tailwind")
            confidence=$((confidence + 5))
        fi
        if grep -q '"bootstrap"' "$project_dir/package.json"; then
            frameworks+=("bootstrap")
            confidence=$((confidence + 5))
        fi
    fi

    # Set detected frontend
    if [[ ${#frameworks[@]} -gt 0 ]]; then
        DETECTED_TECH["frontend"]=$(IFS=,; echo "${frameworks[*]}")
        DETECTED_TECH["frontend_confidence"]="$confidence"
    fi
}

# Backend technology detection
detect_backend() {
    local project_dir="$1"
    local confidence=0
    local technologies=()

    # Node.js detection
    if [[ -f "$project_dir/package.json" ]]; then
        technologies+=("nodejs")
        confidence=$((confidence + 30))

        # Express.js detection
        if grep -q '"express"' "$project_dir/package.json"; then
            technologies+=("express")
            confidence=$((confidence + 20))
        fi

        # NestJS detection
        if grep -q '"@nestjs"' "$project_dir/package.json"; then
            technologies+=("nestjs")
            confidence=$((confidence + 25))
        fi

        # Fastify detection
        if grep -q '"fastify"' "$project_dir/package.json"; then
            technologies+=("fastify")
            confidence=$((confidence + 20))
        fi
    fi

    # Python detection
    if [[ -f "$project_dir/requirements.txt" ]] || [[ -f "$project_dir/pyproject.toml" ]] || [[ -f "$project_dir/Pipfile" ]]; then
        technologies+=("python")
        confidence=$((confidence + 40))

        # Django detection
        if [[ -f "$project_dir/manage.py" ]] || grep -q "django" "$project_dir/requirements.txt" 2>/dev/null; then
            technologies+=("django")
            confidence=$((confidence + 25))
        fi

        # FastAPI detection
        if grep -q "fastapi" "$project_dir/requirements.txt" 2>/dev/null || grep -q "fastapi" "$project_dir/pyproject.toml" 2>/dev/null; then
            technologies+=("fastapi")
            confidence=$((confidence + 25))
        fi

        # Flask detection
        if grep -q "flask" "$project_dir/requirements.txt" 2>/dev/null; then
            technologies+=("flask")
            confidence=$((confidence + 20))
        fi
    fi

    # Java detection
    if [[ -f "$project_dir/pom.xml" ]] || [[ -f "$project_dir/build.gradle" ]]; then
        technologies+=("java")
        confidence=$((confidence + 40))

        # Spring Boot detection
        if grep -q "spring-boot" "$project_dir/pom.xml" 2>/dev/null || grep -q "spring-boot" "$project_dir/build.gradle" 2>/dev/null; then
            technologies+=("spring-boot")
            confidence=$((confidence + 25))
        fi
    fi

    # .NET detection
    if [[ -f "$project_dir"/*.csproj ]] || [[ -f "$project_dir"/*.sln ]]; then
        technologies+=("dotnet")
        confidence=$((confidence + 40))

        # ASP.NET Core detection
        if grep -q "Microsoft.AspNetCore" "$project_dir"/*.csproj 2>/dev/null; then
            technologies+=("aspnet-core")
            confidence=$((confidence + 25))
        fi
    fi

    # Go detection
    if [[ -f "$project_dir/go.mod" ]]; then
        technologies+=("go")
        confidence=$((confidence + 40))

        # Gin detection
        if grep -q "gin-gonic/gin" "$project_dir/go.mod"; then
            technologies+=("gin")
            confidence=$((confidence + 20))
        fi
    fi

    # Rust detection
    if [[ -f "$project_dir/Cargo.toml" ]]; then
        technologies+=("rust")
        confidence=$((confidence + 40))

        # Actix Web detection
        if grep -q "actix-web" "$project_dir/Cargo.toml"; then
            technologies+=("actix-web")
            confidence=$((confidence + 20))
        fi
    fi

    # PHP detection
    if [[ -f "$project_dir/composer.json" ]] || find "$project_dir" -name "*.php" -type f | head -1 | grep -q php; then
        technologies+=("php")
        confidence=$((confidence + 35))

        # Laravel detection
        if [[ -f "$project_dir/artisan" ]] || grep -q "laravel/framework" "$project_dir/composer.json" 2>/dev/null; then
            technologies+=("laravel")
            confidence=$((confidence + 25))
        fi
    fi

    # Set detected backend
    if [[ ${#technologies[@]} -gt 0 ]]; then
        DETECTED_TECH["backend"]=$(IFS=,; echo "${technologies[*]}")
        DETECTED_TECH["backend_confidence"]="$confidence"
    fi
}

# Database technology detection
detect_database() {
    local project_dir="$1"
    local confidence=0
    local databases=()

    # Check configuration files and dependencies
    if [[ -f "$project_dir/package.json" ]]; then
        if grep -q '"pg"\|"postgres"' "$project_dir/package.json"; then
            databases+=("postgresql")
            confidence=$((confidence + 25))
        fi
        if grep -q '"mysql"' "$project_dir/package.json"; then
            databases+=("mysql")
            confidence=$((confidence + 25))
        fi
        if grep -q '"mongodb"\|"mongoose"' "$project_dir/package.json"; then
            databases+=("mongodb")
            confidence=$((confidence + 25))
        fi
        if grep -q '"redis"' "$project_dir/package.json"; then
            databases+=("redis")
            confidence=$((confidence + 15))
        fi
        if grep -q '"sqlite"' "$project_dir/package.json"; then
            databases+=("sqlite")
            confidence=$((confidence + 20))
        fi
    fi

    # Python database detection
    if [[ -f "$project_dir/requirements.txt" ]]; then
        if grep -q "psycopg2\|postgresql" "$project_dir/requirements.txt"; then
            databases+=("postgresql")
            confidence=$((confidence + 25))
        fi
        if grep -q "mysql\|pymysql" "$project_dir/requirements.txt"; then
            databases+=("mysql")
            confidence=$((confidence + 25))
        fi
        if grep -q "pymongo" "$project_dir/requirements.txt"; then
            databases+=("mongodb")
            confidence=$((confidence + 25))
        fi
        if grep -q "redis" "$project_dir/requirements.txt"; then
            databases+=("redis")
            confidence=$((confidence + 15))
        fi
    fi

    # Docker compose detection
    if [[ -f "$project_dir/docker-compose.yml" ]] || [[ -f "$project_dir/docker-compose.yaml" ]]; then
        local compose_file=""
        [[ -f "$project_dir/docker-compose.yml" ]] && compose_file="$project_dir/docker-compose.yml"
        [[ -f "$project_dir/docker-compose.yaml" ]] && compose_file="$project_dir/docker-compose.yaml"

        if [[ -n "$compose_file" ]]; then
            if grep -q "postgres" "$compose_file"; then
                databases+=("postgresql")
                confidence=$((confidence + 20))
            fi
            if grep -q "mysql" "$compose_file"; then
                databases+=("mysql")
                confidence=$((confidence + 20))
            fi
            if grep -q "mongo" "$compose_file"; then
                databases+=("mongodb")
                confidence=$((confidence + 20))
            fi
            if grep -q "redis" "$compose_file"; then
                databases+=("redis")
                confidence=$((confidence + 15))
            fi
        fi
    fi

    # Database files detection
    if find "$project_dir" -name "*.db" -o -name "*.sqlite" -o -name "*.sqlite3" | head -1 | grep -q .; then
        databases+=("sqlite")
        confidence=$((confidence + 30))
    fi

    # Set detected databases
    if [[ ${#databases[@]} -gt 0 ]]; then
        DETECTED_TECH["database"]=$(IFS=,; echo "${databases[*]}")
        DETECTED_TECH["database_confidence"]="$confidence"
    fi
}

# Infrastructure and deployment detection
detect_infrastructure() {
    local project_dir="$1"
    local confidence=0
    local infrastructure=()

    # Docker detection
    if [[ -f "$project_dir/Dockerfile" ]]; then
        infrastructure+=("docker")
        confidence=$((confidence + 30))
    fi

    if [[ -f "$project_dir/docker-compose.yml" ]] || [[ -f "$project_dir/docker-compose.yaml" ]]; then
        infrastructure+=("docker-compose")
        confidence=$((confidence + 25))
    fi

    # Kubernetes detection
    if find "$project_dir" -name "*.yaml" -o -name "*.yml" | xargs grep -l "apiVersion:\|kind:" 2>/dev/null | head -1 | grep -q .; then
        infrastructure+=("kubernetes")
        confidence=$((confidence + 25))
    fi

    # CI/CD detection
    if [[ -d "$project_dir/.github/workflows" ]]; then
        infrastructure+=("github-actions")
        confidence=$((confidence + 20))
    fi

    if [[ -f "$project_dir/.gitlab-ci.yml" ]]; then
        infrastructure+=("gitlab-ci")
        confidence=$((confidence + 20))
    fi

    if [[ -f "$project_dir/Jenkinsfile" ]]; then
        infrastructure+=("jenkins")
        confidence=$((confidence + 20))
    fi

    # Cloud platform detection
    if [[ -f "$project_dir/vercel.json" ]] || grep -q "vercel" "$project_dir/package.json" 2>/dev/null; then
        infrastructure+=("vercel")
        confidence=$((confidence + 15))
    fi

    if [[ -f "$project_dir/netlify.toml" ]]; then
        infrastructure+=("netlify")
        confidence=$((confidence + 15))
    fi

    # Terraform detection
    if find "$project_dir" -name "*.tf" | head -1 | grep -q .; then
        infrastructure+=("terraform")
        confidence=$((confidence + 25))
    fi

    # Set detected infrastructure
    if [[ ${#infrastructure[@]} -gt 0 ]]; then
        DETECTED_TECH["infrastructure"]=$(IFS=,; echo "${infrastructure[*]}")
        DETECTED_TECH["infrastructure_confidence"]="$confidence"
    fi
}

# Business domain inference
detect_business_domain() {
    local project_dir="$1"
    local confidence=0
    local domain="general"

    # Check for domain-specific files and directories
    local project_name=$(basename "$project_dir")
    local readme_content=""

    # Read README if exists
    if [[ -f "$project_dir/README.md" ]]; then
        readme_content=$(cat "$project_dir/README.md" | tr '[:upper:]' '[:lower:]')
    elif [[ -f "$project_dir/readme.md" ]]; then
        readme_content=$(cat "$project_dir/readme.md" | tr '[:upper:]' '[:lower:]')
    fi

    # E-commerce indicators
    if echo "$readme_content $project_name" | grep -q "shop\|store\|cart\|payment\|checkout\|ecommerce\|e-commerce"; then
        domain="ecommerce"
        confidence=$((confidence + 30))
    fi

    # FinTech indicators
    if echo "$readme_content $project_name" | grep -q "bank\|finance\|payment\|trading\|crypto\|wallet\|fintech"; then
        domain="fintech"
        confidence=$((confidence + 30))
    fi

    # Healthcare indicators
    if echo "$readme_content $project_name" | grep -q "health\|medical\|patient\|hospital\|clinic\|healthcare"; then
        domain="healthcare"
        confidence=$((confidence + 30))
    fi

    # Education indicators
    if echo "$readme_content $project_name" | grep -q "school\|education\|learning\|course\|student\|teacher"; then
        domain="education"
        confidence=$((confidence + 30))
    fi

    # Gaming indicators
    if echo "$readme_content $project_name" | grep -q "game\|gaming\|player\|score\|level"; then
        domain="gaming"
        confidence=$((confidence + 30))
    fi

    # Social media indicators
    if echo "$readme_content $project_name" | grep -q "social\|chat\|message\|post\|follow\|friend"; then
        domain="social"
        confidence=$((confidence + 25))
    fi

    # Enterprise indicators
    if echo "$readme_content $project_name" | grep -q "enterprise\|corporate\|business\|management\|admin\|dashboard"; then
        domain="enterprise"
        confidence=$((confidence + 25))
    fi

    DETECTED_TECH["business_domain"]="$domain"
    DETECTED_TECH["domain_confidence"]="$confidence"
}

# Project scale assessment
assess_project_scale() {
    local project_dir="$1"
    local confidence=0
    local scale="sme"

    # Count project files (excluding node_modules, .git, etc.)
    local file_count=$(find "$project_dir" -type f \
        ! -path "*/node_modules/*" \
        ! -path "*/.git/*" \
        ! -path "*/vendor/*" \
        ! -path "*/target/*" \
        ! -path "*/build/*" \
        ! -path "*/dist/*" \
        | wc -l)

    # Directory structure complexity
    local dir_depth=$(find "$project_dir" -type d \
        ! -path "*/node_modules/*" \
        ! -path "*/.git/*" \
        ! -path "*/vendor/*" \
        | awk -F/ 'NF > max_depth {max_depth = NF} END {print max_depth}')

    # Scale assessment based on file count and structure
    if [[ $file_count -lt 50 ]] && [[ $dir_depth -lt 4 ]]; then
        scale="startup"
        confidence=$((confidence + 25))
    elif [[ $file_count -gt 500 ]] || [[ $dir_depth -gt 6 ]]; then
        scale="enterprise"
        confidence=$((confidence + 25))
    else
        scale="sme"
        confidence=$((confidence + 30))
    fi

    # Enterprise indicators
    if [[ -f "$project_dir/docker-compose.yml" ]] || [[ -d "$project_dir/.github" ]] || [[ -f "$project_dir/Jenkinsfile" ]]; then
        scale="enterprise"
        confidence=$((confidence + 15))
    fi

    # Microservices indicators
    if find "$project_dir" -name "service.yml" -o -name "*-service*" | head -1 | grep -q .; then
        scale="enterprise"
        confidence=$((confidence + 20))
    fi

    DETECTED_TECH["project_scale"]="$scale"
    DETECTED_TECH["scale_confidence"]="$confidence"
}

# Generate comprehensive detection report
generate_report() {
    echo -e "\n${CHECK} ${GREEN}TECHNOLOGY DETECTION COMPLETE${NC}"
    echo "================================================================================"

    # Frontend technologies
    if [[ -n "${DETECTED_TECH[frontend]:-}" ]]; then
        echo -e "${INFO} ${BLUE}Frontend:${NC} ${DETECTED_TECH[frontend]} (confidence: ${DETECTED_TECH[frontend_confidence]}%)"
    fi

    # Backend technologies
    if [[ -n "${DETECTED_TECH[backend]:-}" ]]; then
        echo -e "${INFO} ${BLUE}Backend:${NC} ${DETECTED_TECH[backend]} (confidence: ${DETECTED_TECH[backend_confidence]}%)"
    fi

    # Database technologies
    if [[ -n "${DETECTED_TECH[database]:-}" ]]; then
        echo -e "${INFO} ${BLUE}Database:${NC} ${DETECTED_TECH[database]} (confidence: ${DETECTED_TECH[database_confidence]}%)"
    fi

    # Infrastructure
    if [[ -n "${DETECTED_TECH[infrastructure]:-}" ]]; then
        echo -e "${INFO} ${BLUE}Infrastructure:${NC} ${DETECTED_TECH[infrastructure]} (confidence: ${DETECTED_TECH[infrastructure_confidence]}%)"
    fi

    # Business domain and scale
    echo -e "${INFO} ${BLUE}Business Domain:${NC} ${DETECTED_TECH[business_domain]} (confidence: ${DETECTED_TECH[domain_confidence]}%)"
    echo -e "${INFO} ${BLUE}Project Scale:${NC} ${DETECTED_TECH[project_scale]} (confidence: ${DETECTED_TECH[scale_confidence]}%)"
}

# Main detection function
detect_project_technologies() {
    local project_dir="$1"

    init_detector "$project_dir"

    echo -e "${INFO} Running comprehensive technology detection..."

    detect_frontend "$project_dir"
    detect_backend "$project_dir"
    detect_database "$project_dir"
    detect_infrastructure "$project_dir"
    detect_business_domain "$project_dir"
    assess_project_scale "$project_dir"

    generate_report

    # Return detection results as JSON-like format for easy parsing
    echo "DETECTION_RESULTS_START"
    for key in "${!DETECTED_TECH[@]}"; do
        echo "$key=${DETECTED_TECH[$key]}"
    done
    echo "DETECTION_RESULTS_END"
}

# Execute if run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    if [[ $# -lt 1 ]]; then
        echo "Usage: $0 <project_directory>"
        exit 1
    fi

    detect_project_technologies "$1"
fi