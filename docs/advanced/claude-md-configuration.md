# CLAUDE.md Configuration Guide

*Complete reference for configuring My Name Is Claude through CLAUDE.md*

## 🎯 Configuration Overview

**CLAUDE.md is the central configuration file that controls all framework behavior:**

- **🎯 Project Metadata** - Core project information and characteristics
- **🔧 Technology Stack** - Frameworks, languages, and tools
- **🤖 Agent Behavior** - How agents adapt to your project
- **⚡ AI Tools Integration** - MCP tools and automation settings
- **🏗️ Workflow Configuration** - Development processes and standards
- **📊 Quality Standards** - Testing, security, and performance requirements

**Proper configuration ensures optimal framework performance and agent recommendations.**

---

## 📋 Complete Configuration Reference

### **Section 1: Project Metadata**
*Core project identification and classification*

```markdown
## Project Metadata
- **project_name**: "your-project-name"
- **project_description**: "Brief description of what your project does"
- **project_version**: "1.0.0"
- **primary_language**: "typescript"
- **secondary_languages**: ["python", "sql", "bash"]
- **business_domain**: "fintech"
- **project_scale**: "sme"
- **development_stage**: "production"
```

#### **Configuration Options:**

**primary_language:**
- `"typescript"` - TypeScript/JavaScript projects
- `"python"` - Python applications
- `"java"` - Java/JVM applications
- `"csharp"` - .NET/C# applications
- `"go"` - Go applications
- `"rust"` - Rust applications
- `"cpp"` - C++ applications
- `"swift"` - Swift/iOS applications
- `"kotlin"` - Kotlin/Android applications

**business_domain:**
- `"web_development"` - General web applications
- `"fintech"` - Financial technology
- `"healthcare"` - Healthcare and medical systems
- `"ecommerce"` - E-commerce platforms
- `"edtech"` - Educational technology
- `"gaming"` - Gaming and entertainment
- `"iot"` - Internet of Things
- `"ai_ml"` - AI/ML applications
- `"enterprise_software"` - B2B enterprise solutions
- `"saas"` - Software as a Service platforms

**project_scale:**
- `"startup"` - Small team, rapid iteration, MVP focus
- `"sme"` - Small/medium enterprise, established processes
- `"enterprise"` - Large organization, compliance, governance

**development_stage:**
- `"planning"` - Requirements and design phase
- `"development"` - Active development
- `"testing"` - Quality assurance and testing
- `"production"` - Live system in production
- `"maintenance"` - Ongoing maintenance and updates
- `"legacy"` - Legacy system requiring modernization

### **Section 2: Technology Stack Configuration**
*Detailed technology and framework specifications*

```markdown
## Technologies
**Framework**: React, Node.js, PostgreSQL
**Frontend**: React 18, TypeScript, Next.js 13, Tailwind CSS
**Backend**: Node.js 18, Express 4.18, TypeScript
**Database**: PostgreSQL 15, Redis 7
**Testing**: Jest, Cypress, Supertest, React Testing Library
**Infrastructure**: Docker, Kubernetes, AWS
**CI/CD**: GitHub Actions, Docker Hub
**Monitoring**: DataDog, Sentry
```

#### **Technology Stack Examples by Type:**

**Modern Web Application:**
```markdown
**Frontend**: React 18, TypeScript, Vite, Tailwind CSS
**Backend**: Node.js, Express, TypeScript
**Database**: PostgreSQL, Redis
**Authentication**: JWT, OAuth2
**Testing**: Jest, Cypress, Playwright
**Infrastructure**: Docker, AWS, CloudFront
```

**Enterprise Java Application:**
```markdown
**Backend**: Java 17, Spring Boot 3.0, Maven
**Database**: PostgreSQL, MongoDB
**Security**: Spring Security, OAuth2, LDAP
**Testing**: JUnit 5, Mockito, TestContainers
**Infrastructure**: Docker, Kubernetes, OpenShift
**Monitoring**: Micrometer, Prometheus, Grafana
```

