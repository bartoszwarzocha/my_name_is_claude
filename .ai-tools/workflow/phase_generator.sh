#!/bin/bash

# Phase-Based Development Guide Generator
# Part of Intelligent Project Workflow Generation System
# Generates customized development phases with milestones and quality gates

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

# Phase generator configuration
readonly PHASE_TEMPLATES_DIR="$(dirname "$0")/phase_templates"
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

# Load project profile from workflow analyzer
load_project_profile() {
    local project_dir="${1:-$PWD}"
    local profile_file="$OUTPUT_DIR/project_profile.json"

    if [[ -f "$profile_file" ]]; then
        log_info "Loading existing project profile from $profile_file"
        cat "$profile_file"
    else
        log_warning "Project profile not found. Running workflow analysis first..."

        # Check if workflow_analyzer.sh exists and run it
        local analyzer_path="$(dirname "$0")/workflow_analyzer.sh"
        if [[ -x "$analyzer_path" ]]; then
            "$analyzer_path" "$project_dir"
            [[ -f "$profile_file" ]] && cat "$profile_file"
        else
            log_error "Cannot load project profile. Please run workflow analysis first."
            return 1
        fi
    fi
}

# Generate phase structure based on project characteristics
generate_phase_structure() {
    local project_profile="$1"

    # Extract key characteristics from project profile
    local complexity
    local technology_stack
    local business_domain
    local project_scale
    local team_size
    local security_requirements
    local compliance_needs

    complexity=$(echo "$project_profile" | jq -r '.complexity // "medium"')
    technology_stack=$(echo "$project_profile" | jq -r '.technology_stack // []')
    business_domain=$(echo "$project_profile" | jq -r '.business_domain // "general"')
    project_scale=$(echo "$project_profile" | jq -r '.project_scale // "sme"')
    team_size=$(echo "$project_profile" | jq -r '.team_characteristics.size // "medium"')
    security_requirements=$(echo "$project_profile" | jq -r '.security_requirements // "standard"')
    compliance_needs=$(echo "$project_profile" | jq -r '.compliance_requirements // []')

    log_info "Generating phase structure for $complexity complexity, $project_scale scale project"

    # Select appropriate phase template based on characteristics
    local phase_template
    case "$complexity-$project_scale" in
        "low-startup")
            phase_template="agile_mvp"
            ;;
        "medium-startup"|"medium-sme")
            phase_template="iterative_development"
            ;;
        "high-sme"|"high-enterprise")
            phase_template="enterprise_waterfall_hybrid"
            ;;
        "critical-enterprise")
            phase_template="regulated_enterprise"
            ;;
        *)
            phase_template="standard_agile"
            ;;
    esac

    log_info "Selected phase template: $phase_template"

    # Generate phase configuration
    cat << EOF
{
    "phase_template": "$phase_template",
    "project_characteristics": {
        "complexity": "$complexity",
        "technology_stack": $technology_stack,
        "business_domain": "$business_domain",
        "project_scale": "$project_scale",
        "team_size": "$team_size",
        "security_requirements": "$security_requirements",
        "compliance_needs": $compliance_needs
    },
    "phases": $(generate_phases_for_template "$phase_template" "$project_profile")
}
EOF
}

# Generate phases for specific template
generate_phases_for_template() {
    local template="$1"
    local project_profile="$2"

    case "$template" in
        "agile_mvp")
            generate_mvp_phases "$project_profile"
            ;;
        "iterative_development")
            generate_iterative_phases "$project_profile"
            ;;
        "enterprise_waterfall_hybrid")
            generate_enterprise_hybrid_phases "$project_profile"
            ;;
        "regulated_enterprise")
            generate_regulated_phases "$project_profile"
            ;;
        *)
            generate_standard_agile_phases "$project_profile"
            ;;
    esac
}

