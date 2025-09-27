---
description: Quick setup of AI tools without interactive menu
argument-hint: [--profile=type] [--skip-validation]
---

Rapidly configure AI tools for the current project:

1. Detect project type and technology stack from CLAUDE.md
2. Initialize AI-tools framework (.ai-tools/ directory)
3. Configure appropriate AI models and agents
4. Set up project-specific AI tool profiles
5. Validate AI tools integration
6. Generate configuration summary:
   - Enabled AI capabilities
   - Configured models and agents
   - Integration status
   - Next steps for optimization

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- If arguments contain "--profile=type": Set up specific AI profile (e.g., "--profile=development", "--profile=analytics", "--profile=enterprise")
- If arguments contain "--skip-validation": Skip validation steps and proceed with basic setup
- If no arguments or empty: Auto-detect project type and set up appropriate AI tools with full validation

Output: AI tools setup summary with configuration details and validation results.