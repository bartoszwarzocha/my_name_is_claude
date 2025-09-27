---
description: Todo Agent Tasks
argument-hint: [$ARGUMENTS]
---

Execute todo agent tasks functionality:

1. Parse request: $ARGUMENTS
2. Analyze project context from CLAUDE.md
3. Activate appropriate agents for expertise
4. Perform todo agent tasks operations
5. Generate comprehensive output with actionable results

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- Parse arguments to understand agent tasks scope
- If specific agent mentioned: Show tasks for that agent only
- If status mentioned: Filter by task status (e.g., "pending", "in_progress", "completed")
- If no arguments or empty: Display all agent tasks across the project

Output: Complete todo agent tasks results with detailed recommendations.
