# Checkpoint Storage Directory

**DO NOT COMMIT** - This directory contains runtime checkpoint data

## Directory Structure

```
.claude/checkpoints/
├── agent_execution/       # Agent-level checkpoints (session retention)
├── quality_gate/          # Quality validation checkpoints (24h retention)
├── commit_preparation/    # Pre-commit checkpoints (7d retention)
└── manual/                # User-created checkpoints (30d retention)
```

## Retention Policy

Checkpoints are automatically cleaned up based on retention policy:
- **agent_execution**: Deleted at session end
- **quality_gate**: 24 hours
- **commit_preparation**: 7 days
- **manual**: 30 days

## Storage Format

Checkpoints are stored as compressed JSON with diffs for space efficiency.

## Configuration

See `.claude/config/checkpoint-system.json` for full configuration.