# Generate MVP-focused phases (startups, prototypes)
generate_mvp_phases() {
    local project_profile="$1"

    cat << 'EOF'
[
    {
        "name": "Discovery & MVP Definition",
        "duration_weeks": 2,
        "description": "Define MVP scope, validate assumptions, and establish technical foundation",
        "key_activities": [
            "User research and problem validation",
            "MVP scope definition and feature prioritization",
            "Technology stack selection and architecture planning",
            "Development environment setup"
        ],
        "deliverables": [
            "MVP Requirements Document",
            "Technical Architecture Plan",
            "Development Environment",
            "Initial User Stories and Acceptance Criteria"
        ],
        "quality_gates": [
            "MVP scope validated with stakeholders",
            "Technical feasibility confirmed",
            "Development environment operational",
            "Team aligned on goals and timeline"
        ],
        "success_criteria": [
            "Clear MVP definition with measurable success metrics",
            "Technical architecture supports scalability requirements",
            "All team members have working development environments",
            "Stakeholder approval on project direction"
        ]
    },
    {
        "name": "MVP Core Development",
        "duration_weeks": 4,
        "description": "Build MVP core features with focus on user validation",
        "key_activities": [
            "Core feature development and integration",
            "Basic user interface implementation",
            "Essential backend services development",
            "Continuous user feedback collection and integration"
        ],
        "deliverables": [
            "Working MVP with core features",
            "Basic user interface",
            "Essential API endpoints",
            "User feedback collection system"
        ],
        "quality_gates": [
            "Core features functional and tested",
            "User interface intuitive and responsive",
            "API endpoints secure and performant",
            "User feedback positive on core value proposition"
        ],
        "success_criteria": [
            "MVP demonstrates core value to target users",
            "Technical foundation supports expected user load",
            "User feedback validates problem-solution fit",
            "Code quality meets maintainability standards"
        ]
    },
    {
        "name": "MVP Launch & Iteration",
        "duration_weeks": 2,
        "description": "Launch MVP, collect user data, and plan next iteration",
        "key_activities": [
            "Production deployment and monitoring setup",
            "User onboarding and feedback collection",
            "Analytics implementation and data analysis",
            "Next iteration planning based on user data"
        ],
        "deliverables": [
            "Production MVP deployment",
            "User analytics and feedback system",
            "Launch performance report",
            "Next iteration roadmap"
        ],
        "quality_gates": [
            "Production deployment stable and monitored",
            "User analytics collecting meaningful data",
            "User feedback indicating product-market fit progress",
            "Next iteration plan based on real user data"
        ],
        "success_criteria": [
            "MVP successfully serving real users in production",
            "User engagement metrics meet initial targets",
            "Technical platform stable under real usage",
            "Clear data-driven direction for next iteration"
        ]
    }
]
EOF
}

# Generate iterative development phases (SME, medium complexity)
generate_iterative_phases() {
    local project_profile="$1"

    cat << 'EOF'
[
    {
        "name": "Requirements & Architecture",
        "duration_weeks": 3,
        "description": "Comprehensive requirements gathering and system architecture design",
        "key_activities": [
            "Stakeholder requirements gathering and documentation",
            "System architecture design and technology selection",
            "Database design and data modeling",
            "Security architecture and compliance planning"
        ],
        "deliverables": [
            "Business Requirements Document",
            "System Architecture Document",
            "Database Design Specification",
            "Security and Compliance Plan"
        ],
        "quality_gates": [
            "Requirements validated with all stakeholders",
            "Architecture reviewed and approved by technical team",
            "Database design supports performance requirements",
            "Security plan meets compliance requirements"
        ],
        "success_criteria": [
            "Complete understanding of business requirements",
            "Scalable architecture supporting growth requirements",
            "Data model optimized for expected usage patterns",
            "Security framework prevents identified threat vectors"
        ]
    },
    {
        "name": "Foundation Development",
        "duration_weeks": 4,
        "description": "Build core system foundation and essential infrastructure",
        "key_activities": [
            "Core backend services development",
            "Database implementation and optimization",
            "Authentication and authorization system",
            "Basic frontend framework and navigation"
        ],
        "deliverables": [
            "Core backend API services",
            "Production database with optimized schema",
            "User authentication and session management",
            "Frontend framework with basic navigation"
        ],
        "quality_gates": [
            "Backend services handle expected load with <2s response time",
            "Database performance meets requirements under load testing",
            "Authentication system secure against common threats",
            "Frontend framework responsive across target devices"
        ],
        "success_criteria": [
            "Solid technical foundation supporting all planned features",
            "System architecture demonstrates scalability",
            "Security measures protect user data and system access",
            "Development team velocity established and sustainable"
        ]
    },
    {
        "name": "Feature Development Sprint 1",
        "duration_weeks": 3,
        "description": "Implement priority features with complete user workflows",
        "key_activities": [
            "High-priority feature development",
            "User interface components and user experience optimization",
            "API integration and data flow implementation",
            "Unit testing and integration testing"
        ],
        "deliverables": [
            "Priority features with complete workflows",
            "Polished user interface components",
            "Tested API integrations",
            "Automated test suite covering core functionality"
        ],
        "quality_gates": [
            "All priority features functional and user-tested",
            "User interface meets accessibility standards",
            "API integrations reliable and error-handling complete",
            "Test coverage >80% for implemented features"
        ],
        "success_criteria": [
            "Users can complete end-to-end workflows successfully",
            "System performance remains stable with added features",
            "Code quality maintained through review processes",
            "Feature implementation matches business requirements"
        ]
    },
    {
        "name": "Feature Development Sprint 2",
        "duration_weeks": 3,
        "description": "Complete remaining features and optimize user experience",
        "key_activities": [
            "Secondary feature implementation",
            "User experience refinement and optimization",
            "Performance optimization and caching",
            "Cross-browser and cross-device testing"
        ],
        "deliverables": [
            "Complete feature set implementation",
            "Optimized user experience across all interfaces",
            "Performance-tuned system with caching strategies",
            "Cross-platform compatibility validation"
        ],
        "quality_gates": [
            "All planned features implemented and tested",
            "User experience optimized based on feedback",
            "System performance meets all specified requirements",
            "Application works consistently across target platforms"
        ],
        "success_criteria": [
            "Application provides complete value to target users",
            "Performance excellent across all user scenarios",
            "User interface intuitive and efficient",
            "Technical debt minimal and manageable"
        ]
    },
    {
        "name": "Testing & Deployment Preparation",
        "duration_weeks": 2,
        "description": "Comprehensive testing, security validation, and production preparation",
        "key_activities": [
            "End-to-end testing and user acceptance testing",
            "Security testing and vulnerability assessment",
            "Performance testing under realistic load conditions",
            "Production deployment planning and documentation"
        ],
        "deliverables": [
            "Complete test results and bug resolution",
            "Security assessment report and fixes",
            "Performance test results and optimization",
            "Production deployment guide and runbooks"
        ],
        "quality_gates": [
            "All tests passing with no critical issues",
            "Security vulnerabilities addressed and verified",
            "Performance requirements met under load testing",
            "Production deployment process tested and documented"
        ],
        "success_criteria": [
            "Application ready for production with confidence",
            "All quality standards met or exceeded",
            "Security posture appropriate for production use",
            "Operations team prepared for production support"
        ]
    },
    {
        "name": "Production Launch & Monitoring",
        "duration_weeks": 1,
        "description": "Deploy to production and establish monitoring and support processes",
        "key_activities": [
            "Production deployment execution",
            "Monitoring and alerting system setup",
            "User training and documentation delivery",
            "Post-launch support and issue resolution"
        ],
        "deliverables": [
            "Live production application",
            "Monitoring dashboard and alert system",
            "User documentation and training materials",
            "Support processes and escalation procedures"
        ],
        "quality_gates": [
            "Production deployment successful with no critical issues",
            "Monitoring system detecting and alerting on issues",
            "Users successfully onboarded and productive",
            "Support team responding to issues within SLA"
        ],
        "success_criteria": [
            "Application serving users successfully in production",
            "System stability and performance meeting expectations",
            "Users adopting application and achieving intended benefits",
            "Support and maintenance processes functioning effectively"
        ]
    }
]
EOF
}

