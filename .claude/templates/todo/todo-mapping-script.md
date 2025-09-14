# TODO Mapping Script - Hierarchical Task Management Automation

**Purpose: Production-ready automation for Epic → Feature → Task → Subtask hierarchical TODO creation and agent coordination**

---

## 🎯 System Overview

This script provides **concrete, executable instructions** for agents to automatically create and coordinate hierarchical TODO structures based on CLAUDE.md configuration.

### Hierarchy Execution Flow

```yaml
business-analyst (Epic) → product-manager (Feature) → software-architect (Task) → implementation-agents (Subtask)
```

---

## 📋 Epic Level Creation (business-analyst, product-manager)

### Epic Creation Algorithm

```yaml
# CLAUDE.md Configuration Check
if epic_management == true and business-analyst in epic_owners:

  # Step 1: Epic Creation via TodoWrite
  Epic_Creation_Process:
    1. Use TodoWrite to create: "Epic: [Business Initiative Name]"
    2. Set status: "in_progress"
    3. Set activeForm: "Analyzing business requirements for [initiative]"

  # Step 2: Epic Breakdown Structure
  Epic_Breakdown_Template:
    Epic_Title: "Epic: Complete user authentication system overhaul"
    Business_Value: "Enable secure user management and compliance with GDPR"
    Success_Criteria:
      - "Users can securely login with multi-factor authentication"
      - "System meets GDPR compliance requirements"
      - "Authentication response time < 200ms"
      - "99.9% authentication availability"

    Estimated_Duration: "8-12 weeks"
    Estimated_Features: "3-5 features"
    Estimated_Tasks: "15-25 tasks"
    Estimated_Subtasks: "60-120 subtasks"

  # Step 3: Handoff Protocol
  Epic_Handoff_to_Product_Manager:
    1. Mark Epic todo as "completed"
    2. Create handoff todo: "Feature breakdown for Epic: [name]"
    3. Assign to product-manager
    4. Set dependency: "Epic validation completed"
```

### Epic Creation TodoWrite Commands

**Concrete TodoWrite usage for business-analyst:**

```typescript
// Step 1: Create Epic Analysis Todo
TodoWrite({
  content: "Epic: User authentication system overhaul - business analysis",
  status: "in_progress",
  activeForm: "Analyzing business requirements for authentication system"
});

// Step 2: Create Stakeholder Coordination Todo
TodoWrite({
  content: "Coordinate authentication requirements with stakeholders",
  status: "pending",
  activeForm: "Coordinating with stakeholders"
});

// Step 3: Create Epic Validation Todo
TodoWrite({
  content: "Validate Epic business value and feasibility",
  status: "pending",
  activeForm: "Validating Epic with reviewer"
});

// Step 4: Create Feature Breakdown Handoff
TodoWrite({
  content: "Handoff authenticated Epic to product-manager for Feature breakdown",
  status: "pending",
  activeForm: "Preparing Epic handoff to product-manager"
});
```

---

## 🏗️ Feature Level Breakdown (product-manager, software-architect)

### Feature Creation Algorithm

```yaml
# CLAUDE.md Configuration Check
if feature_breakdown == true and product-manager in epic_owners:

  # Step 1: Feature Creation from Epic
  Feature_Creation_Process:
    1. Receive Epic handoff from business-analyst
    2. Use TodoWrite to create: "Feature: [User-Facing Capability]"
    3. Break Epic into 3-5 Features based on user journeys

  # Step 2: Feature Template Structure
  Feature_Breakdown_Template:
    Epic_Reference: "Epic: Complete user authentication system overhaul"

    Feature_1:
      Title: "OAuth2 with multi-factor authentication"
      User_Value: "Users can login securely with external providers and MFA"
      Acceptance_Criteria:
        - "Users can login with Google/GitHub OAuth2"
        - "SMS/Email MFA required for sensitive operations"
        - "Remember device for 30 days option"
      Estimated_Duration: "2-3 weeks"
      Priority: "Critical"

    Feature_2:
      Title: "Session management dashboard"
      User_Value: "Users can view and manage their active sessions"
      Acceptance_Criteria:
        - "Users see list of active sessions with device/location"
        - "Users can terminate individual sessions"
        - "Real-time session activity notifications"
      Estimated_Duration: "1-2 weeks"
      Priority: "High"

  # Step 3: Technical Feasibility Coordination
  Feature_Technical_Handoff:
    1. Coordinate with software-architect for technical feasibility
    2. Validate with ux-designer for user experience requirements
    3. Create Task breakdown handoff to software-architect
```

