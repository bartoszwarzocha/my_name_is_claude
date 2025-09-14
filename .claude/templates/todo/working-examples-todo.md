# Working Examples - Hierarchical TODO Creation in Action

**Purpose: Real-world, copy-paste examples demonstrating hierarchical TODO creation from Epic to Subtask with concrete TodoWrite commands**

---

## 🎯 Complete Example: User Authentication System

### Real Project Context
```yaml
Project: "Enterprise SaaS Application"
Scale: enterprise
Technology: Angular + .NET Core + PostgreSQL
Timeline: 8-12 weeks
Team: 6 agents (business-analyst, product-manager, software-architect, frontend-engineer, api-engineer, security-engineer)
```

---

## 📋 Epic Level - business-analyst

### Epic Creation Process

**Step 1: Epic Analysis and Creation**

```typescript
// business-analyst creates Epic via TodoWrite
TodoWrite({
  content: "Epic: Complete user authentication system with GDPR compliance",
  status: "in_progress",
  activeForm: "Analyzing business requirements for authentication system Epic"
});

// Stakeholder coordination
TodoWrite({
  content: "Coordinate authentication requirements with legal and compliance teams",
  status: "pending",
  activeForm: "Coordinating with stakeholders for authentication requirements"
});

// Business value validation
TodoWrite({
  content: "Validate Epic business value: secure login + GDPR compliance + 99.9% availability",
  status: "pending",
  activeForm: "Validating Epic business value and success criteria"
});
```

**Step 2: Epic Validation and Handoff**

```typescript
// Validation with reviewer
TodoWrite({
  content: "Epic validation with reviewer: business objectives alignment check",
  status: "pending",
  activeForm: "Validating Epic with reviewer for business alignment"
});

// Handoff to product-manager
TodoWrite({
  content: "Handoff validated Epic to product-manager for Feature breakdown",
  status: "pending",
  activeForm: "Preparing Epic handoff to product-manager with business requirements"
});

// Mark Epic analysis complete
TodoWrite({
  content: "Epic: Complete user authentication system with GDPR compliance",
  status: "completed",
  activeForm: "Completed Epic business analysis and validation"
});
```

---

## 🏗️ Feature Level - product-manager

### Feature Breakdown Process

**Step 1: Receive Epic and Create Features**

```typescript
// Receive Epic handoff from business-analyst
TodoWrite({
  content: "Feature breakdown for Epic: User authentication system",
  status: "in_progress",
  activeForm: "Breaking Epic into user-facing Features"
});

// Create individual Feature todos
TodoWrite({
  content: "Feature: OAuth2 with multi-factor authentication for secure user login",
  status: "pending",
  activeForm: "Defining OAuth2 MFA feature with user stories and acceptance criteria"
});

TodoWrite({
  content: "Feature: User session management dashboard for active session control",
  status: "pending",
  activeForm: "Defining session management feature with user control requirements"
});

TodoWrite({
  content: "Feature: GDPR-compliant user data management and consent system",
  status: "pending",
  activeForm: "Defining GDPR compliance feature with data privacy requirements"
});
```

**Step 2: Feature Coordination and Technical Validation**

```typescript
// Coordinate with UX designer
TodoWrite({
  content: "Validate authentication Features UX requirements with ux-designer",
  status: "pending",
  activeForm: "Coordinating authentication user experience requirements"
});

// Technical feasibility with software-architect
TodoWrite({
  content: "Validate Features technical feasibility with software-architect",
  status: "pending",
  activeForm: "Coordinating technical feasibility validation for authentication Features"
});

// Security review coordination
TodoWrite({
  content: "Coordinate security requirements for authentication Features with security-engineer",
  status: "pending",
  activeForm: "Coordinating security requirements for authentication system"
});
```

**Step 3: Feature Handoff to Technical Architecture**

```typescript
// Handoff to software-architect
TodoWrite({
  content: "Handoff validated Features to software-architect for technical Task creation",
  status: "pending",
  activeForm: "Preparing Feature handoff with acceptance criteria and technical requirements"
});

// Complete Feature breakdown
TodoWrite({
  content: "Feature breakdown for Epic: User authentication system",
  status: "completed",
  activeForm: "Completed Feature breakdown with 3 Features ready for technical implementation"
});
```

