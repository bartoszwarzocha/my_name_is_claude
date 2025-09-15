**🤖 AGENT ACTIVATION:** This prompt automatically activates the `project-owner` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# Project Maintenance Automation

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Automatically maintain project documentation consistency and framework integrity by detecting changes in framework components and intelligently propagating updates across all dependent files. Ensure continuous compliance with framework standards while preserving project coherence and eliminating manual synchronization overhead.

Key capabilities include:
- **Change Detection and Impact Analysis** - Monitor framework components for modifications and assess propagation requirements
- **Automated Documentation Synchronization** - Update all dependent files based on detected changes
- **Framework Integrity Assurance** - Maintain compliance with framework rules and standards
- **Quality Gate Validation** - Ensure all changes meet enterprise-grade quality requirements
- **Cross-Reference Maintenance** - Preserve internal links and dependencies across documentation

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Change Detection and Analysis
1. **Component Monitoring** - Scan framework directories (agents/, prompts/, hooks/, root files) for modifications
2. **Change Classification** - Categorize detected changes by type and impact scope
3. **Dependency Mapping** - Identify all files and sections requiring updates based on changes
4. **Impact Assessment** - Determine update priority and sequence based on dependencies
5. **Compliance Validation** - Verify changes follow framework rules and standards

### Phase 2: Intelligent Update Propagation
1. **Documentation Analysis** - Parse current state of all documentation files
2. **Content Synchronization** - Update statistics, lists, cross-references, and metadata
3. **Template Maintenance** - Propagate CLAUDE.md changes to CLAUDE_template.md
4. **Directory Structure Updates** - Maintain accurate project structure representations
5. **Cross-Reference Repair** - Update internal links and dependencies

### Phase 3: Framework Integrity and Quality Assurance
1. **Roadmap Synchronization** - Mark completed roadmap items and update priorities
2. **Version Management** - Handle semantic versioning and changelog updates (when requested)
3. **Example Validation** - Ensure all examples reflect current framework capabilities
4. **Compliance Enforcement** - Validate framework rules across all updated files
5. **Quality Gate Validation** - Verify enterprise-grade standards compliance

### Phase 4: Reporting and Verification
1. **Change Summary Generation** - Document all performed updates and their rationale
2. **Integrity Verification** - Validate successful completion of all updates
3. **Compliance Reporting** - Confirm adherence to framework standards
4. **Recommendation Engine** - Suggest additional improvements or optimizations
5. **Update Documentation** - Record maintenance activities for future reference

## 3. ✅ VALIDATION CRITERIA

### Change Detection Accuracy
- **Complete Component Coverage** - All framework directories monitored for changes
- **Change Classification Precision** - Accurate categorization of modification types and impact
- **Dependency Resolution** - Correct identification of all files requiring updates
- **Priority Assessment** - Appropriate sequencing of updates based on dependencies
- **False Positive Minimization** - Avoid unnecessary updates for irrelevant changes

### Documentation Synchronization Quality
- **Content Accuracy** - All statistics, lists, and metadata reflect current framework state
- **Cross-Reference Integrity** - Internal links and dependencies remain functional
- **Template Consistency** - CLAUDE_template.md accurately mirrors CLAUDE.md standards
- **Directory Structure Accuracy** - Project structure representations match actual organization
- **Language Compliance** - All updates follow EN/PL language standards

### Framework Compliance Assurance
- **Rule Adherence** - All changes comply with framework development guidelines
- **Quantitative Data Elimination** - No violations of quantitative information restrictions
- **Agent-Prompt Binding Integrity** - Perfect alignment between agents and prompts maintained
- **Technology Agnostic Design** - Updates preserve framework's technology-neutral approach
- **Quality Standards** - All changes meet enterprise-grade quality requirements

### Process Efficiency and Reliability
- **Automation Completeness** - Minimal manual intervention required for routine updates
- **Error Handling** - Robust recovery from partial failures or unexpected conditions
- **Performance Optimization** - Efficient processing of large-scale framework changes
- **Audit Trail Generation** - Complete documentation of all performed updates
- **Rollback Capability** - Ability to reverse updates if issues are detected

## 4. 📚 USAGE EXAMPLES

