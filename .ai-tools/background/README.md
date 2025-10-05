# Background Task Management System

**My Name Is Claude Framework v3.5.0**

Non-blocking background task execution with intelligent scheduling, multi-channel notifications, and comprehensive analysis engines.

## Overview

The Background Task Management System enables automatic execution of long-running tasks without blocking development workflow. It integrates file watching, git hooks, priority-based scheduling, and multi-channel notifications to provide enterprise-grade background task automation.

## Features

### Core Capabilities

- **Non-Blocking Execution** - Tasks run in isolated processes without blocking main workflow
- **Priority-Based Scheduling** - Intelligent queue management with adaptive priority calculation
- **Multi-Channel Notifications** - Console, desktop, file, and email notifications
- **Auto-Triggering** - File watching, git hooks, scheduled tasks, and manual triggers
- **Resource Management** - CPU and memory monitoring with configurable limits
- **State Persistence** - Crash recovery with automatic state restoration
- **Comprehensive Analysis** - Security scanning, performance profiling, code quality analysis

### Task Types

#### Security Scan
- **Tools**: Bandit (Python), npm audit (Node.js), Safety (Python dependencies)
- **Features**: Vulnerability detection, dependency auditing, severity classification
- **Auto-Trigger**: File changes, scheduled intervals
- **Notifications**: Issues and completion

#### Performance Profile
- **Analysis**: Code complexity, file sizes, performance metrics
- **Tools**: Radon (Python complexity), custom analyzers
- **Features**: Complexity scoring, file size analysis, refactoring recommendations
- **Auto-Trigger**: Test runs, manual execution

#### Code Analysis
- **Tools**: Pylint (Python), ESLint (JavaScript/TypeScript)
- **Features**: Code quality checks, style enforcement, best practices validation
- **Auto-Trigger**: Git commits, scheduled intervals
- **Notifications**: High issue counts, critical errors

#### Test Runner
- **Support**: pytest, unittest, npm test, Maven, Gradle
- **Features**: Auto-detection, test execution, result tracking
- **Auto-Trigger**: File changes (debounced), git push
- **Notifications**: Failures only

### Notification Channels

#### Console
- Real-time logging with severity indicators
- Colored output with emoji icons
- Configurable minimum severity

#### Desktop
- Platform-specific notifications (Linux notify-send, macOS osascript, Windows toast)
- Urgency/priority mapping
- Automatic retry on failure

#### File
- JSON-based log rotation
- Configurable retention and size limits
- Structured logging for analysis

#### Email
- HTML and text formats
- SMTP with TLS support
- Severity filtering
- Template-based formatting

## Architecture

```
.ai-tools/background/
├── background_task_manager.py   # Main orchestrator
├── core/
│   ├── task_runner.py          # Task execution engine
│   ├── task_queue.py           # Priority queue and scheduler
│   ├── task_utils.py           # Utility functions
│   ├── notifier.py             # Notification system
│   ├── file_watcher.py         # File system monitoring
│   ├── git_integration.py      # Git hooks integration
│   └── analysis_engine.py      # Analysis engines
└── README.md                   # This file
```

### Component Integration

