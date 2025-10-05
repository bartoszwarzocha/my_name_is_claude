#!/usr/bin/env python3
"""
Hook Validation System - My Name Is Claude Framework v3.4.0

Security and safety validation for hooks before execution.

This is a TEMPLATE implementation. Actual implementation should:
1. Adapt to project security requirements
2. Integrate with existing security scanning tools
3. Follow project-specific validation patterns
"""

import os
import re
import ast
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Set, Any, Tuple
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class ValidationResult:
    """Result of hook validation"""
    valid: bool
    errors: List[str]
    warnings: List[str]
    security_score: int  # 0-100
    details: Dict[str, Any]


class HookValidator:
    """
    Security and safety validation for hooks
    """

    # Dangerous patterns to detect
    DANGEROUS_PATTERNS = [
        r'os\.system\([^)]*\)',
        r'subprocess\.call\([^)]*shell=True',
        r'eval\(',
        r'exec\(',
        r'__import__\(',
        r'open\([^)]*[\'"]w[\'"]',
        r'rm\s+-rf',
        r'shutil\.rmtree',
        r'os\.remove',
        r'os\.unlink',
    ]

    # Required security practices
    REQUIRED_PATTERNS = [
        r'#!/usr/bin/env python3',  # Shebang
        r'""".*?"""',  # Docstring
    ]

    # Allowed imports
    ALLOWED_IMPORTS = {
        'os', 'sys', 'json', 'logging', 'pathlib', 'subprocess',
        'argparse', 'typing', 'dataclasses', 'enum', 'time',
        'datetime', 'collections', 're', 'hashlib', 'functools'
    }

    def __init__(self, strict_mode: bool = False):
        """
        Initialize validator

        Args:
            strict_mode: Enable strict validation rules
        """
        self.strict_mode = strict_mode

    def validate_hook(self, hook_path: Path) -> ValidationResult:
        """
        Validate a hook file

        Args:
            hook_path: Path to hook file

        Returns:
            Validation result
        """
        errors = []
        warnings = []
        details = {}

        if not hook_path.exists():
            return ValidationResult(
                valid=False,
                errors=[f"Hook file not found: {hook_path}"],
                warnings=[],
                security_score=0,
                details={}
            )

        try:
            with open(hook_path, 'r') as f:
                content = f.read()

            # Syntax validation
            syntax_valid, syntax_errors = self._validate_syntax(content)
            if not syntax_valid:
                errors.extend(syntax_errors)

            # Security validation
            security_score, security_issues = self._validate_security(content)
            if security_issues['errors']:
                errors.extend(security_issues['errors'])
            if security_issues['warnings']:
                warnings.extend(security_issues['warnings'])

            # Structure validation
            structure_valid, structure_warnings = self._validate_structure(content)
            warnings.extend(structure_warnings)

            # Import validation
            import_valid, import_issues = self._validate_imports(content)
            if not import_valid:
                if self.strict_mode:
                    errors.extend(import_issues)
                else:
                    warnings.extend(import_issues)

            # Permissions validation
            perm_valid, perm_warnings = self._validate_permissions(hook_path)
            warnings.extend(perm_warnings)

            # Size validation
            size_valid, size_warning = self._validate_size(hook_path)
            if size_warning:
                warnings.append(size_warning)

            details = {
                'security_score': security_score,
                'file_size': hook_path.stat().st_size,
                'line_count': len(content.split('\n')),
                'checksum': self._calculate_checksum(hook_path)
            }

            valid = len(errors) == 0 and security_score >= (80 if self.strict_mode else 60)

            return ValidationResult(
                valid=valid,
                errors=errors,
                warnings=warnings,
                security_score=security_score,
                details=details
            )

        except Exception as e:
            logger.error(f"Validation failed for {hook_path}: {e}")
            return ValidationResult(
                valid=False,
                errors=[f"Validation exception: {str(e)}"],
                warnings=[],
                security_score=0,
                details={}
            )

    def _validate_syntax(self, content: str) -> Tuple[bool, List[str]]:
        """Validate Python syntax"""
        try:
            ast.parse(content)
            return True, []
        except SyntaxError as e:
            return False, [f"Syntax error at line {e.lineno}: {e.msg}"]

    def _validate_security(self, content: str) -> Tuple[int, Dict[str, List[str]]]:
        """
        Validate security

        Returns:
            Tuple of (security_score, issues_dict)
        """
        errors = []
        warnings = []
        score = 100

        # Check for dangerous patterns
        for pattern in self.DANGEROUS_PATTERNS:
            matches = re.findall(pattern, content)
            if matches:
                score -= 20
                errors.append(f"Dangerous pattern detected: {pattern}")

        # Check for hardcoded secrets
        secret_patterns = [
            r'password\s*=\s*[\'"][^\'"]+[\'"]',
            r'api_key\s*=\s*[\'"][^\'"]+[\'"]',
            r'token\s*=\s*[\'"][^\'"]+[\'"]',
            r'secret\s*=\s*[\'"][^\'"]+[\'"]',
        ]

        for pattern in secret_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                score -= 15
                warnings.append(f"Potential hardcoded secret detected: {pattern}")

        # Check for network operations
        network_patterns = [
            r'requests\.',
            r'urllib\.',
            r'socket\.',
            r'http\.',
        ]

        for pattern in network_patterns:
            if re.search(pattern, content):
                score -= 5
                warnings.append(f"Network operation detected: {pattern}")

        # Check for file operations
        file_patterns = [
            r'open\(',
            r'with open',
        ]

        write_operations = re.findall(r'open\([^)]*[\'"]w', content)
        if write_operations:
            score -= 10
            warnings.append("File write operations detected")

        return max(0, score), {'errors': errors, 'warnings': warnings}

    def _validate_structure(self, content: str) -> Tuple[bool, List[str]]:
        """Validate code structure"""
        warnings = []

        # Check for shebang
        if not content.startswith('#!/usr/bin/env python3'):
            warnings.append("Missing shebang line")

        # Check for module docstring
        try:
            tree = ast.parse(content)
            if not ast.get_docstring(tree):
                warnings.append("Missing module docstring")
        except:
            pass

        # Check for main guard
        if 'if __name__' not in content:
            warnings.append("Missing __main__ guard")

        # Check for logging
        if 'import logging' not in content and 'from logging' not in content:
            warnings.append("No logging configured")

        return True, warnings

    def _validate_imports(self, content: str) -> Tuple[bool, List[str]]:
        """Validate imports"""
        issues = []

        try:
            tree = ast.parse(content)

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name.split('.')[0] not in self.ALLOWED_IMPORTS:
                            issues.append(f"Unapproved import: {alias.name}")

                elif isinstance(node, ast.ImportFrom):
                    if node.module and node.module.split('.')[0] not in self.ALLOWED_IMPORTS:
                        issues.append(f"Unapproved import: from {node.module}")

        except Exception as e:
            issues.append(f"Import validation failed: {e}")

        return len(issues) == 0, issues

    def _validate_permissions(self, hook_path: Path) -> Tuple[bool, List[str]]:
        """Validate file permissions"""
        warnings = []

        # Check if executable
        if not os.access(hook_path, os.X_OK):
            warnings.append("Hook is not executable (consider chmod +x)")

        # Check ownership
        stat_info = hook_path.stat()
        if stat_info.st_uid == 0:
            warnings.append("Hook is owned by root (security risk)")

        # Check world-writable
        if stat_info.st_mode & 0o002:
            warnings.append("Hook is world-writable (security risk)")

        return True, warnings

    def _validate_size(self, hook_path: Path) -> Tuple[bool, Optional[str]]:
        """Validate file size"""
        max_size = 1024 * 1024  # 1MB
        size = hook_path.stat().st_size

        if size > max_size:
            return False, f"Hook file too large: {size} bytes (max: {max_size})"

        return True, None

    def _calculate_checksum(self, file_path: Path) -> str:
        """Calculate SHA256 checksum"""
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()

    def validate_hook_signature(self, hook_path: Path, expected_checksum: str) -> bool:
        """
        Validate hook hasn't been tampered with

        Args:
            hook_path: Path to hook file
            expected_checksum: Expected SHA256 checksum

        Returns:
            True if checksum matches
        """
        actual_checksum = self._calculate_checksum(hook_path)
        return actual_checksum == expected_checksum

    def generate_validation_report(self, results: List[Tuple[str, ValidationResult]]) -> str:
        """
        Generate validation report

        Args:
            results: List of (hook_name, validation_result) tuples

        Returns:
            Formatted validation report
        """
        report = []
        report.append("=" * 80)
        report.append("HOOK VALIDATION REPORT")
        report.append("=" * 80)
        report.append("")

        total = len(results)
        valid = sum(1 for _, r in results if r.valid)
        invalid = total - valid

        report.append(f"Total Hooks: {total}")
        report.append(f"Valid: {valid} ✅")
        report.append(f"Invalid: {invalid} ❌")
        report.append("")

        for hook_name, result in results:
            report.append("-" * 80)
            report.append(f"Hook: {hook_name}")
            report.append(f"Status: {'✅ VALID' if result.valid else '❌ INVALID'}")
            report.append(f"Security Score: {result.security_score}/100")
            report.append("")

            if result.errors:
                report.append("Errors:")
                for error in result.errors:
                    report.append(f"  ❌ {error}")
                report.append("")

            if result.warnings:
                report.append("Warnings:")
                for warning in result.warnings:
                    report.append(f"  ⚠️  {warning}")
                report.append("")

            if result.details:
                report.append("Details:")
                for key, value in result.details.items():
                    report.append(f"  {key}: {value}")
                report.append("")

        report.append("=" * 80)

        return "\n".join(report)


