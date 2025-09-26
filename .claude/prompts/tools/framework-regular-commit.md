# 📦 Framework Regular Commit Workflow

**Purpose**: Standard workflow for regular commits without version changes
**Use Case**: Feature development, bug fixes, documentation updates, code improvements
**Expected Time**: 5-10 minutes

---

## 🔍 **CHANGE ASSESSMENT**

### Identify Modified Components
- [ ] Run `git status` to see all changed files
- [ ] Categorize changes:
  - **Agents**: `.claude/agents/` modifications
  - **Prompts**: `.claude/prompts/` additions/updates
  - **Documentation**: `docs/`, `README.md`, `CHANGELOG.md` changes
  - **Tools**: `.claude/monitoring/`, `ai-tools.sh`, scripts
  - **Core Config**: `CLAUDE.md`, `FRAMEWORK_ROADMAP.md`

### Impact Analysis
- [ ] Determine scope: single component vs multi-component
- [ ] Assess if changes affect framework functionality
- [ ] Check if documentation updates are needed
- [ ] Identify any breaking changes or new requirements

---

## 📚 **TARGETED UPDATES**

### Documentation Maintenance
- [ ] **If agents modified**: Verify agent count accuracy in README.md (45 total)
- [ ] **If new features added**: Update relevant sections in README.md
- [ ] **If workflow changed**: Update documentation in `docs/` directory
- [ ] **If progress made**: Update `FRAMEWORK_ROADMAP.md` completion status
- [ ] Check cross-references in modified files are still accurate

### Quality Documentation
- [ ] **If quality improved**: Update quality scores if measurable improvement
- [ ] **If agents standardized**: Update compliance percentages
- [ ] **If new capabilities**: Ensure enterprise readiness claims accurate
- [ ] Update any outdated status claims in documentation

---

## 🔍 **FOCUSED VALIDATION**

### Component-Specific Checks
- [ ] **If agents changed**: Run template validation for affected agents
  ```bash
  python3 .claude/monitoring/quality/template-validator.py
  ```
- [ ] **If monitoring tools updated**: Test monitoring functionality
- [ ] **If AI tools modified**: Quick test of `./ai-tools.sh` functionality
- [ ] **If prompts added**: Verify prompt structure and binding

### Cross-Component Integration
- [ ] Check that modified components integrate properly
- [ ] Verify no broken internal links or references
- [ ] Test critical paths if core functionality touched
- [ ] Ensure TodoWrite integration intact if workflow modified

---

## 📦 **GIT COMMIT PROCESS**

### Pre-Commit Review
- [ ] Review `git status` output carefully
- [ ] Check `git diff` for unintended changes
- [ ] Verify staged vs unstaged files are correct
- [ ] Confirm no sensitive information in changes
- [ ] Remove any temporary or debug files

### Staging and Commit Preparation
- [ ] Stage appropriate files: `git add [specific files]` or `git add .`
- [ ] Verify staging area with `git status`
- [ ] Prepare clear, descriptive commit message

### Commit Message Creation
- [ ] Use format:
  ```
  [Component] Brief description of changes

  - Specific change or improvement 1
  - Specific change or improvement 2
  - Additional context if needed

  🤖 Generated with [Claude Code](https://claude.ai/code)

  Co-Authored-By: Claude <noreply@anthropic.com>
  ```
- [ ] Component examples: `[Agents]`, `[Docs]`, `[Tools]`, `[Prompts]`, `[Quality]`

### Execute Commit and Push
- [ ] Execute commit with prepared message
- [ ] Push to GitHub: `git push origin main`
- [ ] Verify push completed successfully

---

## ✅ **VERIFICATION**

### GitHub Sync Confirmation
- [ ] Check GitHub repository shows latest commit
- [ ] Verify all changed files appear correctly
- [ ] Confirm commit message displays properly
- [ ] Check no merge conflicts or issues

### Basic Functionality Check
- [ ] Quick test of modified functionality if applicable
- [ ] Verify documentation changes render correctly
- [ ] Confirm framework still operational
- [ ] Test any new features or fixes

---

## 🎯 **WHEN TO ESCALATE TO VERSION RELEASE**

**Consider version bump if changes include:**
- ⚡ Major new features or capabilities
- 🏗️ Structural framework changes
- 📊 Significant quality improvements
- 🎯 Enterprise readiness milestones
- 🔧 Breaking changes or API modifications

**Indicators for version release workflow:**
- Multiple component categories affected
- Documentation claims significant improvements
- Quality metrics substantially improved
- New enterprise capabilities added

---

## 🚨 **COMMON GOTCHAS**

**Watch out for:**
- ❌ Forgetting to update README.md agent counts after agent changes
- ❌ Leaving TODO comments or debug code in commits
- ❌ Breaking cross-references when moving files
- ❌ Inconsistent formatting in modified agents
- ❌ Outdated status claims in documentation
- ❌ Missing integration testing after multi-component changes

**Quick fixes:**
- ✅ Use `grep -r "45 agents"` to find agent count references
- ✅ Search for "TODO", "FIXME", "DEBUG" before committing
- ✅ Test internal links in modified documentation
- ✅ Run template validator if unsure about agent compliance

---

*Use this checklist for consistent, quality commits that maintain framework integrity*