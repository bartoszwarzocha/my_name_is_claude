# AI Tools Configuration for {project_name}

## 🤖 AI-Assisted Development Setup

This project is configured to work with the following AI development tools:

### Serena Integration
{serena_status}

**Serena is used for:**
- Code navigation and symbol search
- Intelligent code editing and refactoring
- Project structure analysis
- Automated testing and building
- Cross-file dependency tracking
- Language server integration

**Setup:**
- Configuration: `.serena/project.yml`
- Language: {language}
- Active tools: All Serena tools enabled
- Memory system: Project-specific context storage

### Context7 Integration  
{context7_status}

**Context7 is used for:**
- Advanced code generation and scaffolding
- Complex code migrations and transformations
- Multi-file refactoring operations
- Architecture pattern implementation
- Database schema migrations
- API endpoint generation
- Test suite generation
- Documentation generation
- Configuration file templating
- Infrastructure-as-Code generation

**Recommended Context7 Usage:**
- **Code Generation**: New features, components, services
- **Migrations**: Database schema changes, API version upgrades
- **Refactoring**: Large-scale code restructuring
- **Scaffolding**: New modules, test suites, configuration
- **Documentation**: API docs, README updates, code comments

## 🔄 Agent-AI Tool Integration

### Phase 1: Business Discovery & Analysis
- **business-analyst**: Use Context7 for business process documentation
- **product-manager**: Use Context7 for requirement documentation generation
- **ux-designer**: Use Context7 for user journey documentation
- **reviewer**: Use both tools for comprehensive analysis

### Phase 2: Architecture & UX Design
- **software-architect**: Use Context7 for architecture documentation and diagrams
- **ux-designer**: Use Context7 for design system documentation
- **security-engineer**: Use Context7 for security policy documentation
- **data-engineer**: Use Context7 for data model and ETL documentation

### Phase 3: Development & Continuous QA
- **frontend-engineer**: Use Context7 for component generation, Serena for editing
- **api-engineer**: Use Context7 for API scaffolding, Serena for implementation
- **data-engineer**: Use Context7 for migration scripts, Serena for optimization
- **security-engineer**: Use Context7 for security configuration generation
- **qa-engineer**: Use Context7 for test suite generation, Serena for execution

### Phase 4: Deployment & Operations
- **deployment-engineer**: Use Context7 for IaC generation, Serena for configuration

### Phase 5: Monitoring & Continuous Improvement
- **All agents**: Use Context7 for documentation updates, Serena for code analysis

## 🛠️ Tool Selection Guidelines

### Use Serena When:
- ✅ Navigating existing codebase
- ✅ Making targeted code edits
- ✅ Analyzing code structure and dependencies
- ✅ Running tests and builds
- ✅ Debugging and troubleshooting
- ✅ Code review and quality analysis

### Use Context7 When:
- ✅ Generating new code from scratch
- ✅ Creating complex multi-file features
- ✅ Performing large-scale refactoring
- ✅ Migrating between versions or frameworks
- ✅ Generating documentation and configurations
- ✅ Creating test suites and mock data

### Use Both Together When:
- 🔄 **Code Generation + Refinement**: Context7 generates, Serena refines
- 🔄 **Migration + Validation**: Context7 migrates, Serena validates
- 🔄 **Scaffolding + Implementation**: Context7 scaffolds, Serena implements
- 🔄 **Documentation + Analysis**: Context7 documents, Serena analyzes

## 📋 Common Workflows

### New Feature Development
1. **business-analyst** (Context7): Generate requirement documentation
2. **software-architect** (Context7): Generate architecture documentation  
3. **frontend-engineer** (Context7): Generate component scaffolding
4. **api-engineer** (Context7): Generate API endpoints
5. **qa-engineer** (Context7): Generate test suites
6. **All agents** (Serena): Refine, debug, and optimize implementation

### Bug Fix and Maintenance
1. **reviewer** (Serena): Analyze issue and impact
2. **Relevant agent** (Serena): Navigate and fix code
3. **qa-engineer** (Serena): Run tests and validate fix
4. **deployment-engineer** (Serena): Deploy and monitor

### Major Refactoring
1. **software-architect** (Context7 + Serena): Plan and document refactoring
2. **Relevant agents** (Context7): Generate new structure
3. **All agents** (Serena): Migrate existing code
4. **qa-engineer** (Serena): Validate refactoring
5. **reviewer** (Serena): Final quality review

## 🔧 Configuration Management

### Environment Variables
```bash
# AI Tool Configuration
USE_SERENA={use_serena}
USE_CONTEXT7={use_context7}
SERENA_PROJECT_PATH=.serena/project.yml
AI_ASSISTED_DEVELOPMENT=true
```

### Project Metadata
```markdown
## AI Tools Configuration
- **serena_enabled**: {use_serena}
- **context7_enabled**: {use_context7}
- **ai_assisted_development**: true
- **preferred_ai_workflow**: {ai_workflow_preference}
```

This configuration ensures optimal collaboration between human developers, AI agents, and development tools for maximum productivity and code quality.