### New Agent Integration Scenario
**Context**: Added `mobile-engineer` agent to `.claude/agents/mobile/mobile-engineer.md`
**Automated Updates**:
- **README.md**: Update agent count in directory tree, add to agent list with competencies
- **CLAUDE.md**: Add to Section 4. Agents and Roles under appropriate category
- **CLAUDE_template.md**: Synchronize new agent to template for future projects
- **FRAMEWORK_ROADMAP.md**: Mark related roadmap items as completed, update priorities
- **Directory Documentation**: Update all references to agent count and capabilities

### Prompt Library Enhancement Scenario
**Context**: Added emergency response prompts to `.claude/prompts/agents/project/`
**Automated Updates**:
- **README.md**: Update prompt library statistics and capability descriptions
- **CLAUDE.md**: Update Section 14. Prompt Library Status with new categories
- **Agent-Prompt Binding**: Verify directory structure matches agent activation patterns
- **Cross-References**: Update all internal references to prompt capabilities
- **Example Updates**: Refresh usage examples to include new prompt types

### Framework Rules Modification Scenario
**Context**: Updated framework development guidelines in CLAUDE.md
**Automated Updates**:
- **CLAUDE_template.md**: Propagate rule changes to template for new projects
- **Compliance Validation**: Check all existing files against updated rules
- **Documentation Updates**: Reflect rule changes in relevant documentation sections
- **Quality Gate Updates**: Modify validation criteria to include new requirements
- **Example Alignment**: Ensure all examples comply with updated rules

### Hooks Infrastructure Enhancement Scenario
**Context**: Added new automation hooks to `.claude/hooks/` directory
**Automated Updates**:
- **README.md**: Update integration capabilities and automation features
- **Documentation**: Update hooks documentation and usage guidelines
- **Framework Capabilities**: Reflect enhanced automation in capability descriptions
- **Example Integration**: Update integration examples to showcase new hooks
- **Directory Structure**: Update project structure documentation

### Version Release Management Scenario (On Request)
**Context**: User requests version update from 2.1.0 to 2.2.0
**Automated Updates**:
- **VERSION file**: Update semantic version number
- **CHANGELOG.md**: Generate new release section with accumulated changes
- **README.md**: Update version badges and release information
- **CLAUDE.md**: Update project metadata and version references
- **Examples Validation**: Verify all examples work with new version
- **Template Updates**: Ensure templates reference correct framework version

### Multi-Component Integration Scenario
**Context**: Simultaneous updates to agents, prompts, and configuration
**Automated Updates**:
- **Comprehensive Analysis**: Assess cumulative impact of all changes
- **Prioritized Updates**: Sequence updates to maintain consistency throughout process
- **Cross-Component Validation**: Ensure agent-prompt-configuration alignment
- **Integration Testing**: Validate framework coherence after all updates
- **Complete Documentation**: Update all affected documentation systematically

### Framework Evolution Tracking Scenario
**Context**: Major architectural changes affecting multiple framework components
**Automated Updates**:
- **Evolution Documentation**: Track framework capability progression
- **Backward Compatibility**: Ensure existing projects remain functional
- **Migration Guidance**: Generate update instructions for existing projects
- **Impact Assessment**: Document changes to framework usage patterns
- **Strategic Alignment**: Verify changes align with roadmap objectives

---

## 🎯 EXECUTION APPROACH

**Intelligent Automation Workflow**:
1. **Continuous Monitoring** - Maintain awareness of framework component changes
2. **Smart Analysis** - Apply intelligence to determine optimal update strategies
3. **Coordinated Execution** - Perform updates in logical sequence to maintain consistency
4. **Quality Assurance** - Validate all changes against framework standards
5. **Comprehensive Reporting** - Document all activities for transparency and audit

**Adaptive Behavior**:
- **Minor Changes**: Quick synchronization of statistics and metadata
- **Major Changes**: Comprehensive analysis and coordinated update across all affected files
- **Breaking Changes**: Enhanced validation and compatibility checking
- **Framework Evolution**: Strategic analysis and documentation of architectural progression

**Success Deliverables**:
- **Perfect Documentation Synchronization** - All files accurately reflect framework state
- **Framework Integrity Maintenance** - Rules compliance and quality standards preserved
- **Automated Quality Assurance** - Continuous validation of enterprise-grade standards
- **Comprehensive Change Tracking** - Complete audit trail of all maintenance activities