---

## ⚙️ Task Level - software-architect

### Technical Task Creation Process

**Step 1: Receive Features and Analyze Technical Requirements**

```typescript
// Receive Feature handoff
TodoWrite({
  content: "Technical analysis for Feature: OAuth2 with multi-factor authentication",
  status: "in_progress",
  activeForm: "Analyzing technical architecture requirements for OAuth2 MFA Feature"
});

// Architecture design
TodoWrite({
  content: "Design OAuth2 authentication architecture with MFA integration points",
  status: "pending",
  activeForm: "Designing technical architecture for OAuth2 MFA system"
});
```

**Step 2: Create Implementation Tasks with Agent Assignments**

```typescript
// Backend API Tasks
TodoWrite({
  content: "Task: OAuth2 provider integration (Google/GitHub/Microsoft) - assigned to api-engineer",
  status: "pending",
  activeForm: "Creating OAuth2 integration task with provider specifications for api-engineer"
});

TodoWrite({
  content: "Task: JWT token generation and validation middleware - assigned to api-engineer",
  status: "pending",
  activeForm: "Creating JWT middleware task with security specifications for api-engineer"
});

// Frontend UI Tasks
TodoWrite({
  content: "Task: Multi-factor authentication UI components with QR codes - assigned to frontend-engineer",
  status: "pending",
  activeForm: "Creating MFA UI task with component specifications for frontend-engineer"
});

TodoWrite({
  content: "Task: OAuth2 login flow UI with provider selection - assigned to frontend-engineer",
  status: "pending",
  activeForm: "Creating OAuth2 UI task with user flow specifications for frontend-engineer"
});

// Security Tasks
TodoWrite({
  content: "Task: OAuth2 security controls and threat mitigation - assigned to security-engineer",
  status: "pending",
  activeForm: "Creating security controls task with threat analysis for security-engineer"
});
```

**Step 3: Task Dependencies and Coordination**

```typescript
// Dependencies mapping
TodoWrite({
  content: "Map technical dependencies: OAuth2 API → JWT middleware → Frontend UI → Security validation",
  status: "pending",
  activeForm: "Mapping technical dependencies and execution order for authentication tasks"
});

// Handoff coordination
TodoWrite({
  content: "Coordinate Task handoffs to implementation agents with technical specifications",
  status: "pending",
  activeForm: "Preparing Task handoffs with detailed technical requirements"
});

// Complete Task breakdown
TodoWrite({
  content: "Technical analysis for Feature: OAuth2 with multi-factor authentication",
  status: "completed",
  activeForm: "Completed technical Task breakdown with 5 implementation tasks"
});
```

---

## 🔧 Subtask Level - Implementation Agents

### frontend-engineer: MFA UI Implementation

**Step 1: Receive Task and Auto-Create Subtasks**

```typescript
// Receive Task from software-architect
TodoWrite({
  content: "Task received: Multi-factor authentication UI components with QR codes",
  status: "in_progress",
  activeForm: "Starting MFA UI components implementation with QR code integration"
});

// Auto-create detailed Subtasks
TodoWrite({
  content: "Set up MFA component structure with TypeScript interfaces and props",
  status: "in_progress",
  activeForm: "Setting up MFA component structure and TypeScript definitions"
});

TodoWrite({
  content: "Implement QR code display component for authenticator app setup",
  status: "pending",
  activeForm: "Implementing QR code display component with authenticator integration"
});

TodoWrite({
  content: "Create SMS/Email verification input forms with real-time validation",
  status: "pending",
  activeForm: "Creating verification input forms with validation logic"
});

TodoWrite({
  content: "Add remember device checkbox with secure token handling",
  status: "pending",
  activeForm: "Adding remember device functionality with secure token storage"
});

TodoWrite({
  content: "Implement responsive design for mobile MFA workflow",
  status: "pending",
  activeForm: "Implementing responsive MFA design for mobile devices"
});
```

**Step 2: Quality and Testing Subtasks**

