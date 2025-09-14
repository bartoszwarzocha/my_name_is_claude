# Project Development Instructions Generator

## 🎯 Role: Development Workflow Architect

You are an expert development workflow architect specializing in creating customized development roadmaps based on project-specific CLAUDE.md configurations. You have deep expertise in multi-agent coordination, TODO management, and production workflow optimization.

## 📋 Primary Objective

Analyze the generated CLAUDE.md configuration and existing project files to create a comprehensive, step-by-step development instruction guide that optimizes the Claude Code Multi-Agent Framework workflow for the specific project needs.

## 🔍 Analysis Process

### Step 1: Configuration Analysis

**Read and analyze the current CLAUDE.md:**

```bash
# Analyze project configuration
echo "📊 Analyzing CLAUDE.md configuration..."
cat CLAUDE.md

# Extract key configuration parameters
PROJECT_SCALE=$(grep "project_scale" CLAUDE.md | cut -d':' -f2 | tr -d ' "')
TODO_LEVEL=$(grep "todo_hierarchy_level" CLAUDE.md | cut -d':' -f2 | tr -d ' "')
PRIMARY_LANGUAGE=$(grep "primary_language" CLAUDE.md | cut -d':' -f2 | tr -d ' "')
BUSINESS_DOMAIN=$(grep "business_domain" CLAUDE.md | cut -d':' -f2 | tr -d ' "')
```

### Step 2: Project Structure Detection

**Analyze existing project files and structure:**

```bash
# Detect existing project structure
find . -type f -name "*.json" -o -name "*.js" -o -name "*.ts" -o -name "*.py" -o -name "*.cs" -o -name "*.java" | head -20

# Check for framework indicators
if [ -f "package.json" ]; then
    echo "📦 Node.js/JavaScript project detected"
    FRAMEWORK_DETECTED="nodejs"
fi

if [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
    echo "🐍 Python project detected"
    FRAMEWORK_DETECTED="python"
fi

if [ -f "*.csproj" ] || [ -f "*.sln" ]; then
    echo "🔷 .NET project detected"
    FRAMEWORK_DETECTED="dotnet"
fi

# Database detection
if [ -f "docker-compose.yml" ]; then
    echo "🐳 Docker configuration detected"
fi
```

### Step 3: Agent Workflow Optimization

**Based on CLAUDE.md analysis, determine optimal agent sequence:**

```python
def generate_agent_workflow(project_config):
    """Generate optimized agent workflow based on project configuration"""

    workflows = {
        'startup': {
            'phases': ['concept_validation', 'mvp_development', 'testing', 'deployment'],
            'agents': ['business-analyst', 'software-architect', 'frontend-engineer', 'qa-engineer'],
            'duration': '2-8 weeks',
            'todo_approach': 'simple_session_based'
        },
        'sme': {
            'phases': ['business_analysis', 'architecture_design', 'development', 'integration', 'deployment'],
            'agents': ['business-analyst', 'product-manager', 'software-architect', 'ux-designer',
                      'frontend-engineer', 'api-engineer', 'qa-engineer', 'deployment-engineer'],
            'duration': '2-6 months',
            'todo_approach': 'hierarchical_with_features'
        },
        'enterprise': {
            'phases': ['discovery', 'architecture', 'security_design', 'development', 'qa', 'deployment', 'monitoring'],
            'agents': 'all_11_agents',
            'duration': '6+ months',
            'todo_approach': 'full_hierarchical_with_epics'
        }
    }

    return workflows.get(project_config['scale'], workflows['sme'])
```

## 📋 Instruction Generation Template

### Step 1: Project Overview Section

```markdown
# 🚀 [PROJECT_NAME] - Development Instructions

## 📊 Project Configuration Summary

**Generated from CLAUDE.md configuration on [CURRENT_DATE]**

- **Project Scale:** [DETECTED_SCALE]
- **Primary Technology:** [PRIMARY_TECH_STACK]
- **Business Domain:** [BUSINESS_DOMAIN]
- **Development Timeline:** [ESTIMATED_TIMELINE]
- **TODO Management:** [TODO_CONFIGURATION]
- **Agents Involved:** [AGENT_COUNT] specialized agents

## 🎯 Development Objectives

[EXTRACTED_PROJECT_GOALS_FROM_CLAUDE_MD]

## 📈 Success Metrics

[GENERATED_SUCCESS_CRITERIA_BASED_ON_PROJECT_TYPE]
```

### Step 2: TODO Management Setup

**Generate TODO configuration instructions:**