```
┌─────────────────────────────────────────┐
│   Background Task Manager               │
├─────────────────────────────────────────┤
│  ┌────────────┐  ┌──────────────────┐  │
│  │ File       │  │ Git Hooks        │  │
│  │ Watcher    │  │ Manager          │  │
│  └─────┬──────┘  └────────┬─────────┘  │
│        │                   │             │
│        ├───────┬───────────┤             │
│                ▼                         │
│  ┌─────────────────────────────────┐    │
│  │  Smart Task Scheduler           │    │
│  │  (Priority Queue + Learning)    │    │
│  └───────────┬─────────────────────┘    │
│              ▼                           │
│  ┌─────────────────────────────────┐    │
│  │  Task Runner                    │    │
│  │  (Process Isolation)            │    │
│  └───────────┬─────────────────────┘    │
│              ▼                           │
│  ┌─────────────────────────────────┐    │
│  │  Analysis Engine                │    │
│  │  - Security Scanner             │    │
│  │  - Performance Profiler         │    │
│  │  - Code Analyzer                │    │
│  └───────────┬─────────────────────┘    │
│              ▼                           │
│  ┌─────────────────────────────────┐    │
│  │  Notification System            │    │
│  │  - Console / Desktop            │    │
│  │  - File / Email                 │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

## Configuration

Configuration is managed through `.claude/config/background-tasks.json`:

### Execution Settings

```json
{
  "execution": {
    "max_concurrent_tasks": 5,
    "task_timeout_seconds": 3600,
    "process_isolation": true,
    "max_retries": 3,
    "retry_delay_seconds": 10
  }
}
```

### Resource Limits

```json
{
  "resource_limits": {
    "max_memory_mb": 2048,
    "max_cpu_percent": 50,
    "priority": "low"
  }
}
```

### Task Types

```json
{
  "task_types": {
    "security_scan": {
      "enabled": true,
      "auto_trigger": {
        "on_file_change": true,
        "interval_minutes": 30
      },
      "priority": "high",
      "timeout_seconds": 600,
      "notification_on_complete": true,
      "notification_on_issues": true
    }
  }
}
```

### Triggers

#### File Watching

```json
{
  "triggers": {
    "file_watch": {
      "enabled": true,
      "paths": ["**/*.py", "**/*.js", "**/*.ts"],
      "exclude_paths": ["**/node_modules/**", "**/.venv/**"]
    }
  }
}
```

#### Git Hooks

```json
{
  "triggers": {
    "git_hooks": {
      "enabled": true,
      "pre_commit": ["code_analysis"],
      "post_commit": ["security_scan"],
      "pre_push": ["test_runner", "performance_profile"]
    }
  }
}
```

#### Scheduled Tasks

```json
{
  "triggers": {
    "scheduled": {
      "enabled": true,
      "tasks": [
        {
          "name": "daily_security_scan",
          "task_type": "security_scan",
          "schedule": "0 2 * * *"
        }
      ]
    }
  }
}
```

## Usage

### Starting the Background Task Manager

```bash
# Start in foreground
python .ai-tools/background/background_task_manager.py start

# Check status
python .ai-tools/background/background_task_manager.py status

# Stop manager
python .ai-tools/background/background_task_manager.py stop
```

### Installing Git Hooks

```bash
# Install all configured git hooks
python .ai-tools/background/background_task_manager.py install-hooks

# Check hook status
python .ai-tools/background/git_integration.py status

# Uninstall hooks
python .ai-tools/background/background_task_manager.py uninstall-hooks
```

### Manual Task Execution

#### Run Security Scan

```bash
python .ai-tools/background/core/analysis_engine.py security --output results.json
```

#### Run Performance Profile

```bash
python .ai-tools/background/core/analysis_engine.py performance --output results.json
```

#### Run Code Analysis

```bash
python .ai-tools/background/core/analysis_engine.py code --output results.json
```

#### Run All Analyses

```bash
python .ai-tools/background/core/analysis_engine.py all --output results.json
```

### Testing Components

#### Test File Watcher

```bash
python .ai-tools/background/core/file_watcher.py --config .claude/config/background-tasks.json
```

#### Test Notifications

```bash
python .ai-tools/background/core/notifier.py \
  --severity warning \
  --title "Test Notification" \
  --message "This is a test message"
```

## Task Scheduling

### Priority Levels

```python
TaskPriority.CRITICAL = 1000  # Security issues, critical errors
TaskPriority.HIGH = 100       # Tests, important analysis
TaskPriority.MEDIUM = 10      # Code quality, performance
TaskPriority.LOW = 1          # Documentation, technical debt
```

### Adaptive Scheduling

The Smart Task Scheduler learns from task execution history:

- **Failing Tasks** - Automatically increased priority after repeated failures
- **Quick Tasks** - Slightly reduced priority for efficient queue management
- **Task History** - Maintains last 100 executions per task type
- **Dynamic Adjustment** - Real-time priority calculation based on patterns

### Queue Management

- **Max Queue Size**: 1000 tasks (configurable)
- **Overflow Handling**: Drops lowest-priority tasks when full
- **Duplicate Detection**: Prevents same task from queueing multiple times
- **Queue Time Tracking**: Records time spent in queue for metrics

## Notification System

### Severity Levels

1. **info** - General information, task completion
2. **warning** - Non-critical issues, performance concerns
3. **error** - Task failures, recoverable errors
4. **critical** - Security vulnerabilities, system failures

### Template System

```python
# Using built-in templates
notifier.task_completed(task_name="Security Scan", duration=45.2)
notifier.task_failed(task_name="Test Runner", error="3 tests failed")
notifier.high_resource_usage(resource="CPU", percent=85.5)

