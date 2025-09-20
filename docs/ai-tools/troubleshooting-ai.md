# AI Tools Troubleshooting Guide

*Quick solutions for common AI tools issues*

## 🎯 Quick Diagnostic

**Having AI tools issues? Start here:**

```bash
# Quick system check
echo "=== AI TOOLS DIAGNOSTIC ==="
echo "1. Framework structure:"
ls -la .claude/ .ai-tools/ 2>/dev/null

echo "2. AI Agent Selector:"
python ./.ai-tools/core/demo/demo_project_analyzer.py . 2>&1 | head -5

echo "3. Python dependencies:"
python -c "import pandas, numpy, scikit_learn" 2>/dev/null && echo "✅ ML dependencies OK" || echo "❌ Missing ML dependencies"

echo "4. Project configuration:"
grep -E "ai_tools|serena|context" CLAUDE.md 2>/dev/null || echo "❌ No AI configuration in CLAUDE.md"
```

## 🚨 Common Issues & Quick Fixes

### **Issue 1: AI Agent Selector Not Working**

#### **Symptoms:**
- No agent recommendations
- Error: "ModuleNotFoundError" when running project analyzer
- Empty analysis results

#### **Diagnosis:**
```bash
# Test AI agent selector
python ./.ai-tools/core/demo/demo_project_analyzer.py .

# Check for specific errors:
# - Import errors → Missing dependencies
# - No output → Project structure issues
# - Wrong recommendations → Configuration problems
```

#### **Solutions:**

**Fix 1: Install missing dependencies**
```bash
# Install required Python packages
pip install pandas numpy scikit-learn joblib

# Or if using the virtual environment
./.ai-tools/venv/bin/pip install pandas numpy scikit-learn joblib
```

**Fix 2: Fix project structure detection**
```bash
# Ensure project has recognizable structure
ls package.json requirements.txt pom.xml go.mod 2>/dev/null

# If no config files, create minimal one:
# For Node.js projects:
echo '{"name":"my-project","version":"1.0.0"}' > package.json

# For Python projects:
echo "# Project dependencies" > requirements.txt
```

**Fix 3: Manual configuration fallback**
```markdown
# Add to CLAUDE.md
## AI Tools Configuration
- **ai_tools_enabled**: true
- **fallback_mode**: "rule_based"
- **manual_agent_selection**: true
```

---

### **Issue 2: Serena Integration Problems**

#### **Symptoms:**
- "Serena not found" errors
- Serena commands not working
- Project indexing failures

#### **Diagnosis:**
```bash
# Check Serena installation
ls .serena/ 2>/dev/null && echo "✅ Serena directory exists" || echo "❌ No .serena directory"
ls .serena/project.yml 2>/dev/null && echo "✅ Project indexed" || echo "❌ Project not indexed"

# Test Serena functionality
serena status 2>/dev/null || echo "❌ Serena command not available"
```

#### **Solutions:**

**Fix 1: Initialize Serena for project**
```bash
# If Serena is installed but not initialized
serena init .
serena index

# Verify initialization
ls .serena/
cat .serena/project.yml
```

**Fix 2: Use framework without Serena**
```markdown
# Configure CLAUDE.md for non-Serena operation
## MCP Tools Integration
- **serena_enabled**: false
- **use_builtin_analysis**: true
- **code_navigation**: "standard"
```

**Fix 3: Alternative code navigation**
```bash
# Use built-in framework navigation
"Analyze project structure using built-in tools"
"Use standard code analysis instead of Serena"
```

---

### **Issue 3: Context7 Integration Issues**

#### **Symptoms:**
- Context7 commands not working
- Code generation failures
- "Context7 not available" messages

#### **Diagnosis:**
```bash
# Check Context7 availability
context7 --version 2>/dev/null || echo "❌ Context7 not installed"

# Check framework integration
grep -i context7 .claude/settings.local.json 2>/dev/null || echo "No Context7 configuration"
```

#### **Solutions:**

**Fix 1: Use framework without Context7**
```bash
# Framework works without Context7 - use manual code generation
"Generate code manually using frontend-engineer agent"
"Create component structure using built-in templates"
```

**Fix 2: Alternative code generation**
```markdown
# Configure for manual development
## Development Approach
- **code_generation**: "manual"
- **use_templates**: true
- **scaffolding_method**: "framework_prompts"
```

---

### **Issue 4: Poor Agent Recommendations**

#### **Symptoms:**
- Incorrect agent suggestions
- Recommendations don't match your project
- Missing important agents in recommendations

