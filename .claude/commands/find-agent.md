---
description: Find Agent
argument-hint: [$ARGUMENTS]
---

Execute find agent functionality:

1. Parse request: $ARGUMENTS
2. Analyze project context from CLAUDE.md
3. Activate appropriate agents for expertise
4. Perform find agent operations
5. Generate comprehensive output with actionable results

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- Parse arguments to understand agent search criteria
- If technology mentioned: Find agents with expertise in that technology
- If role/function mentioned: Find agents matching that role
- If specific skills mentioned: Search agent competencies for matching skills
- If no arguments or empty: Provide overview of all available agents

Output: Complete find agent results with detailed recommendations.
