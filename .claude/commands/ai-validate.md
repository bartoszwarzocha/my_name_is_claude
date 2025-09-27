---
description: Quick quality validation without full menu
argument-hint: [--scope=area] [--fix-issues]
---

Perform rapid AI-powered quality validation:

1. Execute quality gates from .ai-tools/validation/
2. Scan codebase for common quality issues
3. Validate against project standards in CLAUDE.md
4. Check framework compliance and best practices
5. Run automated quality metrics
6. Generate validation report with:
   - Quality score (0-100)
   - Critical violations requiring immediate fix
   - Quality recommendations
   - Code standards compliance
   - Framework integration status

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- If arguments contain "--scope=area": Focus validation on specific area (e.g., "--scope=code", "--scope=architecture", "--scope=security")
- If arguments contain "--fix-issues": Automatically attempt to fix detected issues where possible
- If no arguments or empty: Perform comprehensive quality validation across all areas

Output: Concise quality report with actionable improvement items and compliance status.