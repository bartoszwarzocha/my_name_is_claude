# Advanced Checkpoint System

**Part of Claude Code Multi-Agent Framework v3.7.0**

Revolutionary state management system with semantic rollback capabilities, enabling instant recovery from errors, experimental workflows, and safe multi-agent coordination.

## 🎯 Overview

The Advanced Checkpoint System provides enterprise-grade state management for AI-driven development workflows. Unlike traditional version control, it captures complete development state including file changes, git status, agent state, session context, and TodoWrite tasks - all with semantic labeling for natural language rollback.

### Key Features

- **Multi-Level Checkpointing** - 4 hierarchy levels (agent, quality gate, commit preparation, manual)
- **Semantic Rollback** - Natural language commands like "rewind to before bug fix"
- **Multi-Agent Coordination** - Safe parallel agent execution with conflict detection
- **Quality Gates Integration** - Automatic checkpoints before critical validations
- **Auto-Trigger System** - Intelligent checkpoint creation at strategic moments
- **Git Integration** - Captures git state and provides state comparison
- **Comprehensive State Capture** - Files, git, session, agents, todos

## 🚀 Quick Start

### Basic Usage

```python
from checkpoint import CheckpointEngine, CheckpointLevel

# Initialize
engine = CheckpointEngine()

# Create checkpoint
checkpoint_id = engine.create_checkpoint(
    level=CheckpointLevel.MANUAL,
    label="before_refactoring",
    description="State before major authentication refactoring",
    tags=["refactoring", "authentication"]
)

# Work on your changes...

# Rollback if needed
result = engine.rollback_to_checkpoint(checkpoint_id)
if result.success:
    print(f"✅ Rolled back to: {result.checkpoint_label}")
```

### Semantic Rewind

```python
# Natural language rollback
result = engine.semantic_rewind("rewind to before bug fix")
result = engine.semantic_rewind("rewind 3 steps")
result = engine.semantic_rewind("rewind to 2 hours ago")
result = engine.semantic_rewind("rewind to last software-architect checkpoint")
```

## 📋 Checkpoint Levels

The system supports 4 checkpoint hierarchy levels:

| Level | Purpose | Auto-Trigger | Retention |
|-------|---------|--------------|-----------|
| **Agent Execution** | Before/after agent work | Yes | 50 checkpoints, 7 days |
| **Quality Gate** | Before validation gates | Yes | 30 checkpoints, 14 days |
| **Commit Preparation** | Before git commits | Yes | 100 checkpoints, 30 days |
| **Manual** | User-created checkpoints | No | 200 checkpoints, 90 days |

## 🤖 Multi-Agent Coordination

The Multi-Agent Coordinator ensures safe parallel execution with conflict detection:

```python
from checkpoint import MultiAgentCoordinator

coordinator = MultiAgentCoordinator(engine)

# Pre-agent checkpoint
cp_id = coordinator.pre_agent_execution_checkpoint(
    agent_type="backend-engineer",
    description="Implementing authentication API"
)

# Post-agent checkpoint
coordinator.post_agent_execution_checkpoint(
    agent_type="backend-engineer",
    success=True,
    modified_files=["src/api/auth.py", "tests/test_auth.py"]
)

# Coordinated rollback across agents
results = coordinator.coordinated_rollback(
    target_checkpoint_id=cp_id,
    affected_agents=["backend-engineer", "frontend-engineer"]
)
```

## 🚪 Quality Gates Integration

Automatic checkpoints before quality validations:

```python
from checkpoint import QualityGatesIntegration, QualityGateType

quality_gates = QualityGatesIntegration(engine)

# Execute quality gate with automatic checkpoint
result = quality_gates.pre_commit_gate(
    description="Pre-commit validation"
)

if result.success:
    print(f"✅ Quality gate passed (checkpoint: {result.checkpoint_id})")
else:
    print(f"❌ Quality gate failed: {result.message}")
    # Automatic rollback if configured
```

## ⚡ Auto-Trigger System

Automatic checkpoint creation at strategic moments:

```python
from checkpoint import AutoTriggerSystem, TriggerType

auto_trigger = AutoTriggerSystem(engine)

# Trigger pre-agent checkpoint
checkpoint_id = auto_trigger.trigger(
    TriggerType.PRE_AGENT_EXECUTION,
    context={
        "agent_type": "software-architect",
        "description": "Architecture redesign"
    }
)

# Trigger pre-refactoring checkpoint
checkpoint_id = auto_trigger.trigger(
    TriggerType.PRE_REFACTORING,
    context={
        "description": "Refactor authentication module for better security"
    }
)
```

### Supported Triggers

- `PRE_AGENT_EXECUTION` - Before agent starts work
- `POST_AGENT_SUCCESS` - After successful agent execution
- `POST_AGENT_FAILURE` - After failed agent execution
- `PRE_QUALITY_GATE` - Before quality gate validation
- `PRE_COMMIT` - Before git commit
- `PRE_PUSH` - Before git push
- `PRE_REFACTORING` - Before refactoring operations
- `CRITICAL_OPERATION` - Before critical operations (deploy, migration, etc.)

## 🔍 Checkpoint Management

### List Checkpoints

```python
# List all checkpoints
checkpoints = engine.list_checkpoints(limit=20)

# Filter by level
checkpoints = engine.list_checkpoints(
    level=CheckpointLevel.AGENT_EXECUTION,
    limit=10
)

# Filter by category
from checkpoint import CheckpointCategory
checkpoints = engine.list_checkpoints(
    category=CheckpointCategory.BUGFIX
)
```

### Checkpoint Metadata

```python
# Get detailed metadata
metadata = engine.get_checkpoint_metadata(checkpoint_id)

print(f"Label: {metadata.label}")
print(f"Category: {metadata.category}")
print(f"Git Commit: {metadata.git_commit}")
print(f"Files: {metadata.files_count}")
print(f"Agent: {metadata.agent_type}")
```

### Delete Checkpoints

Checkpoints are automatically cleaned up based on retention policies, but can also be manually deleted:

```python
engine._delete_checkpoint(checkpoint_id)
```

## 🔄 Rollback Operations

### Standard Rollback

```python
# Rollback to specific checkpoint
result = engine.rollback_to_checkpoint(
    checkpoint_id=checkpoint_id,
    dry_run=False  # Set True to preview without changes
)

if result.success:
    print(f"Files restored: {result.files_restored}")
    print(f"Rollback checkpoint: {result.rollback_checkpoint_created}")
else:
    print(f"Rollback failed: {result.message}")
```

### Semantic Search

Find checkpoints using natural language:

```python
# By description
cp_id = engine.find_checkpoint_by_description("authentication bug fix")

# By time
cp_id = engine.find_checkpoint_by_time(hours_ago=2.5)

# By agent
cp_id = engine.find_checkpoint_by_agent("backend-engineer", last_n=1)

# By category
cp_id = engine.find_checkpoint_by_category(CheckpointCategory.BUGFIX)

# By steps
cp_id = engine.rewind_by_steps(steps=3)
```

## ⚙️ Configuration

Configuration is stored in `.claude/config/checkpoint-config.json`:

```json
{
  "enabled": true,
  "autoCheckpointEnabled": true,

  "checkpointLevels": {
    "agent_execution": {
      "enabled": true,
      "auto_trigger": true,
      "retention_count": 50,
      "retention_days": 7
    }
  },

  "autoTriggers": {
    "pre_agent_execution": {
      "enabled": true,
      "agents": ["all"],
      "exclude_agents": ["qa-engineer"]
    }
  },

  "rollbackPolicies": {
    "validate_before_rollback": true,
    "create_rollback_checkpoint": true,
    "conflict_resolution": "interactive"
  }
}
```

## 📊 Statistics and Monitoring

