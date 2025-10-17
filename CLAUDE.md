# CLAUDE.md – Claude Code Multi-Agent Framework

## Project Metadata
- **project_name**: "my_name_is_claude"
- **project_description**: "Claude Code Multi-Agent Framework - AI-Driven Software Engineering"
- **project_version**: "3.10.0"
- **primary_language**: "markdown" (prompts), "python/typescript" (tooling)
- **business_domain**: "software_development_tools"
- **project_scale**: "enterprise"
- **development_stage**: "production"

## Project Overview
Fortune 500-ready development framework enabling AI-driven software engineering through intelligent agent coordination with comprehensive prompt library, multi-agent orchestration, session management, hierarchical TODO management, and MCP tools integration.

**Core Capabilities**: Comprehensive AI agents, enterprise-grade prompts with functional design, intelligent session management, hierarchical TODO orchestration, MCP tools integration (Serena, Context7, Playwright), technology-agnostic design, quality assurance framework, security & compliance, real-time monitoring & analytics, automated quality validation, comprehensive visualization systems.

**Goals**: Accelerate development, improve code quality, enhance collaboration, standardize processes, enable scalability from startup to enterprise, continuous learning and improvement.

## Technologies
**Framework**: Prompt engineering (markdown), multi-agent orchestration, session management, TodoWrite integration, MCP tools, Git integration, quality assurance

**Supported Stacks**: Frontend (React, Angular, Vue, TypeScript, JavaScript, HTML5/CSS3, PWA, wxWidgets+C++/Python), Graphics (OpenGL, Vulcan, OpenCV), Backend (Python, Node.js, Java, .NET Core, Go, Rust), APIs (REST, GraphQL, gRPC), Databases (SQL/NoSQL), Infrastructure (Docker, Kubernetes, Cloud), Testing (Jest, Pytest, Cypress), Security (OWASP, threat modeling)

## Agents and Roles

**Framework includes 45 specialized agents across 3 categories:**

### Core Agents (12)
**Strategy**: product-manager, business-analyst
**Management**: session-manager
**Architecture**: software-architect, ux-designer
**Development**: frontend-engineer, backend-engineer, api-engineer, data-engineer
**Quality**: qa-engineer, security-engineer
**Operations**: deployment-engineer

### Enterprise Agents (24)
**Advanced Operations**: sre-engineer, reliability-engineer, performance-engineer, monitoring-engineer, incident-responder, capacity-planner
**Infrastructure**: cloud-engineer, platform-engineer, database-administrator, network-architect, integration-architect, middleware-engineer, devops-architect, automation-engineer
**Governance**: enterprise-architect, compliance-auditor, governance-architect, risk-manager, reviewer
**Management**: project-owner, project-coordinator
**Analytics**: data-scientist, technical-writer
**Specialized**: mobile-developer

### Custom Agents (9)
**Graphics & Math**: graphics-3d-engineer, graphics-2d-engineer, math-specialist
**Hardware**: electronics-engineer, embedded-engineer
**Desktop & CAD**: desktop-specialist, cad-engineer, 3d-addon-developer
**Scientific**: scientific-computing-specialist

Agent competencies are defined in `.claude/agents/` directory organized in hierarchical structure (core/, enterprise/, custom/).

## Integrations
**MCP Tools**: Serena (project indexing), Context7 (context analysis), Playwright (web automation)
**Development**: Git, code quality tools, testing frameworks, build systems, deployment platforms, monitoring
**External**: Claude AI API, Git hosting, package registries, cloud services

## Model Configuration
**Intelligent Cost Optimization**: Automated model selection (Opus/Sonnet/Haiku) with 50% cost reduction through smart profile management
**Profiles**: Fast (Haiku - speed priority), Balanced (Sonnet - optimal ratio), Quality (Opus - critical decisions)
**Agent Mapping**: Complete mapping for all agents with task-specific overrides and intelligent auto-selection
**Cost Management**: Budget tracking, alerts, auto-downgrade strategies, usage analytics, ROI reporting
**Configuration**: `.claude/config/model-profiles.json`, `agent-model-mapping.json`, `cost-optimization.json`
**Documentation**: Comprehensive guide in `docs/getting-started/v3.3.0-features-guide.md`, overview in `.claude/config/INFO.md`

