# New Project Initialization Prompt

**Drag-and-drop ready! Just paste this prompt and I'll guide you through setup.**

---

## 🚀 Initialize New Project with Agent Framework

I'll help you create a new project using the Claude Code Agent Framework with 11 specialized agents. Let me analyze your context and ask only for what I need.

### Step 1: Context Analysis

Let me first check if there's any existing project context:

1. **Check current directory structure** - see if this is already a project
2. **Look for existing CLAUDE.md** - detect any current configuration
3. **Identify any existing tech stack** - from package.json, requirements.txt, etc.
4. **Assess project scope** - from existing files and structure

### Step 2: Smart Information Gathering

Based on my analysis, I'll ask only for missing information:

**If I can't detect project name:**
- What should I call this project?

**If I can't detect programming language:**
- What's your primary programming language? (csharp, python, rust, java, typescript, go, cpp, ruby)

**If I can't detect business domain:**
- What business domain is this? (ecommerce, fintech, healthcare, saas, enterprise, iot, other)

**If I can't detect project scale:**
- What's the project scale? (startup, sme, enterprise)

**AI Development Tools (I'll always ask about these):**
- Do you want to use **Serena** for code navigation and intelligent editing? (y/n)
- Do you want to use **Context7** for advanced code generation and migrations? (y/n)

**If I can't detect specific requirements:**
- Any special technologies or constraints I should know about?

### Step 3: Intelligent Setup

Once I have the information, I'll automatically:

1. **Create customized CLAUDE.md** with:
   - Project metadata section filled with your details
   - Technology stack appropriate for your language/domain
   - Business domain configuration optimized for your use case
   - Agent roles tailored to your project scale and needs

2. **Set up Serena integration** with:
   - `.serena` directory creation
   - `project.yml` configured for your language and project
   - Automatic initialization with `serena onboarding`
   - Initial prompt containing full agent context

3. **Create project structure** including:
   - Directory structure appropriate for your tech stack
   - Basic configuration files (package.json, requirements.txt, etc.)
   - .gitignore tailored to your language and frameworks
   - README.md with agent framework documentation

4. **Initialize development environment** with:
   - Build/dependency configuration files
   - Basic CI/CD templates if appropriate
   - Development database setup if needed
   - Environment variable templates

### Step 4: Agent-Ready Project

After setup, you'll have:

- ✅ **Fully configured CLAUDE.md** adapted to your project
- ✅ **Working Serena integration** with agent context
- ✅ **Complete project structure** ready for development  
- ✅ **All 11 agents** able to understand your project
- ✅ **5-phase workflow** ready to execute
- ✅ **Development environment** prepared

### Smart Defaults I'll Use

**For Startups:**
- Simplified agent workflow focusing on speed
- MVP-focused technology choices
- Basic but scalable architecture patterns

**For SME/Enterprise:**
- Full 11-agent workflow with governance
- Enterprise-grade technology selections
- Comprehensive security and compliance setup

**Language-Specific Optimizations:**
- **Python**: FastAPI/Django, pytest, poetry/pip
- **TypeScript**: React/Vue/Angular, Jest, npm/yarn
- **C#**: ASP.NET Core, xUnit, dotnet CLI
- **Java**: Spring Boot, JUnit, Maven/Gradle
- **Rust**: Actix/Axum, cargo, tokio
- **Go**: Gin/Echo, testing package, modules

### Ready to Start

Just paste this prompt and I'll begin the intelligent setup process! I'll:
1. Analyze your current context
2. Ask minimal questions for missing info
3. Set up everything automatically
4. Give you a ready-to-use project with agent framework

No manual editing of prompts required - just drag, drop, and go! 🚀