### Feature Creation TodoWrite Commands

**Concrete TodoWrite usage for product-manager:**

```typescript
// Step 1: Receive Epic Handoff
TodoWrite({
  content: "Feature breakdown for Epic: User authentication system",
  status: "in_progress",
  activeForm: "Breaking Epic into user-facing Features"
});

// Step 2: Create Individual Feature Todos
TodoWrite({
  content: "Feature: OAuth2 with multi-factor authentication implementation",
  status: "pending",
  activeForm: "Defining OAuth2 MFA feature requirements"
});

TodoWrite({
  content: "Feature: Session management dashboard for users",
  status: "pending",
  activeForm: "Defining session management feature requirements"
});

// Step 3: Coordination Todos
TodoWrite({
  content: "Validate Feature technical feasibility with software-architect",
  status: "pending",
  activeForm: "Coordinating technical feasibility validation"
});

TodoWrite({
  content: "Validate Feature UX requirements with ux-designer",
  status: "pending",
  activeForm: "Coordinating UX requirements validation"
});

// Step 4: Task Breakdown Handoff
TodoWrite({
  content: "Handoff validated Features to software-architect for Task creation",
  status: "pending",
  activeForm: "Preparing Feature handoff to software-architect"
});
```

---

## ⚙️ Task Level Implementation (software-architect → implementation agents)

### Task Creation Algorithm

```yaml
# CLAUDE.md Configuration Check
if auto_task_creation == true and software-architect in feature_owners:

  # Step 1: Technical Task Breakdown
  Task_Creation_Process:
    1. Receive Feature handoff from product-manager
    2. Analyze Feature technical requirements
    3. Create Task todos for each implementation component
    4. Assign Tasks to appropriate technical agents

  # Step 2: Task Assignment Matrix
  Task_Assignment_Rules:
    "OAuth2 integration": "api-engineer"
    "Multi-factor authentication UI": "frontend-engineer"
    "User session database design": "data-engineer"
    "Authentication security controls": "security-engineer"
    "Session management frontend": "frontend-engineer"
    "Session API endpoints": "api-engineer"
    "Infrastructure deployment": "deployment-engineer"
    "Testing automation": "qa-engineer"

  # Step 3: Task Dependencies Mapping
  Task_Dependencies:
    "Frontend OAuth UI" depends_on: "API OAuth endpoints"
    "Session UI" depends_on: "Session database schema"
    "Security testing" depends_on: "Security controls implementation"
    "Deployment" depends_on: "All implementation tasks completed"
```

### Task Creation TodoWrite Commands

**Concrete TodoWrite usage for software-architect:**

```typescript
// Step 1: Feature Analysis
TodoWrite({
  content: "Technical analysis for Feature: OAuth2 with MFA",
  status: "in_progress",
  activeForm: "Analyzing technical requirements for OAuth2 MFA feature"
});

// Step 2: Create Implementation Task Todos
TodoWrite({
  content: "Task: OAuth2 provider integration (Google/GitHub) - assigned to api-engineer",
  status: "pending",
  activeForm: "Creating OAuth2 integration task for api-engineer"
});

TodoWrite({
  content: "Task: Multi-factor authentication UI components - assigned to frontend-engineer",
  status: "pending",
  activeForm: "Creating MFA UI task for frontend-engineer"
});

TodoWrite({
  content: "Task: User authentication database schema - assigned to data-engineer",
  status: "pending",
  activeForm: "Creating database schema task for data-engineer"
});

// Step 3: Dependency Coordination Todos
TodoWrite({
  content: "Map Task dependencies and execution order",
  status: "pending",
  activeForm: "Mapping technical dependencies between Tasks"
});

// Step 4: Implementation Handoff Todos
TodoWrite({
  content: "Handoff OAuth2 integration Task to api-engineer with specifications",
  status: "pending",
  activeForm: "Preparing Task handoff to api-engineer"
});
```

---

## 🔧 Subtask Level Execution (implementation agents)

### Subtask Auto-Creation Algorithm