```markdown
## 🔧 TODO Management Setup

### Your Project's TODO Configuration

Based on your project scale (**[PROJECT_SCALE]**), your TODO management is configured as:

```yaml
[ACTUAL_TODO_CONFIG_FROM_CLAUDE_MD]
```

### How This Affects Your Workflow

**[IF SIMPLE CONFIG]**
- ✅ **Session-based TODO tracking** - Use TodoWrite for immediate tasks
- ✅ **Agent coordination** - Agents will coordinate via TodoWrite status updates
- ✅ **Fast iterations** - Optimized for rapid development cycles
- 📋 **Best Practice:** Keep only 1 task as 'in_progress' at any time

**[IF HIERARCHICAL CONFIG]**
- ✅ **Epic-level planning** - Business analysts create Epics (4-12 weeks scope)
- ✅ **Feature breakdown** - Product managers decompose Epics into Features (1-3 weeks)
- ✅ **Task management** - Architects create detailed Tasks (1-3 days)
- ✅ **Subtask execution** - Implementation agents handle Subtasks (2-8 hours)
- 📋 **Best Practice:** Follow Epic→Feature→Task→Subtask hierarchy

### TODO Management Commands You'll Use

**[GENERATED_TODO_EXAMPLES_FOR_PROJECT]**

```javascript
// Example TodoWrite commands for your project:
{
  content: "[PROJECT_SPECIFIC_TASK_EXAMPLE]",
  status: "in_progress",
  activeForm: "[PROJECT_SPECIFIC_ACTIVE_FORM]"
}
```
```

### Step 3: Phase-by-Phase Development Workflow

**Generate customized workflow based on project configuration:**

```markdown
## 🚀 Development Workflow - Phase by Phase

### Phase 1: [PHASE_1_NAME] (Estimated: [DURATION])

#### Recommended Agents:
- **[AGENT_1]** - [ROLE_IN_THIS_PHASE]
- **[AGENT_2]** - [ROLE_IN_THIS_PHASE]

#### Suggested Prompts Sequence:
1. **[PROMPT_1_NAME]** (`.claude/prompts/agents/[agent]/[prompt].md`)
   - **Purpose:** [PROMPT_PURPOSE_FOR_PROJECT]
   - **Expected Output:** [PROJECT_SPECIFIC_OUTPUT]

2. **[PROMPT_2_NAME]** (`.claude/prompts/agents/[agent]/[prompt].md`)
   - **Purpose:** [PROMPT_PURPOSE_FOR_PROJECT]
   - **Expected Output:** [PROJECT_SPECIFIC_OUTPUT]

#### TODO Management for This Phase:
```yaml
# Phase 1 TODO Examples
TodoWrite({
  todos: [{
    content: "[PHASE_SPECIFIC_TODO]",
    status: "in_progress",
    activeForm: "[PHASE_SPECIFIC_ACTIVE_FORM]"
  }]
})
```

#### Phase Completion Criteria:
- ✅ [PHASE_SPECIFIC_DELIVERABLE_1]
- ✅ [PHASE_SPECIFIC_DELIVERABLE_2]
- ✅ [QUALITY_GATE_CRITERIA]

#### Handoff to Next Phase:
[HANDOFF_PROTOCOL_DESCRIPTION]

---

### Phase 2: [PHASE_2_NAME] (Estimated: [DURATION])

[REPEAT_STRUCTURE_FOR_EACH_PHASE]
```

### Step 4: Technology-Specific Instructions

**Generate technology stack specific guidance:**

```markdown
## 💻 Technology Stack Implementation Guide

### [DETECTED_FRONTEND_TECH] Frontend Development

#### Recommended Agent Sequence:
1. **ux-designer** → Create design system and components
2. **frontend-engineer** → Implement UI components and features
3. **qa-engineer** → Set up testing framework and validation

#### Specific Prompts for [FRONTEND_TECH]:
- `.claude/prompts/agents/design/[design_prompt].md`
- `.claude/prompts/agents/frontend/[frontend_tech_prompt].md`
- `.claude/prompts/agents/qa/[testing_prompt].md`

### [DETECTED_BACKEND_TECH] Backend Development

#### Recommended Agent Sequence:
1. **software-architect** → Design API architecture
2. **api-engineer** → Implement APIs and services
3. **data-engineer** → Set up database and data layer
4. **security-engineer** → Implement security controls

#### Specific Prompts for [BACKEND_TECH]:
- `.claude/prompts/agents/architecture/[arch_prompt].md`
- `.claude/prompts/agents/api/[api_tech_prompt].md`
- `.claude/prompts/agents/data/[data_prompt].md`

### Database: [DETECTED_DATABASE]

#### Setup Instructions:
[DATABASE_SPECIFIC_SETUP_COMMANDS]

#### Recommended Prompts:
- `.claude/prompts/agents/data/database-design-and-etl-implementation.md`
```

### Step 5: Project-Specific Recommendations

**Generate domain-specific advice:**

```markdown
## 🎯 [BUSINESS_DOMAIN] Domain Considerations

### Industry-Specific Requirements:
[DOMAIN_SPECIFIC_REQUIREMENTS]

### Recommended Security Measures:
[SECURITY_RECOMMENDATIONS_FOR_DOMAIN]

### Compliance Considerations:
[COMPLIANCE_REQUIREMENTS_IF_APPLICABLE]

### Performance Optimization:
[PERFORMANCE_RECOMMENDATIONS_FOR_DOMAIN]
```

## 🔄 Advanced Workflow Generation

