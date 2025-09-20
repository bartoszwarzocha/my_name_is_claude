# First Steps with Claude Code Framework

*Complete post-installation guide for getting productive with the framework immediately*

## 🎯 What You'll Accomplish

**In the next 20 minutes, you'll:**
- ✅ Validate your framework installation
- ✅ Set up Python environment for AI features
- ✅ Configure CLAUDE.md for your project
- ✅ Complete your first AI-assisted development task
- ✅ Understand core framework workflows

**By the end, you'll be productive with Claude Code Framework and ready for advanced features.**

---

## 📋 Prerequisites

Before starting, ensure you've completed:
- **[Framework Installation](framework-installation.md)** - Framework copied to your project
- **Project Directory** - You're in a directory with framework files (`.claude/`, `.ai-tools/`, etc.)
- **Basic Tools** - Python 3.8+, Git, text editor of choice

---

## 🔧 Step 1: Post-Installation Validation (5 minutes)

### **Verify Framework Files**
```bash
# Navigate to your project directory
cd /path/to/your-project

# Check essential framework files exist
ls -la .claude/ .ai-tools/
ls -la ai-tools.sh CLAUDE_template.md

# Expected output:
# .claude/          - Agent definitions and prompts
# .ai-tools/        - AI-powered development tools
# ai-tools.sh       - Framework launcher script
# CLAUDE_template.md - Configuration template
```

### **Test Framework Scripts**
```bash
# Make scripts executable (if needed)
chmod +x ai-tools.sh

# Test framework launcher
./ai-tools.sh --help

# Expected output:
# Claude Code Multi-Agent Framework
# Usage: ./ai-tools.sh [command] [options]
# Commands: status, help, version, analyze
```

### **Validate Directory Structure**
```bash
# Check agent definitions
ls .claude/agents/core/
# Should show: architecture, development, management, etc.

# Check AI tools core
ls .ai-tools/core/
# Should show: core, integration, demo, etc.

# Check prompts library
ls .claude/prompts/
# Should show: agents, init, workflows
```

**✅ Checkpoint**: All framework files present and scripts executable.

---

## 🐍 Step 2: Python Environment Setup (5 minutes)

### **Create Python Virtual Environment**
```bash
# Create virtual environment for AI tools
python -m venv .ai-tools/venv

# Activate virtual environment
# Linux/macOS:
source .ai-tools/venv/bin/activate

# Windows:
.ai-tools/venv/Scripts/activate

# Verify activation (prompt should show (.ai-tools))
which python
# Should show: /path/to/your-project/.ai-tools/venv/bin/python
```

### **Install Python Dependencies**
```bash
# Install core dependencies for AI features
pip install pandas numpy scikit-learn joblib

# Install additional useful packages (optional)
pip install psutil requests

# Verify installation
pip list | grep -E "pandas|numpy|scikit"
# Should show installed versions
```

### **Test AI Tools Core**
```bash
# Test basic AI functionality
python -c "
import pandas as pd
import numpy as np
import sklearn
print('✅ AI dependencies installed successfully')
print(f'Pandas: {pd.__version__}')
print(f'NumPy: {np.__version__}')
print(f'Scikit-learn: {sklearn.__version__}')
"

# Expected output:
# ✅ AI dependencies installed successfully
# Pandas: [version]
# NumPy: [version]
# Scikit-learn: [version]
```

**✅ Checkpoint**: Python environment ready with AI dependencies.

---

## 📝 Step 3: CLAUDE.md Configuration (5 minutes)

### **Choose Configuration Method**

#### **Option A: Quick Template Setup (Recommended for First Time)**
```bash
# Copy template to active configuration
cp CLAUDE_template.md CLAUDE.md

# Edit with basic project information
nano CLAUDE.md  # or code CLAUDE.md
```

**Essential changes to make:**
```markdown
## Project Metadata
- **project_name**: "your-actual-project-name"
- **project_description**: "Brief description of your project"
- **primary_language**: "typescript"  # Change to your main language
- **business_domain**: "web_development"  # Change to your domain
- **project_scale**: "startup"  # startup, sme, or enterprise
```

#### **Option B: AI-Powered Generation (For Advanced Setup)**
```bash
# Use AI-powered CLAUDE.md generation
# See: claude-md-generation.md for detailed instructions

# Quick AI generation:
# 1. Use .claude/prompts/init/new-project.md prompt
# 2. AI analyzes your project and generates optimal configuration
# 3. Review and customize generated CLAUDE.md
```

### **Validate Configuration**
```bash
# Test configuration with AI Agent Selector
python ./.ai-tools/core/demo/demo_project_analyzer.py .

# Expected output:
# 🎯 PROJECT ANALYSIS
# Technology Stack: [Your detected stack]
# Business Domain: [Your specified domain]
# Project Scale: [Your specified scale]
#
# 🤖 RECOMMENDED AGENTS
# Primary: [agent-name] (confidence: 0.XX)
# Secondary: [agent-name] (confidence: 0.XX)
```

