# Claude Code Framework - Versioning Rules

## 📋 Semantic Versioning Standard

**Format:** `MAJOR.MINOR.PATCH` (e.g., 3.0.1)

Based on [Semantic Versioning 2.0.0](https://semver.org/) with framework-specific interpretations.

## 🔢 Version Number Guidelines

### MAJOR Version (X.0.0)
**When to increment:**
- Breaking changes to framework structure
- Major architectural redesign
- Incompatible changes to CLAUDE.md format
- Agent system restructure
- Changes requiring user migration effort

**Examples:**
- `2.0.0 → 3.0.0`: Complete agent system overhaul
- Framework directory structure changes
- Incompatible prompt format changes
- CLAUDE.md specification breaking changes

**Timeline:** Quarterly or as needed for major releases

### MINOR Version (0.X.0)
**When to increment:**
- New agents added to framework
- New major features or capabilities
- Significant documentation additions
- New framework components or tools
- Backward-compatible enhancements

**Examples:**
- `3.0.0 → 3.1.0`: Added 5 new specialized agents
- New AI-powered agent selection system
- Major documentation restructure
- New MCP tools integration
- Interactive setup wizard addition

**Timeline:** Monthly or when substantial features are ready

### PATCH Version (0.0.X)
**When to increment:**
- Bug fixes and minor corrections
- Documentation improvements and clarifications
- Setup process improvements
- Small template updates
- Configuration file fixes
- README updates and badge corrections

**Examples:**
- `3.0.0 → 3.0.1`: Fixed MCP tools documentation
- Setup script improvements
- Typo corrections in documentation
- Minor template adjustments
- Configuration file updates

**Timeline:** As needed, typically within days of issues

## 🎯 Framework-Specific Rules

### Documentation-Only Changes
**Rule:** Documentation improvements warrant PATCH version increment
**Rationale:** User-facing changes that improve framework usability

### Agent Additions/Modifications
- **New agent:** MINOR version
- **Agent improvement:** PATCH version
- **Agent removal/breaking change:** MAJOR version

### Template and Configuration Changes
- **New template:** MINOR version
- **Template improvement:** PATCH version
- **Breaking template change:** MAJOR version

### Setup and Installation Changes
- **New setup tools:** MINOR version
- **Setup improvements:** PATCH version
- **Breaking setup changes:** MAJOR version

## 📅 Release Schedule Guidelines

### Development Flow
```
Daily Work → Accumulate → Version Decision → Release
```

### Timing Recommendations
- **PATCH:** Release immediately when fixing user-impacting issues
- **MINOR:** Bundle features, release monthly or when complete
- **MAJOR:** Plan carefully, coordinate with roadmap, quarterly timing

### Emergency Releases
**Hotfix Process:**
1. Critical bug discovered
2. Create immediate PATCH release
3. Follow full version update checklist
4. Document emergency nature in CHANGELOG

## 🚫 Anti-Patterns to Avoid

### Version Increment Mistakes
- ❌ **Skipping versions** (3.0.0 → 3.0.2 without 3.0.1)
- ❌ **Wrong increment type** (PATCH for new features)
- ❌ **Multiple increments** (changing both MINOR and PATCH)
- ❌ **Rollback versions** (going backward in numbering)

### Change Classification Errors
- ❌ **Documentation as MAJOR** (unless breaking format changes)
- ❌ **Bug fixes as MINOR** (should be PATCH)
- ❌ **New agents as PATCH** (should be MINOR)

## 📊 Version Decision Matrix

| Change Type | Impact | Version | Example |
|-------------|--------|---------|---------|
| New Agent | Medium | MINOR | Added `graphics-3d-engineer` |
| Bug Fix | Low | PATCH | Fixed MCP tools empty screen |
| Documentation | Low | PATCH | Added setup guide |
| New Feature | Medium | MINOR | AI agent selection system |
| Breaking Change | High | MAJOR | CLAUDE.md format change |
| Framework Restructure | High | MAJOR | Directory layout change |
| Setup Improvement | Low | PATCH | Better error messages |
| Template Addition | Medium | MINOR | New project template |

## 🔄 Version Update Workflow Integration

### Before Making Changes
1. Consider version impact of planned changes
2. Group related changes for single version
3. Plan version increment type

### After Making Changes
1. Use `.claude/templates/version-management/version-update-checklist.md`
2. Follow semantic versioning rules
3. Validate with version sync checker

### Communication
- **MAJOR:** Announce in advance, document migration
- **MINOR:** Document new features clearly
- **PATCH:** Simple changelog entry sufficient

---

**Framework Standard:** All version decisions must follow these rules to ensure predictable, semantic versioning for users and contributors.