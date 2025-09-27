# Agent Handoff Command

**Command**: `/agent-handoff [from] [to]`
**Category**: Agent Management
**Description**: Przekazanie zadania lub kontekstu między agentami

## Usage

```
/agent-handoff desktop-specialist backend-engineer
/agent-handoff "graphics-3d-engineer" "math-specialist"
/agent-handoff current qa-engineer
```

## Functionality

Manages smooth transitions of work between agents, ensuring context preservation and proper coordination.

### Handoff Types
- **Task Transfer**: Complete task ownership transfer
- **Context Sharing**: Shared context for collaboration
- **Sequential Workflow**: Planned handoff in workflow
- **Emergency Transfer**: Immediate transfer for blockers

### Process
1. **Context Capture**: Extract current agent's context and progress
2. **Knowledge Transfer**: Package relevant information for receiving agent
3. **State Transition**: Update TodoWrite task assignments
4. **Coordination Setup**: Establish communication channel between agents
5. **Validation**: Confirm successful handoff completion

### Output Format
```
🔄 AGENT HANDOFF INITIATED

From: desktop-specialist (GUI Implementation)
To: backend-engineer (Data Layer Integration)

Transfer Package:
✅ Current context and decisions
✅ Work progress and deliverables
✅ Technical specifications
✅ Dependency requirements
✅ Quality criteria

TodoWrite Updates:
• Task #1.2 ownership: desktop-specialist → backend-engineer
• New coordination task created for interface integration
• Dependencies updated for downstream tasks

Status: Handoff Complete ✅
```

## Special Cases

### `current` Keyword
Uses currently active agent as source
```
/agent-handoff current qa-engineer
```

### Multi-Agent Handoff
```
/agent-handoff "frontend-engineer backend-engineer" qa-engineer
```

### Emergency Handoff
```
/agent-handoff desktop-specialist backend-engineer --emergency
```

## Integration

- TodoWrite automatic task reassignment
- Context preservation and transfer
- Multi-agent workflow coordination
- Session state management