**🤖 AGENT ACTIVATION:** This prompt automatically activates the `session-manager` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# Session Context Validation and Integrity Assurance

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Validate session context integrity, detect corruption, and ensure reliable session state before initialization or restoration. Perform comprehensive validation of stored session summaries, project state consistency, TODO tracking accuracy, and MCP tools integration status. Identify context inconsistencies, repair corrupted data where possible, and provide clear guidance for session recovery or reinitialization when validation fails.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Context Integrity Assessment and Validation
1. **Validate stored session state files** - Check existence, format, and completeness of SESSION_STATE.md, SESSION_TODOS.md, and CONTINUATION_CONTEXT.md
2. **Verify project state consistency** - Compare stored context with current project files, git history, and configuration changes
3. **Assess context timestamp validity** - Evaluate context age, identify stale data, and determine if refresh is needed
4. **Validate cross-reference accuracy** - Check internal references, file paths, and dependency relationships in stored context
5. **Detect context corruption indicators** - Identify inconsistencies, missing data, or format violations in session files

### Phase 2: Project State Synchronization Validation
1. **Compare current vs stored project structure** - Validate directory structure, file existence, and organizational changes
2. **Verify git repository consistency** - Check for new commits, branch changes, or repository state modifications
3. **Assess configuration drift** - Compare current CLAUDE.md, package files, and environment settings with stored context
4. **Validate external dependencies** - Check availability of databases, APIs, services, and integration points referenced in context
5. **Identify breaking changes** - Detect modifications that could invalidate stored session assumptions or workflows

### Phase 3: MCP Tools and Integration Validation
1. **Verify MCP tools availability and status** - Check Serena, Context7, Playwright, and other configured tools accessibility
2. **Validate tool configuration consistency** - Ensure MCP tool settings match current project requirements and stored context
3. **Assess integration point functionality** - Test critical tool integrations and identify any configuration or connectivity issues
4. **Check tool version compatibility** - Verify MCP tools versions are compatible with stored session requirements
5. **Validate tool-specific context data** - Ensure Serena indices, Context7 mappings, and other tool data are current and accurate

### Phase 4: Context Repair and Recovery Strategies
1. **Attempt automatic context repair** - Fix minor inconsistencies, update stale references, and resolve simple format issues
2. **Generate context refresh recommendations** - Identify areas requiring manual review or complete context regeneration
3. **Create validation report with actionable guidance** - Document all issues found with specific resolution steps
4. **Provide session initialization alternatives** - Recommend whether to proceed with current context, refresh specific components, or restart completely
5. **Establish context validation checkpoints** - Set up ongoing validation procedures to prevent future corruption

### Phase 5: Quality Assurance and Monitoring Integration
1. **Implement context health monitoring** - Create continuous validation processes for active sessions
2. **Establish validation metrics and thresholds** - Define acceptable context quality levels and degradation indicators
3. **Create validation automation** - Set up automatic context validation during session transitions and key operations
4. **Generate validation performance analytics** - Track validation effectiveness and identify improvement opportunities
5. **Integrate with framework quality gates** - Ensure context validation aligns with overall framework quality standards

## 3. ✅ VALIDATION CRITERIA

### Context Integrity Validation Success
- **Session state files validated**: All required session files exist, are properly formatted, and contain complete data
- **Project state consistency confirmed**: Current project structure matches stored context expectations with acceptable variance
- **Context freshness verified**: Session context age is within acceptable limits or refresh strategy is defined
- **Cross-references validated**: All internal references, file paths, and dependency relationships are accurate and current
- **Corruption detection completed**: Any context corruption is identified with clear severity assessment and repair options

### Project Synchronization Validation Success
- **Structure consistency confirmed**: Project directory structure, critical files, and organizational changes properly assessed
- **Git repository state validated**: Repository changes identified and compatibility with stored context determined
- **Configuration alignment verified**: Current project configuration matches stored context or drift is properly documented
- **Dependency availability confirmed**: All external dependencies and integration points are accessible and functional
- **Breaking changes identified**: Any modifications that could impact session effectiveness are clearly documented

### MCP Tools Integration Validation Success
- **Tool availability confirmed**: All configured MCP tools are accessible and responding properly
- **Configuration consistency verified**: MCP tool settings align with project requirements and stored session context
- **Integration functionality validated**: Critical tool integrations tested and confirmed operational
- **Version compatibility assured**: MCP tool versions compatible with session requirements and framework standards
- **Tool-specific context validated**: All tool-generated context data is current, accurate, and properly synchronized

### Recovery and Quality Assurance Success
- **Context repair completed**: Automatic repairs applied successfully where possible without data loss
- **Clear guidance provided**: Specific, actionable recommendations for resolving any identified context issues
- **Validation report comprehensive**: Complete documentation of validation results with clear resolution paths
- **Session readiness determined**: Clear recommendation on session initialization approach based on validation results
- **Monitoring integration active**: Ongoing context validation and quality monitoring procedures established

## 4. 📚 USAGE EXAMPLES

### Standard Session Continuation Validation
**Scenario**: Validating context before continuing development session from previous day
**Validation Focus**:
- Check SESSION_STATE.md for completeness and consistency
- Verify no major project changes occurred overnight
- Confirm MCP tools are functional and indices are current
- Validate TODO status accuracy and project priorities remain relevant

### Post-Interruption Context Recovery Validation
**Scenario**: Validating session context after unexpected interruption or system crash
**Validation Focus**:
- Assess potential context corruption from incomplete save operations
- Verify project state matches expectations at interruption time
- Check for partial file updates or inconsistent state
- Determine if emergency context reconstruction is needed

### Multi-Day Project Gap Validation
**Scenario**: Resuming work after extended absence with potential significant project changes
**Validation Focus**:
- Comprehensive project state comparison with stored context
- Git history analysis for major architectural or dependency changes
- Complete MCP tools revalidation and reindexing if necessary
- Assessment of context relevance and business priority shifts

### Team Handoff Context Validation
**Scenario**: Validating context integrity before transferring session to different team member
**Validation Focus**:
- Ensure context completeness for knowledge transfer
- Verify all external dependencies are accessible to new team member
- Check that stored context contains sufficient detail for effective handoff
- Validate MCP tools configuration matches team member's environment

### Production Deployment Context Validation
**Scenario**: Validating development context before major deployment or release preparation
**Validation Focus**:
- Ensure development context aligns with production requirements
- Verify no critical dependencies or configurations are missing
- Check that session context supports deployment workflow requirements
- Validate integration points and external service compatibility

---

## 🎯 EXECUTION APPROACH

**Systematic Context Validation Process**:
1. **Comprehensive integrity assessment** - Systematic validation of all stored context components
2. **Risk-based validation prioritization** - Focus validation efforts on highest-impact context elements
3. **Intelligent repair and recovery** - Attempt automatic fixes while preserving context accuracy and completeness
4. **Clear decision support** - Provide specific guidance for session initialization based on validation results

**Adaptive Validation Strategies**:
- **Fresh sessions**: Focus on project state analysis and MCP tools integration
- **Continuation sessions**: Emphasize context consistency and freshness validation
- **Recovery sessions**: Prioritize corruption detection and repair capabilities
- **Handoff sessions**: Ensure context completeness and accessibility for different users

**Quality Integration Approach**:
- **Proactive validation** - Regular context health checks during active sessions
- **Continuous monitoring** - Ongoing validation to prevent context degradation
- **Framework integration** - Alignment with overall framework quality standards and procedures
- **User experience focus** - Ensure validation enhances rather than impedes session productivity