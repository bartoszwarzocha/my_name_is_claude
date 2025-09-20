**🤖 AGENT ACTIVATION:** This prompt automatically activates the `project-owner` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# Project Versioning and Change Documentation Management

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Manage project versioning strategy and maintain comprehensive changelog documentation that accurately reflects development progress, feature additions, bug fixes, and breaking changes. Establish semantic versioning practices, automate version management where possible, and ensure stakeholders have clear visibility into project evolution and release planning.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Version Strategy and Change History Analysis
**Objective**: Analyze versioning requirements and implement comprehensive change history analysis and documentation

1. **Version Strategy Analysis and Planning**
   - Assess current versioning approach analyzing version numbering, tagging practices, and release patterns
   - Evaluate semantic versioning compliance determining adherence to semver principles
   - Analyze change impact patterns, plan version numbering strategy, and establish release milestone planning

2. **Change History Analysis and Documentation**
   - Parse development history extracting changes from git commits, pull requests, and issue tracking systems
   - Categorize change types classifying as features, fixes, breaking changes, or maintenance
   - Identify unreleased changes, validate change descriptions, and map changes to version increments

### Phase 2: Changelog Generation and Release Management
**Objective**: Execute changelog generation and establish comprehensive version release and communication planning

1. **Changelog Generation and Enhancement**
   - Generate structured changelog creating formatted documentation following established conventions
   - Enhance change descriptions improving clarity for different audiences
   - Add contextual information, organize for different audiences, and cross-reference with documentation

2. **Version Release and Communication Planning**
   - Plan version increment strategy determining next version number based on accumulated changes
   - Prepare release communication drafting release notes and stakeholder communications
   - Establish version tagging process, configure automated processes, and plan stakeholder notification

## 3. ✅ VALIDATION CRITERIA

### Version Strategy and Change History Analysis
**Versioning Strategy Excellence**: Semantic versioning properly applied with version numbers accurately reflecting change impact, consistent versioning practices with all releases following established conventions, release planning aligned supporting business goals and technical roadmap requirements, breaking change management with major version increments for incompatible changes

**Change History Excellence**: Deprecation lifecycle managed with deprecated features properly versioned and communicated, all significant changes documented with features, fixes, and improvements recorded, change descriptions clear and actionable enabling stakeholder understanding, appropriate categorization with changes classified by type and impact

### Changelog Generation and Release Management
**Changelog Excellence**: Migration guidance provided with breaking changes including clear upgrade instructions, cross-references complete with links to relevant documentation and pull requests, development workflow integrated with changelog and versioning incorporated into processes, automation functional with version bumping and changelog generation working

**Release Management Excellence**: Release process streamlined with version tagging and stakeholder communication coordinated, quality standards maintained with consistent formatting and information architecture, stakeholder communication effective with appropriate audiences receiving relevant information through suitable channels

## 4. 📚 USAGE EXAMPLES

**API Library with Breaking Changes**: JavaScript SDK with major versions for breaking changes, minor versions for new features, patch versions for fixes, pre-release versions for beta testing, detailed deprecation timelines

**SaaS Platform with Regular Releases**: Web application with calendar-based versioning (YYYY.MM.PATCH), feature flag coordination, separate API versioning, changelog sections for different user types, in-app release notes

**Open Source CLI Tool**: Command-line application with strict semantic versioning for plugin compatibility, automated changelog generation, breaking change detection, separate plugin API versioning, community contribution tracking

**Enterprise Application with Compliance**: Financial services application with detailed change tracking for compliance, security update categorization, rollback capability documentation, change approval workflow integration, compliance impact assessment

**Mobile Application with App Store**: React Native app with version coordination between app stores and backend, feature rollout planning, app store review timeline integration, user communication strategy, API compatibility maintenance

---

## 🎯 EXECUTION APPROACH

**Version Management Excellence**: Comprehensive change analysis → stakeholder-aware versioning → communication-focused approach → beneficial process automation

**Quality Assurance for Versioning**: Change impact validation confirming version increments appropriately reflect change impact, changelog accuracy verification cross-referencing entries with actual changes, stakeholder communication testing validating information serves intended audiences, process consistency checking ensuring practices remain consistent

**Adaptive Versioning Strategies**: API-focused projects emphasizing backward compatibility tracking and breaking change management, user-facing applications focusing on feature communication and impact explanation, enterprise systems prioritizing compliance tracking and rollback documentation, open source projects emphasizing community contribution tracking and compatibility