#!/usr/bin/env python3
"""
Git Integration - My Name Is Claude Framework v3.5.0

Git hooks integration for automatic task triggering.

This is a TEMPLATE implementation. Actual implementation should:
1. Adapt to project git workflow
2. Integrate with existing git hooks
3. Follow project-specific git conventions
"""

import os
import sys
import json
import subprocess
import logging
from pathlib import Path
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass, field
from datetime import datetime

logger = logging.getLogger(__name__)


@dataclass
class GitEvent:
    """Git event data"""
    event_type: str  # pre-commit, post-commit, pre-push, post-merge
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    commit_hash: Optional[str] = None
    commit_message: Optional[str] = None
    changed_files: List[str] = field(default_factory=list)
    branch: Optional[str] = None
    metadata: Dict = field(default_factory=dict)


class GitHooksManager:
    """
    Manager for git hooks integration
    """

    def __init__(
        self,
        config: Dict,
        task_scheduler: Optional[Callable[[str, Dict], None]] = None
    ):
        """
        Initialize git hooks manager

        Args:
            config: Git hooks configuration
            task_scheduler: Callback to schedule tasks
        """
        self.config = config
        self.enabled = config.get('enabled', True)
        self.task_scheduler = task_scheduler
        self.hooks_config = {
            'pre_commit': config.get('pre_commit', []),
            'post_commit': config.get('post_commit', []),
            'pre_push': config.get('pre_push', []),
            'post_merge': config.get('post_merge', [])
        }
        self.git_dir = self._find_git_dir()

    def _find_git_dir(self) -> Optional[Path]:
        """Find .git directory"""
        current_dir = Path.cwd()
        while current_dir != current_dir.parent:
            git_dir = current_dir / '.git'
            if git_dir.exists():
                return git_dir
            current_dir = current_dir.parent
        return None

    def install_hooks(self) -> bool:
        """
        Install git hooks

        Returns:
            True if hooks installed successfully
        """
        if not self.enabled:
            logger.info("Git hooks integration is disabled")
            return False

        if not self.git_dir:
            logger.error("Git directory not found")
            return False

        hooks_dir = self.git_dir / 'hooks'
        hooks_dir.mkdir(exist_ok=True)

        # Install each hook
        hooks_to_install = ['pre-commit', 'post-commit', 'pre-push', 'post-merge']
        installed = 0

        for hook_name in hooks_to_install:
            if self._install_hook(hooks_dir, hook_name):
                installed += 1

        logger.info(f"Installed {installed}/{len(hooks_to_install)} git hooks")
        return installed > 0

    def _install_hook(self, hooks_dir: Path, hook_name: str) -> bool:
        """Install a specific git hook"""
        hook_file = hooks_dir / hook_name
        hook_config_name = hook_name.replace('-', '_')

        # Check if tasks configured for this hook
        if not self.hooks_config.get(hook_config_name):
            logger.debug(f"No tasks configured for {hook_name}, skipping")
            return False

        # Create hook script
        hook_script = self._generate_hook_script(hook_name, hook_config_name)

        try:
            # Check if hook already exists
            if hook_file.exists():
                # Backup existing hook
                backup_file = hooks_dir / f"{hook_name}.backup"
                hook_file.rename(backup_file)
                logger.info(f"Backed up existing {hook_name} hook")

            # Write new hook
            with open(hook_file, 'w') as f:
                f.write(hook_script)

            # Make executable
            hook_file.chmod(0o755)

            logger.info(f"Installed {hook_name} hook")
            return True
        except Exception as e:
            logger.error(f"Failed to install {hook_name} hook: {e}")
            return False

    def _generate_hook_script(self, hook_name: str, hook_config_name: str) -> str:
        """Generate hook script content"""
        # Get Python interpreter path
        python_path = sys.executable

        # Get this script path
        script_path = Path(__file__).resolve()

        hook_script = f"""#!/bin/bash
# Auto-generated git hook by My Name Is Claude Framework v3.5.0
# This hook triggers background tasks defined in .claude/config/background-tasks.json

# Hook: {hook_name}
# Generated: {datetime.now().isoformat()}

# Trigger background tasks
{python_path} {script_path} trigger {hook_config_name} "$@"

# Exit with success (don't block git operations)
exit 0
"""
        return hook_script

    def uninstall_hooks(self) -> bool:
        """
        Uninstall git hooks

        Returns:
            True if hooks uninstalled successfully
        """
        if not self.git_dir:
            logger.error("Git directory not found")
            return False

        hooks_dir = self.git_dir / 'hooks'
        if not hooks_dir.exists():
            return True

        hooks_to_remove = ['pre-commit', 'post-commit', 'pre-push', 'post-merge']
        removed = 0

        for hook_name in hooks_to_remove:
            hook_file = hooks_dir / hook_name

            if hook_file.exists():
                try:
                    # Check if it's our hook (contains our marker)
                    with open(hook_file, 'r') as f:
                        content = f.read()

                    if 'My Name Is Claude Framework' in content:
                        # Restore backup if exists
                        backup_file = hooks_dir / f"{hook_name}.backup"
                        if backup_file.exists():
                            hook_file.unlink()
                            backup_file.rename(hook_file)
                            logger.info(f"Restored backup for {hook_name}")
                        else:
                            hook_file.unlink()
                            logger.info(f"Removed {hook_name} hook")
                        removed += 1
                except Exception as e:
                    logger.error(f"Failed to remove {hook_name} hook: {e}")

        logger.info(f"Uninstalled {removed}/{len(hooks_to_remove)} git hooks")
        return removed > 0

    def trigger_hook(self, hook_type: str, args: List[str] = None) -> bool:
        """
        Trigger hook manually

        Args:
            hook_type: Type of hook (pre_commit, post_commit, etc.)
            args: Hook arguments

        Returns:
            True if hook triggered successfully
        """
        if not self.enabled:
            return False

        args = args or []

        # Get git information
        event = self._create_git_event(hook_type, args)

        # Get tasks to trigger
        tasks_to_trigger = self.hooks_config.get(hook_type, [])

        if not tasks_to_trigger:
            logger.debug(f"No tasks configured for {hook_type}")
            return True

        # Trigger each task
        logger.info(f"Git hook {hook_type}: triggering {len(tasks_to_trigger)} tasks")

        for task_type in tasks_to_trigger:
            self._trigger_task(task_type, event)

        return True

    def _create_git_event(self, hook_type: str, args: List[str]) -> GitEvent:
        """Create git event from hook execution"""
        event = GitEvent(event_type=hook_type)

        try:
            # Get current branch
            event.branch = self._run_git_command(['rev-parse', '--abbrev-ref', 'HEAD'])

            # Get last commit info (if exists)
            if hook_type in ['post_commit', 'post_merge']:
                event.commit_hash = self._run_git_command(['rev-parse', 'HEAD'])
                event.commit_message = self._run_git_command(['log', '-1', '--pretty=%B'])

            # Get changed files
            if hook_type == 'pre_commit':
                # Staged files
                files_output = self._run_git_command(['diff', '--cached', '--name-only'])
            elif hook_type in ['post_commit', 'post_merge']:
                # Files in last commit
                files_output = self._run_git_command(['diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD'])
            else:
                files_output = ""

            if files_output:
                event.changed_files = [f.strip() for f in files_output.split('\n') if f.strip()]

            # Store hook arguments
            event.metadata['hook_args'] = args

        except Exception as e:
            logger.error(f"Failed to get git information: {e}")

        return event

    def _run_git_command(self, args: List[str]) -> str:
        """Run git command and return output"""
        try:
            result = subprocess.run(
                ['git'] + args,
                capture_output=True,
                text=True,
                check=True,
                timeout=10
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            logger.debug(f"Git command failed: {e}")
            return ""
        except subprocess.TimeoutExpired:
            logger.error("Git command timed out")
            return ""

    def _trigger_task(self, task_type: str, event: GitEvent):
        """Trigger a task"""
        if not self.task_scheduler:
            logger.warning(f"No task scheduler configured, cannot trigger {task_type}")
            return

        logger.info(f"Triggering task: {task_type} (git hook: {event.event_type})")

        try:
            task_data = {
                'trigger_type': 'git_hook',
                'git_event': {
                    'event_type': event.event_type,
                    'branch': event.branch,
                    'commit_hash': event.commit_hash,
                    'commit_message': event.commit_message,
                    'changed_files': event.changed_files,
                    'timestamp': event.timestamp
                }
            }
            self.task_scheduler(task_type, task_data)
        except Exception as e:
            logger.error(f"Failed to trigger task {task_type}: {e}")

    def get_hook_status(self) -> Dict[str, bool]:
        """Get status of installed hooks"""
        status = {}

        if not self.git_dir:
            return status

        hooks_dir = self.git_dir / 'hooks'
        if not hooks_dir.exists():
            return status

        for hook_name in ['pre-commit', 'post-commit', 'pre-push', 'post-merge']:
            hook_file = hooks_dir / hook_name
            installed = False

            if hook_file.exists():
                try:
                    with open(hook_file, 'r') as f:
                        content = f.read()
                    installed = 'My Name Is Claude Framework' in content
                except:
                    pass

            status[hook_name] = installed

        return status


class GitTaskMonitor:
    """
    Monitor git repository for task-relevant events
    """

    def __init__(self, config: Dict):
        """
        Initialize git task monitor

        Args:
            config: Monitor configuration
        """
        self.config = config
        self.git_dir = self._find_git_dir()

    def _find_git_dir(self) -> Optional[Path]:
        """Find .git directory"""
        current_dir = Path.cwd()
        while current_dir != current_dir.parent:
            git_dir = current_dir / '.git'
            if git_dir.exists():
                return git_dir
            current_dir = current_dir.parent
        return None

    def get_recent_commits(self, count: int = 10) -> List[Dict]:
        """Get recent commits"""
        if not self.git_dir:
            return []

        try:
            result = subprocess.run(
                ['git', 'log', f'-{count}', '--pretty=format:%H|%an|%ae|%at|%s'],
                capture_output=True,
                text=True,
                check=True,
                timeout=10
            )

            commits = []
            for line in result.stdout.strip().split('\n'):
                if not line:
                    continue

                parts = line.split('|', 4)
                if len(parts) == 5:
                    commits.append({
                        'hash': parts[0],
                        'author_name': parts[1],
                        'author_email': parts[2],
                        'timestamp': int(parts[3]),
                        'message': parts[4]
                    })

            return commits
        except Exception as e:
            logger.error(f"Failed to get recent commits: {e}")
            return []

    def get_changed_files_since(self, since_hash: str) -> List[str]:
        """Get files changed since a specific commit"""
        if not self.git_dir:
            return []

        try:
            result = subprocess.run(
                ['git', 'diff', '--name-only', since_hash, 'HEAD'],
                capture_output=True,
                text=True,
                check=True,
                timeout=10
            )

            return [f.strip() for f in result.stdout.strip().split('\n') if f.strip()]
        except Exception as e:
            logger.error(f"Failed to get changed files: {e}")
            return []

    def get_current_branch(self) -> Optional[str]:
        """Get current branch name"""
        if not self.git_dir:
            return None

        try:
            result = subprocess.run(
                ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                capture_output=True,
                text=True,
                check=True,
                timeout=5
            )
            return result.stdout.strip()
        except Exception as e:
            logger.error(f"Failed to get current branch: {e}")
            return None

    def is_repo_clean(self) -> bool:
        """Check if repository is clean (no uncommitted changes)"""
        if not self.git_dir:
            return True

        try:
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                capture_output=True,
                text=True,
                check=True,
                timeout=5
            )
            return len(result.stdout.strip()) == 0
        except Exception as e:
            logger.error(f"Failed to check repo status: {e}")
            return False


