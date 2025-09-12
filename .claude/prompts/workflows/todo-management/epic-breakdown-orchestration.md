# Epic Breakdown Orchestration

**Workflow Type: Epic to Feature/Task Decomposition**
**Purpose: Systematically break down business epics into actionable development work**

---

## 🎯 Mission

Transform high-level business initiatives into structured development work through systematic decomposition, ensuring complete coverage, proper sizing, and clear ownership.

## 📋 Epic Breakdown Process

### Phase 1: Epic Analysis and Scoping (1-2 days)

**Step 1.1: Business Context Analysis**

```yaml
agent: business-analyst
prompt: epic-business-analysis.md  # To be created
parallel_with: []
inputs:
  - epic_description
  - business_requirements_document
  - stakeholder_interviews
outputs:
  - business_context_analysis
  - user_impact_assessment
  - success_criteria_definition
duration: 4 hours
priority: high
```

**Step 1.2: Product Strategy Alignment**

```yaml
agent: product-manager
prompt: epic-product-strategy-alignment.md  # To be created
parallel_with: [Step 1.3]
depends_on: [Step 1.1]
inputs:
  - business_context_analysis
  - product_roadmap
  - user_research_data
outputs:
  - product_strategy_alignment
  - user_story_themes
  - mvp_scope_recommendations
duration: 3 hours
priority: high
```

**Step 1.3: User Experience Mapping**

```yaml
agent: ux-designer
prompt: epic-user-experience-mapping.md  # To be created
parallel_with: [Step 1.2]
depends_on: [Step 1.1]
inputs:
  - business_context_analysis
  - user_personas
  - current_user_journeys
outputs:
  - user_experience_requirements
  - interaction_design_needs
  - accessibility_requirements
duration: 4 hours
priority: high
```

**Step 1.4: Epic Validation and Approval**

```yaml
agent: reviewer
prompt: epic-validation-and-approval.md  # To be created
parallel_with: []
depends_on: [Step 1.2, Step 1.3]
inputs:
  - business_context_analysis
  - product_strategy_alignment
  - user_experience_requirements
outputs:
  - validated_epic_scope
  - approved_success_criteria
  - stakeholder_sign_off
duration: 2 hours
priority: critical
```

### Phase 2: Technical Architecture Planning (2-3 days)

**Step 2.1: System Architecture Analysis**

```yaml
agent: software-architect
prompt: epic-architecture-planning.md  # To be created
parallel_with: [Step 2.2]
depends_on: [Phase 1 Complete]
inputs:
  - validated_epic_scope
  - current_system_architecture
  - technical_constraints
outputs:
  - architecture_impact_analysis
  - component_modification_plan
  - integration_requirements
duration: 6 hours
priority: high
```

**Step 2.2: Security Architecture Review**

```yaml
agent: security-engineer
prompt: epic-security-planning.md  # To be created
parallel_with: [Step 2.1, Step 2.3]
depends_on: [Phase 1 Complete]
inputs:
  - validated_epic_scope
  - current_security_architecture
  - compliance_requirements
outputs:
  - security_impact_assessment
  - security_requirements_definition
  - threat_modeling_updates
duration: 4 hours
priority: high
```

**Step 2.3: Data Architecture Planning**

```yaml
agent: data-engineer
prompt: epic-data-architecture-planning.md  # To be created
parallel_with: [Step 2.2]
depends_on: [Step 2.1 - Preliminary Results]
inputs:
  - architecture_impact_analysis
  - current_data_models
  - analytics_requirements
outputs:
  - data_architecture_changes
  - database_modification_plan
  - analytics_implementation_plan
duration: 4 hours
priority: high
```

### Phase 3: Feature Decomposition (1-2 days)

**Step 3.1: Feature Identification and Scoping**

```yaml
agent: software-architect
prompt: feature-identification-and-scoping.md  # To be created
parallel_with: []
depends_on: [Phase 2 Complete]
inputs:
  - architecture_impact_analysis
  - user_experience_requirements
  - security_requirements_definition
outputs:
  - feature_list_with_boundaries
  - feature_dependency_map
  - feature_priority_ranking
duration: 4 hours
priority: critical
```

**Step 3.2: Feature Technical Specification**

```yaml
agent: software-architect
prompt: feature-technical-specification.md  # To be created
parallel_with: [Step 3.3]
depends_on: [Step 3.1]
inputs:
  - feature_list_with_boundaries
  - architecture_impact_analysis
  - integration_requirements
outputs:
  - technical_specifications_per_feature
  - api_contracts_definition
  - database_schema_requirements
duration: 6 hours
priority: high
```

**Step 3.3: Feature UX Specification**

