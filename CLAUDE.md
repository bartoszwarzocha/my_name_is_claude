# CLAUDE.md – Claude Code Multi-Agent Framework Specification

## 0. Project Metadata

- **project_name**: "my_name_is_claude"
- **project_description**: "Claude Code Multi-Agent Framework - Advanced Development Framework for AI-Driven Software Engineering"
- **project_version**: "2.1.0"
- **framework_version**: "2.1.0"
- **last_updated**: "2025-09-15"
- **primary_language**: "markdown" (prompts), "python/typescript" (tooling)
- **business_domain**: "software_development_tools"
- **project_scale**: "enterprise"
- **development_stage**: "production"

## 1. Project Description

The Claude Code Multi-Agent Framework is an advanced, enterprise-grade development framework that enables AI-driven software engineering through intelligent agent coordination. This framework provides a comprehensive prompt library, multi-agent orchestration system, and intelligent session management for automated software development workflows.

Key capabilities include:
- **11 Specialized AI Agents** for different aspects of software development
- **65+ Professional Prompts** covering complete development lifecycle
- **Intelligent Session Management** with automatic state recovery and context analysis
- **Hierarchical TODO Management** with enterprise-grade task orchestration
- **MCP Tools Integration** (Serena, Context7, Playwright) for enhanced automation
- **Technology-Agnostic Design** adaptable to any development stack
- **Quality Assurance Framework** with continuous validation and improvement

---

## 2. Domains and Goals

### Business Domains
- **AI-Driven Software Development**: Automated code generation, architecture design, testing
- **Prompt Engineering**: Advanced prompt design patterns for software engineering tasks
- **Workflow Orchestration**: Multi-agent coordination and task management
- **Quality Assurance**: Automated validation, testing, and continuous improvement
- **Session Management**: Intelligent context preservation and state recovery
- **Documentation Automation**: Comprehensive documentation generation and maintenance

### Main Project Goals
- **Accelerate Development**: Reduce development time through intelligent automation
- **Improve Code Quality**: Ensure consistent, high-quality code through AI-driven reviews
- **Enhance Collaboration**: Seamless multi-agent coordination and handoffs
- **Standardize Processes**: Consistent development workflows across projects
- **Enable Scalability**: Framework adaptable from startup to enterprise scale
- **Continuous Learning**: Framework improves through usage and feedback patterns

---

## 3. Technologies

### Core Framework Technologies
- **Prompt Engineering**: Markdown-based prompt library with functional design patterns
- **Multi-Agent Orchestration**: Claude Code agent coordination and workflow management
- **Session Management**: Advanced context analysis, state recovery, and continuation systems
- **TodoWrite Integration**: Hierarchical task management with enterprise-grade tracking
- **MCP Tools Integration**: Serena (project indexing), Context7 (context analysis), Playwright (web automation)
- **Git Integration**: Advanced version control integration with automated change tracking
- **Quality Assurance**: Automated validation, testing frameworks, and continuous improvement

### Supported Development Stacks
- **Frontend Technologies**: React, Angular, Vue.js, TypeScript, JavaScript, HTML5/CSS3, PWA
- **Backend Technologies**: Python (FastAPI, Django), Node.js (Express), Java (Spring Boot), .NET Core, Go, Rust
- **API Technologies**: REST APIs, GraphQL, OpenAPI/Swagger, Microservices, gRPC
- **Database Technologies**: PostgreSQL, MySQL, MongoDB, Redis, SQLAlchemy, Entity Framework
- **Infrastructure & DevOps**: Docker, Kubernetes, AWS, Azure, GCP, CI/CD pipelines, Terraform
- **Testing & Quality**: Jest, Pytest, Cypress, SonarQube, automated testing frameworks
- **Security**: OWASP compliance, threat modeling, penetration testing, secure code review

---

## 4. Agents and Roles

The list of available agents and their competency scope is defined in files:

### Core Strategy and Planning

- **product-manager** - Product strategy, requirements gathering, stakeholder management
- **business-analyst** - Business process analysis, requirements documentation, stakeholder communication
- **reviewer** - Quality assurance, requirements validation, risk assessment

### Architecture and Design

- **software-architect** - System architecture, technology selection, scalability planning
- **ux-designer** - User experience design, design systems, accessibility, user research

### Development

- **frontend-engineer** - User interface development, responsive design, performance optimization
- **api-engineer** - API design, microservices, service integration, distributed systems
- **data-engineer** - Data architecture, ETL pipelines, analytics, database optimization

### Quality and Security

- **qa-engineer** - Test automation, quality processes, performance testing, continuous improvement
- **security-engineer** - Application security, threat modeling, compliance, security architecture

### Operations

- **deployment-engineer** - DevOps, CI/CD pipelines, infrastructure automation, monitoring

Each agent's competency scope is located in the corresponding file in the `.claude/agents` directory. If you want to add a new agent or modify a role, edit the appropriate agent file.

---

## 5. Integrations and Dependencies

### Framework-Specific Integrations
- **MCP Tools Suite**:
  - **Serena**: Project indexing, context management, and intelligent project navigation
  - **Context7**: Advanced context analysis, pattern recognition, and semantic understanding
  - **Playwright**: Web automation, testing, and browser-based development tasks

### Development Ecosystem Integration
- **Version Control**: Advanced Git integration with automated change tracking and branch management
- **Code Quality**: SonarQube, ESLint, Prettier, and other quality assurance tools
- **Testing Frameworks**: Jest, Pytest, Cypress, Testing Library, and automated testing suites
- **Build Systems**: Webpack, Vite, Maven, Gradle, npm/yarn, and modern build toolchains
- **Deployment Platforms**: Docker, Kubernetes, AWS, Azure, Vercel, Netlify
- **Monitoring & Analytics**: Application performance monitoring, logging, and metrics collection