**If you see errors:**
```bash
# Common fixes:
# 1. Check Python dependencies
pip install pandas numpy scikit-learn

# 2. Verify CLAUDE.md format
grep -E "project_name|primary_language" CLAUDE.md

# 3. Run in fallback mode if needed
python -c "
import sys
sys.path.append('.')
print('Framework path OK')
"
```

**✅ Checkpoint**: CLAUDE.md configured and AI analysis working.

---

## 🤖 Step 4: First AI-Assisted Task (10 minutes)

### **Task: Get Agent Recommendations for a Simple Feature**

#### **Scenario: Adding User Authentication**
```bash
# Ask for agent recommendations for authentication feature
# This demonstrates core framework functionality
```

**Example interaction:**
```
You: "I want to add user authentication to my project. Which agents should I use and what approach do you recommend?"

Expected AI Response:
🤖 AGENT RECOMMENDATION ANALYSIS
Based on your project configuration:

Primary Agents:
- security-engineer (confidence: 0.94) - Authentication security patterns
- api-engineer (confidence: 0.91) - Backend authentication API
- frontend-engineer (confidence: 0.88) - Login/register UI components

Recommended Approach:
1. security-engineer: Design secure authentication architecture
2. api-engineer: Implement JWT-based authentication API
3. frontend-engineer: Create responsive authentication UI
4. qa-engineer: Develop comprehensive authentication tests
```

#### **Follow Through: Architecture Planning**
```bash
# Use the recommended security-engineer agent for authentication design
```

**Example follow-up:**
```
You: "Using security-engineer agent, design a secure authentication system for my [React/Node.js/Python/etc.] application."

Expected Response:
🔒 AUTHENTICATION ARCHITECTURE DESIGN

Security Requirements:
- JWT token-based authentication
- Password hashing with bcrypt
- Rate limiting on auth endpoints
- HTTPS enforcement
- Session management with refresh tokens

Implementation Plan:
1. Database schema for users and sessions
2. Authentication middleware
3. Password policy enforcement
4. Account lockout mechanism
5. Security headers and CORS configuration

Technology Integration:
[Customized for your technology stack from CLAUDE.md]
```

#### **Practical Implementation**
```bash
# Follow the agent's recommendations to implement authentication
# This demonstrates the complete framework workflow:

# 1. Agent Analysis → 2. Architecture Design → 3. Implementation Guidance
```

### **Validate Framework Workflow**

**Check that you experienced:**
- ✅ **Accurate Agent Selection** - Recommendations matched your needs
- ✅ **Project-Specific Advice** - Guidance adapted to your technology stack
- ✅ **Actionable Recommendations** - Clear, implementable steps
- ✅ **Quality Focus** - Security, testing, and best practices included

**✅ Checkpoint**: Successfully completed first AI-assisted development task.

---

## 🎯 Step 5: Understanding Core Workflows (5 minutes)

### **Framework Development Pattern**

**Standard workflow you just experienced:**
```
1. Define Task/Feature
   ↓
2. Get AI Agent Recommendations (using project context)
   ↓
3. Activate Recommended Agents
   ↓
4. Receive Project-Specific Guidance
   ↓
5. Implement with Quality Focus
```

### **Key Framework Concepts**

#### **Agent Specialization**
- **Strategic Agents**: business-analyst, product-manager
- **Architecture Agents**: software-architect, ux-designer
- **Development Agents**: frontend-engineer, api-engineer, backend-engineer
- **Quality Agents**: qa-engineer, security-engineer
- **Operations Agents**: deployment-engineer, platform-engineer

#### **Context Adaptation**
- Agents automatically read your CLAUDE.md configuration
- Recommendations adapt to your technology stack
- Advice scales to your project complexity
- Quality standards match your requirements

#### **AI Tools Integration**
- **AI Agent Selector**: Recommends optimal agents for tasks
- **Serena** (if available): Code analysis and navigation
- **Context7** (if available): Advanced code generation
- **Hybrid Workflows**: Combining multiple AI tools

### **Next Development Tasks**

**Try these tasks to build famiciency:**

1. **Frontend Feature**: "Help me create a responsive user dashboard"
   - Expected agents: frontend-engineer, ux-designer

2. **API Development**: "Design REST API for product catalog"
   - Expected agents: api-engineer, data-engineer

3. **Quality Improvement**: "Review my code for security issues"
   - Expected agents: security-engineer, qa-engineer

4. **Performance Optimization**: "Optimize my application performance"
   - Expected agents: performance-engineer, frontend-engineer

---

