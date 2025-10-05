#!/usr/bin/env python3
"""
Task Utilities - My Name Is Claude Framework v3.5.0

Common utilities for background task management.
"""

import os
import sys
import json
import hashlib
import psutil
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def get_project_root() -> Path:
    """Get project root directory"""
    current_dir = Path.cwd()
    markers = ['.git', '.claude', 'CLAUDE.md']

    while current_dir != current_dir.parent:
        for marker in markers:
            if (current_dir / marker).exists():
                return current_dir
        current_dir = current_dir.parent

    return Path.cwd()


def ensure_directory(path: str) -> Path:
    """
    Ensure directory exists

    Args:
        path: Directory path

    Returns:
        Path object
    """
    dir_path = Path(path)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def get_system_resources() -> Dict[str, Any]:
    """
    Get current system resource usage

    Returns:
        Dictionary with resource information
    """
    try:
        return {
            'cpu_percent': psutil.cpu_percent(interval=1),
            'memory_percent': psutil.virtual_memory().percent,
            'memory_available_mb': psutil.virtual_memory().available / (1024 * 1024),
            'disk_percent': psutil.disk_usage('/').percent,
            'process_count': len(psutil.pids())
        }
    except Exception as e:
        logger.error(f"Failed to get system resources: {e}")
        return {}


def check_resource_availability(
    max_cpu_percent: float = 80.0,
    max_memory_percent: float = 80.0
) -> bool:
    """
    Check if system has enough resources

    Args:
        max_cpu_percent: Maximum CPU usage
        max_memory_percent: Maximum memory usage

    Returns:
        True if resources available
    """
    try:
        resources = get_system_resources()
        return (
            resources.get('cpu_percent', 0) < max_cpu_percent and
            resources.get('memory_percent', 0) < max_memory_percent
        )
    except:
        return True  # Assume available if check fails


def generate_task_id(task_type: str, unique_data: str = "") -> str:
    """
    Generate unique task ID

    Args:
        task_type: Type of task
        unique_data: Additional unique data

    Returns:
        Task ID
    """
    timestamp = datetime.now().isoformat()
    data = f"{task_type}:{timestamp}:{unique_data}"
    hash_digest = hashlib.md5(data.encode()).hexdigest()[:8]
    return f"{task_type}_{hash_digest}"


def format_duration(seconds: float) -> str:
    """Format duration in human-readable format"""
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
    """Format file size in human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_count < 1024.0:
            return f"{bytes_count:.1f} {unit}"
        bytes_count /= 1024.0
    return f"{bytes_count:.1f} PB"


def load_json_file(file_path: str) -> Optional[Dict]:
    """Load JSON file"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load JSON file {file_path}: {e}")
        return None


def save_json_file(file_path: str, data: Dict, indent: int = 2) -> bool:
    """Save JSON file"""
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w') as f:
            json.dump(data, f, indent=indent)
        return True
    except Exception as e:
        logger.error(f"Failed to save JSON file {file_path}: {e}")
        return False


def get_file_hash(file_path: str, algorithm: str = 'md5') -> Optional[str]:
    """Calculate file hash"""
    try:
        hash_func = hashlib.new(algorithm)
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        logger.error(f"Failed to calculate hash for {file_path}: {e}")
        return None


class TaskTimer:
    """Context manager for timing task execution"""

    def __init__(self, task_name: str):
        self.task_name = task_name
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = datetime.now()
        logger.info(f"Starting {self.task_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = datetime.now()
        duration = (self.end_time - self.start_time).total_seconds()

        if exc_type is None:
            logger.info(f"✅ {self.task_name} completed in {format_duration(duration)}")
        else:
            logger.error(f"❌ {self.task_name} failed after {format_duration(duration)}: {exc_val}")

        return False

    @property
    def duration(self) -> float:
        """Get duration in seconds"""
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return 0.0


class RateLimiter:
    """Simple rate limiter for task execution"""

    def __init__(self, max_calls: int, time_window: int):
        """
        Initialize rate limiter

        Args:
            max_calls: Maximum calls allowed
            time_window: Time window in seconds
        """
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls: List[float] = []

    def allow(self) -> bool:
        """
        Check if call is allowed

        Returns:
            True if call is within rate limit
        """
        now = datetime.now().timestamp()

        # Remove old calls outside time window
        self.calls = [t for t in self.calls if now - t < self.time_window]

        # Check if under limit
        if len(self.calls) < self.max_calls:
            self.calls.append(now)
            return True

        return False

    def wait_time(self) -> float:
        """
        Get time to wait until next call is allowed

        Returns:
            Seconds to wait
        """
        if not self.calls:
            return 0.0

        now = datetime.now().timestamp()
        oldest_call = min(self.calls)
        wait = self.time_window - (now - oldest_call)

        return max(0.0, wait)
