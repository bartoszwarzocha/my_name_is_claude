"""
Advanced Checkpoint System - Core Module

Part of Claude Code Multi-Agent Framework v3.7.0

Core components for checkpoint management, rollback, and coordination.
"""

from .checkpoint_engine import (
    CheckpointEngine,
    CheckpointLevel,
    CheckpointCategory,
    CheckpointMetadata,
    RollbackResult
)

from .multi_agent_coordinator import (
    MultiAgentCoordinator,
    AgentCheckpointState,
    ConflictInfo,
    ConflictResolutionStrategy
)

from .quality_gates_integration import (
    QualityGatesIntegration,
    QualityGateType,
    QualityGateResult
)

__all__ = [
    # Checkpoint Engine
    "CheckpointEngine",
    "CheckpointLevel",
    "CheckpointCategory",
    "CheckpointMetadata",
    "RollbackResult",

    # Multi-Agent Coordinator
    "MultiAgentCoordinator",
    "AgentCheckpointState",
    "ConflictInfo",
    "ConflictResolutionStrategy",

    # Quality Gates Integration
    "QualityGatesIntegration",
    "QualityGateType",
    "QualityGateResult",
]

__version__ = "3.7.0"
