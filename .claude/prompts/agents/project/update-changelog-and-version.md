**🤖 AGENT ACTIVATION:** This prompt automatically activates the `project-owner` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# Project Versioning and Change Documentation Management

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Manage project versioning strategy and maintain comprehensive changelog documentation that accurately reflects development progress, feature additions, bug fixes, and breaking changes. Establish semantic versioning practices, automate version management where possible, and ensure stakeholders have clear visibility into project evolution and release planning.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Version Strategy Analysis and Planning
1. **Assess current versioning approach** - Analyze existing version numbering, tagging practices, and release patterns
2. **Evaluate semantic versioning compliance** - Determine adherence to semver principles and identify improvement opportunities
3. **Analyze change impact patterns** - Review historical changes to understand breaking vs. non-breaking change frequency
4. **Plan version numbering strategy** - Design appropriate versioning scheme for project type, audience, and release cadence
5. **Establish release milestone planning** - Define major/minor/patch release criteria and timeline strategies

### Phase 2: Change History Analysis and Documentation
1. **Parse development history** - Extract changes from git commits, pull requests, and issue tracking systems
2. **Categorize change types** - Classify changes as features, fixes, breaking changes, performance improvements, or maintenance
3. **Identify unreleased changes** - Catalog all changes since last version release for upcoming release planning
4. **Validate change descriptions** - Ensure change descriptions are accurate, clear, and useful for stakeholders
5. **Map changes to version increments** - Determine appropriate version number changes based on change impact

### Phase 3: Changelog Generation and Enhancement
1. **Generate structured changelog** - Create formatted changelog following established conventions and best practices
2. **Enhance change descriptions** - Improve clarity and usefulness of change descriptions for different audiences
3. **Add contextual information** - Include migration guides, deprecation notices, and impact assessments where needed
4. **Organize for different audiences** - Structure information for developers, users, and business stakeholders appropriately
5. **Cross-reference with documentation** - Link changelog entries to relevant documentation and migration guides

### Phase 4: Version Release and Communication Planning
1. **Plan version increment strategy** - Determine next version number based on accumulated changes and impact analysis
2. **Prepare release communication** - Draft release notes, announcements, and stakeholder communications
3. **Establish version tagging process** - Plan git tagging, release branch management, and deployment coordination
4. **Configure automated processes** - Set up automated version bumping, changelog generation, and release workflows
5. **Plan stakeholder notification** - Organize communication to users, developers, and business stakeholders about releases

## 3. ✅ VALIDATION CRITERIA

### Versioning Strategy and Compliance
- **Semantic versioning properly applied**: Version numbers accurately reflect change impact (major/minor/patch)
- **Consistent versioning practices**: All releases follow established versioning conventions and patterns
- **Release planning aligned**: Version increments support business goals and technical roadmap requirements
- **Breaking change management**: Major version increments properly used for incompatible changes
- **Deprecation lifecycle managed**: Deprecated features properly versioned and communicated with migration timelines

### Changelog Quality and Completeness
- **All significant changes documented**: Features, fixes, breaking changes, and improvements properly recorded
- **Change descriptions clear and actionable**: Stakeholders can understand impact and required actions
- **Appropriate categorization**: Changes properly classified by type and impact for easy consumption
- **Migration guidance provided**: Breaking changes include clear upgrade instructions and compatibility notes
- **Cross-references complete**: Links to relevant documentation, issues, and pull requests included

### Process Integration and Automation
- **Development workflow integrated**: Changelog and versioning incorporated into regular development processes
- **Automation functional**: Automated version bumping and changelog generation working where appropriate
- **Release process streamlined**: Version tagging, release notes, and stakeholder communication coordinated
- **Quality standards maintained**: Consistent formatting, style, and information architecture across releases
- **Stakeholder communication effective**: Appropriate audiences receive relevant version information through suitable channels

## 4. 📚 USAGE EXAMPLES

### API Library with Breaking Changes
**Project Context**: JavaScript SDK with frequent API improvements, backward compatibility concerns
**Versioning Strategy**:
- Major versions for breaking API changes with migration guides
- Minor versions for new features maintaining backward compatibility
- Patch versions for bug fixes and performance improvements
- Pre-release versions for beta testing new features
- Detailed deprecation timeline spanning multiple minor versions

### SaaS Platform with Regular Feature Releases
**Project Context**: Web application with monthly feature releases, diverse user base
**Versioning Strategy**:
- Calendar-based versioning (YYYY.MM.PATCH) for predictable release communication
- Feature flag coordination with version releases
- Separate API versioning for integration stability
- Changelog sections for different user types (admin, end-user, developer)
- Release notes integrated with in-app notifications

### Open Source CLI Tool
**Project Context**: Command-line application with plugin ecosystem, semantic versioning requirements
**Versioning Strategy**:
- Strict semantic versioning for plugin compatibility
- Automated changelog generation from conventional commits
- Breaking change detection for command-line interface modifications
- Plugin API versioning separate from application versioning
- Community contribution tracking in changelog

### Enterprise Application with Compliance Requirements
**Project Context**: Financial services application with regulatory compliance and audit requirements
**Versioning Strategy**:
- Detailed change tracking for compliance and audit purposes
- Security update categorization and priority communication
- Rollback capability documentation for each version
- Change approval workflow integration with version management
- Compliance impact assessment for each version release

### Mobile Application with App Store Coordination
**Project Context**: React Native app with iOS/Android distribution, feature rollout coordination
**Versioning Strategy**:
- Version coordination between app stores and backend services
- Feature rollout planning with gradual deployment strategies
- App store review timeline integration with version planning
- User communication strategy for app updates and new features
- Backend API compatibility maintenance across mobile app versions

---

## 🎯 EXECUTION APPROACH

**Version Management Process**:
1. **Comprehensive change analysis** - Review all changes since last version for impact assessment
2. **Stakeholder-aware versioning** - Consider impact on different user types when planning version increments
3. **Communication-focused approach** - Ensure version information serves stakeholder decision-making needs
4. **Process automation where beneficial** - Automate routine tasks while maintaining human oversight for strategic decisions

**Quality Assurance for Versioning**:
- **Change impact validation** - Confirm version increments appropriately reflect actual change impact
- **Changelog accuracy verification** - Cross-reference changelog entries with actual changes and their effects
- **Stakeholder communication testing** - Validate that version information serves intended audiences effectively
- **Process consistency checking** - Ensure versioning and changelog practices remain consistent over time

**Adaptive Versioning Strategies**:
- **API-focused projects**: Emphasize backward compatibility tracking and breaking change management
- **User-facing applications**: Focus on feature communication and user impact explanation
- **Enterprise systems**: Prioritize compliance tracking, security updates, and rollback documentation
- **Open source projects**: Emphasize community contribution tracking and plugin/extension compatibility