**🤖 AGENT ACTIVATION:** This prompt automatically activates the `project-owner` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# New Project Framework Initialization

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Initialize a new project with Claude Code Multi-Agent Framework by analyzing existing project context, interactively gathering missing requirements, and automatically establishing framework configuration, directory structure, and development environment. Enable seamless integration of the framework into any existing or greenfield project while preserving existing work and adapting to detected technology patterns.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Existing Project Context Discovery
1. **Analyze current directory structure** - Detect existing project files, folders, and organization patterns
2. **Identify technology stack indicators** - Scan for package.json, requirements.txt, pom.xml, *.csproj, go.mod, Cargo.toml
3. **Detect existing configuration files** - Find build configs, CI/CD files, Docker files, database configs
4. **Assess project maturity** - Evaluate existing codebase size, complexity, and development stage
5. **Identify integration constraints** - Detect existing tools, frameworks, and architectural patterns

### Phase 2: Interactive Requirements Gathering
1. **Present discovered context** - Show detected technologies, structure, and project characteristics
2. **Request missing critical information** - Ask only for information that cannot be auto-detected:
   - Project name (if not evident from directory or package files)
   - Business domain (if not clear from codebase context)
   - Project scale (startup/sme/enterprise based on complexity and goals)
   - TODO management preferences (simple/hierarchical based on team size)
3. **Confirm technology stack choices** - Validate detected primary language and frameworks
4. **Gather agent preferences** - Determine which of 14 agents are needed for project scope
5. **Configure quality requirements** - Set performance, security, scalability standards based on project scale

### Phase 3: Framework Integration and Structure Creation
1. **Create CLAUDE.md configuration** - Generate framework configuration based on gathered requirements
2. **Establish .claude directory structure** - Create agents/, prompts/, docs/, templates/, hooks/ directories
3. **Generate technology-appropriate project structure** - Create directories based on detected/selected stack:
   - Frontend projects: src/, components/, assets/, public/
   - Backend projects: src/, lib/, tests/, docs/
   - Full-stack: separate frontend/backend or monorepo structure
   - Libraries: lib/, examples/, tests/, docs/
4. **Initialize development environment files** - Create appropriate config files:
   - Package management (package.json, requirements.txt, pom.xml, etc.)
   - Build tools (webpack.config.js, vite.config.ts, build.gradle, etc.)
   - Testing frameworks (jest.config.js, pytest.ini, etc.)
   - Code quality (eslint, prettier, pre-commit hooks)
5. **Configure version control integration** - Setup .gitignore, README.md, and framework-aware git hooks

### Phase 4: Development Environment Validation and Handoff
1. **Validate framework integration** - Test CLAUDE.md configuration completeness and agent accessibility
2. **Verify development environment** - Ensure build tools, dependencies, and tooling work correctly
3. **Test agent coordination setup** - Validate TODO management and agent communication patterns
4. **Generate initialization report** - Document what was created, configured, and next steps
5. **Provide next steps guidance** - Recommend first agents to engage and development workflow to follow

## 3. ✅ VALIDATION CRITERIA

### Project Detection and Analysis Completeness
- **Technology stack accurately identified** - Primary language and frameworks correctly detected
- **Existing structure preserved** - No existing project files or directories damaged or overwritten
- **Project scale appropriately assessed** - Startup/SME/enterprise classification matches complexity
- **Integration constraints respected** - Framework integration works with existing tools and patterns
- **Missing requirements identified** - Only essential undetectable information requested from user

### Framework Configuration Success
- **CLAUDE.md properly generated** - All required sections populated with project-specific information
- **Agent selection optimized** - Chosen agents align with project needs and development phases
- **TODO management configured** - Complexity level matches team size and project management needs
- **Quality standards appropriate** - Performance, security, scalability requirements match project scale
- **Technology integration coherent** - All configured technologies work together effectively

