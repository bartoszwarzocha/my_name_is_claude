---
description: Display status of all active agents in the project
argument-hint: [--detailed] [--active-only]
---

Analyze and display the status of all agents in the project:

1. Read CLAUDE.md to identify active technologies and project context
2. Check current TodoWrite tasks to see active assignments
3. Display comprehensive agent dashboard with:
   - Status of each agent (active/available/coordinating/standby)
   - Current TodoWrite task assignments
   - Inter-agent collaboration patterns
   - Workload assessment and capacity
   - Recent activity timeline

Arguments: $ARGUMENTS

**Argument Handling Logic:**
- If arguments contain "--detailed": Show comprehensive agent details including competencies, recent activity history, inter-agent collaboration patterns, workload assessment and capacity with timeline
- If arguments contain "--active-only": Display only agents with current TodoWrite assignments, hide agents in standby mode
- If no arguments or empty: Show standard agent status overview with key metrics

Output format: Clean dashboard with icons, sections for different agent types, and actionable insights.