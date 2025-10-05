#!/usr/bin/env python3
"""
Background Task Manager - My Name Is Claude Framework v3.5.0

Main orchestrator for background task management system.

Integrates:
- Task execution engine (task_runner.py)
- Priority queue management (task_queue.py)
- Notification system (notifier.py)
- File watching (file_watcher.py)
- Git hooks (git_integration.py)
- Analysis engine (analysis_engine.py)
"""

import os
import sys
import json
import time
import logging
import signal
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

# Add core directory to path
sys.path.insert(0, str(Path(__file__).parent / 'core'))

from task_runner import BackgroundTaskRunner, BackgroundTask, TaskPriority
from task_queue import TaskQueue, SmartTaskScheduler
from task_utils import get_project_root, generate_task_id
from notifier import NotificationSystem
from file_watcher import TaskTriggerManager
from git_integration import GitHooksManager
from analysis_engine import AnalysisEngine

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(name)s] %(message)s'
)
logger = logging.getLogger(__name__)


class BackgroundTaskManager:
    """
    Main background task management system

    Coordinates all background task components:
    - Task execution and scheduling
    - File watching and git hooks
    - Notifications
    - Analysis engines
    """

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize background task manager

        Args:
            config_path: Path to configuration file
        """
        self.config_path = config_path or self._get_default_config_path()
        self.config = self._load_config()
        self.running = False

        # Initialize components
        logger.info("Initializing Background Task Manager v3.5.0...")

        # Task execution
        self.task_runner = BackgroundTaskRunner(self.config_path)
        self.task_queue = TaskQueue(max_size=1000)
        self.task_scheduler = SmartTaskScheduler(self.task_queue)

        # Notifications
        notification_config = self.config.get('notification_system', {})
        self.notifier = NotificationSystem(notification_config)

        # Analysis engines
        self.analysis_engine = AnalysisEngine(self.config)

        # Triggers
        triggers_config = self.config.get('triggers', {})

        # File watcher
        self.trigger_manager = TaskTriggerManager(
            config=self.config,
            task_scheduler=self._schedule_triggered_task
        )

        # Git hooks
        git_hooks_config = triggers_config.get('git_hooks', {})
        self.git_hooks_manager = GitHooksManager(
            config=git_hooks_config,
            task_scheduler=self._schedule_triggered_task
        )

        # Setup signal handlers
        signal.signal(signal.SIGINT, self._handle_shutdown)
        signal.signal(signal.SIGTERM, self._handle_shutdown)

        logger.info("Background Task Manager initialized")

    def _get_default_config_path(self) -> str:
        """Get default configuration path"""
        project_root = get_project_root()
        return str(project_root / '.claude' / 'config' / 'background-tasks.json')

    def _load_config(self) -> Dict:
        """Load configuration file"""
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            return {'enabled': False}

    def start(self):
        """Start background task manager"""
        if not self.config.get('enabled', True):
            logger.warning("Background tasks disabled in configuration")
            return

        if self.running:
            logger.warning("Background task manager already running")
            return

        self.running = True
        logger.info("Starting background task manager...")

        # Start trigger manager (file watcher)
        self.trigger_manager.start()

        # Notify startup
        self.notifier.notify(
            event_type='system_startup',
            severity='info',
            title='Background Task Manager Started',
            message='Background task manager is now running'
        )

        # Main loop
        try:
            while self.running:
                self._process_tasks()
                time.sleep(1)
        except Exception as e:
            logger.error(f"Error in main loop: {e}")
            self.stop()

    def stop(self):
        """Stop background task manager"""
        if not self.running:
            return

        logger.info("Stopping background task manager...")
        self.running = False

        # Stop components
        self.trigger_manager.stop()
        self.task_runner.stop_all_tasks()

        # Notify shutdown
        self.notifier.notify(
            event_type='system_shutdown',
            severity='info',
            title='Background Task Manager Stopped',
            message='Background task manager has been stopped'
        )

        logger.info("Background task manager stopped")

    def _handle_shutdown(self, signum, frame):
        """Handle shutdown signals"""
        logger.info(f"Received signal {signum}, shutting down...")
        self.stop()
        sys.exit(0)

    def _process_tasks(self):
        """Process tasks from queue"""
        # Get next task from queue
        task_data = self.task_scheduler.get_next_task()

        if not task_data:
            return

        # Create and submit task
        task_type = task_data.get('task_type', '')
        task_id = task_data.get('task_id', '')

        logger.info(f"Processing task: {task_type} ({task_id})")

        # Execute based on task type
        if task_type == 'security_scan':
            self._execute_security_scan(task_id, task_data)
        elif task_type == 'performance_profile':
            self._execute_performance_profile(task_id, task_data)
        elif task_type == 'code_analysis':
            self._execute_code_analysis(task_id, task_data)
        elif task_type == 'test_runner':
            self._execute_test_runner(task_id, task_data)
        else:
            logger.warning(f"Unknown task type: {task_type}")

    def _schedule_triggered_task(self, task_type: str, trigger_data: Dict):
        """Schedule a task triggered by file change or git hook"""
        task_id = generate_task_id(task_type, str(datetime.now().timestamp()))

        # Get task configuration
        task_config = self.config.get('task_types', {}).get(task_type, {})

        if not task_config.get('enabled', False):
            logger.debug(f"Task type {task_type} is disabled")
            return

        # Get priority
        priority_map = {
            'critical': TaskPriority.CRITICAL.value,
            'high': TaskPriority.HIGH.value,
            'medium': TaskPriority.MEDIUM.value,
            'low': TaskPriority.LOW.value
        }
        priority = priority_map.get(task_config.get('priority', 'medium'), TaskPriority.MEDIUM.value)

        # Schedule task
        task_data = {
            **trigger_data,
            'task_type': task_type,
            'config': task_config
        }

        success = self.task_scheduler.schedule_task(
            task_id=task_id,
            task_type=task_type,
            task_data=task_data,
            base_priority=priority
        )

        if success:
            logger.info(f"Scheduled task: {task_type} (ID: {task_id}, priority: {priority})")

            # Notify if configured
            if task_config.get('notification_on_start', False):
                self.notifier.task_started(task_type, task_id)
        else:
            logger.warning(f"Failed to schedule task: {task_type}")

    def _execute_security_scan(self, task_id: str, task_data: Dict):
        """Execute security scan task"""
        start_time = time.time()

        try:
            # Run security analysis
            result = self.analysis_engine.run_analysis('security_scan')

            if result:
                duration = time.time() - start_time

                # Notify based on result
                task_config = task_data.get('config', {})

                if result.status == 'success' and task_config.get('notification_on_complete', False):
                    self.notifier.task_completed('Security Scan', duration)
                elif result.status in ['warning', 'error'] and task_config.get('notification_on_issues', True):
                    self.notifier.task_failed('Security Scan', result.summary)

                # Record completion
                self.task_scheduler.record_task_completion('security_scan', duration, result.status == 'success')

                # Save result
                self._save_analysis_result(task_id, result)
        except Exception as e:
            logger.error(f"Security scan failed: {e}")
            self.notifier.task_failed('Security Scan', str(e))
            self.task_scheduler.record_task_completion('security_scan', time.time() - start_time, False)

    def _execute_performance_profile(self, task_id: str, task_data: Dict):
        """Execute performance profiling task"""
        start_time = time.time()

        try:
            # Run performance analysis
            result = self.analysis_engine.run_analysis('performance_profile')

            if result:
                duration = time.time() - start_time

                # Notify based on result
                task_config = task_data.get('config', {})

                if result.status == 'success' and task_config.get('notification_on_complete', False):
                    self.notifier.task_completed('Performance Profile', duration)
                elif result.status in ['warning', 'error'] and task_config.get('notification_on_issues', True):
                    self.notifier.task_failed('Performance Profile', result.summary)

                # Record completion
                self.task_scheduler.record_task_completion('performance_profile', duration, result.status == 'success')

                # Save result
                self._save_analysis_result(task_id, result)
        except Exception as e:
            logger.error(f"Performance profiling failed: {e}")
            self.notifier.task_failed('Performance Profile', str(e))
            self.task_scheduler.record_task_completion('performance_profile', time.time() - start_time, False)

    def _execute_code_analysis(self, task_id: str, task_data: Dict):
        """Execute code analysis task"""
        start_time = time.time()

        try:
            # Run code analysis
            result = self.analysis_engine.run_analysis('code_analysis')

            if result:
                duration = time.time() - start_time

                # Notify based on result
                task_config = task_data.get('config', {})

                if result.status == 'success' and task_config.get('notification_on_complete', False):
                    self.notifier.task_completed('Code Analysis', duration)
                elif result.status in ['warning', 'error'] and task_config.get('notification_on_issues', True):
                    self.notifier.task_failed('Code Analysis', result.summary)

                # Record completion
                self.task_scheduler.record_task_completion('code_analysis', duration, result.status == 'success')

                # Save result
                self._save_analysis_result(task_id, result)
        except Exception as e:
            logger.error(f"Code analysis failed: {e}")
            self.notifier.task_failed('Code Analysis', str(e))
            self.task_scheduler.record_task_completion('code_analysis', time.time() - start_time, False)

    def _execute_test_runner(self, task_id: str, task_data: Dict):
        """Execute test runner task"""
        start_time = time.time()

        try:
            # Detect and run tests
            test_command = self._detect_test_command()

            if not test_command:
                logger.warning("No test command detected")
                return

            # Create background task
            task = BackgroundTask(
                task_id=task_id,
                name='Test Runner',
                task_type='test_runner',
                priority='high',
                timeout=task_data.get('config', {}).get('timeout_seconds', 1200),
                command=test_command
            )

            # Submit task
            self.task_runner.submit_task(task)

            # Wait for completion (simplified - should use async)
            time.sleep(2)

            # Get result
            result = self.task_runner.get_task_status(task_id)

            if result:
                duration = time.time() - start_time

                # Notify based on result
                task_config = task_data.get('config', {})

                if result.exit_code == 0 and task_config.get('notification_on_complete', False):
                    self.notifier.task_completed('Test Runner', duration)
                elif result.exit_code != 0 and task_config.get('notification_on_issues', True):
                    self.notifier.task_failed('Test Runner', result.error or 'Tests failed')

                # Record completion
                self.task_scheduler.record_task_completion('test_runner', duration, result.exit_code == 0)
        except Exception as e:
            logger.error(f"Test runner failed: {e}")
            self.notifier.task_failed('Test Runner', str(e))
            self.task_scheduler.record_task_completion('test_runner', time.time() - start_time, False)

    def _detect_test_command(self) -> Optional[List[str]]:
        """Detect test command based on project type"""
        project_root = get_project_root()

        # Python: pytest or unittest
        if (project_root / 'pytest.ini').exists() or (project_root / 'setup.py').exists():
            return ['pytest']
        elif (project_root / 'tests').exists():
            return ['python', '-m', 'unittest', 'discover']

        # Node.js: npm test
        if (project_root / 'package.json').exists():
            return ['npm', 'test']

        # Java: Maven or Gradle
        if (project_root / 'pom.xml').exists():
            return ['mvn', 'test']
        elif (project_root / 'build.gradle').exists():
            return ['gradle', 'test']

        return None

    def _save_analysis_result(self, task_id: str, result):
        """Save analysis result to file"""
        try:
            storage_config = self.config.get('storage', {})
            results_dir = Path(storage_config.get('task_results_dir', 'project_archive/background-tasks/results'))
            results_dir.mkdir(parents=True, exist_ok=True)

            result_file = results_dir / f"{task_id}.json"

            from dataclasses import asdict
            result_dict = asdict(result)

            with open(result_file, 'w') as f:
                json.dump(result_dict, f, indent=2)

            logger.debug(f"Saved analysis result: {result_file}")
        except Exception as e:
            logger.error(f"Failed to save analysis result: {e}")

    def install_git_hooks(self) -> bool:
        """Install git hooks"""
        return self.git_hooks_manager.install_hooks()

    def uninstall_git_hooks(self) -> bool:
        """Uninstall git hooks"""
        return self.git_hooks_manager.uninstall_hooks()

    def get_status(self) -> Dict:
        """Get system status"""
        return {
            'running': self.running,
            'queue': self.task_scheduler.get_queue_info(),
            'git_hooks': self.git_hooks_manager.get_hook_status(),
            'enabled': self.config.get('enabled', True)
        }


def main():
    """CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Background Task Manager v3.5.0')
    parser.add_argument('command', choices=['start', 'stop', 'status', 'install-hooks', 'uninstall-hooks'])
    parser.add_argument('--config', help='Configuration file path')
    parser.add_argument('--daemon', action='store_true', help='Run as daemon')

    args = parser.parse_args()

    # Create manager
    manager = BackgroundTaskManager(config_path=args.config)

    if args.command == 'start':
        if args.daemon:
            # TODO: Implement daemon mode
            logger.warning("Daemon mode not yet implemented")
        else:
            manager.start()

    elif args.command == 'stop':
        manager.stop()

    elif args.command == 'status':
        status = manager.get_status()
        print(json.dumps(status, indent=2))

    elif args.command == 'install-hooks':
        success = manager.install_git_hooks()
        print(f"Git hooks {'installed' if success else 'installation failed'}")

    elif args.command == 'uninstall-hooks':
        success = manager.uninstall_git_hooks()
        print(f"Git hooks {'uninstalled' if success else 'uninstall failed'}")


if __name__ == '__main__':
    main()