# Generate enterprise hybrid phases (complex, large scale)
generate_enterprise_hybrid_phases() {
    local project_profile="$1"

    cat << 'EOF'
[
    {
        "name": "Enterprise Analysis & Planning",
        "duration_weeks": 4,
        "description": "Comprehensive enterprise analysis, stakeholder alignment, and detailed planning",
        "key_activities": [
            "Enterprise stakeholder analysis and requirements gathering",
            "Current state analysis and gap assessment",
            "Risk assessment and mitigation strategy development",
            "Enterprise architecture design and governance alignment"
        ],
        "deliverables": [
            "Enterprise Requirements Specification",
            "Current State Analysis Report",
            "Risk Assessment and Mitigation Plan",
            "Enterprise Architecture Document"
        ],
        "quality_gates": [
            "All enterprise stakeholders aligned on requirements",
            "Current state analysis validated by subject matter experts",
            "Risk mitigation strategies approved by governance board",
            "Architecture compliant with enterprise standards"
        ],
        "success_criteria": [
            "Clear understanding of enterprise impact and integration points",
            "Risk management strategy addresses all identified threats",
            "Architecture supports enterprise scalability and governance",
            "Project timeline and resources approved by executive stakeholders"
        ]
    },
    {
        "name": "Foundation & Integration Architecture",
        "duration_weeks": 5,
        "description": "Build enterprise-grade foundation with integration architecture",
        "key_activities": [
            "Enterprise integration layer development",
            "Security framework implementation with enterprise SSO",
            "Data governance and compliance framework setup",
            "Enterprise monitoring and logging infrastructure"
        ],
        "deliverables": [
            "Enterprise integration services",
            "Security framework with SSO integration",
            "Data governance and audit framework",
            "Enterprise monitoring and observability platform"
        ],
        "quality_gates": [
            "Integration services connect successfully with enterprise systems",
            "Security framework passes enterprise security review",
            "Data governance meets regulatory compliance requirements",
            "Monitoring platform provides enterprise-level visibility"
        ],
        "success_criteria": [
            "Solid enterprise foundation supporting all planned functionality",
            "Security posture meets enterprise and regulatory standards",
            "Integration architecture enables seamless enterprise workflows",
            "Observability platform supports enterprise operations requirements"
        ]
    },
    {
        "name": "Core Platform Development",
        "duration_weeks": 6,
        "description": "Develop core platform capabilities with enterprise scalability",
        "key_activities": [
            "Core business logic development with enterprise patterns",
            "Scalable data processing and workflow engines",
            "Enterprise user interface with accessibility compliance",
            "API gateway and microservices architecture implementation"
        ],
        "deliverables": [
            "Core platform services with enterprise scalability",
            "High-performance data processing capabilities",
            "Enterprise-grade user interface meeting accessibility standards",
            "API gateway with comprehensive service management"
        ],
        "quality_gates": [
            "Platform handles enterprise-scale load requirements",
            "Data processing meets performance and accuracy requirements",
            "User interface compliant with enterprise accessibility standards",
            "API gateway provides security, throttling, and monitoring"
        ],
        "success_criteria": [
            "Platform demonstrates enterprise-level reliability and performance",
            "Architecture supports horizontal scaling for enterprise growth",
            "User experience meets enterprise usability and accessibility requirements",
            "Service architecture enables independent development and deployment"
        ]
    },
    {
        "name": "Business Function Implementation",
        "duration_weeks": 8,
        "description": "Implement complete business functions with workflow automation",
        "key_activities": [
            "End-to-end business workflow implementation",
            "Enterprise reporting and analytics capabilities",
            "Workflow automation and business rule engines",
            "Integration testing with enterprise systems"
        ],
        "deliverables": [
            "Complete business workflow automation",
            "Enterprise reporting dashboard and analytics",
            "Business rule engine with configurable workflows",
            "Validated integrations with all enterprise systems"
        ],
        "quality_gates": [
            "Business workflows handle all identified use cases correctly",
            "Reporting provides accurate, real-time enterprise insights",
            "Business rules configurable without code changes",
            "Enterprise integrations tested under realistic conditions"
        ],
        "success_criteria": [
            "Business users can complete all required workflows efficiently",
            "Analytics provide actionable insights for business decision-making",
            "System integrates seamlessly with existing enterprise processes",
            "Performance remains optimal under enterprise usage patterns"
        ]
    },
    {
        "name": "Enterprise Testing & Validation",
        "duration_weeks": 4,
        "description": "Comprehensive enterprise testing including security and compliance",
        "key_activities": [
            "Enterprise-scale load testing and performance validation",
            "Comprehensive security testing and penetration testing",
            "Compliance validation and audit preparation",
            "Enterprise user acceptance testing across all business units"
        ],
        "deliverables": [
            "Load testing results and performance optimization",
            "Security assessment report with remediation verification",
            "Compliance audit report and certification preparation",
            "User acceptance testing results and issue resolution"
        ],
        "quality_gates": [
            "System meets all enterprise performance requirements under load",
            "Security assessment shows no critical or high-risk vulnerabilities",
            "Compliance validation confirms regulatory requirements met",
            "User acceptance testing shows high satisfaction across business units"
        ],
        "success_criteria": [
            "System ready for enterprise production with confidence",
            "Security posture appropriate for enterprise risk profile",
            "Compliance framework supports regulatory audit requirements",
            "Business users validated system meets operational needs"
        ]
    },
    {
        "name": "Enterprise Deployment & Transition",
        "duration_weeks": 3,
        "description": "Phased enterprise deployment with change management",
        "key_activities": [
            "Phased production deployment with rollback capability",
            "Enterprise change management and user training",
            "Operations runbook development and team training",
            "Business continuity planning and disaster recovery setup"
        ],
        "deliverables": [
            "Production system deployed across enterprise",
            "Comprehensive user training and change management program",
            "Operations runbooks and support team training",
            "Business continuity and disaster recovery procedures"
        ],
        "quality_gates": [
            "Production deployment successful with minimal business disruption",
            "User adoption proceeding according to change management plan",
            "Operations team fully trained and supporting system effectively",
            "Business continuity procedures tested and verified"
        ],
        "success_criteria": [
            "Enterprise users successfully utilizing system for business value",
            "System operating reliably at enterprise scale",
            "Operations and support processes functioning effectively",
            "Business continuity and risk management requirements satisfied"
        ]
    }
]
EOF
}