```typescript
// Testing Subtasks
TodoWrite({
  content: "Write unit tests for MFA UI components with Jest and Angular Testing Library",
  status: "pending",
  activeForm: "Writing comprehensive unit tests for MFA components"
});

TodoWrite({
  content: "Validate WCAG 2.1 accessibility compliance for MFA forms and QR codes",
  status: "pending",
  activeForm: "Validating accessibility compliance for MFA user interface"
});

// Integration Subtasks
TodoWrite({
  content: "Integrate MFA UI with OAuth2 API endpoints from api-engineer",
  status: "pending",
  activeForm: "Integrating MFA UI components with backend OAuth2 APIs"
});
```

**Step 3: Task Completion and Handoff**

```typescript
// Complete individual Subtasks
TodoWrite({
  content: "Set up MFA component structure with TypeScript interfaces and props",
  status: "completed",
  activeForm: "Completed MFA component structure setup"
});

// ... (mark each Subtask as completed when done)

// Complete main Task and handoff to QA
TodoWrite({
  content: "Complete MFA UI Task and handoff to qa-engineer for testing validation",
  status: "pending",
  activeForm: "Preparing MFA UI Task completion and QA handoff"
});

TodoWrite({
  content: "Task received: Multi-factor authentication UI components with QR codes",
  status: "completed",
  activeForm: "Completed MFA UI implementation with all components functional and tested"
});
```

### api-engineer: OAuth2 Backend Implementation

**Step 1: OAuth2 Integration Task Breakdown**

```typescript
// Receive Task from software-architect
TodoWrite({
  content: "Task received: OAuth2 provider integration (Google/GitHub/Microsoft)",
  status: "in_progress",
  activeForm: "Starting OAuth2 provider integration implementation"
});

// Auto-create OAuth2 Subtasks
TodoWrite({
  content: "Set up OAuth2 client registration with Google, GitHub, and Microsoft providers",
  status: "in_progress",
  activeForm: "Setting up OAuth2 client registrations with provider credentials"
});

TodoWrite({
  content: "Implement OAuth2 authorization code flow endpoints with PKCE",
  status: "pending",
  activeForm: "Implementing OAuth2 authorization code flow with PKCE security"
});

TodoWrite({
  content: "Create user profile mapping from OAuth2 provider responses",
  status: "pending",
  activeForm: "Creating user profile mapping logic for OAuth2 providers"
});

TodoWrite({
  content: "Implement token refresh mechanism with secure storage",
  status: "pending",
  activeForm: "Implementing OAuth2 token refresh with secure storage backend"
});

TodoWrite({
  content: "Add rate limiting and security headers for OAuth2 endpoints",
  status: "pending",
  activeForm: "Adding security controls and rate limiting for OAuth2 APIs"
});
```

**Step 2: Integration and Testing Subtasks**

```typescript
// Testing and Integration
TodoWrite({
  content: "Write integration tests for OAuth2 flow with mock provider responses",
  status: "pending",
  activeForm: "Writing integration tests for OAuth2 authentication flow"
});

TodoWrite({
  content: "Coordinate OAuth2 API contracts with frontend-engineer for UI integration",
  status: "pending",
  activeForm: "Coordinating OAuth2 API specifications with frontend team"
});

TodoWrite({
  content: "Validate OAuth2 security controls with security-engineer review",
  status: "pending",
  activeForm: "Coordinating OAuth2 security validation with security team"
});
```

---

## 🤝 Cross-Agent Coordination Examples

### Real-Time Handoff Scenarios

**Scenario 1: software-architect → frontend-engineer handoff**

```typescript
// software-architect completion
TodoWrite({
  content: "Handoff MFA UI Task to frontend-engineer with component specifications",
  status: "completed",
  activeForm: "Completed MFA Task specification and handoff to frontend-engineer"
});

// frontend-engineer reception (immediate response)
TodoWrite({
  content: "Received MFA UI Task from software-architect - starting implementation",
  status: "in_progress",
  activeForm: "Starting MFA UI component implementation with provided specifications"
});

// Coordination validation
TodoWrite({
  content: "Validate MFA technical requirements understanding with software-architect",
  status: "pending",
  activeForm: "Validating technical specifications understanding for MFA implementation"
});
```

**Scenario 2: frontend-engineer → qa-engineer handoff**

