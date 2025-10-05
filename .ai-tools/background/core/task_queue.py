#!/usr/bin/env python3
"""
Task Queue Manager - My Name Is Claude Framework v3.5.0

Priority-based task queue with intelligent scheduling.

This is a TEMPLATE implementation. Actual implementation should:
1. Adapt to project workload patterns
2. Integrate with existing scheduling systems
3. Follow project-specific priority rules
"""

import json
import time
import heapq
import threading
from pathlib import Path
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field, asdict
from datetime import datetime
from collections import defaultdict
import logging

logger = logging.getLogger(__name__)


@dataclass(order=True)
class QueuedTask:
    """Task in queue with priority"""
    priority: int = field(compare=True)
    task_id: str = field(compare=False)
    task_data: Dict = field(default_factory=dict, compare=False)
    queued_at: str = field(default_factory=lambda: datetime.now().isoformat(), compare=False)


class TaskQueue:
    """
    Priority-based task queue with intelligent scheduling
    """

    def __init__(self, max_size: int = 1000):
        """
        Initialize task queue

        Args:
            max_size: Maximum queue size
        """
        self.max_size = max_size
        self.queue: List[QueuedTask] = []
        self.task_index: Dict[str, QueuedTask] = {}
        self.lock = threading.Lock()
        self.stats = {
            'total_queued': 0,
            'total_dequeued': 0,
            'total_dropped': 0,
            'current_size': 0
        }

    def enqueue(self, task_id: str, task_data: Dict, priority: int = 10) -> bool:
        """
        Add task to queue

        Args:
            task_id: Unique task identifier
            task_data: Task data
            priority: Task priority (higher = more important)

        Returns:
            True if task was queued
        """
        with self.lock:
            # Check if task already in queue
            if task_id in self.task_index:
                logger.warning(f"Task {task_id} already in queue, skipping")
                return False

            # Check queue size
            if len(self.queue) >= self.max_size:
                logger.warning(f"Queue full ({self.max_size}), dropping oldest low-priority task")
                self._drop_lowest_priority_task()
                self.stats['total_dropped'] += 1

            # Add to queue
            queued_task = QueuedTask(
                priority=-priority,  # Negative for min-heap behavior (higher priority = lower number)
                task_id=task_id,
                task_data=task_data
            )

            heapq.heappush(self.queue, queued_task)
            self.task_index[task_id] = queued_task
            self.stats['total_queued'] += 1
            self.stats['current_size'] = len(self.queue)

            logger.info(f"Queued task {task_id} with priority {priority} (queue size: {len(self.queue)})")
            return True

    def dequeue(self) -> Optional[Dict]:
        """
        Remove and return highest priority task

        Returns:
            Task data or None if queue empty
        """
        with self.lock:
            if not self.queue:
                return None

            queued_task = heapq.heappop(self.queue)
            del self.task_index[queued_task.task_id]

            self.stats['total_dequeued'] += 1
            self.stats['current_size'] = len(self.queue)

            # Add queue time to task data
            queued_at = datetime.fromisoformat(queued_task.queued_at)
            queue_time = (datetime.now() - queued_at).total_seconds()
            queued_task.task_data['queue_time'] = queue_time

            logger.info(f"Dequeued task {queued_task.task_id} (queued for {queue_time:.1f}s)")
            return queued_task.task_data

    def peek(self) -> Optional[Dict]:
        """
        Get highest priority task without removing

        Returns:
            Task data or None if queue empty
        """
        with self.lock:
            if not self.queue:
                return None
            return self.queue[0].task_data

    def remove(self, task_id: str) -> bool:
        """
        Remove specific task from queue

        Args:
            task_id: Task ID to remove

        Returns:
            True if task was removed
        """
        with self.lock:
            if task_id not in self.task_index:
                return False

            # Remove from index
            queued_task = self.task_index[task_id]
            del self.task_index[task_id]

            # Remove from heap (expensive operation, but rare)
            self.queue.remove(queued_task)
            heapq.heapify(self.queue)

            self.stats['current_size'] = len(self.queue)
            logger.info(f"Removed task {task_id} from queue")
            return True

    def _drop_lowest_priority_task(self):
        """Drop lowest priority task to make room"""
        if not self.queue:
            return

        # Find task with lowest priority (highest number due to negation)
        lowest_priority_task = max(self.queue, key=lambda t: t.priority)

        # Remove it
        self.queue.remove(lowest_priority_task)
        heapq.heapify(self.queue)
        del self.task_index[lowest_priority_task.task_id]

        logger.warning(f"Dropped low-priority task {lowest_priority_task.task_id}")

    def clear(self):
        """Clear all tasks from queue"""
        with self.lock:
            self.queue.clear()
            self.task_index.clear()
            self.stats['current_size'] = 0
            logger.info("Queue cleared")

    def size(self) -> int:
        """Get current queue size"""
        with self.lock:
            return len(self.queue)

    def is_empty(self) -> bool:
        """Check if queue is empty"""
        with self.lock:
            return len(self.queue) == 0

    def get_stats(self) -> Dict:
        """Get queue statistics"""
        with self.lock:
            return self.stats.copy()

    def get_tasks_by_priority(self) -> Dict[int, List[str]]:
        """Get tasks grouped by priority"""
        with self.lock:
            by_priority = defaultdict(list)
            for task in self.queue:
                by_priority[-task.priority].append(task.task_id)
            return dict(by_priority)