# Generate regulated enterprise phases (financial, healthcare, etc.)
generate_regulated_phases() {
    local project_profile="$1"

    cat << 'EOF'
[
    {
        "name": "Regulatory Analysis & Compliance Planning",
        "duration_weeks": 6,
        "description": "Comprehensive regulatory analysis and compliance framework design",
        "key_activities": [
            "Regulatory requirements analysis and interpretation",
            "Compliance framework design and governance structure",
            "Risk assessment with regulatory impact analysis",
            "Audit trail and documentation standards establishment"
        ],
        "deliverables": [
            "Regulatory Compliance Requirements Document",
            "Compliance Framework and Governance Plan",
            "Regulatory Risk Assessment with Mitigation Strategies",
            "Audit Trail and Documentation Standards"
        ],
        "quality_gates": [
            "Regulatory requirements validated with compliance experts",
            "Compliance framework approved by legal and regulatory teams",
            "Risk mitigation strategies address all regulatory concerns",
            "Documentation standards meet audit requirements"
        ],
        "success_criteria": [
            "Complete understanding of regulatory landscape and requirements",
            "Compliance framework supports ongoing regulatory obligations",
            "Risk management approach satisfies regulatory risk appetite",
            "Documentation strategy supports regulatory audits and examinations"
        ]
    },
    {
        "name": "Secure Foundation & Compliance Infrastructure",
        "duration_weeks": 7,
        "description": "Build highly secure foundation with comprehensive compliance controls",
        "key_activities": [
            "Security-first architecture with defense-in-depth implementation",
            "Comprehensive audit logging and monitoring system",
            "Data governance framework with privacy and protection controls",
            "Regulatory reporting and compliance monitoring infrastructure"
        ],
        "deliverables": [
            "Hardened security architecture with multiple protection layers",
            "Comprehensive audit and monitoring system",
            "Data governance framework with privacy protection",
            "Regulatory reporting automation and compliance dashboards"
        ],
        "quality_gates": [
            "Security architecture passes regulatory security review",
            "Audit system captures all required regulatory events",
            "Data governance meets privacy and protection regulatory requirements",
            "Compliance monitoring provides real-time regulatory status"
        ],
        "success_criteria": [
            "Security foundation exceeds regulatory security requirements",
            "Audit capabilities support all regulatory reporting obligations",
            "Data governance framework protects sensitive information appropriately",
            "Compliance monitoring enables proactive regulatory management"
        ]
    },
    {
        "name": "Regulated Core Development",
        "duration_weeks": 10,
        "description": "Develop core functionality with embedded compliance controls",
        "key_activities": [
            "Core business logic with embedded compliance controls",
            "Regulated data processing with validation and controls",
            "User interface with compliance workflow integration",
            "Regulatory reporting automation and validation"
        ],
        "deliverables": [
            "Core platform with integrated compliance controls",
            "Regulated data processing engine with validation",
            "Compliance-aware user interface and workflows",
            "Automated regulatory reporting with validation controls"
        ],
        "quality_gates": [
            "All business logic incorporates required compliance controls",
            "Data processing meets regulatory accuracy and validation requirements",
            "User workflows enforce compliance procedures correctly",
            "Regulatory reporting generates accurate, auditable reports"
        ],
        "success_criteria": [
            "Core functionality operates within regulatory constraints",
            "System enforces compliance automatically without user burden",
            "Data processing maintains regulatory accuracy and integrity",
            "Regulatory reporting supports compliance obligations efficiently"
        ]
    },
    {
        "name": "Comprehensive Compliance Testing",
        "duration_weeks": 6,
        "description": "Exhaustive testing including regulatory compliance validation",
        "key_activities": [
            "Regulatory compliance testing and validation",
            "Security testing with regulatory security standards",
            "Data integrity and privacy protection testing",
            "Regulatory scenario testing and edge case validation"
        ],
        "deliverables": [
            "Comprehensive compliance test results and validation",
            "Security testing report meeting regulatory standards",
            "Data integrity and privacy protection test verification",
            "Regulatory scenario test results with edge case handling"
        ],
        "quality_gates": [
            "All regulatory compliance tests pass without exceptions",
            "Security testing meets or exceeds regulatory security standards",
            "Data integrity and privacy protection verified under all conditions",
            "Edge case scenarios handled according to regulatory requirements"
        ],
        "success_criteria": [
            "System demonstrates full regulatory compliance under testing",
            "Security posture exceeds regulatory minimum requirements",
            "Data protection mechanisms function correctly under all scenarios",
            "Regulatory edge cases handled appropriately with proper controls"
        ]
    },
    {
        "name": "Regulatory Review & Certification Preparation",
        "duration_weeks": 4,
        "description": "Prepare for regulatory review and obtain necessary certifications",
        "key_activities": [
            "Regulatory review preparation and documentation compilation",
            "Third-party security and compliance assessment coordination",
            "Certification application and evidence preparation",
            "Regulatory communication and stakeholder alignment"
        ],
        "deliverables": [
            "Complete regulatory review package",
            "Third-party assessment reports and remediation verification",
            "Certification applications with supporting evidence",
            "Regulatory stakeholder communication and approval documentation"
        ],
        "quality_gates": [
            "Regulatory review package complete and submitted",
            "Third-party assessments show full compliance",
            "Certification applications approved or in final review",
            "Regulatory stakeholders approve system for production use"
        ],
        "success_criteria": [
            "System approved for production use by regulatory authorities",
            "All required certifications obtained or pending final approval",
            "Third-party validation confirms regulatory compliance",
            "Regulatory risk appropriately managed and documented"
        ]
    },
    {
        "name": "Controlled Production Deployment",
        "duration_weeks": 4,
        "description": "Carefully managed production deployment with regulatory oversight",
        "key_activities": [
            "Phased production deployment with regulatory notification",
            "Continuous compliance monitoring and regulatory reporting",
            "Regulated change management and approval processes",
            "Ongoing regulatory relationship and compliance management"
        ],
        "deliverables": [
            "Production system operating under regulatory oversight",
            "Continuous compliance monitoring and reporting system",
            "Regulatory change management processes and procedures",
            "Ongoing regulatory compliance management framework"
        ],
        "quality_gates": [
            "Production deployment completed with regulatory approval",
            "Compliance monitoring functioning and reporting correctly",
            "Change management processes meet ongoing regulatory requirements",
            "Regulatory relationship established for ongoing oversight"
        ],
        "success_criteria": [
            "System operating successfully in regulated production environment",
            "Ongoing regulatory compliance maintained automatically",
            "Regulatory authorities satisfied with system operation and oversight",
            "Business achieving value while maintaining full regulatory compliance"
        ]
    }
]
EOF
}

