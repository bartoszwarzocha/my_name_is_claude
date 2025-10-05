#!/usr/bin/env python3
"""
Hook Utilities - My Name Is Claude Framework v3.4.0

Common utilities and helper functions for hook development and execution.

This is a TEMPLATE implementation. Actual implementation should:
1. Adapt to project conventions
2. Integrate with existing utility libraries
3. Follow project-specific patterns
"""

import os
import sys
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any, Callable
from functools import wraps
import time

logger = logging.getLogger(__name__)


class HookContext:
    """Context manager for hook execution"""

    def __init__(self, hook_name: str, context_data: Optional[Dict] = None):
        """
        Initialize hook context

        Args:
            hook_name: Name of the hook
            context_data: Additional context data
        """
        self.hook_name = hook_name
        self.context_data = context_data or {}
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        """Enter context"""
        self.start_time = time.time()
        logger.info(f"Starting hook: {self.hook_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context"""
        self.end_time = time.time()
        duration = self.end_time - self.start_time

        if exc_type is None:
            logger.info(f"✅ Hook {self.hook_name} completed in {duration:.2f}s")
        else:
            logger.error(f"❌ Hook {self.hook_name} failed after {duration:.2f}s: {exc_val}")

        return False  # Don't suppress exceptions


def timed_execution(func: Callable) -> Callable:
    """
    Decorator to measure execution time

    Args:
        func: Function to time

    Returns:
        Wrapped function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
            duration = time.time() - start
            logger.info(f"⏱️  {func.__name__} completed in {duration:.2f}s")
            return result
        except Exception as e:
            duration = time.time() - start
            logger.error(f"❌ {func.__name__} failed after {duration:.2f}s: {e}")
            raise
    return wrapper


def retry_on_failure(max_retries: int = 3, delay: float = 1.0) -> Callable:
    """
    Decorator to retry function on failure

    Args:
        max_retries: Maximum number of retries
        delay: Delay between retries in seconds

    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_retries:
                        logger.warning(
                            f"Attempt {attempt + 1}/{max_retries} failed for {func.__name__}: {e}"
                        )
                        time.sleep(delay)
                    else:
                        logger.error(
                            f"All {max_retries} retries failed for {func.__name__}: {e}"
                        )

            raise last_exception

        return wrapper
    return decorator


def get_hook_context() -> Dict[str, Any]:
    """
    Get hook execution context from environment

    Returns:
        Dictionary with context data
    """
    context_json = os.environ.get('HOOK_CONTEXT', '{}')
    try:
        return json.loads(context_json)
    except json.JSONDecodeError:
        logger.warning("Failed to parse HOOK_CONTEXT, returning empty context")
        return {}


def set_hook_result(success: bool, message: str = "", data: Optional[Dict] = None):
    """
    Set hook execution result

    Args:
        success: Whether hook succeeded
        message: Result message
        data: Additional result data
    """
    result = {
        'success': success,
        'message': message,
        'data': data or {}
    }

    # Write to stdout for hook engine to capture
    print(json.dumps(result))

    # Exit with appropriate code
    sys.exit(0 if success else 1)


def get_project_root() -> Path:
    """
    Find project root directory

    Returns:
        Path to project root
    """
    current_dir = Path.cwd()

    # Look for markers of project root
    markers = ['.git', '.claude', 'CLAUDE.md', 'pyproject.toml', 'package.json']

    while current_dir != current_dir.parent:
        for marker in markers:
            if (current_dir / marker).exists():
                return current_dir
        current_dir = current_dir.parent

    # Default to current directory
    return Path.cwd()


def get_hooks_directory() -> Path:
    """
    Get hooks directory path

    Returns:
        Path to hooks directory
    """
    return get_project_root() / '.claude' / 'hooks'


def load_hook_config(config_name: str) -> Dict:
    """
    Load hook configuration file

    Args:
        config_name: Name of config file (without .json)

    Returns:
        Configuration dictionary
    """
    config_path = get_hooks_directory() / 'config' / f'{config_name}.json'

    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load config {config_name}: {e}")
        return {}


def run_command(command: List[str], timeout: int = 60, capture_output: bool = True) -> Dict:
    """
    Run shell command

    Args:
        command: Command and arguments as list
        timeout: Command timeout in seconds
        capture_output: Whether to capture stdout/stderr

    Returns:
        Dictionary with command results
    """
    import subprocess

    try:
        result = subprocess.run(
            command,
            capture_output=capture_output,
            text=True,
            timeout=timeout
        )

        return {
            'success': result.returncode == 0,
            'exit_code': result.returncode,
            'stdout': result.stdout if capture_output else '',
            'stderr': result.stderr if capture_output else ''
        }
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'exit_code': -1,
            'error': f'Command timed out after {timeout}s'
        }
    except Exception as e:
        return {
            'success': False,
            'exit_code': -1,
            'error': str(e)
        }


def check_file_exists(file_path: str, required: bool = True) -> bool:
    """
    Check if file exists

    Args:
        file_path: Path to file
        required: Whether file is required

    Returns:
        True if file exists

    Raises:
        FileNotFoundError: If file doesn't exist and required=True
    """
    path = Path(file_path)
    exists = path.exists()

    if not exists and required:
        raise FileNotFoundError(f"Required file not found: {file_path}")

    return exists


def ensure_directory(directory: str):
    """
    Ensure directory exists

    Args:
        directory: Directory path
    """
    Path(directory).mkdir(parents=True, exist_ok=True)


