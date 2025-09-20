# Framework Installation Guide

*Complete guide for installing Claude Code Framework in new or existing projects*

## 🎯 Installation Overview

**Claude Code Framework can be installed in two ways:**

1. **🆕 New Project Installation** - Adding framework to a new project directory
2. **🔄 Existing Project Integration** - Adding framework to an existing codebase

**Both methods use the `copy_framework_to_project.sh` script for safe, reliable installation.**

---

## 📋 Prerequisites

### **System Requirements**
- **Operating System**: Linux, macOS, or Windows with WSL2
- **Python**: 3.8+ (recommended: 3.11+)
- **Git**: Version 2.20+
- **Disk Space**: 2GB+ free space
- **Memory**: 4GB+ RAM (8GB+ recommended for AI features)

### **Required Access**
- Claude Code Framework source directory (this repository)
- Target project directory (read/write permissions)
- Internet connection (for Python dependencies)

---

## 🚀 Installation Methods

### **Method 1: New Project Installation**

#### **Step 1: Create Project Directory**
```bash
# Create new project directory
mkdir my-awesome-project
cd my-awesome-project

# Initialize git (recommended)
git init
echo "node_modules/" > .gitignore
echo ".ai-tools/venv/" >> .gitignore
echo ".ai-tools/core/data/" >> .gitignore
echo ".claude/sessions/" >> .gitignore
```

#### **Step 2: Copy Framework**
```bash
# Navigate to framework source directory
cd /path/to/claude-code-framework

# Copy framework to your project (dry run first)
./copy_framework_to_project.sh /path/to/my-awesome-project --dry-run

# Review what will be copied, then execute
./copy_framework_to_project.sh /path/to/my-awesome-project
```

#### **Step 3: Navigate to Your Project**
```bash
cd /path/to/my-awesome-project

# Verify framework installation
ls -la
# Should see: .ai-tools/ .claude/ ai-tools.sh CLAUDE_template.md
```

### **Method 2: Existing Project Integration**

#### **Step 1: Backup Your Project**
```bash
# Create backup before integration
cd /path/to/existing-project
git checkout -b framework-integration-backup

# Or create manual backup
tar -czf "../project-backup-$(date +%Y%m%d).tar.gz" .
```

#### **Step 2: Check for Conflicts**
```bash
# Navigate to framework source
cd /path/to/claude-code-framework

# Check what would be copied to your project
./copy_framework_to_project.sh /path/to/existing-project --dry-run

# If conflicts exist, use backup mode
./copy_framework_to_project.sh /path/to/existing-project --backup
```

#### **Step 3: Verify Integration**
```bash
cd /path/to/existing-project

# Check framework files are present
ls -la .ai-tools/ .claude/
ls -la ai-tools.sh CLAUDE_template.md
```

---

## 🔧 Copy Script Options

### **Available Options**

| Option | Description | Use Case |
|--------|-------------|----------|
| `--dry-run` | Show what would be copied without copying | Safe preview before installation |
| `--backup` | Create backups of existing files | Existing project integration |
| `--force` | Skip confirmation prompts | Automated installation scripts |
| `--help` | Show usage information | Learn about available options |

### **Usage Examples**

#### **Safe Installation with Preview**
```bash
# Preview what will be copied
./copy_framework_to_project.sh /path/to/project --dry-run

# Execute after review
./copy_framework_to_project.sh /path/to/project
```

#### **Existing Project with Backups**
```bash
# Install with automatic backups of existing files
./copy_framework_to_project.sh /path/to/existing-project --backup
```

#### **Automated Installation**
```bash
# No prompts for scripted installations
./copy_framework_to_project.sh /path/to/project --force
```

### **What Gets Copied**

#### **Essential Directories**
- **`.ai-tools/`** - AI-powered development tools (excluding venv/)
- **`.claude/`** - Agent definitions and prompts library
- **`.mcp-tools/`** - MCP (Model Context Protocol) integrations
- **`init_concept/`** - Project initialization templates

#### **Essential Files**
- **`ai-tools.sh`** - Main framework launcher script
- **`mcp-tools.sh`** - MCP tools launcher
- **`VERSION`** - Framework version information