**Python Data Science Platform:**
```markdown
**Backend**: Python 3.11, FastAPI, SQLAlchemy
**Data**: PostgreSQL, ClickHouse, Redis
**ML/AI**: scikit-learn, TensorFlow, PyTorch
**Testing**: pytest, hypothesis, great-expectations
**Infrastructure**: Docker, Kubernetes, Jupyter
**Monitoring**: MLflow, Weights & Biases
```

**Mobile Application:**
```markdown
**Mobile**: React Native, TypeScript, Expo
**Backend**: Node.js, Express, GraphQL
**Database**: PostgreSQL, MongoDB
**Authentication**: Firebase Auth, Auth0
**Testing**: Jest, Detox, Maestro
**Infrastructure**: AWS, Firebase, CodePush
```

### **Section 3: Team and Collaboration**
*Team structure and collaboration settings*

```markdown
## Team Configuration
- **team_size**: "large_team"
- **development_methodology**: "agile"
- **collaboration_tools**: ["git", "slack", "jira", "figma"]
- **review_process**: "pull_request_required"
- **testing_strategy**: "comprehensive"
- **deployment_frequency**: "daily"
```

#### **Configuration Options:**

**team_size:**
- `"solo"` - Individual developer
- `"small_team"` - 2-5 developers
- `"medium_team"` - 6-15 developers
- `"large_team"` - 16+ developers

**development_methodology:**
- `"agile"` - Scrum, Kanban, iterative development
- `"waterfall"` - Sequential development phases
- `"lean"` - Lean startup methodology
- `"devops"` - DevOps-focused continuous delivery

**testing_strategy:**
- `"basic"` - Unit tests only
- `"standard"` - Unit + integration tests
- `"comprehensive"` - Unit + integration + E2E + performance

**deployment_frequency:**
- `"on_demand"` - Manual deployments
- `"weekly"` - Weekly release cycles
- `"daily"` - Daily deployments
- `"continuous"` - Continuous deployment

### **Section 4: AI Tools Integration**
*MCP tools and AI features configuration*

```markdown
## MCP Tools Integration
- **serena_enabled**: true
- **serena_auto_index**: true
- **serena_analysis_depth**: "deep"
- **context7_enabled**: true
- **context7_auto_generation**: false
- **code_navigation**: "serena_enhanced"

## AI Tools Configuration
- **ai_tools_enabled**: true
- **ai_agent_selector**: "enabled"
- **intelligent_code_analysis**: true
- **auto_agent_recommendations**: true
- **ai_workflow_preference**: "balanced"
```

#### **AI Tools Options:**

**serena_analysis_depth:**
- `"shallow"` - Basic code structure analysis
- `"normal"` - Standard dependency and pattern analysis
- `"deep"` - Comprehensive semantic analysis

**ai_workflow_preference:**
- `"conservative"` - Minimal AI intervention, human control
- `"balanced"` - AI suggestions with human oversight
- `"aggressive"` - Maximum AI automation with validation

**code_navigation:**
- `"standard"` - Basic file navigation
- `"serena_enhanced"` - Intelligent code navigation with Serena
- `"full_ai"` - Complete AI-assisted navigation

### **Section 5: Quality and Standards**
*Code quality, security, and performance requirements*

```markdown
## Quality Standards
- **code_coverage_minimum**: 85
- **security_scan_required**: true
- **performance_budget_enabled**: true
- **accessibility_compliance**: "wcag_aa"
- **code_style_enforcement**: "strict"

## Security Configuration
- **security_framework**: "owasp"
- **vulnerability_scanning**: "automated"
- **compliance_requirements**: ["gdpr", "pci_dss"]
- **security_review_required**: true

## Performance Standards
- **performance_budget**: {
  "first_contentful_paint": "1.5s",
  "largest_contentful_paint": "2.5s",
  "cumulative_layout_shift": "0.1",
  "first_input_delay": "100ms"
}
```

#### **Quality Standards Options:**

**accessibility_compliance:**
- `"none"` - No accessibility requirements
- `"basic"` - Basic accessibility features
- `"wcag_a"` - WCAG 2.1 Level A compliance
- `"wcag_aa"` - WCAG 2.1 Level AA compliance
- `"wcag_aaa"` - WCAG 2.1 Level AAA compliance