```yaml
# CLAUDE.md Configuration Check
if subtask_auto_creation == true and task_owners includes current_agent:

  # Step 1: Task Reception and Analysis
  Subtask_Creation_Process:
    1. Receive Task handoff from software-architect
    2. Analyze Task complexity and requirements
    3. Auto-create detailed Subtasks via TodoWrite
    4. Execute Subtasks with progress tracking

  # Step 2: Agent-Specific Subtask Templates
  Frontend_Engineer_Subtasks:
    Task_Input: "Multi-factor authentication UI components"
    Auto_Generated_Subtasks:
      - "Set up MFA component structure and TypeScript interfaces"
      - "Implement QR code display for authenticator app setup"
      - "Create SMS/Email verification input forms with validation"
      - "Add remember device checkbox with secure token handling"
      - "Implement responsive design for mobile MFA workflow"
      - "Write unit tests for all MFA UI components"
      - "Add accessibility compliance (WCAG 2.1) for MFA forms"

  API_Engineer_Subtasks:
    Task_Input: "OAuth2 provider integration (Google/GitHub)"
    Auto_Generated_Subtasks:
      - "Set up OAuth2 client registration with Google/GitHub"
      - "Implement OAuth2 authorization code flow endpoints"
      - "Create JWT token generation and validation middleware"
      - "Add user profile mapping from OAuth2 providers"
      - "Implement token refresh mechanism with secure storage"
      - "Add rate limiting and security headers for auth endpoints"
      - "Write integration tests for OAuth2 flow with mock providers"

  # Step 3: Progress Tracking Automation
  Subtask_Progress_Tracking:
    - Mark Subtasks as "completed" when implementation finished
    - Auto-update parent Task progress based on Subtask completion
    - Generate progress reports via TodoWrite daily standups
    - Coordinate with qa-engineer for testing validation
```

### Subtask Creation TodoWrite Commands

**Concrete TodoWrite usage for frontend-engineer:**

```typescript
// Step 1: Receive Task Handoff
TodoWrite({
  content: "Task received: Multi-factor authentication UI components",
  status: "in_progress",
  activeForm: "Starting MFA UI components implementation"
});

// Step 2: Auto-Create Detailed Subtasks
TodoWrite({
  content: "Set up MFA component structure with TypeScript interfaces",
  status: "in_progress",
  activeForm: "Setting up MFA component structure"
});

TodoWrite({
  content: "Implement QR code display for authenticator app setup",
  status: "pending",
  activeForm: "Implementing QR code display component"
});

TodoWrite({
  content: "Create SMS/Email verification forms with validation logic",
  status: "pending",
  activeForm: "Creating verification input forms"
});

TodoWrite({
  content: "Add remember device functionality with secure token handling",
  status: "pending",
  activeForm: "Adding remember device feature"
});

// Step 3: Quality and Testing Subtasks
TodoWrite({
  content: "Write comprehensive unit tests for MFA UI components",
  status: "pending",
  activeForm: "Writing unit tests for MFA components"
});

TodoWrite({
  content: "Validate WCAG 2.1 accessibility compliance for MFA forms",
  status: "pending",
  activeForm: "Validating accessibility compliance"
});

// Step 4: Task Completion and Handoff
TodoWrite({
  content: "Complete MFA UI Task and handoff to qa-engineer for testing",
  status: "pending",
  activeForm: "Preparing Task completion and QA handoff"
});
```

---

## 🤝 Agent Coordination Protocols

### Cross-Agent Communication Algorithm

```yaml
# CLAUDE.md Configuration Check
if agent_coordination == true:

  # Step 1: Handoff Protocol Automation
  Agent_Handoff_Rules:
    business-analyst → product-manager: "Epic validated and ready for Feature breakdown"
    product-manager → software-architect: "Features defined with acceptance criteria"
    software-architect → implementation-agents: "Tasks created with technical specifications"
    implementation-agents → qa-engineer: "Implementation completed and ready for testing"
    qa-engineer → deployment-engineer: "Quality validation passed and ready for deployment"

  # Step 2: Coordination TodoWrite Patterns
  Handoff_TodoWrite_Template:
    Sending_Agent_Todo:
      content: "Handoff [work item] to [receiving agent] with [deliverables]"
      status: "completed"
      activeForm: "Completed [work item] handoff to [receiving agent]"

    Receiving_Agent_Todo:
      content: "Received [work item] from [sending agent] - starting [next phase]"
      status: "in_progress"
      activeForm: "Starting [next phase] for [work item]"

  # Step 3: Progress Synchronization
  Progress_Sync_Protocol:
    - Daily: All agents update TodoWrite with current status
    - Weekly: Generate progress summary across all hierarchy levels
    - Milestone: Validate completion criteria before phase transitions
    - Blockers: Auto-escalate to reviewer when dependencies block progress
```

