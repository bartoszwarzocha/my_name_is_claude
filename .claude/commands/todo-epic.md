# Todo Epic Command

**Command**: `/todo-epic [name]`
**Category**: TodoWrite Integration
**Description**: Stwórz nowy epic w hierarchii TodoWrite

## Usage

```
/todo-epic "User Authentication System"
/todo-epic "Advanced Export Features" --template=feature
/todo-epic "Performance Optimization" --priority=high
```

## Functionality

Creates new epic-level todo in TodoWrite hierarchy with automatic feature and task breakdown suggestions.

### Epic Structure
- **Epic Level**: High-level business capability
- **Feature Level**: Major functional components
- **Task Level**: Implementation units
- **Subtask Level**: Detailed work items

### Agent Integration
Automatically assigns appropriate agents based on epic scope and technology requirements.

### Output Format
```
📋 NEW EPIC CREATED

Epic: "Advanced Export Features"
Priority: High
Estimated Duration: 3-4 weeks
Assigned Agents: 4

📊 EPIC BREAKDOWN:

Epic: Advanced Export Features
├── Feature 1: Multi-Format Export Engine
│   ├── Task 1.1: PDF Export Implementation (backend-engineer)
│   ├── Task 1.2: DOCX Export Integration (backend-engineer)
│   ├── Task 1.3: ODT Export via OpenOffice API (backend-engineer)
│   └── Task 1.4: Export Quality Validation (qa-engineer)
│
├── Feature 2: Export Configuration System
│   ├── Task 2.1: Export Settings UI (desktop-specialist)
│   ├── Task 2.2: Template Management (desktop-specialist)
│   ├── Task 2.3: Custom Format Options (software-architect)
│   └── Task 2.4: Export Presets (ux-designer)
│
├── Feature 3: Batch Export Capabilities
│   ├── Task 3.1: Multi-Document Export (backend-engineer)
│   ├── Task 3.2: Progress Tracking UI (desktop-specialist)
│   ├── Task 3.3: Error Handling System (qa-engineer)
│   └── Task 3.4: Export Queue Management (backend-engineer)
│
└── Feature 4: Export Quality & Validation
    ├── Task 4.1: Format Validation Rules (qa-engineer)
    ├── Task 4.2: Export Testing Suite (qa-engineer)
    ├── Task 4.3: Performance Benchmarks (qa-engineer)
    └── Task 4.4: User Acceptance Tests (qa-engineer)

🤖 AGENT ASSIGNMENTS:

Primary Agents:
• backend-engineer: Export engine implementation (6 tasks)
• desktop-specialist: UI and user experience (3 tasks)
• qa-engineer: Testing and validation (5 tasks)
• software-architect: Architecture and design (1 task)

Supporting Agents:
• ux-designer: User interface design consultation

📈 EPIC METRICS:

Total Tasks: 15
Estimated Effort: 120 hours
Critical Path: 18 days
Dependencies: 4 cross-feature dependencies

🎯 SUCCESS CRITERIA:

✅ Export to PDF, DOCX, ODT formats
✅ Configurable export templates
✅ Batch export for multiple documents
✅ 95% export success rate
✅ Export time < 30 seconds per document
✅ Comprehensive error handling
✅ User-friendly configuration interface

📅 MILESTONES:

Week 1: Basic export engine (Features 1)
Week 2: Configuration system (Feature 2)
Week 3: Batch capabilities (Feature 3)
Week 4: Quality assurance (Feature 4)

✨ EPIC READY FOR DEVELOPMENT!

TodoWrite Status: Epic created with 15 tasks
Agent Coordination: Automatic assignments applied
Next Steps: Begin Feature 1 implementation
```

## Options

### `--template=[type]`
Use predefined epic templates (feature, infrastructure, quality, research)

### `--priority=[level]`
Set epic priority (low, medium, high, critical)

### `--agents="agent1,agent2"`
Override automatic agent assignments

### `--duration=[weeks]`
Specify estimated duration for planning

## Integration

- TodoWrite hierarchy management
- Automatic agent assignment
- Cross-epic dependency tracking
- Milestone planning system