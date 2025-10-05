"""
Advanced Checkpoint System

Part of Claude Code Multi-Agent Framework v3.7.0

Revolutionary state management with semantic rollback, multi-agent coordination,
and automatic triggering for Fortune 500-ready software development.

Features:
- Multi-level checkpointing (agent/quality/commit/manual)
- Semantic rollback ("rewind to before bug")
- Multi-agent coordination with conflict detection
- Quality gates integration
- Auto-trigger system
- Git state integration
- Session and TodoWrite state capture
"""

from .core import (
    CheckpointEngine,
    CheckpointLevel,
    CheckpointCategory,
    CheckpointMetadata,
    RollbackResult,
    MultiAgentCoordinator,
    AgentCheckpointState,
    ConflictInfo,
    ConflictResolutionStrategy,
    QualityGatesIntegration,
    QualityGateType,
    QualityGateResult
)

from .triggers import (
    AutoTriggerSystem,
    TriggerType
)

__all__ = [
    # Core Engine
    "CheckpointEngine",
    "CheckpointLevel",
    "CheckpointCategory",
    "CheckpointMetadata",
    "RollbackResult",

    # Multi-Agent Coordination
    "MultiAgentCoordinator",
    "AgentCheckpointState",
    "ConflictInfo",
    "ConflictResolutionStrategy",

    # Quality Gates
    "QualityGatesIntegration",
    "QualityGateType",
    "QualityGateResult",

    # Auto-Triggers
    "AutoTriggerSystem",
    "TriggerType",
]

__version__ = "3.7.0"
