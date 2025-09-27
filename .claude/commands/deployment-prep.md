---
description: Prepare project for deployment
argument-hint: [--environment=env] [--check-only]
---

Prepare project for production deployment:

1. Activate deployment-engineer for expertise
2. Analyze deployment requirements from CLAUDE.md
3. Validate build and production readiness
4. Check dependencies and security compliance
5. Prepare deployment configuration and scripts
6. Generate deployment checklist with:
   - Production readiness assessment
   - Environment configuration validation
   - Security and compliance verification
   - Performance optimization recommendations
   - Deployment script and automation setup
   - Monitoring and rollback procedures

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- If arguments contain "--environment=env": Prepare for specific environment (e.g., "--environment=production", "--environment=staging", "--environment=development")
- If arguments contain "--check-only": Perform deployment readiness check without making changes
- If no arguments or empty: Prepare for production deployment with comprehensive validation

Output: Complete deployment preparation with checklists, configurations, and automation scripts.
