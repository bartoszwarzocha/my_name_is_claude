#!/bin/bash

# Technology Stack Workflow Adaptation Engine
# Part of Intelligent Project Workflow Generation System
# Adapts workflows to specific technology stacks and integration patterns

set -euo pipefail

# Color codes for professional output
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly PURPLE='\033[0;35m'
readonly CYAN='\033[0;36m'
readonly WHITE='\033[1;37m'
readonly NC='\033[0m' # No Color

# Stack adapter configuration
readonly STACK_PATTERNS_DIR="$(dirname "$0")/stack_patterns"
readonly OUTPUT_DIR="./workflow_output"

# Logging functions
log_info() { echo -e "${CYAN}ℹ️  INFO:${NC} $*" >&2; }
log_success() { echo -e "${GREEN}✅ SUCCESS:${NC} $*" >&2; }
log_warning() { echo -e "${YELLOW}⚠️  WARNING:${NC} $*" >&2; }
log_error() { echo -e "${RED}❌ ERROR:${NC} $*" >&2; }

# Create output directory if it doesn't exist
create_output_directory() {
    [[ ! -d "$OUTPUT_DIR" ]] && mkdir -p "$OUTPUT_DIR"
}

# Load project technology stack analysis
load_technology_analysis() {
    local project_dir="${1:-$PWD}"
    local analysis_file="$OUTPUT_DIR/technology_analysis.json"

    if [[ -f "$analysis_file" ]]; then
        log_info "Loading existing technology analysis from $analysis_file"
        cat "$analysis_file"
    else
        log_info "Technology analysis not found. Running project detection..."

        # Check if project_detector.sh exists and run it
        local detector_path="$(dirname "$0")/../setup/project_detector.sh"
        if [[ -x "$detector_path" ]]; then
            # Generate comprehensive technology analysis
            generate_technology_analysis "$project_dir" "$detector_path"
        else
            log_error "Cannot load technology analysis. Please run project detection first."
            return 1
        fi
    fi
}

# Generate comprehensive technology analysis
generate_technology_analysis() {
    local project_dir="$1"
    local detector_path="$2"
    local analysis_file="$OUTPUT_DIR/technology_analysis.json"

    log_info "Generating comprehensive technology stack analysis"

    # Run existing project detection
    local basic_analysis
    basic_analysis=$(cd "$project_dir" && "$detector_path" --json)

    # Enhance with detailed technology integration analysis
    local enhanced_analysis
    enhanced_analysis=$(analyze_technology_integration "$project_dir" "$basic_analysis")

    # Save enhanced analysis
    echo "$enhanced_analysis" | jq '.' > "$analysis_file"
    echo "$enhanced_analysis"
}

# Analyze technology integration patterns and dependencies
analyze_technology_integration() {
    local project_dir="$1"
    local basic_analysis="$2"

    log_info "Analyzing technology integration patterns and dependencies"

    # Extract basic information
    local frontend_tech
    local backend_tech
    local database_tech
    local additional_tech

    frontend_tech=$(echo "$basic_analysis" | jq -r '.frontend.primary // "none"')
    backend_tech=$(echo "$basic_analysis" | jq -r '.backend.primary // "none"')
    database_tech=$(echo "$basic_analysis" | jq -r '.database.primary // "none"')
    additional_tech=$(echo "$basic_analysis" | jq '.additional_technologies // []')

    # Analyze integration complexity
    local integration_complexity
    integration_complexity=$(assess_integration_complexity "$frontend_tech" "$backend_tech" "$database_tech" "$additional_tech")

    # Identify technology-specific workflow requirements
    local workflow_requirements
    workflow_requirements=$(identify_workflow_requirements "$frontend_tech" "$backend_tech" "$database_tech" "$project_dir")

    # Analyze deployment and infrastructure needs
    local infrastructure_requirements
    infrastructure_requirements=$(analyze_infrastructure_requirements "$frontend_tech" "$backend_tech" "$database_tech" "$project_dir")

    # Generate comprehensive technology analysis
    cat << EOF
{
    "basic_analysis": $basic_analysis,
    "integration_analysis": {
        "frontend_technology": "$frontend_tech",
        "backend_technology": "$backend_tech",
        "database_technology": "$database_tech",
        "additional_technologies": $additional_tech,
        "integration_complexity": $integration_complexity,
        "workflow_requirements": $workflow_requirements,
        "infrastructure_requirements": $infrastructure_requirements
    },
    "stack_patterns": $(identify_stack_patterns "$frontend_tech" "$backend_tech" "$database_tech"),
    "adaptation_requirements": $(analyze_adaptation_requirements "$frontend_tech" "$backend_tech" "$database_tech" "$project_dir")
}
EOF
}

