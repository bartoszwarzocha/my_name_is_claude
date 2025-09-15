**🤖 AGENT ACTIVATION:** This prompt automatically activates the `session-manager` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# Session Documentation and Continuity Preparation

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Generate comprehensive session summary documenting accomplishments, insights, and project state for optimal future session continuity. Capture completed work, pending tasks, lessons learned, and strategic decisions to enable seamless work resumption and preserve institutional knowledge. Create actionable documentation that facilitates productive future sessions and maintains development momentum.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Accomplishment Documentation and Analysis
1. **Catalog completed deliverables** - Document finished tasks, features, fixes, and other work items with quality assessments
2. **Measure progress against objectives** - Evaluate session goals achievement and business value delivery
3. **Assess quality outcomes** - Review testing results, code review outcomes, and validation completeness
4. **Document technical decisions** - Record architecture choices, technology selections, and design rationale
5. **Capture performance metrics** - Note development velocity, efficiency improvements, and resource utilization

### Phase 2: Knowledge Preservation and Insight Extraction
1. **Extract lessons learned** - Identify discoveries, problem-solving approaches, and effective solution patterns
2. **Document blockers and resolutions** - Record encountered obstacles and successful mitigation strategies
3. **Preserve critical context** - Capture business insights, stakeholder feedback, and decision-making context
4. **Identify best practices** - Note effective workflows, tool usage, and collaboration patterns discovered
5. **Record strategic insights** - Document architecture evolution, technology insights, and business alignment learnings

### Phase 3: Current State Assessment and Future Planning
1. **Analyze project health indicators** - Assess build status, test coverage, code quality, and technical debt
2. **Identify immediate next steps** - Determine most logical continuation points and quick win opportunities
3. **Evaluate pending dependencies** - Document blockers, external requirements, and resource needs
4. **Assess timeline and priority impacts** - Consider how session progress affects milestones and business goals
5. **Plan resource requirements** - Identify skills, tools, and access needed for future work continuation

### Phase 4: Continuity Documentation and State Persistence
1. **Generate comprehensive session summary** - Create structured documentation covering all session aspects
2. **Write session state to persistent storage** - Save summary to SESSION_STATE.md file for cross-session continuity
3. **Update project documentation** - Sync relevant discoveries and decisions with project knowledge base
4. **Persist current TODO status** - Write current task status to SESSION_TODOS.md for continuation tracking
5. **Create continuation context file** - Generate structured handoff information in CONTINUATION_CONTEXT.md

### Phase 5: MCP Tools Integration (If Available)
1. **Detect Serena MCP availability** - Check for .serena directory existence and tool accessibility
2. **Synchronize project state with Serena** - Update Serena's project index with session changes and new files
3. **Trigger comprehensive reindexing** - Refresh Serena's code navigation and search capabilities
4. **Validate Serena integration** - Ensure project knowledge is properly indexed and searchable
5. **Update Serena project configuration** - Sync any project structure or workflow changes with Serena settings

## 3. ✅ VALIDATION CRITERIA

### Accomplishment Documentation Completeness
- **All deliverables catalogued**: Completed tasks, features, fixes, and work items documented with quality assessments
- **Progress accurately measured**: Session objectives evaluation and business value delivery assessment completed
- **Quality outcomes documented**: Testing results, code review outcomes, and validation status recorded
- **Technical decisions preserved**: Architecture choices, technology selections, and design rationale captured
- **Performance metrics recorded**: Development velocity, efficiency improvements, and resource utilization noted

### Knowledge and Context Preservation
- **Lessons learned extracted**: Discoveries, problem-solving approaches, and effective solution patterns identified
- **Blocker resolutions documented**: Encountered obstacles and successful mitigation strategies recorded
- **Critical context preserved**: Business insights, stakeholder feedback, and decision-making context captured
- **Best practices identified**: Effective workflows, tool usage, and collaboration patterns documented
- **Strategic insights recorded**: Architecture evolution, technology insights, and business alignment learnings preserved

