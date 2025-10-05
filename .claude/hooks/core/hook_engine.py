#!/usr/bin/env python3
"""
Hook Execution Engine - My Name Is Claude Framework v3.4.0

Core engine for executing hooks with priority-based scheduling, parallel execution,
error handling, and performance monitoring.

This is a TEMPLATE implementation. Actual implementation should:
1. Detect Python environment and dependencies
2. Adapt to project structure
3. Integrate with existing logging/monitoring systems
4. Follow project-specific error handling patterns
"""

import os
import sys
import json
import time
import subprocess
import multiprocessing
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('project_archive/logs/hooks-execution.log')
    ]
)
logger = logging.getLogger(__name__)


class HookPriority(Enum):
    """Hook execution priority levels"""
    CRITICAL = 1000
    HIGH = 100
    MEDIUM = 10
    LOW = 1


class HookStatus(Enum):
    """Hook execution status"""
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    TIMEOUT = "timeout"
    SKIPPED = "skipped"


@dataclass
class HookResult:
    """Result of hook execution"""
    hook_name: str
    status: HookStatus
    execution_time: float
    output: str = ""
    error: str = ""
    exit_code: int = 0
    retries: int = 0


@dataclass
class Hook:
    """Hook definition"""
    name: str
    path: str
    priority: str
    timeout: int
    category: str = ""
    enabled: bool = True
    retry_count: int = 3
    retry_delay: int = 5


