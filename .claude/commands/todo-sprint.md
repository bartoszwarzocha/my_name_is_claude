---
description: Todo Sprint
argument-hint: [$ARGUMENTS]
---

Execute todo sprint functionality:

1. Parse request: $ARGUMENTS
2. Analyze project context from CLAUDE.md
3. Activate appropriate agents for expertise
4. Perform todo sprint operations
5. Generate comprehensive output with actionable results

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- Parse arguments to understand sprint management request
- If sprint name/number mentioned: Focus on specific sprint
- If action specified: Perform specific action (e.g., "start", "plan", "review", "close")
- If no arguments or empty: Display current sprint status and planning overview

Output: Complete todo sprint results with detailed recommendations.