## Output Styles
**Context-Aware Communication**: Four specialized styles for different stakeholders and scenarios
**Styles**: Technical (developers), Executive (management), Educational (learners), Code Review (reviewers)
**Auto-Selection**: Intelligent style matching based on agent type, task, and audience
**Language Support**: English/Polish with preserved tone and structure across languages
**Configuration**: `.claude/config/output-styles.json`
**Documentation**: Comprehensive guide in `docs/getting-started/v3.3.0-features-guide.md`

## Advanced Checkpoint System
**Revolutionary State Management**: 70% reduction in development rework through intelligent rollback
**Checkpoint Levels**: Agent execution, quality gates, commit preparation, manual checkpoints
**Semantic Rewind**: Smart rollback with semantic understanding (before bug, last working state, before refactoring)
**Multi-Agent Coordination**: Per-agent checkpoints for granular rollback, workflow state preservation
**Auto-Triggers**: Before agent execution, quality gates, commits, deployments, refactoring, test failures
**Configuration**: `.claude/config/checkpoint-system.json`
**Storage**: `.claude/checkpoints/` with JSON diffs, compression, auto-cleanup

## Parallel Agent Execution
**3x Development Speed**: Concurrent multi-agent workflows with intelligent coordination
**Agent Teams**: Pre-configured teams (Full-Stack, Architecture, Compliance, Operations, Data)
**Smart Distribution**: Automatic workload balancing, dependency resolution, conflict detection
**Scalability**: Dynamic scaling (1-5 concurrent agents), resource optimization, budget-aware execution
**Failure Handling**: Continue on failure, retry strategies, fallback to sequential, preserve successful work
**Configuration**: `.claude/config/parallel-agents.json`
**Monitoring**: Real-time progress tracking, execution metrics, performance analytics

## Extended Thinking Mode
**Deep Reasoning System**: Structured analysis for complex decisions with documented rationale and alternatives evaluation
**5-Phase Process**: Problem analysis → Alternative generation → Evaluation → Trade-off analysis → Recommendation with confidence scores
**Trigger System**: 3-tier activation (Critical: architecture/security decisions, High-value: optimization/refactoring, Experimental: research/innovation)
**Thinking Logs**: JSON-formatted decision records with alternatives, evaluation criteria, confidence assessments, and validation metrics
**Quality Standards**: Minimum 3 alternatives, confidence thresholds (0.70-0.90), risk assessment, validation criteria
**Framework Integration**: TodoWrite coordination, checkpoint integration, quality gate analysis, diagnostic capabilities
**Configuration**: `.claude/config/extended-thinking-config.json`, `.claude/config/diagnostic-framework-integration.json`
**Storage**: `.claude/thinking-logs/` with structured JSON logs organized by agent and decision type
**Documentation**: Comprehensive guide in `docs/advanced/extended-thinking-mode.md`

## Claude Skills Architecture
**Plugin Ecosystem**: Hybrid Layered Skills architecture optimized for Claude API integration (8-skill limit per request)
**Architecture**: 1 Foundation skill (orchestration layer) + 7 domain skills (Architecture, Development, Data, Quality, Security, Operations, Custom)
**Foundation Skill**: Always-load orchestration layer with session-manager, product-manager, and business-analyst for multi-agent coordination
**Domain Skills**: Specialized skills loaded on-demand based on workflow requirements (web development, data engineering, security audit, etc.)
**Conversion**: Automated agent-to-skill converter with complete dependency mapping and collaboration pattern preservation
**Size Optimization**: Efficient structure using only 3.5% of 8MB per-skill capacity (0.28MB total for 8 skills)
**Framework Integration**: Preserves TodoWrite, Extended Thinking, CLAUDE.md adaptation, and MCP tools integration
**Configuration**: `.claude/config/skills-conversion-mapping.json`, `.claude/config/skills-dependency-mapping.json`
**Output**: `work/skills-output/` with production-ready skills validated against Claude API requirements
**Status**: Prototype complete with 30/32 agents converted (93.8% coverage), 100% structure validation, ready for API upload