### External Service Dependencies
- **Claude AI API**: Core AI capabilities for agent intelligence and natural language processing
- **Git Hosting**: GitHub, GitLab, Bitbucket integration for repository management
- **Package Registries**: npm, PyPI, Maven Central, NuGet for dependency management
- **Cloud Services**: AWS S3, Azure Blob, Google Cloud Storage for asset management

---

## 6. Non-functional Requirements

### Performance Requirements
- **Prompt Response Time**: < 2 seconds for complex multi-agent prompts
- **Agent Coordination**: Parallel execution capabilities for independent tasks
- **Context Loading**: Efficient project analysis and context restoration (< 5 seconds)
- **Memory Usage**: Optimized context management to prevent memory bloat
- **Throughput**: Support for concurrent multi-agent workflows without degradation

### Scalability Requirements
- **Multi-Project Support**: Framework reusable across unlimited projects simultaneously
- **Agent Extensibility**: Easy addition of new specialized agents without core changes
- **Prompt Library Growth**: Modular architecture supporting 100+ prompts efficiently
- **User Base**: Support from individual developers to enterprise teams (1-1000+ users)
- **Workflow Complexity**: Handle simple tasks to complex multi-week project orchestration

### Reliability Requirements
- **Session Recovery**: 99.9% success rate in state restoration after interruptions
- **Error Handling**: Graceful degradation when external tools (MCP) are unavailable
- **Data Integrity**: Guaranteed consistency in TODO management and session state
- **Fault Tolerance**: Continue operations even if individual agents encounter errors
- **Backup & Recovery**: Automatic session backup and multi-point recovery options

### Security Requirements
- **No Hardcoded Secrets**: Dynamic configuration detection and secure credential management
- **Safe Code Generation**: All generated code validated and sanitized before execution
- **Access Control**: Controlled framework modification with permission-based agent access
- **Data Protection**: Secure handling of project data and intellectual property
- **Audit Trail**: Comprehensive logging of all agent actions and system modifications

---

## 7. Special Notes

### Technological Constraints
- **Open Source Preference**: Prioritize open-source solutions for maximum compatibility and transparency
- **Platform Agnostic**: Framework must work across Windows, macOS, and Linux environments
- **Minimal External Dependencies**: Core framework should work with minimal external tool requirements
- **Claude API Dependency**: Framework specifically designed for Claude AI capabilities and limitations

### Coding Style Preferences
- **Readability First**: All code and prompts must prioritize clarity and maintainability
- **Functional Design**: Prompts must use functional descriptions rather than implementation specifics
- **Consistent Naming**: Follow established naming conventions across all framework components
- **Documentation Standards**: Every prompt and agent must include comprehensive documentation

### Special Guidelines for Agents
- **File Language Standard**: ALL framework files (prompts, documentation, code) MUST be written in English
- **Conversation Language**: Conversations with users can be in Polish or English based on user preference
- **Documentation Standards**: NEVER use quantitative information in documentation (avoid "X prompts", "Y agents")
- **Communication Style**: Professional, concise, and action-oriented communication
- **Error Handling**: Always provide specific, actionable error messages and recovery suggestions
- **Collaboration Protocol**: Agents must clearly communicate handoffs and dependencies
- **Quality Standards**: Every agent output must meet enterprise-grade quality requirements

---

## 8. TODO Management Configuration

### Task Management Strategy

- **todo_management_enabled**: true (Active hierarchical TODO management system)
- **todo_hierarchy_level**: hierarchical (Enterprise-grade complexity management)
- **auto_task_creation**: true (Intelligent task breakdown by specialized agents)
- **progress_tracking**: enterprise (Comprehensive tracking across all framework development)

### TodoWrite Integration

- **session_todos**: true (TodoWrite manages all immediate session tasks and progress)
- **agent_coordination**: true (All agents coordinate through shared TODO system)
- **task_handoffs**: true (Seamless automatic handoffs between specialized agents)

### Hierarchical TODO System Configuration

- **epic_management**: true (Epic-level framework development initiatives)
- **feature_breakdown**: true (Feature-level component development and improvements)
- **task_granularity**: detailed (Comprehensive task breakdown for quality assurance)
- **subtask_tracking**: true (Granular tracking for complex multi-agent workflows)

### Agent TODO Responsibilities

**Epic Level (Business Strategy):**
- **epic_owners**: [business-analyst, product-manager] - responsible for Epic creation and management
- **epic_validation**: [reviewer] - validates Epic definitions and business value

**Feature Level (Architecture):**
- **feature_owners**: [software-architect, ux-designer, security-engineer] - break Epics into Features
- **feature_coordination**: [true/false] - coordinate Feature dependencies across agents

**Task Level (Implementation):**
- **task_owners**: [frontend-engineer, api-engineer, data-engineer, qa-engineer] - execute Tasks
- **task_estimation**: [true/false] - agents provide time estimates for Tasks
- **task_dependencies**: [true/false] - track dependencies between Tasks

**Subtask Level (Execution):**
- **subtask_auto_creation**: [true/false] - agents automatically break Tasks into Subtasks
- **subtask_completion_tracking**: [true/false] - track individual Subtask completion

### Progress Reporting

- **daily_standups**: [true/false] - generate daily progress reports
- **weekly_summaries**: [true/false] - weekly progress and velocity reports
- **milestone_tracking**: [true/false] - track major project milestones
- **burndown_charts**: [true/false] - generate burndown and velocity metrics

