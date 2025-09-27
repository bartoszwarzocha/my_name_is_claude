---
description: Multi-agent comprehensive code review
argument-hint: [--scope=files] [--focus=area]
---

Conduct thorough multi-agent code review:

1. Activate appropriate review agents (qa-engineer, security-engineer, software-architect)
2. Analyze code quality, security, and architectural compliance
3. Check against project standards from CLAUDE.md
4. Review for best practices and coding standards
5. Identify potential bugs, security issues, and performance problems
6. Generate comprehensive review report with:
   - Code quality assessment and metrics
   - Security vulnerability analysis
   - Architecture compliance review
   - Performance optimization suggestions
   - Best practices compliance checklist
   - Actionable improvement recommendations

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- If arguments contain "--scope=files": Focus review on specific files or directories (e.g., "--scope=src/", "--scope=*.ts")
- If arguments contain "--focus=area": Focus on specific area (e.g., "--focus=security", "--focus=performance", "--focus=maintainability")
- If no arguments or empty: Perform comprehensive multi-agent code review across entire codebase

Output: Multi-perspective code review with prioritized recommendations and implementation guidance.