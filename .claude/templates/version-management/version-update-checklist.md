# Version Update Checklist

## 📋 Pre-Update Preparation

### 1. Determine Version Type
- [ ] **MAJOR** (X.0.0) - Breaking changes, new architecture, major feature overhauls
- [ ] **MINOR** (0.X.0) - New features, agents, major documentation additions, new capabilities
- [ ] **PATCH** (0.0.X) - Bug fixes, minor documentation updates, setup improvements, small fixes

### 2. Prepare Change Documentation
- [ ] List all changes made since last version
- [ ] Categorize changes (Added, Changed, Fixed, Removed)
- [ ] Use `.claude/templates/version-management/changelog-template.md`

## 🔄 Version Update Process

### Phase 1: File Updates
**Required Files to Update:**

- [ ] **README.md**
  - [ ] Badge: `[![Version](https://img.shields.io/badge/Version-X.X.X`
  - [ ] Text: `**Current Version:** X.X.X | **Release Date:** YYYY-MM-DD`

- [ ] **CLAUDE.md**
  - [ ] Line: `"project_version": "X.X.X"`

- [ ] **CHANGELOG.md**
  - [ ] Add new entry at top using changelog template
  - [ ] Update date and version

- [ ] **docs/README.md**
  - [ ] Check for version references and update if present

### Phase 2: Validation
- [ ] Run version sync validator: `.claude/templates/version-management/version-sync-validator.sh`
- [ ] Verify all version numbers match
- [ ] Check git status for all modified files

### Phase 3: Git Operations
- [ ] Stage all version-related files: `git add README.md CLAUDE.md CHANGELOG.md docs/README.md`
- [ ] Commit with standard message (see template below)
- [ ] Push to GitHub: `git push origin main`

## 📝 Standard Commit Message Template

```
Version X.X.X Release - [Brief Description]

- Updated all version references to X.X.X
- Updated release date to [Current Date]
- [Key changes summary]

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

## ⚠️ Common Mistakes to Avoid

- [ ] **Don't forget CLAUDE.md** - Critical framework file often missed
- [ ] **Check all README files** - Multiple files may contain versions
- [ ] **Update release date** - Not just version number
- [ ] **Validate before commit** - Use sync validator script
- [ ] **Standard commit format** - Use template above

## 🎯 Version Update Examples

### PATCH Release (3.0.0 → 3.0.1)
**Triggers:** Documentation fixes, setup improvements, minor bug fixes
**Files:** README.md, CLAUDE.md, CHANGELOG.md
**Timeline:** Same day as changes

### MINOR Release (3.0.1 → 3.1.0)
**Triggers:** New agents, significant documentation, new features
**Files:** All version files + potential docs updates
**Timeline:** Weekly/bi-weekly

### MAJOR Release (3.1.0 → 4.0.0)
**Triggers:** Framework restructure, breaking changes, major architecture updates
**Files:** All version files + comprehensive documentation review
**Timeline:** Monthly/quarterly

## 🔧 Post-Release Actions

- [ ] Verify GitHub reflects new version
- [ ] Check that badges display correctly
- [ ] Validate documentation links work
- [ ] Test framework functionality if significant changes
- [ ] Update any dependent projects if applicable

---

**Framework Rule:** Always use this checklist for version updates to ensure consistency and completeness.