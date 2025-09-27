---
description: Quick Docs
argument-hint: [$ARGUMENTS]
---

Execute quick docs functionality:

1. Parse request: $ARGUMENTS
2. Analyze project context from CLAUDE.md
3. Activate appropriate agents for expertise
4. Perform quick docs operations
5. Generate comprehensive output with actionable results

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- Parse arguments to understand documentation request
- If specific topic mentioned: Generate documentation for that topic (e.g., "API", "setup", "agents")
- If format specified: Generate in specified format (e.g., "markdown", "html", "pdf")
- If no arguments or empty: Generate comprehensive project documentation overview

Output: Complete quick docs results with detailed recommendations.
