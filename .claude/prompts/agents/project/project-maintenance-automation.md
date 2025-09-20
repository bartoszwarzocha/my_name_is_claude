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

### Phase 1: Change Detection and Update Propagation
**Objective**: Detect framework changes and propagate updates intelligently

1. **Change Analysis and Classification**
   - Scan framework directories for modifications and categorize by impact scope
   - Map dependencies and determine update priority and sequence
   - Validate changes follow framework rules and compliance standards
   - Parse current documentation state and assess synchronization requirements

2. **Intelligent Update Propagation**
   - Synchronize statistics, lists, cross-references, and metadata across files
   - Maintain CLAUDE_template.md alignment with CLAUDE.md changes
   - Update directory structure representations and repair cross-references
   - Propagate agent and prompt additions to relevant documentation

### Phase 2: Quality Assurance and Reporting
**Objective**: Ensure framework integrity and document all maintenance activities

1. **Framework Integrity and Compliance**
   - Synchronize roadmap items and handle version management when requested
   - Validate examples reflect current capabilities and enforce framework rules
   - Verify enterprise-grade standards compliance across all updated files
   - Maintain agent-prompt binding integrity and technology-agnostic design

2. **Verification and Documentation**
   - Generate comprehensive change summaries with update rationale
   - Validate successful completion and confirm framework standards adherence
   - Document maintenance activities and suggest additional improvements
   - Create complete audit trail for transparency and future reference

## 3. ✅ VALIDATION CRITERIA

### Accuracy and Quality Standards
**Detection and Synchronization**:
- Complete component coverage with accurate change classification and dependency resolution
- Content accuracy ensuring statistics, lists, and metadata reflect current framework state
- Cross-reference integrity maintaining functional internal links and dependencies
- Template consistency with CLAUDE_template.md mirroring CLAUDE.md standards

**Compliance and Process Efficiency**:
- Framework rule adherence with quantitative data elimination and agent-prompt binding integrity
- Technology-agnostic design preservation and enterprise-grade quality standards
- Automation completeness requiring minimal manual intervention with robust error handling
- Complete audit trail generation and rollback capability for issue recovery

## 4. 📚 USAGE EXAMPLES

**Cross-Component Maintenance Examples**

**New Agent Integration**: Added mobile-engineer agent
- **Updates**: README.md agent count, CLAUDE.md roles section, template synchronization, roadmap completion

**Prompt Library Enhancement**: Added emergency response prompts
- **Updates**: Library statistics, agent-prompt binding verification, cross-reference updates, example refresh

**Framework Rules Modification**: Updated development guidelines
- **Updates**: Template propagation, compliance validation, documentation alignment, quality gate updates

**Version Release Management**: User-requested version update
- **Updates**: VERSION file, CHANGELOG generation, badge updates, metadata synchronization, template references

**Multi-Component Integration**: Simultaneous agent, prompt, and configuration updates
- **Updates**: Comprehensive impact analysis, prioritized sequencing, cross-component validation, complete documentation

**Framework Evolution**: Major architectural changes
- **Updates**: Evolution tracking, backward compatibility, migration guidance, impact assessment, strategic alignment

---

## 🎯 EXECUTION APPROACH

**Intelligent Automation Workflow**: Continuous monitoring → smart analysis → coordinated execution → quality assurance → comprehensive reporting

**Adaptive Behavior**: Minor changes (quick sync), Major changes (comprehensive analysis), Breaking changes (enhanced validation), Framework evolution (strategic documentation)

**Success Deliverables**: Perfect documentation synchronization, framework integrity maintenance, automated quality assurance, comprehensive change tracking