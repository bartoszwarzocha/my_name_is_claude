#!/usr/bin/env python3
"""
Background Task Runner - My Name Is Claude Framework v3.5.0

Main task execution engine for background task management.

This is a TEMPLATE implementation. Actual implementation should:
1. Adapt to project environment and requirements
2. Integrate with existing monitoring systems
3. Follow project-specific execution patterns
"""

import os
import sys
import json
import time
import signal
import logging
import multiprocessing
from pathlib import Path
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field, asdict
from enum import Enum
from datetime import datetime
import traceback

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(name)s] %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('project_archive/logs/background-tasks.log')
    ]
)
logger = logging.getLogger(__name__)


class TaskStatus(Enum):
    """Task execution status"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    TIMEOUT = "timeout"
    CANCELLED = "cancelled"


class TaskPriority(Enum):
    """Task priority levels"""
    CRITICAL = 1000
    HIGH = 100
    MEDIUM = 10
    LOW = 1


@dataclass
class TaskResult:
    """Result of task execution"""
    task_id: str
    task_name: str
    status: TaskStatus
    start_time: str
    end_time: Optional[str] = None
    duration: float = 0.0
    output: str = ""
    error: str = ""
    exit_code: int = 0
    retries: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class BackgroundTask:
    """Background task definition"""
    task_id: str
    name: str
    task_type: str
    priority: str
    timeout: int
    command: Optional[List[str]] = None
    function: Optional[Callable] = None
    args: tuple = field(default_factory=tuple)
    kwargs: Dict = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    status: TaskStatus = TaskStatus.PENDING
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    started_at: Optional[str] = None
    completed_at: Optional[str] = None


class BackgroundTaskRunner:
    """
    Main background task execution engine with process isolation
    and resource management
    """

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize background task runner

        Args:
            config_path: Path to configuration file
        """
        self.config_path = config_path or self._get_default_config_path()
        self.config = self._load_config()
        self.running_tasks: Dict[str, multiprocessing.Process] = {}
        self.task_results: Dict[str, TaskResult] = {}
        self.shutdown_requested = False

        # Setup signal handlers
        signal.signal(signal.SIGINT, self._handle_shutdown)
        signal.signal(signal.SIGTERM, self._handle_shutdown)

        # Create necessary directories
        self._ensure_directories()

        # Load previous state if exists
        self._load_state()

    def _get_default_config_path(self) -> str:
        """Get default configuration path"""
        current_dir = Path.cwd()
        while current_dir != current_dir.parent:
            config_file = current_dir / '.claude' / 'config' / 'background-tasks.json'
            if config_file.exists():
                return str(config_file)
            current_dir = current_dir.parent
        return '.claude/config/background-tasks.json'

    def _load_config(self) -> Dict:
        """Load configuration file"""
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            return self._get_default_config()

    def _get_default_config(self) -> Dict:
        """Get default configuration"""
        return {
            "enabled": True,
            "execution": {
                "max_concurrent_tasks": 5,
                "task_timeout_seconds": 3600,
                "process_isolation": True,
                "max_retries": 3
            }
        }

    def _ensure_directories(self):
        """Ensure required directories exist"""
        storage = self.config.get('storage', {})
        for key in ['task_results_dir', 'task_logs_dir']:
            path = storage.get(key, '')
            if path:
                Path(path).mkdir(parents=True, exist_ok=True)

        # Ensure log directory exists
        Path('project_archive/logs').mkdir(parents=True, exist_ok=True)
        Path('project_archive/background-tasks').mkdir(parents=True, exist_ok=True)

    def _load_state(self):
        """Load previous state from disk"""
        storage = self.config.get('storage', {})
        state_file = Path(storage.get('task_state_file', 'project_archive/background-tasks/state.json'))

        if state_file.exists():
            try:
                with open(state_file, 'r') as f:
                    state = json.load(f)
                    # Restore task results
                    for task_id, result_dict in state.get('task_results', {}).items():
                        result_dict['status'] = TaskStatus(result_dict['status'])
                        self.task_results[task_id] = TaskResult(**result_dict)
                    logger.info(f"Loaded state with {len(self.task_results)} task results")
            except Exception as e:
                logger.error(f"Failed to load state: {e}")

    def _save_state(self):
        """Save current state to disk"""
        storage = self.config.get('storage', {})
        state_file = Path(storage.get('task_state_file', 'project_archive/background-tasks/state.json'))

        try:
            state = {
                'task_results': {
                    task_id: {**asdict(result), 'status': result.status.value}
                    for task_id, result in self.task_results.items()
                },
                'timestamp': datetime.now().isoformat()
            }

            state_file.parent.mkdir(parents=True, exist_ok=True)
            with open(state_file, 'w') as f:
                json.dump(state, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save state: {e}")

    def _handle_shutdown(self, signum, frame):
        """Handle shutdown signals"""
        logger.info("Shutdown signal received, stopping all tasks...")
        self.shutdown_requested = True
        self.stop_all_tasks()
        self._save_state()
        sys.exit(0)

    def submit_task(self, task: BackgroundTask) -> str:
        """
        Submit a task for background execution

        Args:
            task: Task to execute

        Returns:
            Task ID
        """
        if not self.config.get('enabled', True):
            logger.warning("Background tasks disabled in configuration")
            return ""

        # Check concurrent task limit
        max_concurrent = self.config.get('execution', {}).get('max_concurrent_tasks', 5)
        if len(self.running_tasks) >= max_concurrent:
            logger.warning(f"Maximum concurrent tasks ({max_concurrent}) reached, queuing task")
            # TODO: Implement task queue
            return task.task_id

        # Start task in background process
        if self.config.get('execution', {}).get('process_isolation', True):
            process = multiprocessing.Process(
                target=self._execute_task_isolated,
                args=(task,),
                name=f"task-{task.task_id}"
            )
            process.start()
            self.running_tasks[task.task_id] = process
            logger.info(f"Started background task: {task.name} (ID: {task.task_id})")
        else:
            # Execute in current process (for debugging)
            self._execute_task_isolated(task)

        return task.task_id

    def _execute_task_isolated(self, task: BackgroundTask):
        """
        Execute task in isolated process

        Args:
            task: Task to execute
        """
        start_time = time.time()
        task.started_at = datetime.now().isoformat()
        task.status = TaskStatus.RUNNING

        result = TaskResult(
            task_id=task.task_id,
            task_name=task.name,
            status=TaskStatus.RUNNING,
            start_time=task.started_at
        )

        try:
            # Execute task
            if task.function:
                # Execute Python function
                output = task.function(*task.args, **task.kwargs)
                result.output = str(output) if output else ""
                result.status = TaskStatus.COMPLETED
                result.exit_code = 0
            elif task.command:
                # Execute shell command
                import subprocess
                proc = subprocess.run(
                    task.command,
                    capture_output=True,
                    text=True,
                    timeout=task.timeout
                )
                result.output = proc.stdout
                result.error = proc.stderr
                result.exit_code = proc.returncode
                result.status = TaskStatus.COMPLETED if proc.returncode == 0 else TaskStatus.FAILED
            else:
                raise ValueError("Task must have either function or command")

        except subprocess.TimeoutExpired:
            result.status = TaskStatus.TIMEOUT
            result.error = f"Task timed out after {task.timeout}s"
            logger.error(f"Task {task.name} timed out")

        except Exception as e:
            result.status = TaskStatus.FAILED
            result.error = str(e) + "\n" + traceback.format_exc()
            logger.error(f"Task {task.name} failed: {e}")

        finally:
            # Record completion
            end_time = time.time()
            result.end_time = datetime.now().isoformat()
            result.duration = end_time - start_time

            # Save result
            self.task_results[task.task_id] = result
            self._save_task_result(result)

            # Remove from running tasks
            if task.task_id in self.running_tasks:
                del self.running_tasks[task.task_id]

            # Send notification
            self._send_notification(result)

            # Save state
            self._save_state()

            logger.info(f"Task {task.name} completed with status: {result.status.value} ({result.duration:.2f}s)")

    def _save_task_result(self, result: TaskResult):
        """Save task result to disk"""
        storage = self.config.get('storage', {})
        results_dir = Path(storage.get('task_results_dir', 'project_archive/background-tasks/results'))
        results_dir.mkdir(parents=True, exist_ok=True)

        result_file = results_dir / f"{result.task_id}.json"
        try:
            with open(result_file, 'w') as f:
                result_dict = asdict(result)
                result_dict['status'] = result.status.value
                json.dump(result_dict, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save task result: {e}")

    def _send_notification(self, result: TaskResult):
        """Send notification about task completion"""
        notification_config = self.config.get('notification_system', {})
        if not notification_config.get('enabled', False):
            return

        # Determine if notification should be sent
        task_config = self.config.get('task_types', {}).get(result.metadata.get('task_type', ''), {})

        should_notify = False
        if result.status == TaskStatus.COMPLETED and task_config.get('notification_on_complete', False):
            should_notify = True
        elif result.status in [TaskStatus.FAILED, TaskStatus.TIMEOUT] and task_config.get('notification_on_issues', True):
            should_notify = True

        if not should_notify:
            return

        # Build notification message
        templates = notification_config.get('notification_templates', {})
        if result.status == TaskStatus.COMPLETED:
            template = templates.get('task_completed', 'Task completed: {task_name}')
            message = template.format(task_name=result.task_name, duration=result.duration)
        elif result.status == TaskStatus.FAILED:
            template = templates.get('task_failed', 'Task failed: {task_name}')
            message = template.format(task_name=result.task_name, error=result.error[:100])
        elif result.status == TaskStatus.TIMEOUT:
            template = templates.get('task_timeout', 'Task timeout: {task_name}')
            message = template.format(task_name=result.task_name, timeout=result.duration)
        else:
            message = f"Task {result.task_name}: {result.status.value}"

        # Send to enabled channels
        channels = notification_config.get('channels', {})

        # Console notification
        if channels.get('console', {}).get('enabled', True):
            if result.status == TaskStatus.COMPLETED:
                logger.info(message)
            else:
                logger.warning(message)

        # Desktop notification
        if channels.get('desktop', {}).get('enabled', False):
            self._send_desktop_notification(message)

    def _send_desktop_notification(self, message: str):
        """Send desktop notification"""
        try:
            import platform
            system = platform.system().lower()

            if system == 'linux':
                os.system(f'notify-send "Background Task" "{message}"')
            elif system == 'darwin':
                os.system(f'osascript -e \'display notification "{message}" with title "Background Task"\'')
            elif system == 'windows':
                # Windows toast notification (requires win10toast package)
                try:
                    from win10toast import ToastNotifier
                    toaster = ToastNotifier()
                    toaster.show_toast("Background Task", message, duration=5)
                except ImportError:
                    logger.debug("win10toast not available for Windows notifications")
        except Exception as e:
            logger.debug(f"Failed to send desktop notification: {e}")

    def get_task_status(self, task_id: str) -> Optional[TaskResult]:
        """Get status of a task"""
        return self.task_results.get(task_id)

    def list_running_tasks(self) -> List[str]:
        """Get list of currently running task IDs"""
        return list(self.running_tasks.keys())

    def stop_task(self, task_id: str) -> bool:
        """
        Stop a running task

        Args:
            task_id: Task ID to stop

        Returns:
            True if task was stopped
        """
        if task_id not in self.running_tasks:
            return False

        process = self.running_tasks[task_id]
        process.terminate()
        process.join(timeout=5)

        if process.is_alive():
            process.kill()
            process.join()

        # Mark as cancelled
        if task_id in self.task_results:
            self.task_results[task_id].status = TaskStatus.CANCELLED

        del self.running_tasks[task_id]
        logger.info(f"Stopped task: {task_id}")
        return True

    def stop_all_tasks(self):
        """Stop all running tasks"""
        task_ids = list(self.running_tasks.keys())
        for task_id in task_ids:
            self.stop_task(task_id)

    def cleanup_old_results(self, days: int = 7):
        """
        Cleanup old task results

        Args:
            days: Number of days to keep
        """
        storage = self.config.get('storage', {})
        results_dir = Path(storage.get('task_results_dir', 'project_archive/background-tasks/results'))

        if not results_dir.exists():
            return

        cutoff_time = time.time() - (days * 24 * 60 * 60)
        cleaned = 0

        for result_file in results_dir.glob('*.json'):
            if result_file.stat().st_mtime < cutoff_time:
                result_file.unlink()
                cleaned += 1

        if cleaned > 0:
            logger.info(f"Cleaned up {cleaned} old task results")


def main():
    """CLI entry point for task runner"""
    import argparse

    parser = argparse.ArgumentParser(description='Background Task Runner')
    parser.add_argument('command', choices=['start', 'stop', 'status', 'list', 'cleanup'])
    parser.add_argument('--task-id', help='Task ID for stop/status commands')
    parser.add_argument('--config', help='Configuration file path')

    args = parser.parse_args()

    runner = BackgroundTaskRunner(config_path=args.config)

    if args.command == 'start':
        logger.info("Background task runner started")
        # Keep running
        try:
            while not runner.shutdown_requested:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Shutting down...")
            runner.stop_all_tasks()

    elif args.command == 'stop':
        if args.task_id:
            success = runner.stop_task(args.task_id)
            print(f"Task {'stopped' if success else 'not found'}")
        else:
            runner.stop_all_tasks()
            print("All tasks stopped")

    elif args.command == 'status':
        if args.task_id:
            result = runner.get_task_status(args.task_id)
            if result:
                print(json.dumps(asdict(result), indent=2, default=str))
            else:
                print("Task not found")
        else:
            print(f"Running tasks: {len(runner.list_running_tasks())}")
            print(f"Completed tasks: {len(runner.task_results)}")

    elif args.command == 'list':
        running = runner.list_running_tasks()
        print(f"Running tasks ({len(running)}):")
        for task_id in running:
            print(f"  - {task_id}")

    elif args.command == 'cleanup':
        runner.cleanup_old_results()
        print("Cleanup completed")


if __name__ == '__main__':
    main()