### Integration Settings

- **external_tools**: [none/jira/asana/trello/other] - integrate with external project management
- **notification_system**: [true/false] - enable TODO status change notifications
- **automation_hooks**: [true/false] - use .claude/hooks for TODO automation
- **api_integration**: [true/false] - expose TODO data via API for external tools

### TODO Management Templates

**For Startup Projects (project_scale: startup):**
```yaml
todo_management_enabled: true
todo_hierarchy_level: simple
auto_task_creation: true
progress_tracking: session
session_todos: true
agent_coordination: true
epic_management: false
feature_breakdown: true
task_granularity: standard
```

**For SME Projects (project_scale: sme):**
```yaml
todo_management_enabled: true
todo_hierarchy_level: hierarchical
auto_task_creation: true
progress_tracking: project
session_todos: true
agent_coordination: true
epic_management: true
feature_breakdown: true
task_granularity: detailed
milestone_tracking: true
```

**For Enterprise Projects (project_scale: enterprise):**
```yaml
todo_management_enabled: true
todo_hierarchy_level: hierarchical
auto_task_creation: true
progress_tracking: enterprise
session_todos: true
agent_coordination: true
epic_management: true
feature_breakdown: true
task_granularity: detailed
subtask_tracking: true
daily_standups: true
weekly_summaries: true
burndown_charts: true
external_tools: jira
api_integration: true
```

---

## 9. Contact and Project Owners

### Project Ownership
- **Framework Maintainer**: Claude Code Multi-Agent Framework Team
- **Technical Architecture**: Distributed across specialized AI agents
- **Business Strategy**: Product-manager and business-analyst agents
- **Quality Assurance**: QA-engineer and security-engineer agents

### Communication Channels
- **Primary Interface**: Claude Code CLI and agent orchestration system
- **Documentation**: Comprehensive prompt library and framework documentation
- **Issue Tracking**: Integrated with TodoWrite hierarchical task management
- **Version Control**: Git-based change management and collaboration

### Governance Structure
- **Framework Evolution**: Continuous improvement through usage analysis and feedback
- **Quality Control**: Automated validation and manual review processes
- **Security Oversight**: Regular security audits and vulnerability assessments
- **Performance Monitoring**: Continuous performance optimization and bottleneck identification

---

## 10. Prompt Development Guidelines

### ✅ FUNCTIONAL APPROACH - MANDATORY RULES

**These rules are ENFORCED across all framework prompts and agent interactions:**

1. **Functional Descriptions Only**
   - Describe **WHAT** needs to be accomplished, not **HOW** to implement it
   - Focus on outcomes, requirements, and success criteria
   - Example: ✅ "Implement user authentication with secure session management"
   - Anti-pattern: ❌ `const UserAuth: React.FC = () => { /* specific React code */ }`

2. **Technology-Agnostic Patterns**
   - Use general algorithms, architectural patterns, and design principles
   - Avoid assumptions about specific frameworks, libraries, or tools
   - Example: ✅ "Create responsive component using framework conventions"
   - Anti-pattern: ❌ "Use React hooks and Material-UI components"

3. **Validation Criteria Definition**
   - Define clear success conditions and acceptance criteria
   - Specify measurable outcomes and quality standards
   - Example: ✅ "Ensure all tests pass, code coverage >90%, performance <2s"
   - Anti-pattern: ❌ "Run pytest /specific/path/tests.py"

4. **Template Examples Only**
   - Code examples must be clearly marked as templates or patterns
   - Provide adaptable structures, not copy-paste implementations
   - Example: ✅ "Example implementation pattern: [code block marked as TEMPLATE]"
   - Anti-pattern: ❌ Complete production-ready code without adaptation guidance

5. **CLAUDE.md Configuration Adaptability**
   - Always read and adapt to project-specific CLAUDE.md configuration
   - Use project metadata to determine technology stack, scale, and requirements
   - Extract business domain, primary language, and project characteristics from CLAUDE.md
   - Adapt prompt behavior based on configured project specifications
   - Example: ✅ "Read CLAUDE.md to determine primary_language and adapt accordingly"
   - Anti-pattern: ❌ "This works for React projects" without checking CLAUDE.md

### ❌ HARDCODING VIOLATIONS - STRICTLY FORBIDDEN

**These practices will cause prompt rejection and require immediate rewrite:**

1. **File Path Hardcoding**
   - No hardcoded directories: `.claude/`, `src/main/java/`, `components/`
   - No specific file references without dynamic detection
   - No assumptions about project structure organization

2. **Technology Lock-in**
   - No assumptions about React, Spring Boot, Docker, etc. without detection
   - No framework-specific code without adaptation mechanisms
   - No tool-specific commands without fallback alternatives

3. **Implementation Code Embedding**
   - No complete classes, functions, or components in prompts
   - No production-ready code without customization guidance
   - No copy-paste solutions without contextual adaptation

4. **Tool-Specific Commands**
   - No hardcoded commands like `serena onboarding`, `pytest /path/` without detection
   - No assumptions about available tools without verification
   - No rigid toolchain dependencies without alternatives

### 🔄 RUNTIME CODE GENERATION PROCESS

**All agents must follow this adaptive process:**

1. **Project Analysis Phase**
   ```
   → Read CLAUDE.md configuration for project specifications
   → Extract technology stack, scale, and business domain from project metadata
   → Detect current project structure and development patterns
   → Identify available tools and frameworks based on CLAUDE.md
   → Analyze existing patterns and conventions
   → Determine optimal approach based on CLAUDE.md configuration
   ```

