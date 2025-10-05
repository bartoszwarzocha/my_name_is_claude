#!/usr/bin/env python3
"""
File Watcher - My Name Is Claude Framework v3.5.0

File system monitoring for automatic task triggering.

This is a TEMPLATE implementation. Actual implementation should:
1. Adapt to project file structure
2. Integrate with existing build/watch systems
3. Follow project-specific file monitoring patterns
"""

import os
import sys
import time
import logging
import threading
from pathlib import Path
from typing import Dict, List, Set, Callable, Optional
from dataclasses import dataclass, field
from datetime import datetime
import fnmatch
import hashlib

logger = logging.getLogger(__name__)


@dataclass
class FileEvent:
    """File system event"""
    event_type: str  # created, modified, deleted
    file_path: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    file_hash: Optional[str] = None


class FileWatcher:
    """
    File system watcher for automatic task triggering
    """

    def __init__(
        self,
        config: Dict,
        on_file_change: Optional[Callable[[FileEvent], None]] = None
    ):
        """
        Initialize file watcher

        Args:
            config: File watcher configuration
            on_file_change: Callback for file change events
        """
        self.config = config
        self.enabled = config.get('enabled', True)
        self.watch_paths = config.get('paths', [])
        self.exclude_paths = config.get('exclude_paths', [])
        self.on_file_change = on_file_change

        # Internal state
        self.file_hashes: Dict[str, str] = {}
        self.running = False
        self.watch_thread: Optional[threading.Thread] = None
        self.check_interval = 2  # seconds

        # Debouncing
        self.pending_events: Dict[str, FileEvent] = {}
        self.debounce_time = 1.0  # seconds

    def start(self):
        """Start watching files"""
        if not self.enabled:
            logger.info("File watcher is disabled")
            return

        if self.running:
            logger.warning("File watcher already running")
            return

        self.running = True
        self.watch_thread = threading.Thread(target=self._watch_loop, daemon=True)
        self.watch_thread.start()
        logger.info(f"File watcher started (monitoring {len(self.watch_paths)} patterns)")

    def stop(self):
        """Stop watching files"""
        if not self.running:
            return

        self.running = False
        if self.watch_thread:
            self.watch_thread.join(timeout=5)
        logger.info("File watcher stopped")

    def _watch_loop(self):
        """Main watch loop"""
        # Initial scan to build file hashes
        self._scan_files()

        while self.running:
            try:
                # Check for file changes
                self._check_changes()

                # Process pending events (debouncing)
                self._process_pending_events()

                # Sleep
                time.sleep(self.check_interval)
            except Exception as e:
                logger.error(f"Error in watch loop: {e}")
                time.sleep(5)

    def _scan_files(self):
        """Scan all matching files and compute hashes"""
        logger.info("Scanning files for initial state...")

        project_root = self._get_project_root()
        matched_files = set()

        # Find all matching files
        for pattern in self.watch_paths:
            for file_path in self._find_matching_files(project_root, pattern):
                if not self._is_excluded(file_path):
                    matched_files.add(file_path)

        # Compute hashes
        for file_path in matched_files:
            try:
                file_hash = self._compute_file_hash(file_path)
                self.file_hashes[str(file_path)] = file_hash
            except Exception as e:
                logger.debug(f"Failed to hash {file_path}: {e}")

        logger.info(f"Initial scan complete: {len(self.file_hashes)} files tracked")

    def _check_changes(self):
        """Check for file changes"""
        project_root = self._get_project_root()
        current_files = set()

        # Find current matching files
        for pattern in self.watch_paths:
            for file_path in self._find_matching_files(project_root, pattern):
                if not self._is_excluded(file_path):
                    current_files.add(str(file_path))

        # Check for new or modified files
        for file_path in current_files:
            try:
                file_hash = self._compute_file_hash(file_path)

                if file_path not in self.file_hashes:
                    # New file
                    self._queue_event(FileEvent(
                        event_type='created',
                        file_path=file_path,
                        file_hash=file_hash
                    ))
                    self.file_hashes[file_path] = file_hash
                elif self.file_hashes[file_path] != file_hash:
                    # Modified file
                    self._queue_event(FileEvent(
                        event_type='modified',
                        file_path=file_path,
                        file_hash=file_hash
                    ))
                    self.file_hashes[file_path] = file_hash
            except Exception as e:
                logger.debug(f"Failed to check {file_path}: {e}")

        # Check for deleted files
        for file_path in list(self.file_hashes.keys()):
            if file_path not in current_files:
                self._queue_event(FileEvent(
                    event_type='deleted',
                    file_path=file_path
                ))
                del self.file_hashes[file_path]

    def _queue_event(self, event: FileEvent):
        """Queue event for debouncing"""
        self.pending_events[event.file_path] = event
        logger.debug(f"Queued event: {event.event_type} {event.file_path}")

    def _process_pending_events(self):
        """Process pending events after debounce time"""
        now = time.time()

        for file_path, event in list(self.pending_events.items()):
            event_time = datetime.fromisoformat(event.timestamp).timestamp()
            if now - event_time >= self.debounce_time:
                # Process event
                if self.on_file_change:
                    try:
                        self.on_file_change(event)
                        logger.info(f"File {event.event_type}: {event.file_path}")
                    except Exception as e:
                        logger.error(f"Error processing file event: {e}")

                # Remove from pending
                del self.pending_events[file_path]

    def _find_matching_files(self, root: Path, pattern: str) -> List[str]:
        """Find files matching pattern"""
        matches = []

        # Handle glob patterns
        if '**' in pattern:
            # Recursive pattern
            parts = pattern.split('/')
            for file_path in root.rglob(parts[-1]):
                if file_path.is_file():
                    rel_path = str(file_path.relative_to(root))
                    if fnmatch.fnmatch(rel_path, pattern):
                        matches.append(str(file_path))
        else:
            # Non-recursive pattern
            for file_path in root.glob(pattern):
                if file_path.is_file():
                    matches.append(str(file_path))

        return matches

    def _is_excluded(self, file_path: str) -> bool:
        """Check if file path is excluded"""
        for exclude_pattern in self.exclude_paths:
            if fnmatch.fnmatch(file_path, exclude_pattern):
                return True

            # Also check if any parent directory matches
            path_parts = Path(file_path).parts
            for i in range(len(path_parts)):
                partial_path = str(Path(*path_parts[:i + 1]))
                if fnmatch.fnmatch(partial_path, exclude_pattern):
                    return True

        return False

    def _compute_file_hash(self, file_path: str) -> str:
        """Compute MD5 hash of file"""
        hash_md5 = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def _get_project_root(self) -> Path:
        """Get project root directory"""
        current_dir = Path.cwd()
        markers = ['.git', '.claude', 'CLAUDE.md']

        while current_dir != current_dir.parent:
            for marker in markers:
                if (current_dir / marker).exists():
                    return current_dir
            current_dir = current_dir.parent

        return Path.cwd()


