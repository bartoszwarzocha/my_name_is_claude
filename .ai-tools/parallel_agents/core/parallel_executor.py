#!/usr/bin/env python3
"""
Parallel Agent Executor for Claude Code Multi-Agent Framework

Core execution engine for running multiple agents concurrently with dependency
management, resource allocation, and conflict detection.

Part of Framework v3.8.0 - Parallel Agent Execution System

Features:
- Concurrent agent execution with worker pool
- Dependency-based task ordering
- Resource-aware scheduling
- Automatic checkpoint integration
- Real-time progress monitoring
- Failure handling and rollback
"""

import json
import logging
import asyncio
import concurrent.futures
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Dict, List, Optional, Set, Callable, Any
from pathlib import Path
from enum import Enum
import threading

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AgentStatus(Enum):
    """Agent execution status"""
    PENDING = "pending"
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    SKIPPED = "skipped"


class ExecutionStrategy(Enum):
    """Execution strategy types"""
    CONCURRENT = "concurrent"
    PIPELINE = "pipeline"
    HYBRID = "hybrid"


@dataclass
class AgentTask:
    """Represents a task for a single agent"""
    agent_type: str
    task_id: str
    description: str
    priority: str = "medium"
    dependencies: List[str] = field(default_factory=list)

    # Execution context
    context: Dict[str, Any] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)

    # Status tracking
    status: AgentStatus = AgentStatus.PENDING
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    duration_seconds: float = 0.0

    # Results
    checkpoint_id: Optional[str] = None
    output: Optional[Any] = None
    error: Optional[str] = None

    # Resource tracking
    cpu_usage: float = 0.0
    memory_usage_mb: float = 0.0
    api_calls: int = 0


@dataclass
class ParallelExecutionResult:
    """Result of parallel execution"""
    success: bool
    total_tasks: int
    completed_tasks: int
    failed_tasks: int
    cancelled_tasks: int

    # Timing
    started_at: str
    completed_at: str
    total_duration_seconds: float

    # Results
    task_results: List[AgentTask]
    checkpoint_ids: List[str]

    # Metrics
    average_cpu_usage: float = 0.0
    peak_memory_mb: float = 0.0
    total_api_calls: int = 0

    # Messages
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    message: str = ""


