# Background Task Management System

**My Name Is Claude Framework v3.5.0**

## Overview

The Background Task Management System enables automatic execution of long-running tasks without blocking your development workflow. It provides enterprise-grade infrastructure for security scanning, performance profiling, code analysis, and automated testing with intelligent scheduling and multi-channel notifications.

## Why Background Tasks?

**Problem:** Long-running analysis tasks (security scans, performance profiling, comprehensive testing) block your development workflow and interrupt productivity.

**Solution:** Background Task Management System runs these tasks in isolated processes with intelligent scheduling, automatic triggering, and comprehensive notifications - allowing you to continue developing while tasks execute in the background.

## Key Features

### 🎯 Core Capabilities

- **Non-Blocking Execution** - Tasks run in isolated processes without blocking main workflow
- **Intelligent Scheduling** - Priority-based queue with adaptive learning from task history
- **Multi-Channel Notifications** - Console, desktop, file, and email alerts
- **Auto-Triggering** - File watching, git hooks, scheduled tasks, manual execution
- **Enterprise Reliability** - State persistence, crash recovery, resource monitoring

### 📊 Built-In Analysis Engines

#### Security Scanner
Automatically scans your codebase for security vulnerabilities using multiple tools:
- **Bandit** - Python security scanner
- **npm audit** - Node.js dependency vulnerabilities
- **Safety** - Python dependency vulnerability checker

**Features:**
- Automatic tool detection and execution
- Severity classification (critical, high, medium, low)
- Aggregated findings across all tools
- Fix recommendations

#### Performance Profiler
Analyzes code performance and quality metrics:
- **Cyclomatic Complexity** - Function complexity scoring with Radon
- **File Size Analysis** - Large file detection and recommendations
- **Code Metrics** - Lines of code, average file size, complexity trends

**Features:**
- High complexity threshold detection (>10)
- Refactoring recommendations for complex functions
- Module splitting suggestions for large files

#### Code Quality Analyzer
Enforces code quality standards and best practices:
- **Pylint** - Python linter and code quality checker
- **ESLint** - JavaScript/TypeScript quality analyzer

**Features:**
- Style enforcement and best practices validation
- Error and warning classification
- Fix suggestions and recommendations

#### Test Runner
Automatically executes your test suite:
- **Framework Detection** - pytest, unittest, npm test, Maven, Gradle
- **Auto-Execution** - Runs tests after code changes (with debouncing)
- **Result Tracking** - Stores test results for analysis

### 🔔 Notification System

**Four notification channels** with independent configuration:

#### Console Notifications
- Real-time logging with severity indicators
- Colored output with emoji icons (✅ ⚠️ ❌ 🚨)
- Configurable minimum severity level

#### Desktop Notifications
- **Linux** - notify-send with urgency levels
- **macOS** - osascript display notification
- **Windows** - Toast notifications

#### File Logging
- JSON-based structured logging
- Automatic log rotation (configurable size and file count)
- 7-day retention by default

#### Email Notifications
- HTML and plain text formats
- SMTP with TLS support
- Template-based messaging
- Severity filtering

### 🔍 Auto-Triggering System

#### File Watching
Monitor specific files and automatically trigger tasks on changes:
```json
{
  "paths": ["**/*.py", "**/*.js", "**/*.ts"],
  "exclude_paths": ["**/node_modules/**", "**/.venv/**"]
}
```

**Features:**
- Glob pattern matching
- Hash-based change detection (MD5)
- Debouncing (1s default) to prevent rapid re-triggers
- Event types: created, modified, deleted

#### Git Hooks Integration
Automatically trigger tasks at specific points in your git workflow:
- **pre-commit** - Before commit creation (code analysis)
- **post-commit** - After commit creation (security scan)
- **pre-push** - Before pushing to remote (test runner, performance profile)
- **post-merge** - After merge operations

**Features:**
- Automatic installation and uninstallation
- Existing hook backup and restoration
- Non-blocking execution (always exits 0)
- Changed files detection per commit

#### Scheduled Tasks
Run tasks at specific times using cron expressions:
```json
{
  "tasks": [
    {
      "name": "daily_security_scan",
      "task_type": "security_scan",
      "schedule": "0 2 * * *"
    }
  ]
}
```