2. **Context Adaptation Phase**
   ```
   → Adjust recommendations to detected technology stack
   → Customize patterns to project-specific requirements
   → Align with established coding standards and practices
   → Consider project scale and complexity requirements
   ```

3. **Dynamic Code Generation Phase**
   ```
   → Generate tailored implementations based on analysis
   → Create context-appropriate scripts and configurations
   → Provide technology-specific examples when needed
   → Include validation and testing approaches
   ```

4. **Validation and Quality Assurance**
   ```
   → Verify compatibility with detected project setup
   → Ensure generated code follows project conventions
   → Test integration with existing systems and workflows
   → Provide rollback options and error recovery procedures
   ```

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

#### **1. FUNCTIONAL REQUIREMENTS** - What needs to be checked/accomplished
```markdown
✅ REQUIRED: "Analyze project health by evaluating code quality, test coverage,
             dependency security, and documentation completeness"

❌ MISSING: Unclear description of prompt objectives
```

#### **2. HIGH-LEVEL ALGORITHMS** - How to approach the problem
```markdown
✅ REQUIRED: "1. Discover project structure and technology stack
              2. Identify applicable quality metrics for detected technologies
              3. Run analysis using detected tools (with fallbacks)
              4. Aggregate results into comprehensive health report"

❌ MISSING: No logical execution steps provided
```

#### **3. VALIDATION CRITERIA** - What conditions must be met
```markdown
✅ REQUIRED: "SUCCESS CRITERIA:
              - All detected test suites pass (coverage >80%)
              - No critical security vulnerabilities found
              - Documentation exists for main components
              - Build process completes without errors"

❌ MISSING: No measurable success criteria defined
```

#### **4. USAGE EXAMPLES** - For different scenarios
```markdown
✅ REQUIRED: "USAGE SCENARIOS:
              - React + Jest project: Uses npm test, ESLint, security audit
              - Python + pytest: Uses pytest, mypy, bandit, documentation check
              - Java + Maven: Uses mvn test, SpotBugs, checkstyle validation"

❌ MISSING: No examples showing technology adaptability
```

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

**Examples:**
```markdown
❌ FORBIDDEN: "Framework includes 44 agent-specific prompts and 5 session management prompts"
✅ CORRECT: "Framework includes comprehensive agent-specific prompts and session management capabilities"

❌ FORBIDDEN: "Business Analysis (3 prompts)"
✅ CORRECT: "Business Analysis"

❌ FORBIDDEN: "Total of 11 specialized AI agents"
✅ CORRECT: "Specialized AI agents covering complete development lifecycle"
```

#### **4. Consistency Requirements**
- **Maintain consistency** between English files and Polish conversations
- **Use established terminology** from framework specification
- **Preserve technical accuracy** across language boundaries
- **Document language choices** in project configuration when relevant

### ✅ **ACCEPTABLE CODE EXCEPTIONS**

**These cases are ACCEPTABLE when meeting specified conditions:**

#### **1. Configuration Templates** (as examples, not rigid implementations)
```markdown
✅ ACCEPTABLE: "Example Docker configuration template:
[TEMPLATE - ADAPT TO YOUR PROJECT]
FROM node:18
WORKDIR /app
# Customize based on your project structure"
```

#### **2. Pattern Examples** (clearly marked as examples)
```markdown
✅ ACCEPTABLE: "Example React component pattern:
[PATTERN EXAMPLE - CUSTOMIZE FOR YOUR NEEDS]
const Component: React.FC = () => {
  // Your implementation here
}"
```

#### **3. Generic Utilities** (not structure-specific)
```markdown
✅ ACCEPTABLE: "Generic utility functions:
[UTILITY TEMPLATE - ADAPT TO YOUR STACK]
function validateEmail(email: string): boolean {
  // Universal validation logic
}"
```

#### **4. Common Universal Templates** (industry-standard configurations)
```markdown
✅ ACCEPTABLE: "Standard configuration files universal across technology stacks:
[COMMON TEMPLATE - STANDARD INDUSTRY PATTERN]
# .gitignore template
node_modules/
*.log
.env
.DS_Store

# Basic Dockerfile template
FROM alpine:latest
WORKDIR /app
COPY . .
# Customize based on your technology stack"
```

#### **5. User-Requested Code Templates** (explicit user requests for examples)
```markdown
✅ ACCEPTABLE: "When user explicitly asks for code example or starting template:
[USER-REQUESTED TEMPLATE - CUSTOMIZE AS NEEDED]
// User requested authentication middleware example
const authMiddleware = (req, res, next) => {
  // Implement based on your auth strategy
  // Adapt to your framework (Express, Koa, etc.)
}"
```

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

#### **Phase 1: Business Functionality Analysis**
1. **Read original prompt completely** - Understand what the prompt was designed to accomplish
2. **Identify core business purpose** - Extract the fundamental business problem being solved
3. **Map functional requirements** - Document what specific outcomes the prompt delivers
4. **Analyze unique value proposition** - Understand why this prompt exists and what makes it necessary
5. **Document integration points** - Identify how this prompt works with other framework components

#### **Phase 2: Compliance Gap Assessment**
1. **Evaluate structure compliance** - Check against 4-component mandatory structure
2. **Identify hardcoding violations** - Find technology lock-ins, hardcoded paths, rigid implementations
3. **Assess adaptability gaps** - Determine where prompt fails to adapt to different projects
4. **Review validation criteria** - Check if success criteria are measurable and clear
5. **Analyze usage examples** - Verify examples show cross-technology adaptability