class HookEngine:
    """
    Core hook execution engine with priority scheduling and parallel execution
    """

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize hook engine

        Args:
            config_path: Path to hooks configuration directory
        """
        self.config_path = config_path or self._get_default_config_path()
        self.hooks_dir = Path(self.config_path).parent
        self.config = self._load_config()
        self.agent_hooks = self._load_agent_hooks()
        self.quality_gates = self._load_quality_gates()
        self.monitoring_config = self._load_monitoring_config()

    def _get_default_config_path(self) -> str:
        """Get default configuration path"""
        # Detect project root
        current_dir = Path.cwd()
        while current_dir != current_dir.parent:
            claude_dir = current_dir / '.claude' / 'hooks' / 'config'
            if claude_dir.exists():
                return str(claude_dir)
            current_dir = current_dir.parent

        # Fallback to relative path
        return '.claude/hooks/config'

    def _load_config(self) -> Dict:
        """Load global hooks configuration"""
        config_file = Path(self.config_path) / 'hooks-config.json'
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load hooks config: {e}")
            return self._get_default_config()

    def _load_agent_hooks(self) -> Dict:
        """Load agent-specific hook mappings"""
        config_file = Path(self.config_path) / 'agent-hooks.json'
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Failed to load agent hooks: {e}")
            return {}

    def _load_quality_gates(self) -> Dict:
        """Load quality gate definitions"""
        config_file = Path(self.config_path) / 'quality-gates.json'
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Failed to load quality gates: {e}")
            return {}

    def _load_monitoring_config(self) -> Dict:
        """Load monitoring configuration"""
        config_file = Path(self.config_path) / 'monitoring-config.json'
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Failed to load monitoring config: {e}")
            return {}

    def _get_default_config(self) -> Dict:
        """Get default configuration"""
        return {
            "enabled": True,
            "execution": {
                "parallel": True,
                "max_concurrent_hooks": 5,
                "timeout_seconds": 300,
                "retries": 3
            },
            "error_handling": {
                "continue_on_failure": False,
                "log_errors": True
            }
        }

    def execute_hooks(
        self,
        hook_type: str,
        agent_name: Optional[str] = None,
        context: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Execute hooks for given type and agent

        Args:
            hook_type: Type of hooks (pre-agent, post-agent, pre-commit, etc.)
            agent_name: Name of agent (if agent-specific)
            context: Additional context for hook execution

        Returns:
            Dictionary with execution results
        """
        if not self.config.get('enabled', True):
            logger.info("Hooks system is disabled")
            return {'success': True, 'skipped': True}

        # Get hooks to execute
        hooks = self._get_hooks_for_type(hook_type, agent_name)

        if not hooks:
            logger.info(f"No hooks found for type: {hook_type}")
            return {'success': True, 'hooks': []}

        # Sort by priority
        sorted_hooks = self._sort_hooks_by_priority(hooks)

        logger.info(f"Executing {len(sorted_hooks)} hooks for {hook_type}")

        # Execute hooks
        results = []
        if self.config.get('execution', {}).get('parallel', True):
            results = self._execute_hooks_parallel(sorted_hooks, context)
        else:
            results = self._execute_hooks_sequential(sorted_hooks, context)

        # Analyze results
        success = all(r.status == HookStatus.SUCCESS for r in results)
        failed = [r for r in results if r.status == HookStatus.FAILED]

        return {
            'success': success,
            'total_hooks': len(results),
            'failed_hooks': len(failed),
            'results': [self._result_to_dict(r) for r in results],
            'errors': [r.error for r in failed]
        }

    def _get_hooks_for_type(
        self,
        hook_type: str,
        agent_name: Optional[str]
    ) -> List[Hook]:
        """Get hooks for specified type and agent"""
        hooks = []

        # Parse hook type (e.g., "pre-agent", "post-agent", "pre-commit")
        category = hook_type.replace('-', '_')

        # Agent-specific hooks
        if agent_name and agent_name in self.agent_hooks:
            agent_config = self.agent_hooks[agent_name]
            hook_list = agent_config.get(f'{category}_hooks', [])

            for hook_def in hook_list:
                hooks.append(Hook(
                    name=hook_def['name'],
                    path=hook_def['path'],
                    priority=hook_def['priority'],
                    timeout=hook_def['timeout'],
                    category=category
                ))

        # Default hooks
        if '_default' in self.agent_hooks:
            default_config = self.agent_hooks['_default']
            hook_list = default_config.get(f'{category}_hooks', [])

            for hook_def in hook_list:
                # Don't duplicate if already added for agent
                if not any(h.name == hook_def['name'] for h in hooks):
                    hooks.append(Hook(
                        name=hook_def['name'],
                        path=hook_def['path'],
                        priority=hook_def['priority'],
                        timeout=hook_def['timeout'],
                        category=category
                    ))

        return hooks

    def _sort_hooks_by_priority(self, hooks: List[Hook]) -> List[Hook]:
        """Sort hooks by priority (critical > high > medium > low)"""
        priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        return sorted(hooks, key=lambda h: priority_order.get(h.priority.lower(), 999))

    def _execute_hooks_sequential(
        self,
        hooks: List[Hook],
        context: Optional[Dict]
    ) -> List[HookResult]:
        """Execute hooks sequentially"""
        results = []
        for hook in hooks:
            result = self._execute_single_hook(hook, context)
            results.append(result)

            # Stop on failure if configured
            if (result.status == HookStatus.FAILED and
                not self.config.get('error_handling', {}).get('continue_on_failure', False)):
                logger.error(f"Hook {hook.name} failed, stopping execution")
                break

        return results

    def _execute_hooks_parallel(
        self,
        hooks: List[Hook],
        context: Optional[Dict]
    ) -> List[HookResult]:
        """Execute hooks in parallel with concurrency limit"""
        max_concurrent = self.config.get('execution', {}).get('max_concurrent_hooks', 5)

        # Group by priority
        priority_groups = {}
        for hook in hooks:
            priority_groups.setdefault(hook.priority, []).append(hook)

        results = []

        # Execute each priority group
        for priority in ['critical', 'high', 'medium', 'low']:
            group = priority_groups.get(priority, [])
            if not group:
                continue

            # Execute group in parallel with concurrency limit
            with multiprocessing.Pool(processes=min(max_concurrent, len(group))) as pool:
                group_results = pool.starmap(
                    self._execute_single_hook,
                    [(hook, context) for hook in group]
                )
                results.extend(group_results)

                # Stop on critical failure
                if priority in ['critical', 'high']:
                    failed = [r for r in group_results if r.status == HookStatus.FAILED]
                    if failed and not self.config.get('error_handling', {}).get('continue_on_failure', False):
                        logger.error(f"Critical/High priority hook failed, stopping")
                        return results

        return results

    def _execute_single_hook(
        self,
        hook: Hook,
        context: Optional[Dict]
    ) -> HookResult:
        """Execute a single hook with retry logic"""
        logger.info(f"Executing hook: {hook.name} (priority: {hook.priority})")

        start_time = time.time()
        retries = 0
        max_retries = self.config.get('execution', {}).get('retries', 3)

        while retries <= max_retries:
            try:
                # Build hook path
                hook_path = Path(self.hooks_dir) / hook.path

                if not hook_path.exists():
                    return HookResult(
                        hook_name=hook.name,
                        status=HookStatus.FAILED,
                        execution_time=time.time() - start_time,
                        error=f"Hook file not found: {hook_path}"
                    )

                # Execute hook
                result = subprocess.run(
                    ['python3', str(hook_path)],
                    capture_output=True,
                    text=True,
                    timeout=hook.timeout,
                    env={**os.environ, 'HOOK_CONTEXT': json.dumps(context or {})}
                )

                execution_time = time.time() - start_time

                if result.returncode == 0:
                    logger.info(f"✅ Hook {hook.name} succeeded ({execution_time:.2f}s)")
                    return HookResult(
                        hook_name=hook.name,
                        status=HookStatus.SUCCESS,
                        execution_time=execution_time,
                        output=result.stdout,
                        exit_code=result.returncode,
                        retries=retries
                    )
                else:
                    # Retry on failure
                    retries += 1
                    if retries <= max_retries:
                        logger.warning(f"Hook {hook.name} failed, retrying ({retries}/{max_retries})")
                        time.sleep(hook.retry_delay)
                        continue
                    else:
                        logger.error(f"❌ Hook {hook.name} failed after {retries} retries")
                        return HookResult(
                            hook_name=hook.name,
                            status=HookStatus.FAILED,
                            execution_time=execution_time,
                            output=result.stdout,
                            error=result.stderr,
                            exit_code=result.returncode,
                            retries=retries
                        )

            except subprocess.TimeoutExpired:
                logger.error(f"⏱️  Hook {hook.name} timed out after {hook.timeout}s")
                return HookResult(
                    hook_name=hook.name,
                    status=HookStatus.TIMEOUT,
                    execution_time=hook.timeout,
                    error=f"Hook execution timed out after {hook.timeout}s",
                    retries=retries
                )

            except Exception as e:
                logger.error(f"Hook {hook.name} raised exception: {e}")
                retries += 1
                if retries > max_retries:
                    return HookResult(
                        hook_name=hook.name,
                        status=HookStatus.FAILED,
                        execution_time=time.time() - start_time,
                        error=str(e),
                        retries=retries
                    )
                time.sleep(hook.retry_delay)

    def _result_to_dict(self, result: HookResult) -> Dict:
        """Convert HookResult to dictionary"""
        return {
            'hook_name': result.hook_name,
            'status': result.status.value,
            'execution_time': result.execution_time,
            'output': result.output,
            'error': result.error,
            'exit_code': result.exit_code,
            'retries': result.retries
        }


