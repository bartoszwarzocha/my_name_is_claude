---
description: Check dependencies and compatibility issues
argument-hint: [--update] [--security]
---

Analyze project dependencies and compatibility:

1. Scan all dependency files (package.json, requirements.txt, etc.)
2. Check for outdated packages and security vulnerabilities
3. Analyze compatibility between dependencies
4. Validate against technology stack in CLAUDE.md
5. Check for licensing conflicts and compliance issues
6. Generate dependency report with:
   - Outdated dependencies with upgrade paths
   - Security vulnerabilities and fixes
   - Compatibility issues and resolutions
   - License compliance status
   - Optimization recommendations

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- If arguments contain "--update": Automatically update compatible dependencies and provide upgrade recommendations
- If arguments contain "--security": Focus specifically on security vulnerabilities and critical security updates
- If no arguments or empty: Perform comprehensive dependency analysis including outdated packages, security, and compatibility

Output: Comprehensive dependency analysis with security and compatibility recommendations.