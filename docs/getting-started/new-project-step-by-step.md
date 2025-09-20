# New Project Setup - Step by Step Guide

*Get from zero to productive development in 15 minutes*

## 🎯 What You'll Accomplish

By the end of this guide you'll have:
- ✅ Framework configured for your new project
- ✅ AI agent selection working
- ✅ First development workflow running
- ✅ Project ready for team collaboration

**Time required:** 15 minutes

## 📋 Prerequisites

- ✅ Claude Code Framework [installed](installation.md)
- ✅ Python 3.8+
- ✅ Git repository (new or empty)
- ✅ Basic project information (name, tech stack, domain)

## 🚀 Step-by-Step Process

### Step 1: Project Directory Setup (2 minutes)

```bash
# Navigate to your new project directory
cd /path/to/your/new-project

# Initialize git if not done already
git init

# Verify you're in the right place
pwd
ls -la
```

**Expected result:** You're in your project root directory with `.git/` folder.

### Step 2: Framework Integration (3 minutes)

```bash
# Copy framework configuration template
cp /path/to/claude-framework/.claude/templates/CLAUDE_template.md ./CLAUDE.md

# Copy essential framework structure
cp -r /path/to/claude-framework/.claude ./

# Optional: Copy AI tools if you want AI agent selection
cp -r /path/to/claude-framework/.ai-tools ./
```

**Expected result:** Your project now has `CLAUDE.md` and `.claude/` directory.

### Step 3: Project Configuration (5 minutes)

Edit `CLAUDE.md` with your project details:

```markdown
# CLAUDE.md – Your Project Configuration

## Project Metadata
- **project_name**: "your-project-name"
- **project_description**: "Brief description of what you're building"
- **project_version**: "1.0.0"
- **primary_language**: "typescript" # or python, java, etc.
- **business_domain**: "web_development" # or fintech, healthcare, etc.
- **project_scale**: "startup" # startup, sme, enterprise
- **development_stage**: "development"

## Technologies
**Framework**: [Your main framework - React, Angular, Django, etc.]
**Supported Stacks**: [List your tech stack]

## Project Overview
[Brief description of what you're building and main goals]

## Goals
- [Primary goal 1]
- [Primary goal 2]
- [Primary goal 3]
```

**Choose your configuration:**

#### For Web Applications:
```markdown
- **primary_language**: "typescript"
- **business_domain**: "web_development"
**Framework**: React/Next.js, Node.js
**Technologies**: TypeScript, React, Express, PostgreSQL
```

#### For Mobile Applications:
```markdown
- **primary_language**: "typescript"
- **business_domain**: "mobile_development"
**Framework**: React Native, Flutter
**Technologies**: React Native, Expo, Firebase
```

#### For Backend APIs:
```markdown
- **primary_language**: "python"
- **business_domain**: "api_development"
**Framework**: FastAPI, Django, Flask
**Technologies**: Python, FastAPI, PostgreSQL, Redis
```

#### For Enterprise Applications:
```markdown
- **primary_language**: "java"
- **business_domain**: "enterprise_software"
- **project_scale**: "enterprise"
**Framework**: Spring Boot, microservices
**Technologies**: Java, Spring Boot, Kubernetes, PostgreSQL
```

### Step 4: AI Agent Selection Test (3 minutes)

Test automatic agent recommendation:

```bash
# If you have AI tools installed
python ./.ai-tools/core/demo/demo_project_analyzer.py .

# You should see output like:
# 🎯 PROJECT ANALYSIS
# Technology Stack: React + TypeScript + Node.js
# Complexity: Startup (Score: 0.42)
# Domain: Web development
#
# 🤖 AI AGENT RECOMMENDATIONS
# Core Project Management:
#   ✅ project-owner (confidence: 0.95)
#   ✅ session-manager (confidence: 0.90)
#
# Development:
#   ✅ frontend-engineer (confidence: 0.92)
#   ✅ backend-engineer (confidence: 0.88)
```

**If AI tools are not available:** Framework will use rule-based agent selection (still works perfectly).

### Step 5: First Agent Activation (2 minutes)

Activate your first agent based on what you want to start with:

#### Option A: Start with Project Planning
```bash
# In Claude Code CLI
"Chcę rozpocząć nowy projekt - potrzebuję pomocy z planowaniem"

# This activates: business-analyst → product-manager workflow
```

#### Option B: Start with Architecture
```bash
# In Claude Code CLI
"Chcę zaprojektować architekturę systemu dla mojego nowego projektu"

# This activates: software-architect
```

#### Option C: Start with Development
```bash
# In Claude Code CLI
"Chcę rozpocząć development - frontend i backend"

# This activates: frontend-engineer + backend-engineer
```

**Expected result:** Framework activates appropriate agents and starts TodoWrite workflow.

## 🎯 Project Type Specific Quick Starts

