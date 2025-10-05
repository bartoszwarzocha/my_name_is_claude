"""
Parallel Agent Execution System - Core Module

Part of Claude Code Multi-Agent Framework v3.8.0

Core components for parallel agent execution, task queue, and dependency management.
"""

from .parallel_executor import (
    ParallelExecutor,
    AgentTask,
    AgentStatus,
    ExecutionStrategy,
    ParallelExecutionResult
)

from .task_queue import (
    TaskQueue,
    QueuedTask,
    Priority
)

from .dependency_manager import (
    DependencyManager,
    AgentDependency
)

__all__ = [
    # Parallel Executor
    "ParallelExecutor",
    "AgentTask",
    "AgentStatus",
    "ExecutionStrategy",
    "ParallelExecutionResult",

    # Task Queue
    "TaskQueue",
    "QueuedTask",
    "Priority",

    # Dependency Manager
    "DependencyManager",
    "AgentDependency",
]

__version__ = "3.8.0"