# Assess integration complexity between technologies
assess_integration_complexity() {
    local frontend="$1"
    local backend="$2"
    local database="$3"
    local additional="$4"

    local complexity_score=0
    local complexity_factors=()

    # Analyze frontend-backend integration complexity
    case "$frontend-$backend" in
        "react-node"|"vue-node"|"angular-node")
            complexity_score=$((complexity_score + 1))
            complexity_factors+=("Standard JavaScript full-stack integration")
            ;;
        "react-python"|"vue-python"|"angular-python")
            complexity_score=$((complexity_score + 2))
            complexity_factors+=("Cross-language frontend-backend integration")
            ;;
        "react-java"|"vue-java"|"angular-java")
            complexity_score=$((complexity_score + 3))
            complexity_factors+=("Enterprise-level cross-language integration")
            ;;
        "react-csharp"|"vue-csharp"|"angular-csharp")
            complexity_score=$((complexity_score + 2))
            complexity_factors+=("Microsoft stack cross-technology integration")
            ;;
        *)
            complexity_score=$((complexity_score + 2))
            complexity_factors+=("Custom technology stack integration")
            ;;
    esac

    # Analyze database integration complexity
    case "$database" in
        "sqlite"|"mysql"|"postgresql")
            complexity_score=$((complexity_score + 1))
            complexity_factors+=("Standard relational database integration")
            ;;
        "mongodb"|"redis")
            complexity_score=$((complexity_score + 2))
            complexity_factors+=("NoSQL database integration patterns")
            ;;
        "multiple")
            complexity_score=$((complexity_score + 3))
            complexity_factors+=("Multi-database architecture complexity")
            ;;
        *)
            complexity_score=$((complexity_score + 1))
            ;;
    esac

    # Analyze additional technology complexity
    local additional_count
    additional_count=$(echo "$additional" | jq 'length')
    if [[ $additional_count -gt 3 ]]; then
        complexity_score=$((complexity_score + 2))
        complexity_factors+=("High number of additional technologies")
    elif [[ $additional_count -gt 1 ]]; then
        complexity_score=$((complexity_score + 1))
        complexity_factors+=("Multiple supporting technologies")
    fi

    # Determine complexity level
    local complexity_level
    if [[ $complexity_score -le 2 ]]; then
        complexity_level="low"
    elif [[ $complexity_score -le 4 ]]; then
        complexity_level="medium"
    elif [[ $complexity_score -le 6 ]]; then
        complexity_level="high"
    else
        complexity_level="very_high"
    fi

    cat << EOF
{
    "level": "$complexity_level",
    "score": $complexity_score,
    "factors": $(printf '%s\n' "${complexity_factors[@]}" | jq -R . | jq -s .)
}
EOF
}

# Identify technology-specific workflow requirements
identify_workflow_requirements() {
    local frontend="$1"
    local backend="$2"
    local database="$3"
    local project_dir="$4"

    local requirements=()

    # Frontend-specific workflow requirements
    case "$frontend" in
        "react")
            requirements+=("React component testing with Jest and React Testing Library")
            requirements+=("Component story development for Storybook")
            requirements+=("React hooks and state management validation")
            requirements+=("Accessibility testing for React components")
            ;;
        "angular")
            requirements+=("Angular unit testing with Jasmine and Karma")
            requirements+=("Angular end-to-end testing with Protractor or Cypress")
            requirements+=("Angular CLI build optimization and bundling")
            requirements+=("TypeScript compilation and type checking")
            ;;
        "vue")
            requirements+=("Vue component testing with Vue Test Utils")
            requirements+=("Vue.js Single File Component validation")
            requirements+=("Vuex state management testing")
            requirements+=("Vue CLI build and deployment optimization")
            ;;
        *)
            requirements+=("Frontend framework-specific testing and validation")
            ;;
    esac

    # Backend-specific workflow requirements
    case "$backend" in
        "node")
            requirements+=("Node.js API testing with Jest or Mocha")
            requirements+=("Express.js middleware testing and validation")
            requirements+=("NPM dependency security scanning")
            requirements+=("Node.js performance profiling and optimization")
            ;;
        "python")
            requirements+=("Python unit testing with pytest or unittest")
            requirements+=("Python API testing with FastAPI or Django test framework")
            requirements+=("Python dependency management with pip or Poetry")
            requirements+=("Python code quality checking with Black and flake8")
            ;;
        "java")
            requirements+=("Java unit testing with JUnit and Mockito")
            requirements+=("Spring Boot integration testing")
            requirements+=("Maven or Gradle build and dependency management")
            requirements+=("Java code quality analysis with SonarQube")
            ;;
        "csharp")
            requirements+=(".NET unit testing with xUnit or NUnit")
            requirements+=("ASP.NET Core integration testing")
            requirements+=("NuGet package management and security scanning")
            requirements+=(".NET code analysis and quality gates")
            ;;
        *)
            requirements+=("Backend framework-specific testing and validation")
            ;;
    esac

    # Database-specific workflow requirements
    case "$database" in
        "postgresql"|"mysql")
            requirements+=("Database migration testing and rollback procedures")
            requirements+=("SQL query performance testing and optimization")
            requirements+=("Database backup and recovery validation")
            requirements+=("Relational database integrity and constraint testing")
            ;;
        "mongodb")
            requirements+=("MongoDB document validation and schema testing")
            requirements+=("NoSQL query optimization and indexing validation")
            requirements+=("MongoDB replica set and sharding testing")
            requirements+=("Document database backup and recovery procedures")
            ;;
        "sqlite")
            requirements+=("SQLite database file integrity and performance testing")
            requirements+=("Local database migration and seeding procedures")
            ;;
        *)
            requirements+=("Database-specific testing and validation procedures")
            ;;
    esac

    # Add integration-specific requirements
    requirements+=("End-to-end integration testing across full technology stack")
    requirements+=("API contract testing between frontend and backend")
    requirements+=("Database connection and transaction testing")
    requirements+=("Cross-browser and cross-platform compatibility testing")

    # Convert to JSON array
    printf '%s\n' "${requirements[@]}" | jq -R . | jq -s .
}

