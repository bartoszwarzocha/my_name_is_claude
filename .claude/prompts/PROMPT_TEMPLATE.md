# 📝 Prompt Template - Manual Creation Guide

**Agent: [AGENT_NAME]**
**Purpose: [ONE_LINE_DESCRIPTION_OF_WHAT_THIS_PROMPT_ACCOMPLISHES]**

---

## 1. FUNCTIONAL REQUIREMENTS

Define WHAT needs to be accomplished (not HOW):

- **Primary Objective**: [MAIN_BUSINESS_GOAL_THIS_PROMPT_SERVES]
- **Success Outcomes**: [LIST_OF_MEASURABLE_OUTCOMES]
- **Business Value**: [WHY_THIS_PROMPT_MATTERS_FOR_PROJECT]
- **Scope**: [BOUNDARIES_AND_LIMITATIONS]

Example functional requirements:
- ✅ "Implement user authentication with secure session management"
- ✅ "Analyze code quality and generate improvement recommendations"
- ❌ "Run pytest /specific/path/tests.py" (too specific)
- ❌ "Create React component with useState hook" (technology lock-in)

## 2. HIGH-LEVEL ALGORITHMS

Define the logical steps to achieve the functional requirements:

### Phase 1: [DISCOVERY_AND_ANALYSIS_PHASE_NAME]

1. [READ_PROJECT_CONFIGURATION_STEP]
2. [DETECT_TECHNOLOGY_STACK_STEP]
3. [ANALYZE_EXISTING_CODEBASE_STEP]
4. [IDENTIFY_REQUIREMENTS_STEP]

### Phase 2: [SOLUTION_DESIGN_PHASE_NAME]

1. [DESIGN_APPROACH_STEP]
2. [CREATE_IMPLEMENTATION_STRATEGY_STEP]
3. [VALIDATE_APPROACH_STEP]
4. [PLAN_INTEGRATION_STEP]

### Phase 3: [IMPLEMENTATION_PHASE_NAME]

1. [EXECUTE_SOLUTION_STEP]
2. [VALIDATE_IMPLEMENTATION_STEP]
3. [TEST_INTEGRATION_STEP]
4. [DOCUMENT_RESULTS_STEP]

Each phase should be:
- Technology agnostic (works with any stack)
- Measurable (clear completion criteria)
- Adaptable (customizable to project needs)

## 3. VALIDATION CRITERIA

Define measurable success conditions:

### SUCCESS CRITERIA:

- **Completion Requirements**:
  - [SPECIFIC_DELIVERABLES_CREATED_AND_VALIDATED]
  - [INTEGRATION_WITH_EXISTING_COMPONENTS_SUCCESSFUL]
  - [QUALITY_METRICS_MEET_DEFINED_THRESHOLDS]

- **Quality Gates**:
  - [CODE_FOLLOWS_PROJECT_CONVENTIONS]
  - [ALL_TESTS_PASS_WITH_COVERAGE_PERCENTAGE]
  - [SECURITY_REQUIREMENTS_VALIDATED]
  - [PERFORMANCE_BENCHMARKS_MET]

- **Business Validation**:
  - [BUSINESS_STAKEHOLDER_REQUIREMENTS_SATISFIED]
  - [USER_EXPERIENCE_IMPROVED_OR_MAINTAINED]
  - [TECHNICAL_DEBT_REDUCED_OR_CONTAINED]

Examples of good validation criteria:
- ✅ "All unit tests pass with >90% coverage"
- ✅ "API response time <200ms for 95% of requests"
- ✅ "Security scan shows zero critical vulnerabilities"
- ❌ "Code looks good" (not measurable)
- ❌ "Tests run successfully" (not specific enough)

## 4. USAGE EXAMPLES

Provide concrete examples for different technology stacks and project contexts:

### [SCENARIO_1_NAME] (CLAUDE.md: project_scale="[SCALE]", primary_language="[LANGUAGE]")

```text
1. [DETECTION_STEP_FOR_THIS_SCENARIO]
2. [APPROACH_SELECTION_FOR_THIS_CONTEXT]
3. [IMPLEMENTATION_STRATEGY_FOR_THIS_STACK]
4. [VALIDATION_APPROACH_FOR_THIS_SCALE]
5. [DELIVERABLE_SPECIFIC_TO_THIS_SCENARIO]
```

### [SCENARIO_2_NAME] (CLAUDE.md: project_scale="[SCALE]", business_domain="[DOMAIN]")

```text
1. [DETECTION_STEP_FOR_THIS_SCENARIO]
2. [APPROACH_SELECTION_FOR_THIS_CONTEXT]
3. [IMPLEMENTATION_STRATEGY_FOR_THIS_DOMAIN]
4. [VALIDATION_APPROACH_FOR_THIS_SCALE]
5. [DELIVERABLE_SPECIFIC_TO_THIS_SCENARIO]
```

### [SCENARIO_3_NAME] (existing codebase with [SPECIFIC_CHARACTERISTICS])