## ✅ Validation Checklist

### **Framework Installation Validation**
- [ ] **Framework files present** - .claude/, .ai-tools/, scripts exist
- [ ] **Scripts executable** - ai-tools.sh runs without errors
- [ ] **Python environment** - Virtual environment created and activated
- [ ] **Dependencies installed** - pandas, numpy, scikit-learn available
- [ ] **CLAUDE.md configured** - Project metadata accurate and complete
- [ ] **AI analysis working** - demo_project_analyzer.py runs successfully

### **Framework Functionality Validation**
- [ ] **Agent recommendations** - AI suggests appropriate agents for tasks
- [ ] **Project adaptation** - Recommendations match your technology stack
- [ ] **Quality focus** - Security, testing, performance included in guidance
- [ ] **Actionable advice** - Clear, implementable recommendations provided
- [ ] **Workflow understanding** - Clear on how to use framework for development

### **Ready for Production Use**
- [ ] **Confident with basic workflow** - Can get agent recommendations for tasks
- [ ] **Understanding agent specializations** - Know which agents to use when
- [ ] **Configuration validated** - CLAUDE.md accurately reflects project
- [ ] **Environment stable** - No errors in framework operation
- [ ] **Next steps identified** - Clear path for continued framework usage

---

## 🚀 Next Steps

### **Immediate Next Steps (Next 30 minutes)**
1. **[AI Tools Overview](../ai-tools/ai-tools-overview.md)** - Learn about Serena and Context7 capabilities
2. **[Development Workflow](../workflows/development-workflow.md)** - Master the complete development process
3. **[Agent Selection Guide](../reference/agent-reference.md)** - Understand all available agents

### **Short-term Learning (Next week)**
1. **[Team Collaboration](../workflows/team-collaboration.md)** - Multi-developer patterns (if working with team)
2. **[Serena Integration](../ai-tools/serena-integration.md)** - Set up intelligent code analysis
3. **[Framework Customization](../advanced/framework-customization.md)** - Adapt framework to your workflow

### **Advanced Mastery (Next month)**
1. **[Custom Agent Development](../advanced/custom-agent-development.md)** - Create specialized agents
2. **[Hybrid AI Workflows](../ai-tools/hybrid-workflows.md)** - Master multi-tool coordination
3. **[Enterprise Features](../advanced/enterprise-deployment.md)** - Scale framework across organization

### **Project-Specific Next Steps**

**For New Projects:**
- Complete feature development using agent recommendations
- Set up quality assurance with qa-engineer guidance
- Implement deployment pipeline with deployment-engineer

**For Existing Projects:**
- Analyze codebase with Serena for improvement opportunities
- Gradually integrate framework into existing workflows
- Use agents to modernize legacy components

**For Teams:**
- Set up team collaboration workflows
- Standardize agent usage across team members
- Implement shared quality standards and processes

---

## 🆘 Troubleshooting

### **Common Issues After Installation**

#### **Issue: Python Import Errors**
```bash
# Fix Python path issues
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Or add to .env file
echo "PYTHONPATH=$(pwd)" > .env
```

#### **Issue: AI Analysis Not Working**
```bash
# Check dependencies
pip install pandas numpy scikit-learn joblib

# Test in isolation
python -c "from ai_tools.core.data_collection_system import ProjectContextAnalyzer; print('OK')"

# Run in fallback mode if needed
python ./.ai-tools/core/demo/demo_project_analyzer.py . --fallback
```

#### **Issue: Poor Agent Recommendations**
```bash
# Check CLAUDE.md accuracy
grep -E "primary_language|business_domain|project_scale" CLAUDE.md

# Ensure technology stack matches actual project
# Update business domain to be more specific
# Adjust project scale based on actual complexity
```

#### **Issue: Framework Scripts Not Working**
```bash
# Fix permissions
chmod +x ai-tools.sh

# Check script location
ls -la ai-tools.sh

# Run with explicit bash
bash ai-tools.sh --help
```

### **Getting Additional Help**
- **[Troubleshooting Guide](../reference/troubleshooting.md)** - Comprehensive problem solving
- **[AI Tools Troubleshooting](../ai-tools/troubleshooting-ai.md)** - AI-specific issues
- **[Configuration Help](../advanced/claude-md-configuration.md)** - CLAUDE.md optimization

---

**🎉 Congratulations! You're now productive with Claude Code Framework!**

**What you've accomplished:**
- ✅ **Framework Installation Validated** - Everything working correctly
- ✅ **Environment Configured** - Python and dependencies ready
- ✅ **AI Analysis Functional** - Agent recommendations working
- ✅ **First Task Completed** - Experienced core workflow
- ✅ **Ready for Development** - Confident using framework for real work

**You're ready to accelerate your development with AI-powered assistance!**