# Analyze infrastructure and deployment requirements
analyze_infrastructure_requirements() {
    local frontend="$1"
    local backend="$2"
    local database="$3"
    local project_dir="$4"

    local infrastructure=()
    local deployment_strategies=()
    local monitoring_requirements=()

    # Frontend deployment requirements
    case "$frontend" in
        "react"|"vue"|"angular")
            infrastructure+=("Static file hosting (CDN, S3, or similar)")
            infrastructure+=("Build process automation (webpack, Vite, or CLI tools)")
            deployment_strategies+=("Single Page Application deployment with routing support")
            monitoring_requirements+=("Frontend error tracking and performance monitoring")
            ;;
        *)
            infrastructure+=("Frontend-specific hosting and build requirements")
            ;;
    esac

    # Backend deployment requirements
    case "$backend" in
        "node")
            infrastructure+=("Node.js runtime environment (Docker, PM2, or cloud platforms)")
            infrastructure+=("NPM package management and security scanning")
            deployment_strategies+=("API server deployment with load balancing and scaling")
            monitoring_requirements+=("Node.js application performance monitoring and logging")
            ;;
        "python")
            infrastructure+=("Python runtime with WSGI/ASGI server (Gunicorn, Uvicorn)")
            infrastructure+=("Python package management and virtual environments")
            deployment_strategies+=("Python web application deployment with container orchestration")
            monitoring_requirements+=("Python application monitoring with APM tools")
            ;;
        "java")
            infrastructure+=("Java Runtime Environment and application server")
            infrastructure+=("Maven/Gradle build automation and artifact management")
            deployment_strategies+=("Enterprise Java deployment with clustering and failover")
            monitoring_requirements+=("JVM monitoring and application performance management")
            ;;
        "csharp")
            infrastructure+=(".NET runtime and hosting environment")
            infrastructure+=("NuGet package management and deployment automation")
            deployment_strategies+=(".NET application deployment with IIS or container platforms")
            monitoring_requirements+=(".NET application monitoring and health checks")
            ;;
        *)
            infrastructure+=("Backend-specific runtime and deployment requirements")
            ;;
    esac

    # Database deployment requirements
    case "$database" in
        "postgresql"|"mysql")
            infrastructure+=("Relational database server with backup and replication")
            infrastructure+=("Database migration and schema management tools")
            deployment_strategies+=("Database deployment with high availability and disaster recovery")
            monitoring_requirements+=("Database performance monitoring and query optimization")
            ;;
        "mongodb")
            infrastructure+=("MongoDB server with replica sets and sharding")
            infrastructure+=("NoSQL database backup and recovery procedures")
            deployment_strategies+=("MongoDB cluster deployment with automatic failover")
            monitoring_requirements+=("MongoDB performance and replica set monitoring")
            ;;
        "sqlite")
            infrastructure+=("Local database file management and backup procedures")
            deployment_strategies+=("Embedded database deployment with application bundling")
            ;;
        *)
            infrastructure+=("Database-specific deployment and management requirements")
            ;;
    esac

    cat << EOF
{
    "infrastructure_components": $(printf '%s\n' "${infrastructure[@]}" | jq -R . | jq -s .),
    "deployment_strategies": $(printf '%s\n' "${deployment_strategies[@]}" | jq -R . | jq -s .),
    "monitoring_requirements": $(printf '%s\n' "${monitoring_requirements[@]}" | jq -R . | jq -s .)
}
EOF
}