```text
1. [DETECTION_STEP_FOR_THIS_SCENARIO]
2. [APPROACH_SELECTION_FOR_THIS_CONTEXT]
3. [IMPLEMENTATION_STRATEGY_FOR_LEGACY]
4. [VALIDATION_APPROACH_FOR_MIGRATION]
5. [DELIVERABLE_SPECIFIC_TO_THIS_SCENARIO]
```

Each example should show:
- How prompt adapts to different contexts
- Technology-specific implementation approaches
- Scale-appropriate solutions
- Real-world project scenarios

---

## 📋 PROMPT CREATION CHECKLIST

### ✅ MANDATORY REQUIREMENTS

- [ ] **Agent Assignment**: Prompt assigned to appropriate specialized agent
- [ ] **Purpose Statement**: Clear one-line description of prompt's business purpose
- [ ] **4-Component Structure**: All sections (Functional Requirements, Algorithms, Validation, Examples) completed
- [ ] **Functional Approach**: Describes WHAT to accomplish, not HOW to implement
- [ ] **Technology Agnostic**: Works across different technology stacks and project scales
- [ ] **CLAUDE.md Integration**: References and adapts to project configuration
- [ ] **Measurable Criteria**: Clear, testable success conditions defined

### ✅ QUALITY VALIDATION

- [ ] **No Hardcoded Paths**: No assumptions about specific file or directory structure
- [ ] **No Technology Lock-in**: No assumptions about specific frameworks without detection
- [ ] **No Production Code**: No complete implementations without customization guidance
- [ ] **Clear Examples**: Usage scenarios show cross-technology adaptability
- [ ] **Business Value**: Clear connection to business outcomes and project goals

### ✅ CODE INCLUSION RULES

IF including code examples, ENSURE:

- [ ] **Proper Labeling**: Marked as TEMPLATE/PATTERN/EXAMPLE/UTILITY/COMMON/USER-REQUESTED
- [ ] **Adaptation Instructions**: Clear guidance on customization for specific projects
- [ ] **Optional Nature**: Prompt functions correctly without the code examples
- [ ] **Genericity**: Code doesn't assume specific project structure (except Common Templates)

## 💡 PROMPT WRITING BEST PRACTICES

### DO

- ✅ Start with business value and outcomes
- ✅ Use algorithmic thinking for step-by-step approaches
- ✅ Provide multiple technology stack examples
- ✅ Include clear success metrics and validation criteria
- ✅ Reference CLAUDE.md configuration for adaptation
- ✅ Focus on what makes the prompt unique and valuable

### DON'T

- ❌ Assume specific technology stack without detection
- ❌ Hardcode file paths or directory structures
- ❌ Provide complete production-ready implementations
- ❌ Use tool-specific commands without fallbacks
- ❌ Create generic prompts that duplicate existing functionality

## 🔄 INTEGRATION WITH FRAMEWORK

Define how this prompt integrates with other framework components:

### Input Dependencies

- [REQUIRES_AGENT_X_TO_COMPLETE_PREREQUISITE_TASK]
- [USES_OUTPUT_FROM_PROMPT_Y_AS_INPUT]
- [DEPENDS_ON_SHARED_RESOURCE_Z]

### Output Handoffs

- [DELIVERS_DELIVERABLE_TO_AGENT_Z_FOR_NEXT_PHASE]
- [UPDATES_SHARED_RESOURCE_FOR_OTHER_AGENTS]
- [PROVIDES_INPUT_FOR_DOWNSTREAM_PROCESSES]

### Shared Resources

- TodoWrite system for task tracking and coordination
- CLAUDE.md configuration for project adaptation
- Session state for context preservation across agents

### Workflow Integration

- **Which agents**: [AGENTS_THAT_SHOULD_USE_THIS_PROMPT]
- **When in lifecycle**: [DEVELOPMENT_STAGE_WHEN_MOST_VALUABLE]
- **Coordination**: [HOW_COORDINATES_WITH_MULTI_AGENT_ORCHESTRATION]

---

**DELIVERABLES:**

- [LIST_SPECIFIC_OUTPUTS_THIS_PROMPT_GENERATES]
- [ARTIFACTS_CREATED_OR_MODIFIED]
- [DOCUMENTATION_OR_REPORTS_PRODUCED]

**COLLABORATION POINTS:**

- **[AGENT_1]**: [DESCRIBE_COLLABORATION_AND_HANDOFF_POINTS]
- **[AGENT_2]**: [DESCRIBE_COLLABORATION_AND_HANDOFF_POINTS]

---

*[ADD_CLOSING_STATEMENT_ABOUT_PROMPT_VALUE_AND_OUTCOMES]*

## 🚀 FINAL VALIDATION

Before submitting your prompt, verify:

1. **Business Alignment**: Does this prompt solve a real business problem?
2. **Framework Compliance**: Does it follow all mandatory rules and structure?
3. **Technology Adaptability**: Will it work across different project types and scales?
4. **Integration Value**: Does it add unique value to the framework ecosystem?
5. **Quality Standards**: Is it clear, complete, and maintainable?

**Remember**: Great prompts enable agents to deliver consistent, high-quality results across diverse projects while maintaining business focus and technical excellence.