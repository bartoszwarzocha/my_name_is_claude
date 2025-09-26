# Claude Code Multi-Agent Framework - Agent Workflow Patterns

## 1. Standard Development Workflow

```mermaid
sequenceDiagram
    participant User
    participant PM as product-manager
    participant BA as business-analyst
    participant SA as software-architect
    participant UX as ux-designer
    participant FE as frontend-engineer
    participant BE as backend-engineer
    participant QA as qa-engineer
    participant SEC as security-engineer
    participant DEPLOY as deployment-engineer

    User->>PM: Project Requirements
    PM->>BA: Analyze Business Needs
    BA->>SA: Technical Requirements
    SA->>UX: Architecture Constraints

    par Frontend Development
        UX->>FE: Design System & Wireframes
        FE->>FE: Implement UI Components
    and Backend Development
        SA->>BE: System Architecture
        BE->>BE: Implement APIs & Services
    end

    FE->>QA: Frontend Testing
    BE->>QA: Backend Testing
    QA->>SEC: Security Review
    SEC->>DEPLOY: Security Approval
    DEPLOY->>User: Production Deployment

    Note over PM,DEPLOY: All agents coordinate via TodoWrite system
```

## 2. Enterprise Project Workflow

```mermaid
sequenceDiagram
    participant User
    participant EA as enterprise-architect
    participant GA as governance-architect
    participant RM as risk-manager
    participant COMP as compliance-auditor
    participant PM as product-manager
    participant SA as software-architect
    participant SRE as sre-engineer
    participant MON as monitoring-engineer
    participant DEPLOY as deployment-engineer

    User->>EA: Enterprise Initiative
    EA->>GA: Governance Review
    GA->>RM: Risk Assessment
    RM->>COMP: Compliance Check
    COMP->>PM: Approved Requirements

    PM->>SA: Technical Planning
    SA->>SRE: Reliability Requirements
    SRE->>MON: Monitoring Strategy

    par Development Phase
        SA->>SA: Development Oversight
    and Operations Preparation
        SRE->>SRE: SLA Definition
        MON->>MON: Observability Setup
    end

    SA->>COMP: Implementation Review
    COMP->>DEPLOY: Compliance Approval
    DEPLOY->>MON: Production Deployment
    MON->>SRE: Operations Handover

    Note over EA,SRE: Enterprise governance at every step
```

## 3. Multi-Agent Coordination Pattern

```mermaid
graph TD
    subgraph "TodoWrite Orchestration Layer"
        TODO[TodoWrite System<br/>Task Coordination]
        EPIC[Epic Level<br/>Strategic Initiatives]
        FEATURE[Feature Level<br/>Development Tasks]
        TASK[Task Level<br/>Implementation]
        SUBTASK[Subtask Level<br/>Detailed Work]
    end

    subgraph "Agent Coordination Patterns"
        subgraph "Parallel Execution"
            A1[Agent 1<br/>Frontend Work]
            A2[Agent 2<br/>Backend Work]
            A3[Agent 3<br/>Database Work]
        end

        subgraph "Sequential Handoffs"
            B1[Agent 1<br/>Requirements]
            B2[Agent 2<br/>Design]
            B3[Agent 3<br/>Implementation]
            B4[Agent 4<br/>Testing]
        end

        subgraph "Collaborative Review"
            C1[Agent 1<br/>Primary Work]
            C2[Agent 2<br/>Review & Feedback]
            C3[Agent 3<br/>Quality Gate]
        end
    end

    subgraph "Coordination Mechanisms"
        HANDOFF[Agent Handoff<br/>State Transfer]
        CONFLICT[Conflict Resolution<br/>Priority Management]
        DEPS[Dependency Tracking<br/>Prerequisite Management]
    end

    TODO --> EPIC
    EPIC --> FEATURE
    FEATURE --> TASK
    TASK --> SUBTASK

    EPIC --> B1
    FEATURE --> A1
    FEATURE --> A2
    FEATURE --> A3
    TASK --> C1

    B1 --> B2
    B2 --> B3
    B3 --> B4

    A1 --> HANDOFF
    A2 --> HANDOFF
    A3 --> HANDOFF

    C1 --> C2
    C2 --> C3

    HANDOFF --> CONFLICT
    CONFLICT --> DEPS

    classDef todoLevel fill:#e3f2fd
    classDef agentWork fill:#e8f5e8
    classDef coordination fill:#fff3e0

    class TODO,EPIC,FEATURE,TASK,SUBTASK todoLevel
    class A1,A2,A3,B1,B2,B3,B4,C1,C2,C3 agentWork
    class HANDOFF,CONFLICT,DEPS coordination
```

