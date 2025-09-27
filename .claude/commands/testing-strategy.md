---
description: Setup comprehensive testing strategy
argument-hint: [--type=test_type] [--coverage]
---

Design and implement comprehensive testing strategy:

1. Analyze project type and technology stack from CLAUDE.md
2. Activate qa-engineer for testing expertise
3. Design testing pyramid (unit, integration, e2e)
4. Set up testing frameworks and tools
5. Create test automation pipeline
6. Generate testing strategy with:
   - Test coverage requirements and goals
   - Testing framework recommendations
   - Test automation pipeline design
   - Performance and security testing plans
   - CI/CD integration strategy
   - Quality gates and acceptance criteria

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- If arguments contain "--type=test_type": Focus on specific test type (e.g., "--type=unit", "--type=integration", "--type=e2e", "--type=performance")
- If arguments contain "--coverage": Include comprehensive code coverage analysis and requirements
- If no arguments or empty: Design complete testing strategy with all test types and coverage requirements

Output: Complete testing strategy with framework setup, automation pipeline, and quality assurance plan.
