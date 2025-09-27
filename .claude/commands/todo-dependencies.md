---
description: Todo Dependencies
argument-hint: [$ARGUMENTS]
---

Execute todo dependencies functionality:

1. Parse request: $ARGUMENTS
2. Analyze project context from CLAUDE.md
3. Activate appropriate agents for expertise
4. Perform todo dependencies operations
5. Generate comprehensive output with actionable results

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- Parse arguments to understand dependency analysis scope
- If specific task mentioned: Show dependencies for that task
- If critical path requested: Show critical path analysis
- If no arguments or empty: Display comprehensive dependency analysis for all TODO items

Output: Complete todo dependencies results with detailed recommendations.
