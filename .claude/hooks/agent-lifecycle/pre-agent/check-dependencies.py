#!/usr/bin/env python3
"""
Check Dependencies Hook - My Name Is Claude Framework v3.4.0

Checks that all required dependencies are available.

META: priority: high
META: timeout: 60
META: category: agent-lifecycle/pre-agent
"""

import sys
import importlib
from pathlib import Path

# Add hooks utils to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'core'))

from hook_utils import (
    HookContext, HookLogger, get_hook_context, set_hook_result,
    run_command, get_project_root
)


def check_python_version() -> tuple[bool, list[str]]:
    """
    Check Python version

    Returns:
        Tuple of (success, errors)
    """
    errors = []
    version_info = sys.version_info

    if version_info.major < 3 or (version_info.major == 3 and version_info.minor < 8):
        errors.append(f"Python 3.8+ required, found {version_info.major}.{version_info.minor}")

    return len(errors) == 0, errors


def check_python_packages() -> tuple[bool, list[str], list[str]]:
    """
    Check required Python packages

    Returns:
        Tuple of (success, missing_packages, warnings)
    """
    required_packages = []
    optional_packages = ['requests', 'psutil', 'pyyaml']

    missing_required = []
    missing_optional = []

    # Check required packages
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            missing_required.append(package)

    # Check optional packages
    for package in optional_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            missing_optional.append(package)

    warnings = []
    if missing_optional:
        warnings.append(f"Optional packages missing: {', '.join(missing_optional)}")

    return len(missing_required) == 0, missing_required, warnings


def check_system_tools() -> tuple[bool, list[str]]:
    """
    Check required system tools

    Returns:
        Tuple of (success, missing_tools)
    """
    required_tools = ['git']
    optional_tools = ['docker', 'kubectl', 'npm']

    missing = []

    # Check required tools
    for tool in required_tools:
        result = run_command(['which', tool], capture_output=True)
        if not result['success']:
            missing.append(tool)

    return len(missing) == 0, missing


def check_git_repository() -> tuple[bool, list[str]]:
    """
    Check Git repository status

    Returns:
        Tuple of (success, warnings)
    """
    warnings = []

    result = run_command(['git', 'rev-parse', '--git-dir'], capture_output=True)
    if not result['success']:
        warnings.append("Not a Git repository")
        return True, warnings  # Warning, not error

    # Check if there are uncommitted changes
    result = run_command(['git', 'status', '--porcelain'], capture_output=True)
    if result['success'] and result['stdout'].strip():
        warnings.append("Uncommitted changes in repository")

    return True, warnings


def check_claude_md() -> tuple[bool, list[str]]:
    """
    Check CLAUDE.md exists and is valid

    Returns:
        Tuple of (success, errors)
    """
    errors = []
    project_root = get_project_root()
    claude_md = project_root / 'CLAUDE.md'

    if not claude_md.exists():
        errors.append("CLAUDE.md not found in project root")
        return False, errors

    # Check file is not empty
    try:
        content = claude_md.read_text()
        if len(content.strip()) < 100:
            errors.append("CLAUDE.md appears to be incomplete")
    except Exception as e:
        errors.append(f"Failed to read CLAUDE.md: {e}")

    return len(errors) == 0, errors


def main():
    """Main hook execution"""
    logger = HookLogger("check-dependencies")
    context = get_hook_context()

    with HookContext("check-dependencies", context):
        try:
            logger.info("Checking dependencies")

            all_errors = []
            all_warnings = []

            # Check Python version
            success, errors = check_python_version()
            if not success:
                all_errors.extend(errors)
                logger.error(f"Python version check failed: {errors}")
            else:
                logger.info(f"✅ Python version OK: {sys.version_info.major}.{sys.version_info.minor}")

            # Check Python packages
            success, missing, warnings = check_python_packages()
            if not success:
                all_errors.append(f"Missing required packages: {', '.join(missing)}")
                logger.error(f"Package check failed: missing {missing}")
            if warnings:
                all_warnings.extend(warnings)
                logger.warning(f"Package warnings: {warnings}")

            # Check system tools
            success, missing = check_system_tools()
            if not success:
                all_errors.append(f"Missing required tools: {', '.join(missing)}")
                logger.error(f"System tools check failed: missing {missing}")
            else:
                logger.info("✅ System tools OK")

            # Check Git repository
            success, warnings = check_git_repository()
            if warnings:
                all_warnings.extend(warnings)
                logger.warning(f"Git warnings: {warnings}")

            # Check CLAUDE.md
            success, errors = check_claude_md()
            if not success:
                all_errors.extend(errors)
                logger.error(f"CLAUDE.md check failed: {errors}")
            else:
                logger.info("✅ CLAUDE.md OK")

            # Return results
            if all_errors:
                set_hook_result(
                    success=False,
                    message=f"Dependency check failed: {', '.join(all_errors)}",
                    data={'errors': all_errors, 'warnings': all_warnings}
                )
            else:
                logger.info("✅ All dependencies checked successfully")
                set_hook_result(
                    success=True,
                    message="Dependency check passed",
                    data={'warnings': all_warnings}
                )

        except Exception as e:
            logger.error(f"Hook failed: {e}")
            set_hook_result(
                success=False,
                message=f"check-dependencies failed: {e}"
            )


if __name__ == '__main__':
    main()
