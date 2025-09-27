---
description: Framework Sync
argument-hint: [$ARGUMENTS]
---

Execute framework sync functionality:

1. Parse request: $ARGUMENTS
2. Analyze project context from CLAUDE.md
3. Activate appropriate agents for expertise
4. Perform framework sync operations
5. Generate comprehensive output with actionable results

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- Parse arguments to understand sync target and options
- If remote repository specified: Sync with specified remote
- If specific components mentioned: Sync only those components (e.g., "agents", "prompts", "templates")
- If no arguments or empty: Perform complete framework synchronization with default remote

Output: Complete framework sync results with detailed recommendations.
