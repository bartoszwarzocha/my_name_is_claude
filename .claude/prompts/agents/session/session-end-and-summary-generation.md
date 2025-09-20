**🤖 AGENT ACTIVATION:** This prompt automatically activates the `session-manager` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# Session Documentation and Continuity Preparation

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Generate comprehensive session summary documenting accomplishments, insights, and project state for optimal future session continuity. Capture completed work, pending tasks, lessons learned, and strategic decisions to enable seamless work resumption and preserve institutional knowledge. Create actionable documentation that facilitates productive future sessions and maintains development momentum.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Accomplishment Documentation and Knowledge Preservation
**Objective**: Analyze session outcomes and implement comprehensive knowledge preservation and state assessment

1. **Accomplishment Documentation and Analysis**
   - Catalog completed deliverables documenting finished tasks, features, and fixes with quality assessments
   - Measure progress against objectives evaluating session goals achievement and business value delivery
   - Assess quality outcomes, document technical decisions, and capture performance metrics

2. **Knowledge Preservation and State Assessment**
   - Extract lessons learned identifying discoveries, problem-solving approaches, and effective solution patterns
   - Document blockers and resolutions, preserve critical context, and identify best practices
   - Analyze project health indicators, identify immediate next steps, and evaluate pending dependencies

### Phase 2: Continuity Documentation and Integration
**Objective**: Execute comprehensive state persistence and establish MCP tools integration

1. **Continuity Documentation and State Persistence**
   - Generate comprehensive session summary creating structured documentation covering all session aspects
   - Write session state to persistent storage saving summary to SESSION_STATE.md for cross-session continuity
   - Update project documentation, persist TODO status, and create continuation context file

2. **MCP Tools Integration (If Available)**
   - Detect Serena MCP availability checking for .serena directory existence and tool accessibility
   - Synchronize project state with Serena updating project index with session changes
   - Trigger comprehensive reindexing, validate integration, and update project configuration

## 3. ✅ VALIDATION CRITERIA

### Accomplishment Documentation and Knowledge Preservation
**Documentation Completeness Excellence**: All deliverables catalogued with completed tasks and quality assessments documented, progress accurately measured with session objectives evaluation completed, quality outcomes documented with testing results and validation status recorded, technical decisions preserved with architecture choices and design rationale captured

**Knowledge Preservation Excellence**: Lessons learned extracted with discoveries and effective solution patterns identified, blocker resolutions documented with obstacles and mitigation strategies recorded, critical context preserved with business insights and decision-making context captured, best practices identified with effective workflows documented, strategic insights recorded with architecture evolution learnings preserved

### Continuity Documentation and Integration
**State Persistence Excellence**: Session state successfully persisted with summary saved to SESSION_STATE.md, TODO status preserved with current priorities written to SESSION_TODOS.md, continuation context documented with handoff information saved, dependencies and blockers mapped with external requirements documented, cross-session continuity enabled with necessary information stored

**MCP Integration Excellence**: Serena MCP detection successful with proper identification of directory and tool accessibility, project index synchronized with session changes updated, reindexing completed with comprehensive refresh of navigation capabilities, integration validated with project knowledge properly indexed, configuration updated with structure changes reflected

## 4. 📚 USAGE EXAMPLES

**Feature Development Session**: User authentication API completed, frontend integration 80% done, OAuth complexity insights, next steps include frontend completion and password reset implementation

**Bug Investigation Session**: Critical payment bug fixed, root cause race condition identified, next steps include transaction monitoring implementation and similar pattern review

**Architecture Planning Session**: Microservices decomposition strategy designed, API contracts defined, data consistency challenges identified, stakeholder validation needed for contracts

**Code Quality Improvement Session**: Technical debt audit completed, refactoring plan created, test coverage gaps identified, next steps include remaining module refactoring and quality gates

**Security Assessment Session**: Vulnerability scan completed, 3 critical issues fixed, infrastructure hardening effective, next steps include moderate issue resolution and security monitoring

---

## 🎯 EXECUTION APPROACH

**Session Documentation Excellence**: Comprehensive accomplishment review → insight extraction and knowledge capture → intentional state persistence → future planning and continuity preparation

**Quality Assurance for Session Summaries**: Completeness verification ensuring all significant work and insights are captured, accuracy validation confirming technical details and progress assessments, actionability assessment verifying next steps are specific, context sufficiency ensuring adequate information for productive continuation

**Adaptive Documentation Strategies**: Quick sessions focusing on immediate accomplishments and next steps, complex sessions emphasizing technical decisions and architectural context, problem-solving sessions highlighting discovered issues and resolution approaches, planning sessions documenting decisions and strategic direction with stakeholder context