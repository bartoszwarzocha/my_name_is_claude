# Emergency Session State Recovery and Context Restoration

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Recover and restore development session context when normal session continuity has been disrupted or compromised. Analyze project state from available artifacts, reconstruct development context, validate system integrity, and establish productive session recovery without losing critical work or momentum. Handle scenarios where session summaries are unavailable, corrupted, or incomplete.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Disruption Assessment and State Analysis
1. **Assess interruption impact** - Determine extent of context loss, missing information, and potential data integrity issues
2. **Analyze available artifacts** - Inventory git history, file modifications, configuration states, and documentation
3. **Reconstruct timeline** - Build understanding of recent development activity and project progression
4. **Identify recovery complexity** - Evaluate what can be restored automatically vs. requires manual investigation
5. **Determine recovery strategy** - Select optimal approach based on available information and project criticality

### Phase 2: Project Context Reconstruction
1. **Parse version control history** - Extract commit messages, file changes, and development patterns from git log
2. **Analyze project structure changes** - Compare current state with previous stable configurations
3. **Reconstruct work streams** - Identify active development areas, feature branches, and incomplete work
4. **Extract business context** - Parse documentation, issue trackers, and communication artifacts for project priorities
5. **Map dependency relationships** - Understand external integrations, blockers, and resource requirements

### Phase 3: System Integrity Validation and Environment Recovery
1. **Validate build system integrity** - Test compilation, dependency resolution, and build pipeline functionality
2. **Verify testing framework status** - Confirm test suites operational, coverage accurate, and quality metrics valid
3. **Check development environment** - Validate IDE configurations, tool availability, and access credentials
4. **Assess framework integration** - Confirm CLAUDE.md validity, agent availability, and TODO management operational
5. **Validate external integrations** - Test connections to databases, APIs, deployment systems, and monitoring

### Phase 4: Productive Session Recovery and Continuation Planning
1. **Synthesize recovered context** - Combine reconstructed information into coherent project understanding
2. **Identify immediate priorities** - Determine most critical tasks based on recovered context and business needs
3. **Plan recovery actions** - Create specific steps to address missing context, fix issues, and resume productivity
4. **Establish monitoring** - Set up validation checks to prevent similar disruptions and ensure recovery success
5. **Initialize productive session** - Provide clear context and next steps for effective work resumption

## 3. ✅ VALIDATION CRITERIA

### Recovery Completeness and Accuracy
- **Context gaps identified**: All missing information and unknown project state areas clearly documented
- **Available artifacts fully analyzed**: Git history, file changes, configurations, and documentation comprehensively reviewed
- **Timeline accurately reconstructed**: Recent development activity and project progression properly understood
- **Work streams mapped**: Active development areas, incomplete work, and pending tasks identified
- **Recovery strategy appropriate**: Selected approach matches available information and project needs

### System Integrity and Environment Validation
- **Build system operational**: Compilation, dependencies, and build pipeline confirmed functional
- **Testing framework validated**: Test suites running correctly with accurate coverage and quality metrics
- **Development environment ready**: IDE, tools, access, and configurations confirmed operational
- **Framework integration intact**: CLAUDE.md, agents, and TODO management confirmed functional
- **External integrations verified**: Database, API, deployment, and monitoring connections tested

### Session Recovery Quality and Productivity
- **Critical context restored**: Sufficient project understanding for productive work resumption
- **Immediate priorities identified**: Clear next steps based on business needs and recovered context
- **Recovery plan actionable**: Specific steps to address gaps, fix issues, and resume development
- **Monitoring established**: Validation checks and prevention measures implemented
- **Productive session enabled**: Clear context and objectives for effective work continuation

## 4. 📚 USAGE EXAMPLES

### Git Repository Corruption Recovery
**Disruption**: Local git repository corrupted, working directory changes unclear
**Recovery Process**:
- Clone fresh repository from remote, compare with local working directory
- Identify uncommitted changes and work in progress
- Validate build and test functionality after repository restoration
- Reconstruct recent work context from file timestamps and content analysis

### Development Environment Failure
**Disruption**: IDE crashed, session state lost, configuration corrupted
**Recovery Process**:
- Restore IDE configuration from backups or defaults
- Analyze recent file modifications and open project artifacts
- Validate development environment functionality and tool availability
- Reconstruct work context from git history and project documentation

### Framework Configuration Corruption
**Disruption**: CLAUDE.md corrupted, agent configurations lost, TODO management broken
**Recovery Process**:
- Restore CLAUDE.md from git history or regenerate from project analysis
- Validate agent availability and framework integration
- Reconstruct TODO management state from git commits and documentation
- Re-establish session context from available project artifacts

### System Crash During Development
**Disruption**: Unexpected system shutdown, unsaved work potentially lost, session context unclear
**Recovery Process**:
- Check for auto-saved files, temporary backups, and IDE recovery files
- Compare current state with last known git commit
- Validate system integrity and development environment functionality
- Reconstruct work progress from file modifications and available artifacts

### Team Handoff Without Documentation
**Disruption**: Taking over project from another developer without proper handoff documentation
**Recovery Process**:
- Analyze git history for development patterns and recent activity
- Extract business context from project documentation and code comments
- Identify active work streams and pending tasks from branch analysis
- Establish development environment and validate project functionality

---

## 🎯 EXECUTION APPROACH

**Emergency Recovery Process**:
1. **Rapid state assessment** - Quickly identify what information is available and what is missing
2. **Systematic artifact analysis** - Methodically examine all available project artifacts and history
3. **Intelligent context reconstruction** - Combine available information into coherent project understanding
4. **Environment validation** - Ensure all systems and tools are functional before resuming work

**Recovery Strategy Selection**:
- **Complete context loss**: Full project analysis and reconstruction from available artifacts
- **Partial context loss**: Targeted recovery focusing on missing or corrupted information
- **Environment corruption**: System and tool validation with context preservation
- **Handoff scenarios**: Comprehensive project analysis with stakeholder context building

**Risk Mitigation and Prevention**:
- **Regular state backup**: Establish automatic session summary and context preservation
- **Environment monitoring**: Detect and prevent corruption or integrity issues
- **Recovery validation**: Confirm successful recovery before resuming development work
- **Documentation standards**: Maintain sufficient project documentation for emergency recovery