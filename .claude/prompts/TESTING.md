# Drag-and-Drop Workflow Testing Guide

## 🧪 Testing the Hybrid Initialization System

### Test Scenarios

#### Scenario 1: New Project (Empty Directory)
```bash
mkdir test-new-project
cd test-new-project
# Drag .claude/prompts/init/new-project.md to Claude
```

**Expected Behavior:**
- Claude asks for: project name, language, domain, scale
- Creates CLAUDE.md with metadata section populated
- Creates .serena/project.yml with filled placeholders
- Runs `serena onboarding`
- Creates basic project structure
- No errors, ready to use

#### Scenario 2: Existing Python Project
```bash
mkdir test-existing-python
cd test-existing-python
echo "flask==2.0.0" > requirements.txt
touch app.py
echo "# My Python App" > README.md
# Drag .claude/prompts/init/existing-project.md to Claude
```

**Expected Behavior:**
- Claude detects Python, Flask
- Asks minimal questions (project name, domain)
- Creates CLAUDE.md reflecting existing setup
- Sets up Serena with language: python
- Does NOT modify existing files
- Provides integration recommendations

#### Scenario 3: Existing Project with CLAUDE.md
```bash
mkdir test-existing-with-claude
cd test-existing-with-claude
# Copy existing CLAUDE.md with populated metadata
# Drag .claude/prompts/init/existing-project.md to Claude
```

**Expected Behavior:**
- Claude reads existing CLAUDE.md
- Uses existing metadata, asks nothing
- Updates only agent framework components
- Preserves all existing configuration
- Focuses on pure integration

### Dynamic Field Testing

#### Test: Placeholder Replacement in Templates

**Before (Template):**
```yaml
project_name: "{project_name}"
language: {language}
initial_prompt: |
  You are working on the {project_name} project.
  - Language: {language}
  - Domain: {business_domain}
```

**After (Generated for "MyApp", Python, FinTech):**
```yaml
project_name: "MyApp"
language: python
initial_prompt: |
  You are working on the MyApp project.
  - Language: python
  - Domain: fintech
```

#### Test: CLAUDE.md Metadata Population

**Template Section:**
```markdown
## 0. Project Metadata
- **project_name**: [project name, e.g., "task-manager-app"]
- **primary_language**: [main language: csharp, python, rust, java, typescript, go, cpp, ruby]
- **business_domain**: [domain: ecommerce, fintech, healthcare, saas, enterprise, iot, etc.]
```

**After Population:**
```markdown
## 0. Project Metadata
- **project_name**: MyApp
- **primary_language**: python
- **business_domain**: fintech
- **project_scale**: startup
- **development_stage**: mvp
```

### Integration Points Testing

#### Test: Context Detection
1. **Empty directory** → New project flow
2. **Has package.json** → Node.js detected, existing project flow
3. **Has requirements.txt** → Python detected, existing project flow
4. **Has .csproj** → C# detected, existing project flow
5. **Has CLAUDE.md** → Read metadata, minimal questions

#### Test: Safety Guarantees
- **NO modification** of existing source files
- **NO changes** to package.json/requirements.txt/etc.
- **ONLY additions** of .claude/ and .serena/ directories
- **READ-ONLY analysis** first in existing projects

### Error Handling Testing

#### Test: Invalid Language Detection
```bash
# Create project with ambiguous files
touch main.py
touch app.js
touch main.go
# Should ask which language is primary
```

#### Test: Missing Serena
```bash
# Test without Serena installed
# Should provide installation instructions
# Should offer alternative setup
```

#### Test: Permission Issues
```bash
# Test in read-only directory
# Should handle gracefully
# Should suggest alternative approach
```

### Success Criteria

#### New Project Success
- ✅ CLAUDE.md created and populated
- ✅ .serena/project.yml created with no {placeholders}
- ✅ Serena initialization successful
- ✅ All 11 agents can access project context
- ✅ Basic project structure appropriate for tech stack

#### Existing Project Success  
- ✅ No existing files modified
- ✅ CLAUDE.md reflects current project accurately
- ✅ Serena integration works alongside existing tools
- ✅ Agent framework adds value without disruption
- ✅ Clear adoption roadmap provided

#### Template System Success
- ✅ All {placeholders} replaced with actual values
- ✅ No template artifacts left in generated files
- ✅ Context properly propagated to all agents
- ✅ Dynamic content makes sense for project type

### Manual Testing Checklist

#### Before Testing
- [ ] Have Serena installed and working
- [ ] Have Context7 available for comparison
- [ ] Clean test directories prepared
- [ ] Various project types ready for testing

#### During Testing
- [ ] Drag-and-drop works without editing prompts
- [ ] Questions asked are minimal and relevant
- [ ] Generated files have no placeholder artifacts
- [ ] Existing files remain unchanged (when appropriate)
- [ ] Error messages are helpful and actionable

#### After Testing
- [ ] All generated files are valid and usable
- [ ] Agents can successfully access project context
- [ ] Serena onboarding completes successfully
- [ ] Integration feels seamless and valuable
- [ ] Documentation matches actual behavior

### Regression Testing

#### Test: Template Changes
- Modify CLAUDE.md template
- Verify new projects get updates
- Verify existing projects remain stable

#### Test: New Agent Addition
- Add 12th agent to framework
- Verify templates update correctly
- Verify existing projects can adopt new agent

#### Test: Workflow Changes
- Update 5-phase workflow
- Verify prompts reflect changes
- Verify agent coordination remains intact

This testing framework ensures the hybrid initialization system works reliably for both new and existing projects with minimal user friction.