# Generate standard agile phases (default)
generate_standard_agile_phases() {
    local project_profile="$1"

    cat << 'EOF'
[
    {
        "name": "Sprint 0: Project Setup & Planning",
        "duration_weeks": 2,
        "description": "Establish project foundation, team structure, and initial backlog",
        "key_activities": [
            "Team formation and role definition",
            "Initial backlog creation and story estimation",
            "Development environment setup and CI/CD pipeline",
            "Architecture planning and technology decisions"
        ],
        "deliverables": [
            "Project charter and team structure",
            "Initial product backlog with estimated stories",
            "Development environment and CI/CD pipeline",
            "High-level architecture and technology stack documentation"
        ],
        "quality_gates": [
            "Team roles defined and responsibilities clear",
            "Product backlog prioritized and ready for development",
            "Development environment functional for all team members",
            "Architecture decisions documented and approved"
        ],
        "success_criteria": [
            "Team ready to begin productive development sprints",
            "Clear project vision and success metrics established",
            "Technical foundation supports iterative development",
            "Stakeholder expectations aligned with delivery approach"
        ]
    },
    {
        "name": "Development Sprint 1-2: Core Foundation",
        "duration_weeks": 4,
        "description": "Build core application foundation and essential features",
        "key_activities": [
            "Core backend services and database implementation",
            "Basic user authentication and authorization",
            "Frontend framework and essential user interface components",
            "API design and initial endpoint implementation"
        ],
        "deliverables": [
            "Working core application with basic functionality",
            "User authentication and session management",
            "Frontend framework with navigation and basic components",
            "RESTful API with core endpoints and documentation"
        ],
        "quality_gates": [
            "Core functionality works end-to-end with user testing",
            "Authentication system secure and user-friendly",
            "Frontend responsive and accessible across target devices",
            "API endpoints functional with proper error handling"
        ],
        "success_criteria": [
            "Stakeholders can see working software demonstrating value",
            "Technical foundation supports planned feature development",
            "User experience foundation established and validated",
            "Development velocity established for future sprint planning"
        ]
    },
    {
        "name": "Development Sprint 3-4: Feature Implementation",
        "duration_weeks": 4,
        "description": "Implement primary features and enhance user experience",
        "key_activities": [
            "Priority feature development based on product backlog",
            "User interface enhancement and user experience optimization",
            "Advanced backend functionality and business logic",
            "Integration testing and quality assurance"
        ],
        "deliverables": [
            "Primary features implemented and user-tested",
            "Enhanced user interface with improved user experience",
            "Complete backend functionality supporting business requirements",
            "Comprehensive test suite with automated testing"
        ],
        "quality_gates": [
            "All priority features meet acceptance criteria",
            "User interface provides excellent user experience",
            "Backend services handle expected load and edge cases",
            "Test coverage adequate for confident releases"
        ],
        "success_criteria": [
            "Application provides significant value to target users",
            "User feedback positive on feature implementation and usability",
            "System performance meets requirements under realistic usage",
            "Code quality maintained through review and testing processes"
        ]
    },
    {
        "name": "Development Sprint 5-6: Enhancement & Polish",
        "duration_weeks": 4,
        "description": "Complete remaining features and optimize overall experience",
        "key_activities": [
            "Remaining feature implementation and refinement",
            "Performance optimization and system tuning",
            "User experience polish and accessibility improvements",
            "Security hardening and vulnerability assessment"
        ],
        "deliverables": [
            "Complete feature set with polished implementation",
            "Optimized system performance and resource usage",
            "Refined user experience meeting accessibility standards",
            "Security-hardened application with vulnerability assessment"
        ],
        "quality_gates": [
            "All planned features implemented and working correctly",
            "System performance optimized and meeting requirements",
            "User experience excellent across all supported platforms",
            "Security assessment shows acceptable risk profile"
        ],
        "success_criteria": [
            "Application ready for production use with confidence",
            "User experience delights users and supports adoption",
            "Technical implementation supports scalability and maintenance",
            "Security posture appropriate for intended usage and data"
        ]
    },
    {
        "name": "Release Preparation & Deployment",
        "duration_weeks": 2,
        "description": "Prepare for production release and deploy to live environment",
        "key_activities": [
            "Final testing including user acceptance testing",
            "Production deployment planning and execution",
            "User documentation and training material creation",
            "Monitoring and support process establishment"
        ],
        "deliverables": [
            "Production-ready application with complete testing",
            "Live production deployment with monitoring",
            "User documentation and training materials",
            "Support processes and escalation procedures"
        ],
        "quality_gates": [
            "All testing completed successfully with no critical issues",
            "Production deployment successful with proper monitoring",
            "Users able to successfully use application with documentation",
            "Support team ready to handle user questions and issues"
        ],
        "success_criteria": [
            "Application serving users successfully in production",
            "Users adopting application and achieving intended benefits",
            "System stable and performing well under real usage",
            "Support and maintenance processes functioning effectively"
        ]
    }
]
EOF
}