#### **Phase 3: Functionality-Preserving Rewrite**
1. **Preserve core business value** - Ensure original business functionality is maintained
2. **Restructure using 4-component format** - Apply mandatory structure while keeping original purpose
3. **Remove compliance violations** - Eliminate hardcoding while preserving functional intent
4. **Enhance adaptability** - Make prompt work across different technology stacks and project types
5. **Maintain integration compatibility** - Ensure prompt still works with other framework components

#### **Phase 4: Validation and Enhancement**
1. **Verify business functionality intact** - Confirm original business value is preserved
2. **Test structure compliance** - Validate 4-component format is properly implemented
3. **Validate cross-technology examples** - Ensure examples work across different stacks
4. **Check integration points** - Confirm compatibility with other framework components
5. **Enhance where beneficial** - Improve prompt effectiveness while maintaining core purpose

**CRITICAL SUCCESS CRITERIA for prompt repairs:**
- ✅ **Original business functionality preserved** - Prompt still solves the same business problem
- ✅ **Structure compliance achieved** - 4-component format properly implemented
- ✅ **Technology agnostic** - Works across all supported technology stacks
- ✅ **Integration maintained** - Compatible with other framework components
- ✅ **Enhanced effectiveness** - Improved clarity and usability while preserving original intent

**FAILURE INDICATORS to avoid:**
- ❌ **Lost business functionality** - Prompt no longer solves original business problem
- ❌ **Broken integrations** - No longer works with other framework components
- ❌ **Reduced effectiveness** - Less useful than original despite better structure
- ❌ **Missing unique value** - Generic prompt that doesn't serve specific business need

---

## 11. Agent Creation and Management Rules

### 📋 **Agent Creation Standards**

All new agents MUST follow the established framework pattern to ensure consistency, quality, and integration with the TodoWrite workflow system.

#### **Mandatory Agent File Structure**

**File Location:** `.claude/agents/[category]/[agent-name].md`

**Required YAML Header:**
```yaml
---
name: agent-name
description: Senior [role] specializing in [primary focus]. Over a decade of experience [key experience areas]. Expert in [core competencies]. Adapts to project specifications defined in CLAUDE.md, focusing on [primary outcomes].
---
```

#### **Required Content Sections**

Every agent file MUST contain these sections in this exact order:

1. **Agent Header and Core Description**
   ```markdown
   # Agent Senior [Role Name]

   You are a senior [role] with over a decade of experience [specific expertise]. Your role is to **automatically adapt to project requirements** defined in the `CLAUDE.md` file, providing optimal [domain] solutions for specific [technology/business] contexts.

   **IMPORTANT**: Always read the `CLAUDE.md` file in the project root directory at the beginning of your work to adapt your competencies to:
   - [Domain-specific requirements]
   - [Technology stack considerations]
   - [Business domain adaptation needs]
   - **TODO Management Configuration (Section 8)** - adapt [role-specific] task coordination and [role-specific] tracking
   ```

2. **TODO Management Integration (MANDATORY)**
   ```markdown
   ## 📋 TODO Management Integration

   Based on `CLAUDE.md` Section 8 configuration, this agent will automatically:

   ### [Role]-Level Task Management
   - **When `[relevant_config]: true`**: [Specific TODO responsibilities]
   - **When `auto_task_creation: true`**: [Task breakdown responsibilities]
   - **When `session_todos: true`**: [TodoWrite integration patterns]

   ### [Role]-Specific TODO Responsibilities
   ```yaml
   # [Role] Task Patterns
   if [relevant_condition]:
     1. [Step-by-step TODO workflow]
     2. [Coordination patterns]
     3. [Handoff procedures]
   ```

3. **Universal [Role] Philosophy**
   - 4 core principles specific to the role
   - Focus on outcomes and value delivery
   - Integration with framework principles

4. **Adaptive Technology Specializations**
   - Technology stack adaptation patterns
   - Business domain specializations
   - Integration requirements

5. **Core [Role] Competencies**
   - Technical competencies
   - Process competencies
   - Collaboration competencies

6. **Domain-Specific Implementations**
   - YAML examples for different business domains
   - Concrete implementation patterns

7. **[Role]-Specific Specializations**
   - Advanced techniques
   - Industry best practices
   - Quality standards

8. **Final Adaptation Reminder**
   ```markdown
   Remember: **I always check CLAUDE.md at the beginning of a project and adapt all the above [role] approaches and [competency areas] to the specific project requirements, technology stack, and business domain.**
   ```

#### **Agent Category Organization**

**Required Directory Structure:**
```
.claude/agents/
├── business/          # Business analysis and strategy
├── planner/           # Product management and planning
├── design/            # UX/UI design and user research
├── architecture/      # System architecture and design
├── frontend/          # Frontend development
├── api/               # API and backend services
├── data/              # Data engineering and analytics
├── security/          # Security engineering
├── quality/           # QA and testing
├── deployment/        # DevOps and infrastructure
└── [new-category]/    # New specialized categories as needed
```

### 🎯 **Agent Quality Standards**

#### **Mandatory Quality Requirements**

1. **CLAUDE.md Integration**
   - MUST read CLAUDE.md at start of every session
   - MUST adapt to project technology stack
   - MUST respect business domain requirements
   - MUST follow TODO Management Configuration (Section 8)

2. **TodoWrite Workflow Integration**
   - MUST integrate with hierarchical TODO system
   - MUST define clear task breakdown patterns
   - MUST specify handoff protocols
   - MUST coordinate with other agents via TODOs

3. **Functional Approach Compliance**
   - MUST use functional descriptions (WHAT, not HOW)
   - MUST be technology-agnostic in base patterns
   - MUST provide adaptation mechanisms
   - MUST avoid hardcoded implementations

4. **Professional Standard**
   - MUST represent 10+ years of expert-level experience
   - MUST provide enterprise-grade solutions
   - MUST include comprehensive competency coverage
   - MUST maintain consistency with existing agents

#### **Content Quality Standards**

1. **Completeness**
   - Comprehensive competency coverage for the role
   - Business domain adaptation examples
   - Technology stack integration patterns
   - Collaboration and handoff protocols

2. **Adaptability**
   - Works across different project scales (startup → enterprise)
   - Supports multiple technology stacks
   - Adapts to various business domains
   - Integrates with different compliance requirements

3. **Clarity and Usability**
   - Clear, actionable guidance
   - Concrete examples and patterns
   - Step-by-step workflows
   - Integration points clearly defined

### 🔧 **Agent Creation Process**

#### **Step-by-Step Creation Workflow**

1. **Identify Role Need**
   - Analyze gap in current agent coverage
   - Define unique value proposition
   - Ensure no overlap with existing agents

2. **Define Core Competencies**
   - List 3-5 core competency areas
   - Define unique technical specializations
   - Map business domain applications

3. **Create Agent Structure**
   - Use agent template structure (see above)
   - Adapt TODO Management integration
   - Define collaboration protocols

4. **Validate Quality**
   - Review against quality standards
   - Ensure CLAUDE.md integration
   - Verify TodoWrite compatibility
   - Test cross-agent coordination

5. **Integration Testing**
   - Test with existing agent workflows
   - Validate handoff protocols
   - Ensure no conflicts or overlaps

#### **Agent Template Generator**

**When creating new agents, use this template:**

```markdown
---
name: [agent-name]
description: Senior [role] specializing in [focus]. Over a decade of experience [key areas]. Expert in [core competencies]. Adapts to project specifications defined in CLAUDE.md, focusing on [outcomes].
---