#### **Diagnosis:**
```bash
# Check project detection accuracy
python ./.ai-tools/core/demo/demo_project_analyzer.py . | grep -A 10 "PROJECT ANALYSIS"

# Common issues:
# - Wrong technology detection
# - Incorrect complexity assessment
# - Missing business domain
```

#### **Solutions:**

**Fix 1: Improve project detection**
```markdown
# Enhance CLAUDE.md with specific details
## Project Metadata
- **primary_language**: "typescript" # Be specific
- **secondary_languages**: ["python", "sql"] # Add all languages
- **main_frameworks**: ["react", "express", "postgresql"] # List all major frameworks
- **business_domain**: "fintech" # Be specific about domain
- **project_scale**: "sme" # startup, sme, enterprise
- **team_size**: "small_team" # solo, small_team, large_team
- **development_stage**: "active_development" # planning, development, maintenance, legacy

## Current Technology Stack
**Frontend**: React 18, TypeScript, Next.js 13, Tailwind CSS
**Backend**: Node.js 18, Express 4.18, TypeScript
**Database**: PostgreSQL 15, Redis 7
**Infrastructure**: Docker, Kubernetes, AWS
**Testing**: Jest, Cypress, Supertest
**CI/CD**: GitHub Actions, Docker Hub
```

**Fix 2: Manual agent override**
```bash
# Override AI recommendations when needed
"I want to use security-engineer and frontend-engineer for this task"
"Activate api-engineer instead of suggested backend-engineer"
"Use qa-engineer for quality review regardless of recommendations"
```

**Fix 3: Feedback loop improvement**
```bash
# Provide feedback to improve future recommendations
"The recommended agents worked well for this React project"
"Backend-engineer was better than api-engineer for this task"
"Security-engineer should be included for all fintech projects"
```

---

### **Issue 5: Framework Performance Issues**

#### **Symptoms:**
- Slow agent activation
- Long analysis times
- Framework becomes unresponsive

#### **Diagnosis:**
```bash
# Check system resources
echo "=== PERFORMANCE DIAGNOSTIC ==="
echo "Memory usage:"
ps aux | grep python | head -5

echo "Disk space:"
df -h .

echo "File count in .ai-tools:"
find .ai-tools -type f | wc -l
```

#### **Solutions:**

**Fix 1: Optimize AI tools cache**
```bash
# Clear AI tools cache
rm -rf .ai-tools/core/data/cache/
rm -rf .ai-tools/core/models/cache/

# Restart with fresh cache
python ./.ai-tools/core/demo/demo_project_analyzer.py .
```

**Fix 2: Reduce analysis scope**
```markdown
# Configure lighter analysis
## Performance Settings
- **analysis_depth**: "basic" # basic, standard, comprehensive
- **cache_enabled**: true
- **background_analysis**: false
- **real_time_updates**: false
```

**Fix 3: Selective AI features**
```bash
# Disable heavy features if not needed
echo "AI_DEEP_ANALYSIS=false" >> .env
echo "ML_RECOMMENDATIONS=basic" >> .env
```

---

### **Issue 6: Environment and Dependencies**

#### **Symptoms:**
- Import errors in Python scripts
- "Command not found" errors
- Version compatibility issues

#### **Diagnosis:**
```bash
# Check Python environment
python --version
which python

# Check package installation
pip list | grep -E "pandas|numpy|scikit|joblib"

# Check framework structure
ls -la .ai-tools/core/
ls -la .claude/agents/
```

#### **Solutions:**

**Fix 1: Virtual environment setup**
```bash
# Create dedicated virtual environment
python -m venv .ai-tools/venv
source .ai-tools/venv/bin/activate  # Linux/Mac
# or .ai-tools/venv/Scripts/activate  # Windows

# Install requirements
pip install -r .ai-tools/requirements.txt
```

**Fix 2: System-wide installation**
```bash
# Install globally if virtual environment issues
pip install --user pandas numpy scikit-learn joblib

# Or using conda
conda install pandas numpy scikit-learn joblib
```

**Fix 3: Alternative Python versions**
```bash
# Try with different Python version
python3 ./.ai-tools/core/demo/demo_project_analyzer.py .
python3.9 ./.ai-tools/core/demo/demo_project_analyzer.py .
python3.11 ./.ai-tools/core/demo/demo_project_analyzer.py .
```

---

## 🛡️ Fallback Strategies

### **When AI Tools Completely Fail:**

#### **Strategy 1: Rule-Based Agent Selection**
```bash
# Use manual agent selection based on project type
# Web frontend → frontend-engineer
# REST API → api-engineer
# Database work → data-engineer
# Security concerns → security-engineer
# Quality assurance → qa-engineer
```