### Coordination TodoWrite Commands

**Example: software-architect handoff to frontend-engineer:**

```typescript
// software-architect completion
TodoWrite({
  content: "Handoff MFA UI Task to frontend-engineer with component specifications",
  status: "completed",
  activeForm: "Completed MFA Task breakdown and handoff to frontend-engineer"
});

// frontend-engineer reception
TodoWrite({
  content: "Received MFA UI Task from software-architect - starting implementation",
  status: "in_progress",
  activeForm: "Starting MFA UI component implementation"
});

// Coordination validation
TodoWrite({
  content: "Validate technical specifications understanding with software-architect",
  status: "pending",
  activeForm: "Validating technical requirements understanding"
});
```

---

## ⚡ Configuration-Driven Automation

### CLAUDE.md Integration Logic

```yaml
# Dynamic Configuration Reading
Configuration_Adaptation:

  # Startup Project Configuration
  if project_scale == "startup":
    Epic_Management: false
    Feature_Breakdown: true
    Task_Granularity: "standard"
    Subtask_Auto_Creation: true
    Agent_Coordination: true
    Progress_Tracking: "session"

  # Enterprise Project Configuration
  if project_scale == "enterprise":
    Epic_Management: true
    Feature_Breakdown: true
    Task_Granularity: "detailed"
    Subtask_Auto_Creation: true
    Subtask_Completion_Tracking: true
    Agent_Coordination: true
    Task_Dependencies: true
    Progress_Tracking: "enterprise"
    Daily_Standups: true
    Weekly_Summaries: true
    External_Tools: "jira"

# Automation Rules Based on Configuration
Automation_Logic:
  if epic_management == false:
    # Skip Epic level, start with Features
    Entry_Point: "product-manager Feature creation"

  if task_granularity == "minimal":
    # Reduce Subtask creation detail
    Subtask_Count: "3-5 per Task"

  if external_tools == "jira":
    # Add external sync todos
    External_Sync: "Sync TODO status with Jira every 24h"
```

---

## 🎯 Success Criteria and Validation

### Hierarchy Completion Validation

```yaml
# Automated Success Validation
Success_Criteria_Check:

  Epic_Success:
    - All Features marked as "completed"
    - Business value metrics achieved
    - Stakeholder acceptance confirmed
    - reviewer approval obtained

  Feature_Success:
    - All Tasks marked as "completed"
    - Acceptance criteria validated
    - User testing completed
    - qa-engineer approval obtained

  Task_Success:
    - All Subtasks marked as "completed"
    - Implementation tested and functional
    - Code review passed
    - Ready for deployment

  Subtask_Success:
    - Specific implementation completed
    - Unit tests passing
    - Code meets quality standards
    - Handoff documentation created
```

### Production Readiness Checklist

```yaml
Production_Readiness:
  Technical_Validation:
    - All implementation Subtasks completed
    - qa-engineer testing validation passed
    - security-engineer security approval obtained
    - deployment-engineer infrastructure ready

  Business_Validation:
    - product-manager feature acceptance confirmed
    - business-analyst business value validated
    - reviewer quality gate approval obtained
    - Stakeholder final approval documented

  Deployment_Readiness:
    - All agent todos marked as "completed"
    - No blocking dependencies remaining
    - rollback plan documented
    - monitoring and alerting configured
```

---

## 🚀 Implementation Quick Start

### For Agents - Immediate Usage

1. **Read CLAUDE.md Section 8** at session start
2. **Apply configuration-driven logic** based on project settings
3. **Use TodoWrite commands** exactly as specified in templates above
4. **Follow handoff protocols** for seamless agent coordination
5. **Track progress** according to configured granularity level

### For Project Teams - Setup

1. **Configure CLAUDE.md Section 8** with desired TODO management settings
2. **Initialize project** using new-project.md or existing-project.md prompts
3. **Start with appropriate entry point** based on project scale and current state
4. **Monitor progress** via TodoWrite reports and agent coordination

**This mapping script transforms the TODO Management system from "configured" to "production-ready automation."**