# 🚀 Framework Version Release Workflow

**Purpose**: Complete workflow for releasing Claude Code Framework with version bump
**Use Case**: Major releases, feature milestones, enterprise updates
**Expected Time**: 15-20 minutes

---

## 📋 **PRE-RELEASE VALIDATION**

### Framework Integrity Check
- [ ] Run template validation: `python3 .claude/monitoring/quality/template-validator.py`
- [ ] Verify 45/45 agents at 100% compliance
- [ ] Run quality assessment: `python3 .claude/monitoring/quality/quality-assessor.py`
- [ ] Check current quality score (maintain 100/100)
- [ ] Test AI tools system: `./ai-tools.sh` (system status check)
- [ ] Verify monitoring dashboards are operational

### Documentation Consistency
- [ ] Verify all agent counts accurate (45 total: 12 core + 24 enterprise + 9 custom)
- [ ] Check framework status claims match reality
- [ ] Validate all file paths in documentation exist
- [ ] Confirm cross-references are accurate
- [ ] Test all example commands in docs

---

## 🔢 **VERSION UPDATE PROCESS**

### Core Framework Files
- [ ] Update `CLAUDE.md`: `project_version: "X.X.X"`
- [ ] Update `README.md`: Version badge URL and "Current Version" field
- [ ] Check if `CHANGELOG.md` pattern needs version update
- [ ] Verify `package.json` or similar files for version consistency

### Agent Version Updates (45 files)
- [ ] Update "Framework Version: X.X.X" in all agent files
- [ ] Use batch update or manual verification for consistency
- [ ] Confirm template version alignment if template changed

### Python Tools Updates
- [ ] Update version in `.claude/monitoring/quality/*.py` files if they contain version info
- [ ] Check AI tools scripts for version references
- [ ] Update any version-specific configurations

### Template and Configuration Updates
- [ ] Update `.claude/templates/agent_template.md` framework version if changed
- [ ] Check any version references in hooks or scripts
- [ ] Verify MCP tools configurations don't have hardcoded versions

---

## 📚 **DOCUMENTATION UPDATES**

### CHANGELOG Updates
- [ ] Add new version section to `CHANGELOG.md`
- [ ] Document all major changes, features, and fixes
- [ ] Include framework status improvements
- [ ] Add business impact and metrics if significant

### ROADMAP Updates
- [ ] Mark completed items in `FRAMEWORK_ROADMAP.md`
- [ ] Update completion percentages and status
- [ ] Add new priorities if framework direction changed
- [ ] Update enterprise readiness metrics

### README and Core Docs
- [ ] Update feature counts and metrics in `README.md`
- [ ] Refresh framework status and achievements
- [ ] Update quality scores and compliance rates
- [ ] Verify all badges and links work correctly

---

## 🔍 **QUALITY ASSURANCE**

### Final Validation Suite
- [ ] Re-run template validation to confirm 100% compliance
- [ ] Execute quality assessment for final score
- [ ] Test critical framework functions (agent discovery, setup wizard)
- [ ] Verify monitoring systems operational
- [ ] Quick smoke test of AI tools functionality

### Cross-System Integration
- [ ] Test TodoWrite integration if framework components changed
- [ ] Verify MCP tools integration (Serena, Context7, Playwright)
- [ ] Check session management and state preservation
- [ ] Confirm Git integration and automation works

---

## 📦 **GIT RELEASE PROCESS**

### Pre-Commit Preparation
- [ ] Review `git status` - identify all changed files
- [ ] Verify staged vs unstaged changes are appropriate
- [ ] Check for any untracked files that should be included
- [ ] Confirm no sensitive information in commits

### Release Commit
- [ ] `git add .` (or selective staging if preferred)
- [ ] Create release commit with format:
  ```
  Framework vX.X.X - [Brief Description of Major Changes]

  - [Key feature/improvement 1]
  - [Key feature/improvement 2]
  - [Key feature/improvement 3]

  Framework Status:
  - XX/XX agents (100% compliance)
  - XXX/100 quality score
  - [Other key metrics]

  🤖 Generated with [Claude Code](https://claude.ai/code)

  Co-Authored-By: Claude <noreply@anthropic.com>
  ```

### GitHub Push and Verification
- [ ] `git push origin main`
- [ ] Verify push completed successfully
- [ ] Check GitHub repository reflects latest changes
- [ ] Consider creating release tag if major version
- [ ] Verify GitHub Actions/workflows if they exist

---

## ✅ **POST-RELEASE VERIFICATION**

### Framework Status Confirmation
- [ ] Quick validation that all systems operational
- [ ] Confirm version consistency across all files
- [ ] Test framework from fresh perspective (new session)
- [ ] Verify documentation matches actual functionality

### Communication and Follow-up
- [ ] Update any external references to framework version
- [ ] Consider announcement if significant milestone
- [ ] Document lessons learned from release process
- [ ] Plan next development phase if needed

---

## 🎯 **SUCCESS CRITERIA**

**Release is successful when:**
- ✅ All validation checks pass
- ✅ Version consistency across entire framework
- ✅ Documentation accurately reflects capabilities
- ✅ GitHub repository updated and accessible
- ✅ Framework functionality confirmed operational
- ✅ Quality metrics maintained or improved

**Common Issues to Watch:**
- ⚠️ Missed version updates in agent files
- ⚠️ Documentation claims not matching reality
- ⚠️ Broken cross-references after structural changes
- ⚠️ Quality regression due to incomplete testing

---

*Use this checklist with TodoWrite for progress tracking and team coordination*