# Custom notifications
notifier.notify(
    event_type='custom_event',
    severity='info',
    title='Custom Title',
    message='Custom message',
    metadata={'key': 'value'}
)
```

### Channel Configuration

Each channel can be independently configured with:

- **enabled**: Boolean flag to enable/disable channel
- **min_severity**: Minimum severity level to trigger notifications
- **Platform-specific settings**: Desktop notifications, SMTP configuration, file rotation

## Analysis Engines

### Security Analyzer

**Supported Tools:**
- **Bandit** - Python security scanner
- **npm audit** - Node.js dependency auditor
- **Safety** - Python dependency vulnerability checker

**Detection:**
- Automatically detects available tools
- Runs all applicable scanners
- Aggregates results across tools

**Output:**
- Severity classification (critical, high, medium, low)
- Finding details (file, line, message)
- Fix recommendations
- Summary statistics

### Performance Analyzer

**Metrics:**
- **Cyclomatic Complexity** - Function complexity scoring (Radon)
- **File Size Analysis** - Large file detection
- **Code Metrics** - Lines of code, average file size

**Thresholds:**
- High complexity: >10
- Large file: >1000 lines

**Recommendations:**
- Refactoring suggestions for complex functions
- Module splitting recommendations for large files

### Code Analyzer

**Supported Tools:**
- **Pylint** - Python linter
- **ESLint** - JavaScript/TypeScript linter

**Features:**
- Style enforcement
- Best practices validation
- Error and warning detection

**Output:**
- Issue severity (error, warning, info)
- File and line location
- Rule violations
- Fix suggestions

## File Watching

### Pattern Matching

```json
{
  "paths": [
    "**/*.py",      // All Python files recursively
    "**/*.js",      // All JavaScript files
    "src/**/*.ts"   // TypeScript files in src/
  ],
  "exclude_paths": [
    "**/node_modules/**",
    "**/.venv/**",
    "**/dist/**"
  ]
}
```

### Debouncing

- **Default**: 1 second debounce time
- **Configurable**: Per task type debounce settings
- **Purpose**: Prevents multiple triggers from rapid file changes

### Event Types

- **created** - New file detected
- **modified** - File content changed (hash-based detection)
- **deleted** - File removed

## Git Integration

### Hook Types

- **pre-commit** - Before commit is created
- **post-commit** - After commit is created
- **pre-push** - Before pushing to remote
- **post-merge** - After merge operation

### Installation

Hooks are installed in `.git/hooks/` with automatic backup of existing hooks.

### Hook Execution

```bash
#!/bin/bash
# Auto-generated git hook by My Name Is Claude Framework v3.5.0

# Trigger background tasks
python .ai-tools/background/core/git_integration.py trigger post_commit

# Exit with success (don't block git operations)
exit 0
```

### Safety

- Non-blocking execution (always exits 0)
- Backup creation for existing hooks
- Framework marker for identification
- Restore capability

## Monitoring & Metrics

### Collected Metrics

```json
{
  "metrics": {
    "task_execution_time": true,
    "task_success_rate": true,
    "resource_usage": true,
    "queue_length": true,
    "concurrent_tasks": true
  }
}
```

### Storage

- **Location**: `project_archive/logs/background-tasks-metrics.json`
- **Retention**: 30 days (configurable)
- **Format**: JSON with timestamps

### Task Results

- **Location**: `project_archive/background-tasks/results/`
- **Format**: JSON per task execution
- **Retention**: 7 days (configurable)
- **Auto-cleanup**: On startup and scheduled

## Error Handling

### Retry Logic

```json
{
  "execution": {
    "max_retries": 3,
    "retry_delay_seconds": 10
  }
}
```

### Timeout Handling

- Per-task timeout configuration
- Graceful termination (SIGTERM, then SIGKILL)
- Timeout notification
- Status tracking

### Crash Recovery

- State persistence to JSON
- Automatic restoration on startup
- Task result preservation
- Queue state recovery

## Dependencies

### Required

```bash
pip install psutil         # System resource monitoring
```

### Optional Analysis Tools

```bash
# Python security and quality
pip install bandit safety radon pylint

# JavaScript/TypeScript quality
npm install -g eslint