# Agent Senior [Role]

[Follow complete structure as defined above]
```

### 🚫 **Agent Creation Restrictions**

#### **Forbidden Practices**

1. **No Quantitative Information**
   - Do NOT include specific numbers of tools, frameworks, years
   - Use descriptive terms: "comprehensive", "extensive", "complete"
   - Exception: "Over a decade of experience" is allowed

2. **No Technology Lock-in**
   - MUST be adaptable to multiple technology stacks
   - MUST read CLAUDE.md for technology configuration
   - MUST provide fallback patterns

3. **No Hardcoded Implementations**
   - MUST use functional descriptions
   - MUST provide adaptation guidance
   - MUST avoid copy-paste code solutions

4. **No Overlap with Existing Agents**
   - Each agent MUST have unique value proposition
   - MUST complement, not duplicate existing agents
   - MUST define clear boundaries and handoffs

### 📊 **Agent Validation Checklist**

Before adding any new agent, verify:

- [ ] Follows mandatory file structure
- [ ] Includes complete TODO Management Integration
- [ ] Reads and adapts to CLAUDE.md
- [ ] Integrates with TodoWrite workflow
- [ ] Uses functional approach patterns
- [ ] Provides enterprise-level competencies
- [ ] Includes business domain adaptations
- [ ] Defines clear collaboration protocols
- [ ] Maintains consistency with existing agents
- [ ] No quantitative information included
- [ ] Technology-agnostic base patterns
- [ ] Comprehensive quality coverage

### 🎯 **Agent Evolution and Maintenance**

#### **Ongoing Agent Management**

1. **Regular Updates**
   - Review agent effectiveness quarterly
   - Update competencies based on industry evolution
   - Maintain consistency across framework

2. **Quality Assurance**
   - Regular audits against quality standards
   - User feedback integration
   - Performance optimization

3. **Framework Alignment**
   - Ensure alignment with framework evolution
   - Update TODO Management integration as needed
   - Maintain CLAUDE.md compatibility

Remember: **Agent quality is fundamental to framework success. Every agent must represent world-class expertise while maintaining adaptability and integration with the TodoWrite workflow system.**

### 🔗 **Agent-Prompt Binding System**

To ensure seamless integration between specialized prompts and their corresponding agents, the framework implements an automatic agent activation system.

#### **Automatic Agent Activation Rules**

**Directory-Based Agent Binding:**
```
.claude/prompts/agents/[agent-category]/ → Activates corresponding agent from .claude/agents/[agent-category]/
```

**Binding Examples:**
- `.claude/prompts/agents/api/rest-api-design.md` → **Automatically activates** `api-engineer` agent
- `.claude/prompts/agents/frontend/react-component.md` → **Automatically activates** `frontend-engineer` agent
- `.claude/prompts/agents/security/threat-modeling.md` → **Automatically activates** `security-engineer` agent
- `.claude/prompts/agents/planner/mvp-scoping.md` → **Automatically activates** `product-manager` agent
- `.claude/prompts/agents/quality/performance-optimization.md` → **Automatically activates** `qa-engineer` agent

#### **Prompt Header Requirements for Agent Binding**

Every prompt in `.claude/prompts/agents/[category]/` MUST include this header:

```markdown
**🤖 AGENT ACTIVATION:** This prompt automatically activates the `[agent-name]` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.
```

#### **Agent Activation Workflow**

When any prompt from `.claude/prompts/agents/[category]/` is used:

1. **Automatic Agent Selection**
   ```yaml
   # API Development Example
   prompt_path: ".claude/prompts/agents/api/rest-api-design.md"
   detected_category: "api"
   activated_agent: "api-engineer"
   agent_file: ".claude/agents/api/api-engineer.md"

   # Product Management Example
   prompt_path: ".claude/prompts/agents/planner/mvp-scoping.md"
   detected_category: "planner"
   activated_agent: "product-manager"
   agent_file: ".claude/agents/planner/product-manager.md"

   # Quality Assurance Example
   prompt_path: ".claude/prompts/agents/quality/performance-testing.md"
   detected_category: "quality"
   activated_agent: "qa-engineer"
   agent_file: ".claude/agents/quality/qa-engineer.md"
   ```

2. **Agent Context Loading**
   - Agent reads CLAUDE.md for project adaptation
   - Agent applies TODO Management Configuration (Section 8)
   - Agent coordinates with other agents as defined

3. **Task Execution Integration**
   - Agent uses TodoWrite for task management
   - Agent follows prompt functional requirements
   - Agent applies agent-specific competencies and patterns

4. **Quality Assurance**
   - Agent ensures enterprise-grade implementation
   - Agent validates against business domain requirements
   - Agent coordinates handoffs with other agents

#### **Multi-Agent Coordination via Prompts**

**Cross-Agent Prompt Usage:**
- Prompts may reference multiple agents for complex tasks
- Primary agent (directory-based) leads coordination
- Secondary agents provide specialized input

**Example:**
```markdown
**Primary Agent:** api-engineer (from directory location)
**Coordination:** With security-engineer for API security validation
**Coordination:** With frontend-engineer for API integration patterns
```

#### **Agent-Prompt Quality Standards**

1. **Functional Alignment**
   - Prompt defines WHAT needs to be accomplished
   - Agent provides HOW based on expertise and project context
   - Integration ensures optimal technical implementation

2. **Context Adaptation**
   - Agent automatically adapts prompt execution to project technology stack
   - Agent applies business domain specialization
   - Agent follows project-specific TODO Management configuration

3. **Seamless Integration**
   - No manual agent selection required
   - Automatic context loading and adaptation
   - TodoWrite integration handled transparently

#### **Implementation Verification**

To verify proper agent-prompt binding:

```bash
# Check prompt location determines agent activation
prompt_file=".claude/prompts/agents/api/rest-api-design.md"
agent_category=$(echo $prompt_file | cut -d'/' -f4)  # "api"
activated_agent="${agent_category}-engineer"         # "api-engineer"
agent_file=".claude/agents/${agent_category}/${activated_agent}.md"