## Getting Started

### Installation

Background Task Management System is included with My Name Is Claude v3.5.0. No additional installation required.

**Optional analysis tools:**
```bash
# Python analysis tools
pip install bandit safety radon pylint

# JavaScript/TypeScript analysis
npm install -g eslint

# Windows desktop notifications
pip install win10toast
```

### Configuration

All configuration is managed through `.claude/config/background-tasks.json`.

**Key configuration sections:**

#### Execution Settings
```json
{
  "execution": {
    "max_concurrent_tasks": 5,
    "task_timeout_seconds": 3600,
    "process_isolation": true,
    "max_retries": 3
  }
}
```

#### Resource Limits
```json
{
  "resource_limits": {
    "max_memory_mb": 2048,
    "max_cpu_percent": 50,
    "priority": "low"
  }
}
```

#### Task Types
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
      "notification_on_complete": true,
      "notification_on_issues": true
    }
  }
}
```

### Basic Usage

#### Start Background Task Manager
```bash
python .ai-tools/background/background_task_manager.py start
```

#### Install Git Hooks
```bash
python .ai-tools/background/background_task_manager.py install-hooks
```

#### Run Manual Analysis
```bash
# Security scan
python .ai-tools/background/core/analysis_engine.py security --output results.json

# Performance profile
python .ai-tools/background/core/analysis_engine.py performance --output results.json

# Code analysis
python .ai-tools/background/core/analysis_engine.py code --output results.json

