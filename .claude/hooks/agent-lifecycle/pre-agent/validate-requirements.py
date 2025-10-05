#!/usr/bin/env python3
"""
Validate Requirements Hook - My Name Is Claude Framework v3.4.0

Validates that all requirements are met before agent execution.

META: priority: critical
META: timeout: 30
META: category: agent-lifecycle/pre-agent
"""

import sys
from pathlib import Path

# Add hooks utils to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'core'))

from hook_utils import (
    HookContext, HookLogger, get_hook_context, set_hook_result,
    get_project_root, check_file_exists
)


def validate_framework_files() -> tuple[bool, list[str]]:
    """
    Validate core framework files exist

    Returns:
        Tuple of (success, errors)
    """
    errors = []
    project_root = get_project_root()

    required_files = [
        'CLAUDE.md',
        '.claude/agents',
        '.claude/prompts',
        '.ai-tools'
    ]

    for file_path in required_files:
        full_path = project_root / file_path
        if not full_path.exists():
            errors.append(f"Required file/directory not found: {file_path}")

    return len(errors) == 0, errors


def validate_agent_exists(agent_name: str) -> tuple[bool, list[str]]:
    """
    Validate agent definition exists

    Args:
        agent_name: Name of the agent

    Returns:
        Tuple of (success, errors)
    """
    if not agent_name:
        return True, []  # No agent specified

    errors = []
    project_root = get_project_root()

    # Check core agents
    agent_file = project_root / '.claude' / 'agents' / 'core' / f'{agent_name}.md'
    if agent_file.exists():
        return True, []

    # Check enterprise agents
    agent_file = project_root / '.claude' / 'agents' / 'enterprise' / f'{agent_name}.md'
    if agent_file.exists():
        return True, []

    # Check custom agents
    custom_categories = ['graphics', 'hardware', 'desktop', 'scientific']
    for category in custom_categories:
        agent_file = project_root / '.claude' / 'agents' / 'custom' / category / f'{agent_name}.md'
        if agent_file.exists():
            return True, []

    errors.append(f"Agent definition not found: {agent_name}")
    return False, errors


def validate_task_requirements(context: dict) -> tuple[bool, list[str]]:
    """
    Validate task-specific requirements

    Args:
        context: Hook execution context

    Returns:
        Tuple of (success, errors)
    """
    errors = []
    task = context.get('task', '')

    if not task:
        errors.append("No task specified in context")
        return False, errors

    # Validate task description length
    if len(task) < 10:
        errors.append("Task description too short (minimum 10 characters)")

    return len(errors) == 0, errors


def main():
    """Main hook execution"""
    logger = HookLogger("validate-requirements")
    context = get_hook_context()

    with HookContext("validate-requirements", context):
        try:
            logger.info("Validating requirements before agent execution")

            all_errors = []

            # Validate framework files
            success, errors = validate_framework_files()
            if not success:
                all_errors.extend(errors)
                logger.error(f"Framework validation failed: {errors}")

            # Validate agent exists
            agent_name = context.get('agent_name', '')
            if agent_name:
                success, errors = validate_agent_exists(agent_name)
                if not success:
                    all_errors.extend(errors)
                    logger.error(f"Agent validation failed: {errors}")
            else:
                logger.warning("No agent name in context, skipping agent validation")

            # Validate task requirements
            success, errors = validate_task_requirements(context)
            if not success:
                all_errors.extend(errors)
                logger.error(f"Task validation failed: {errors}")

            # Return results
            if all_errors:
                set_hook_result(
                    success=False,
                    message=f"Requirements validation failed: {', '.join(all_errors)}",
                    data={'errors': all_errors}
                )
            else:
                logger.info("✅ All requirements validated successfully")
                set_hook_result(
                    success=True,
                    message="Requirements validation passed"
                )

        except Exception as e:
            logger.error(f"Hook failed: {e}")
            set_hook_result(
                success=False,
                message=f"validate-requirements failed: {e}"
            )


if __name__ == '__main__':
    main()