# Special mappings for non-standard naming
case "$agent_category" in
  "planner") activated_agent="product-manager" ;;  # planner → product-manager
  "quality") activated_agent="qa-engineer" ;;      # quality → qa-engineer
  *) activated_agent="${agent_category}-engineer"  # standard pattern
esac
```

This system ensures that specialized prompts always execute with appropriate agent expertise while maintaining the functional design approach and TodoWrite integration.

---

## 12. Framework Directory Structure

```
my_name_is_claude/
├── .claude/                           # Framework core directory
│   ├── agents/                        # AI agent definitions (11 agents)
│   │   ├── business/                  # Business analysis agents
│   │   ├── product/                   # Product management agents
│   │   ├── design/                    # UX/UI design agents
│   │   ├── architecture/              # System architecture agents
│   │   ├── frontend/                  # Frontend development agents
│   │   ├── api/                       # API development agents
│   │   ├── data/                      # Data engineering agents
│   │   ├── security/                  # Security engineering agents
│   │   ├── deployment/                # DevOps and deployment agents
│   │   ├── qa/                        # Quality assurance agents
│   │   └── review/                    # Code review and audit agents
│   ├── prompts/                       # Comprehensive prompt library (65+ prompts)
│   │   ├── session/                   # Session management (5 prompts) ✅
│   │   ├── project/                   # Project management (8 prompts) ⚠️
│   │   ├── agents/                    # Agent-specific prompts (44 prompts) 🚨
│   │   ├── workflows/                 # Multi-agent orchestration workflows
│   │   ├── init/                      # Project initialization and setup
│   │   └── PROMPTS_IMPLEMENTATION_CHECKLIST.md
│   ├── docs/                          # Framework documentation
│   │   ├── agent-sdlc-workflow.puml   # Development lifecycle diagrams
│   │   └── architecture/              # Architecture documentation
│   ├── templates/                     # Configuration and code templates
│   │   ├── claude/                    # Claude-specific templates
│   │   └── serena/                    # Serena MCP integration templates
│   └── hooks/                         # Automation and event hooks
├── CLAUDE.md                          # This file - Framework specification
├── README.md                          # Project overview and quick start
├── LICENSE                            # Framework licensing information
├── CHANGELOG.md                       # Version history and updates
├── VERSION                            # Current framework version
└── copilot.md                         # Additional configuration file
```

### Directory Purpose and Responsibilities

- **/.claude/agents/**: Contains 11 specialized AI agents, each with specific competency areas
- **/.claude/prompts/**: 65+ professional-grade prompts for complete development lifecycle
- **/.claude/docs/**: Comprehensive framework documentation and architecture diagrams
- **/.claude/templates/**: Reusable templates for rapid project setup and configuration
- **/.claude/hooks/**: Automation scripts and event-driven framework enhancements

---

## 12. Prompt Library Status and Quality Assessment

### 📊 Current Implementation Status

**Total Framework Components:**
- **AI Agents**: 11 specialized agents across development lifecycle
- **Prompt Library**: 65+ prompts with varying quality and implementation status
- **Workflow Orchestration**: Multi-agent coordination and handoff systems
- **Session Management**: Advanced state management and context preservation

### ✅ COMPLETED AND VALIDATED (Priority 1)

**Session Management Prompts (5/5 - 100% Complete):**
- ✅ `session-start-and-context-analysis.md` - Comprehensive session initialization
- ✅ `session-continuation-from-summary.md` - Advanced context restoration
- ✅ `session-end-and-summary-generation.md` - Intelligent session summarization
- ✅ `session-state-recovery.md` - Robust state recovery after interruptions
- ✅ `serena-sync-and-update.md` - MCP tools integration and synchronization

### 🚨 CRITICAL QUALITY ISSUES IDENTIFIED

**Project Management Prompts (0/8 - Requires Complete Functional Rewrite):**
- ❌ All 8 prompts contained hardcoded Python scripts and specific file paths
- ❌ Removed due to violations of functional design principles
- ⚠️ Need complete rewrite using functional approach defined in Section 10

**Agent Implementation Prompts (28/44 - 64% Require Major Fixes):**

*High Severity Issues (28 files - 64%):*
- **Data Layer (3/3 - 100% HIGH)**: 2,290+ lines of hardcoded Spring Boot, SQLAlchemy, Entity Framework code
- **API Layer (5/6 - 83% HIGH)**: Complete implementations of Spring Boot, Node.js GraphQL, Docker configs
- **Frontend Layer (7/10 - 70% HIGH)**: 1,452+ lines of React/Angular TypeScript, testing frameworks
- **Security Layer (4/6 - 67% HIGH)**: 1,411+ lines of Java/Spring/.NET security implementations

*Medium Severity Issues (12 files - 27%):*
- Technology-specific tool preferences and configuration assumptions
- Framework integration patterns with limited adaptability

*Acceptable Quality (4 files - 9%):*
- Proper functional descriptions with minimal hardcoding issues
- Business and planning prompts generally follow correct patterns

### 🎯 Quality Improvement Priorities

**Immediate Actions Required:**
1. **Rewrite Project Management prompts** using functional approach (Priority 2)
2. **Refactor 28 HIGH SEVERITY agent prompts** to remove hardcoded implementations
3. **Update Session Management prompts** to remove framework-specific paths
4. **Establish quality validation** process to prevent future violations

**Success Metrics:**
- **Functional Compliance**: 100% of prompts use functional descriptions
- **Technology Agnostic**: 0% hardcoded technology assumptions
- **Adaptability Score**: Framework works across all supported technology stacks
- **Maintainability Index**: Easy updates without breaking existing functionality

---

## 13. Change History

### Version History

- **Project Creation Date**: 2025-09-11
- **Current Version**: 2.1.0
- **Last Updated**: 2025-09-15
- **Framework Status**: Production-ready with revolutionary agent-prompt integration

### Version Control Integration

- **Repository**: Local development repository (my_name_is_claude)
- **Branch Strategy**: Main branch with feature development
- **Version Tags**: Semantic versioning aligned with framework releases
- **Change Tracking**: Automated through Claude Code session management

### Major Framework Milestones

**2025-09-11 - Framework Foundation (v2.0.0)**
- ✅ Initial framework architecture established
- ✅ 11 specialized AI agents defined and implemented
- ✅ Basic prompt library structure created
- ✅ Multi-agent orchestration system designed

**2025-09-15 - Framework Optimization & Agent-Prompt Integration (v2.1.0)**
- ✅ Revolutionary agent-prompt binding system with automatic activation
- ✅ Perfect directory structure alignment (100% prompt-agent compatibility)
- ✅ Simplified TodoWrite integration with streamlined hooks
- ✅ Comprehensive agent creation standards and quality framework
- ✅ Enhanced documentation system with quantitative data removal
- ✅ Framework cleanup removing over-engineered components

**2025-09-14 - Session Management Implementation (v2.0.1)**
- ✅ Complete session management system (5/5 prompts)
- ✅ Advanced context analysis and state recovery
- ✅ MCP tools integration (Serena, Context7, Playwright)
- ✅ TodoWrite hierarchical task management integration
- ✅ Comprehensive framework specification (this document)

**2025-09-14 - Quality Crisis Discovery**
- 🚨 Identified critical hardcoding issues in 64% of agent prompts
- 🚨 Discovered functional design violations across framework
- ✅ Established functional design principles and mandatory rules
- ✅ Created comprehensive quality assessment and improvement plan
- ⚠️ Removed non-compliant Project Management prompts for rewrite

### Current Development Status

**Completed Components:**
- ✅ **Agent-Prompt Integration System**: Revolutionary automatic binding with 100% compatibility
- ✅ **Simplified TodoWrite Framework**: Streamlined hooks and coordination patterns
- ✅ **Agent Creation Standards**: Comprehensive quality framework and validation
- ✅ **Framework Architecture**: Complete specification with optimization guidelines
- ✅ **Directory Structure**: Perfect alignment between prompts and agents
- ✅ **Documentation System**: Enhanced with quantitative data cleanup

**Next Priorities:**
- 📋 **Agent Prompt Quality**: Continue refactoring remaining prompts to functional patterns
- 📋 **Advanced Automation**: AI-powered agent selection and workflow optimization
- 📋 **Community Features**: Agent marketplace and contribution system
- 📋 **Performance Monitoring**: Real-time framework performance analytics

### Change Log Format

All changes follow semantic versioning and comprehensive documentation:

```markdown
## [2.0.x] - 2025-MM-DD

### Added
- New framework capabilities and features

### Changed
- Improvements to existing functionality

### Fixed
- Bug fixes and quality improvements

### Removed
- Deprecated or non-compliant components

### Quality
- Prompt compliance and functional design improvements
```

---

*Fill in the above sections according to project requirements. Claude Code agents will automatically adapt their competencies based on this file.*
