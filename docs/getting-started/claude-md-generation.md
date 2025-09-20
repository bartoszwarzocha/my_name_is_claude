# CLAUDE.md Generation Guide

*Complete guide for generating and configuring CLAUDE.md for optimal framework performance*

## 🎯 Overview

**CLAUDE.md is the central configuration file that controls all framework behavior.** This guide shows you three methods to create an optimal CLAUDE.md for your project:

1. **🤖 AI-Powered Generation** - Use built-in AI prompts for automatic configuration
2. **📋 Template-Based Setup** - Customize the provided template for your needs
3. **⚙️ Manual Configuration** - Hand-craft configuration for specific requirements

**Proper CLAUDE.md configuration ensures accurate AI agent recommendations and optimal framework performance.**

---

## 🤖 Method 1: AI-Powered Generation

### **Using Built-in AI Prompts**

The framework includes specialized prompts for intelligent CLAUDE.md generation:

#### **For New Projects - Interactive Setup**
```bash
# Navigate to your project directory
cd /path/to/your-project

# Use the new project initialization prompt
# This prompt analyzes your project and interactively gathers requirements
```

**Prompt Location**: `.claude/prompts/init/new-project.md`

**What it does:**
- Analyzes existing project structure and files
- Detects technology stack from package.json, requirements.txt, etc.
- Identifies project maturity and complexity
- Interactively asks for missing information
- Generates complete CLAUDE.md configuration

**Example Usage:**
```bash
# Example prompt execution:
"Initialize new project with framework configuration"

# The prompt will:
# 1. Analyze current directory structure
# 2. Detect React + TypeScript + Node.js stack
# 3. Ask about business domain (e.g., "ecommerce")
# 4. Determine project scale based on complexity
# 5. Generate optimized CLAUDE.md
```

#### **For Existing Projects - Legacy Integration**
```bash
# For projects with existing codebase
```

**Prompt Location**: `.claude/prompts/init/existing-project.md`

**What it does:**
- Comprehensive analysis of existing codebase
- Identifies legacy patterns and modernization opportunities
- Recommends integration strategy
- Generates CLAUDE.md for gradual framework adoption

#### **From Project Concept - Document-Based Generation**
```bash
# For projects starting from business documents or concepts
```

**Prompt Location**: `.claude/prompts/init/claude_md_from_concept.md`

**What it does:**
- Analyzes documents in `init_concept/` folder
- Extracts project requirements from any format (markdown, Word docs, notes)
- Identifies business domain and technical requirements
- Generates complete CLAUDE.md from concept documents

**Setup Process:**
```bash
# 1. Create concept folder
mkdir init_concept

# 2. Add your project documents
cp project-requirements.md init_concept/
cp technical-notes.txt init_concept/
cp business-plan.docx init_concept/

# 3. Use the concept analysis prompt
# Prompt will read all files and generate CLAUDE.md
```

### **AI Generation Workflow**

#### **Step 1: Project Analysis**
The AI prompt analyzes:
- **Directory Structure**: Files, folders, project organization
- **Technology Indicators**: package.json, requirements.txt, build configs
- **Existing Configuration**: Docker files, CI/CD configs, database settings
- **Code Patterns**: Programming languages, frameworks, architecture

#### **Step 2: Interactive Refinement**
The AI asks targeted questions:
- **Project Identity**: Name, description, core purpose
- **Business Domain**: Industry sector (fintech, healthcare, ecommerce, etc.)
- **Project Scale**: Startup/SME/Enterprise based on complexity
- **Team Size**: Solo, small team, large team
- **Quality Requirements**: Performance, security, compliance needs

#### **Step 3: Configuration Generation**
The AI generates:
- **Complete CLAUDE.md**: All required sections with optimal settings
- **Technology Stack**: Detected and validated technology choices
- **Agent Recommendations**: Optimal agents for your project type
- **Quality Standards**: Appropriate standards for your scale
- **Workflow Configuration**: Development processes and automation

