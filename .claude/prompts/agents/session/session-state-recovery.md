**🤖 AGENT ACTIVATION:** This prompt automatically activates the `session-manager` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# Emergency Session State Recovery and Context Restoration

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Recover and restore development session context when normal session continuity has been disrupted or compromised. Analyze project state from available artifacts, reconstruct development context, validate system integrity, and establish productive session recovery without losing critical work or momentum. Handle scenarios where session summaries are unavailable, corrupted, or incomplete.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Disruption Assessment and Context Reconstruction
**Objective**: Analyze disruption impact and implement comprehensive project context reconstruction and system validation

1. **Disruption Assessment and State Analysis**
   - Assess interruption impact determining extent of context loss and potential data integrity issues
   - Analyze available artifacts inventorying git history, file modifications, and documentation
   - Reconstruct timeline, identify recovery complexity, and determine optimal recovery strategy

2. **Project Context Reconstruction and System Validation**
   - Parse version control history extracting commit messages, file changes, and development patterns
   - Analyze project structure changes, reconstruct work streams, and extract business context
   - Validate build system integrity, verify testing framework status, and check development environment

### Phase 2: MCP Recovery and Session Restoration
**Objective**: Execute MCP tools recovery and establish comprehensive session recovery and continuation planning

1. **MCP Tools Recovery and Integration (If Available)**
   - Detect and assess Serena MCP checking for .serena directory and evaluating tool state after disruption
   - Recover Serena project index restoring or rebuilding project indexing and navigation capabilities
   - Synchronize recovered context, validate MCP functionality, and update tool configuration

2. **Productive Session Recovery and Continuation Planning**
   - Synthesize recovered context combining reconstructed, current, and Serena information into coherent understanding
   - Identify immediate priorities, plan recovery actions, and establish monitoring
   - Initialize productive session providing clear context and next steps for effective work resumption

## 3. ✅ VALIDATION CRITERIA

### Disruption Assessment and Context Reconstruction
**Recovery Completeness Excellence**: Context gaps identified with all missing information and unknown project state areas clearly documented, available artifacts fully analyzed with git history and configurations comprehensively reviewed, timeline accurately reconstructed with recent development activity properly understood, work streams mapped with active development areas and pending tasks identified

**System Validation Excellence**: Recovery strategy appropriate with selected approach matching available information and project needs, build system operational with compilation and dependencies confirmed functional, testing framework validated with test suites running correctly, development environment ready with IDE and configurations operational, framework integration intact with CLAUDE.md and agents functional

### MCP Recovery and Session Restoration
**MCP Recovery Excellence**: External integrations verified with database, API, and monitoring connections tested, MCP tools recovery successful with Serena functionality restored and configuration updated, context synchronization complete with recovered information properly integrated

**Session Recovery Excellence**: Critical context restored with sufficient project understanding for productive work resumption, immediate priorities identified with clear next steps based on business needs, recovery plan actionable with specific steps to address gaps, monitoring established with validation checks implemented, productive session enabled with clear context and objectives

## 4. 📚 USAGE EXAMPLES

**Git Repository Corruption**: Local repository corrupted with working directory changes unclear, recovery involves cloning fresh repository, identifying uncommitted changes, validating build functionality, reconstructing work context

**Development Environment Failure**: IDE crashed with session state lost, recovery involves restoring IDE configuration, analyzing recent modifications, validating environment functionality, reconstructing work context

**Framework Configuration Corruption**: CLAUDE.md corrupted with agent configurations lost, recovery involves restoring CLAUDE.md from git history, validating agent availability, reconstructing TODO management state

**System Crash During Development**: Unexpected shutdown with unsaved work potentially lost, recovery involves checking auto-saved files, comparing with last commit, validating system integrity, reconstructing work progress

**Team Handoff Without Documentation**: Taking over project without proper handoff, recovery involves analyzing git history patterns, extracting business context, identifying active work streams, establishing development environment

---

## 🎯 EXECUTION APPROACH

**Emergency Recovery Excellence**: Rapid state assessment → systematic artifact analysis → intelligent context reconstruction → environment validation

**Recovery Strategy Selection**: Complete context loss requiring full project analysis and reconstruction from available artifacts, partial context loss needing targeted recovery focusing on missing information, environment corruption requiring system validation with context preservation, handoff scenarios needing comprehensive project analysis with stakeholder context building

**Risk Mitigation and Prevention**: Regular state backup establishing automatic session summary and context preservation, environment monitoring detecting and preventing corruption issues, recovery validation confirming successful recovery before resuming work, documentation standards maintaining sufficient project documentation for emergency recovery