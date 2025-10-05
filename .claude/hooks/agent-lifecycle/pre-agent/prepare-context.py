#!/usr/bin/env python3
"""
Prepare Context Hook - My Name Is Claude Framework v3.4.0

Prepares execution context for agent.

META: priority: medium
META: timeout: 20
META: category: agent-lifecycle/pre-agent
"""

import sys
import os
from pathlib import Path
from datetime import datetime

# Add hooks utils to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'core'))

from hook_utils import (
    HookContext, HookLogger, get_hook_context, set_hook_result,
    get_project_root, get_git_info, load_json
)


def prepare_environment_context() -> dict:
    """
    Prepare environment context information

    Returns:
        Environment context dictionary
    """
    return {
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'platform': sys.platform,
        'cwd': str(Path.cwd()),
        'timestamp': datetime.now().isoformat(),
        'user': os.environ.get('USER', 'unknown')
    }


def prepare_project_context() -> dict:
    """
    Prepare project context information

    Returns:
        Project context dictionary
    """
    project_root = get_project_root()

    context = {
        'project_root': str(project_root),
        'project_name': project_root.name,
    }

    # Try to load CLAUDE.md metadata
    try:
        claude_md_path = project_root / 'CLAUDE.md'
        if claude_md_path.exists():
            content = claude_md_path.read_text()

            # Extract basic metadata (simple parsing)
            for line in content.split('\n'):
                if 'project_version' in line:
                    context['project_version'] = line.split(':')[-1].strip().strip('"')
                elif 'project_description' in line:
                    context['project_description'] = line.split(':')[-1].strip().strip('"')

    except Exception:
        pass

    # Add Git information
    git_info = get_git_info()
    context['git'] = git_info

    return context


def prepare_agent_context(agent_name: str) -> dict:
    """
    Prepare agent-specific context

    Args:
        agent_name: Name of the agent

    Returns:
        Agent context dictionary
    """
    if not agent_name:
        return {}

    project_root = get_project_root()

    context = {
        'agent_name': agent_name,
        'agent_type': 'unknown'
    }

    # Determine agent type based on location
    categories = [
        ('core', '.claude/agents/core'),
        ('enterprise', '.claude/agents/enterprise'),
        ('custom', '.claude/agents/custom')
    ]

    for agent_type, path in categories:
        agent_path = project_root / path
        if agent_path.exists():
            for agent_file in agent_path.rglob(f'{agent_name}.md'):
                context['agent_type'] = agent_type
                context['agent_file'] = str(agent_file.relative_to(project_root))
                break

    return context


def prepare_execution_context(task: str) -> dict:
    """
    Prepare execution context

    Args:
        task: Task description

    Returns:
        Execution context dictionary
    """
    return {
        'task': task,
        'task_length': len(task),
        'execution_id': f"exec_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        'start_time': datetime.now().isoformat()
    }


def main():
    """Main hook execution"""
    logger = HookLogger("prepare-context")
    context = get_hook_context()

    with HookContext("prepare-context", context):
        try:
            logger.info("Preparing execution context")

            # Prepare all context components
            prepared_context = {}

            # Environment context
            env_context = prepare_environment_context()
            prepared_context['environment'] = env_context
            logger.info(f"Environment: Python {env_context['python_version']} on {env_context['platform']}")

            # Project context
            project_context = prepare_project_context()
            prepared_context['project'] = project_context
            logger.info(f"Project: {project_context['project_name']} at {project_context['project_root']}")

            # Agent context
            agent_name = context.get('agent_name', '')
            if agent_name:
                agent_context = prepare_agent_context(agent_name)
                prepared_context['agent'] = agent_context
                logger.info(f"Agent: {agent_name} ({agent_context.get('agent_type', 'unknown')})")

            # Execution context
            task = context.get('task', '')
            if task:
                exec_context = prepare_execution_context(task)
                prepared_context['execution'] = exec_context
                logger.info(f"Execution ID: {exec_context['execution_id']}")

            # Merge with original context
            prepared_context['original_context'] = context

            logger.info("✅ Context prepared successfully")
            set_hook_result(
                success=True,
                message="Context preparation completed",
                data=prepared_context
            )

        except Exception as e:
            logger.error(f"Hook failed: {e}")
            set_hook_result(
                success=False,
                message=f"prepare-context failed: {e}"
            )


if __name__ == '__main__':
    main()
