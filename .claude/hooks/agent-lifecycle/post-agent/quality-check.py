#!/usr/bin/env python3
"""
Quality Check Hook - My Name Is Claude Framework v3.4.0

Performs quality checks after agent execution.

META: priority: high
META: timeout: 120
META: category: agent-lifecycle/post-agent
"""

import sys
from pathlib import Path

# Add hooks utils to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'core'))

from hook_utils import (
    HookContext, HookLogger, get_hook_context, set_hook_result,
    run_command, get_project_root
)


def check_code_style() -> tuple[bool, list[str], dict]:
    """
    Check code style compliance

    Returns:
        Tuple of (success, errors, stats)
    """
    logger = HookLogger("quality-check.code-style")
    errors = []
    stats = {}

    # Try common Python linters
    linters = [
        (['flake8', '--version'], ['flake8', '.'], 'flake8'),
        (['pylint', '--version'], ['pylint', '--rcfile=.pylintrc', '.'], 'pylint'),
        (['black', '--version'], ['black', '--check', '.'], 'black')
    ]

    for check_cmd, lint_cmd, name in linters:
        # Check if linter is available
        result = run_command(check_cmd, capture_output=True, timeout=5)
        if not result['success']:
            logger.info(f"{name} not available, skipping")
            continue

        # Run linter
        result = run_command(lint_cmd, capture_output=True, timeout=60)
        stats[name] = {
            'available': True,
            'passed': result['success']
        }

        if not result['success']:
            errors.append(f"{name} found issues")
            logger.warning(f"{name} found issues (non-blocking)")

    return True, errors, stats  # Non-blocking


def check_documentation() -> tuple[bool, list[str], dict]:
    """
    Check documentation completeness

    Returns:
        Tuple of (success, warnings, stats)
    """
    warnings = []
    stats = {
        'readme_exists': False,
        'claude_md_exists': False,
        'docs_dir_exists': False
    }

    project_root = get_project_root()

    # Check README
    readme_files = ['README.md', 'readme.md', 'Readme.md']
    for readme in readme_files:
        if (project_root / readme).exists():
            stats['readme_exists'] = True
            break

    if not stats['readme_exists']:
        warnings.append("README.md not found")

    # Check CLAUDE.md
    if (project_root / 'CLAUDE.md').exists():
        stats['claude_md_exists'] = True
    else:
        warnings.append("CLAUDE.md not found")

    # Check docs directory
    if (project_root / 'docs').exists():
        stats['docs_dir_exists'] = True
        stats['docs_count'] = len(list((project_root / 'docs').rglob('*.md')))

    return True, warnings, stats


def check_test_coverage() -> tuple[bool, list[str], dict]:
    """
    Check test coverage (if available)

    Returns:
        Tuple of (success, warnings, stats)
    """
    logger = HookLogger("quality-check.test-coverage")
    warnings = []
    stats = {
        'coverage_available': False,
        'coverage_percent': 0
    }

    # Check if pytest-cov is available
    result = run_command(['pytest', '--version'], capture_output=True, timeout=5)
    if not result['success']:
        logger.info("pytest not available, skipping coverage check")
        return True, warnings, stats

    # Try to run coverage
    result = run_command(
        ['pytest', '--cov=.', '--cov-report=term-missing'],
        capture_output=True,
        timeout=120
    )

    if result['success']:
        stats['coverage_available'] = True

        # Try to parse coverage percentage
        for line in result['stdout'].split('\n'):
            if 'TOTAL' in line and '%' in line:
                try:
                    coverage = int(line.split('%')[0].split()[-1])
                    stats['coverage_percent'] = coverage

                    if coverage < 80:
                        warnings.append(f"Test coverage below 80%: {coverage}%")
                except:
                    pass

    return True, warnings, stats


def check_file_structure() -> tuple[bool, list[str], dict]:
    """
    Check project file structure

    Returns:
        Tuple of (success, warnings, stats)
    """
    warnings = []
    stats = {
        'has_gitignore': False,
        'has_tests': False,
        'has_requirements': False
    }

    project_root = get_project_root()

    # Check .gitignore
    if (project_root / '.gitignore').exists():
        stats['has_gitignore'] = True
    else:
        warnings.append(".gitignore not found")

    # Check tests directory
    test_dirs = ['tests', 'test', '__tests__']
    for test_dir in test_dirs:
        if (project_root / test_dir).exists():
            stats['has_tests'] = True
            break

    if not stats['has_tests']:
        warnings.append("No tests directory found")

    # Check requirements file
    req_files = ['requirements.txt', 'Pipfile', 'pyproject.toml', 'setup.py']
    for req_file in req_files:
        if (project_root / req_file).exists():
            stats['has_requirements'] = True
            break

    return True, warnings, stats


def main():
    """Main hook execution"""
    logger = HookLogger("quality-check")
    context = get_hook_context()

    with HookContext("quality-check", context):
        try:
            logger.info("Performing quality checks")

            all_errors = []
            all_warnings = []
            all_stats = {}

            # Code style check
            success, errors, stats = check_code_style()
            all_stats['code_style'] = stats
            if errors:
                all_warnings.extend([f"Code style: {e}" for e in errors])

            # Documentation check
            success, warnings, stats = check_documentation()
            all_stats['documentation'] = stats
            if warnings:
                all_warnings.extend([f"Documentation: {w}" for w in warnings])

            # Test coverage check
            success, warnings, stats = check_test_coverage()
            all_stats['test_coverage'] = stats
            if warnings:
                all_warnings.extend([f"Test coverage: {w}" for w in warnings])

            # File structure check
            success, warnings, stats = check_file_structure()
            all_stats['file_structure'] = stats
            if warnings:
                all_warnings.extend([f"File structure: {w}" for w in warnings])

            # Calculate overall quality score
            quality_score = 100
            quality_score -= len(all_errors) * 20
            quality_score -= len(all_warnings) * 5
            quality_score = max(0, quality_score)

            all_stats['quality_score'] = quality_score

            logger.info(f"Quality score: {quality_score}/100")
            logger.info(f"Errors: {len(all_errors)}, Warnings: {len(all_warnings)}")

            # Quality checks are warnings, not blocking
            set_hook_result(
                success=True,
                message=f"Quality check completed (score: {quality_score}/100)",
                data={
                    'quality_score': quality_score,
                    'errors': all_errors,
                    'warnings': all_warnings,
                    'stats': all_stats
                }
            )

        except Exception as e:
            logger.error(f"Hook failed: {e}")
            set_hook_result(
                success=False,
                message=f"quality-check failed: {e}"
            )


if __name__ == '__main__':
    main()
