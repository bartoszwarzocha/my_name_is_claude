---
description: Best practices for development area
argument-hint: [area_or_technology]
---

Provide best practices recommendations for the specified area:

1. Parse requested area or technology: $ARGUMENTS
2. Analyze project context from CLAUDE.md
3. Activate relevant expert agents for specialized guidance
4. Compile industry-standard best practices
5. Customize recommendations for project specifics
6. Generate comprehensive best practices guide with:
   - Technology-specific best practices
   - Code quality and standards guidelines
   - Security and performance recommendations
   - Testing and deployment best practices
   - Team collaboration and workflow guidelines
   - Tool and framework specific advice

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- If arguments provided: Focus on specific area or technology (e.g., "React", "security", "testing", "performance", "Python")
- If no arguments or empty: Provide general best practices across all development areas relevant to the project

Output: Curated best practices guide with actionable recommendations and implementation examples.