### **Example AI-Generated CLAUDE.md**

```markdown
## Project Metadata
- **project_name**: "ecommerce-platform"
- **project_description**: "Modern e-commerce platform with AI recommendations"
- **project_version**: "1.0.0"
- **primary_language**: "typescript"
- **business_domain**: "ecommerce"
- **project_scale**: "sme"
- **development_stage**: "development"

## Technologies
**Frontend**: React 18, TypeScript, Next.js 13, Tailwind CSS
**Backend**: Node.js 18, Express, TypeScript, Prisma
**Database**: PostgreSQL 15, Redis 7
**Authentication**: NextAuth.js, JWT
**Testing**: Jest, Cypress, React Testing Library
**Infrastructure**: Vercel, AWS S3, Stripe

## AI Tools Configuration
- **ai_tools_enabled**: true
- **ai_workflow_preference**: "balanced"
- **serena_enabled**: true
- **context7_enabled**: true

## Quality Standards
- **code_coverage_minimum**: 80
- **security_scan_required**: true
- **performance_budget_enabled**: true
- **accessibility_compliance**: "wcag_aa"
```

---

## 📋 Method 2: Template-Based Setup

### **Using CLAUDE_template.md**

After framework installation, you'll have `CLAUDE_template.md` ready for customization:

#### **Step 1: Copy Template**
```bash
# Navigate to your project
cd /path/to/your-project

# Copy template to active configuration
cp CLAUDE_template.md CLAUDE.md
```

#### **Step 2: Customize Configuration**
```bash
# Edit with your preferred editor
nano CLAUDE.md
# or
code CLAUDE.md
# or
vim CLAUDE.md
```

#### **Step 3: Essential Customizations**

**Project Identity:**
```markdown
## Project Metadata
- **project_name**: "your-actual-project-name"
- **project_description**: "Clear description of what your project does"
- **primary_language**: "typescript"  # Match your main language
- **business_domain**: "fintech"      # Your industry sector
- **project_scale**: "startup"       # startup, sme, enterprise
```

**Technology Stack:**
```markdown
## Technologies
**Frontend**: React 18, TypeScript, Vite  # Your actual frontend stack
**Backend**: Node.js, Express, TypeScript # Your actual backend stack
**Database**: PostgreSQL, Redis          # Your actual databases
**Testing**: Jest, Cypress               # Your testing tools
```

**Quality Requirements:**
```markdown
## Quality Standards
- **code_coverage_minimum**: 85         # Your coverage target
- **security_scan_required**: true      # Security requirements
- **performance_budget_enabled**: true  # Performance monitoring
```

### **Template Customization Examples**

#### **React + Node.js Startup:**
```markdown
## Project Metadata
- **project_scale**: "startup"
- **development_stage**: "development"
- **team_size**: "small_team"

## Quality Standards
- **code_coverage_minimum**: 75
- **testing_strategy**: "standard"
- **deployment_frequency**: "daily"
```

#### **Enterprise Java Application:**
```markdown
## Project Metadata
- **primary_language**: "java"
- **project_scale**: "enterprise"
- **business_domain**: "fintech"

## Technologies
**Backend**: Java 17, Spring Boot 3.0, Maven
**Database**: PostgreSQL, MongoDB
**Security**: Spring Security, OAuth2

## Quality Standards
- **code_coverage_minimum**: 90
- **security_scan_required**: true
- **compliance_requirements**: ["pci_dss", "sox"]
```

#### **Python Data Science Project:**
```markdown
## Project Metadata
- **primary_language**: "python"
- **business_domain**: "ai_ml"
- **project_scale**: "sme"

## Technologies
**Backend**: Python 3.11, FastAPI, SQLAlchemy
**Data**: PostgreSQL, ClickHouse, Redis
**ML/AI**: scikit-learn, TensorFlow, PyTorch
**Infrastructure**: Docker, Kubernetes, Jupyter
```