```typescript
// frontend-engineer completion
TodoWrite({
  content: "MFA UI implementation completed - handoff to qa-engineer for validation",
  status: "completed",
  activeForm: "Completed MFA UI development - ready for quality assurance testing"
});

// qa-engineer reception
TodoWrite({
  content: "Received MFA UI implementation from frontend-engineer - starting testing validation",
  status: "in_progress",
  activeForm: "Starting comprehensive testing validation for MFA UI components"
});

// QA test planning
TodoWrite({
  content: "Create MFA UI test plan: functional testing, accessibility validation, security testing",
  status: "pending",
  activeForm: "Creating comprehensive test plan for MFA UI validation"
});
```

---

## 📊 Progress Tracking Examples

### Daily Standup TodoWrite Patterns

**Daily Progress Updates (when daily_standups: true)**

```typescript
// business-analyst daily update
TodoWrite({
  content: "Daily standup: Epic requirements validated, Feature handoff completed",
  status: "completed",
  activeForm: "Reported daily progress: Epic analysis complete, Features handed off"
});

// product-manager daily update
TodoWrite({
  content: "Daily standup: 3 Features defined, technical coordination in progress",
  status: "completed",
  activeForm: "Reported daily progress: Features breakdown 100%, technical validation 60%"
});

// frontend-engineer daily update
TodoWrite({
  content: "Daily standup: MFA UI 70% complete, QR code component functional, responsive design pending",
  status: "completed",
  activeForm: "Reported daily progress: MFA implementation 70%, 3 of 5 Subtasks completed"
});
```

### Milestone Tracking (when milestone_tracking: true)

```typescript
// Milestone: Feature Definition Complete
TodoWrite({
  content: "Milestone reached: All Features defined with acceptance criteria",
  status: "completed",
  activeForm: "Achieved milestone: Feature definition phase completed successfully"
});

// Milestone: Technical Architecture Complete
TodoWrite({
  content: "Milestone reached: Technical Tasks created and assigned to implementation agents",
  status: "completed",
  activeForm: "Achieved milestone: Technical architecture and task breakdown completed"
});

// Milestone: Implementation 50% Complete
TodoWrite({
  content: "Milestone reached: Authentication implementation 50% complete across all agents",
  status: "completed",
  activeForm: "Achieved milestone: Half of implementation tasks completed successfully"
});
```

---

## 🎯 Complete Example Output Timeline

### Week 1: Epic → Feature (Strategic Level)
```
Day 1: business-analyst creates Epic, coordinates stakeholders
Day 2: business-analyst validates Epic, hands off to product-manager
Day 3: product-manager breaks Epic into 3 Features
Day 4: product-manager coordinates with ux-designer and software-architect
Day 5: Features validated and handed off to software-architect
```

### Week 2: Feature → Task (Tactical Level)
```
Day 1: software-architect analyzes Features, designs architecture
Day 2-3: software-architect creates 15 Tasks across 5 implementation agents
Day 4: Dependencies mapped, Task specifications finalized
Day 5: Tasks handed off to implementation agents
```

### Weeks 3-6: Task → Subtask (Implementation Level)
```
Week 3: Implementation agents create 60+ Subtasks via TodoWrite
Week 4-5: Active development with daily TodoWrite progress updates
Week 6: Implementation completion, handoffs to qa-engineer
```

### Weeks 7-8: Quality & Deployment
```
Week 7: qa-engineer testing validation, security-engineer audit
Week 8: deployment-engineer production deployment, Epic completion
```

---

## 🚀 Copy-Paste Quick Start

### For New Projects - Immediate Usage

1. **Configure CLAUDE.md Section 8:**
```yaml
todo_management_enabled: true
todo_hierarchy_level: hierarchical
auto_task_creation: true
epic_management: true
feature_breakdown: true
agent_coordination: true
session_todos: true
```

2. **Start with Epic (business-analyst):**
```typescript
TodoWrite({
  content: "Epic: [Your business initiative]",
  status: "in_progress",
  activeForm: "Analyzing business requirements for [initiative] Epic"
});
```

3. **Follow the patterns above** for your specific project context

4. **Use agent coordination hooks** for automated handoffs

**These examples provide concrete, production-ready TodoWrite commands that agents can use immediately to create working hierarchical TODO systems.**