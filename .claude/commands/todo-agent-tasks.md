# Todo Agent Tasks Command

**Command**: `/todo-agent-tasks [agent]`
**Category**: TodoWrite Integration
**Description**: Zadania przypisane do konkretnego agenta

## Usage

```
/todo-agent-tasks backend-engineer
/todo-agent-tasks desktop-specialist --status=active
/todo-agent-tasks qa-engineer --timeline
```

## Functionality

Shows all tasks assigned to specific agent with status, priorities, and timeline information.

### Output Format
```
🤖 AGENT TASK DASHBOARD

Agent: backend-engineer
Specialization: Python Backend Development, Database Integration
Workload: 80% (High)
Active Tasks: 3 | Completed: 8 | Total: 11

┌─ ACTIVE TASKS ──────────────────────────────────────────┐
│                                                         │
│ 🔄 [EPIC 1.2] DOCX Export Integration                   │
│    Priority: High | Due: Today                         │
│    Progress: 75% (Est. 2 hours remaining)              │
│    Dependencies: None                                   │
│    Next Action: Finalize formatting engine             │
│                                                         │
│ 🔄 [EPIC 3.1] Multi-Document Export                     │
│    Priority: Medium | Due: Oct 2                       │
│    Progress: 15% (Planning phase)                      │
│    Dependencies: Task 1.2 completion                   │
│    Next Action: Design batch processing architecture   │
│                                                         │
│ 🔄 [EPIC 3.4] Export Queue Management                   │
│    Priority: Medium | Due: Oct 3                       │
│    Progress: 5% (Initial research)                     │
│    Dependencies: Task 3.1 design                      │
│    Next Action: Research queue implementation patterns │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ COMPLETED TASKS (Last 5) ──────────────────────────────┐
│ ✅ [EPIC 1.1] PDF Export Implementation (Sep 26)       │
│ ✅ [EPIC 1.3] ODT Export via OpenOffice API (Sep 25)   │
│ ✅ [SETUP] Database Schema Updates (Sep 24)            │
│ ✅ [CORE] SQLite Integration Enhancement (Sep 23)      │
│ ✅ [INIT] Project Structure Setup (Sep 22)             │
└─────────────────────────────────────────────────────────┘

📊 AGENT PERFORMANCE:

Current Sprint:
• Tasks completed: 8/11 (73%)
• Average completion time: 1.2 days
• Quality rating: 95% (Excellent)
• Collaboration efficiency: 92%

Weekly Velocity:
• Week 1: 4 tasks completed
• Week 2: 7 tasks completed (ongoing)
• Velocity trend: +75% (Improving)

🎯 UPCOMING WORKLOAD:

Next 3 Days:
• Today: Complete Task 1.2 (High priority)
• Tomorrow: Begin Task 3.1 design phase
• Oct 1: Review and refinement

Next Week:
• Oct 2: Multi-document export implementation
• Oct 3: Queue management system
• Oct 4: Integration testing with qa-engineer

⚡ EFFICIENCY INSIGHTS:

Strengths:
• Excellent at database integration tasks
• High code quality and documentation
• Effective collaboration with desktop-specialist

Optimization Opportunities:
• Consider parallel development on Task 3.4
• Could benefit from pair programming on complex algorithms
• Schedule regular check-ins with software-architect

🤝 COLLABORATION STATUS:

Active Collaborations:
• → desktop-specialist: UI-backend integration
• → qa-engineer: Export validation pipeline
• ← software-architect: Architecture guidance

Handoff Schedule:
• Task 1.2 → qa-engineer (Today, 5PM)
• Task 3.1 design → desktop-specialist (Oct 2)

✨ AGENT STATUS: 🔥 HIGH PERFORMANCE
```

## Options

### `--status=[active|completed|pending]`
Filter tasks by status

### `--timeline`
Show detailed timeline and deadlines

### `--collaboration`
Focus on multi-agent collaboration tasks

## Integration

- TodoWrite agent assignment system
- Performance tracking
- Collaboration monitoring
- Workload optimization