# Generate quality gates based on project characteristics
generate_quality_gates() {
    local project_profile="$1"
    local phases="$2"

    # Extract quality requirements from project profile
    local security_requirements
    local compliance_needs
    local performance_requirements
    local scalability_requirements

    security_requirements=$(echo "$project_profile" | jq -r '.security_requirements // "standard"')
    compliance_needs=$(echo "$project_profile" | jq -r '.compliance_requirements // []')
    performance_requirements=$(echo "$project_profile" | jq -r '.performance_requirements // "standard"')
    scalability_requirements=$(echo "$project_profile" | jq -r '.scalability_requirements // "medium"')

    log_info "Generating quality gates for $security_requirements security, $performance_requirements performance"

    # Generate comprehensive quality gates
    cat << EOF
{
    "quality_framework": {
        "security_level": "$security_requirements",
        "compliance_requirements": $compliance_needs,
        "performance_level": "$performance_requirements",
        "scalability_level": "$scalability_requirements"
    },
    "phase_quality_gates": $(echo "$phases" | jq '[.[] | {
        phase_name: .name,
        quality_gates: .quality_gates,
        validation_requirements: (
            if ($security_requirements == "high" or $security_requirements == "critical") then
                .quality_gates + ["Security review and vulnerability assessment required"]
            else
                .quality_gates
            end |
            if ($compliance_needs | length > 0) then
                . + ["Compliance validation against regulatory requirements"]
            else
                .
            end |
            if ($performance_requirements == "high") then
                . + ["Performance testing under realistic load conditions"]
            else
                .
            end
        )
    }]')
}
EOF
}

