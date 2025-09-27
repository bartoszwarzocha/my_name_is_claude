---
description: Framework Backup
argument-hint: [$ARGUMENTS]
---

Execute framework backup functionality:

1. Parse request: $ARGUMENTS
2. Analyze project context from CLAUDE.md
3. Activate appropriate agents for expertise
4. Perform framework backup operations
5. Generate comprehensive output with actionable results

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- Parse arguments to understand backup scope and options
- If specific components mentioned: Backup only those components (e.g., "agents", "prompts", "config")
- If backup location specified: Use specified backup destination
- If no arguments or empty: Perform complete framework backup with default settings

Output: Complete framework backup results with detailed recommendations.