# Identify common technology stack patterns
identify_stack_patterns() {
    local frontend="$1"
    local backend="$2"
    local database="$3"

    local pattern_name="custom"
    local pattern_category="custom"
    local pattern_description="Custom technology stack"
    local common_practices=()

    # Identify well-known stack patterns
    case "$frontend-$backend-$database" in
        "react-node-mongodb")
            pattern_name="MERN"
            pattern_category="javascript_fullstack"
            pattern_description="MongoDB, Express.js, React, Node.js full-stack JavaScript"
            common_practices+=("Component-based React development with hooks")
            common_practices+=("RESTful API development with Express.js")
            common_practices+=("MongoDB document modeling and aggregation")
            common_practices+=("Full-stack JavaScript testing with Jest")
            ;;
        "angular-node-mongodb")
            pattern_name="MEAN"
            pattern_category="javascript_fullstack"
            pattern_description="MongoDB, Express.js, Angular, Node.js full-stack JavaScript"
            common_practices+=("Angular component and service architecture")
            common_practices+=("TypeScript development across frontend and backend")
            common_practices+=("Angular CLI build and testing automation")
            common_practices+=("MongoDB integration with Mongoose ODM")
            ;;
        "react-node-postgresql"|"react-node-mysql")
            pattern_name="React-Node-SQL"
            pattern_category="javascript_fullstack"
            pattern_description="React frontend with Node.js backend and SQL database"
            common_practices+=("React component development with modern hooks")
            common_practices+=("Node.js API development with SQL query optimization")
            common_practices+=("Database migration and seeding automation")
            common_practices+=("Full-stack integration testing")
            ;;
        "react-python-postgresql"|"react-python-mysql")
            pattern_name="React-Python-SQL"
            pattern_category="python_web"
            pattern_description="React frontend with Python backend and SQL database"
            common_practices+=("React SPA development with API integration")
            common_practices+=("Python web framework development (Django/FastAPI)")
            common_practices+=("Database ORM usage and migration management")
            common_practices+=("Cross-language API contract testing")
            ;;
        "angular-java-postgresql"|"angular-java-mysql")
            pattern_name="Angular-Spring-SQL"
            pattern_category="enterprise_java"
            pattern_description="Angular frontend with Spring Boot backend and SQL database"
            common_practices+=("Angular enterprise application development")
            common_practices+=("Spring Boot microservices architecture")
            common_practices+=("Enterprise database design and optimization")
            common_practices+=("Enterprise-grade testing and quality assurance")
            ;;
        *)
            # Identify partial patterns
            if [[ "$frontend" == "react" || "$frontend" == "vue" || "$frontend" == "angular" ]] && [[ "$backend" == "node" ]]; then
                pattern_name="JavaScript-SPA"
                pattern_category="javascript_spa"
                pattern_description="Modern JavaScript Single Page Application with Node.js"
                common_practices+=("Modern JavaScript frontend development")
                common_practices+=("Node.js API server development")
                common_practices+=("JavaScript build tooling and optimization")
            elif [[ "$backend" == "python" ]]; then
                pattern_name="Python-Web"
                pattern_category="python_web"
                pattern_description="Python web application with modern frontend"
                common_practices+=("Python web framework development")
                common_practices+=("Python package management and virtual environments")
                common_practices+=("Python testing and code quality automation")
            elif [[ "$backend" == "java" ]]; then
                pattern_name="Java-Enterprise"
                pattern_category="enterprise_java"
                pattern_description="Enterprise Java application with modern frontend"
                common_practices+=("Enterprise Java development patterns")
                common_practices+=("Maven/Gradle build automation")
                common_practices+=("Enterprise-grade testing and deployment")
            fi
            ;;
    esac

    # Add universal practices based on pattern category
    case "$pattern_category" in
        "javascript_fullstack")
            common_practices+=("NPM/Yarn package management across stack")
            common_practices+=("ESLint and Prettier code formatting")
            common_practices+=("Docker containerization for development and deployment")
            ;;
        "python_web")
            common_practices+=("Python virtual environments and dependency management")
            common_practices+=("Python code formatting with Black and linting with flake8")
            common_practices+=("Python application containerization and deployment")
            ;;
        "enterprise_java")
            common_practices+=("Maven/Gradle enterprise build management")
            common_practices+=("SonarQube code quality analysis")
            common_practices+=("Enterprise application server deployment")
            ;;
        *)
            common_practices+=("Cross-technology build and deployment automation")
            common_practices+=("Technology-specific testing and quality assurance")
            ;;
    esac

    cat << EOF
{
    "pattern_name": "$pattern_name",
    "pattern_category": "$pattern_category",
    "pattern_description": "$pattern_description",
    "common_practices": $(printf '%s\n' "${common_practices[@]}" | jq -R . | jq -s .),
    "stack_characteristics": {
        "frontend_framework": "$frontend",
        "backend_framework": "$backend",
        "database_technology": "$database",
        "integration_type": "${pattern_category}"
    }
}
EOF
}