# Windows desktop notifications
pip install win10toast
```

## Best Practices

### Configuration

1. **Start Conservative** - Begin with lower concurrent task limits
2. **Monitor Resources** - Watch CPU and memory usage initially
3. **Tune Timeouts** - Adjust based on actual task durations
4. **Enable Gradually** - Start with manual triggers, then add auto-triggers

### Task Design

1. **Idempotent Tasks** - Design tasks that can safely retry
2. **Quick Feedback** - Use notifications for long-running tasks
3. **Resource Aware** - Respect system resource limits
4. **Error Handling** - Gracefully handle missing tools/dependencies

### Notification Management

1. **Severity Tuning** - Set appropriate minimum severity levels
2. **Channel Selection** - Use multiple channels for redundancy
3. **Template Customization** - Adapt messages to project needs
4. **Email Sparingly** - Reserve email for critical issues

## Troubleshooting

### Tasks Not Triggering

1. Check configuration: `background-tasks.json` enabled flag
2. Verify file patterns: Match actual project structure
3. Check exclusions: Ensure important files not excluded
4. Review logs: `project_archive/logs/background-tasks.log`

### High Resource Usage

1. Reduce concurrent tasks: Lower `max_concurrent_tasks`
2. Increase timeouts: Prevent premature termination
3. Adjust priority: Set resource-intensive tasks to low priority
4. Check tool efficiency: Profile individual analysis tools

### Notification Issues

1. **Desktop**: Verify platform-specific tools installed
2. **Email**: Check SMTP configuration and credentials
3. **File**: Ensure log directory writable
4. **Console**: Check logging level configuration

### Git Hooks Not Working

1. Verify installation: `background_task_manager.py install-hooks`
2. Check permissions: Hooks must be executable (chmod +x)
3. Review hook status: `git_integration.py status`
4. Check git directory: Ensure `.git/hooks/` exists

## Performance Considerations

### Resource Management

- **Process Isolation** - Each task runs in separate process
- **CPU Limits** - Configurable max CPU percentage
- **Memory Limits** - Maximum memory per task
- **I/O Priority** - Low priority I/O operations

### Optimization Tips

1. **Queue Size** - Balance between memory and task capacity
2. **Check Interval** - File watcher check frequency (default: 2s)
3. **Debounce Time** - File change debouncing (default: 1s)
4. **Cleanup Frequency** - Result cleanup interval (default: 5 minutes)

## Security Considerations

### Safe Execution

- Process isolation prevents cross-contamination
- Non-blocking git hooks don't interfere with commits
- State files use restrictive permissions
- No hardcoded credentials

### Audit Trail

- All task executions logged
- Git hook triggering recorded
- Analysis results archived
- Notification delivery tracked

## Integration Examples

### Custom Task Types

```python
from background_task_manager import BackgroundTaskManager
from core.task_runner import BackgroundTask

manager = BackgroundTaskManager()

# Define custom task
custom_task = BackgroundTask(
    task_id="custom_123",
    name="Custom Analysis",
    task_type="custom",
    priority="medium",
    timeout=600,
    command=["python", "custom_analyzer.py"]
)

# Submit task
manager.task_runner.submit_task(custom_task)
```

### Custom Analyzers

```python
from core.analysis_engine import BaseAnalyzer, AnalysisResult

class CustomAnalyzer(BaseAnalyzer):
    def analyze(self) -> AnalysisResult:
        result = AnalysisResult(
            analysis_type='custom',
            status='success'
        )

        # Your analysis logic here

        return result
```

### Custom Notifications

```python
from core.notifier import NotificationChannel, NotificationEvent

class SlackChannel(NotificationChannel):
    def send(self, event: NotificationEvent) -> bool:
        # Slack integration logic
        pass
```

## Future Enhancements

- Distributed task execution across multiple machines
- Web-based dashboard for monitoring
- Advanced scheduling with cron expressions
- Machine learning for priority optimization
- Plugin system for custom analyzers
- Real-time WebSocket notifications
- Docker container support
- Kubernetes integration

## Support

For issues, questions, or contributions:

1. Check existing documentation
2. Review configuration examples
3. Examine log files
4. Consult framework guidelines in `CLAUDE.md`

---

**My Name Is Claude Framework v3.5.0**
Background Task Management System
© 2025 Bartosz Warzocha & My Name Is Claude Team
