# Todo Dependencies Command

**Command**: `/todo-dependencies`
**Category**: TodoWrite Integration
**Description**: Analiza dependencies między zadaniami

## Usage

```
/todo-dependencies
/todo-dependencies --critical-path
/todo-dependencies --blocking
/todo-dependencies --graph
```

## Functionality

Analyzes task dependencies, identifies critical paths, and shows potential bottlenecks in project workflow.

### Output Format
```
🔗 TASK DEPENDENCY ANALYSIS

Project: book_writing_app
Total Tasks: 16
Dependencies: 12
Critical Path Length: 8 tasks

┌─ DEPENDENCY GRAPH ──────────────────────────────────────┐
│                                                         │
│     [Epic] Advanced Export Features                    │
│              │                                          │
│    ┌─────────┼─────────┐                              │
│    │         │         │                              │
│ [1.1 PDF] [1.2 DOCX] [1.3 ODT]                       │
│    │         │         │                              │
│    └─────────┼─────────┘                              │
│              │                                          │
│         [1.4 Validation] ← Critical Path               │
│              │                                          │
│    ┌─────────┼─────────┐                              │
│    │         │         │                              │
│ [2.1 UI]  [2.2 Mgmt] [2.3 Config]                   │
│    │         │         │                              │
│    └─────────┼─────────┘                              │
│              │                                          │
│         [3.1 Batch] ← Potential Bottleneck             │
│              │                                          │
│         [3.2 Progress]                                  │
│              │                                          │
│         [4.1 Testing] ← Final Gate                     │
│                                                         │
└─────────────────────────────────────────────────────────┘

🚨 CRITICAL PATH (8 tasks, 12 days):

Task 1.2 → Task 1.4 → Task 2.1 → Task 3.1 → Task 3.2 → Task 4.1
│         │         │         │         │         │
Today     Tomorrow  Oct 1     Oct 2     Oct 3     Oct 4

⚠️ DEPENDENCY RISKS:

High Risk:
• Task 1.4 blocked by Task 1.2 (backend-engineer overloaded)
• Task 3.1 has 3 dependencies (potential bottleneck)

Medium Risk:
• Task 2.1 waiting for UX mockups (external dependency)
• Task 4.1 requires all previous tasks (final integration risk)

🔍 BLOCKING ANALYSIS:

Currently Blocking:
┌─ Task 1.2 (DOCX Export) ────────────────────────────────┐
│ Blocks: Task 1.4, Task 3.1, Task 4.1                   │
│ Impact: 3 downstream tasks                              │
│ Agent: backend-engineer (75% complete)                  │
│ Resolution: Est. completion today                       │
└─────────────────────────────────────────────────────────┘

┌─ UX Mockups (External) ─────────────────────────────────┐
│ Blocks: Task 2.1 (Export Settings UI)                   │
│ Impact: 1 downstream task                               │
│ Agent: External (ux-designer)                           │
│ Resolution: Escalation needed                           │
└─────────────────────────────────────────────────────────┘

💡 OPTIMIZATION RECOMMENDATIONS:

Immediate Actions:
1. 🔥 Focus backend-engineer on Task 1.2 completion
2. 🔄 Start Task 2.2 (Template Management) in parallel
3. 📋 Create placeholder UI for Task 2.1 to unblock progress

Strategic Improvements:
• Consider parallel execution of Tasks 2.2 and 2.3
• Pre-plan Task 3.1 architecture while waiting for dependencies
• Schedule qa-engineer availability for Task 4.1

🎯 DEPENDENCY RESOLUTION:

Short Term (Today):
✅ Complete Task 1.2 (backend-engineer priority)
🔄 Begin Task 2.2 parallel development
📞 Escalate UX mockups requirement

Medium Term (This Week):
🔄 Implement placeholder UI solution
🔄 Begin Task 3.1 architecture planning
📋 Prepare Task 4.1 testing strategy

📊 IMPACT ANALYSIS:

If Task 1.2 delayed by 1 day:
• Project delay: 1 day
• Affected tasks: 3
• Critical path extension: 1 day

If UX mockups unavailable:
• Alternative: Use placeholder UI
• Quality impact: Minor (10% UX score)
• Schedule impact: None (parallel development)

✨ OPTIMIZATION POTENTIAL: 2 days saved with parallel execution
```

## Options

### `--critical-path`
Show only critical path analysis

### `--blocking`
Focus on currently blocking tasks

### `--graph`
Visual dependency graph representation

## Integration

- TodoWrite dependency tracking
- Critical path calculation
- Risk assessment algorithms
- Optimization suggestions