# Analyze adaptation requirements for technology stack
analyze_adaptation_requirements() {
    local frontend="$1"
    local backend="$2"
    local database="$3"
    local project_dir="$4"

    local build_requirements=()
    local testing_adaptations=()
    local deployment_adaptations=()
    local quality_gates=()

    # Frontend-specific adaptations
    case "$frontend" in
        "react")
            build_requirements+=("Webpack or Vite build configuration for React")
            build_requirements+=("Babel transformation for modern JavaScript features")
            testing_adaptations+=("Jest configuration for React component testing")
            testing_adaptations+=("React Testing Library for component behavior testing")
            quality_gates+=("React component accessibility testing")
            quality_gates+=("React performance optimization validation")
            ;;
        "angular")
            build_requirements+=("Angular CLI build configuration and optimization")
            build_requirements+=("TypeScript compilation and type checking")
            testing_adaptations+=("Angular testing setup with Jasmine and Karma")
            testing_adaptations+=("Angular end-to-end testing framework configuration")
            quality_gates+=("Angular application performance budgets")
            quality_gates+=("TypeScript strict mode compliance")
            ;;
        "vue")
            build_requirements+=("Vue CLI build configuration for Single File Components")
            build_requirements+=("Vue.js template compilation and optimization")
            testing_adaptations+=("Vue Test Utils configuration for component testing")
            testing_adaptations+=("Vue.js application testing with Cypress or similar")
            quality_gates+=("Vue.js component performance optimization")
            quality_gates+=("Vue.js accessibility and usability validation")
            ;;
        *)
            build_requirements+=("Frontend framework-specific build configuration")
            testing_adaptations+=("Frontend testing framework setup and configuration")
            ;;
    esac

    # Backend-specific adaptations
    case "$backend" in
        "node")
            build_requirements+=("Node.js application bundling and optimization")
            build_requirements+=("NPM dependency management and security scanning")
            testing_adaptations+=("Node.js API testing with Jest or Mocha framework")
            testing_adaptations+=("Express.js middleware and route testing")
            quality_gates+=("Node.js security vulnerability scanning")
            quality_gates+=("Node.js performance profiling and optimization")
            deployment_adaptations+=("Node.js application containerization with Docker")
            deployment_adaptations+=("PM2 or similar process management for Node.js")
            ;;
        "python")
            build_requirements+=("Python package building with setuptools or Poetry")
            build_requirements+=("Python dependency management and virtual environments")
            testing_adaptations+=("Python testing with pytest or unittest framework")
            testing_adaptations+=("Python API testing with FastAPI or Django test client")
            quality_gates+=("Python code quality checking with Black, flake8, mypy")
            quality_gates+=("Python security scanning with bandit or similar")
            deployment_adaptations+=("Python application containerization")
            deployment_adaptations+=("WSGI/ASGI server configuration for Python applications")
            ;;
        "java")
            build_requirements+=("Maven or Gradle build automation for Java")
            build_requirements+=("Java compilation and JAR/WAR packaging")
            testing_adaptations+=("JUnit and Mockito testing framework setup")
            testing_adaptations+=("Spring Boot integration testing configuration")
            quality_gates+=("SonarQube code quality analysis for Java")
            quality_gates+=("Java security scanning and dependency checking")
            deployment_adaptations+=("Java application server deployment (Tomcat, WildFly)")
            deployment_adaptations+=("Java application containerization and orchestration")
            ;;
        *)
            build_requirements+=("Backend framework-specific build and compilation")
            testing_adaptations+=("Backend testing framework configuration")
            ;;
    esac

    # Database-specific adaptations
    case "$database" in
        "postgresql"|"mysql")
            build_requirements+=("Database migration scripts and schema management")
            testing_adaptations+=("Database testing with test database setup and cleanup")
            quality_gates+=("Database query performance testing and optimization")
            quality_gates+=("Database integrity and constraint validation")
            deployment_adaptations+=("Database backup and recovery automation")
            deployment_adaptations+=("Database high availability and replication setup")
            ;;
        "mongodb")
            build_requirements+=("MongoDB document validation and indexing setup")
            testing_adaptations+=("MongoDB testing with test database and collection setup")
            quality_gates+=("MongoDB query optimization and index analysis")
            quality_gates+=("MongoDB document schema validation")
            deployment_adaptations+=("MongoDB replica set and sharding configuration")
            deployment_adaptations+=("MongoDB backup and disaster recovery procedures")
            ;;
        "sqlite")
            build_requirements+=("SQLite database initialization and seeding scripts")
            testing_adaptations+=("SQLite testing with temporary database files")
            quality_gates+=("SQLite database file integrity and performance testing")
            deployment_adaptations+=("SQLite database bundling and deployment automation")
            ;;
        *)
            build_requirements+=("Database-specific setup and configuration requirements")
            ;;
    esac

    cat << EOF
{
    "build_requirements": $(printf '%s\n' "${build_requirements[@]}" | jq -R . | jq -s .),
    "testing_adaptations": $(printf '%s\n' "${testing_adaptations[@]}" | jq -R . | jq -s .),
    "deployment_adaptations": $(printf '%s\n' "${deployment_adaptations[@]}" | jq -R . | jq -s .),
    "quality_gates": $(printf '%s\n' "${quality_gates[@]}" | jq -R . | jq -s .)
}
EOF
}

