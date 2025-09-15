**🤖 AGENT ACTIVATION:** This prompt automatically activates the `project-owner` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# Comprehensive Project Documentation Synchronization

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Synchronize and update all project documentation to maintain consistency with current codebase, configuration, and business requirements. Analyze documentation gaps, identify outdated content, and generate comprehensive updates that reflect actual project state. Ensure documentation serves developers, stakeholders, and future maintenance teams effectively.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Documentation Discovery and Gap Analysis
1. **Inventory existing documentation** - Scan project for README files, API docs, architecture diagrams, user guides, and technical specifications
2. **Analyze documentation currency** - Compare documentation timestamps with recent code changes and feature development
3. **Identify coverage gaps** - Find undocumented components, APIs, configurations, and business processes
4. **Assess documentation quality** - Evaluate clarity, accuracy, completeness, and usefulness of existing content
5. **Map stakeholder documentation needs** - Determine what different audiences (developers, users, business) require

### Phase 2: Content Analysis and Validation
1. **Validate technical accuracy** - Cross-reference code examples, API specifications, and configuration details with actual implementation
2. **Review business alignment** - Ensure documentation reflects current business goals, user workflows, and value propositions
3. **Check accessibility and format** - Assess readability, organization, and accessibility of documentation for intended audiences
4. **Identify redundant content** - Find duplicate information and consolidation opportunities
5. **Evaluate maintenance burden** - Assess which documentation requires frequent updates and automation opportunities

### Phase 3: Documentation Strategy and Planning
1. **Design documentation architecture** - Plan optimal organization and structure for all documentation types
2. **Prioritize update activities** - Rank documentation updates by business impact, user needs, and maintenance urgency
3. **Plan automation opportunities** - Identify documentation that can be auto-generated from code, configs, or APIs
4. **Define maintenance processes** - Establish procedures for keeping documentation current with development changes
5. **Select appropriate tools and formats** - Choose formats and platforms that best serve each documentation purpose

### Phase 4: Documentation Generation and Integration
1. **Generate missing documentation** - Create new documentation for undocumented components and processes
2. **Update existing content** - Revise outdated documentation to reflect current project state
3. **Implement automation** - Set up auto-generation for API docs, configuration references, and other maintainable content
4. **Establish quality standards** - Define documentation standards, templates, and review processes
5. **Integrate with development workflow** - Ensure documentation updates are part of regular development processes

## 3. ✅ VALIDATION CRITERIA

### Documentation Coverage and Accuracy
- **Complete inventory created**: All existing documentation identified and catalogued by type and audience
- **Gap analysis comprehensive**: Missing documentation needs clearly identified and prioritized
- **Technical accuracy validated**: Code examples, API specs, and configuration details match actual implementation
- **Business alignment confirmed**: Documentation reflects current business goals, processes, and user workflows
- **Quality standards met**: All documentation meets readability, organization, and accessibility requirements

### Content Quality and Usefulness
- **Stakeholder needs addressed**: Different audiences have appropriate documentation for their use cases
- **Information architecture optimized**: Documentation organized logically with clear navigation and cross-references
- **Maintenance burden minimized**: Automated generation implemented where possible, manual processes streamlined
- **Redundancy eliminated**: Duplicate information consolidated, single sources of truth established
- **Standards consistently applied**: Templates, formatting, and style guidelines used throughout

### Integration and Sustainability
- **Development workflow integrated**: Documentation updates incorporated into regular development processes
- **Automation functional**: Auto-generation of API docs, configs, and other maintainable content operational
- **Quality processes established**: Review procedures and maintenance schedules defined and functional
- **Accessibility ensured**: Documentation available to intended audiences through appropriate channels
- **Future maintenance planned**: Processes and responsibilities defined for ongoing documentation maintenance

## 4. 📚 USAGE EXAMPLES

### API-First SaaS Platform Documentation
**Project Context**: RESTful API with web dashboard, multiple client SDKs, complex authentication
**Documentation Updates**:
- Auto-generated OpenAPI specs with code examples
- Updated SDK documentation with current authentication flows
- Refreshed user guides reflecting new dashboard features
- Architecture diagrams showing current microservices structure
- Integration guides for third-party developers

### Enterprise Legacy System Modernization
**Project Context**: Large monolithic application being gradually modernized with microservices
**Documentation Updates**:
- Migration guide documenting modernization progress and patterns
- Updated architecture diagrams showing hybrid legacy-modern structure
- API documentation for new microservices with integration examples
- Updated deployment procedures for containerized components
- Business process documentation reflecting workflow changes

### Open Source Development Tool
**Project Context**: CLI tool with plugins, extensive configuration options, active community
**Documentation Updates**:
- Comprehensive README with installation and quick start guides
- Auto-generated CLI help documentation from code annotations
- Plugin development guide with examples and best practices
- Configuration reference with all options and use cases
- Contributing guide for community developers

### Mobile Application with Backend Services
**Project Context**: React Native app with Node.js backend, real-time features, app store distribution
**Documentation Updates**:
- API documentation for mobile-backend communication
- Updated app store submission guides reflecting current build process
- Architecture documentation showing real-time data flow
- Development environment setup for mobile and backend
- User guide reflecting current app features and workflows

### Data Analytics Platform
**Project Context**: Python-based analytics pipeline with web interface, multiple data sources
**Documentation Updates**:
- Data pipeline documentation with current ETL processes
- API documentation for analytics endpoints and visualizations
- User guide for web interface with current features
- Data source integration guides with authentication examples
- Performance tuning guide based on production experience

---

## 🎯 EXECUTION APPROACH

**Comprehensive Documentation Process**:
1. **Systematic documentation audit** - Catalog all existing documentation and identify gaps systematically
2. **Stakeholder-driven prioritization** - Focus updates on documentation that provides highest value to users
3. **Automation-first approach** - Implement auto-generation where possible to reduce maintenance burden
4. **Integration with development** - Make documentation updates part of regular development workflow

**Quality Assurance Strategy**:
- **Technical accuracy validation** - Cross-reference all technical details with actual implementation
- **User experience testing** - Validate documentation usefulness with actual users and use cases
- **Consistency checking** - Ensure formatting, style, and organization standards throughout
- **Maintenance sustainability** - Design processes that keep documentation current with minimal effort

**Adaptive Documentation Strategies**:
- **API-heavy projects**: Emphasize auto-generated API docs with rich examples and integration guides
- **User-facing applications**: Focus on user guides, tutorials, and onboarding documentation
- **Developer tools**: Prioritize technical documentation, examples, and contribution guides
- **Enterprise systems**: Emphasize architecture, security, and operational documentation