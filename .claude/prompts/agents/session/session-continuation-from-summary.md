**🤖 AGENT ACTIVATION:** This prompt automatically activates the `session-manager` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# Session Continuity Restoration and Context Synthesis

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Restore development session context from previous session summary, analyze project changes since last session, and establish seamless work continuity. Synthesize historical context with current project state to identify optimal continuation points, validate priorities, and configure session for productive work resumption without losing momentum or missing critical updates.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: State Recovery and Integration
**Objective**: Restore session context and integrate with current project state

1. **State Recovery and Context Reconstruction**
   - Load SESSION_STATE.md, SESSION_TODOS.md, and CONTINUATION_CONTEXT.md files
   - Extract accomplished tasks, pending work, decisions made, and session outcomes
   - Rebuild task tracking from persisted TODO status and priorities
   - Analyze session gap timeframe and reconstruct work context

2. **Current State Integration and Gap Analysis**
   - Review git commits, file modifications, and configuration updates since last session
   - Validate framework status including CLAUDE.md updates and agent configurations
   - Compare context deltas and evaluate external impacts on project state
   - Reconcile inconsistencies between historical context and current reality

### Phase 2: Continuation Planning and Session Initialization
**Objective**: Plan productive continuation and initialize session with integrated context

1. **Priority Validation and MCP Tools Integration**
   - Validate previous priorities and assess momentum opportunities
   - Evaluate new constraints and refine task priorities based on current urgency
   - Detect and integrate Serena MCP tools when available
   - Synchronize Serena project context with historical session summaries

2. **Session Initialization and Context Handoff**
   - Synthesize comprehensive context combining historical, current, and tool information
   - Configure TODO restoration with updated priorities using TodoWrite tool
   - Prepare agent coordination and establish session objectives
   - Enable productive continuation with clear context for immediate work resumption

## 3. ✅ VALIDATION CRITERIA

### Recovery and Integration Standards
**State Recovery and Context Quality**:
- Session state files successfully loaded with historical context fully reconstructed
- TODO status accurately restored and work streams mapped from saved context
- Project changes assessed with framework status validated and context deltas identified
- External impacts evaluated and inconsistencies resolved between historical and current state

**Continuation and Tool Integration**:
- Priorities validated with momentum opportunities identified and resource constraints assessed
- Session objectives defined enabling productive resumption with clear continuation context
- Serena MCP successfully detected when available with project context loaded and synchronized
- Integrated context validated providing complete project understanding for immediate work resumption

## 4. 📚 USAGE EXAMPLES

**Cross-Context Continuation Examples**

**Feature Development**: Authentication API completed → design approved → resume frontend integration, address security requirements

**Bug Fix Resume**: Payment bug identified, partial fix → staging restored → complete testing, validate scenarios, deploy

**Architecture Planning**: Microservices analysis done → team feedback received → incorporate feedback, adjust scope, finalize roadmap

**Data Pipeline Development**: Ingestion built, transformation started → new sources added → resolve performance, integrate sources

**Security Audit Follow-up**: Vulnerability scan completed → 3 issues fixed → validate fixes, accelerate remaining remediation

---

## 🎯 EXECUTION APPROACH

**Restoration Process**: File-based state recovery → deep summary analysis → TODO restoration → gap assessment → context synthesis

**Adaptive Strategies**: Short gaps (momentum maintenance), Medium gaps (context validation), Long gaps (comprehensive re-analysis), Context changes (hybrid approach)

**Success Indicators**: Seamless work resumption, preserved insights, updated priorities, agent readiness