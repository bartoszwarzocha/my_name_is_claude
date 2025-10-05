"""
Background Task Management Core Components - My Name Is Claude Framework v3.5.0
"""

from .task_runner import BackgroundTaskRunner, BackgroundTask, TaskStatus, TaskPriority
from .task_queue import TaskQueue, SmartTaskScheduler, QueuedTask
from .task_utils import get_project_root, get_system_resources, generate_task_id, TaskTimer, RateLimiter
from .notifier import NotificationSystem, NotificationEvent, NotificationChannel
from .file_watcher import FileWatcher, TaskTriggerManager, FileEvent
from .git_integration import GitHooksManager, GitTaskMonitor, GitEvent
from .analysis_engine import AnalysisEngine, AnalysisResult, SecurityAnalyzer, PerformanceAnalyzer, CodeAnalyzer

__all__ = [
    'BackgroundTaskRunner',
    'BackgroundTask',
    'TaskStatus',
    'TaskPriority',
    'TaskQueue',
    'SmartTaskScheduler',
    'QueuedTask',
    'get_project_root',
    'get_system_resources',
    'generate_task_id',
    'TaskTimer',
    'RateLimiter',
    'NotificationSystem',
    'NotificationEvent',
    'NotificationChannel',
    'FileWatcher',
    'TaskTriggerManager',
    'FileEvent',
    'GitHooksManager',
    'GitTaskMonitor',
    'GitEvent',
    'AnalysisEngine',
    'AnalysisResult',
    'SecurityAnalyzer',
    'PerformanceAnalyzer',
    'CodeAnalyzer'
]