# Generate milestone definitions with success metrics
generate_milestones() {
    local phases="$1"
    local project_profile="$2"

    log_info "Generating project milestones and success metrics"

    # Extract project characteristics for milestone customization
    local project_scale
    local business_domain

    project_scale=$(echo "$project_profile" | jq -r '.project_scale // "sme"')
    business_domain=$(echo "$project_profile" | jq -r '.business_domain // "general"')

    # Generate milestone structure
    cat << EOF
{
    "milestone_framework": {
        "project_scale": "$project_scale",
        "business_domain": "$business_domain",
        "success_measurement_approach": "outcome_focused"
    },
    "milestones": $(echo "$phases" | jq '[.[] | {
        milestone_name: (.name + " Completion"),
        target_week: (
            if .duration_weeks then
                ([.duration_weeks] | add)
            else
                4
            end
        ),
        success_criteria: .success_criteria,
        business_value: (
            if (.name | contains("MVP")) then
                "Validated product-market fit and user value proposition"
            elif (.name | contains("Foundation") or .name | contains("Setup")) then
                "Technical foundation supporting all planned functionality"
            elif (.name | contains("Feature") or .name | contains("Development")) then
                "Working features providing user value and business benefits"
            elif (.name | contains("Testing") or .name | contains("Quality")) then
                "Production-ready quality with confidence in reliability"
            elif (.name | contains("Deploy") or .name | contains("Launch")) then
                "Live system serving users and delivering business value"
            else
                "Planned outcomes achieved meeting stakeholder expectations"
            end
        ),
        risk_mitigation: [
            "Regular stakeholder communication and expectation management",
            "Continuous integration and automated testing",
            "Iterative development with frequent validation",
            "Proactive risk identification and mitigation planning"
        ]
    }]')
}
EOF
}

# Generate complete phase-based development guide
generate_development_guide() {
    local project_dir="${1:-$PWD}"

    log_info "🚀 Generating Phase-Based Development Guide"
    log_info "Project directory: $project_dir"

    create_output_directory

    # Load or generate project profile
    local project_profile
    if ! project_profile=$(load_project_profile "$project_dir"); then
        log_error "Failed to load project profile. Please run workflow analysis first."
        return 1
    fi

    # Generate phase structure
    log_info "📋 Generating phase structure based on project characteristics"
    local phase_structure
    phase_structure=$(generate_phase_structure "$project_profile")

    # Extract phases for further processing
    local phases
    phases=$(echo "$phase_structure" | jq '.phases')

    # Generate quality gates
    log_info "🛡️ Generating quality gates and validation criteria"
    local quality_gates
    quality_gates=$(generate_quality_gates "$project_profile" "$phases")

    # Generate milestones
    log_info "📊 Generating milestones and success metrics"
    local milestones
    milestones=$(generate_milestones "$phases" "$project_profile")

    # Combine everything into comprehensive development guide
    local development_guide
    development_guide=$(cat << EOF
{
    "metadata": {
        "generated_at": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
        "generator": "phase_generator.sh",
        "version": "1.0.0",
        "project_directory": "$project_dir"
    },
    "project_profile": $project_profile,
    "phase_structure": $phase_structure,
    "quality_framework": $quality_gates,
    "milestone_framework": $milestones,
    "implementation_guide": {
        "usage_instructions": [
            "Each phase contains specific activities, deliverables, and success criteria",
            "Quality gates must be passed before proceeding to next phase",
            "Milestones provide checkpoints for stakeholder communication",
            "Adapt timeline and activities based on project-specific constraints"
        ],
        "team_coordination": [
            "Assign phase ownership to appropriate team members",
            "Schedule regular milestone reviews with stakeholders",
            "Use quality gates for go/no-go decision making",
            "Maintain documentation throughout development process"
        ],
        "risk_management": [
            "Monitor progress against milestone targets",
            "Escalate quality gate failures immediately",
            "Adapt phases based on changing requirements or constraints",
            "Maintain communication with all stakeholders throughout process"
        ]
    }
}
EOF
)

    # Save development guide to output file
    local output_file="$OUTPUT_DIR/development_guide.json"
    echo "$development_guide" | jq '.' > "$output_file"

    log_success "Phase-Based Development Guide generated successfully"
    log_info "Output file: $output_file"

    # Generate human-readable summary
    generate_guide_summary "$development_guide" "$OUTPUT_DIR"

    return 0
}