# Adapt workflow phases to technology stack
adapt_workflow_phases() {
    local technology_analysis="$1"
    local base_phases="$2"

    log_info "Adapting workflow phases to technology stack requirements"

    # Extract technology characteristics
    local frontend_tech
    local backend_tech
    local database_tech
    local stack_pattern
    local integration_complexity

    frontend_tech=$(echo "$technology_analysis" | jq -r '.integration_analysis.frontend_technology // "none"')
    backend_tech=$(echo "$technology_analysis" | jq -r '.integration_analysis.backend_technology // "none"')
    database_tech=$(echo "$technology_analysis" | jq -r '.integration_analysis.database_technology // "none"')
    stack_pattern=$(echo "$technology_analysis" | jq -r '.stack_patterns.pattern_name // "custom"')
    integration_complexity=$(echo "$technology_analysis" | jq -r '.integration_analysis.integration_complexity.level // "medium"')

    # Load workflow requirements and adaptation requirements
    local workflow_requirements
    local adaptation_requirements

    workflow_requirements=$(echo "$technology_analysis" | jq '.integration_analysis.workflow_requirements')
    adaptation_requirements=$(echo "$technology_analysis" | jq '.adaptation_requirements')

    log_info "Adapting for $stack_pattern stack ($integration_complexity complexity)"

    # Adapt each phase based on technology requirements
    local adapted_phases
    adapted_phases=$(echo "$base_phases" | jq --argjson tech_analysis "$technology_analysis" '
        map(. + {
            technology_adaptations: {
                stack_pattern: ($tech_analysis.stack_patterns.pattern_name // "custom"),
                build_requirements: ($tech_analysis.adaptation_requirements.build_requirements // []),
                testing_adaptations: ($tech_analysis.adaptation_requirements.testing_adaptations // []),
                deployment_adaptations: ($tech_analysis.adaptation_requirements.deployment_adaptations // [])
            },
            enhanced_activities: (
                .key_activities +
                if (.name | contains("Foundation") or .name | contains("Setup")) then
                    ($tech_analysis.adaptation_requirements.build_requirements // [])
                elif (.name | contains("Development") or .name | contains("Feature")) then
                    ($tech_analysis.integration_analysis.workflow_requirements // [])
                elif (.name | contains("Testing") or .name | contains("Quality")) then
                    ($tech_analysis.adaptation_requirements.testing_adaptations // [])
                elif (.name | contains("Deploy") or .name | contains("Launch")) then
                    ($tech_analysis.adaptation_requirements.deployment_adaptations // [])
                else
                    []
                end
            ),
            enhanced_quality_gates: (
                .quality_gates +
                ($tech_analysis.adaptation_requirements.quality_gates // [])
            )
        })
    ')

    echo "$adapted_phases"
}

# Generate technology-specific agent recommendations
generate_agent_recommendations() {
    local technology_analysis="$1"

    log_info "Generating technology-specific agent recommendations"

    # Extract technology characteristics
    local frontend_tech
    local backend_tech
    local database_tech
    local stack_pattern

    frontend_tech=$(echo "$technology_analysis" | jq -r '.integration_analysis.frontend_technology // "none"')
    backend_tech=$(echo "$technology_analysis" | jq -r '.integration_analysis.backend_technology // "none"')
    database_tech=$(echo "$technology_analysis" | jq -r '.integration_analysis.database_technology // "none"')
    stack_pattern=$(echo "$technology_analysis" | jq -r '.stack_patterns.pattern_name // "custom"')

    local primary_agents=()
    local supporting_agents=()
    local specialized_agents=()

    # Core agents for any stack
    primary_agents+=("frontend-engineer")
    primary_agents+=("backend-engineer")
    primary_agents+=("qa-engineer")

    # Frontend-specific agents
    case "$frontend_tech" in
        "react"|"vue"|"angular")
            supporting_agents+=("ux-designer")
            specialized_agents+=("performance-engineer")
            ;;
    esac

    # Backend-specific agents
    case "$backend_tech" in
        "node"|"python"|"java"|"csharp")
            supporting_agents+=("api-engineer")
            ;;
    esac

    # Database-specific agents
    case "$database_tech" in
        "postgresql"|"mysql"|"mongodb")
            supporting_agents+=("data-engineer")
            supporting_agents+=("database-administrator")
            ;;
    esac

    # Stack pattern-specific agents
    case "$stack_pattern" in
        "MERN"|"MEAN"|"React-Node-SQL")
            specialized_agents+=("devops-architect")
            specialized_agents+=("monitoring-engineer")
            ;;
        "React-Python-SQL"|"Python-Web")
            specialized_agents+=("automation-engineer")
            specialized_agents+=("deployment-engineer")
            ;;
        "Angular-Spring-SQL"|"Java-Enterprise")
            specialized_agents+=("enterprise-architect")
            specialized_agents+=("security-engineer")
            specialized_agents+=("compliance-auditor")
            ;;
    esac

    # Always include essential support agents
    supporting_agents+=("software-architect")
    supporting_agents+=("deployment-engineer")

    cat << EOF
{
    "stack_pattern": "$stack_pattern",
    "technology_stack": {
        "frontend": "$frontend_tech",
        "backend": "$backend_tech",
        "database": "$database_tech"
    },
    "agent_recommendations": {
        "primary_agents": $(printf '%s\n' "${primary_agents[@]}" | jq -R . | jq -s .),
        "supporting_agents": $(printf '%s\n' "${supporting_agents[@]}" | jq -R . | jq -s .),
        "specialized_agents": $(printf '%s\n' "${specialized_agents[@]}" | jq -R . | jq -s .)
    },
    "agent_coordination_pattern": $(generate_coordination_pattern "$stack_pattern" "$primary_agents" "$supporting_agents" "$specialized_agents")
}
EOF
}

# Generate agent coordination pattern for technology stack
generate_coordination_pattern() {
    local stack_pattern="$1"
    local primary_agents="$2"
    local supporting_agents="$3"
    local specialized_agents="$4"

    local coordination_phases=()

    case "$stack_pattern" in
        "MERN"|"MEAN"|"React-Node-SQL")
            coordination_phases+=("Phase 1: software-architect + frontend-engineer + backend-engineer (parallel architecture and foundation)")
            coordination_phases+=("Phase 2: frontend-engineer + api-engineer (parallel UI and API development)")
            coordination_phases+=("Phase 3: data-engineer + qa-engineer (parallel data layer and testing)")
            coordination_phases+=("Phase 4: devops-architect + deployment-engineer (deployment preparation)")
            coordination_phases+=("Phase 5: monitoring-engineer + qa-engineer (production monitoring)")
            ;;
        "React-Python-SQL"|"Python-Web")
            coordination_phases+=("Phase 1: software-architect + backend-engineer (backend-first architecture)")
            coordination_phases+=("Phase 2: frontend-engineer + api-engineer (frontend integration)")
            coordination_phases+=("Phase 3: data-engineer + automation-engineer (data and automation)")
            coordination_phases+=("Phase 4: deployment-engineer + qa-engineer (deployment and testing)")
            ;;
        "Angular-Spring-SQL"|"Java-Enterprise")
            coordination_phases+=("Phase 1: enterprise-architect + software-architect (enterprise architecture)")
            coordination_phases+=("Phase 2: backend-engineer + security-engineer (secure backend)")
            coordination_phases+=("Phase 3: frontend-engineer + ux-designer (enterprise UI)")
            coordination_phases+=("Phase 4: qa-engineer + compliance-auditor (quality and compliance)")
            coordination_phases+=("Phase 5: deployment-engineer + monitoring-engineer (enterprise deployment)")
            ;;
        *)
            coordination_phases+=("Phase 1: software-architect + primary development agents (architecture)")
            coordination_phases+=("Phase 2: primary agents parallel development (core features)")
            coordination_phases+=("Phase 3: supporting agents integration (integration and testing)")
            coordination_phases+=("Phase 4: specialized agents deployment (deployment and monitoring)")
            ;;
    esac

    printf '%s\n' "${coordination_phases[@]}" | jq -R . | jq -s .
}