## Requirements
**Performance**: <2s prompt response, parallel execution, <5s context loading, optimized memory
**Scalability**: Multi-project support, agent extensibility, unlimited prompts, 1-1000+ users
**Reliability**: 99.9% session recovery, graceful degradation, data integrity, fault tolerance
**Security**: No hardcoded secrets, safe code generation, access control, data protection, audit trail

## Framework Guidelines
**Constraints**: Open-source preference, platform agnostic (Windows/macOS/Linux), minimal dependencies, Claude AI optimized
**Style**: Readability first, functional design (WHAT not HOW), consistent naming, comprehensive documentation
**Agent Rules**: English files, Polish/English conversations, no quantitative documentation, professional communication, specific error handling, clear collaboration, enterprise quality

## File Organization Rules - MANDATORY
**CRITICAL**: These rules are NON-NEGOTIABLE and MUST be followed without exception:

1. **TEMPORARY AND WORKING FILES** → `/work/` directory ONLY
   - ALL temporary files, working files, test scripts, debug files
   - Scripts created during development/debugging process
   - Any file that is not permanent part of the framework
   - **NEVER create these files in project root or any other location**
2. **CONCEPTUAL AND DEVELOPMENT DOCUMENTATION** → `/project_archive/` directory ONLY
   - Conceptual files, implementation reports, development notes
   - Execution reports, analysis documents, research findings
   - Development files, design documents, implementation guides
   - **ALL non-code documentation that describes development process**
3. **CLARIFYING INTENT** → ALWAYS ask clarifying questions whenever it is less than 90% confident in user intent

**VIOLATION OF THESE RULES IS UNACCEPTABLE AND MUST BE IMMEDIATELY CORRECTED**

## TODO Management
**Core**: Hierarchical system with TodoWrite integration, agent coordination, auto task creation, enterprise tracking
**Levels**: Epic (business-analyst, product-manager) → Feature (architects) → Task (engineers) → Subtask (detailed)
**Scale Templates**:
- **Startup**: Simple hierarchy, session tracking
- **SME**: Full hierarchy, milestone tracking
- **Enterprise**: Complete system + external integration

## Project Ownership
**Team**: Bartosz Warzocha & 'My Name Is Clode' Claude Code Multi-Agent Framework Team with distributed AI agent architecture
**Interface**: Claude Code CLI, comprehensive documentation, TodoWrite integration, Git-based collaboration
**Governance**: Continuous improvement, automated quality control, security oversight, performance monitoring

## Roadmap Management
**Priority Structure**: 🚨 CRITICAL → 🔥 HIGH → ⭐ MEDIUM → 🔮 LOW
**Categories**: Agents, Prompts, Configuration, Workflows, Analytics, Integrations, UX
**Standards**: Priority-based (no timelines/versions), functional descriptions, business value, integration requirements, quality compliance
**Process**: Assess value → evaluate complexity → assign priority → categorize → document requirements

## Maintenance Rules
**Auto Operations**: Agent/prompt/hook changes trigger documentation updates, badge standards (orange: framework, green: enterprise, blue: license)
**Triggers**: Component changes → doc updates, batch operations → consolidated updates, rule changes → compliance validation
**Quality**: Framework rule compliance, quantitative data elimination, agent-prompt binding integrity, technology agnostic preservation

---

## Command-Agent Mapping
**Core Commands**: Session (save/restore/start), Project (health check/new/release), Business (analysis/requirements), Product (planning/MVP), Development (frontend/backend/API), Quality (tests/security), Architecture (design/deployment)
**Rules**: Polish/English support, context awareness, fuzzy matching, multi-command handling, Serena MCP integration, intelligent recognition

## Prompt Development
**Functional Approach**: WHAT not HOW, technology-agnostic patterns, validation criteria, template examples only, CLAUDE.md adaptability
**Forbidden**: Hardcoded file paths, technology lock-in, implementation code embedding, tool-specific commands
**Structure**: 1) Functional requirements, 2) High-level algorithms, 3) Validation criteria, 4) Usage examples
**Languages**: English files, Polish/English conversations, no quantitative documentation

### ❌ HARDCODING VIOLATIONS - STRICTLY FORBIDDEN

**These practices will cause prompt rejection and require immediate rewrite:**