**code_style_enforcement:**
- `"none"` - No automated style enforcement
- `"basic"` - Basic linting rules
- `"standard"` - Standard style guide enforcement
- `"strict"` - Strict style guide with zero tolerance

**security_framework:**
- `"owasp"` - OWASP security guidelines
- `"nist"` - NIST cybersecurity framework
- `"iso27001"` - ISO 27001 security standards
- `"custom"` - Custom security framework

### **Section 6: Workflow Configuration**
*Development process and automation settings*

```markdown
## Workflow Configuration
- **git_workflow**: "github_flow"
- **branch_protection**: true
- **automated_testing**: "on_pr"
- **deployment_strategy**: "blue_green"
- **rollback_strategy**: "automatic"

## TODO Management
- **todo_system**: "hierarchical"
- **auto_task_creation**: true
- **milestone_tracking**: true
- **progress_reporting**: "weekly"

## Documentation Standards
- **api_documentation**: "openapi"
- **code_documentation**: "required"
- **user_documentation**: "comprehensive"
- **architecture_documentation**: "c4_model"
```

#### **Workflow Options:**

**git_workflow:**
- `"github_flow"` - Simple feature branch workflow
- `"git_flow"` - Git Flow with develop/master branches
- `"gitlab_flow"` - GitLab Flow with environment branches
- `"trunk_based"` - Trunk-based development

**deployment_strategy:**
- `"rolling"` - Rolling deployments
- `"blue_green"` - Blue-green deployments
- `"canary"` - Canary deployments
- `"recreate"` - Recreate deployments

**todo_system:**
- `"simple"` - Basic task tracking
- `"hierarchical"` - Epic → Feature → Task hierarchy
- `"milestone_based"` - Milestone-driven planning

---

## 🔧 Advanced Configuration Patterns

### **Multi-Environment Configuration**
*Different settings for development, staging, production*

```markdown
## Environment-Specific Configuration

### Development Environment
- **ai_tools_enabled**: true
- **serena_analysis_depth**: "deep"
- **auto_agent_recommendations**: true
- **code_generation_enabled**: true

### Staging Environment
- **ai_tools_enabled**: true
- **serena_analysis_depth**: "normal"
- **auto_agent_recommendations**: false
- **security_scan_required**: true

### Production Environment
- **ai_tools_enabled**: false
- **monitoring_enhanced**: true
- **security_scan_required**: true
- **performance_monitoring**: "real_time"
```

### **Technology-Specific Optimizations**
*Optimized configurations for specific tech stacks*

#### **React/TypeScript Frontend:**
```markdown
## Frontend-Optimized Configuration
- **primary_language**: "typescript"
- **frontend_framework**: "react"
- **ui_library**: "material_ui"
- **state_management**: "redux_toolkit"
- **bundler**: "vite"
- **testing_framework**: "jest_rtl"

## Agent Preferences
- **primary_agents**: ["frontend-engineer", "ux-designer"]
- **secondary_agents**: ["performance-engineer", "qa-engineer"]
```

#### **Node.js/Express Backend:**
```markdown
## Backend-Optimized Configuration
- **primary_language**: "typescript"
- **backend_framework**: "express"
- **orm**: "prisma"
- **validation**: "zod"
- **authentication**: "jwt"
- **api_style**: "rest"

## Agent Preferences
- **primary_agents**: ["api-engineer", "backend-engineer"]
- **secondary_agents**: ["security-engineer", "data-engineer"]
```

#### **Python/FastAPI Application:**
```markdown
## Python-Optimized Configuration
- **primary_language**: "python"
- **backend_framework**: "fastapi"
- **orm**: "sqlalchemy"
- **validation**: "pydantic"
- **async_support**: true
- **api_documentation**: "openapi"

## Agent Preferences
- **primary_agents**: ["api-engineer", "data-engineer"]
- **secondary_agents**: ["performance-engineer", "security-engineer"]
```

### **Scale-Specific Configurations**

