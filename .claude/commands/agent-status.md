# Agent Status Command

**Command**: `/agent-status`
**Category**: Agent Management
**Description**: Wyświetla status wszystkich aktywnych agentów w projekcie

## Usage

```
/agent-status
/agent-status --detailed
/agent-status --active-only
```

## Functionality

Provides comprehensive overview of all agents currently involved in the project, their roles, current tasks, and coordination status.

### Status Categories
- **Active**: Currently working on tasks
- **Available**: Ready for assignment
- **Coordinating**: Involved in multi-agent workflows
- **Standby**: Passive monitoring mode

### Information Displayed
- Agent name and specialization
- Current TodoWrite task assignments
- Collaboration status with other agents
- Recent activity timeline
- Workload assessment

### Output Format
```
🤖 AGENT STATUS DASHBOARD

Project: [project_name]
Framework: Claude Code Multi-Agent v3.1.0
Active Agents: [count] | Available: [count] | Total: [count]

┌─ ACTIVE AGENTS ─────────────────────────────────────────┐
│ 🖥️  desktop-specialist                                  │
│     Status: Working on GUI implementation               │
│     Current Task: Main window design (TodoWrite #1.2)   │
│     Collaboration: → backend-engineer (data layer)      │
│     Workload: High (3 active tasks)                     │
│                                                         │
│ ⚙️  backend-engineer                                     │
│     Status: Implementing SQLite integration             │
│     Current Task: Database schema (TodoWrite #2.1)      │
│     Collaboration: ← desktop-specialist, → qa-engineer  │
│     Workload: Medium (2 active tasks)                   │
└─────────────────────────────────────────────────────────┘

┌─ COORDINATING AGENTS ───────────────────────────────────┐
│ 🏗️  software-architect                                  │
│     Status: Architecture review and guidance            │
│     Role: Strategic oversight and design decisions      │
│     Active Workflows: 2 multi-agent features           │
└─────────────────────────────────────────────────────────┘

┌─ AVAILABLE AGENTS ──────────────────────────────────────┐
│ 🔍 qa-engineer - Ready for testing assignments         │
│ 🎨 ux-designer - Available for UI/UX consultation      │
│ 🚀 deployment-engineer - Standby for deployment        │
└─────────────────────────────────────────────────────────┘
```

## Integration

- Real-time TodoWrite integration
- Session state tracking
- Multi-agent workflow monitoring
- Performance metrics collection

## Options

### `--detailed`
Shows extended information including:
- Detailed task descriptions
- Agent competency utilization
- Historical performance metrics
- Collaboration efficiency ratings

### `--active-only`
Filters to show only agents currently working on tasks

### `--json`
Outputs status in JSON format for programmatic access

## Examples

### Standard Status Check
```
/agent-status

Quick overview of all agents and their current state
```

### Detailed Analysis
```
/agent-status --detailed

Comprehensive dashboard with performance metrics and collaboration analysis
```