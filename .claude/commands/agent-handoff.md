---
description: Execute smooth handoff between agents
argument-hint: <from_agent> <to_agent> [context]
---

Perform a structured handoff between agents:

1. Parse handoff request: $ARGUMENTS

**Argument Handling Logic:**
- First argument: Source agent to transfer work from (required)
- Second argument: Target agent to transfer work to (required)
- Third argument: Additional context for handoff (optional)
- Validate both agents exist and are available for handoff
2. Process the validated handoff request
3. Gather current context from source agent:
   - Active TodoWrite tasks
   - Work in progress
   - Important decisions made
   - Known issues or blockers
4. Prepare handoff documentation
5. Transfer responsibilities:
   - Reassign TodoWrite tasks
   - Update agent status
   - Provide context summary
   - Set up collaboration if needed

Output: Handoff summary with transferred responsibilities and next steps for the receiving agent.