**Forbidden Practices:**
1. **File Path Hardcoding** - No hardcoded directories without detection
2. **Technology Lock-in** - No framework assumptions without adaptation
3. **Implementation Code** - No complete production-ready code
4. **Tool Commands** - No hardcoded commands without alternatives

### 🔄 RUNTIME CODE GENERATION PROCESS

**All agents must follow this adaptive process:**

**4-Phase Process:**
1. **Project Analysis** - Read CLAUDE.md, detect technology stack, analyze patterns
2. **Context Adaptation** - Customize to project requirements and standards
3. **Code Generation** - Create tailored implementations with validation
4. **Quality Assurance** - Verify compatibility and integration

### 🎯 PROMPT QUALITY STANDARDS

**Every prompt must meet these enterprise-grade standards:**

- **Clarity**: Unambiguous instructions and expected outcomes
- **Completeness**: All necessary information for successful execution
- **Consistency**: Aligned with framework standards and conventions
- **Adaptability**: Works across different technology stacks and project sizes
- **Maintainability**: Easy to update and extend without breaking changes
- **Performance**: Efficient execution with minimal resource consumption
- **Error Handling**: Robust error detection and recovery mechanisms

### 📋 **MANDATORY PROMPT STRUCTURE**

**Every prompt MUST contain these 4 components:**

**4 Required Components:**
1. **FUNCTIONAL REQUIREMENTS** - What needs to be accomplished
2. **HIGH-LEVEL ALGORITHMS** - How to approach the problem
3. **VALIDATION CRITERIA** - What conditions must be met
4. **USAGE EXAMPLES** - Cross-technology scenarios

### 📋 **LANGUAGE AND DOCUMENTATION STANDARDS**

**MANDATORY LANGUAGE RULES for all framework components:**

#### **1. File Content Language**
- **All framework files** (prompts, documentation, code) MUST be written in **English**
- **File names** and **directory names** MUST be in **English**
- **Comments in code** MUST be in **English**
- **Technical documentation** MUST be in **English**

#### **2. Conversation Language**
- **Conversations with users** can be in **Polish or English** based on user preference
- **Adapt to user's language** - respond in the language user initiated conversation
- **Technical terms** should use English terminology even in Polish conversations
- **Framework names and components** remain in English regardless of conversation language

#### **3. Documentation Quantitative Information**
- **NEVER use quantitative information** in documentation files (README.md, guides, etc.)
- **Avoid specific numbers** like "44 prompts", "5 agents", "10 files"
- **Use descriptive terms** instead: "comprehensive prompts", "specialized agents", "complete coverage"
- **Exception**: Version numbers, dates, and technical specifications are allowed

**Examples**: Use "comprehensive prompts" not "44 prompts", "specialized agents" not "11 agents"

#### **4. Directory Tree Documentation Standards**
- **ALWAYS use actual filesystem structure** - never use outdated or assumed directory listings
- **One level deep only** - show only top-level directories within each folder being documented
- **Include direct files** - list files that exist directly in the documented folder
- **Real-time verification** - use `ls`, `tree`, or file system tools to verify actual structure before documentation
- **Complete accuracy** - every listed directory and file MUST actually exist in the filesystem
- **No assumptions** - never assume directory structure based on previous knowledge or templates

**Process**: Always verify actual structure with `ls`, show one level deep only, update based on filesystem reality

**CRITICAL REMINDER**: After creating new directories (like `.claude/commands/`), ALWAYS update README.md directory tree to reflect the new structure. Check for missing directories in all documentation before any release or major update.

#### **5. Consistency Requirements**
- **Maintain consistency** between English files and Polish conversations
- **Use established terminology** from framework specification
- **Preserve technical accuracy** across language boundaries
- **Document language choices** in project configuration when relevant

### ✅ **ACCEPTABLE CODE EXCEPTIONS**

**These cases are ACCEPTABLE when meeting specified conditions:**

**Acceptable Code Types:**
1. **Configuration Templates** - Clearly marked as adaptable examples
2. **Pattern Examples** - Framework-agnostic patterns for customization
3. **Generic Utilities** - Universal functions not tied to specific structures
4. **Universal Templates** - Industry-standard configurations
5. **User-Requested** - When explicitly requested by user

