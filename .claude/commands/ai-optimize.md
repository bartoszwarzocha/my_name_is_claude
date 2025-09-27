---
description: AI-powered performance optimization suggestions
argument-hint: [--target=area] [--aggressive]
---

Generate performance optimization recommendations using AI analysis:

1. Analyze current codebase for performance bottlenecks
2. Scan CLAUDE.md for technology-specific optimization patterns
3. Utilize AI-powered analysis tools from .ai-tools/
4. Identify optimization opportunities:
   - Code performance issues
   - Architecture improvements
   - Resource utilization
   - Build and deployment optimizations
5. Generate actionable recommendations with:
   - Priority levels (critical/high/medium/low)
   - Expected performance impact
   - Implementation complexity
   - Risk assessment

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- If arguments contain "--target=area": Focus optimization analysis on specific area (e.g., "--target=frontend", "--target=database", "--target=performance")
- If arguments contain "--aggressive": Include high-risk, high-reward optimizations with detailed risk assessment
- If no arguments or empty: Perform comprehensive optimization analysis across all areas with conservative recommendations

Output: Prioritized optimization roadmap with implementation guides.