#### **Startup Configuration:**
```markdown
## Startup-Optimized Settings
- **project_scale**: "startup"
- **development_methodology**: "lean"
- **testing_strategy**: "standard"
- **deployment_frequency**: "daily"
- **ai_workflow_preference**: "aggressive"
- **code_style_enforcement**: "standard"
- **todo_system**: "simple"
```

#### **Enterprise Configuration:**
```markdown
## Enterprise-Optimized Settings
- **project_scale**: "enterprise"
- **development_methodology**: "agile"
- **testing_strategy**: "comprehensive"
- **deployment_frequency**: "weekly"
- **ai_workflow_preference**: "conservative"
- **code_style_enforcement**: "strict"
- **security_scan_required**: true
- **compliance_requirements**: ["sox", "gdpr", "hipaa"]
- **todo_system**: "hierarchical"
- **architecture_documentation**: "required"
```

---

## 🎯 Configuration Best Practices

### **✅ Essential Best Practices**

1. **Start Minimal** - Begin with basic configuration, expand gradually
2. **Technology Accuracy** - Ensure technology stack matches actual implementation
3. **Regular Updates** - Update configuration as project evolves
4. **Environment Specificity** - Use different configs for dev/staging/prod
5. **Team Alignment** - Ensure entire team understands configuration choices
6. **Documentation** - Document non-obvious configuration decisions
7. **Validation** - Test configuration changes with AI Agent Selector

### **⚠️ Common Configuration Mistakes**

1. **Outdated Technology Stack** - Listing old versions or deprecated tools
2. **Mismatched Scale** - Wrong project_scale for actual team size
3. **Over-Engineering** - Too many tools for simple projects
4. **Under-Engineering** - Insufficient tooling for complex projects
5. **Inconsistent Settings** - Conflicting configuration values
6. **Missing Critical Info** - Incomplete technology or team information
7. **Static Configuration** - Never updating as project grows

### **🔧 Configuration Validation**

#### **Automated Validation:**
```bash
# Test configuration with AI Agent Selector
python ./.ai-tools/core/demo/demo_project_analyzer.py .

# Expected validation output:
# ✅ Configuration valid
# ✅ Technology stack detected correctly
# ✅ Agent recommendations align with settings
# ⚠️  Recommendation: Update Node.js version in config
```

#### **Manual Validation Checklist:**
- [ ] **Technology Stack Current** - All versions up to date
- [ ] **Business Domain Accurate** - Correct domain classification
- [ ] **Team Size Realistic** - Matches actual team
- [ ] **Development Stage Accurate** - Current project phase
- [ ] **Quality Standards Appropriate** - Realistic for project scale
- [ ] **AI Tools Properly Configured** - Tools available and working
- [ ] **Security Requirements Met** - Compliance needs addressed

---

## 📊 Configuration Impact Analysis

### **How Configuration Affects Framework Behavior**

#### **Agent Selection Impact:**
```yaml
Configuration Setting → Agent Recommendation Impact:

business_domain: "fintech" → Higher security-engineer confidence
project_scale: "enterprise" → More governance-focused agents
primary_language: "typescript" → Frontend/backend engineer preferences
testing_strategy: "comprehensive" → Higher qa-engineer priority
```

#### **Workflow Impact:**
```yaml
Configuration Setting → Workflow Behavior:

ai_workflow_preference: "aggressive" → More automated suggestions
security_scan_required: true → Security validation in all workflows
deployment_frequency: "continuous" → More deployment-focused agents
team_size: "large_team" → Coordination-focused recommendations
```

#### **Quality Impact:**
```yaml
Configuration Setting → Quality Standards:

code_coverage_minimum: 85 → Stricter testing requirements
accessibility_compliance: "wcag_aa" → UX/accessibility focus
performance_budget_enabled: true → Performance optimization priority
code_style_enforcement: "strict" → Zero tolerance for style violations
```

---

## 🚨 Troubleshooting Configuration Issues

### **Common Problems and Solutions**

