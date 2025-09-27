---
description: Todo Epic
argument-hint: [$ARGUMENTS]
---

Execute todo epic functionality:

1. Parse request: $ARGUMENTS
2. Analyze project context from CLAUDE.md
3. Activate appropriate agents for expertise
4. Perform todo epic operations
5. Generate comprehensive output with actionable results

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- Parse arguments to understand epic management request
- If epic name mentioned: Focus on specific epic (create, update, or analyze)
- If action specified: Perform specific action (e.g., "create", "breakdown", "status")
- If no arguments or empty: Display overview of all epics and their status

Output: Complete todo epic results with detailed recommendations.
