**🤖 AGENT ACTIVATION:** This prompt automatically activates the `session-manager` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# MCP Serena Integration and Project Synchronization

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Integrate and synchronize project state with MCP Serena for intelligent code navigation, project indexing, and enhanced development workflow. Update Serena project configuration, refresh code indices, validate integration status, and optimize tool utilization for maximum development productivity. Ensure seamless coordination between Claude Code framework and Serena MCP capabilities.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Serena Integration Assessment and Configuration
1. **Detect Serena availability** - Check if MCP Serena is installed, configured, and accessible for project integration
2. **Analyze project structure** - Assess project organization, technology stack, and development patterns for optimal Serena configuration
3. **Evaluate indexing requirements** - Determine which files, directories, and code patterns should be indexed for navigation
4. **Configure project settings** - Update or create Serena project.yml with project-specific settings and preferences
5. **Validate integration readiness** - Confirm Serena can access project files and perform indexing operations

### Phase 2: Project Indexing and Code Analysis Synchronization
1. **Initialize project indexing** - Trigger comprehensive Serena indexing of project codebase and documentation
2. **Configure language support** - Set up language-specific analysis for detected programming languages and frameworks
3. **Update navigation indices** - Refresh code structure, symbol definitions, and cross-reference mappings
4. **Sync documentation links** - Index project documentation and establish links between code and docs
5. **Validate index completeness** - Confirm all relevant project components are properly indexed and searchable

### Phase 3: Development Workflow Integration and Optimization
1. **Configure editor integration** - Set up Serena integration with IDE and development tools for seamless navigation
2. **Optimize search capabilities** - Configure intelligent code search patterns and contextual navigation features
3. **Enable real-time synchronization** - Set up automatic index updates on file changes and git commits
4. **Configure collaboration features** - Enable project sharing and team collaboration capabilities if applicable
5. **Integrate with framework agents** - Configure Serena to support Claude Code agent workflows and context sharing

### Phase 4: Status Validation and Performance Optimization
1. **Validate integration status** - Test Serena functionality, navigation accuracy, and search performance
2. **Optimize configuration settings** - Adjust indexing preferences, search parameters, and performance settings
3. **Configure monitoring and alerts** - Set up notifications for index updates, sync issues, and integration problems
4. **Document integration setup** - Record configuration decisions and usage patterns for team reference
5. **Establish maintenance procedures** - Plan regular sync operations and integration health checks

## 3. ✅ VALIDATION CRITERIA

### Integration Setup and Configuration Success
- **Serena availability confirmed**: MCP Serena is installed, accessible, and properly configured for project use
- **Project configuration complete**: project.yml properly configured with project-specific settings and preferences
- **Language support enabled**: All project programming languages and frameworks properly configured for analysis
- **Integration permissions verified**: Serena has appropriate access to project files and development tools
- **Baseline configuration documented**: Integration setup and configuration decisions recorded for reference

### Indexing and Synchronization Completeness
- **Project fully indexed**: All relevant source code, documentation, and configuration files indexed and searchable
- **Navigation accuracy validated**: Code symbols, definitions, and cross-references properly mapped and accessible
- **Real-time sync operational**: File changes and git commits automatically trigger appropriate index updates
- **Search functionality verified**: Intelligent code search, pattern matching, and contextual navigation working correctly
- **Documentation integration complete**: Project docs indexed and linked with corresponding code components

### Workflow Integration and Performance Quality
- **Editor integration functional**: Seamless navigation and search capabilities available in development environment
- **Agent workflow support**: Serena properly configured to support Claude Code framework agent operations
- **Performance optimized**: Index updates, search operations, and navigation perform within acceptable response times
- **Collaboration ready**: Team sharing and collaboration features configured appropriately for project needs
- **Monitoring established**: Health checks, alerts, and maintenance procedures operational and documented

## 4. 📚 USAGE EXAMPLES

### React TypeScript Project Integration
**Project Context**: Large React application with TypeScript, 500+ components, complex state management
**Serena Configuration**:
- Language support: TypeScript, JavaScript, JSX, CSS
- Index focus: Component definitions, hook usage patterns, type definitions
- Navigation optimization: Component hierarchy, prop interfaces, state flows
- Integration: VSCode extension with intelligent autocomplete and navigation

### Enterprise Java Microservices Integration
**Project Context**: Spring Boot microservices architecture, multiple modules, shared libraries
**Serena Configuration**:
- Language support: Java, XML, YAML configuration files
- Index focus: Service interfaces, data models, configuration properties
- Navigation optimization: Cross-service dependencies, API contracts, shared utilities
- Integration: IntelliJ IDEA plugin with microservice architecture visualization

### Python Data Science Project Integration
**Project Context**: Jupyter notebooks, pandas workflows, machine learning pipelines
**Serena Configuration**:
- Language support: Python, Jupyter notebooks, YAML, SQL
- Index focus: Function definitions, data transformations, model implementations
- Navigation optimization: Pipeline stages, data dependencies, analysis workflows
- Integration: JupyterLab extension with notebook-aware navigation

### Full-Stack Node.js Application Integration
**Project Context**: Express.js backend, React frontend, shared utilities, database migrations
**Serena Configuration**:
- Language support: JavaScript, TypeScript, SQL, JSON
- Index focus: API endpoints, database models, shared types, utility functions
- Navigation optimization: Full-stack data flow, API-frontend connections, database relationships
- Integration: VSCode workspace with mono-repo aware navigation

### Legacy Codebase Modernization Integration
**Project Context**: Large legacy application, mixed technologies, gradual modernization in progress
**Serena Configuration**:
- Language support: Multiple legacy and modern languages as detected
- Index focus: Interface boundaries, modernization targets, dependency relationships
- Navigation optimization: Legacy-modern code bridges, refactoring opportunities, impact analysis
- Integration: Cross-language navigation with modernization progress tracking

---

## 🎯 EXECUTION APPROACH

**Integration and Sync Process**:
1. **Comprehensive Serena assessment** - Verify availability, capabilities, and optimal configuration approach
2. **Project-aware configuration** - Set up Serena with project-specific settings and preferences
3. **Intelligent indexing execution** - Perform comprehensive project indexing with real-time synchronization
4. **Workflow integration validation** - Confirm seamless integration with development tools and agent workflows

**Adaptive Configuration Strategies**:
- **Large codebases**: Focus on incremental indexing and performance optimization
- **Multi-language projects**: Configure comprehensive language support with cross-language navigation
- **Team environments**: Enable collaboration features and shared configuration management
- **Legacy systems**: Emphasize dependency analysis and modernization support navigation

**Integration Success Metrics**:
- **Navigation efficiency**: Reduced time to find code definitions, references, and related components
- **Search accuracy**: High relevance and completeness of code search results and pattern matching
- **Sync performance**: Fast index updates and minimal impact on development workflow
- **Agent coordination**: Effective support for Claude Code framework multi-agent operations