def read_file(file_path: str) -> str:
    """
    Read file contents

    Args:
        file_path: Path to file

    Returns:
        File contents as string
    """
    with open(file_path, 'r') as f:
        return f.read()


def write_file(file_path: str, content: str):
    """
    Write content to file

    Args:
        file_path: Path to file
        content: Content to write
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, 'w') as f:
        f.write(content)


def append_to_file(file_path: str, content: str):
    """
    Append content to file

    Args:
        file_path: Path to file
        content: Content to append
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, 'a') as f:
        f.write(content)


def load_json(file_path: str) -> Dict:
    """
    Load JSON file

    Args:
        file_path: Path to JSON file

    Returns:
        Parsed JSON data
    """
    with open(file_path, 'r') as f:
        return json.load(f)


def save_json(file_path: str, data: Dict, indent: int = 2):
    """
    Save data to JSON file

    Args:
        file_path: Path to JSON file
        data: Data to save
        indent: JSON indentation
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, 'w') as f:
        json.dump(data, f, indent=indent)


def format_duration(seconds: float) -> str:
    """
    Format duration in human-readable format

    Args:
        seconds: Duration in seconds

    Returns:
        Formatted duration string
    """
    if seconds < 1:
        return f"{seconds * 1000:.0f}ms"
    elif seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        secs = seconds % 60
        return f"{minutes}m {secs:.0f}s"
    else:
        hours = int(seconds / 3600)
        minutes = int((seconds % 3600) / 60)
        return f"{hours}h {minutes}m"


def format_size(bytes_count: int) -> str:
    """
    Format file size in human-readable format

    Args:
        bytes_count: Size in bytes

    Returns:
        Formatted size string
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_count < 1024.0:
            return f"{bytes_count:.1f} {unit}"
        bytes_count /= 1024.0
    return f"{bytes_count:.1f} PB"


def get_git_info() -> Dict:
    """
    Get Git repository information

    Returns:
        Dictionary with Git info
    """
    info = {
        'is_git_repo': False,
        'branch': None,
        'commit': None,
        'dirty': False
    }

    try:
        # Check if git repo
        result = run_command(['git', 'rev-parse', '--git-dir'], capture_output=True)
        if result['success']:
            info['is_git_repo'] = True

            # Get branch
            result = run_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True)
            if result['success']:
                info['branch'] = result['stdout'].strip()

            # Get commit
            result = run_command(['git', 'rev-parse', 'HEAD'], capture_output=True)
            if result['success']:
                info['commit'] = result['stdout'].strip()[:8]

            # Check if dirty
            result = run_command(['git', 'status', '--porcelain'], capture_output=True)
            if result['success']:
                info['dirty'] = len(result['stdout'].strip()) > 0

    except Exception as e:
        logger.debug(f"Failed to get Git info: {e}")

    return info


def notify(message: str, level: str = "info"):
    """
    Send notification

    Args:
        message: Notification message
        level: Notification level (info, warning, error)
    """
    # Log to console
    if level == "error":
        logger.error(message)
    elif level == "warning":
        logger.warning(message)
    else:
        logger.info(message)

    # Additional notification channels can be added here
    # (e.g., Slack, email, desktop notification)


class HookLogger:
    """Specialized logger for hooks"""

    def __init__(self, hook_name: str):
        """
        Initialize hook logger

        Args:
            hook_name: Name of the hook
        """
        self.hook_name = hook_name
        self.logger = logging.getLogger(f"hook.{hook_name}")

    def info(self, message: str):
        """Log info message"""
        self.logger.info(f"[{self.hook_name}] {message}")

    def warning(self, message: str):
        """Log warning message"""
        self.logger.warning(f"[{self.hook_name}] {message}")

    def error(self, message: str):
        """Log error message"""
        self.logger.error(f"[{self.hook_name}] {message}")

    def debug(self, message: str):
        """Log debug message"""
        self.logger.debug(f"[{self.hook_name}] {message}")


# Example hook template
HOOK_TEMPLATE = '''#!/usr/bin/env python3
"""
{hook_name} - My Name Is Claude Framework v3.4.0

{description}

META: priority: {priority}
META: timeout: {timeout}
META: category: {category}
"""

import sys
from pathlib import Path

# Add hooks utils to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'core'))

from hook_utils import HookContext, HookLogger, get_hook_context, set_hook_result


def main():
    """Main hook execution"""
    logger = HookLogger("{hook_name}")
    context = get_hook_context()

    with HookContext("{hook_name}", context):
        try:
            # Hook implementation here
            logger.info("Executing {hook_name}")

            # TODO: Implement hook logic

            # Success
            set_hook_result(
                success=True,
                message="{hook_name} completed successfully"
            )

        except Exception as e:
            logger.error(f"Hook failed: {{e}}")
            set_hook_result(
                success=False,
                message=f"{hook_name} failed: {{e}}"
            )


if __name__ == '__main__':
    main()
'''


def generate_hook_template(
    hook_name: str,
    category: str,
    description: str = "",
    priority: str = "medium",
    timeout: int = 60
) -> str:
    """
    Generate hook template code

    Args:
        hook_name: Name of the hook
        category: Hook category
        description: Hook description
        priority: Hook priority
        timeout: Hook timeout

    Returns:
        Generated hook code
    """
    return HOOK_TEMPLATE.format(
        hook_name=hook_name,
        category=category,
        description=description or f"Hook: {hook_name}",
        priority=priority,
        timeout=timeout
    )