```yaml
agent: ux-designer
prompt: feature-ux-specification.md  # To be created
parallel_with: [Step 3.2]
depends_on: [Step 3.1]
inputs:
  - feature_list_with_boundaries
  - user_experience_requirements
  - interaction_design_needs
outputs:
  - ux_specifications_per_feature
  - wireframes_and_mockups
  - user_flow_definitions
duration: 8 hours
priority: high
```

### Phase 4: Task Breakdown and Assignment (1 day)

**Step 4.1: Development Task Creation**

```yaml
agents: [api-engineer, frontend-engineer, data-engineer]
prompt: development-task-breakdown.md  # To be created
parallel_with: [Step 4.2]
depends_on: [Step 3.2, Step 3.3]
inputs:
  - technical_specifications_per_feature
  - ux_specifications_per_feature
  - development_standards
outputs:
  - implementation_task_list
  - task_effort_estimates
  - technical_dependency_mapping
duration: 4 hours
priority: high
```

**Step 4.2: Quality and Security Task Creation**

```yaml
agents: [qa-engineer, security-engineer]
prompt: quality-security-task-breakdown.md  # To be created
parallel_with: [Step 4.1]
depends_on: [Step 3.2, Step 3.3]
inputs:
  - technical_specifications_per_feature
  - security_requirements_definition
  - quality_standards
outputs:
  - testing_task_list
  - security_implementation_tasks
  - quality_gate_definitions
duration: 3 hours
priority: high
```

**Step 4.3: Infrastructure and Deployment Task Creation**

```yaml
agent: deployment-engineer
prompt: infrastructure-deployment-task-breakdown.md  # To be created
parallel_with: []
depends_on: [Step 4.1, Step 4.2]
inputs:
  - implementation_task_list
  - infrastructure_requirements
  - deployment_strategies
outputs:
  - infrastructure_task_list
  - deployment_task_list
  - monitoring_setup_tasks
duration: 2 hours
priority: medium
```

**Step 4.4: Task Assignment and Scheduling**

```yaml
agent: reviewer
prompt: task-assignment-and-scheduling.md  # To be created
parallel_with: []
depends_on: [Step 4.1, Step 4.2, Step 4.3]
inputs:
  - all_task_lists
  - team_capacity_data
  - project_timeline_constraints
outputs:
  - assigned_task_hierarchy
  - development_schedule
  - resource_allocation_plan
duration: 2 hours
priority: critical
```

## 🎯 Detailed Task Breakdown Templates

### Epic → Feature Mapping

```yaml
epic_to_feature_mapping:
  epic: "User Authentication System Overhaul"
  
  features:
    - name: "OAuth2 Implementation"
      scope: "Replace legacy auth with OAuth2"
      owner: api-engineer
      estimated_duration: "2 weeks"
      dependencies: []
      
    - name: "Multi-Factor Authentication"
      scope: "Add MFA support for enhanced security"
      owner: security-engineer
      estimated_duration: "1.5 weeks"
      dependencies: ["OAuth2 Implementation"]
      
    - name: "User Profile Management"
      scope: "Modern user profile interface"
      owner: frontend-engineer
      estimated_duration: "1 week"
      dependencies: ["OAuth2 Implementation"]
      
    - name: "Session Management"
      scope: "Advanced session handling and security"
      owner: api-engineer
      estimated_duration: "1 week"
      dependencies: ["OAuth2 Implementation", "Multi-Factor Authentication"]
      
    - name: "Authentication Analytics"
      scope: "Login analytics and security monitoring"
      owner: data-engineer
      estimated_duration: "0.5 weeks"
      dependencies: ["OAuth2 Implementation"]
```

### Feature → Task Breakdown

