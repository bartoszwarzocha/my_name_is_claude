**🤖 AGENT ACTIVATION:** This prompt automatically activates the `project-owner` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# Project Structure Modernization and Optimization

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Analyze current project structure and organization to identify modernization opportunities that improve maintainability, scalability, and developer experience. Implement contemporary project organization patterns, optimize file and directory structures, enhance build processes, and ensure project layout supports team collaboration and long-term evolution.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Current Structure Analysis and Assessment
1. **Analyze existing project organization** - Map current directory structure, file organization patterns, and architectural boundaries
2. **Evaluate development workflow efficiency** - Assess how current structure supports or hinders development, testing, and deployment processes
3. **Identify structural technical debt** - Find inconsistent organization patterns, legacy structures, and maintainability challenges
4. **Assess team collaboration impact** - Evaluate how project structure affects team productivity, code sharing, and knowledge transfer
5. **Benchmark against industry standards** - Compare current organization with contemporary best practices for project type and technology stack

### Phase 2: Modernization Strategy Design and Planning
1. **Design target project structure** - Plan improved organization that addresses identified limitations and supports future growth
2. **Plan migration approach and timeline** - Design safe, incremental migration strategy minimizing disruption to active development
3. **Assess backward compatibility requirements** - Identify integration points and dependencies that must be preserved during reorganization
4. **Plan tooling and automation updates** - Design updates to build processes, CI/CD pipelines, and development tools for new structure
5. **Design team onboarding and documentation** - Plan knowledge transfer and documentation updates for structural changes

### Phase 3: Structure Implementation and Migration Execution
1. **Implement core structural improvements** - Execute planned directory reorganization, file moves, and architectural boundary improvements
2. **Update build and deployment processes** - Modify build configurations, packaging processes, and deployment scripts for new structure
3. **Migrate development tooling configuration** - Update IDE settings, linting configurations, and development environment setup
4. **Update documentation and guides** - Revise project documentation, setup instructions, and development guidelines for new structure
5. **Validate migration completeness** - Ensure all functionality works correctly in new structure and no components lost during migration

### Phase 4: Process Integration and Team Adoption
1. **Establish structure maintenance guidelines** - Define standards and processes for maintaining improved project organization over time
2. **Update development workflow documentation** - Revise development guides, code review processes, and collaboration procedures
3. **Plan team training and transition support** - Organize knowledge transfer sessions and provide resources for team adaptation
4. **Implement automated structure validation** - Set up tools and processes to prevent structure degradation and enforce organization standards
5. **Monitor adoption success and iterate** - Track team productivity impact and make refinements based on usage patterns and feedback

## 3. ✅ VALIDATION CRITERIA

### Structural Organization and Maintainability Improvement
- **Logical organization implemented**: Directory structure clearly reflects architectural boundaries and functional responsibilities
- **File organization optimized**: Related files grouped logically with clear naming conventions and consistent patterns
- **Technical debt reduced**: Legacy structural issues addressed and inconsistent organization patterns eliminated
- **Scalability enhanced**: Structure supports project growth and team expansion without major reorganization needs
- **Navigation efficiency improved**: Developers can locate and work with code more efficiently in reorganized structure

### Development Workflow and Tooling Integration
- **Build processes optimized**: Build times improved and build configuration simplified through better organization
- **Development tools updated**: IDE configurations, linting, testing, and debugging tools work seamlessly with new structure
- **CI/CD pipeline enhanced**: Deployment processes more efficient and reliable with improved project organization
- **Dependency management improved**: Package management, import structures, and dependency relationships clearer and more maintainable
- **Testing organization enhanced**: Test files and testing processes better organized and more discoverable

### Team Collaboration and Knowledge Transfer
- **Team productivity maintained or improved**: Development velocity sustained or increased during and after transition
- **Knowledge sharing enhanced**: Project structure facilitates code review, pair programming, and knowledge transfer between team members
- **Onboarding efficiency improved**: New team members can understand and navigate project structure more quickly
- **Documentation current**: All project documentation updated to reflect new structure and organization patterns
- **Standards compliance achieved**: Project follows contemporary best practices for technology stack and development methodology

## 4. 📚 USAGE EXAMPLES

### Legacy Monolith Modularization
**Project Context**: Large monolithic application with poor separation of concerns, mixed architectural layers
**Modernization Approach**:
- Separate presentation, business logic, and data access layers into clear directory hierarchies
- Extract reusable components into shared modules with proper dependency management
- Implement domain-driven design organization with bounded contexts and clear service boundaries
- Migrate from flat file structure to hierarchical organization reflecting application architecture
- Update build process to support modular compilation and testing strategies

### Frontend Application Structure Optimization
**Project Context**: React/Angular/Vue application with components, assets, and utilities scattered across directories
**Modernization Approach**:
- Organize components by feature domains rather than technical types
- Implement atomic design system structure with clear component hierarchy
- Separate business logic from presentation components using custom hooks or services
- Optimize asset organization with logical grouping and efficient loading strategies
- Implement barrel exports and index files for cleaner import statements

### Microservices Repository Consolidation
**Project Context**: Multiple related services in separate repositories creating coordination and sharing challenges
**Modernization Approach**:
- Implement monorepo structure with proper workspace management and build orchestration
- Share common libraries, utilities, and configuration across services with proper versioning
- Organize services by business domain with clear service boundaries and interface definitions
- Implement consistent project structure patterns across all services for maintainability
- Set up unified development environment and tooling configuration for all services

### API Development Project Restructuring
**Project Context**: REST API with controllers, models, and configuration mixed together lacking clear separation
**Modernization Approach**:
- Implement layered architecture with clear separation between controllers, services, and data access
- Organize endpoints by resource domains rather than technical concerns
- Separate configuration management with environment-specific and feature-specific settings
- Implement proper error handling, middleware, and cross-cutting concern organization
- Structure testing with unit, integration, and end-to-end tests clearly separated and organized

### Open Source Library Organization Enhancement
**Project Context**: Popular library with core functionality, examples, documentation, and tooling mixed together
**Modernization Approach**:
- Separate core library code from examples, documentation, and development tooling
- Implement proper package structure with clear public API boundaries and internal implementation separation
- Organize examples and documentation for different use cases and skill levels
- Set up proper release and distribution structure with automated packaging and versioning
- Implement contributor-friendly structure with clear guidelines and development setup

---

## 🎯 EXECUTION APPROACH

**Strategic Modernization Process**:
1. **Risk-aware migration planning** - Prioritize changes based on impact and risk to minimize disruption during transition
2. **Incremental implementation strategy** - Execute changes in phases to maintain development velocity and allow for adjustments
3. **Team-centered approach** - Design changes that improve team productivity and collaboration effectiveness
4. **Future-oriented planning** - Structure changes to support anticipated project growth and technology evolution

**Quality Assurance During Modernization**:
- **Functionality preservation** - Ensure all existing functionality continues working throughout reorganization process
- **Performance impact monitoring** - Track build times, development efficiency, and runtime performance during changes
- **Team productivity measurement** - Monitor developer velocity and satisfaction during and after structural changes
- **Automated validation** - Use automated testing and validation to catch issues introduced during reorganization

**Sustainability and Long-term Success**:
- **Documentation-driven change** - Maintain comprehensive documentation of new structure and organization principles
- **Process integration** - Embed structure maintenance into regular development workflows and code review processes
- **Continuous improvement** - Establish feedback mechanisms and regular review cycles for ongoing structural optimization
- **Knowledge preservation** - Ensure team knowledge of structural decisions and principles survives team changes