**MANDATORY CONDITIONS for acceptable code:**
- **Clear labeling** as TEMPLATE/PATTERN/EXAMPLE/UTILITY/COMMON/USER-REQUESTED
- **Adaptation instructions** - how to customize for specific projects
- **Genericity** - doesn't assume specific project structure (except Common Templates)
- **Optional nature** - prompt works without the code
- **User context** - for User-Requested, must be response to explicit user request for code

### ❌ **STRICTLY FORBIDDEN PRACTICES**

1. **Hardcoded file paths**: `.claude/`, `src/main/java/` (without TEMPLATE marking)
2. **Rigid directory structures**: `mkdir -p .serena/{index,cache}` (without adaptation)
3. **Production-ready implementations**: Complete components without customization options
4. **Tool-specific commands**: `serena onboarding`, `pytest /path/` (without detection/fallback)
5. **Technology lock-in**: Assumptions about specific frameworks without detection

### 🔧 **PROMPT UPDATE AND REPAIR PROCESS**

**When updating or repairing existing prompts, MANDATORY process:**

**4-Phase Repair Process:**
1. **Business Analysis** - Understand original purpose and value proposition
2. **Compliance Assessment** - Check structure, identify violations, assess adaptability
3. **Functionality-Preserving Rewrite** - Apply 4-component structure while preserving business value
4. **Validation** - Verify functionality, structure compliance, and integration compatibility

**Success Criteria**: Preserve business functionality, achieve structure compliance, maintain technology agnostic design, keep integration compatibility
**Failure Indicators**: Lost functionality, broken integrations, reduced effectiveness, missing unique value

---

## Component Creation Standards

**Template-Driven Development**: All new framework components must follow established templates to ensure consistency, quality, and integration.

### Agent Creation
**Template**: `.claude/templates/agent_template.md`
**Requirements**: 8 mandatory sections, enterprise-grade quality, TodoWrite integration, CLAUDE.md adaptation
**Process**: Copy template → customize placeholders → validate structure → test integration

### Prompt Creation
**Template**: `.claude/templates/prompt_template.md`
**Requirements**: 4 mandatory components, technology-agnostic design, quality gates compliance, functional approach
**Process**: Copy template → define requirements → implement examples → validate quality gates

### Quality Standards
**Agent Standards**: Professional competencies (10+ years experience), complete TODO workflow integration, automatic CLAUDE.md adaptation, technology-agnostic design
**Prompt Standards**: Functional design (WHAT not HOW), cross-technology examples, hardcoding violation prevention, enterprise-grade quality

### Version Management
**Templates**: `.claude/templates/version-management/`
**Components**: Version update checklist, semantic versioning rules, changelog template, sync validator
**Process**: Automated version synchronization across all framework files with validation

### Agent-Prompt Integration
**Auto-Activation**: Prompts in `.claude/prompts/agents/[category]/` automatically activate corresponding agents
**Coordination**: Multi-agent workflows through TodoWrite integration and framework orchestration

---