def main():
    """CLI entry point for hook validator"""
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Hook Validation Tool')
    parser.add_argument('hook_path', help='Path to hook file to validate')
    parser.add_argument('--strict', action='store_true', help='Enable strict validation')
    parser.add_argument('--checksum', help='Expected checksum for signature validation')

    args = parser.parse_args()

    validator = HookValidator(strict_mode=args.strict)
    hook_path = Path(args.hook_path)

    # Validate hook
    result = validator.validate_hook(hook_path)

    # Print results
    print(f"\nValidation Results for: {hook_path.name}")
    print("=" * 60)
    print(f"Status: {'✅ VALID' if result.valid else '❌ INVALID'}")
    print(f"Security Score: {result.security_score}/100")
    print()

    if result.errors:
        print("Errors:")
        for error in result.errors:
            print(f"  ❌ {error}")
        print()

    if result.warnings:
        print("Warnings:")
        for warning in result.warnings:
            print(f"  ⚠️  {warning}")
        print()

    if result.details:
        print("Details:")
        for key, value in result.details.items():
            print(f"  {key}: {value}")
        print()

    # Checksum validation if requested
    if args.checksum:
        checksum_valid = validator.validate_hook_signature(hook_path, args.checksum)
        print(f"Checksum Validation: {'✅ VALID' if checksum_valid else '❌ INVALID'}")

    sys.exit(0 if result.valid else 1)


if __name__ == '__main__':
    main()