# All analyses
python .ai-tools/background/core/analysis_engine.py all --output results.json
```

#### Check System Status
```bash
python .ai-tools/background/background_task_manager.py status
```

## Task Types

### security_scan
**Purpose:** Scan codebase for security vulnerabilities

**Triggers:**
- File changes (configurable patterns)
- Scheduled intervals (default: 30 minutes)
- Manual execution

**Tools Used:**
- Bandit (Python)
- npm audit (Node.js)
- Safety (Python dependencies)

**Configuration:**
```json
{
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
```

### performance_profile
**Purpose:** Analyze code performance and complexity

**Triggers:**
- Test runs
- Manual execution

**Analysis:**
- Cyclomatic complexity (Radon)
- File size metrics
- Code quality indicators

**Configuration:**
```json
{
  "performance_profile": {
    "enabled": true,
    "auto_trigger": {
      "on_test_run": true
    },
    "priority": "medium",
    "timeout_seconds": 1800,
    "notification_on_complete": true,
    "notification_on_issues": true
  }
}
```

### code_analysis
**Purpose:** Enforce code quality standards

**Triggers:**
- Git commits
- Scheduled intervals (default: 60 minutes)

**Tools Used:**
- Pylint (Python)
- ESLint (JavaScript/TypeScript)

**Configuration:**
```json
{
  "code_analysis": {
    "enabled": true,
    "auto_trigger": {
      "on_commit": true,
      "interval_minutes": 60
    },
    "priority": "low",
    "timeout_seconds": 900,
    "notification_on_complete": false,
    "notification_on_issues": true
  }
}
```

### test_runner
**Purpose:** Execute automated test suite

**Triggers:**
- File changes (with 10s debounce)
- Git push (pre-push hook)

**Supported Frameworks:**
- pytest, unittest (Python)
- npm test (Node.js)
- Maven test, Gradle test (Java)

**Configuration:**
```json
{
  "test_runner": {
    "enabled": true,
    "auto_trigger": {
      "on_file_change": true,
      "debounce_seconds": 10
    },
    "priority": "high",
    "timeout_seconds": 1200,
    "notification_on_complete": false,
    "notification_on_issues": true
  }
}
```

## Advanced Features

### Smart Task Scheduling

The scheduler learns from task execution history to optimize priorities:

**Adaptive Priority Calculation:**
- Automatically boosts priority for frequently failing tasks
- Reduces priority for quick-completing tasks
- Maintains last 100 executions per task type
- Real-time adjustment based on patterns

**Priority Levels:**
```python
TaskPriority.CRITICAL = 1000  # Security issues, critical errors
TaskPriority.HIGH = 100       # Tests, important analysis
TaskPriority.MEDIUM = 10      # Code quality, performance
TaskPriority.LOW = 1          # Documentation, technical debt
```

### Resource Management

**CPU and Memory Limits:**
```json
{
  "resource_limits": {
    "max_memory_mb": 2048,
    "max_cpu_percent": 50,
    "priority": "low"
  }
}
```

**Resource Monitoring:**
- Real-time CPU and memory tracking
- Task execution resource consumption
- Automatic throttling when limits approached

### State Persistence

**Crash Recovery:**
- Automatic state save every task completion
- State restoration on manager restart
- Task result preservation
- Queue state recovery

**Storage:**
- Task results: `project_archive/background-tasks/results/`
- Task state: `project_archive/background-tasks/state.json`
- Logs: `project_archive/logs/background-tasks.log`

**Retention:**
- Results: 7 days (configurable)
- Logs: 10MB per file, 5 files max
- Automatic cleanup on startup

## Workflow Examples

### Example 1: Continuous Security Monitoring

**Scenario:** Automatically scan for security vulnerabilities during development

**Setup:**
1. Enable security_scan in configuration
2. Configure file watching for source files
3. Set notification preferences

**Configuration:**
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
      "notification_on_issues": true
    }
  },
  "triggers": {
    "file_watch": {
      "enabled": true,
      "paths": ["**/*.py", "**/*.js"],
      "exclude_paths": ["**/node_modules/**", "**/.venv/**"]
    }
  }
}
```

**Result:**
- Security scans run automatically when you modify source files
- Desktop notifications for critical/high severity issues
- Continuous monitoring without workflow interruption

### Example 2: Pre-Commit Quality Gates

**Scenario:** Ensure code quality before committing

**Setup:**
1. Install git hooks
2. Configure code_analysis for pre-commit
3. Set appropriate timeouts

**Configuration:**
```json
{
  "triggers": {
    "git_hooks": {
      "enabled": true,
      "pre_commit": ["code_analysis"],
      "post_commit": ["security_scan"]
    }
  }
}
```

**Installation:**
```bash
python .ai-tools/background/background_task_manager.py install-hooks
```

**Result:**
- Code analysis runs before each commit
- Security scan runs after commit completes
- Non-blocking (commits never blocked)
- Notifications for issues found

### Example 3: Automated Testing Pipeline

**Scenario:** Run tests automatically after code changes

**Setup:**
1. Enable test_runner with debouncing
2. Configure desktop notifications for failures

**Configuration:**
```json
{
  "task_types": {
    "test_runner": {
      "enabled": true,
      "auto_trigger": {
        "on_file_change": true,
        "debounce_seconds": 10
      },
      "priority": "high",
      "notification_on_issues": true
    }
  }
}
```

**Result:**
- Tests run 10 seconds after last file change
- Prevents rapid re-execution during active coding
- Desktop notifications for test failures
- Background execution doesn't interrupt development

## Troubleshooting

### Tasks Not Triggering

**Problem:** Auto-triggers not working

**Solutions:**
1. Check configuration enabled flag:
   ```json
   {"enabled": true}
   ```

2. Verify file patterns match your project:
   ```bash
   ls -la **/*.py  # Check if files match patterns
   ```

3. Review exclusion patterns:
   ```json
   {"exclude_paths": ["**/node_modules/**"]}
   ```

4. Check logs:
   ```bash
   tail -f project_archive/logs/background-tasks.log
   ```

### High Resource Usage

**Problem:** Background tasks consuming too much CPU/memory

**Solutions:**
1. Reduce concurrent tasks:
   ```json
   {"max_concurrent_tasks": 3}
   ```

2. Increase timeouts to prevent premature termination:
   ```json
   {"task_timeout_seconds": 7200}
   ```

3. Adjust resource limits:
   ```json
   {
     "max_memory_mb": 1024,
     "max_cpu_percent": 30
   }
   ```

### Notification Issues

**Problem:** Not receiving notifications

**Desktop Notifications:**
- Linux: Install `libnotify-bin` package
- macOS: Ensure Terminal has notification permissions
- Windows: Install `pip install win10toast`

**Email Notifications:**
1. Verify SMTP configuration:
   ```json
   {
     "smtp_server": "smtp.gmail.com",
     "smtp_port": 587,
     "from_email": "your-email@gmail.com"
   }
   ```

2. Check credentials (use environment variables)
3. Test SMTP connection manually

### Git Hooks Not Working

**Problem:** Git hooks not executing tasks

**Solutions:**
1. Verify installation:
   ```bash
   python .ai-tools/background/background_task_manager.py install-hooks
   ```

2. Check hook permissions:
   ```bash
   chmod +x .git/hooks/pre-commit
   ```

3. Review hook status:
   ```bash
   ls -la .git/hooks/
   ```

4. Check hook configuration:
   ```json
   {
     "git_hooks": {
       "enabled": true,
       "pre_commit": ["code_analysis"]
     }
   }
   ```

## Best Practices

### Configuration

1. **Start Conservative** - Begin with lower concurrent task limits and increase as needed
2. **Monitor Resources** - Watch CPU and memory usage initially to tune limits
3. **Tune Timeouts** - Adjust based on actual task durations in your environment
4. **Enable Gradually** - Start with manual triggers, then add auto-triggers

### Task Design

1. **Idempotent Tasks** - Design tasks that can safely retry without side effects
2. **Quick Feedback** - Use notifications for long-running tasks
3. **Resource Aware** - Respect system resource limits and priorities
4. **Error Handling** - Gracefully handle missing tools or dependencies

### Notification Management

1. **Severity Tuning** - Set appropriate minimum severity levels per channel
2. **Channel Selection** - Use multiple channels for redundancy
3. **Template Customization** - Adapt notification messages to your project needs
4. **Email Sparingly** - Reserve email notifications for critical issues only

### Performance Optimization

1. **Queue Size** - Balance between memory usage and task capacity
2. **Check Interval** - Tune file watcher check frequency (default: 2s)
3. **Debounce Time** - Adjust file change debouncing based on typing speed
4. **Cleanup Frequency** - Configure result retention to manage disk usage

## Integration with Framework

### Integration Points

**Framework Configuration:**
- Reads `.claude/config/background-tasks.json`
- Auto-detects project root via `.git`, `.claude`, `CLAUDE.md`

**Analysis Tools:**
- Integrates Bandit, Safety, Radon, Pylint, ESLint, npm audit
- Auto-detects installed tools and adapts

**Test Frameworks:**
- Supports pytest, unittest, npm test, Maven, Gradle
- Framework detection and auto-configuration

**Notification Platforms:**
- Platform-specific implementations (Linux, macOS, Windows)
- Graceful degradation when tools unavailable

### Workflow Integration

**Session Management:**
- Compatible with framework session management
- State preserved across sessions

**TodoWrite Integration:**
- Task execution can trigger TodoWrite updates
- Progress tracking through framework

**MCP Tools:**
- Can be integrated with Serena and Context7
- Future enhancement opportunity

## Additional Resources

- **Full Technical Documentation** - `.ai-tools/background/README.md`
- **Source Code** - `.ai-tools/background/`
- **Configuration Template** - `.claude/config/background-tasks.json`
- **CHANGELOG** - Version history and release notes
- **FRAMEWORK_ROADMAP** - Future enhancements

## Summary

Background Task Management System provides enterprise-grade infrastructure for running long-running analysis tasks without interrupting your development workflow. With intelligent scheduling, multi-channel notifications, comprehensive analysis engines, and auto-triggering capabilities, it ensures continuous code quality, security, and performance monitoring while you focus on development.

**Key Benefits:**
- ✅ Non-blocking workflow - develop while tasks run
- ✅ Automatic quality checks - continuous security, performance, code analysis
- ✅ Intelligent prioritization - critical tasks execute first
- ✅ Comprehensive notifications - never miss important issues
- ✅ Enterprise reliability - process isolation, crash recovery, state persistence
- ✅ Flexible integration - file watching, git hooks, scheduled tasks, manual execution

For detailed configuration options and advanced usage, see `.ai-tools/background/README.md`.
