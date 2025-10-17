# Legacy Agents Backup

**Backup Date**: 2025-10-17
**Reason**: Agent Structure Cleanup - Phase 0 Pre-Skills Preparation
**Original Location**: `.claude/agents/`

## What is This?

This directory contains backup copies of **flat agent files** that were removed during the agent structure cleanup.

### Background

The framework had a duplication issue:
- **90 agent files** instead of expected **45**
- Agents existed in TWO locations:
  - **Hierarchical structure** (correct): `.claude/agents/core/architecture/`, `/development/`, etc.
  - **Flat structure** (duplicate): `.claude/agents/core/*.md`, `/enterprise/*.md`, etc.

### What Was Backed Up

All flat agent files from:
- `.claude/agents/core/*.md` → `legacy-agents/core/` (12 files)
- `.claude/agents/enterprise/*.md` → `legacy-agents/enterprise/` (24 files)
- `.claude/agents/custom/*.md` → `legacy-agents/custom/` (9 files)

**Total**: 45 flat agent stub files

### Why Were They Removed?

**Analysis revealed:**
- Flat files: Oct 5, 2025 - ~1KB each (generic stubs)
- Hierarchical files: Sept 29, 2025 - ~13KB each (complete enterprise agents)

**Conclusion**: Flat files were accidental stubs/placeholders. Hierarchical files are the production-quality implementations.

### Current Structure

After cleanup, framework has **45 agents** in hierarchical structure only:
```
.claude/agents/
├── core/
│   ├── architecture/
│   ├── data/
│   ├── development/
│   ├── management/
│   ├── operations/
│   ├── quality/
│   └── strategy/
├── enterprise/
│   ├── advanced-operations/
│   ├── analytics/
│   ├── governance/
│   ├── infrastructure/
│   ├── integration/
│   ├── management/
│   └── specialized/
└── custom/
    ├── desktop/
    ├── graphics/
    ├── hardware/
    └── scientific/
```

## Recovery

If you need to recover these files:
1. Files are preserved in this directory
2. Copy needed files back to `.claude/agents/`
3. **WARNING**: This will recreate the duplication issue

## Related Tasks

This cleanup was part of **Phase 0: Pre-Skills Foundation** preparation:
- Day 1: Agent Duplication Resolution ✅
- Day 2: Agent Standardization Completion
- Day 3: Task Tool Registry Update

See `FRAMEWORK_ROADMAP.md` for full context.

---

**Framework Version**: 3.9.0+
**Cleanup By**: Phase 0 Preparation - Skills & Extended Thinking Integration
