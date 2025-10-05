#!/usr/bin/env python3
"""
Analysis Engine - My Name Is Claude Framework v3.5.0

Long-running analysis engine for security scanning, performance profiling,
and code quality analysis.

This is a TEMPLATE implementation. Actual implementation should:
1. Adapt to project-specific tools and requirements
2. Integrate with existing analysis systems
3. Follow project-specific analysis patterns
"""

import os
import sys
import json
import subprocess
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict
from datetime import datetime
import time
import re

logger = logging.getLogger(__name__)


@dataclass
class AnalysisResult:
    """Analysis result data"""
    analysis_type: str
    status: str  # success, warning, error
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    duration: float = 0.0
    findings: List[Dict[str, Any]] = field(default_factory=list)
    metrics: Dict[str, Any] = field(default_factory=dict)
    summary: str = ""
    recommendations: List[str] = field(default_factory=list)


class BaseAnalyzer:
    """Base class for analyzers"""

    def __init__(self, config: Dict):
        """
        Initialize analyzer

        Args:
            config: Analyzer configuration
        """
        self.config = config
        self.enabled = config.get('enabled', True)
        self.timeout = config.get('timeout_seconds', 600)

    def analyze(self) -> AnalysisResult:
        """
        Run analysis

        Returns:
            Analysis result
        """
        raise NotImplementedError

    def _run_command(
        self,
        command: List[str],
        timeout: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Run command and return output

        Args:
            command: Command to run
            timeout: Timeout in seconds

        Returns:
            Command result with stdout, stderr, exit_code
        """
        timeout = timeout or self.timeout

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=self._get_project_root()
            )

            return {
                'stdout': result.stdout,
                'stderr': result.stderr,
                'exit_code': result.returncode,
                'success': result.returncode == 0
            }
        except subprocess.TimeoutExpired:
            return {
                'stdout': '',
                'stderr': f'Command timed out after {timeout}s',
                'exit_code': -1,
                'success': False,
                'timeout': True
            }
        except Exception as e:
            return {
                'stdout': '',
                'stderr': str(e),
                'exit_code': -1,
                'success': False,
                'error': str(e)
            }

    def _get_project_root(self) -> Path:
        """Get project root directory"""
        current_dir = Path.cwd()
        markers = ['.git', '.claude', 'CLAUDE.md']

        while current_dir != current_dir.parent:
            for marker in markers:
                if (current_dir / marker).exists():
                    return current_dir
            current_dir = current_dir.parent

        return Path.cwd()

    def _find_files(self, patterns: List[str], exclude_patterns: List[str] = None) -> List[Path]:
        """Find files matching patterns"""
        exclude_patterns = exclude_patterns or []
        project_root = self._get_project_root()
        matches = []

        for pattern in patterns:
            for file_path in project_root.rglob(pattern):
                if file_path.is_file():
                    # Check exclusions
                    excluded = False
                    for exclude in exclude_patterns:
                        if exclude in str(file_path):
                            excluded = True
                            break

                    if not excluded:
                        matches.append(file_path)

        return matches


class SecurityAnalyzer(BaseAnalyzer):
    """Security vulnerability scanner"""

    def analyze(self) -> AnalysisResult:
        """Run security analysis"""
        start_time = time.time()
        result = AnalysisResult(
            analysis_type='security_scan',
            status='success'
        )

        try:
            # Detect available security tools
            tools_results = []

            # Try bandit for Python
            if self._has_python_files():
                bandit_result = self._run_bandit()
                if bandit_result:
                    tools_results.append(bandit_result)

            # Try npm audit for JavaScript/Node.js
            if self._has_node_project():
                npm_result = self._run_npm_audit()
                if npm_result:
                    tools_results.append(npm_result)

            # Try safety for Python dependencies
            if self._has_python_project():
                safety_result = self._run_safety()
                if safety_result:
                    tools_results.append(safety_result)

            # Aggregate results
            total_findings = 0
            severity_counts = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}

            for tool_result in tools_results:
                result.findings.extend(tool_result.get('findings', []))
                for finding in tool_result.get('findings', []):
                    severity = finding.get('severity', 'low').lower()
                    if severity in severity_counts:
                        severity_counts[severity] += 1
                    total_findings += 1

            # Determine overall status
            if severity_counts['critical'] > 0:
                result.status = 'error'
            elif severity_counts['high'] > 0:
                result.status = 'warning'

            # Generate summary
            result.summary = self._generate_security_summary(total_findings, severity_counts)
            result.metrics = {
                'total_findings': total_findings,
                'severity_counts': severity_counts,
                'tools_used': len(tools_results)
            }

            # Generate recommendations
            result.recommendations = self._generate_security_recommendations(severity_counts)

        except Exception as e:
            result.status = 'error'
            result.summary = f"Security analysis failed: {e}"
            logger.error(f"Security analysis error: {e}")

        finally:
            result.duration = time.time() - start_time

        return result

    def _has_python_files(self) -> bool:
        """Check if project has Python files"""
        return len(self._find_files(['*.py'])) > 0

    def _has_python_project(self) -> bool:
        """Check if project has Python dependency files"""
        project_root = self._get_project_root()
        return (
            (project_root / 'requirements.txt').exists() or
            (project_root / 'Pipfile').exists() or
            (project_root / 'pyproject.toml').exists()
        )

    def _has_node_project(self) -> bool:
        """Check if project has Node.js files"""
        project_root = self._get_project_root()
        return (project_root / 'package.json').exists()

    def _run_bandit(self) -> Optional[Dict]:
        """Run bandit security scanner"""
        cmd_result = self._run_command(['bandit', '-r', '.', '-f', 'json'])

        if not cmd_result['success']:
            logger.debug("Bandit not available or failed")
            return None

        try:
            output = json.loads(cmd_result['stdout'])
            findings = []

            for issue in output.get('results', []):
                findings.append({
                    'tool': 'bandit',
                    'severity': issue.get('issue_severity', 'LOW').lower(),
                    'confidence': issue.get('issue_confidence', 'LOW'),
                    'message': issue.get('issue_text', ''),
                    'file': issue.get('filename', ''),
                    'line': issue.get('line_number', 0),
                    'code': issue.get('code', '')
                })

            return {'findings': findings}
        except Exception as e:
            logger.error(f"Failed to parse bandit output: {e}")
            return None

    def _run_npm_audit(self) -> Optional[Dict]:
        """Run npm audit"""
        cmd_result = self._run_command(['npm', 'audit', '--json'])

        if not cmd_result['success'] and not cmd_result.get('stdout'):
            logger.debug("npm audit not available or failed")
            return None

        try:
            output = json.loads(cmd_result['stdout'])
            findings = []

            vulnerabilities = output.get('vulnerabilities', {})
            for pkg_name, vuln_data in vulnerabilities.items():
                findings.append({
                    'tool': 'npm-audit',
                    'severity': vuln_data.get('severity', 'low'),
                    'package': pkg_name,
                    'message': vuln_data.get('via', [{}])[0].get('title', 'Vulnerability found'),
                    'current_version': vuln_data.get('range', ''),
                    'fixed_version': vuln_data.get('fixAvailable', {}).get('version', 'N/A')
                })

            return {'findings': findings}
        except Exception as e:
            logger.error(f"Failed to parse npm audit output: {e}")
            return None

    def _run_safety(self) -> Optional[Dict]:
        """Run safety check for Python dependencies"""
        cmd_result = self._run_command(['safety', 'check', '--json'])

        if not cmd_result['success']:
            logger.debug("Safety not available or failed")
            return None

        try:
            output = json.loads(cmd_result['stdout'])
            findings = []

            for issue in output:
                findings.append({
                    'tool': 'safety',
                    'severity': 'high' if issue.get('is_high', False) else 'medium',
                    'package': issue.get('package', ''),
                    'message': issue.get('advisory', ''),
                    'vulnerable_versions': issue.get('vulnerable_spec', ''),
                    'fixed_version': issue.get('fixed_in', ['N/A'])[0]
                })

            return {'findings': findings}
        except Exception as e:
            logger.error(f"Failed to parse safety output: {e}")
            return None

    def _generate_security_summary(self, total: int, severity_counts: Dict) -> str:
        """Generate security scan summary"""
        if total == 0:
            return "✅ No security vulnerabilities found"

        parts = [f"Found {total} security issue{'s' if total != 1 else ''}:"]

        for severity in ['critical', 'high', 'medium', 'low']:
            count = severity_counts[severity]
            if count > 0:
                emoji = {'critical': '🚨', 'high': '❌', 'medium': '⚠️', 'low': 'ℹ️'}
                parts.append(f"{emoji[severity]} {count} {severity}")

        return ' '.join(parts)

    def _generate_security_recommendations(self, severity_counts: Dict) -> List[str]:
        """Generate security recommendations"""
        recommendations = []

        if severity_counts['critical'] > 0:
            recommendations.append("CRITICAL: Address critical vulnerabilities immediately")

        if severity_counts['high'] > 0:
            recommendations.append("Update vulnerable dependencies to patched versions")

        if severity_counts['medium'] > 0 or severity_counts['low'] > 0:
            recommendations.append("Review and plan fixes for medium/low severity issues")

        if sum(severity_counts.values()) == 0:
            recommendations.append("Continue regular security scans")

        return recommendations


class PerformanceAnalyzer(BaseAnalyzer):
    """Performance profiling and analysis"""

    def analyze(self) -> AnalysisResult:
        """Run performance analysis"""
        start_time = time.time()
        result = AnalysisResult(
            analysis_type='performance_profile',
            status='success'
        )

        try:
            # Analyze code complexity
            complexity_result = self._analyze_complexity()
            if complexity_result:
                result.findings.extend(complexity_result.get('findings', []))
                result.metrics.update(complexity_result.get('metrics', {}))

            # Analyze file sizes
            size_result = self._analyze_file_sizes()
            if size_result:
                result.findings.extend(size_result.get('findings', []))
                result.metrics.update(size_result.get('metrics', {}))

            # Generate summary
            total_issues = len(result.findings)
            result.summary = f"Performance analysis found {total_issues} issue{'s' if total_issues != 1 else ''}"

            if total_issues > 10:
                result.status = 'warning'

            # Generate recommendations
            result.recommendations = self._generate_performance_recommendations(result.findings)

        except Exception as e:
            result.status = 'error'
            result.summary = f"Performance analysis failed: {e}"
            logger.error(f"Performance analysis error: {e}")

        finally:
            result.duration = time.time() - start_time

        return result

    def _analyze_complexity(self) -> Optional[Dict]:
        """Analyze code complexity"""
        try:
            # Try radon for Python files
            python_files = self._find_files(['*.py'], ['venv', '.venv', 'node_modules'])

            if not python_files:
                return None

            findings = []
            total_complexity = 0
            file_count = 0

            for file_path in python_files:
                # Run radon complexity analysis
                cmd_result = self._run_command(['radon', 'cc', str(file_path), '-j'])

                if cmd_result['success']:
                    try:
                        complexity_data = json.loads(cmd_result['stdout'])

                        for func_data in complexity_data.get(str(file_path), []):
                            complexity = func_data.get('complexity', 0)
                            total_complexity += complexity

                            if complexity > 10:  # High complexity threshold
                                findings.append({
                                    'type': 'high_complexity',
                                    'file': str(file_path),
                                    'function': func_data.get('name', ''),
                                    'complexity': complexity,
                                    'line': func_data.get('lineno', 0)
                                })

                        file_count += 1
                    except:
                        pass

            avg_complexity = total_complexity / file_count if file_count > 0 else 0

            return {
                'findings': findings,
                'metrics': {
                    'average_complexity': round(avg_complexity, 2),
                    'files_analyzed': file_count
                }
            }
        except Exception as e:
            logger.debug(f"Complexity analysis failed: {e}")
            return None

    def _analyze_file_sizes(self) -> Optional[Dict]:
        """Analyze file sizes"""
        try:
            code_files = self._find_files(
                ['*.py', '*.js', '*.ts', '*.java', '*.cpp', '*.c'],
                ['venv', '.venv', 'node_modules', 'dist', 'build']
            )

            findings = []
            total_size = 0
            large_file_threshold = 1000  # lines

            for file_path in code_files:
                try:
                    with open(file_path, 'r') as f:
                        line_count = sum(1 for _ in f)

                    total_size += line_count

                    if line_count > large_file_threshold:
                        findings.append({
                            'type': 'large_file',
                            'file': str(file_path),
                            'lines': line_count,
                            'recommendation': 'Consider splitting into smaller modules'
                        })
                except:
                    pass

            avg_size = total_size / len(code_files) if code_files else 0

            return {
                'findings': findings,
                'metrics': {
                    'total_code_files': len(code_files),
                    'average_file_size': round(avg_size, 0),
                    'total_lines': total_size
                }
            }
        except Exception as e:
            logger.debug(f"File size analysis failed: {e}")
            return None

    def _generate_performance_recommendations(self, findings: List[Dict]) -> List[str]:
        """Generate performance recommendations"""
        recommendations = []

        high_complexity = sum(1 for f in findings if f.get('type') == 'high_complexity')
        large_files = sum(1 for f in findings if f.get('type') == 'large_file')

        if high_complexity > 0:
            recommendations.append(f"Refactor {high_complexity} high-complexity function{'s' if high_complexity != 1 else ''}")

        if large_files > 0:
            recommendations.append(f"Split {large_files} large file{'s' if large_files != 1 else ''} into smaller modules")

        if not findings:
            recommendations.append("Code structure looks good, maintain current practices")

        return recommendations


class CodeAnalyzer(BaseAnalyzer):
    """Code quality and style analysis"""

    def analyze(self) -> AnalysisResult:
        """Run code analysis"""
        start_time = time.time()
        result = AnalysisResult(
            analysis_type='code_analysis',
            status='success'
        )

        try:
            # Run linters based on project type
            tools_results = []

            if self._has_python_files():
                pylint_result = self._run_pylint()
                if pylint_result:
                    tools_results.append(pylint_result)

            if self._has_javascript_files():
                eslint_result = self._run_eslint()
                if eslint_result:
                    tools_results.append(eslint_result)

            # Aggregate results
            total_issues = 0
            severity_counts = {'error': 0, 'warning': 0, 'info': 0}

            for tool_result in tools_results:
                result.findings.extend(tool_result.get('findings', []))
                for finding in tool_result.get('findings', []):
                    severity = finding.get('severity', 'info').lower()
                    if severity in severity_counts:
                        severity_counts[severity] += 1
                    total_issues += 1

            # Determine overall status
            if severity_counts['error'] > 10:
                result.status = 'error'
            elif severity_counts['warning'] > 20:
                result.status = 'warning'

            # Generate summary
            result.summary = f"Code analysis found {total_issues} issue{'s' if total_issues != 1 else ''}"
            result.metrics = {
                'total_issues': total_issues,
                'severity_counts': severity_counts,
                'tools_used': len(tools_results)
            }

            # Generate recommendations
            result.recommendations = self._generate_code_recommendations(severity_counts)

        except Exception as e:
            result.status = 'error'
            result.summary = f"Code analysis failed: {e}"
            logger.error(f"Code analysis error: {e}")

        finally:
            result.duration = time.time() - start_time

        return result

    def _has_python_files(self) -> bool:
        """Check if project has Python files"""
        return len(self._find_files(['*.py'])) > 0

    def _has_javascript_files(self) -> bool:
        """Check if project has JavaScript files"""
        return len(self._find_files(['*.js', '*.jsx', '*.ts', '*.tsx'])) > 0

    def _run_pylint(self) -> Optional[Dict]:
        """Run pylint"""
        cmd_result = self._run_command(['pylint', '.', '--output-format=json'])

        if not cmd_result['success'] and not cmd_result.get('stdout'):
            logger.debug("Pylint not available or failed")
            return None

        try:
            output = json.loads(cmd_result['stdout']) if cmd_result['stdout'] else []
            findings = []

            for issue in output:
                findings.append({
                    'tool': 'pylint',
                    'severity': issue.get('type', 'info'),
                    'message': issue.get('message', ''),
                    'file': issue.get('path', ''),
                    'line': issue.get('line', 0),
                    'column': issue.get('column', 0),
                    'symbol': issue.get('symbol', '')
                })

            return {'findings': findings}
        except Exception as e:
            logger.error(f"Failed to parse pylint output: {e}")
            return None

    def _run_eslint(self) -> Optional[Dict]:
        """Run eslint"""
        cmd_result = self._run_command(['eslint', '.', '--format=json'])

        if not cmd_result['success'] and not cmd_result.get('stdout'):
            logger.debug("ESLint not available or failed")
            return None

        try:
            output = json.loads(cmd_result['stdout']) if cmd_result['stdout'] else []
            findings = []

            for file_result in output:
                for message in file_result.get('messages', []):
                    severity_map = {1: 'warning', 2: 'error'}
                    findings.append({
                        'tool': 'eslint',
                        'severity': severity_map.get(message.get('severity', 1), 'info'),
                        'message': message.get('message', ''),
                        'file': file_result.get('filePath', ''),
                        'line': message.get('line', 0),
                        'column': message.get('column', 0),
                        'rule': message.get('ruleId', '')
                    })

            return {'findings': findings}
        except Exception as e:
            logger.error(f"Failed to parse eslint output: {e}")
            return None

    def _generate_code_recommendations(self, severity_counts: Dict) -> List[str]:
        """Generate code quality recommendations"""
        recommendations = []

        if severity_counts['error'] > 0:
            recommendations.append(f"Fix {severity_counts['error']} error{'s' if severity_counts['error'] != 1 else ''}")

        if severity_counts['warning'] > 10:
            recommendations.append("Address high number of warnings to improve code quality")

        if sum(severity_counts.values()) == 0:
            recommendations.append("Code quality looks good, maintain current standards")

        return recommendations


class AnalysisEngine:
    """
    Main analysis engine coordinating all analyzers
    """

    def __init__(self, config: Dict):
        """
        Initialize analysis engine

        Args:
            config: Analysis engine configuration
        """
        self.config = config
        self.task_types_config = config.get('task_types', {})

        # Initialize analyzers
        self.analyzers = {
            'security_scan': SecurityAnalyzer(
                self.task_types_config.get('security_scan', {})
            ),
            'performance_profile': PerformanceAnalyzer(
                self.task_types_config.get('performance_profile', {})
            ),
            'code_analysis': CodeAnalyzer(
                self.task_types_config.get('code_analysis', {})
            )
        }

    def run_analysis(self, analysis_type: str) -> Optional[AnalysisResult]:
        """
        Run specific analysis

        Args:
            analysis_type: Type of analysis to run

        Returns:
            Analysis result or None if analyzer not found
        """
        analyzer = self.analyzers.get(analysis_type)
        if not analyzer:
            logger.error(f"Unknown analysis type: {analysis_type}")
            return None

        if not analyzer.enabled:
            logger.info(f"Analyzer {analysis_type} is disabled")
            return None

        logger.info(f"Running {analysis_type}...")
        result = analyzer.analyze()
        logger.info(f"Completed {analysis_type}: {result.summary}")

        return result

    def run_all_analyses(self) -> Dict[str, AnalysisResult]:
        """
        Run all enabled analyses

        Returns:
            Dictionary of analysis results
        """
        results = {}

        for analysis_type, analyzer in self.analyzers.items():
            if analyzer.enabled:
                result = self.run_analysis(analysis_type)
                if result:
                    results[analysis_type] = result

        return results


def main():
    """CLI for analysis engine testing"""
    import argparse

    parser = argparse.ArgumentParser(description='Analysis Engine')
    parser.add_argument('analysis_type', choices=['security', 'performance', 'code', 'all'])
    parser.add_argument('--config', help='Configuration file path')
    parser.add_argument('--output', help='Output file for results')

    args = parser.parse_args()

    # Load config
    if args.config and Path(args.config).exists():
        with open(args.config, 'r') as f:
            config = json.load(f)
    else:
        config = {}

    # Create engine
    engine = AnalysisEngine(config)

    # Run analysis
    if args.analysis_type == 'all':
        results = engine.run_all_analyses()
    else:
        type_map = {
            'security': 'security_scan',
            'performance': 'performance_profile',
            'code': 'code_analysis'
        }
        result = engine.run_analysis(type_map[args.analysis_type])
        results = {type_map[args.analysis_type]: result} if result else {}

    # Output results
    output_data = {
        type_name: asdict(result)
        for type_name, result in results.items()
    }

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(output_data, f, indent=2)
        print(f"Results saved to {args.output}")
    else:
        print(json.dumps(output_data, indent=2))


if __name__ == '__main__':
    main()