## Directory Structure
```
.claude/agents/          # AI agent definitions (45 agents total)
├── core/                # Core development agents (12 agents)
├── enterprise/          # Fortune 500 enterprise agents (24 agents)
└── custom/              # Personal technology stack agents (9 agents)
    ├── graphics/        # 3D/2D graphics and math specialists
    ├── hardware/        # Embedded systems and electronics
    ├── desktop/         # wxWidgets, Qt, CAD, and Blender development
    └── scientific/      # Scientific computing and analysis
.claude/prompts/
├── init/                # Project initialization prompts
├── agents/              # Agent-specific prompts (auto-binding)
├── workflows/           # Multi-agent orchestration
└── tools/               # Framework utility and maintenance prompts
.claude/docs/            # Framework documentation
.claude/config/          # Advanced configuration systems
├── model-profiles.json                      # Fast/Balanced/Quality profiles
├── agent-model-mapping.json                 # Agent-to-model mappings
├── cost-optimization.json                   # Budget and optimization settings
├── output-styles.json                       # Communication style definitions
├── checkpoint-system.json                   # Advanced state management
├── parallel-agents.json                     # Concurrent execution configuration
├── extended-thinking-config.json            # Extended Thinking triggers and thresholds
├── diagnostic-framework-integration.json    # Extended Thinking framework integration
├── skills-conversion-mapping.json           # Agent-to-Skill conversion mapping
├── skills-dependency-mapping.json           # Cross-skill collaboration patterns
└── INFO.md                                  # Configuration overview and guide pointer
.claude/checkpoints/      # Checkpoint storage (gitignored, contains .gitkeep)
.claude/thinking-logs/    # Extended Thinking logs (gitignored, diagnostic artifacts)
.claude/templates/       # Configuration templates
│   ├── version-management/  # Version management system templates
.claude/hooks/           # Automation scripts

.ai-tools/               # AI-Powered Development Tools
├── core/                # Core AI components and logic
│   ├── bin/             # Executable scripts and analyzers
│   ├── core/            # Technology detection and analysis
│   ├── demo/            # Demonstrations and tutorials
│   ├── discovery/       # Agent discovery system
│   ├── integration/     # Framework integration layer
│   └── models/          # System models and interfaces
├── discovery/           # Agent discovery tools
├── setup/               # Installation and configuration tools
│   └── templates/       # Setup template system
├── templates/           # Project templates and generators
└── validation/          # Quality validation tools

project_archive/         # Project documents and research
├── designs/             # Technical design documents
├── implementations/     # Implementation summaries
├── roadmaps/           # Historical roadmaps
└── research/           # Research notes and session files

docs/                   # Comprehensive framework documentation
├── getting-started/    # Installation and quick start guides
├── ai-tools/          # AI tools step-by-step guides
├── workflows/         # Development workflows
├── advanced/          # Advanced configuration
├── reference/         # Technical reference documentation
├── examples/          # Real-world implementation examples
└── architecture/      # System architecture and design

project_archive/         # Project documents and session files (local only)
├── backups/             # System backups
├── sessions/            # Session management files (gitignored)
├── tools/               # Utility scripts and temporary tools (gitignored)
├── designs/             # Technical design documents
├── implementations/     # Implementation summaries
├── roadmaps/           # Historical roadmaps
└── research/           # Research notes and session files

examples/              # Real-world implementation examples
/work/                 # Temporary files (gitignored)
```

## Framework Status
**Components**: Comprehensive AI agents, enterprise-grade prompts, agent-prompt binding, workflow orchestration, session management, project governance, model configuration, output styles, checkpoint system, parallel execution, Extended Thinking mode, Claude Skills architecture
**Quality**: 100% functional compliance, zero hardcoding violations, complete technology stack adaptability, CLAUDE.md integration, enterprise-grade standards, cost optimization ready, deep reasoning capabilities, plugin ecosystem readiness
**Achievements**: Session management (100% complete), agent implementation prompts (high quality), perfect structural compliance, intelligent cost optimization (70% savings), context-aware communication system, advanced state management architecture, parallel agent execution framework, Extended Thinking system with 5-phase analysis, Skills architecture with 8 production-ready skills

## Version History
**Current**: 3.10.0 (Phase 0: Pre-Skills Foundation - Extended Thinking & Skills Architecture)
**Created**: 2025-09-11
**Major Milestones**: Framework foundation (v2.0.0), agent-prompt integration optimization (v2.1.0), AI tools migration (v2.2.0), documentation reorganization and optimization (v3.0.0), comprehensive quality systems and analytics (v3.1.0), ML dependencies cleanup and system optimization (v3.2.0), performance optimization and comprehensive fixes (v3.2.1), cost optimization and advanced capabilities (v3.3.0), intelligent model configuration system (v3.6.0), advanced checkpoint system and context-aware output styles (v3.7.0), parallel agent execution system (v3.8.0), Haiku 4.5 model integration for 70% cost optimization (v3.9.0), Extended Thinking mode and Claude Skills architecture (v3.10.0)
**Status**: Production-ready cost optimization (70% API savings with Haiku 4.5), context-aware communication (4 styles), advanced checkpoint architecture (70% rework reduction), parallel agent execution framework (3x speed potential), Extended Thinking system with deep reasoning (5-phase analysis), Claude Skills architecture (8 production-ready skills), comprehensive configuration system

---

*Claude Code agents automatically adapt their competencies based on this configuration file.*