# Generate complete technology stack adaptation
generate_stack_adaptation() {
    local project_dir="${1:-$PWD}"

    log_info "🔧 Generating Technology Stack Workflow Adaptation"
    log_info "Project directory: $project_dir"

    create_output_directory

    # Load technology analysis
    local technology_analysis
    if ! technology_analysis=$(load_technology_analysis "$project_dir"); then
        log_error "Failed to load technology analysis. Please run project detection first."
        return 1
    fi

    # Load base development phases (should exist from phase_generator)
    local base_phases_file="$OUTPUT_DIR/development_guide.json"
    if [[ ! -f "$base_phases_file" ]]; then
        log_error "Base development guide not found. Please run phase generator first."
        return 1
    fi

    local base_phases
    base_phases=$(jq '.phase_structure.phases' "$base_phases_file")

    # Adapt workflow phases to technology stack
    log_info "🔄 Adapting workflow phases to technology stack"
    local adapted_phases
    adapted_phases=$(adapt_workflow_phases "$technology_analysis" "$base_phases")

    # Generate technology-specific agent recommendations
    log_info "🤖 Generating technology-specific agent recommendations"
    local agent_recommendations
    agent_recommendations=$(generate_agent_recommendations "$technology_analysis")

    # Generate comprehensive stack adaptation
    local stack_adaptation
    stack_adaptation=$(cat << EOF
{
    "metadata": {
        "generated_at": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
        "generator": "stack_adapter.sh",
        "version": "1.0.0",
        "project_directory": "$project_dir"
    },
    "technology_analysis": $technology_analysis,
    "adapted_phases": $adapted_phases,
    "agent_recommendations": $agent_recommendations,
    "integration_guide": {
        "workflow_integration": [
            "Technology-specific build requirements integrated into development phases",
            "Testing adaptations included in quality assurance activities",
            "Deployment adaptations incorporated into release phases",
            "Agent recommendations optimized for technology stack patterns"
        ],
        "implementation_strategy": [
            "Use adapted phases for technology-specific development workflows",
            "Follow agent coordination patterns for optimal team collaboration",
            "Apply technology-specific quality gates throughout development",
            "Leverage stack-specific tools and practices for efficiency"
        ]
    }
}
EOF
)

    # Save stack adaptation to output file
    local output_file="$OUTPUT_DIR/stack_adaptation.json"
    echo "$stack_adaptation" | jq '.' > "$output_file"

    log_success "Technology Stack Workflow Adaptation generated successfully"
    log_info "Output file: $output_file"

    # Generate human-readable summary
    generate_adaptation_summary "$stack_adaptation" "$OUTPUT_DIR"

    return 0
}

