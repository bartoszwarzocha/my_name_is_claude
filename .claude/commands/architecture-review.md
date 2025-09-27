---
description: Comprehensive architecture review with software-architect
argument-hint: [--focus=component] [--depth=level]
---

Conduct thorough architecture analysis and review:

1. Activate software-architect agent for expert analysis
2. Analyze current system architecture from CLAUDE.md and codebase
3. Evaluate architectural patterns and design decisions
4. Assess scalability, maintainability, and performance
5. Review technology choices and integration points
6. Generate comprehensive architecture report with:
   - Architecture diagram and component analysis
   - Design pattern evaluation
   - Scalability and performance assessment
   - Security and compliance review
   - Improvement recommendations
   - Migration and evolution roadmap

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- If arguments contain "--focus=component": Focus review on specific component (e.g., "--focus=frontend", "--focus=database", "--focus=integration")
- If arguments contain "--depth=level": Set analysis depth (e.g., "--depth=shallow", "--depth=detailed", "--depth=comprehensive")
- If no arguments or empty: Perform comprehensive architecture review across all components with detailed analysis

Output: Expert architecture review with visual diagrams and strategic recommendations.