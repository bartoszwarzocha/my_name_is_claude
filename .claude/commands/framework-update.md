---
description: Framework Update
argument-hint: [$ARGUMENTS]
---

Execute framework update functionality:

1. Parse request: $ARGUMENTS
2. Analyze project context from CLAUDE.md
3. Activate appropriate agents for expertise
4. Perform framework update operations
5. Generate comprehensive output with actionable results

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- Parse arguments to understand update scope and version
- If version specified: Update to specific version (e.g., "v3.2.0", "latest", "stable")
- If specific components mentioned: Update only those components (e.g., "agents", "prompts", "tools")
- If no arguments or empty: Perform complete framework update to latest stable version

Output: Complete framework update results with detailed recommendations.