def main():
    """CLI for git hooks management"""
    import argparse

    parser = argparse.ArgumentParser(description='Git Hooks Manager')
    parser.add_argument('command', choices=['install', 'uninstall', 'status', 'trigger'])
    parser.add_argument('hook_type', nargs='?', help='Hook type for trigger command')
    parser.add_argument('--config', help='Configuration file path')

    args = parser.parse_args()

    # Load config
    if args.config and Path(args.config).exists():
        with open(args.config, 'r') as f:
            config = json.load(f).get('triggers', {}).get('git_hooks', {})
    else:
        config = {
            'enabled': True,
            'pre_commit': [],
            'post_commit': [],
            'pre_push': []
        }

    # Create manager
    manager = GitHooksManager(config)

    if args.command == 'install':
        success = manager.install_hooks()
        print(f"Hooks {'installed' if success else 'installation failed'}")

    elif args.command == 'uninstall':
        success = manager.uninstall_hooks()
        print(f"Hooks {'uninstalled' if success else 'uninstall failed'}")

    elif args.command == 'status':
        status = manager.get_hook_status()
        print("Git hooks status:")
        for hook_name, installed in status.items():
            status_str = "✓ installed" if installed else "✗ not installed"
            print(f"  {hook_name}: {status_str}")

    elif args.command == 'trigger':
        if not args.hook_type:
            print("Error: hook_type required for trigger command")
            sys.exit(1)

        success = manager.trigger_hook(args.hook_type, sys.argv[3:])
        print(f"Hook {'triggered' if success else 'trigger failed'}")


if __name__ == '__main__':
    main()