---

## ⚙️ Method 3: Manual Configuration

### **Creating CLAUDE.md from Scratch**

For complete control over configuration:

#### **Step 1: Create Base Structure**
```bash
# Create new CLAUDE.md file
touch CLAUDE.md
```

#### **Step 2: Add Required Sections**
```markdown
# CLAUDE.md – Claude Code Multi-Agent Framework

## Project Metadata
- **project_name**: "your-project"
- **project_description**: "Your project description"
- **project_version**: "1.0.0"
- **primary_language**: "typescript"
- **business_domain**: "web_development"
- **project_scale**: "startup"
- **development_stage**: "development"

## Project Overview
[Brief description of what you're building]

## Technologies
**Framework**: [Your main frameworks]
**Frontend**: [Frontend technologies]
**Backend**: [Backend technologies]
**Database**: [Database technologies]
**Testing**: [Testing frameworks]
**Infrastructure**: [Infrastructure tools]

## Goals
- [Your project goals]
- [Success criteria]
- [Key metrics]
```

#### **Step 3: Advanced Configuration**

**For AI Tools Integration:**
```markdown
## MCP Tools Integration
- **serena_enabled**: true
- **context7_enabled**: true
- **ai_tools_enabled**: true

## AI Tools Configuration
- **ai_agent_selector**: "enabled"
- **intelligent_code_analysis**: true
- **ai_workflow_preference**: "balanced"
```

**For Team Collaboration:**
```markdown
## Team Configuration
- **team_size**: "small_team"
- **development_methodology**: "agile"
- **collaboration_tools**: ["git", "slack", "jira"]
- **review_process**: "pull_request_required"
```

**For Quality Standards:**
```markdown
## Quality Standards
- **code_coverage_minimum**: 80
- **security_scan_required**: true
- **performance_budget_enabled**: true
- **accessibility_compliance**: "wcag_aa"
- **code_style_enforcement**: "strict"
```

### **Configuration Validation**

#### **Test Your Configuration**
```bash
# Validate configuration with AI Agent Selector
python ./.ai-tools/core/demo/demo_project_analyzer.py .

# Expected output:
# ✅ Configuration valid
# ✅ Technology stack detected correctly
# ✅ Agent recommendations align with settings
# 🤖 RECOMMENDED AGENTS: [list of agents]
```

#### **Common Configuration Issues**
- **Mismatched technology stack** - Ensure CLAUDE.md matches actual project technologies
- **Wrong project scale** - Adjust scale based on actual team size and complexity
- **Missing business domain** - Specify domain for accurate agent recommendations
- **Outdated versions** - Keep technology versions current

---

## 🎯 Configuration Examples by Project Type

### **Startup SaaS Application**
```markdown
## Project Metadata
- **project_scale**: "startup"
- **business_domain**: "saas"
- **development_stage**: "development"

## Technologies
**Frontend**: React 18, TypeScript, Next.js
**Backend**: Node.js, Express, Prisma
**Database**: PostgreSQL, Redis
**Infrastructure**: Vercel, Railway

## Quality Standards
- **code_coverage_minimum**: 75
- **testing_strategy**: "standard"
- **deployment_frequency**: "daily"
```

### **Enterprise Financial Platform**
```markdown
## Project Metadata
- **project_scale**: "enterprise"
- **business_domain**: "fintech"
- **development_stage**: "production"

## Technologies
**Backend**: Java 17, Spring Boot, Maven
**Database**: PostgreSQL, MongoDB
**Security**: Spring Security, OAuth2, LDAP
**Infrastructure**: Kubernetes, OpenShift

## Quality Standards
- **code_coverage_minimum**: 90
- **security_scan_required**: true
- **compliance_requirements**: ["pci_dss", "sox"]
```

