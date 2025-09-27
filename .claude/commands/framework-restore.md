---
description: Framework Restore
argument-hint: [$ARGUMENTS]
---

Execute framework restore functionality:

1. Parse request: $ARGUMENTS
2. Analyze project context from CLAUDE.md
3. Activate appropriate agents for expertise
4. Perform framework restore operations
5. Generate comprehensive output with actionable results

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- Parse arguments to understand restore source and options
- If backup file/path specified: Restore from specified backup
- If specific components mentioned: Restore only those components (e.g., "agents", "prompts", "config")
- If no arguments or empty: Restore from latest complete framework backup

Output: Complete framework restore results with detailed recommendations.