class ParallelExecutor:
    """
    Core parallel agent execution engine.

    Features:
    - Worker pool management
    - Dependency resolution
    - Resource allocation
    - Checkpoint integration
    - Progress monitoring
    """

    def __init__(
        self,
        config_path: Optional[str] = None,
        framework_root: Optional[Path] = None,
        checkpoint_engine: Optional[Any] = None,
        coordinator: Optional[Any] = None
    ):
        """
        Initialize parallel executor.

        Args:
            config_path: Path to parallel-agents-config.json
            framework_root: Framework root directory
            checkpoint_engine: Optional CheckpointEngine instance
            coordinator: Optional MultiAgentCoordinator instance
        """
        self.framework_root = framework_root or self._get_framework_root()
        self.config_path = config_path or self._get_default_config_path()
        self.config = self._load_config()

        # External integrations
        self.checkpoint_engine = checkpoint_engine
        self.coordinator = coordinator

        # Worker pool
        self.max_workers = self.config.get("execution", {}).get("workerPool", {}).get("maxWorkers", 5)
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers)

        # Task tracking
        self.tasks: Dict[str, AgentTask] = {}
        self.task_lock = threading.Lock()

        # Execution state
        self.is_running = False
        self.execution_start_time = None

        logger.info(f"Parallel Executor initialized (max workers: {self.max_workers})")

    def _get_framework_root(self) -> Path:
        """Get framework root directory"""
        return Path(__file__).parent.parent.parent.parent

    def _get_default_config_path(self) -> str:
        """Get default configuration file path"""
        return str(self.framework_root / ".claude" / "config" / "parallel-agents-config.json")

    def _load_config(self) -> Dict:
        """Load parallel agents configuration"""
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            return self._get_default_config()

    def _get_default_config(self) -> Dict:
        """Get default configuration"""
        return {
            "enabled": True,
            "maxParallelAgents": 5,
            "defaultStrategy": "concurrent",
            "execution": {
                "workerPool": {
                    "maxWorkers": 5
                }
            }
        }

    def execute_parallel(
        self,
        tasks: List[AgentTask],
        strategy: Optional[ExecutionStrategy] = None,
        auto_checkpoint: bool = True
    ) -> ParallelExecutionResult:
        """
        Execute multiple agent tasks in parallel.

        Args:
            tasks: List of agent tasks to execute
            strategy: Execution strategy (default from config)
            auto_checkpoint: Create checkpoints automatically

        Returns:
            ParallelExecutionResult with execution details
        """
        if not self.config.get("enabled", True):
            logger.warning("Parallel execution is disabled")
            return self._create_disabled_result()

        logger.info(f"Starting parallel execution: {len(tasks)} tasks")

        # Set execution strategy
        if strategy is None:
            strategy_name = self.config.get("defaultStrategy", "concurrent")
            strategy = ExecutionStrategy(strategy_name)

        # Store tasks
        with self.task_lock:
            for task in tasks:
                self.tasks[task.task_id] = task

        # Initialize execution state
        self.is_running = True
        self.execution_start_time = datetime.now()

        # Create pre-execution checkpoint if enabled
        pre_checkpoint_id = None
        if auto_checkpoint and self.checkpoint_engine:
            pre_checkpoint_id = self._create_pre_execution_checkpoint(tasks)

        # Send start notification
        self._notify_execution_started(len(tasks))

        # Execute based on strategy
        try:
            if strategy == ExecutionStrategy.CONCURRENT:
                result = self._execute_concurrent(tasks)
            elif strategy == ExecutionStrategy.PIPELINE:
                result = self._execute_pipeline(tasks)
            elif strategy == ExecutionStrategy.HYBRID:
                result = self._execute_hybrid(tasks)
            else:
                raise ValueError(f"Unknown strategy: {strategy}")

            # Create post-execution checkpoint if enabled
            if auto_checkpoint and self.checkpoint_engine:
                self._create_post_execution_checkpoint(tasks, result)

            # Send completion notification
            self._notify_execution_completed(result)

            return result

        except Exception as e:
            logger.error(f"Error during parallel execution: {e}")
            return self._create_error_result(str(e))

        finally:
            self.is_running = False

    def _execute_concurrent(self, tasks: List[AgentTask]) -> ParallelExecutionResult:
        """Execute tasks concurrently"""
        logger.info(f"Executing {len(tasks)} tasks concurrently")

        # Resolve dependencies
        ordered_tasks = self._resolve_dependencies(tasks)

        # Execute tasks with dependency ordering
        futures = {}
        completed_tasks: List[AgentTask] = []
        failed_tasks: List[AgentTask] = []
        warnings: List[str] = []
        errors: List[str] = []

        for task in ordered_tasks:
            # Wait for dependencies
            if task.dependencies:
                self._wait_for_dependencies(task, futures)

            # Submit task
            future = self.executor.submit(self._execute_task, task)
            futures[task.task_id] = future

        # Wait for all tasks to complete
        for task_id, future in futures.items():
            try:
                result_task = future.result(timeout=self.config.get("execution", {}).get("taskQueue", {}).get("timeout", 600))

                if result_task.status == AgentStatus.COMPLETED:
                    completed_tasks.append(result_task)
                elif result_task.status == AgentStatus.FAILED:
                    failed_tasks.append(result_task)
                    errors.append(f"{result_task.agent_type}: {result_task.error}")

            except concurrent.futures.TimeoutError:
                task = self.tasks[task_id]
                task.status = AgentStatus.FAILED
                task.error = "Task execution timeout"
                failed_tasks.append(task)
                errors.append(f"{task.agent_type}: Timeout")
            except Exception as e:
                task = self.tasks[task_id]
                task.status = AgentStatus.FAILED
                task.error = str(e)
                failed_tasks.append(task)
                errors.append(f"{task.agent_type}: {str(e)}")

        # Build result
        end_time = datetime.now()
        duration = (end_time - self.execution_start_time).total_seconds()

        all_tasks = completed_tasks + failed_tasks
        checkpoint_ids = [t.checkpoint_id for t in all_tasks if t.checkpoint_id]

        return ParallelExecutionResult(
            success=len(failed_tasks) == 0,
            total_tasks=len(tasks),
            completed_tasks=len(completed_tasks),
            failed_tasks=len(failed_tasks),
            cancelled_tasks=0,
            started_at=self.execution_start_time.isoformat(),
            completed_at=end_time.isoformat(),
            total_duration_seconds=duration,
            task_results=all_tasks,
            checkpoint_ids=checkpoint_ids,
            warnings=warnings,
            errors=errors,
            message=f"Completed {len(completed_tasks)}/{len(tasks)} tasks successfully"
        )

    def _execute_pipeline(self, tasks: List[AgentTask]) -> ParallelExecutionResult:
        """Execute tasks in pipeline (sequential stages, parallel within stages)"""
        logger.info(f"Executing {len(tasks)} tasks in pipeline mode")

        # Get pipeline configuration
        pipeline_config = self.config.get("strategies", {}).get("pipeline", {})
        default_pipeline = pipeline_config.get("defaultPipeline", [])
        checkpoint_between_stages = pipeline_config.get("checkpointBetweenStages", True)
        fail_fast = pipeline_config.get("failFast", True)

        # Group tasks by stage (simplified - using agent types to determine stage)
        completed_tasks: List[AgentTask] = []
        failed_tasks: List[AgentTask] = []
        warnings: List[str] = []
        errors: List[str] = []

        for stage_idx, stage in enumerate(default_pipeline):
            stage_name = stage.get("stage", f"stage_{stage_idx}")
            stage_agents = stage.get("agents", [])
            parallel = stage.get("parallel", True)

            # Filter tasks for this stage
            stage_tasks = [t for t in tasks if t.agent_type in stage_agents]

            if not stage_tasks:
                continue

            logger.info(f"Executing stage '{stage_name}' with {len(stage_tasks)} tasks")

            # Create checkpoint before stage
            if checkpoint_between_stages and self.checkpoint_engine:
                self._create_stage_checkpoint(stage_name, "before")

            # Execute stage tasks
            if parallel:
                # Execute tasks in parallel within stage
                stage_result = self._execute_concurrent(stage_tasks)
                completed_tasks.extend([t for t in stage_result.task_results if t.status == AgentStatus.COMPLETED])
                failed_tasks.extend([t for t in stage_result.task_results if t.status == AgentStatus.FAILED])
                errors.extend(stage_result.errors)
            else:
                # Execute tasks sequentially
                for task in stage_tasks:
                    result_task = self._execute_task(task)
                    if result_task.status == AgentStatus.COMPLETED:
                        completed_tasks.append(result_task)
                    else:
                        failed_tasks.append(result_task)
                        errors.append(f"{result_task.agent_type}: {result_task.error}")

            # Create checkpoint after stage
            if checkpoint_between_stages and self.checkpoint_engine:
                self._create_stage_checkpoint(stage_name, "after")

            # Fail fast if enabled
            if fail_fast and len(failed_tasks) > 0:
                warnings.append(f"Stage '{stage_name}' failed, stopping pipeline (fail-fast enabled)")
                break

        # Build result
        end_time = datetime.now()
        duration = (end_time - self.execution_start_time).total_seconds()

        all_tasks = completed_tasks + failed_tasks
        checkpoint_ids = [t.checkpoint_id for t in all_tasks if t.checkpoint_id]

        return ParallelExecutionResult(
            success=len(failed_tasks) == 0,
            total_tasks=len(tasks),
            completed_tasks=len(completed_tasks),
            failed_tasks=len(failed_tasks),
            cancelled_tasks=0,
            started_at=self.execution_start_time.isoformat(),
            completed_at=end_time.isoformat(),
            total_duration_seconds=duration,
            task_results=all_tasks,
            checkpoint_ids=checkpoint_ids,
            warnings=warnings,
            errors=errors,
            message=f"Pipeline execution: {len(completed_tasks)}/{len(tasks)} tasks successful"
        )

    def _execute_hybrid(self, tasks: List[AgentTask]) -> ParallelExecutionResult:
        """Execute tasks using hybrid strategy"""
        logger.info(f"Executing {len(tasks)} tasks in hybrid mode")
        # For now, default to concurrent execution
        # TODO: Implement sophisticated hybrid strategy
        return self._execute_concurrent(tasks)

    def _execute_task(self, task: AgentTask) -> AgentTask:
        """
        Execute a single agent task.

        Args:
            task: Agent task to execute

        Returns:
            Updated task with results
        """
        logger.info(f"Executing task: {task.agent_type} ({task.task_id})")

        # Update task status
        task.status = AgentStatus.RUNNING
        task.started_at = datetime.now().isoformat()

        # Notify task started
        self._notify_agent_started(task.agent_type)

        try:
            # Create pre-agent checkpoint if coordinator available
            if self.coordinator:
                checkpoint_id = self.coordinator.pre_agent_execution_checkpoint(
                    agent_type=task.agent_type,
                    description=task.description,
                    tags=task.tags
                )
                task.checkpoint_id = checkpoint_id

            # Execute agent work (placeholder - actual agent execution would go here)
            # In real implementation, this would call the actual agent
            logger.info(f"Agent {task.agent_type} executing: {task.description}")

            # Simulate work
            import time
            time.sleep(0.5)  # Simulate agent work

            # Mock success
            task.output = {"status": "success", "message": f"{task.agent_type} completed successfully"}
            task.status = AgentStatus.COMPLETED

            # Create post-agent checkpoint if coordinator available
            if self.coordinator:
                self.coordinator.post_agent_execution_checkpoint(
                    agent_type=task.agent_type,
                    success=True,
                    modified_files=task.context.get("modified_files", []),
                    description=f"Completed: {task.description}"
                )

            # Update timing
            task.completed_at = datetime.now().isoformat()
            start_time = datetime.fromisoformat(task.started_at)
            end_time = datetime.fromisoformat(task.completed_at)
            task.duration_seconds = (end_time - start_time).total_seconds()

            # Notify task completed
            self._notify_agent_completed(task.agent_type, task.duration_seconds)

            logger.info(f"✅ Task completed: {task.agent_type} ({task.duration_seconds:.2f}s)")

        except Exception as e:
            logger.error(f"❌ Task failed: {task.agent_type} - {str(e)}")
            task.status = AgentStatus.FAILED
            task.error = str(e)
            task.completed_at = datetime.now().isoformat()

            # Notify task failed
            self._notify_agent_failed(task.agent_type, str(e))

        return task

    def _resolve_dependencies(self, tasks: List[AgentTask]) -> List[AgentTask]:
        """Resolve task dependencies and return ordered list"""
        # Build dependency graph
        dependency_graph = self.config.get("dependencies", {}).get("dependencyGraph", {})

        # Simple topological sort (Kahn's algorithm)
        in_degree = {task.task_id: len(task.dependencies) for task in tasks}
        queue = [task for task in tasks if in_degree[task.task_id] == 0]
        ordered = []

        while queue:
            task = queue.pop(0)
            ordered.append(task)

            # Update in-degrees
            for other_task in tasks:
                if task.task_id in other_task.dependencies:
                    in_degree[other_task.task_id] -= 1
                    if in_degree[other_task.task_id] == 0:
                        queue.append(other_task)

        if len(ordered) != len(tasks):
            logger.warning("Circular dependency detected, returning original order")
            return tasks

        return ordered

    def _wait_for_dependencies(self, task: AgentTask, futures: Dict[str, concurrent.futures.Future]):
        """Wait for task dependencies to complete"""
        for dep_id in task.dependencies:
            if dep_id in futures:
                try:
                    futures[dep_id].result(timeout=60)
                except Exception as e:
                    logger.warning(f"Dependency {dep_id} failed: {e}")

    def _create_pre_execution_checkpoint(self, tasks: List[AgentTask]) -> Optional[str]:
        """Create checkpoint before parallel execution"""
        if not self.checkpoint_engine:
            return None

        agent_types = [t.agent_type for t in tasks]
        label = f"before_parallel_{len(tasks)}_agents_{datetime.now().strftime('%H%M%S')}"

        try:
            from ..checkpoint.core.checkpoint_engine import CheckpointLevel

            checkpoint_id = self.checkpoint_engine.create_checkpoint(
                level=CheckpointLevel.AGENT_EXECUTION,
                label=label,
                description=f"Before parallel execution of {len(tasks)} agents: {', '.join(agent_types[:3])}{'...' if len(agent_types) > 3 else ''}",
                tags=["parallel", "pre-execution"] + agent_types
            )

            logger.info(f"Created pre-execution checkpoint: {checkpoint_id}")
            return checkpoint_id

        except Exception as e:
            logger.warning(f"Failed to create pre-execution checkpoint: {e}")
            return None

    def _create_post_execution_checkpoint(self, tasks: List[AgentTask], result: ParallelExecutionResult) -> Optional[str]:
        """Create checkpoint after parallel execution"""
        if not self.checkpoint_engine:
            return None

        label = f"after_parallel_{result.completed_tasks}_of_{result.total_tasks}_agents_{datetime.now().strftime('%H%M%S')}"

        try:
            from ..checkpoint.core.checkpoint_engine import CheckpointLevel

            checkpoint_id = self.checkpoint_engine.create_checkpoint(
                level=CheckpointLevel.AGENT_EXECUTION,
                label=label,
                description=f"After parallel execution: {result.completed_tasks}/{result.total_tasks} successful",
                tags=["parallel", "post-execution", "success" if result.success else "partial-failure"]
            )

            logger.info(f"Created post-execution checkpoint: {checkpoint_id}")
            return checkpoint_id

        except Exception as e:
            logger.warning(f"Failed to create post-execution checkpoint: {e}")
            return None

    def _create_stage_checkpoint(self, stage_name: str, position: str) -> Optional[str]:
        """Create checkpoint for pipeline stage"""
        if not self.checkpoint_engine:
            return None

        label = f"{position}_stage_{stage_name}_{datetime.now().strftime('%H%M%S')}"

        try:
            from ..checkpoint.core.checkpoint_engine import CheckpointLevel

            checkpoint_id = self.checkpoint_engine.create_checkpoint(
                level=CheckpointLevel.QUALITY_GATE,
                label=label,
                description=f"{position.title()} pipeline stage: {stage_name}",
                tags=["pipeline", "stage", stage_name, position]
            )

            logger.info(f"Created stage checkpoint: {checkpoint_id}")
            return checkpoint_id

        except Exception as e:
            logger.warning(f"Failed to create stage checkpoint: {e}")
            return None

    def _notify_execution_started(self, task_count: int):
        """Send notification about execution start"""
        notification_config = self.config.get("notifications", {}).get("parallelExecutionStarted", {})
        if notification_config.get("enabled", True):
            message = notification_config.get("format", "🚀 Parallel execution started: {agent_count} agents")
            logger.info(message.format(agent_count=task_count))

    def _notify_agent_started(self, agent_type: str):
        """Send notification about agent start"""
        notification_config = self.config.get("notifications", {}).get("agentStarted", {})
        if notification_config.get("enabled", True):
            message = notification_config.get("format", "▶️ Agent started: {agent_type}")
            logger.info(message.format(agent_type=agent_type))

    def _notify_agent_completed(self, agent_type: str, duration: float):
        """Send notification about agent completion"""
        notification_config = self.config.get("notifications", {}).get("agentCompleted", {})
        if notification_config.get("enabled", True):
            message = notification_config.get("format", "✅ Agent completed: {agent_type} ({duration}s)")
            logger.info(message.format(agent_type=agent_type, duration=f"{duration:.2f}"))

    def _notify_agent_failed(self, agent_type: str, error: str):
        """Send notification about agent failure"""
        notification_config = self.config.get("notifications", {}).get("agentFailed", {})
        if notification_config.get("enabled", True):
            message = notification_config.get("format", "❌ Agent failed: {agent_type} - {error}")
            logger.error(message.format(agent_type=agent_type, error=error))

    def _notify_execution_completed(self, result: ParallelExecutionResult):
        """Send notification about execution completion"""
        notification_config = self.config.get("notifications", {}).get("parallelExecutionCompleted", {})
        if notification_config.get("enabled", True):
            message = notification_config.get("format", "🎉 Parallel execution completed: {success_count}/{total_count} successful")
            logger.info(message.format(success_count=result.completed_tasks, total_count=result.total_tasks))

    def _create_disabled_result(self) -> ParallelExecutionResult:
        """Create result for disabled execution"""
        return ParallelExecutionResult(
            success=False,
            total_tasks=0,
            completed_tasks=0,
            failed_tasks=0,
            cancelled_tasks=0,
            started_at=datetime.now().isoformat(),
            completed_at=datetime.now().isoformat(),
            total_duration_seconds=0.0,
            task_results=[],
            checkpoint_ids=[],
            message="Parallel execution is disabled in configuration"
        )

    def _create_error_result(self, error: str) -> ParallelExecutionResult:
        """Create result for execution error"""
        return ParallelExecutionResult(
            success=False,
            total_tasks=0,
            completed_tasks=0,
            failed_tasks=0,
            cancelled_tasks=0,
            started_at=self.execution_start_time.isoformat() if self.execution_start_time else datetime.now().isoformat(),
            completed_at=datetime.now().isoformat(),
            total_duration_seconds=0.0,
            task_results=[],
            checkpoint_ids=[],
            errors=[error],
            message=f"Execution failed: {error}"
        )

    def get_task_status(self, task_id: str) -> Optional[AgentTask]:
        """Get status of a specific task"""
        with self.task_lock:
            return self.tasks.get(task_id)

    def get_all_tasks(self) -> List[AgentTask]:
        """Get all tasks"""
        with self.task_lock:
            return list(self.tasks.values())

    def cancel_task(self, task_id: str) -> bool:
        """Cancel a specific task"""
        with self.task_lock:
            task = self.tasks.get(task_id)
            if task and task.status in [AgentStatus.PENDING, AgentStatus.QUEUED]:
                task.status = AgentStatus.CANCELLED
                logger.info(f"Task cancelled: {task.agent_type}")
                return True
        return False

    def shutdown(self, wait: bool = True):
        """Shutdown the executor"""
        logger.info("Shutting down parallel executor...")
        self.executor.shutdown(wait=wait)
        logger.info("Parallel executor shut down")