def main():
    """CLI entry point for hook engine"""
    import argparse

    parser = argparse.ArgumentParser(description='Hook Execution Engine')
    parser.add_argument('command', choices=['execute', 'execute-category', 'execute-agent'])
    parser.add_argument('--hook', help='Specific hook to execute')
    parser.add_argument('--category', help='Hook category (agent-lifecycle/pre-agent, etc.)')
    parser.add_argument('--agent', help='Agent name')
    parser.add_argument('--phase', choices=['pre', 'post'], help='Agent phase')
    parser.add_argument('--config', help='Configuration directory path')

    args = parser.parse_args()

    # Initialize engine
    engine = HookEngine(config_path=args.config)

    # Execute based on command
    if args.command == 'execute':
        if not args.hook:
            print("Error: --hook is required for 'execute' command")
            sys.exit(1)

        # Execute single hook
        hook = Hook(
            name=args.hook.split('/')[-1].replace('.py', ''),
            path=args.hook,
            priority='medium',
            timeout=300
        )
        result = engine._execute_single_hook(hook, {})
        print(json.dumps(engine._result_to_dict(result), indent=2))
        sys.exit(0 if result.status == HookStatus.SUCCESS else 1)

    elif args.command == 'execute-category':
        if not args.category:
            print("Error: --category is required for 'execute-category' command")
            sys.exit(1)

        result = engine.execute_hooks(args.category)
        print(json.dumps(result, indent=2))
        sys.exit(0 if result['success'] else 1)

    elif args.command == 'execute-agent':
        if not args.agent or not args.phase:
            print("Error: --agent and --phase are required for 'execute-agent' command")
            sys.exit(1)

        hook_type = f"{args.phase}-agent"
        result = engine.execute_hooks(hook_type, agent_name=args.agent)
        print(json.dumps(result, indent=2))
        sys.exit(0 if result['success'] else 1)


if __name__ == '__main__':
    main()
