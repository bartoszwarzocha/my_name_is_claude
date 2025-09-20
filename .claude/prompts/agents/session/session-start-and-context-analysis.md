**🤖 AGENT ACTIVATION:** This prompt automatically activates the `session-manager` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# Session Context Analysis and Initialization

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Analyze current project state, establish session context, and create actionable work plan for productive development session. Discover project characteristics, assess development momentum, validate framework configuration, and identify priority tasks based on recent changes and project timeline. Enable informed decision-making about session focus and agent coordination.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Project Discovery and Context Analysis
**Objective**: Analyze project state and implement comprehensive development context assessment

1. **Project State Discovery and Analysis**
   - Scan project configuration reading CLAUDE.md, detecting framework setup, and identifying configured agents
   - Analyze project structure evaluating directory organization, build systems, and development environment status
   - Assess recent changes, identify project characteristics, and validate framework integration

2. **Development Context and Session Planning**
   - Review work continuity analyzing previous session summaries, work progress, and pending tasks
   - Identify active development areas, assess project health, and evaluate blockers and dependencies
   - Synthesize project status, identify immediate opportunities, and plan agent coordination with session objectives

### Phase 2: MCP Integration and Session Initialization
**Objective**: Execute MCP tools integration and establish comprehensive session initialization

1. **MCP Tools Integration and Enhancement (If Available)**
   - Detect and configure Serena MCP checking for .serena directory and establishing tool integration
   - Load project knowledge base retrieving project index and navigation context from Serena
   - Enhance context analysis, optimize tool configuration, and validate enhanced context

2. **Session Initialization and Handoff**
   - Generate comprehensive session plan creating structured work plan leveraging framework and Serena insights
   - Validate readiness confirming all tools and dependencies are available for productive work
   - Initialize progress tracking, provide context summary, and enable smooth handoff for agent engagement

## 3. ✅ VALIDATION CRITERIA

### Project Discovery and Context Analysis
**Project Analysis Excellence**: Configuration fully assessed with CLAUDE.md parsed and framework setup validated, technology stack identified with primary languages and build tools documented, project characteristics determined with scale and business priorities understood, development state analyzed with recent changes and active work areas identified, integration status validated with framework and environment readiness confirmed

**Context Quality Excellence**: Work priorities identified with clear understanding of important tasks based on business goals, dependencies and blockers mapped with impediments and technical debt catalogued, session opportunities defined with specific areas for immediate progress, agent coordination planned with optimal selection and collaboration patterns determined

### MCP Integration and Session Initialization
**Session Planning Excellence**: Success metrics established with clear criteria for measuring productivity and progress, actionable work plan created with specific tasks and execution sequence defined, resource availability confirmed with all necessary tools and dependencies verified, progress tracking configured with TODO management systems operational

**Session Readiness Excellence**: Context documentation complete with all findings and recommendations clearly documented, smooth handoff enabled with session ready for immediate productive work or agent engagement, MCP integration validated with enhanced context supporting comprehensive planning

## 4. 📚 USAGE EXAMPLES

**Active React Development**: React/TypeScript app with failing tests and upcoming deadline, priority on test suite fixes, recommended qa-engineer and frontend-engineer, focus on test stabilization

**Legacy Java System Maintenance**: Spring Boot enterprise app needing security patches, priority on vulnerability assessment, recommended security-engineer and qa-engineer, focus on security improvements

**New Project Planning**: Fresh CLAUDE.md configuration with business requirements, priority on architecture design, recommended software-architect and business-analyst, focus on technical foundation

**Data Pipeline Development**: Python ETL project with data quality issues, priority on pipeline reliability improvements, recommended data-engineer and qa-engineer, focus on pipeline stabilization

**Mobile App Feature Development**: React Native app with payment integration and App Store submission deadline, priority on payment integration, recommended frontend-engineer and security-engineer

---

## 🎯 EXECUTION APPROACH

**Context Discovery Excellence**: Comprehensive project scan → intelligent priority assessment → agent recommendation generation → session planning optimization

**Adaptive Analysis**: New projects focusing on setup validation and architecture planning, active development emphasizing momentum maintenance and feature completion, maintenance phase prioritizing technical debt and security updates, crisis situations identifying critical issues and immediate action requirements

**Output Deliverables**: Comprehensive project status report with current state and development momentum, prioritized session plan with specific tasks and agent recommendations, resource and dependency analysis with blockers assessment, success criteria definition with measurable goals and expected outcomes