#### **Poor Agent Recommendations:**
```bash
# Problem: AI recommends wrong agents
# Solution: Check technology stack accuracy
grep -E "primary_language|business_domain|project_scale" CLAUDE.md

# Update if incorrect:
# - **primary_language**: "typescript" (not "javascript")
# - **business_domain**: "fintech" (not "web_development")
# - **project_scale**: "enterprise" (not "startup")
```

#### **AI Tools Not Working:**
```bash
# Problem: Serena/Context7 integration failing
# Solution: Verify MCP tools configuration
grep -E "serena_enabled|context7_enabled" CLAUDE.md

# Ensure these are set correctly:
# - **serena_enabled**: true
# - **context7_enabled**: true
# - **ai_tools_enabled**: true
```

#### **Workflow Conflicts:**
```bash
# Problem: Conflicting workflow requirements
# Solution: Check configuration consistency
# Example conflict:
# - **testing_strategy**: "basic"
# - **code_coverage_minimum**: 90
# These conflict - basic testing can't achieve 90% coverage

# Fix by aligning settings:
# - **testing_strategy**: "comprehensive"
# - **code_coverage_minimum**: 90
```

---

## 📚 Configuration Examples

### **Complete Configuration Examples**

#### **Startup SaaS Application:**
```markdown
## Project Metadata
- **project_name**: "taskflow-saas"
- **project_description**: "AI-powered task management SaaS platform"
- **project_version**: "0.8.0"
- **primary_language**: "typescript"
- **business_domain**: "saas"
- **project_scale**: "startup"
- **development_stage**: "development"

## Technologies
**Frontend**: React 18, TypeScript, Next.js 13, Tailwind CSS
**Backend**: Node.js 18, Express, TypeScript, Prisma
**Database**: PostgreSQL 15, Redis
**Authentication**: NextAuth.js, JWT
**Testing**: Jest, Cypress, React Testing Library
**Infrastructure**: Vercel, Railway, AWS S3

## Team Configuration
- **team_size**: "small_team"
- **development_methodology**: "agile"
- **testing_strategy**: "standard"
- **deployment_frequency**: "daily"

## AI Tools Configuration
- **ai_tools_enabled**: true
- **ai_workflow_preference**: "balanced"
- **serena_enabled**: true
- **context7_enabled**: true

## Quality Standards
- **code_coverage_minimum**: 75
- **security_scan_required**: true
- **performance_budget_enabled**: true
- **code_style_enforcement**: "standard"
```

#### **Enterprise Financial Platform:**
```markdown
## Project Metadata
- **project_name**: "fincore-platform"
- **project_description**: "Enterprise financial core banking platform"
- **project_version**: "3.2.1"
- **primary_language**: "java"
- **business_domain**: "fintech"
- **project_scale**: "enterprise"
- **development_stage**: "production"

## Technologies
**Backend**: Java 17, Spring Boot 3.0, Maven
**Database**: PostgreSQL 14, Redis, MongoDB
**Security**: Spring Security, OAuth2, LDAP
**Testing**: JUnit 5, Mockito, TestContainers, Karate
**Infrastructure**: Kubernetes, OpenShift, Jenkins

## Team Configuration
- **team_size**: "large_team"
- **development_methodology**: "agile"
- **testing_strategy**: "comprehensive"
- **deployment_frequency**: "weekly"

## Security Configuration
- **security_framework**: "nist"
- **compliance_requirements**: ["pci_dss", "sox", "gdpr"]
- **security_review_required**: true
- **vulnerability_scanning**: "automated"

## Quality Standards
- **code_coverage_minimum**: 90
- **security_scan_required**: true
- **accessibility_compliance**: "wcag_aa"
- **code_style_enforcement**: "strict"
```

---

**🎯 Next Steps:**

1. **[Framework Customization](framework-customization.md)** - Advanced framework customization
2. **[Custom Agent Development](custom-agent-development.md)** - Create custom agents
3. **[Performance Tuning](performance-tuning.md)** - Optimize framework performance
4. **[Enterprise Deployment](enterprise-deployment.md)** - Scale across organization

**Remember:** Proper CLAUDE.md configuration is foundational to framework effectiveness. Invest time in accurate, detailed configuration for optimal results.