## 4. Crisis Response Workflow

```mermaid
sequenceDiagram
    participant ALERT as Monitoring Alert
    participant INC as incident-responder
    participant SRE as sre-engineer
    participant SEC as security-engineer
    participant DEPLOY as deployment-engineer
    participant RM as risk-manager
    participant COMP as compliance-auditor

    ALERT->>INC: Critical Incident Detected
    INC->>SRE: Incident Classification

    alt Security Incident
        SRE->>SEC: Security Investigation
        SEC->>INC: Security Assessment
    else Performance Incident
        SRE->>DEPLOY: Performance Analysis
        DEPLOY->>INC: Infrastructure Status
    end

    INC->>RM: Business Impact Assessment
    RM->>INC: Risk Mitigation Plan

    par Immediate Response
        INC->>SRE: Execute Recovery Plan
        SRE->>DEPLOY: Deploy Fixes
    and Compliance Response
        INC->>COMP: Compliance Notification
        COMP->>COMP: Audit Trail Creation
    end

    DEPLOY->>SRE: Recovery Confirmation
    SRE->>INC: Service Restored
    INC->>COMP: Incident Documentation
    COMP->>RM: Compliance Review

    Note over INC,COMP: Post-incident analysis and learning
```

## 5. Technology Stack Integration Workflow

```mermaid
graph LR
    subgraph "Project Detection"
        DETECT[AI Tools<br/>Technology Detection]
        ANALYZE[Project Analysis<br/>90+ Technologies]
    end

    subgraph "Agent Selection"
        SELECT[ML Agent Selection<br/>97% Confidence]
        RECOMMEND[Agent Recommendations<br/>Optimal Team]
    end

    subgraph "Technology-Specific Agents"
        subgraph "Frontend Stack"
            REACT[React Projects<br/>frontend-engineer]
            ANGULAR[Angular Projects<br/>frontend-engineer]
            VUE[Vue Projects<br/>frontend-engineer]
        end

        subgraph "Backend Stack"
            NODE[Node.js<br/>backend-engineer]
            PYTHON[Python<br/>backend-engineer]
            JAVA[Java<br/>backend-engineer]
        end

        subgraph "Database Stack"
            POSTGRES[PostgreSQL<br/>database-administrator]
            MONGO[MongoDB<br/>database-administrator]
            REDIS[Redis<br/>database-administrator]
        end

        subgraph "Custom Stack"
            GRAPHICS[Graphics<br/>graphics-3d-engineer]
            EMBEDDED[IoT<br/>embedded-engineer]
            DESKTOP[Desktop<br/>desktop-specialist]
        end
    end

    subgraph "Integration Orchestration"
        ORCHESTRATE[Workflow Orchestration<br/>TodoWrite Integration]
        COORDINATE[Agent Coordination<br/>Cross-technology Support]
    end

    DETECT --> ANALYZE
    ANALYZE --> SELECT
    SELECT --> RECOMMEND

    RECOMMEND --> REACT
    RECOMMEND --> ANGULAR
    RECOMMEND --> VUE
    RECOMMEND --> NODE
    RECOMMEND --> PYTHON
    RECOMMEND --> JAVA
    RECOMMEND --> POSTGRES
    RECOMMEND --> MONGO
    RECOMMEND --> REDIS
    RECOMMEND --> GRAPHICS
    RECOMMEND --> EMBEDDED
    RECOMMEND --> DESKTOP

    REACT --> ORCHESTRATE
    NODE --> ORCHESTRATE
    POSTGRES --> ORCHESTRATE
    GRAPHICS --> ORCHESTRATE

    ORCHESTRATE --> COORDINATE

    classDef detection fill:#e3f2fd
    classDef selection fill:#e8f5e8
    classDef technology fill:#fff3e0
    classDef orchestration fill:#f3e5f5

    class DETECT,ANALYZE detection
    class SELECT,RECOMMEND selection
    class REACT,ANGULAR,VUE,NODE,PYTHON,JAVA,POSTGRES,MONGO,REDIS,GRAPHICS,EMBEDDED,DESKTOP technology
    class ORCHESTRATE,COORDINATE orchestration
```