#### **Special Files**
- **`CLAUDE_template.md`** - Template for project configuration (renamed from CLAUDE.md)
- **`FRAMEWORK_LICENSE`** - Framework licensing terms (renamed from LICENSE)

---

## ⚙️ Post-Installation Setup

### **Step 1: Python Environment Setup**
```bash
# Navigate to your project
cd /path/to/your-project

# Create Python virtual environment for AI tools
python -m venv .ai-tools/venv

# Activate virtual environment
source .ai-tools/venv/bin/activate  # Linux/macOS
# or .ai-tools/venv/Scripts/activate  # Windows

# Install Python dependencies (optional but recommended)
pip install pandas numpy scikit-learn joblib
```

### **Step 2: Framework Validation**
```bash
# Test basic framework functionality
python ./.ai-tools/core/demo/demo_project_analyzer.py .

# Expected output:
# 🎯 PROJECT ANALYSIS
# Technology Stack: [Detected stack]
# Project Scale: [Detected scale]
# 🤖 RECOMMENDED AGENTS
# [Agent recommendations]
```

### **Step 3: Configure CLAUDE.md**

#### **Option A: Use Existing Template**
```bash
# Copy template to active configuration
cp CLAUDE_template.md CLAUDE.md

# Edit configuration for your project
nano CLAUDE.md  # or use your preferred editor
```

#### **Option B: Generate Using AI Prompts**
```bash
# Use framework's AI-powered CLAUDE.md generation
# See "CLAUDE.md Generation" section below for details
```

### **Step 4: Verify Installation**
```bash
# Test AI agent selection
python ./.ai-tools/core/demo/demo_project_analyzer.py .

# Test framework scripts
./ai-tools.sh --help

# Check framework health
./ai-tools.sh status
```

---

## 📝 CLAUDE.md Generation

### **Using Built-in AI Prompts**

The framework includes specialized prompts for generating CLAUDE.md configuration:

#### **For New Projects**
```bash
# Use the new project initialization prompt
# Navigate to .claude/prompts/init/
# Use: new-project.md prompt with your project details
```

#### **For Existing Projects**
```bash
# Use the existing project analysis prompt
# Navigate to .claude/prompts/init/
# Use: existing-project.md prompt to analyze and configure
```

#### **From Project Concept**
```bash
# Generate CLAUDE.md from project concept document
# Use: claude_md_from_concept.md prompt with your concept
```

### **Manual CLAUDE.md Configuration**

#### **Minimal Configuration**
```markdown
## Project Metadata
- **project_name**: "your-project-name"
- **project_description**: "Brief description of your project"
- **project_version**: "1.0.0"
- **primary_language**: "typescript"  # or python, java, etc.
- **business_domain**: "web_development"  # or fintech, healthcare, etc.
- **project_scale**: "startup"  # startup, sme, enterprise
- **development_stage**: "development"

## Technologies
**Frontend**: React, TypeScript, Vite
**Backend**: Node.js, Express, TypeScript
**Database**: PostgreSQL
**Testing**: Jest, Cypress
**Infrastructure**: Docker, AWS
```

#### **Technology-Specific Examples**

**React + Node.js Project:**
```markdown
## Project Metadata
- **primary_language**: "typescript"
- **business_domain**: "web_development"
- **project_scale**: "startup"

## Technologies
**Frontend**: React 18, TypeScript, Vite, Tailwind CSS
**Backend**: Node.js 18, Express, TypeScript
**Database**: PostgreSQL 15, Redis
**Testing**: Jest, Cypress, React Testing Library
```

**Python + Django Project:**
```markdown
## Project Metadata
- **primary_language**: "python"
- **business_domain**: "web_development"
- **project_scale**: "sme"

## Technologies
**Backend**: Python 3.11, Django 4.2, PostgreSQL
**Frontend**: React, TypeScript (if applicable)
**Testing**: pytest, selenium
**Infrastructure**: Docker, Kubernetes
```

---

## 🔍 Troubleshooting Installation

### **Common Issues and Solutions**

#### **Issue: Permission Denied**
```bash
# Fix script permissions
chmod +x copy_framework_to_project.sh

# Fix copied script permissions
chmod +x /path/to/project/ai-tools.sh
chmod +x /path/to/project/mcp-tools.sh
```