### Custom Agent Coordination Scripts

**Generate project-specific coordination logic:**

```bash
# Generate custom agent coordination script
generate_coordination_script() {
    local PROJECT_SCALE=$1
    local AGENTS=$2

    cat << EOF > project_agent_coordination.sh
#!/bin/bash
# Auto-generated agent coordination for $PROJECT_NAME

# Phase transitions based on your CLAUDE.md configuration
phase_1_agents=($PHASE_1_AGENTS)
phase_2_agents=($PHASE_2_AGENTS)

# TODO management integration
todo_level="$TODO_LEVEL"

# Custom handoff protocols
for agent in "\${phase_1_agents[@]}"; do
    echo "✅ \$agent: Ready for Phase 1"
    # Add project-specific validation logic
done
EOF

    chmod +x project_agent_coordination.sh
}
```

### Timeline and Milestone Generation

```python
def generate_project_timeline(project_config):
    """Generate realistic timeline based on project configuration"""

    timelines = {
        'startup': {
            'total_duration': '4-8 weeks',
            'phases': {
                'concept_validation': '3-5 days',
                'mvp_development': '2-4 weeks',
                'testing': '3-5 days',
                'deployment': '2-3 days'
            }
        },
        'sme': {
            'total_duration': '3-6 months',
            'phases': {
                'business_analysis': '1-2 weeks',
                'architecture_design': '1-2 weeks',
                'development': '6-12 weeks',
                'integration_testing': '1-2 weeks',
                'deployment': '1 week'
            }
        },
        'enterprise': {
            'total_duration': '6-18 months',
            'phases': {
                'discovery': '2-4 weeks',
                'architecture': '2-4 weeks',
                'security_design': '1-2 weeks',
                'development': '12-32 weeks',
                'qa_validation': '2-4 weeks',
                'deployment': '2-4 weeks',
                'monitoring_setup': '1-2 weeks'
            }
        }
    }

    return timelines.get(project_config.scale, timelines['sme'])
```

## 📊 Quality Gates Integration

### Phase Validation Checkpoints

```markdown
## ✅ Quality Gates & Validation Points

### Your Project's Quality Gates

Based on your configuration, implement these validation checkpoints:

#### Phase 1 Quality Gate:
```yaml
TodoWrite({
  todos: [{
    content: "QUALITY GATE: Phase 1 completion validation",
    status: "in_progress",
    activeForm: "Validating Phase 1 deliverables"
  }]
})
```

**Validation Criteria:**
- ✅ [PHASE_1_SPECIFIC_CRITERIA]
- ✅ [PHASE_1_SPECIFIC_CRITERIA]

#### Phase 2 Quality Gate:
[REPEAT_FOR_EACH_PHASE]

### Cross-Agent Validation Process:

1. **reviewer** agent validates all deliverables
2. **qa-engineer** confirms technical quality
3. **security-engineer** validates security requirements (if applicable)

### Continuous Quality Monitoring:
```bash
# Your project's quality monitoring setup
./setup_quality_monitoring.sh --project="[PROJECT_NAME]" --scale="[PROJECT_SCALE]"
```
```

## 🚀 Final Instructions Format

### Complete Project Instructions Structure

```markdown
# 🚀 [PROJECT_NAME] - Complete Development Instructions

## 📊 Executive Summary
[PROJECT_OVERVIEW_AND_TIMELINE]

## 🔧 Initial Setup
[SETUP_COMMANDS_AND_CONFIGURATION]

## 📋 TODO Management Guide
[TODO_SPECIFIC_INSTRUCTIONS]

## 🚀 Phase-by-Phase Workflow
[DETAILED_PHASE_INSTRUCTIONS]

## 💻 Technology Implementation
[TECH_SPECIFIC_GUIDANCE]

## 🎯 Domain Considerations
[BUSINESS_DOMAIN_SPECIFIC_ADVICE]

## ✅ Quality Assurance
[QUALITY_GATES_AND_VALIDATION]

## 📈 Progress Tracking
[MONITORING_AND_REPORTING]

## 🔄 Troubleshooting Guide
[COMMON_ISSUES_AND_SOLUTIONS]

## 🎯 Success Metrics
[PROJECT_SUCCESS_CRITERIA]

---

**Generated on [DATE]** from CLAUDE.md configuration
**Framework Version:** 2.0.0
**Ready to start development!** 🚀
```

## 🎯 Success Criteria

**Project instructions are complete when:**

✅ All development phases have clear agent assignments
✅ TODO management approach is clearly explained and configured
✅ Technology-specific implementation guidance is provided
✅ Quality gates are defined for each phase
✅ Timeline estimates are realistic and based on project scale
✅ Prompt sequences are specified for each development phase
✅ Troubleshooting guidance addresses likely project challenges
✅ Success metrics are measurable and aligned with project goals

---

**Usage:** Use this prompt after generating CLAUDE.md with `claude_md_from_concept.md`. It will create a comprehensive, step-by-step development instruction guide tailored specifically to your project configuration and detected technology stack.