class TaskTriggerManager:
    """
    Manages automatic task triggering based on file changes
    """

    def __init__(
        self,
        config: Dict,
        task_scheduler: Optional[Callable[[str, Dict], None]] = None
    ):
        """
        Initialize task trigger manager

        Args:
            config: Trigger configuration
            task_scheduler: Callback to schedule tasks
        """
        self.config = config
        self.task_scheduler = task_scheduler
        self.file_watcher: Optional[FileWatcher] = None
        self.task_types = config.get('task_types', {})

        # Debounce tracking
        self.last_trigger_times: Dict[str, float] = {}

    def start(self):
        """Start trigger manager"""
        # Initialize file watcher if enabled
        file_watch_config = self.config.get('file_watch', {})
        if file_watch_config.get('enabled', False):
            self.file_watcher = FileWatcher(
                config=file_watch_config,
                on_file_change=self._handle_file_change
            )
            self.file_watcher.start()
            logger.info("Task trigger manager started")

    def stop(self):
        """Stop trigger manager"""
        if self.file_watcher:
            self.file_watcher.stop()
        logger.info("Task trigger manager stopped")

    def _handle_file_change(self, event: FileEvent):
        """Handle file change event"""
        logger.debug(f"Processing file change: {event.event_type} {event.file_path}")

        # Check which tasks should be triggered
        for task_type, task_config in self.task_types.items():
            if not task_config.get('enabled', True):
                continue

            auto_trigger = task_config.get('auto_trigger', {})

            # Check if this task should trigger on file changes
            if auto_trigger.get('on_file_change', False):
                # Check debounce
                debounce_seconds = auto_trigger.get('debounce_seconds', 0)
                if self._should_trigger(task_type, debounce_seconds):
                    self._trigger_task(task_type, {
                        'trigger_type': 'file_change',
                        'file_event': {
                            'event_type': event.event_type,
                            'file_path': event.file_path,
                            'timestamp': event.timestamp
                        }
                    })

    def _should_trigger(self, task_type: str, debounce_seconds: float) -> bool:
        """Check if task should be triggered (debouncing)"""
        if debounce_seconds == 0:
            return True

        now = time.time()
        last_trigger = self.last_trigger_times.get(task_type, 0)

        if now - last_trigger >= debounce_seconds:
            self.last_trigger_times[task_type] = now
            return True

        return False

    def _trigger_task(self, task_type: str, trigger_data: Dict):
        """Trigger a task"""
        if not self.task_scheduler:
            logger.warning(f"No task scheduler configured, cannot trigger {task_type}")
            return

        logger.info(f"Triggering task: {task_type}")

        try:
            self.task_scheduler(task_type, trigger_data)
        except Exception as e:
            logger.error(f"Failed to trigger task {task_type}: {e}")

    def trigger_on_commit(self, commit_hash: str, commit_message: str):
        """Trigger tasks on git commit"""
        for task_type, task_config in self.task_types.items():
            if not task_config.get('enabled', True):
                continue

            auto_trigger = task_config.get('auto_trigger', {})
            if auto_trigger.get('on_commit', False):
                self._trigger_task(task_type, {
                    'trigger_type': 'git_commit',
                    'commit_hash': commit_hash,
                    'commit_message': commit_message
                })

    def trigger_on_test_run(self, test_results: Dict):
        """Trigger tasks on test run"""
        for task_type, task_config in self.task_types.items():
            if not task_config.get('enabled', True):
                continue

            auto_trigger = task_config.get('auto_trigger', {})
            if auto_trigger.get('on_test_run', False):
                self._trigger_task(task_type, {
                    'trigger_type': 'test_run',
                    'test_results': test_results
                })

    def trigger_on_package_change(self, package_file: str):
        """Trigger tasks on package file change"""
        for task_type, task_config in self.task_types.items():
            if not task_config.get('enabled', True):
                continue

            auto_trigger = task_config.get('auto_trigger', {})
            if auto_trigger.get('on_package_change', False):
                self._trigger_task(task_type, {
                    'trigger_type': 'package_change',
                    'package_file': package_file
                })


def main():
    """CLI for file watcher testing"""
    import argparse

    parser = argparse.ArgumentParser(description='File Watcher Test')
    parser.add_argument('--config', help='Configuration file path')

    args = parser.parse_args()

    # Load config
    if args.config and Path(args.config).exists():
        import json
        with open(args.config, 'r') as f:
            config = json.load(f).get('triggers', {}).get('file_watch', {})
    else:
        config = {
            'enabled': True,
            'paths': ['**/*.py', '**/*.js'],
            'exclude_paths': ['**/node_modules/**', '**/.venv/**']
        }

    # Create file watcher
    def on_change(event: FileEvent):
        print(f"[{event.timestamp}] {event.event_type.upper()}: {event.file_path}")

    watcher = FileWatcher(config, on_file_change=on_change)
    watcher.start()

    print("File watcher running. Press Ctrl+C to stop...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping file watcher...")
        watcher.stop()


if __name__ == '__main__':
    main()