# Generate human-readable summary of stack adaptation
generate_adaptation_summary() {
    local stack_adaptation="$1"
    local output_dir="$2"
    local summary_file="$output_dir/STACK_ADAPTATION.md"

    # Extract key information
    local stack_pattern
    local frontend_tech
    local backend_tech
    local database_tech
    local complexity_level

    stack_pattern=$(echo "$stack_adaptation" | jq -r '.technology_analysis.stack_patterns.pattern_name')
    frontend_tech=$(echo "$stack_adaptation" | jq -r '.technology_analysis.integration_analysis.frontend_technology')
    backend_tech=$(echo "$stack_adaptation" | jq -r '.technology_analysis.integration_analysis.backend_technology')
    database_tech=$(echo "$stack_adaptation" | jq -r '.technology_analysis.integration_analysis.database_technology')
    complexity_level=$(echo "$stack_adaptation" | jq -r '.technology_analysis.integration_analysis.integration_complexity.level')

    # Generate markdown summary
    cat > "$summary_file" << EOF
# Technology Stack Workflow Adaptation

**Generated:** $(date)
**Stack Pattern:** ${stack_pattern}
**Integration Complexity:** ${complexity_level^}

## Technology Stack Analysis

### Core Technologies
- **Frontend:** ${frontend_tech^}
- **Backend:** ${backend_tech^}
- **Database:** ${database_tech^}

### Stack Pattern Description
$(echo "$stack_adaptation" | jq -r '.technology_analysis.stack_patterns.pattern_description')

## Adapted Development Workflow

$(echo "$stack_adaptation" | jq -r '.adapted_phases[] |
    "### " + .name + " (" + (.duration_weeks // 4 | tostring) + " weeks)\n" +
    .description + "\n\n" +
    "**Technology-Specific Activities:**\n" +
    (.technology_adaptations.build_requirements[]? // empty | "- " + .) +
    (.technology_adaptations.testing_adaptations[]? // empty | "- " + .) +
    (.technology_adaptations.deployment_adaptations[]? // empty | "- " + .) + "\n\n" +
    "**Enhanced Quality Gates:**\n" +
    (.enhanced_quality_gates[]? // empty | "- " + .) + "\n"'
)

## Agent Recommendations

### Primary Development Agents
$(echo "$stack_adaptation" | jq -r '.agent_recommendations.agent_recommendations.primary_agents[]? // empty | "- **" + . + "** - Core development responsibility"')

### Supporting Agents
$(echo "$stack_adaptation" | jq -r '.agent_recommendations.agent_recommendations.supporting_agents[]? // empty | "- **" + . + "** - Specialized support and integration"')

### Specialized Agents
$(echo "$stack_adaptation" | jq -r '.agent_recommendations.agent_recommendations.specialized_agents[]? // empty | "- **" + . + "** - Advanced technology-specific expertise"')

## Agent Coordination Pattern

$(echo "$stack_adaptation" | jq -r '.agent_recommendations.agent_coordination_pattern[]? // empty | "**" + . + "**"')

## Technology-Specific Requirements

### Build Requirements
$(echo "$stack_adaptation" | jq -r '.technology_analysis.adaptation_requirements.build_requirements[]? // empty | "- " + .')

### Testing Adaptations
$(echo "$stack_adaptation" | jq -r '.technology_analysis.adaptation_requirements.testing_adaptations[]? // empty | "- " + .')

### Deployment Adaptations
$(echo "$stack_adaptation" | jq -r '.technology_analysis.adaptation_requirements.deployment_adaptations[]? // empty | "- " + .')

### Quality Gates
$(echo "$stack_adaptation" | jq -r '.technology_analysis.adaptation_requirements.quality_gates[]? // empty | "- " + .')

## Implementation Guidelines

### Workflow Integration
- Technology-specific build requirements are integrated into development phases
- Testing adaptations are included in quality assurance activities
- Deployment adaptations are incorporated into release phases
- Agent recommendations are optimized for technology stack patterns

### Best Practices
- Use adapted phases for technology-specific development workflows
- Follow agent coordination patterns for optimal team collaboration
- Apply technology-specific quality gates throughout development
- Leverage stack-specific tools and practices for maximum efficiency

---

*This technology adaptation was generated automatically based on project analysis. Customize further based on specific project requirements and constraints.*
EOF

    log_success "Human-readable stack adaptation guide created: $summary_file"
}

# Main function
main() {
    local command="${1:-generate}"
    local project_dir="${2:-$PWD}"

    case "$command" in
        "generate")
            generate_stack_adaptation "$project_dir"
            ;;
        "analyze")
            create_output_directory
            load_technology_analysis "$project_dir" | jq '.'
            ;;
        "help"|"--help"|"-h")
            cat << EOF
Technology Stack Workflow Adaptation Engine

USAGE:
    $0 [COMMAND] [PROJECT_DIR]

COMMANDS:
    generate    Generate complete technology stack adaptation (default)
    analyze     Show technology analysis only
    help        Show this help message

ARGUMENTS:
    PROJECT_DIR    Directory to analyze (default: current directory)

EXAMPLES:
    $0                        # Generate adaptation for current directory
    $0 generate /path/to/project    # Generate adaptation for specific project
    $0 analyze                # Show technology analysis only
    $0 help                   # Show help

OUTPUT FILES:
    workflow_output/stack_adaptation.json    # Complete adaptation data
    workflow_output/STACK_ADAPTATION.md     # Human-readable summary

DEPENDENCIES:
    - jq (for JSON processing)
    - project_detector.sh (for technology detection)
    - phase_generator.sh output (for base development phases)
EOF
            ;;
        *)
            log_error "Unknown command: $command"
            log_info "Use '$0 help' for usage information"
            exit 1
            ;;
    esac
}

# Execute main function if script is called directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi