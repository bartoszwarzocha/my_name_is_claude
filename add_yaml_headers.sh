#!/bin/bash

# Script to add YAML headers to all agent files
# Only processes files that don't already have YAML headers

set -e

readonly COLOR_GREEN=$(tput setaf 2)
readonly COLOR_YELLOW=$(tput setaf 3)
readonly COLOR_BLUE=$(tput setaf 4)
readonly COLOR_RESET=$(tput sgr0)

echo "${COLOR_BLUE}Adding YAML headers to agent files...${COLOR_RESET}"

process_agent() {
    local agent_file="$1"
    local agent_name=$(basename "$agent_file" .md)

    # Skip if already has YAML header
    if grep -q "^---" "$agent_file" && grep -q "^name:" "$agent_file"; then
        echo "${COLOR_GREEN}✅ $agent_name already has YAML header${COLOR_RESET}"
        return 0
    fi

    echo "${COLOR_YELLOW}📝 Processing $agent_name...${COLOR_RESET}"

    # Determine category and subcategory from path
    local path_category=""
    local path_subcategory=""
    local agent_type=""

    if [[ "$agent_file" == *"/core/"* ]]; then
        agent_type="Core"
    elif [[ "$agent_file" == *"/enterprise/"* ]]; then
        agent_type="Enterprise"
    elif [[ "$agent_file" == *"/custom/"* ]]; then
        agent_type="Custom"
    else
        agent_type="Core"
    fi

    # Extract category from directory structure
    if [[ "$agent_file" == *"/architecture/"* ]]; then
        path_category="Architecture"
        path_subcategory="System Design"
    elif [[ "$agent_file" == *"/development/"* ]]; then
        path_category="Development"
        path_subcategory="Engineering"
    elif [[ "$agent_file" == *"/data/"* ]]; then
        path_category="Data"
        path_subcategory="Data Engineering"
    elif [[ "$agent_file" == *"/management/"* ]]; then
        path_category="Management"
        path_subcategory="Project Management"
    elif [[ "$agent_file" == *"/operations/"* ]]; then
        path_category="Operations"
        path_subcategory="Infrastructure"
    elif [[ "$agent_file" == *"/quality/"* ]]; then
        path_category="Quality"
        path_subcategory="Quality Assurance"
    elif [[ "$agent_file" == *"/graphics/"* ]]; then
        path_category="Graphics"
        path_subcategory="Visual Computing"
    elif [[ "$agent_file" == *"/hardware/"* ]]; then
        path_category="Hardware"
        path_subcategory="Electronics"
    elif [[ "$agent_file" == *"/desktop/"* ]]; then
        path_category="Desktop"
        path_subcategory="Application Development"
    elif [[ "$agent_file" == *"/scientific/"* ]]; then
        path_category="Scientific"
        path_subcategory="Scientific Computing"
    else
        path_category="General"
        path_subcategory="Software Development"
    fi

    # Generate description based on agent name
    local description=""
    case "$agent_name" in
        "software-architect")
            description="Enterprise systems architect specializing in scalable architecture design, cloud technologies, and mission-critical systems serving millions of users"
            ;;
        "ux-designer")
            description="User experience designer focused on creating intuitive, accessible, and engaging digital experiences through research-driven design"
            ;;
        "data-engineer")
            description="Data engineering specialist building robust data pipelines, warehouses, and analytics infrastructure for enterprise-scale data processing"
            ;;
        "api-engineer")
            description="API development expert designing and implementing scalable REST, GraphQL, and microservices architectures with enterprise security standards"
            ;;
        "backend-engineer")
            description="Backend systems engineer specializing in server-side development, database design, and high-performance distributed systems architecture"
            ;;
        "frontend-engineer")
            description="Frontend development specialist creating responsive, performant user interfaces using modern frameworks and progressive web technologies"
            ;;
        "session-manager")
            description="Session management specialist coordinating multi-agent workflows, state preservation, and seamless handoffs between development phases"
            ;;
        "deployment-engineer")
            description="Deployment and infrastructure automation expert managing CI/CD pipelines, containerization, and cloud platform optimization"
            ;;
        "qa-engineer")
            description="Quality assurance engineer implementing comprehensive testing strategies, automation frameworks, and quality gates for enterprise software"
            ;;
        "security-engineer")
            description="Security engineering specialist implementing secure architecture patterns, threat modeling, and compliance frameworks for enterprise applications"
            ;;
        "business-analyst")
            description="Business requirements analyst bridging stakeholder needs with technical solutions through comprehensive analysis and documentation"
            ;;
        "product-manager")
            description="Product management specialist driving product strategy, roadmap planning, and cross-functional team coordination for successful delivery"
            ;;
        "3d-addon-developer")
            description="3D application addon developer specializing in Blender extensions, Maya plugins, and custom 3D workflow automation tools"
            ;;
        "cad-engineer")
            description="CAD systems engineer developing precision engineering tools, parametric modeling solutions, and technical drawing automation systems"
            ;;
        "desktop-specialist")
            description="Desktop application specialist building native cross-platform applications using modern frameworks like wxWidgets, Qt, and Electron"
            ;;
        "graphics-2d-engineer")
            description="2D graphics engineer specializing in image processing, vector graphics, digital art tools, and high-performance rendering algorithms"
            ;;
        "graphics-3d-engineer")
            description="3D graphics engineer expert in OpenGL, Vulkan, real-time rendering, game engines, and advanced visualization techniques"
            ;;
        "math-specialist")
            description="Mathematical computing specialist implementing numerical algorithms, scientific simulations, and advanced mathematical modeling solutions"
            ;;
        "electronics-engineer")
            description="Electronics systems engineer designing embedded hardware, PCB layouts, sensor integration, and IoT device development"
            ;;
        "embedded-engineer")
            description="Embedded systems engineer developing firmware, real-time systems, microcontroller programming, and hardware-software integration"
            ;;
        "scientific-computing-specialist")
            description="Scientific computing expert developing research software, data analysis tools, and high-performance computing solutions for scientific domains"
            ;;
        *)
            # Generate generic description based on name
            local formatted_name=$(echo "$agent_name" | sed 's/-/ /g' | sed 's/\b\w/\U&/g')
            description="$formatted_name specialist providing expert guidance and implementation support for enterprise-scale projects"
            ;;
    esac

    # Read current content
    local current_content=$(cat "$agent_file")

    # Create YAML header
    local yaml_header="---
name: $(echo "$agent_name" | sed 's/-/ /g' | sed 's/\b\w/\U&/g')
description: \"$description\"
category: $path_category
subcategory: $path_subcategory
agent_type: $agent_type
experience_level: \"Senior (10+ years)\"
framework_version: \"3.2.0+\"
---

"

    # Write new content with YAML header
    echo "$yaml_header$current_content" > "$agent_file"

    echo "${COLOR_GREEN}✅ Added YAML header to $agent_name${COLOR_RESET}"
}

# Process all agent files
find .claude/agents -name "*.md" -type f | while read -r agent_file; do
    process_agent "$agent_file"
done

echo ""
echo "${COLOR_GREEN}🎉 YAML header processing complete!${COLOR_RESET}"
echo "${COLOR_BLUE}Run validation to verify: ./ai-tools.sh -v${COLOR_RESET}"