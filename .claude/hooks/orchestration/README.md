# Workflow Orchestration Scenarios

Comprehensive orchestration scenarios for the Claude Code Multi-Agent Framework. These scenarios provide pre-configured workflows optimized for different project types and development approaches.

## 📁 Available Orchestration Scenarios

### 1. **Rapid MVP Development** (`rapid-mvp-scenario.sh`)

**Purpose:** Optimized workflow for quick MVP development with minimal overhead

**Best For:**
- Startup projects requiring fast time-to-market
- Proof-of-concept developments
- Prototype validation projects
- Resource-constrained early-stage development

**Key Features:**
- ⚡ Streamlined 4-phase workflow
- 🔄 Parallel execution for compatible agents
- 📋 Essential quality gates only
- 🚀 Optimized for speed and core functionality

**Usage:**
```bash
# Basic MVP for startup
./.claude/hooks/orchestration/rapid-mvp-scenario.sh "startup" "minimal"

# Extended MVP with additional features
./.claude/hooks/orchestration/rapid-mvp-scenario.sh "startup" "extended"

# Proof-of-concept development
./.claude/hooks/orchestration/rapid-mvp-scenario.sh "prototype" "minimal"
```

**Agent Flow:**
```
business-analyst → product-manager → 
(software-architect + ux-designer parallel) → 
(frontend-engineer + api-engineer parallel) → qa-engineer → 
deployment-engineer
```

### 2. **Enterprise Security-First Development** (`enterprise-security-first-scenario.sh`)

**Purpose:** Comprehensive workflow with security-by-design approach for enterprise applications

**Best For:**
- Regulated industry applications (fintech, healthcare, government)
- Enterprise applications with compliance requirements
- High-security applications with sensitive data
- Applications requiring GDPR, SOX, HIPAA compliance

**Key Features:**
- 🛡️ Security-by-design from Phase 1
- 📋 Continuous compliance validation
- 🔒 Multi-layered security validation
- 🏛️ Enterprise-grade quality gates

**Usage:**
```bash
# GDPR-compliant enterprise application
./.claude/hooks/orchestration/enterprise-security-first-scenario.sh "gdpr" "high" "enterprise"

# SOX-compliant financial application
./.claude/hooks/orchestration/enterprise-security-first-scenario.sh "sox" "critical" "regulated"

# HIPAA-compliant healthcare application
./.claude/hooks/orchestration/enterprise-security-first-scenario.sh "hipaa" "critical" "healthcare"
```

**Agent Flow:**
```
business-analyst + security-engineer (early threat modeling) → product-manager →
(software-architect + security-engineer + ux-designer + data-engineer parallel) →
(frontend-engineer + api-engineer + data-engineer with continuous security-engineer validation) →
qa-engineer → (deployment-engineer + security-engineer parallel) → reviewer
```

### 3. **Data-Driven Application Development** (`data-driven-scenario.sh`)

**Purpose:** Specialized workflow for data-centric applications with advanced analytics capabilities

**Best For:**
- Analytics platforms and dashboards
- Business intelligence applications
- Machine learning and AI applications
- Real-time data processing systems
- Reporting and visualization tools

**Key Features:**
- 📊 Data architecture-first approach
- 📈 Advanced analytics integration
- 🔍 Data quality and governance framework
- ⚡ Real-time processing capabilities

**Usage:**
```bash
# Advanced analytics platform
./.claude/hooks/orchestration/data-driven-scenario.sh "analytics" "enterprise" "advanced"

# Machine learning application
./.claude/hooks/orchestration/data-driven-scenario.sh "ml" "enterprise" "ai-ml"

# Real-time data processing system
./.claude/hooks/orchestration/data-driven-scenario.sh "realtime" "bigdata" "advanced"

# Business intelligence reporting
./.claude/hooks/orchestration/data-driven-scenario.sh "reporting" "enterprise" "basic"
```

**Agent Flow:**
```
business-analyst + data-engineer (early data analysis) → product-manager →
(data-engineer + software-architect parallel) → ux-designer + security-engineer →
data-engineer → (api-engineer + frontend-engineer parallel) → qa-engineer →
(deployment-engineer + data-engineer parallel) → reviewer
```

## 🚀 Quick Start Guide

### 1. Choose Your Scenario

Select the orchestration scenario that best matches your project requirements:

