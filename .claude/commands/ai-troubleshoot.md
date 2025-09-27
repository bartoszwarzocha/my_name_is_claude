---
description: Debug and resolve AI tools issues
argument-hint: [--component=name] [--verbose]
---

Diagnose and fix AI tools problems:

1. Run comprehensive AI tools diagnostics
2. Check system dependencies and requirements
3. Validate configuration files and settings
4. Test AI model connectivity and performance
5. Analyze error logs and system status
6. Generate troubleshooting report with:
   - Issue identification and classification
   - Root cause analysis
   - Step-by-step resolution instructions
   - Prevention recommendations
   - System health verification

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- If arguments contain "--component=name": Focus troubleshooting on specific component (e.g., "--component=agents", "--component=prompts", "--component=integration")
- If arguments contain "--verbose": Include detailed debugging information, logs analysis, and comprehensive diagnostic data
- If no arguments or empty: Perform general AI tools health check and identify common issues

Output: Diagnostic report with automated fixes and manual resolution steps.