## 6. Quality Gates and Validation Workflow

```mermaid
flowchart TD
    START[Development Task Started] --> ASSIGN[Agent Assignment]

    ASSIGN --> WORK[Agent Execution]
    WORK --> QG1{Quality Gate 1<br/>Code Standards}

    QG1 -->|Pass| QG2{Quality Gate 2<br/>Security Check}
    QG1 -->|Fail| REWORK1[Code Improvement<br/>qa-engineer]
    REWORK1 --> QG1

    QG2 -->|Pass| QG3{Quality Gate 3<br/>Performance Test}
    QG2 -->|Fail| REWORK2[Security Fix<br/>security-engineer]
    REWORK2 --> QG2

    QG3 -->|Pass| QG4{Quality Gate 4<br/>Integration Test}
    QG3 -->|Fail| REWORK3[Performance Fix<br/>performance-engineer]
    REWORK3 --> QG3

    QG4 -->|Pass| DEPLOY[Deployment Ready]
    QG4 -->|Fail| REWORK4[Integration Fix<br/>integration-architect]
    REWORK4 --> QG4

    DEPLOY --> MONITOR[Production Monitoring<br/>monitoring-engineer]
    MONITOR --> FEEDBACK[Feedback Loop<br/>Continuous Improvement]
    FEEDBACK --> START

    classDef qualityGate fill:#ffebee
    classDef rework fill:#fff3e0
    classDef success fill:#e8f5e8

    class QG1,QG2,QG3,QG4 qualityGate
    class REWORK1,REWORK2,REWORK3,REWORK4 rework
    class DEPLOY,MONITOR,FEEDBACK success
```

## Workflow Coordination Principles

### 🎯 TodoWrite Integration
- **Hierarchical Task Management**: Epic → Feature → Task → Subtask
- **Agent Coordination**: Automatic task assignment and handoffs
- **Progress Tracking**: Real-time visibility into workflow status
- **Dependency Management**: Automatic prerequisite tracking

### ⚡ Parallel vs Sequential Execution
- **Parallel Patterns**: Independent development streams (frontend/backend)
- **Sequential Patterns**: Dependent workflow stages (requirements → design → implementation)
- **Hybrid Patterns**: Mixed parallel and sequential execution
- **Load Balancing**: Optimal agent utilization and resource management

### 🔄 Agent Handoff Protocols
1. **State Transfer**: Complete context and work product handoff
2. **Validation Checkpoints**: Quality gates between agent transitions
3. **Rollback Mechanisms**: Ability to return to previous states
4. **Conflict Resolution**: Automated resolution of agent conflicts

### 📊 Workflow Optimization
- **Performance Metrics**: Workflow execution time and efficiency
- **Bottleneck Detection**: Identification of workflow constraints
- **Resource Optimization**: Agent utilization and capacity planning
- **Continuous Improvement**: Workflow pattern learning and optimization

### 🛡️ Enterprise Workflow Features
- **Governance Integration**: Enterprise approval and oversight workflows
- **Compliance Automation**: Regulatory requirement integration
- **Audit Trails**: Complete workflow documentation and traceability
- **Risk Management**: Risk assessment and mitigation throughout workflows

## Workflow Patterns by Project Scale

### Startup Scale (Core Agents)
- **Simple Linear Workflow**: product-manager → software-architect → development → deployment
- **Minimal Governance**: Essential quality gates only
- **Rapid Iteration**: Fast feedback loops and quick pivots

### SME Scale (Core + Selected Enterprise)
- **Enhanced Governance**: Additional compliance and risk management
- **Specialized Operations**: SRE and monitoring integration
- **Quality Focus**: Enhanced testing and security workflows

### Enterprise Scale (Full Ecosystem)
- **Complete Governance**: Full enterprise architecture and compliance
- **Advanced Operations**: Complete SRE, monitoring, and incident response
- **Custom Specializations**: Technology-specific expert agents
- **Global Coordination**: Multi-team and multi-project coordination