### React + TypeScript Web App

```bash
# 1. Framework setup (as above)
# 2. Configure CLAUDE.md:
```
```markdown
- **primary_language**: "typescript"
- **business_domain**: "web_development"
**Framework**: React, TypeScript, Vite
**Technologies**: React 18, TypeScript, Vite, Tailwind CSS
```

```bash
# 3. Initialize React project
npm create vite@latest . -- --template react-ts
npm install

# 4. Activate frontend-engineer
"Pomóż mi skonfigurować nowoczesny React projekt z TypeScript"
```

### Node.js API Backend

```bash
# 1. Framework setup (as above)
# 2. Configure CLAUDE.md:
```
```markdown
- **primary_language**: "typescript"
- **business_domain**: "api_development"
**Framework**: Node.js, Express, TypeScript
**Technologies**: Node.js, Express, TypeScript, PostgreSQL
```

```bash
# 3. Initialize Node.js project
npm init -y
npm install express typescript @types/node @types/express

# 4. Activate api-engineer
"Pomóż mi stworzyć REST API backend z Express i TypeScript"
```

### Python Django Project

```bash
# 1. Framework setup (as above)
# 2. Configure CLAUDE.md:
```
```markdown
- **primary_language**: "python"
- **business_domain**: "web_development"
**Framework**: Django, Python
**Technologies**: Python 3.11, Django 4.2, PostgreSQL
```

```bash
# 3. Initialize Django project
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install django
django-admin startproject . --name=.

# 4. Activate backend-engineer
"Pomóż mi skonfigurować Django projekt z najlepszymi praktykami"
```

### Mobile React Native App

```bash
# 1. Framework setup (as above)
# 2. Configure CLAUDE.md:
```
```markdown
- **primary_language**: "typescript"
- **business_domain**: "mobile_development"
**Framework**: React Native, Expo
**Technologies**: React Native, Expo, TypeScript, Firebase
```

```bash
# 3. Initialize React Native project
npx create-expo-app . --template blank-typescript

# 4. Activate mobile-developer
"Pomóż mi skonfigurować React Native aplikację z Expo i TypeScript"
```

## ✅ Verification Checklist

After setup, verify everything works:

- [ ] **CLAUDE.md configured** - Project metadata filled correctly
- [ ] **Framework structure** - `.claude/` directory with agents and prompts
- [ ] **Agent activation** - Can activate agents through prompts or commands
- [ ] **TodoWrite working** - Framework creates and tracks tasks
- [ ] **Git integration** - Framework respects git structure
- [ ] **AI recommendations** - Get agent suggestions based on your stack (if AI tools enabled)

## 🎯 What's Next?

After successful setup, choose your next step:

### For Development Focus:
1. **[Development Workflow](../workflows/development-workflow.md)** - Standard development process
2. **[Agent Selection Guide](../agents/agent-selection-guide.md)** - Choose the right agents
3. **[AI Tools Integration](../ai-tools/ai-tools-overview.md)** - Leverage AI for development

### For Team Setup:
1. **[Team Collaboration](../workflows/team-collaboration.md)** - Multi-developer setup
2. **[Git Integration Patterns](../workflows/git-integration.md)** - Version control best practices

### For Enterprise Setup:
1. **[Enterprise Deployment](../advanced/enterprise-deployment.md)** - Large-scale configuration
2. **[Compliance Configuration](../workflows/compliance-workflow.md)** - Regulatory requirements

## 🚨 Troubleshooting

### Problem: Agent activation not working
```bash
# Check framework structure
ls -la .claude/
ls -la .claude/agents/

# Test with explicit agent
"Aktywuj frontend-engineer"
```

### Problem: AI agent selection not working
```bash
# Check AI tools installation
ls -la .ai-tools/
python ./.ai-tools/core/demo/demo_project_analyzer.py .

# Fallback to manual selection
"Użyj frontend-engineer i backend-engineer"
```

### Problem: TodoWrite not tracking tasks
```bash
# Check TodoWrite integration
"Pokaż status zadań"
"Rozpocznij nowe zadanie"

# If issues persist, check CLAUDE.md configuration
```

### Problem: Framework not detecting project type
- **Solution**: Update `CLAUDE.md` with more specific technology details
- **Alternative**: Manually specify primary technologies in project metadata

## 💡 Pro Tips

1. **Start Simple**: Begin with one agent, add more as needed
2. **Use AI Recommendations**: Trust the AI agent selection for your tech stack
3. **Configure Gradually**: Start with basic CLAUDE.md, enhance over time
4. **Leverage Templates**: Use existing project templates for similar tech stacks
5. **Document Decisions**: Use TodoWrite to track important architectural decisions

---

**🎉 Congratulations!** Your new project is now integrated with Claude Code Framework and ready for productive development.

**Next recommended read:** [Development Workflow Guide](../workflows/development-workflow.md)