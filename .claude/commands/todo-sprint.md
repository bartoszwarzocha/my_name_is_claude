# Todo Sprint Command

**Command**: `/todo-sprint`
**Category**: TodoWrite Integration
**Description**: Pokaż aktualny sprint i progress

## Usage

```
/todo-sprint
/todo-sprint --planning
/todo-sprint --review
/todo-sprint --next
```

## Functionality

Displays current sprint status, task progress, and agent workload distribution with sprint planning capabilities.

### Sprint Management
- **Current Sprint**: Active tasks and progress
- **Sprint Planning**: Next sprint preparation
- **Sprint Review**: Completed sprint analysis
- **Velocity Tracking**: Team performance metrics

### Output Format
```
🏃‍♂️ CURRENT SPRINT STATUS

Sprint: Week 2 - Export Engine Implementation
Duration: Sep 25 - Oct 1, 2025 (5 days remaining)
Sprint Goal: Complete basic export functionality

📊 SPRINT PROGRESS:

Overall Progress: 68% (11/16 tasks completed)
On Track: 🟢 YES (Slight buffer available)

┌─ ACTIVE TASKS ──────────────────────────────────────────┐
│ 🔄 IN PROGRESS (3 tasks)                                │
│                                                         │
│ [Task 1.2] DOCX Export Integration                     │
│ └─ Agent: backend-engineer                             │
│ └─ Progress: 75% (Est. completion: Today)              │
│ └─ Blockers: None                                      │
│                                                         │
│ [Task 2.1] Export Settings UI                          │
│ └─ Agent: desktop-specialist                           │
│ └─ Progress: 40% (Est. completion: Tomorrow)           │
│ └─ Blockers: Waiting for UX mockups                    │
│                                                         │
│ [Task 1.4] Export Quality Validation                   │
│ └─ Agent: qa-engineer                                  │
│ └─ Progress: 25% (Est. completion: Oct 1)              │
│ └─ Blockers: Dependency on Task 1.2                    │
└─────────────────────────────────────────────────────────┘

┌─ COMPLETED TASKS (11 tasks) ────────────────────────────┐
│ ✅ [Epic] Advanced Export Features planning            │
│ ✅ [Task 1.1] PDF Export Implementation               │
│ ✅ [Task 1.3] ODT Export via OpenOffice API           │
│ ✅ [Task 2.2] Template Management                     │
│ ... and 7 more completed tasks                         │
└─────────────────────────────────────────────────────────┘

┌─ UPCOMING TASKS (2 tasks) ──────────────────────────────┐
│ ⏳ [Task 2.3] Custom Format Options                    │
│ └─ Planned start: Oct 2 (Next sprint)                  │
│                                                         │
│ ⏳ [Task 3.1] Multi-Document Export                    │
│ └─ Planned start: Oct 2 (Next sprint)                  │
└─────────────────────────────────────────────────────────┘

🤖 AGENT WORKLOAD:

┌─ CURRENT ASSIGNMENTS ───────────────────────────────────┐
│ backend-engineer    ████████░░  80%  (2 active tasks)  │
│ desktop-specialist  ██████░░░░  60%  (1 active task)   │
│ qa-engineer         ████░░░░░░  40%  (1 active task)   │
│ software-architect  ░░░░░░░░░░   0%  (Available)       │
└─────────────────────────────────────────────────────────┘

📈 SPRINT METRICS:

Velocity:
• Tasks completed: 11 (Target: 12)
• Story points: 45 (Target: 48)
• Completion rate: 92%

Quality:
• Bug count: 0
• Code review pass rate: 100%
• Test coverage: 94%

Collaboration:
• Agent handoffs: 3 successful
• Blocked tasks: 1 (minor)
• Team efficiency: 88%

⚠️ SPRINT RISKS:

Medium Risk:
• Task 2.1 blocked by UX mockups
• Solution: Use placeholder UI for now

Low Risk:
• Task 1.4 dependent on Task 1.2
• Solution: On track, no action needed

🎯 SPRINT FORECAST:

Likely Outcomes (85% confidence):
✅ Complete Tasks 1.2, 2.1, 1.4
✅ Sprint goal achieved
✅ Ready for next sprint planning

Sprint End Prediction: Oct 1 (On schedule)
Next Sprint Capacity: 14 tasks (full team)

✨ SPRINT STATUS: 🟢 ON TRACK
```

## Options

### `--planning`
Enter sprint planning mode for next sprint

### `--review`
Analyze completed sprint performance

### `--velocity`
Show detailed velocity and performance metrics

## Integration

- TodoWrite task tracking
- Agent workload management
- Sprint planning algorithms
- Performance analytics