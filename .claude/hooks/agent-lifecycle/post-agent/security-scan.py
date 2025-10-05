#!/usr/bin/env python3
"""
Security Scan Hook - My Name Is Claude Framework v3.4.0

Performs security scans after agent execution.

META: priority: critical
META: timeout: 180
META: category: agent-lifecycle/post-agent
"""

import sys
import re
from pathlib import Path

# Add hooks utils to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'core'))

from hook_utils import (
    HookContext, HookLogger, get_hook_context, set_hook_result,
    run_command, get_project_root
)


def scan_for_secrets() -> tuple[bool, list[str], dict]:
    """
    Scan for hardcoded secrets

    Returns:
        Tuple of (success, violations, stats)
    """
    logger = HookLogger("security-scan.secrets")
    violations = []
    stats = {'files_scanned': 0, 'secrets_found': 0}

    project_root = get_project_root()

    # Patterns for common secrets
    secret_patterns = [
        (r'password\s*=\s*[\'"][^\'"]{8,}[\'"]', 'Hardcoded password'),
        (r'api[_-]?key\s*=\s*[\'"][^\'"]{16,}[\'"]', 'API key'),
        (r'secret[_-]?key\s*=\s*[\'"][^\'"]{16,}[\'"]', 'Secret key'),
        (r'token\s*=\s*[\'"][^\'"]{16,}[\'"]', 'Token'),
        (r'aws[_-]?access[_-]?key', 'AWS access key'),
        (r'-----BEGIN (?:RSA )?PRIVATE KEY-----', 'Private key'),
    ]

    # Scan Python and JavaScript files
    for pattern_path in [project_root.rglob('*.py'), project_root.rglob('*.js')]:
        for file_path in pattern_path:
            # Skip virtual environments and node_modules
            if any(skip in str(file_path) for skip in ['venv', 'node_modules', '.git']):
                continue

            stats['files_scanned'] += 1

            try:
                content = file_path.read_text()

                for pattern, description in secret_patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    if matches:
                        violations.append(
                            f"{description} found in {file_path.relative_to(project_root)}"
                        )
                        stats['secrets_found'] += len(matches)
                        logger.warning(f"Found {description} in {file_path.name}")

            except Exception as e:
                logger.debug(f"Failed to scan {file_path}: {e}")

    return len(violations) == 0, violations, stats


def check_dependencies_vulnerabilities() -> tuple[bool, list[str], dict]:
    """
    Check for known vulnerabilities in dependencies

    Returns:
        Tuple of (success, vulnerabilities, stats)
    """
    logger = HookLogger("security-scan.dependencies")
    vulnerabilities = []
    stats = {'scanner_available': False, 'vulnerabilities_found': 0}

    # Try safety (Python)
    result = run_command(['safety', '--version'], capture_output=True, timeout=5)
    if result['success']:
        stats['scanner_available'] = True
        logger.info("Running safety scan...")

        result = run_command(['safety', 'check', '--json'], capture_output=True, timeout=60)
        if result['success']:
            try:
                import json
                data = json.loads(result['stdout'])
                if isinstance(data, list) and len(data) > 0:
                    stats['vulnerabilities_found'] = len(data)
                    for vuln in data[:5]:  # Limit to first 5
                        pkg_name = vuln.get('package', 'unknown')
                        severity = vuln.get('severity', 'unknown')
                        vulnerabilities.append(f"{pkg_name}: {severity} severity")
            except:
                pass

    # Try npm audit (Node.js)
    project_root = get_project_root()
    if (project_root / 'package.json').exists():
        result = run_command(['npm', 'audit', '--json'], capture_output=True, timeout=60)
        if result['success']:
            try:
                import json
                data = json.loads(result['stdout'])
                vuln_count = data.get('metadata', {}).get('vulnerabilities', {})
                high = vuln_count.get('high', 0)
                critical = vuln_count.get('critical', 0)

                if high > 0 or critical > 0:
                    vulnerabilities.append(f"npm: {critical} critical, {high} high vulnerabilities")
                    stats['vulnerabilities_found'] += high + critical
            except:
                pass

    return len(vulnerabilities) == 0, vulnerabilities, stats


def check_insecure_functions() -> tuple[bool, list[str], dict]:
    """
    Check for use of insecure functions

    Returns:
        Tuple of (success, warnings, stats)
    """
    warnings = []
    stats = {'files_scanned': 0, 'insecure_found': 0}

    project_root = get_project_root()

    insecure_patterns = [
        (r'\beval\s*\(', 'Use of eval()'),
        (r'\bexec\s*\(', 'Use of exec()'),
        (r'subprocess\.(?:call|run)\([^)]*shell\s*=\s*True', 'Shell injection risk'),
        (r'pickle\.loads?\(', 'Insecure deserialization'),
    ]

    for file_path in project_root.rglob('*.py'):
        if any(skip in str(file_path) for skip in ['venv', 'node_modules', '.git']):
            continue

        stats['files_scanned'] += 1

        try:
            content = file_path.read_text()

            for pattern, description in insecure_patterns:
                if re.search(pattern, content):
                    warnings.append(
                        f"{description} in {file_path.relative_to(project_root)}"
                    )
                    stats['insecure_found'] += 1

        except Exception:
            pass

    return True, warnings, stats  # Warnings, not blocking


def main():
    """Main hook execution"""
    logger = HookLogger("security-scan")
    context = get_hook_context()

    with HookContext("security-scan", context):
        try:
            logger.info("Performing security scan")

            all_violations = []
            all_warnings = []
            all_stats = {}

            # Scan for secrets
            success, violations, stats = scan_for_secrets()
            all_stats['secrets'] = stats
            if not success:
                all_violations.extend(violations)
                logger.error(f"Found {len(violations)} secret violations")

            # Check dependencies
            success, vulnerabilities, stats = check_dependencies_vulnerabilities()
            all_stats['dependencies'] = stats
            if not success:
                all_violations.extend(vulnerabilities)
                logger.warning(f"Found {len(vulnerabilities)} dependency vulnerabilities")

            # Check insecure functions
            success, warnings, stats = check_insecure_functions()
            all_stats['insecure_functions'] = stats
            if warnings:
                all_warnings.extend(warnings)

            # Calculate security score
            security_score = 100
            security_score -= len(all_violations) * 15
            security_score -= len(all_warnings) * 5
            security_score = max(0, security_score)

            all_stats['security_score'] = security_score

            logger.info(f"Security score: {security_score}/100")

            # Block on critical violations (hardcoded secrets)
            if all_stats['secrets']['secrets_found'] > 0:
                set_hook_result(
                    success=False,
                    message=f"Security scan failed: {len(all_violations)} violations found",
                    data={
                        'security_score': security_score,
                        'violations': all_violations,
                        'warnings': all_warnings,
                        'stats': all_stats
                    }
                )
            else:
                set_hook_result(
                    success=True,
                    message=f"Security scan passed (score: {security_score}/100)",
                    data={
                        'security_score': security_score,
                        'violations': all_violations,
                        'warnings': all_warnings,
                        'stats': all_stats
                    }
                )

        except Exception as e:
            logger.error(f"Hook failed: {e}")
            set_hook_result(
                success=False,
                message=f"security-scan failed: {e}"
            )


if __name__ == '__main__':
    main()