#### **Strategy 2: Framework Core Functionality**
```bash
# Framework works without AI tools
"Use framework core features without AI assistance"
"Activate agents manually based on task requirements"
"Use prompts directly without AI recommendations"
```

#### **Strategy 3: Gradual AI Re-enablement**
```bash
# Start with basic features and add complexity
1. Get basic framework working
2. Test simple agent activation
3. Add AI agent selector when stable
4. Integrate external tools (Serena, Context7) last
```

---

## 📋 Diagnostic Commands Reference

### **Quick Health Check:**
```bash
# Complete framework diagnostic
echo "=== CLAUDE CODE FRAMEWORK DIAGNOSTIC ==="
echo "Framework structure:" && ls -la .claude/ .ai-tools/ 2>/dev/null
echo "Python environment:" && python --version && which python
echo "AI dependencies:" && python -c "import pandas, numpy; print('✅ AI deps OK')" 2>/dev/null || echo "❌ Missing AI dependencies"
echo "Project detection:" && python ./.ai-tools/core/demo/demo_project_analyzer.py . 2>&1 | head -3
echo "Configuration:" && grep -E "project_name|primary_language" CLAUDE.md 2>/dev/null
```

### **Performance Analysis:**
```bash
# Framework performance check
echo "=== PERFORMANCE ANALYSIS ==="
time python ./.ai-tools/core/demo/demo_project_analyzer.py . >/dev/null
echo "File count:" && find . -name "*.py" -o -name "*.js" -o -name "*.ts" | wc -l
echo "Cache size:" && du -sh .ai-tools/core/data/ 2>/dev/null || echo "No cache"
```

### **Configuration Validation:**
```bash
# Validate framework configuration
echo "=== CONFIGURATION VALIDATION ==="
echo "CLAUDE.md exists:" && ls CLAUDE.md >/dev/null && echo "✅" || echo "❌"
echo "Required metadata:" && grep -E "project_name|primary_language|business_domain" CLAUDE.md >/dev/null && echo "✅" || echo "❌"
echo "Agent directory:" && ls .claude/agents/ >/dev/null && echo "✅" || echo "❌"
echo "Prompts directory:" && ls .claude/prompts/ >/dev/null && echo "✅" || echo "❌"
```

---

## 🆘 Emergency Procedures

### **Complete Framework Reset:**
```bash
# Nuclear option - start fresh
echo "⚠️  WARNING: This will reset all framework configuration"
read -p "Continue? (y/N): " confirm
if [[ $confirm == [yY] ]]; then
    # Backup current configuration
    mv .claude .claude.backup.$(date +%Y%m%d-%H%M%S)
    mv .ai-tools .ai-tools.backup.$(date +%Y%m%d-%H%M%S)
    mv CLAUDE.md CLAUDE.md.backup.$(date +%Y%m%d-%H%M%S)

    # Fresh installation
    # [Re-run installation steps from getting-started guide]
    echo "Framework reset complete - follow getting-started guide to reconfigure"
fi
```

### **Safe Mode Operation:**
```bash
# Run framework in safe mode (no AI, basic functionality)
export CLAUDE_SAFE_MODE=true
export AI_TOOLS_DISABLED=true

# Use framework with minimal features
"Use framework in safe mode without AI assistance"
```

---

## 📞 Getting Help

### **Self-Help Resources:**
1. **[Installation Guide](../getting-started/installation.md)** - Reinstall framework components
2. **[Configuration Guide](../advanced/claude-md-configuration.md)** - Fix configuration issues
3. **[Framework Architecture](../advanced/framework-architecture.md)** - Understand system design

### **Community Support:**
1. **Framework Documentation** - Check latest docs for known issues
2. **GitHub Issues** - Search for similar problems and solutions
3. **Team Knowledge** - Check with team members for working configurations

### **Advanced Debugging:**
```bash
# Enable debug logging
export CLAUDE_DEBUG=true
export AI_TOOLS_DEBUG=true

# Run with verbose output
python -v ./.ai-tools/core/demo/demo_project_analyzer.py .

# Capture full diagnostic information
./debug_framework.sh > framework_diagnostic.log 2>&1
```

---

**🎯 Remember:** Most AI tools issues are environment or configuration related. The framework core functionality works even when AI tools have problems. Start with basic features and add AI capabilities incrementally.

**Next steps after resolving issues:**
- **[AI Tools Overview](ai-tools-overview.md)** - Return to AI tools guide
- **[Serena Integration](serena-integration.md)** - Set up Serena properly
- **[Context7 Integration](context7-integration.md)** - Configure Context7 integration