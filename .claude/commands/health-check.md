---
description: Comprehensive project health assessment
argument-hint: [--detailed] [--focus=area]
---

Perform comprehensive health check of the current project:

1. Analyze project structure and configuration
2. Check CLAUDE.md for completeness and accuracy
3. Validate framework integration status
4. Assess code quality and standards compliance
5. Review TodoWrite task status and organization
6. Examine dependencies and potential issues
7. Evaluate agent utilization and effectiveness
8. Generate health report with:
   - Overall health score (0-100)
   - Critical issues requiring immediate attention
   - Warnings and recommendations
   - Optimization opportunities
   - Next steps for improvement

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- If arguments contain "--detailed": Include comprehensive diagnostic information, performance metrics, and detailed analysis
- If arguments contain "--focus=area": Focus health check on specific area (e.g., "--focus=agents", "--focus=prompts", "--focus=performance")
- If no arguments or empty: Perform standard project health assessment with key metrics and recommendations

Output: Detailed health report with actionable recommendations and priority levels.