class SmartTaskScheduler:
    """
    Intelligent task scheduler with adaptive prioritization
    """

    def __init__(self, queue: TaskQueue):
        """
        Initialize scheduler

        Args:
            queue: Task queue to manage
        """
        self.queue = queue
        self.task_history: Dict[str, List[float]] = defaultdict(list)
        self.running_tasks: set = set()
        self.lock = threading.Lock()

    def schedule_task(
        self,
        task_id: str,
        task_type: str,
        task_data: Dict,
        base_priority: int = 10
    ) -> bool:
        """
        Schedule task with adaptive priority

        Args:
            task_id: Task identifier
            task_type: Type of task
            task_data: Task data
            base_priority: Base priority level

        Returns:
            True if task was scheduled
        """
        # Calculate adaptive priority
        priority = self._calculate_adaptive_priority(task_type, base_priority)

        # Add metadata
        task_data['task_id'] = task_id
        task_data['task_type'] = task_type
        task_data['base_priority'] = base_priority
        task_data['calculated_priority'] = priority

        return self.queue.enqueue(task_id, task_data, priority)

    def _calculate_adaptive_priority(self, task_type: str, base_priority: int) -> int:
        """
        Calculate adaptive priority based on task history

        Args:
            task_type: Type of task
            base_priority: Base priority

        Returns:
            Adjusted priority
        """
        # Start with base priority
        priority = base_priority

        # Get task history
        history = self.task_history.get(task_type, [])

        if history:
            # If task type has been failing or timing out, increase priority
            recent_failures = sum(1 for t in history[-10:] if t < 0)
            if recent_failures > 5:
                priority += 20  # Boost priority for problematic tasks

            # If task type completes quickly, slightly decrease priority
            avg_time = sum(abs(t) for t in history[-10:]) / len(history[-10:])
            if avg_time < 10:  # Quick tasks
                priority -= 5

        return max(1, priority)  # Ensure priority is at least 1

    def record_task_completion(self, task_type: str, duration: float, success: bool):
        """
        Record task completion for adaptive learning

        Args:
            task_type: Type of task
            duration: Execution duration
            success: Whether task succeeded
        """
        with self.lock:
            # Store duration (negative if failed)
            self.task_history[task_type].append(duration if success else -duration)

            # Keep only recent history
            if len(self.task_history[task_type]) > 100:
                self.task_history[task_type] = self.task_history[task_type][-100:]

    def mark_running(self, task_id: str):
        """Mark task as running"""
        with self.lock:
            self.running_tasks.add(task_id)

    def mark_completed(self, task_id: str):
        """Mark task as completed"""
        with self.lock:
            self.running_tasks.discard(task_id)

    def get_next_task(self) -> Optional[Dict]:
        """
        Get next task to execute

        Returns:
            Task data or None
        """
        task_data = self.queue.dequeue()
        if task_data:
            self.mark_running(task_data['task_id'])
        return task_data

    def cancel_task(self, task_id: str) -> bool:
        """
        Cancel a queued task

        Args:
            task_id: Task to cancel

        Returns:
            True if task was cancelled
        """
        return self.queue.remove(task_id)

    def get_queue_info(self) -> Dict:
        """Get comprehensive queue information"""
        return {
            'stats': self.queue.get_stats(),
            'tasks_by_priority': self.queue.get_tasks_by_priority(),
            'running_tasks': len(self.running_tasks),
            'current_size': self.queue.size()
        }


def main():
    """CLI for task queue testing"""
    import argparse

    parser = argparse.ArgumentParser(description='Task Queue Manager')
    parser.add_argument('command', choices=['enqueue', 'dequeue', 'stats', 'clear'])
    parser.add_argument('--task-id', help='Task ID')
    parser.add_argument('--priority', type=int, default=10, help='Task priority')
    parser.add_argument('--data', help='Task data (JSON string)')

    args = parser.parse_args()

    queue = TaskQueue()

    if args.command == 'enqueue':
        if not args.task_id:
            print("Error: --task-id required")
            return

        task_data = json.loads(args.data) if args.data else {}
        success = queue.enqueue(args.task_id, task_data, args.priority)
        print(f"Task {'queued' if success else 'failed to queue'}")

    elif args.command == 'dequeue':
        task_data = queue.dequeue()
        if task_data:
            print(json.dumps(task_data, indent=2))
        else:
            print("Queue is empty")

    elif args.command == 'stats':
        stats = queue.get_stats()
        print(json.dumps(stats, indent=2))

    elif args.command == 'clear':
        queue.clear()
        print("Queue cleared")


if __name__ == '__main__':
    main()