- **Speed-focused MVP:** Use `rapid-mvp-scenario.sh`
- **Security-critical enterprise:** Use `enterprise-security-first-scenario.sh`
- **Data and analytics-heavy:** Use `data-driven-scenario.sh`

### 2. Run the Orchestration

#### Automatic Orchestration (Recommended)
```bash
# Automatic scenario selection and execution
./.claude/hooks/orchestration-trigger.sh

# Interactive scenario selection with user confirmation
./.claude/hooks/orchestration-trigger.sh "$(pwd)" "" "interactive"

# Force specific scenario
./.claude/hooks/orchestration-trigger.sh "$(pwd)" "mvp"      # Rapid MVP
./.claude/hooks/orchestration-trigger.sh "$(pwd)" "security" # Enterprise Security
./.claude/hooks/orchestration-trigger.sh "$(pwd)" "data"     # Data-Driven
```

#### Manual Scenario Execution
```bash
# Example: Startup MVP
./.claude/hooks/orchestration/rapid-mvp-scenario.sh "startup" "minimal"

# Example: Enterprise security application
./.claude/hooks/orchestration/enterprise-security-first-scenario.sh "gdpr" "high" "enterprise"

# Example: Analytics platform
./.claude/hooks/orchestration/data-driven-scenario.sh "analytics" "enterprise" "advanced"
```

#### Advanced Conditional Workflows
```bash
# Intelligent conditional workflow execution
./.claude/hooks/orchestration/conditional-workflow-engine.sh "$(pwd)" "fintech" "dynamic"
./.claude/hooks/orchestration/conditional-workflow-engine.sh "$(pwd)" "auto" "learning"
```

### 3. Monitor Progress

#### Real-time Monitoring
```bash
# Real-time orchestration monitoring
./.claude/hooks/orchestration-monitor.sh "watch"

# Check current status
./.claude/hooks/orchestration-monitor.sh "status"

# View performance metrics
./.claude/hooks/orchestration-monitor.sh "metrics"

# View recent logs
./.claude/hooks/orchestration-monitor.sh "logs"

# Stop running orchestrations if needed
./.claude/hooks/orchestration-monitor.sh "kill"
```

#### Manual Progress Tracking
- **Live Progress:** Check `work/orchestration/*.log` files
- **Final Reports:** Review `work/orchestration/*-report-*.md` files
- **Agent Activity:** Monitor `work/agent-activity.log`

## 📊 Orchestration Outputs

### Generated Files and Reports

#### Log Files (`work/orchestration/`)
- `rapid-mvp-YYYYMMDD_HHMMSS.log` - MVP orchestration execution log
- `enterprise-security-YYYYMMDD_HHMMSS.log` - Security-first execution log
- `data-driven-YYYYMMDD_HHMMSS.log` - Data-driven execution log

#### Comprehensive Reports (`work/orchestration/`)
- `rapid-mvp-report-YYYYMMDD_HHMMSS.md` - MVP orchestration analysis
- `enterprise-security-report-YYYYMMDD_HHMMSS.md` - Security orchestration analysis
- `data-driven-report-YYYYMMDD_HHMMSS.md` - Data orchestration analysis

#### Activity Tracking
- `work/orchestration-activity.log` - Cross-scenario activity tracking
- `work/agent-activity.log` - Individual agent coordination log

### Report Contents

Each orchestration generates comprehensive reports including:

1. **Executive Summary** - High-level outcomes and business value
2. **Workflow Analysis** - Phase-by-phase execution details
3. **Quality Validation** - Quality gate results and validation metrics
4. **Technical Deliverables** - Complete list of created assets
5. **Performance Metrics** - Execution efficiency and optimization data
6. **Recommendations** - Next steps and improvement opportunities
7. **Lessons Learned** - Key insights and best practices

## 🛠️ Customization and Extension

### Creating Custom Scenarios

To create a custom orchestration scenario:

1. **Create New Scenario File:**
```bash
cp .claude/hooks/orchestration/rapid-mvp-scenario.sh .claude/hooks/orchestration/custom-scenario.sh
chmod +x .claude/hooks/orchestration/custom-scenario.sh
```

2. **Customize Agent Flow:**
   - Modify agent execution order
   - Adjust parallel execution groups
   - Customize quality gates and validation points
   - Add scenario-specific logic

3. **Update Documentation:**
   - Add scenario description to this README
   - Document usage parameters and examples
   - Include expected outputs and reports

