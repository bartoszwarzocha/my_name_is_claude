"""
Parallel Agent Execution System

Part of Claude Code Multi-Agent Framework v3.8.0

Revolutionary parallel execution system enabling 3x development speed through
concurrent multi-agent workflows with dependency management and automatic checkpointing.

Features:
- Concurrent agent execution (3-5 agents simultaneously)
- Dependency-based task ordering
- Multiple execution strategies (concurrent, pipeline, hybrid)
- Automatic checkpoint integration
- Resource-aware scheduling
- Real-time progress monitoring
- Failure handling and rollback
"""

from .core import (
    ParallelExecutor,
    AgentTask,
    AgentStatus,
    ExecutionStrategy,
    ParallelExecutionResult,
    TaskQueue,
    QueuedTask,
    Priority,
    DependencyManager,
    AgentDependency
)

__all__ = [
    # Core Executor
    "ParallelExecutor",
    "AgentTask",
    "AgentStatus",
    "ExecutionStrategy",
    "ParallelExecutionResult",

    # Task Queue
    "TaskQueue",
    "QueuedTask",
    "Priority",

    # Dependency Management
    "DependencyManager",
    "AgentDependency",
]

__version__ = "3.8.0"