### **Data Science Platform**
```markdown
## Project Metadata
- **primary_language**: "python"
- **business_domain**: "ai_ml"
- **project_scale**: "sme"

## Technologies
**Backend**: Python 3.11, FastAPI
**Data**: PostgreSQL, ClickHouse, Redis
**ML/AI**: scikit-learn, TensorFlow
**Infrastructure**: Docker, Kubernetes

## Quality Standards
- **code_coverage_minimum**: 85
- **performance_monitoring**: "real_time"
- **data_quality_validation**: "automated"
```

---

## 🔧 Advanced Configuration Techniques

### **Environment-Specific Configuration**
```markdown
## Environment Configuration
### Development
- **ai_tools_enabled**: true
- **debugging_enabled**: true
- **hot_reload**: true

### Production
- **ai_tools_enabled**: false
- **monitoring_enhanced**: true
- **performance_monitoring**: "real_time"
```

### **Team Role-Based Configuration**
```markdown
## Team Roles and Agent Assignments
**Architecture**: [Team Lead] - software-architect, security-engineer
**Frontend**: [Developers] - frontend-engineer, ux-designer
**Backend**: [Developers] - api-engineer, data-engineer
**DevOps**: [Engineers] - deployment-engineer, platform-engineer
**QA**: [Engineers] - qa-engineer, security-engineer
```

### **Integration-Specific Configuration**
```markdown
## External Integrations
- **payment_processing**: "stripe"
- **authentication**: "auth0"
- **monitoring**: "datadog"
- **error_tracking**: "sentry"
- **analytics**: "mixpanel"
```

---

## ✅ Configuration Validation Checklist

### **Essential Validation Steps**
- [ ] **Project metadata complete** - All required fields filled
- [ ] **Technology stack accurate** - Matches actual project technologies
- [ ] **Business domain specific** - Correctly categorized industry
- [ ] **Project scale appropriate** - Matches team size and complexity
- [ ] **Quality standards realistic** - Achievable for project scale
- [ ] **AI tools properly configured** - Enabled if tools are available
- [ ] **Team configuration accurate** - Reflects actual team structure

### **Testing Your Configuration**
```bash
# Run project analysis to validate configuration
python ./.ai-tools/core/demo/demo_project_analyzer.py .

# Check for warnings or recommendations
# ✅ All settings should align with project reality
# ⚠️ Address any configuration warnings
# 🔧 Adjust settings based on recommendations
```

---

## 🎯 Next Steps After Configuration

### **Immediate Next Steps**
1. **[Test AI Agent Selection](../ai-tools/ai-tools-overview.md#quick-start)** - Verify agent recommendations
2. **[First AI-Assisted Task](first-steps.md)** - Complete your first framework-guided development
3. **[Development Workflow](../workflows/development-workflow.md)** - Start using framework in development

### **Advanced Configuration**
1. **[Framework Customization](../advanced/framework-customization.md)** - Deep customization options
2. **[Custom Agent Development](../advanced/custom-agent-development.md)** - Create specialized agents
3. **[Team Collaboration Setup](../workflows/team-collaboration.md)** - Multi-developer configuration

---

## 📞 Configuration Support

### **Common Configuration Problems**
- **Poor agent recommendations** → Check technology stack accuracy in CLAUDE.md
- **Missing features** → Verify AI tools configuration and dependencies
- **Performance issues** → Adjust analysis depth and caching settings
- **Team coordination problems** → Review team configuration and role assignments

### **Getting Help**
- **[CLAUDE.md Configuration Reference](../advanced/claude-md-configuration.md)** - Complete configuration guide
- **[Troubleshooting Guide](../reference/troubleshooting.md)** - Common issues and solutions
- **[AI Tools Troubleshooting](../ai-tools/troubleshooting-ai.md)** - AI-specific problems

---

**🎉 You're now ready to generate optimal CLAUDE.md configuration for your project!**

**Remember:** Accurate CLAUDE.md configuration is the foundation for effective AI agent recommendations. Invest time in getting it right for maximum framework value.