# Generate human-readable summary of development guide
generate_guide_summary() {
    local development_guide="$1"
    local output_dir="$2"
    local summary_file="$output_dir/DEVELOPMENT_GUIDE.md"

    # Extract key information
    local project_scale
    local phase_template
    local total_phases
    local total_weeks

    project_scale=$(echo "$development_guide" | jq -r '.project_profile.project_scale // "sme"')
    phase_template=$(echo "$development_guide" | jq -r '.phase_structure.phase_template // "standard_agile"')
    total_phases=$(echo "$development_guide" | jq '.phase_structure.phases | length')
    total_weeks=$(echo "$development_guide" | jq '.phase_structure.phases | map(.duration_weeks // 4) | add')

    # Generate markdown summary
    cat > "$summary_file" << EOF
# Phase-Based Development Guide

**Generated:** $(date)
**Project Scale:** ${project_scale^}
**Phase Template:** ${phase_template}
**Total Phases:** $total_phases
**Estimated Duration:** $total_weeks weeks

## Development Phases Overview

$(echo "$development_guide" | jq -r '.phase_structure.phases[] |
    "### " + .name + " (" + (.duration_weeks // 4 | tostring) + " weeks)\n" +
    .description + "\n\n" +
    "**Key Activities:**\n" +
    (.key_activities[] | "- " + .) + "\n\n" +
    "**Success Criteria:**\n" +
    (.success_criteria[] | "- " + .) + "\n"'
)

## Quality Framework

### Quality Gates Summary
$(echo "$development_guide" | jq -r '.quality_framework.phase_quality_gates[] |
    "**" + .phase_name + ":**\n" +
    (.validation_requirements[] | "- " + .) + "\n"'
)

## Project Milestones

$(echo "$development_guide" | jq -r '.milestone_framework.milestones[] |
    "### " + .milestone_name + " (Week " + (.target_week | tostring) + ")\n" +
    "**Business Value:** " + .business_value + "\n\n" +
    "**Success Criteria:**\n" +
    (.success_criteria[] | "- " + .) + "\n"'
)

## Implementation Guidelines

### Team Coordination
- Assign phase ownership to appropriate team members based on expertise
- Schedule regular milestone reviews with stakeholders for alignment
- Use quality gates for go/no-go decision making at phase transitions
- Maintain comprehensive documentation throughout development process

### Quality Management
- All quality gates must be passed before proceeding to next phase
- Conduct regular reviews of deliverables against acceptance criteria
- Implement continuous integration and automated testing throughout
- Schedule security and compliance reviews at appropriate phase transitions

### Risk Management
- Monitor progress against milestone targets with regular status updates
- Escalate quality gate failures immediately to project stakeholders
- Adapt phases based on changing requirements or discovered constraints
- Maintain proactive communication with all stakeholders throughout process

---

*This development guide was generated automatically based on project analysis. Adapt phases and timelines based on project-specific constraints and requirements.*
EOF

    log_success "Human-readable development guide created: $summary_file"
}

# Main function
main() {
    local command="${1:-generate}"
    local project_dir="${2:-$PWD}"

    case "$command" in
        "generate")
            generate_development_guide "$project_dir"
            ;;
        "help"|"--help"|"-h")
            cat << EOF
Phase-Based Development Guide Generator

USAGE:
    $0 [COMMAND] [PROJECT_DIR]

COMMANDS:
    generate    Generate phase-based development guide (default)
    help        Show this help message

ARGUMENTS:
    PROJECT_DIR    Directory to analyze (default: current directory)

EXAMPLES:
    $0                        # Generate guide for current directory
    $0 generate /path/to/project    # Generate guide for specific project
    $0 help                   # Show help

OUTPUT FILES:
    workflow_output/development_guide.json    # Complete development guide data
    workflow_output/DEVELOPMENT_GUIDE.md     # Human-readable summary

DEPENDENCIES:
    - jq (for JSON processing)
    - workflow_analyzer.sh (for project analysis)
    - project_detector.sh (for technology detection)
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