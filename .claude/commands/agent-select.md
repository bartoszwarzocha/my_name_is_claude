---
description: Automatically select the best agent based on technology stack
argument-hint: <technology_stack>
---

Select the most appropriate agent for the given technologies:

1. Analyze specified technologies: $ARGUMENTS
2. Scan available agents in .claude/agents/ directory
3. Score agent compatibility based on their competencies
4. Check availability (current TodoWrite assignments)
5. Recommend top candidates with:
   - Match score (0-100%)
   - Justification for selection
   - Suggested role in the project
   - Collaboration recommendations with other agents

Output: Ranked list of agents with explanations and next steps for team coordination.