#### **Issue: Python Import Errors**
```bash
# Check Python path
cd /path/to/your-project
python -c "import sys; print('\\n'.join(sys.path))"

# Add project root to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Or create .env file
echo "PYTHONPATH=$(pwd)" > .env
```

#### **Issue: AI Tools Not Working**
```bash
# Check Python dependencies
pip list | grep -E "pandas|numpy|scikit"

# Install missing dependencies
pip install pandas numpy scikit-learn joblib

# Test in fallback mode
python -c "
from ai_tools.integration.ai_agent_selector import AIAgentSelector
selector = AIAgentSelector()
print('AI Tools Status:', 'Enabled' if selector.ai_enabled else 'Fallback Mode')
"
```

#### **Issue: Framework Validation Fails**
```bash
# Check essential files exist
ls -la .ai-tools/core/
ls -la .claude/agents/
ls -la .claude/prompts/

# Re-copy framework if files missing
cd /path/to/claude-code-framework
./copy_framework_to_project.sh /path/to/your-project --force
```

### **Validation Checklist**

#### **Framework Installation Validation**
- [ ] **Directories Copied**: .ai-tools/, .claude/, .mcp-tools/, init_concept/
- [ ] **Scripts Executable**: ai-tools.sh, mcp-tools.sh work
- [ ] **Configuration Present**: CLAUDE_template.md exists
- [ ] **Python Environment**: Virtual environment created and activated
- [ ] **Dependencies Installed**: Core Python packages available
- [ ] **AI Tools Working**: demo_project_analyzer.py runs successfully
- [ ] **CLAUDE.md Configured**: Project-specific configuration created

#### **Project Integration Validation**
- [ ] **No Conflicts**: Existing project files not overwritten unexpectedly
- [ ] **Backup Created**: Original files backed up if using --backup
- [ ] **Git Status Clean**: No unintended changes to existing code
- [ ] **Framework Isolated**: Framework files don't interfere with project
- [ ] **AI Analysis Working**: Project correctly detected and analyzed

---

## 🎯 Next Steps After Installation

### **Immediate Next Steps**
1. **[Configure CLAUDE.md](claude-md-configuration.md)** - Customize for your project
2. **[First AI-Assisted Task](first-steps.md)** - Complete your first framework-guided development
3. **[AI Tools Overview](../ai-tools/ai-tools-overview.md)** - Learn about available AI capabilities

### **For New Projects**
1. **[New Project Step-by-Step](new-project-step-by-step.md)** - Complete new project setup
2. **[Development Workflow](../workflows/development-workflow.md)** - Standard development process
3. **[Agent Selection Guide](../agents/agent-selection-guide.md)** - Choose optimal agents

### **For Existing Projects**
1. **[Existing Project Integration](existing-project-integration.md)** - Advanced integration patterns
2. **[Team Collaboration](../workflows/team-collaboration.md)** - Multi-developer coordination
3. **[Framework Customization](../advanced/framework-customization.md)** - Adapt to existing workflows

### **For Teams**
1. **[Team Setup Guide](../workflows/team-collaboration.md#team-setup)** - Multi-developer configuration
2. **[Enterprise Deployment](../advanced/enterprise-deployment.md)** - Organization-wide rollout
3. **[Custom Agent Development](../advanced/custom-agent-development.md)** - Team-specific agents

---

## 📞 Getting Help

### **Installation Support**
- **Framework Issues**: Check [Troubleshooting Guide](../reference/troubleshooting.md)
- **AI Tools Issues**: See [AI Tools Troubleshooting](../ai-tools/troubleshooting-ai.md)
- **Configuration Help**: Review [CLAUDE.md Configuration](../advanced/claude-md-configuration.md)

### **Community Resources**
- **GitHub Issues**: Report installation problems
- **Documentation**: Submit documentation improvements
- **Examples**: Share successful installation patterns

---

**🎉 You're now ready to use Claude Code Framework in your project!**

**Remember:** Proper installation is the foundation for productive development. Take time to configure CLAUDE.md accurately for optimal AI agent recommendations.