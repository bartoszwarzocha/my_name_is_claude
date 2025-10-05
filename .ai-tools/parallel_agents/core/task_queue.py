#!/usr/bin/env python3
"""
Task Queue Manager for Parallel Agent Execution System

Priority-based task queue with dependency management and resource awareness.

Part of Framework v3.8.0 - Parallel Agent Execution System
"""

import logging
import threading
from collections import deque
from dataclasses import dataclass
from typing import Dict, List, Optional, Set
from enum import Enum
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Priority(Enum):
    """Task priority levels"""
    CRITICAL = 0
    HIGH = 1
    MEDIUM = 2
    LOW = 3


@dataclass
class QueuedTask:
    """Task in queue"""
    task_id: str
    agent_type: str
    priority: Priority
    dependencies: Set[str]
    queued_at: str
    metadata: Dict


class TaskQueue:
    """
    Priority-based task queue with dependency management.

    Features:
    - Priority-based ordering
    - Dependency tracking
    - Resource-aware scheduling
    - Thread-safe operations
    """

    def __init__(self, max_size: int = 100):
        """
        Initialize task queue.

        Args:
            max_size: Maximum queue size
        """
        self.max_size = max_size

        # Separate queues per priority
        self.queues: Dict[Priority, deque] = {
            Priority.CRITICAL: deque(),
            Priority.HIGH: deque(),
            Priority.MEDIUM: deque(),
            Priority.LOW: deque()
        }

        # Task tracking
        self.tasks: Dict[str, QueuedTask] = {}
        self.completed: Set[str] = set()

        # Thread safety
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)

        logger.info(f"Task Queue initialized (max size: {max_size})")

    def enqueue(self, task_id: str, agent_type: str, priority: str = "medium", dependencies: Optional[List[str]] = None, metadata: Optional[Dict] = None) -> bool:
        """
        Add task to queue.

        Args:
            task_id: Unique task identifier
            agent_type: Agent type
            priority: Task priority (critical/high/medium/low)
            dependencies: List of task IDs this task depends on
            metadata: Additional task metadata

        Returns:
            True if task was queued successfully
        """
        with self.lock:
            # Check queue size
            total_size = sum(len(q) for q in self.queues.values())
            if total_size >= self.max_size:
                logger.warning(f"Queue full ({self.max_size}), cannot enqueue task: {task_id}")
                return False

            # Check if task already exists
            if task_id in self.tasks:
                logger.warning(f"Task already queued: {task_id}")
                return False

            # Create queued task
            priority_enum = self._parse_priority(priority)
            queued_task = QueuedTask(
                task_id=task_id,
                agent_type=agent_type,
                priority=priority_enum,
                dependencies=set(dependencies or []),
                queued_at=datetime.now().isoformat(),
                metadata=metadata or {}
            )

            # Add to appropriate priority queue
            self.queues[priority_enum].append(queued_task)
            self.tasks[task_id] = queued_task

            logger.info(f"Task queued: {task_id} ({agent_type}, priority: {priority})")

            # Notify waiting threads
            self.not_empty.notify()

            return True

    def dequeue(self, timeout: Optional[float] = None) -> Optional[QueuedTask]:
        """
        Get next ready task from queue.

        Args:
            timeout: Maximum wait time in seconds

        Returns:
            Next ready task or None
        """
        with self.not_empty:
            # Wait for tasks if queue is empty
            while self._is_empty():
                if not self.not_empty.wait(timeout):
                    return None

            # Get highest priority task with satisfied dependencies
            for priority in Priority:
                queue = self.queues[priority]
                for task in list(queue):
                    if self._are_dependencies_satisfied(task):
                        queue.remove(task)
                        logger.info(f"Task dequeued: {task.task_id} ({task.agent_type})")
                        return task

            return None

    def mark_completed(self, task_id: str):
        """
        Mark task as completed.

        Args:
            task_id: Task identifier
        """
        with self.lock:
            if task_id in self.tasks:
                self.completed.add(task_id)
                del self.tasks[task_id]
                logger.info(f"Task marked completed: {task_id}")

                # Notify waiting threads (dependencies may now be satisfied)
                self.not_empty.notify_all()

    def _are_dependencies_satisfied(self, task: QueuedTask) -> bool:
        """Check if all task dependencies are completed"""
        return all(dep_id in self.completed for dep_id in task.dependencies)

    def _is_empty(self) -> bool:
        """Check if queue is empty"""
        return all(len(q) == 0 for q in self.queues.values())

    def _parse_priority(self, priority: str) -> Priority:
        """Parse priority string to enum"""
        priority_map = {
            "critical": Priority.CRITICAL,
            "high": Priority.HIGH,
            "medium": Priority.MEDIUM,
            "low": Priority.LOW
        }
        return priority_map.get(priority.lower(), Priority.MEDIUM)

    def size(self) -> int:
        """Get total queue size"""
        with self.lock:
            return sum(len(q) for q in self.queues.values())

    def get_statistics(self) -> Dict:
        """Get queue statistics"""
        with self.lock:
            return {
                "total_queued": sum(len(q) for q in self.queues.values()),
                "by_priority": {
                    "critical": len(self.queues[Priority.CRITICAL]),
                    "high": len(self.queues[Priority.HIGH]),
                    "medium": len(self.queues[Priority.MEDIUM]),
                    "low": len(self.queues[Priority.LOW])
                },
                "completed": len(self.completed)
            }


# CLI Interface
if __name__ == "__main__":
    # Test task queue
    print("\n=== Testing Task Queue ===")

    queue = TaskQueue(max_size=10)

    # Enqueue tasks
    print("\n1. Enqueuing tasks")
    queue.enqueue("task_1", "software-architect", priority="high")
    queue.enqueue("task_2", "backend-engineer", priority="medium", dependencies=["task_1"])
    queue.enqueue("task_3", "frontend-engineer", priority="medium", dependencies=["task_1"])
    queue.enqueue("task_4", "qa-engineer", priority="low", dependencies=["task_2", "task_3"])

    # Get statistics
    print("\n2. Queue statistics")
    stats = queue.get_statistics()
    print(f"Total queued: {stats['total_queued']}")
    print(f"By priority: {stats['by_priority']}")

    # Dequeue tasks
    print("\n3. Dequeuing tasks")
    task = queue.dequeue()
    if task:
        print(f"Dequeued: {task.task_id} ({task.agent_type})")
        queue.mark_completed(task.task_id)

    task = queue.dequeue()
    if task:
        print(f"Dequeued: {task.task_id} ({task.agent_type})")
        queue.mark_completed(task.task_id)

    print("\n=== Task Queue Test Complete ===")