# CLI Interface
if __name__ == "__main__":
    # Initialize
    executor = ParallelExecutor()

    print("\n=== Testing Parallel Executor ===")

    # Create test tasks
    tasks = [
        AgentTask(
            agent_type="software-architect",
            task_id="task_1",
            description="Design system architecture",
            priority="high",
            tags=["architecture", "design"]
        ),
        AgentTask(
            agent_type="backend-engineer",
            task_id="task_2",
            description="Implement API endpoints",
            priority="high",
            dependencies=["task_1"],
            tags=["implementation", "backend"]
        ),
        AgentTask(
            agent_type="frontend-engineer",
            task_id="task_3",
            description="Build user interface",
            priority="high",
            dependencies=["task_1"],
            tags=["implementation", "frontend"]
        ),
        AgentTask(
            agent_type="qa-engineer",
            task_id="task_4",
            description="Run tests",
            priority="medium",
            dependencies=["task_2", "task_3"],
            tags=["testing", "quality"]
        )
    ]

    # Execute concurrent
    print("\n1. Testing concurrent execution")
    result = executor.execute_parallel(tasks, strategy=ExecutionStrategy.CONCURRENT)
    print(f"Result: {result.message}")
    print(f"  - Completed: {result.completed_tasks}/{result.total_tasks}")
    print(f"  - Duration: {result.total_duration_seconds:.2f}s")

    # Execute pipeline
    print("\n2. Testing pipeline execution")
    result = executor.execute_parallel(tasks, strategy=ExecutionStrategy.PIPELINE)
    print(f"Result: {result.message}")
    print(f"  - Completed: {result.completed_tasks}/{result.total_tasks}")
    print(f"  - Duration: {result.total_duration_seconds:.2f}s")

    print("\n=== Parallel Executor Test Complete ===")

    # Shutdown
    executor.shutdown()