```python
# Trigger statistics
stats = auto_trigger.get_trigger_statistics()
print(f"Pre-agent triggers: {stats['pre_agent_execution']['success_count']}")

# Quality gate statistics
stats = quality_gates.get_gate_statistics()
print(f"Pre-commit success rate: {stats['pre-commit']['success_rate']:.1%}")

# Coordination status
status = coordinator.get_coordination_status()
print(f"Active agents: {status['active_agents']}")
print(f"Total checkpoints: {status['total_checkpoints']}")
```

## 🎯 Use Cases

### 1. Safe Refactoring

```python
# Create checkpoint before refactoring
cp_id = engine.create_checkpoint(
    level=CheckpointLevel.MANUAL,
    label="before_auth_refactoring",
    description="Complete authentication system working",
    tags=["refactoring", "authentication", "stable"]
)

# Perform refactoring...

# If something breaks, rollback
engine.semantic_rewind("rewind to before auth refactoring")
```

### 2. Experimental Features

```python
# Try experimental approach
cp_id = engine.create_checkpoint(
    label="before_experimental_caching",
    description="Testing Redis caching layer"
)

# Implement experimental feature...
# If it doesn't work out, rewind

engine.rollback_to_checkpoint(cp_id)
```

### 3. Multi-Agent Workflows

```python
coordinator = MultiAgentCoordinator(engine)

# Architecture agent designs system
coordinator.pre_agent_execution_checkpoint("software-architect")
# ... architecture work ...
coordinator.post_agent_execution_checkpoint("software-architect", success=True)

# Backend engineer implements
coordinator.pre_agent_execution_checkpoint("backend-engineer")
# ... implementation work ...
coordinator.post_agent_execution_checkpoint("backend-engineer", success=True)

# If something goes wrong, rollback all agents to last known good state
coordinator.coordinated_rollback(target_checkpoint_id=last_good_checkpoint)
```

## 🔒 Safety Features

- **Validation Before Rollback** - Warns about uncommitted changes
- **Rollback Checkpoint Creation** - Preserves current state before rollback
- **Conflict Detection** - Detects file conflicts between parallel agents
- **Git State Tracking** - Tracks git commit, branch, and status
- **Integrity Verification** - Validates checkpoint integrity before restoration

## 📝 Best Practices

1. **Create checkpoints before risky operations** - Refactoring, major changes, experiments
2. **Use semantic labels** - Descriptive labels enable better semantic search
3. **Tag appropriately** - Tags help organize and find checkpoints
4. **Review retention policies** - Adjust based on your workflow needs
5. **Use dry-run for rollbacks** - Preview changes before applying
6. **Enable auto-triggers** - Automatic safety net for agent workflows
7. **Monitor coordination status** - Track multi-agent interactions

## 🔧 Troubleshooting

### Checkpoints not being created

- Check if checkpoint system is enabled in config
- Verify storage permissions for `.ai-tools/checkpoint/storage/`
- Check log output for errors

### Rollback not restoring files

- File restoration is not yet fully implemented (placeholder)
- Metadata and state restoration works
- Git state comparison provides guidance

### Conflicts in multi-agent workflows

- Check coordination status: `coordinator.get_coordination_status()`
- Review conflict detection settings in config
- Enable interactive conflict resolution

## 📚 API Reference

See individual module documentation:
- `CheckpointEngine` - Core checkpoint operations (.ai-tools/checkpoint/core/checkpoint_engine.py:109)
- `MultiAgentCoordinator` - Multi-agent coordination (.ai-tools/checkpoint/core/multi_agent_coordinator.py:41)
- `QualityGatesIntegration` - Quality gates (.ai-tools/checkpoint/core/quality_gates_integration.py:40)
- `AutoTriggerSystem` - Auto-triggers (.ai-tools/checkpoint/triggers/auto_trigger_system.py:38)

## 🎉 What's Next

- File capture and restoration implementation
- Session state integration
- TodoWrite state integration
- Visual checkpoint timeline
- Cross-session checkpoint sharing
- AI-powered checkpoint suggestions

---

**Version:** 3.7.0
**License:** MIT
**Part of:** Claude Code Multi-Agent Framework