### State Persistence and Future Session Preparation Quality
- **Session state successfully persisted**: Summary saved to SESSION_STATE.md with complete session context
- **TODO status preserved**: Current task status and priorities written to SESSION_TODOS.md
- **Continuation context documented**: Handoff information saved to CONTINUATION_CONTEXT.md for seamless resumption
- **Dependencies and blockers mapped**: External requirements, resource needs, and obstacles documented in persistent files
- **Cross-session continuity enabled**: All necessary information stored in accessible files for future session resumption

### MCP Tools Integration Quality (When Available)
- **Serena MCP detection successful**: Proper identification of .serena directory and tool accessibility
- **Project index synchronized**: Serena successfully updated with all session changes and new files
- **Reindexing completed**: Comprehensive refresh of Serena's code navigation and search capabilities
- **Integration validated**: Project knowledge properly indexed and searchable in Serena
- **Configuration updated**: Any project structure changes reflected in Serena settings

## 4. 📚 USAGE EXAMPLES

### Feature Development Session Completion
**Session Accomplishments**: User authentication API completed, frontend integration 80% done, security review passed
**Key Insights**: OAuth integration complexity underestimated, frontend state management pattern effective
**Next Steps**: Complete frontend integration, implement password reset flow, conduct end-to-end testing
**Continuity Context**: Design mockups approved, security requirements validated, deployment pipeline ready

### Bug Investigation and Resolution Session
**Session Accomplishments**: Critical payment bug identified and fixed, root cause analysis completed, patch deployed
**Key Insights**: Issue caused by race condition in concurrent transactions, monitoring gaps identified
**Next Steps**: Implement additional transaction monitoring, review similar patterns in codebase
**Continuity Context**: Customer impact resolved, monitoring improvements needed, code review feedback addressed

### Architecture Planning Session
**Session Accomplishments**: Microservices decomposition strategy designed, API contracts defined, migration plan created
**Key Insights**: Data consistency challenges more complex than anticipated, team capacity constraints identified
**Next Steps**: Validate API contracts with stakeholders, begin pilot service development, refine migration timeline
**Continuity Context**: Stakeholder approval needed for contracts, infrastructure requirements documented

### Code Quality Improvement Session
**Session Accomplishments**: Technical debt audit completed, refactoring plan created, critical issues addressed
**Key Insights**: Test coverage gaps in legacy modules, code complexity metrics improved significantly
**Next Steps**: Continue refactoring remaining modules, implement automated quality gates
**Continuity Context**: Refactoring priorities established, team training needs identified, quality metrics baseline set

### Security Assessment Session
**Session Accomplishments**: Vulnerability scan completed, 3 critical issues fixed, security documentation updated
**Key Insights**: Infrastructure hardening more effective than expected, team security awareness improving
**Next Steps**: Address remaining 2 moderate issues, implement security monitoring, schedule follow-up audit
**Continuity Context**: Compliance deadline on track, security tools configured, team training completed

---

## 🎯 EXECUTION APPROACH

**Session Documentation and State Persistence Process**:
1. **Comprehensive accomplishment review** - Systematically document all session outcomes and deliverables
2. **Insight extraction and knowledge capture** - Identify and preserve valuable learnings and context
3. **Intentional state persistence** - Use Write tool to save session summary, TODO status, and continuation context to dedicated files
4. **Future planning and continuity preparation** - Organize information for optimal next session productivity
5. **Documentation integration** - Update project knowledge base with relevant discoveries and decisions

**Quality Assurance for Session Summaries**:
- **Completeness verification** - Ensure all significant work and insights are captured
- **Accuracy validation** - Confirm technical details and progress assessments are correct
- **Actionability assessment** - Verify next steps are specific and executable
- **Context sufficiency** - Ensure adequate information for productive session continuation

**Adaptive Documentation Strategies**:
- **Quick sessions**: Focus on immediate accomplishments and next steps
- **Complex sessions**: Emphasize technical decisions, insights, and architectural context
- **Problem-solving sessions**: Highlight discovered issues, resolution approaches, and lessons learned
- **Planning sessions**: Document decisions, rationale, and strategic direction with stakeholder context