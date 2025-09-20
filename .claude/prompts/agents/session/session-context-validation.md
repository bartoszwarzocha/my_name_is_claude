**🤖 AGENT ACTIVATION:** This prompt automatically activates the `session-manager` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# Session Context Validation and Integrity Assurance

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Validate session context integrity, detect corruption, and ensure reliable session state before initialization or restoration. Perform comprehensive validation of stored session summaries, project state consistency, TODO tracking accuracy, and MCP tools integration status. Identify context inconsistencies, repair corrupted data where possible, and provide clear guidance for session recovery or reinitialization when validation fails.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Context Integrity and Project State Validation
**Objective**: Validate session context integrity and project state consistency

1. **Context Integrity Assessment and Project Synchronization**
   - Validate stored session state files (SESSION_STATE.md, SESSION_TODOS.md, CONTINUATION_CONTEXT.md)
   - Verify project state consistency by comparing stored context with current files and git history
   - Assess context timestamp validity and validate cross-reference accuracy
   - Compare current vs stored project structure and verify git repository consistency

2. **MCP Tools Integration and Dependency Validation**
   - Verify MCP tools availability (Serena, Context7, Playwright) and configuration consistency
   - Assess integration point functionality and check tool version compatibility
   - Validate external dependencies and identify breaking changes
   - Ensure tool-specific context data is current and accurate

### Phase 2: Context Repair and Quality Assurance
**Objective**: Repair context issues and establish ongoing validation procedures

1. **Context Repair and Recovery Strategies**
   - Attempt automatic context repair for minor inconsistencies and stale references
   - Generate context refresh recommendations and create validation reports
   - Provide session initialization alternatives based on validation results
   - Establish context validation checkpoints to prevent future corruption

2. **Quality Assurance and Monitoring Integration**
   - Implement context health monitoring with continuous validation processes
   - Establish validation metrics, thresholds, and automation procedures
   - Generate validation performance analytics and improvement opportunities
   - Integrate with framework quality gates for overall standard alignment

## 3. ✅ VALIDATION CRITERIA

### Validation and Recovery Standards
**Context Integrity and Project Synchronization**:
- Session state files validated with proper formatting and complete data
- Project state consistency confirmed with acceptable variance and current cross-references
- Structure consistency confirmed with git repository state validated and configuration alignment verified
- Dependency availability confirmed and breaking changes identified with clear documentation

**Tool Integration and Quality Assurance**:
- MCP tool availability confirmed with configuration consistency and integration functionality validated
- Version compatibility assured and tool-specific context validated for accuracy and synchronization
- Context repair completed with clear guidance provided and comprehensive validation reports
- Session readiness determined with monitoring integration active for ongoing validation

## 4. 📚 USAGE EXAMPLES

**Cross-Context Validation Examples**

**Standard Session Continuation**: Check SESSION_STATE.md completeness, verify no major changes, confirm MCP tools functional

**Post-Interruption Recovery**: Assess potential corruption from incomplete saves, verify project state, check for partial updates

**Multi-Day Project Gap**: Comprehensive project state comparison, git history analysis, complete MCP tools revalidation

**Team Handoff Validation**: Ensure context completeness, verify dependencies accessible, validate MCP tools configuration

**Production Deployment**: Ensure development context aligns with production, verify dependencies, validate integration points

---

## 🎯 EXECUTION APPROACH

**Validation Process**: Comprehensive integrity assessment → risk-based prioritization → intelligent repair → clear decision support

**Adaptive Strategies**: Fresh sessions (project analysis), Continuation (consistency validation), Recovery (corruption detection), Handoff (completeness)

**Quality Integration**: Proactive validation, continuous monitoring, framework integration, user experience focus