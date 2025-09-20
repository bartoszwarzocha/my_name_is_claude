# [Prompt Title]: [Brief Description of Purpose]

**Agent Auto-Activation**: This prompt automatically activates the corresponding agent based on its directory location in `.claude/prompts/agents/[category]/`

**Context Adaptation**: This prompt automatically adapts to project requirements defined in `CLAUDE.md` and integrates with TodoWrite workflow system for task management.

**TODO Integration**: When used, this prompt seamlessly integrates with the TodoWrite system for structured task execution and progress tracking.

---

## 1. FUNCTIONAL REQUIREMENTS

### What This Prompt Accomplishes

**Primary Objective**: [Clear statement of what this prompt achieves]

**Key Outcomes**:
- [Primary Deliverable]: [Main business result or technical output]
- [Secondary Deliverable]: [Supporting outcome or integration result]
- [Quality Outcome]: [Performance, security, or maintainability achievement]

**Success Criteria**:
- [Business Success Metric]: [Measurable business value indicator]
- [Technical Success Metric]: [Performance or quality benchmark]
- [Integration Success Metric]: [Compatibility and adoption measure]

**Scope and Boundaries**:
- **Included**: [What this prompt covers]
- **Excluded**: [What this prompt does not handle]
- **Dependencies**: [Required inputs or prerequisites]

---

## 2. HIGH-LEVEL ALGORITHMS

### Approach Strategy

**Primary Algorithm**: [High-level description of the main approach]

**Processing Steps**:
1. **[Analysis Phase]**: [Project context analysis and requirement identification]
2. **[Design Phase]**: [Solution architecture and implementation strategy]
3. **[Implementation Phase]**: [Technology-adaptive development and integration]
4. **[Validation Phase]**: [Quality assurance and deployment readiness]

**Decision Logic**: `IF [technology constraint] THEN [adaptive approach] ELSE [standard implementation]`

**Optimization Strategies**:
- [Performance Optimization]: [Speed, efficiency, and scalability improvements]
- [Quality Enhancement]: [Code quality, security, and maintainability]
- [Integration Optimization]: [Compatibility and workflow efficiency]

**Error Handling**:
- [Technical Errors]: [System failures, configuration issues, and recovery procedures]
- [Business Logic Errors]: [Validation failures and user guidance]
- [Fallback Strategy]: [Alternative approaches when primary solution fails]

---

## 3. VALIDATION CRITERIA

### Quality Gates

**Functional Validation**:
- [ ] [Primary Function Test]: [Verify core functionality meets requirements]
- [ ] [Integration Test]: [Confirm seamless integration with existing systems]
- [ ] [Performance Validation]: [Ensure performance benchmarks are achieved]

**Technical Validation**:
- [ ] [Code Quality Check]: [Verify technical implementation standards]
- [ ] [Security Assessment]: [Confirm security requirements are met]
- [ ] [Compatibility Verification]: [Ensure cross-platform and technology compatibility]

**Business Validation**:
- [ ] [Business Value Delivery]: [Verify business objectives are achieved]
- [ ] [User Acceptance]: [Confirm usability and user satisfaction]
- [ ] [Stakeholder Approval]: [Ensure stakeholder requirements are satisfied]

**Integration Validation**:
- [ ] **CLAUDE.md Adaptation**: Prompt automatically adapts to project requirements
- [ ] **TodoWrite Integration**: Seamless task management integration
- [ ] **Agent Coordination**: Proper agent activation and coordination
- [ ] **Framework Compliance**: Follows all framework quality standards

### Acceptance Criteria

**Core Requirements**: [Critical business and technical requirements that must be met]
**Enhanced Features**: [Important capabilities that add significant value]
**Future Enhancements**: [Nice-to-have features for future iterations]

---

## 4. USAGE EXAMPLES

### Cross-Technology Scenarios

#### Example 1: [Modern Web Stack] Implementation

**Context**: [React/Angular + Node.js/Python backend with database integration]

**Input**: [Project configuration and requirements]
**Expected Process**: [Analysis → Design → Implementation → Validation]
**Expected Output**: [Technology-adaptive solution with documentation]

#### Example 2: [Enterprise/Legacy] Integration

**Context**: [Enterprise environment with legacy system constraints]

**Input**: [Business requirements and technical constraints]
**Expected Process**: [Legacy analysis → Integration design → Incremental implementation]
**Expected Output**: [Compatible solution with migration strategy]

### Edge Cases and Error Scenarios

#### Technology Constraints
**Situation**: [Incompatible technology stack or missing dependencies]
**Expected Handling**: [Alternative implementation approach or compatibility layer]
**Fallback Strategy**: [Manual process or simplified solution when automation fails]

#### Resource Limitations
**Situation**: [Insufficient resources, time constraints, or technical limitations]
**Expected Handling**: [Scaled-down solution or phased implementation approach]
**Recovery Process**: [Progressive enhancement and future iteration planning]

### Integration Example

**Project Configuration**: `technologies: "React + Node.js"`, `business_domain: "E-commerce"`

**TodoWrite Workflow**:
```yaml
todos:
  - content: "[Analyze e-commerce requirements and React/Node.js architecture]"
    status: "pending"
  - content: "[Implement technology-adaptive solution for e-commerce domain]"
    status: "pending"
```

**Adaptation Result**: [Prompt automatically adapts to e-commerce + React/Node.js context]

---

## TEMPLATE USAGE INSTRUCTIONS

**Compact template enforcing Claude Code Framework quality standards:**

### Required Structure (4 Components):
1. **Functional Requirements** - Clear WHAT statement with measurable outcomes
2. **High-Level Algorithms** - HOW approach with technology-adaptive steps
3. **Validation Criteria** - Quality gates and acceptance criteria
4. **Usage Examples** - Cross-technology scenarios with integration examples

### Quality Standards:

#### Essential Compliance Requirements:
- [ ] **4 Required Sections**: Functional Requirements, Algorithms, Validation, Examples
- [ ] **Framework Integration**: Agent auto-activation, CLAUDE.md adaptation, TodoWrite integration
- [ ] **Technology Agnostic Design**: No hardcoding violations, works across stacks and scales
- [ ] **Enterprise Quality**: Professional standards with clear, measurable outcomes
- [ ] **Adaptability**: Cross-technology examples with robust error handling

### Customization Process:
1. Replace all `[bracketed placeholders]` with role-specific content
2. Ensure all 4 required sections are complete and technology-agnostic
3. Validate CLAUDE.md adaptation and TodoWrite integration
4. Verify no hardcoding violations or technology lock-in exists

### Final Validation:
- [ ] **Complete Structure**: All 4 sections present with enterprise-grade content
- [ ] **Technology Agnostic**: Adapts to any stack without hardcoding violations
- [ ] **Framework Integration**: CLAUDE.md adaptation and TodoWrite workflows functional
- [ ] **Quality Standards**: Professional guidance with measurable outcomes and examples

**Result**: Compact, enterprise-grade prompt meeting framework quality standards.