```yaml
feature_to_task_breakdown:
  feature: "OAuth2 Implementation"
  
  api_tasks:
    - name: "OAuth2 Authorization Server Setup"
      agent: api-engineer
      estimated_hours: 16
      priority: critical
      dependencies: []
      
    - name: "JWT Token Management"
      agent: api-engineer
      estimated_hours: 12
      priority: high
      dependencies: ["OAuth2 Authorization Server Setup"]
      
    - name: "Client Credential Management"
      agent: api-engineer
      estimated_hours: 8
      priority: high
      dependencies: ["OAuth2 Authorization Server Setup"]
      
    - name: "Token Refresh Mechanism"
      agent: api-engineer
      estimated_hours: 6
      priority: medium
      dependencies: ["JWT Token Management"]
      
  frontend_tasks:
    - name: "OAuth2 Login Flow UI"
      agent: frontend-engineer
      estimated_hours: 12
      priority: high
      dependencies: ["OAuth2 Authorization Server Setup"]
      
    - name: "Token Storage and Management"
      agent: frontend-engineer
      estimated_hours: 8
      priority: high
      dependencies: ["JWT Token Management"]
      
    - name: "Authenticated Route Guards"
      agent: frontend-engineer
      estimated_hours: 6
      priority: medium
      dependencies: ["Token Storage and Management"]
      
  data_tasks:
    - name: "User Authentication Schema"
      agent: data-engineer
      estimated_hours: 4
      priority: high
      dependencies: []
      
    - name: "OAuth2 Token Storage Schema"
      agent: data-engineer
      estimated_hours: 3
      priority: high
      dependencies: ["User Authentication Schema"]
      
  security_tasks:
    - name: "OAuth2 Security Configuration"
      agent: security-engineer
      estimated_hours: 8
      priority: critical
      dependencies: ["OAuth2 Authorization Server Setup"]
      
    - name: "Token Security Validation"
      agent: security-engineer
      estimated_hours: 6
      priority: high
      dependencies: ["JWT Token Management"]
      
  testing_tasks:
    - name: "OAuth2 Integration Tests"
      agent: qa-engineer
      estimated_hours: 12
      priority: high
      dependencies: ["OAuth2 Authorization Server Setup", "OAuth2 Login Flow UI"]
      
    - name: "Security Penetration Testing"
      agent: qa-engineer
      estimated_hours: 8
      priority: high
      dependencies: ["OAuth2 Security Configuration"]
      
  deployment_tasks:
    - name: "OAuth2 Environment Configuration"
      agent: deployment-engineer
      estimated_hours: 4
      priority: medium
      dependencies: ["OAuth2 Authorization Server Setup"]
      
    - name: "Authentication Service Deployment"
      agent: deployment-engineer
      estimated_hours: 6
      priority: high
      dependencies: ["OAuth2 Environment Configuration"]
```

## 📊 Automated Breakdown Rules

### Task Sizing Guidelines

```yaml
task_sizing_rules:
  epic:
    min_duration: "4 weeks"
    max_duration: "12 weeks"
    min_features: 3
    max_features: 8
    
  feature:
    min_duration: "3 days"
    max_duration: "3 weeks"
    min_tasks: 5
    max_tasks: 20
    
  task:
    min_duration: "2 hours"
    max_duration: "3 days"
    max_subtasks: 5
    
  auto_split_triggers:
    epic_too_large: "duration > 12 weeks OR features > 8"
    feature_too_large: "duration > 3 weeks OR tasks > 20"
    task_too_large: "duration > 3 days OR complexity > 8"
```

### Dependency Detection Rules

```yaml
dependency_detection:
  automatic_dependencies:
    database_schema: 
      - blocks: ["api_endpoints", "data_migration"]
      - required_for: "any database operations"
      
    authentication_system:
      - blocks: ["user_management", "protected_endpoints"]
      - required_for: "any user-specific features"
      
    api_contracts:
      - blocks: ["frontend_integration", "third_party_integration"]
      - required_for: "any API consumers"
      
    design_system:
      - blocks: ["ui_components", "styling"]
      - required_for: "consistent UI implementation"
```

## 📈 Success Metrics

### Breakdown Quality Metrics

```yaml
quality_metrics:
  completeness:
    - all_epic_requirements_covered: target = 100%
    - feature_boundary_clarity: target > 90%
    - task_acceptance_criteria_defined: target = 100%
    
  sizing_accuracy:
    - task_estimation_variance: target < 25%
    - feature_completion_predictability: target > 80%
    - epic_timeline_accuracy: target > 75%
    
  dependency_management:
    - dependency_identification_accuracy: target > 95%
    - critical_path_optimization: target > 85%
    - parallel_work_maximization: target > 70%
```

### Team Productivity Impact

```yaml
productivity_metrics:
  development_efficiency:
    - reduced_rework_rate: target < 10%
    - faster_feature_delivery: target +25%
    - improved_story_completion_rate: target > 90%
    
  collaboration_effectiveness:
    - cross_team_dependency_clarity: target > 95%
    - handoff_efficiency: target < 2h delay
    - stakeholder_satisfaction: target > 4.5/5
```

## 📤 Final Deliverables

Upon completion of epic breakdown:

- ✅ **Complete Task Hierarchy** with Epic → Features → Tasks → Subtasks
- ✅ **Agent Assignments** with clear ownership and accountability
- ✅ **Dependency Mapping** with critical path identification
- ✅ **Timeline Estimates** with realistic scheduling and milestones
- ✅ **Quality Gates** with acceptance criteria and definitions of done
- ✅ **Resource Allocation** with team capacity and workload balancing
- ✅ **Progress Tracking** setup with metrics and monitoring dashboards

---

*Systematic epic breakdown ensures comprehensive coverage, proper sizing, and clear execution pathways for complex business initiatives.*