### Scenario Template Structure

```bash
#!/bin/bash

# Custom Orchestration Scenario
# Description: Your scenario purpose
# Focus: Key areas and specializations

SCENARIO_NAME="Your Scenario Name"
PARAM1="${1:-default}"
PARAM2="${2:-default}"

# Setup logging
ORCHESTRATION_LOG="work/orchestration/custom-$(date +%Y%m%d_%H%M%S).log"

# Phase 1: Discovery
# ... agent coordination logic

# Phase 2: Architecture
# ... parallel execution groups

# Phase 3: Development  
# ... quality gates and validation

# Phase 4: Deployment
# ... final validation and reporting

# Generate comprehensive report
ORCHESTRATION_REPORT="work/orchestration/custom-report-$(date +%Y%m%d_%H%M%S).md"
# ... report generation
```

## 🎯 Best Practices for Orchestration

### Scenario Selection Guidelines

1. **Project Assessment:**
   - Analyze project requirements and constraints
   - Identify critical success factors (speed, security, data, etc.)
   - Consider compliance and regulatory requirements
   - Evaluate team expertise and resource availability

2. **Parameter Optimization:**
   - Use appropriate parameters for your specific context
   - Consider scalability and future growth requirements
   - Balance speed vs. thoroughness based on project phase
   - Align security level with actual risk requirements

3. **Quality Gate Configuration:**
   - Customize quality gates for your specific requirements
   - Adjust validation strictness based on project criticality
   - Consider automated vs. manual validation points
   - Plan for iterative improvement based on results

### Execution Best Practices

1. **Pre-Orchestration Preparation:**
   - Ensure all required agents have appropriate prompts
   - Verify project requirements are clearly defined
   - Check system requirements and dependencies
   - Review compliance requirements if applicable

2. **During Orchestration:**
   - Monitor progress through generated logs
   - Address quality gate failures promptly
   - Maintain clear communication channels
   - Document decisions and rationale

3. **Post-Orchestration:**
   - Review generated reports thoroughly
   - Implement recommended improvements
   - Document lessons learned for future projects
   - Share insights with team members

## 🔄 Integration with Multi-Agent Framework

### Automatic Integration Points

The orchestration scenarios automatically integrate with:

- **Quality Gates** - Via `quality-gate-checker.sh`
- **Agent Handoffs** - Via `agent-handoff.sh` 
- **Dependency Tracking** - Via `cross-agent-dependency-tracker.sh`
- **Performance Monitoring** - Via `agent-performance-monitor.sh`
- **Compliance Validation** - Via `compliance-automation.sh`
- **Conflict Resolution** - Via `agent-conflict-resolution.sh`

### Coordination with Existing Hooks

Orchestration scenarios work seamlessly with:

- **Task Logging** - All agent activities are logged
- **Documentation Tracking** - Changes are automatically tracked
- **Validation Hooks** - Quality gates are enforced
- **Performance Monitoring** - Metrics are collected automatically

## 📈 Success Metrics and KPIs

### Orchestration Efficiency Metrics

- **Time to Market** - Overall orchestration completion time
- **Quality Gate Pass Rate** - Percentage of successful validations
- **Agent Utilization** - Efficiency of parallel execution
- **Rework Rate** - Number of iterations required per phase

### Business Value Metrics

- **Feature Delivery Speed** - Rate of feature completion
- **Quality Score** - Overall deliverable quality assessment
- **Compliance Adherence** - Regulatory requirement fulfillment
- **Technical Debt** - Accumulated technical debt level

## 🤝 Contributing to Orchestration Scenarios

### Sharing Custom Scenarios

To contribute your custom orchestration scenarios:

1. **Document Scenario Purpose** - Clear description of use case
2. **Provide Usage Examples** - Multiple parameter combinations
3. **Include Success Stories** - Real project applications
4. **Submit via Pull Request** - Follow contribution guidelines

### Enhancement Requests

For orchestration improvements:

1. **Identify Enhancement Need** - Specific gap or opportunity
2. **Describe Expected Behavior** - Detailed requirement specification  
3. **Provide Business Justification** - Value proposition and ROI
4. **Suggest Implementation Approach** - Technical approach and considerations

---

**Note:** These orchestration scenarios represent proven workflows for different project types. They can be customized and extended based on specific project requirements and organizational needs.