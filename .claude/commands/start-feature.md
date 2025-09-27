---
description: Initialize new feature development with agents
argument-hint: <feature_name> [--type=feature_type]
---

Start new feature development with multi-agent coordination:

1. Parse feature request: $ARGUMENTS
2. Analyze feature requirements and scope
3. Select appropriate agents based on technology stack
4. Create TodoWrite epic and feature breakdown
5. Set up development environment and structure
6. Initialize feature branch and workspace
7. Generate feature development plan with:
   - Feature scope and requirements analysis
   - Technology stack recommendations
   - Agent assignments and responsibilities
   - TodoWrite task hierarchy (epic → features → tasks)
   - Development timeline and milestones
   - Quality gates and acceptance criteria

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- First argument: Required feature name (e.g., "user-authentication", "data-visualization")
- If arguments contain "--type=feature_type": Specify feature type (e.g., "--type=frontend", "--type=backend", "--type=fullstack", "--type=api")
- If no type specified: Auto-detect feature type based on project context and requirements

Output: Complete feature initialization with agent coordination, TodoWrite structure, and development roadmap.