### Development Environment Readiness
- **Directory structure follows best practices** - Organization appropriate for detected technology stack
- **Build and dependency management working** - All configuration files properly created and functional
- **Development tools integrated** - Testing, linting, formatting tools configured and operational
- **Version control ready** - Git integration with appropriate ignores and framework awareness
- **Agent communication enabled** - Framework can successfully coordinate multi-agent workflows

## 4. 📚 USAGE EXAMPLES

### Existing React TypeScript Web Application
**Detected Context**: package.json with React, TypeScript, existing src/ directory with components
**User Interaction**:
- Confirmed business domain: "e-commerce"
- Selected project scale: "startup"
- Enabled TODO management: "simple"
**Generated Structure**:
- CLAUDE.md with typescript/react configuration
- Agents: frontend-engineer, api-engineer, qa-engineer
- Enhanced package.json with framework scripts
- .claude/ directory with selected agent configs

### Greenfield Python API Project
**Detected Context**: Empty directory, user indicates Python preference
**User Interaction**:
- Project name: "inventory-api"
- Business domain: "business_process_automation"
- Project scale: "sme"
- TODO management: "hierarchical"
**Generated Structure**:
- Complete Python project structure (src/, tests/, requirements.txt)
- CLAUDE.md with Python/FastAPI configuration
- Agents: business-analyst, backend-engineer, api-engineer, qa-engineer
- Pre-commit hooks and testing framework setup

### Legacy Java Enterprise Integration
**Detected Context**: Existing Maven project with Spring Boot, complex directory structure
**User Interaction**:
- Business domain: "healthcare" (detected from existing packages)
- Project scale: "enterprise" (confirmed based on complexity)
- TODO management: "hierarchical" with enterprise reporting
**Generated Structure**:
- CLAUDE.md preserving existing Maven structure
- Agents: software-architect, security-engineer, backend-engineer, deployment-engineer
- Framework integration without disrupting existing build process

### Mobile React Native Project
**Detected Context**: package.json with React Native dependencies, ios/ and android/ directories
**User Interaction**:
- Business domain: "mobile_application"
- Project scale: "startup"
- Focus on rapid MVP development
**Generated Structure**:
- CLAUDE.md with React Native/mobile configuration
- Agents: ux-designer, frontend-engineer, qa-engineer
- Mobile-specific testing and deployment configurations

### Multi-Service Microservices Architecture
**Detected Context**: Multiple service directories, Docker Compose, Kubernetes configs
**User Interaction**:
- Business domain: "financial_services"
- Project scale: "enterprise"
- TODO management: "hierarchical" with cross-service coordination
**Generated Structure**:
- CLAUDE.md with microservices architecture configuration
- Agents: software-architect, api-engineer, security-engineer, deployment-engineer, qa-engineer
- Service-specific framework integration maintaining existing orchestration

---

## 🎯 EXECUTION APPROACH

**Interactive Workflow**:
1. **Analyze current project context** - Scan directory and detect existing patterns automatically
2. **Present findings and gather requirements** - Show detected information and ask for missing details
3. **Generate framework configuration** - Create CLAUDE.md and directory structure based on requirements
4. **Initialize development environment** - Set up build tools, dependencies, and quality tools
5. **Validate and report** - Ensure everything works correctly and provide next steps

**Adaptive Behavior**:
- **Greenfield projects**: Create complete structure from scratch with best practices
- **Existing projects**: Integrate framework while preserving existing organization and tools
- **Legacy projects**: Careful integration with minimal disruption to existing workflows
- **Multi-technology projects**: Detect and configure for multiple languages/frameworks appropriately

**Success Deliverables**:
- **Fully configured CLAUDE.md** - Ready for multi-agent development workflows
- **Integrated development environment** - Build tools, testing, quality checks operational
- **Framework directory structure** - .claude/ with all necessary agent and prompt configurations
- **Initialization report** - Documentation of changes made and recommended next steps