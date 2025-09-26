#!/usr/bin/env python3
"""
Claude Code Framework Terminology Consistency Checker
Interactive system for terminology validation and consistency enforcement
"""

import os
import re
import json
import yaml
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, asdict
from pathlib import Path
import difflib

@dataclass
class TerminologyIssue:
    """Individual terminology issue found in content"""
    file_path: str
    line_number: int
    issue_type: str
    incorrect_term: str
    correct_term: str
    context: str
    severity: str
    suggestion: str

@dataclass
class TerminologyReport:
    """Comprehensive terminology consistency report"""
    analysis_date: datetime
    files_analyzed: int
    issues_found: int

    # Issue categorization
    critical_issues: List[TerminologyIssue]
    warning_issues: List[TerminologyIssue]
    suggestion_issues: List[TerminologyIssue]

    # Statistics
    consistency_score: float
    most_common_issues: List[Tuple[str, int]]
    terminology_coverage: float

    # Recommendations
    standardization_recommendations: List[str]
    training_topics: List[str]

class FrameworkTerminology:
    """Framework terminology definitions and relationships"""

    def __init__(self):
        self.terms = self._load_terminology_database()
        self.synonyms = self._load_synonym_mappings()
        self.deprecated_terms = self._load_deprecated_terms()
        self.domain_specific = self._load_domain_specific_terms()

    def _load_terminology_database(self) -> Dict[str, Dict[str, Any]]:
        """Load comprehensive terminology database"""
        return {
            # Core Framework Terms
            "agent": {
                "definition": "Specialized AI assistant with domain-specific expertise",
                "correct_forms": ["agent", "agents", "Agent"],
                "incorrect_forms": ["bot", "assistant", "AI helper", "chatbot"],
                "context": "framework_core",
                "examples": ["frontend-engineer agent", "45 agents total"],
                "related_terms": ["agent binding", "agent coordination", "multi-agent system"]
            },
            "agent binding": {
                "definition": "Automatic activation and association of agents with corresponding prompts",
                "correct_forms": ["agent binding", "agent-prompt binding", "binding"],
                "incorrect_forms": ["agent linking", "agent connection", "agent association"],
                "context": "framework_core",
                "examples": ["agent binding system", "prompt-to-agent binding"],
                "related_terms": ["agent", "prompt library", "auto-activation"]
            },
            "claude.md": {
                "definition": "Central project configuration file",
                "correct_forms": ["CLAUDE.md", "Claude.md"],
                "incorrect_forms": ["claude.md", "Claude.MD", "claude-config", "config.md"],
                "context": "configuration",
                "examples": ["CLAUDE.md adaptation", "project CLAUDE.md"],
                "related_terms": ["project configuration", "framework adaptation"]
            },
            "todowrite": {
                "definition": "Hierarchical task management system",
                "correct_forms": ["TodoWrite", "TodoWrite integration"],
                "incorrect_forms": ["todo-write", "todoWrite", "todo_write", "TaskManager"],
                "context": "task_management",
                "examples": ["TodoWrite integration", "using TodoWrite"],
                "related_terms": ["task management", "agent coordination"]
            },
            "framework ecosystem": {
                "definition": "Complete integrated environment including agents, prompts, tools",
                "correct_forms": ["framework ecosystem", "ecosystem", "Framework Ecosystem"],
                "incorrect_forms": ["framework environment", "system ecosystem", "platform"],
                "context": "framework_core",
                "examples": ["framework ecosystem design", "ecosystem integration"],
                "related_terms": ["multi-agent system", "integrated environment"]
            },
            "quality gates": {
                "definition": "Systematic validation checkpoints ensuring quality",
                "correct_forms": ["quality gates", "Quality Gates", "quality gate"],
                "incorrect_forms": ["quality checks", "validation gates", "quality controls"],
                "context": "quality_assurance",
                "examples": ["quality gates validation", "implementing quality gates"],
                "related_terms": ["validation", "compliance", "quality assurance"]
            },
            "enterprise ready": {
                "definition": "Framework maturity suitable for Fortune 500 deployment",
                "correct_forms": ["Enterprise Ready", "enterprise-ready", "enterprise ready"],
                "incorrect_forms": ["enterprise grade", "business ready", "corporate ready"],
                "context": "business",
                "examples": ["Enterprise Ready framework", "enterprise-ready standards"],
                "related_terms": ["Fortune 500", "enterprise-grade", "production ready"]
            },
            "mcp tools": {
                "definition": "Model Context Protocol tools for enhanced functionality",
                "correct_forms": ["MCP tools", "MCP Tools", "MCP tool integration"],
                "incorrect_forms": ["mcp-tools", "MCP-tools", "model context tools"],
                "context": "integration",
                "examples": ["MCP tools integration", "Serena MCP tool"],
                "related_terms": ["Serena", "Context7", "Playwright", "tool integration"]
            },

            # Technical Architecture Terms
            "multi-agent system": {
                "definition": "Distributed AI architecture with multiple specialized agents",
                "correct_forms": ["multi-agent system", "Multi-Agent System", "multi-agent"],
                "incorrect_forms": ["multiple agent system", "agent cluster", "AI swarm"],
                "context": "architecture",
                "examples": ["multi-agent system design", "coordinated multi-agent"],
                "related_terms": ["agent coordination", "distributed system"]
            },
            "technology agnostic": {
                "definition": "Compatible across different technology stacks",
                "correct_forms": ["technology agnostic", "technology-agnostic", "tech-agnostic"],
                "incorrect_forms": ["technology neutral", "platform independent", "stack agnostic"],
                "context": "design_principle",
                "examples": ["technology agnostic design", "technology-agnostic approach"],
                "related_terms": ["hardcoding prevention", "cross-platform"]
            },
            "hardcoding prevention": {
                "definition": "Standard prohibiting fixed paths and technology assumptions",
                "correct_forms": ["hardcoding prevention", "hardcoding violations", "no hardcoding"],
                "incorrect_forms": ["hardcode prevention", "hard coding prevention", "static code prevention"],
                "context": "design_principle",
                "examples": ["hardcoding prevention rules", "avoiding hardcoding violations"],
                "related_terms": ["technology agnostic", "adaptable design"]
            },

            # Quality and Compliance Terms
            "compliance score": {
                "definition": "Quantitative measure of adherence to standards",
                "correct_forms": ["compliance score", "Compliance Score", "compliance rating"],
                "incorrect_forms": ["conformance score", "adherence score", "quality score"],
                "context": "quality_metrics",
                "examples": ["80% compliance score", "compliance score threshold"],
                "related_terms": ["quality metrics", "template compliance"]
            },
            "template compliance": {
                "definition": "Adherence to unified agent template structure",
                "correct_forms": ["template compliance", "Template Compliance", "template conformance"],
                "incorrect_forms": ["template adherence", "template matching", "format compliance"],
                "context": "quality_metrics",
                "examples": ["template compliance validation", "100% template compliance"],
                "related_terms": ["unified template", "agent template"]
            },

            # Business Terms
            "stakeholder management": {
                "definition": "Framework capability to address different user needs",
                "correct_forms": ["stakeholder management", "Stakeholder Management"],
                "incorrect_forms": ["user management", "client management", "customer management"],
                "context": "business",
                "examples": ["stakeholder management approach", "effective stakeholder management"],
                "related_terms": ["user types", "organizational roles"]
            },

            # Performance Terms
            "performance analytics": {
                "definition": "Monitoring system tracking framework effectiveness",
                "correct_forms": ["performance analytics", "Performance Analytics"],
                "incorrect_forms": ["performance monitoring", "analytics dashboard", "performance metrics"],
                "context": "monitoring",
                "examples": ["performance analytics dashboard", "comprehensive performance analytics"],
                "related_terms": ["monitoring", "analytics", "metrics"]
            }
        }

    def _load_synonym_mappings(self) -> Dict[str, str]:
        """Load mappings of acceptable synonyms to preferred terms"""
        return {
            "AI assistant": "agent",
            "chatbot": "agent",
            "bot": "agent",
            "task manager": "TodoWrite",
            "task management": "TodoWrite integration",
            "config file": "CLAUDE.md",
            "configuration": "CLAUDE.md",
            "quality check": "quality gate",
            "validation": "quality gate",
            "enterprise grade": "enterprise ready",
            "business ready": "enterprise ready",
            "tools integration": "MCP tools integration",
            "agent system": "multi-agent system",
            "platform agnostic": "technology agnostic",
            "cross-platform": "technology agnostic"
        }

    def _load_deprecated_terms(self) -> Dict[str, str]:
        """Load deprecated terms and their modern replacements"""
        return {
            "Claude AI assistant": "agent",
            "AI helper": "agent",
            "configuration file": "CLAUDE.md",
            "task list": "TodoWrite",
            "quality control": "quality gates",
            "enterprise grade": "enterprise ready",
            "tool integration": "MCP tools integration",
            "agent cluster": "multi-agent system",
            "hardcode prevention": "hardcoding prevention"
        }

    def _load_domain_specific_terms(self) -> Dict[str, List[str]]:
        """Load domain-specific terminology by category"""
        return {
            "agents": [
                "frontend-engineer", "backend-engineer", "security-engineer",
                "enterprise-architect", "session-manager", "qa-engineer"
            ],
            "mcp_tools": [
                "Serena", "Context7", "Playwright"
            ],
            "categories": [
                "Core Agents", "Enterprise Agents", "Custom Agents"
            ],
            "quality_metrics": [
                "compliance score", "quality gates", "template compliance"
            ]
        }

class TerminologyChecker:
    """Main terminology consistency checker"""

    def __init__(self, framework_root: str):
        self.framework_root = Path(framework_root)
        self.terminology = FrameworkTerminology()
        self.issues = []

        # File patterns to analyze
        self.include_patterns = [
            "**/*.md",
            "**/*.py",
            "**/*.json",
            "**/*.yml",
            "**/*.yaml"
        ]

        # Directories to exclude
        self.exclude_dirs = {
            ".git", "__pycache__", "node_modules", ".venv", "venv",
            "build", "dist", "target", ".cache"
        }

    def analyze_framework_terminology(self) -> TerminologyReport:
        """Analyze entire framework for terminology consistency"""
        print("🔍 Starting comprehensive terminology analysis...")

        # Discover files to analyze
        files_to_analyze = self._discover_files()
        print(f"📋 Found {len(files_to_analyze)} files to analyze")

        # Analyze each file
        all_issues = []
        files_analyzed = 0

        for file_path in files_to_analyze:
            try:
                issues = self._analyze_file(file_path)
                all_issues.extend(issues)
                files_analyzed += 1

                if issues:
                    print(f"⚠️  {file_path.name}: {len(issues)} terminology issues")
                else:
                    print(f"✅ {file_path.name}: No issues found")

            except Exception as e:
                print(f"❌ Error analyzing {file_path}: {e}")

        # Categorize issues
        critical_issues = [i for i in all_issues if i.severity == "critical"]
        warning_issues = [i for i in all_issues if i.severity == "warning"]
        suggestion_issues = [i for i in all_issues if i.severity == "suggestion"]

        # Calculate statistics
        consistency_score = self._calculate_consistency_score(all_issues, files_analyzed)
        most_common_issues = self._analyze_common_issues(all_issues)
        terminology_coverage = self._calculate_terminology_coverage(files_to_analyze)

        # Generate recommendations
        standardization_recommendations = self._generate_standardization_recommendations(all_issues)
        training_topics = self._identify_training_topics(all_issues)

        report = TerminologyReport(
            analysis_date=datetime.now(),
            files_analyzed=files_analyzed,
            issues_found=len(all_issues),
            critical_issues=critical_issues,
            warning_issues=warning_issues,
            suggestion_issues=suggestion_issues,
            consistency_score=consistency_score,
            most_common_issues=most_common_issues,
            terminology_coverage=terminology_coverage,
            standardization_recommendations=standardization_recommendations,
            training_topics=training_topics
        )

        print(f"""
🎯 Terminology Analysis Complete!
📊 Results Summary:
   • Files Analyzed: {files_analyzed}
   • Issues Found: {len(all_issues)}
   • Consistency Score: {consistency_score:.1f}%
   • Critical Issues: {len(critical_issues)}
   • Warning Issues: {len(warning_issues)}
""")

        return report

    def _discover_files(self) -> List[Path]:
        """Discover files to analyze based on patterns"""
        files = []

        for pattern in self.include_patterns:
            pattern_files = self.framework_root.glob(pattern)

            for file_path in pattern_files:
                # Skip excluded directories
                if any(excluded in str(file_path) for excluded in self.exclude_dirs):
                    continue

                # Skip hidden files
                if file_path.name.startswith('.') and file_path.name not in ['.claude']:
                    continue

                files.append(file_path)

        return sorted(set(files))

    def _analyze_file(self, file_path: Path) -> List[TerminologyIssue]:
        """Analyze single file for terminology issues"""
        issues = []

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
        except Exception:
            return issues

        for line_num, line in enumerate(lines, 1):
            line_issues = self._analyze_line(file_path, line_num, line)
            issues.extend(line_issues)

        return issues

    def _analyze_line(self, file_path: Path, line_num: int, line: str) -> List[TerminologyIssue]:
        """Analyze single line for terminology issues"""
        issues = []
        line_lower = line.lower()

        # Check for incorrect terms
        for term_name, term_data in self.terminology.terms.items():
            incorrect_forms = term_data.get("incorrect_forms", [])
            correct_forms = term_data.get("correct_forms", [])

            for incorrect in incorrect_forms:
                if incorrect.lower() in line_lower:
                    # Find the best correct form to suggest
                    correct_term = correct_forms[0] if correct_forms else term_name

                    issue = TerminologyIssue(
                        file_path=str(file_path),
                        line_number=line_num,
                        issue_type="incorrect_term",
                        incorrect_term=incorrect,
                        correct_term=correct_term,
                        context=line.strip(),
                        severity="warning",
                        suggestion=f"Replace '{incorrect}' with '{correct_term}'"
                    )
                    issues.append(issue)

        # Check for deprecated terms
        for deprecated, replacement in self.terminology.deprecated_terms.items():
            if deprecated.lower() in line_lower:
                issue = TerminologyIssue(
                    file_path=str(file_path),
                    line_number=line_num,
                    issue_type="deprecated_term",
                    incorrect_term=deprecated,
                    correct_term=replacement,
                    context=line.strip(),
                    severity="critical",
                    suggestion=f"Update deprecated term '{deprecated}' to '{replacement}'"
                )
                issues.append(issue)

        # Check for inconsistent capitalization
        self._check_capitalization_consistency(file_path, line_num, line, issues)

        return issues

    def _check_capitalization_consistency(self, file_path: Path, line_num: int,
                                        line: str, issues: List[TerminologyIssue]):
        """Check for inconsistent capitalization of key terms"""
        capitalization_rules = {
            "todowrite": "TodoWrite",
            "claude.md": "CLAUDE.md",
            "mcp tools": "MCP tools",
            "enterprise ready": "Enterprise Ready",
            "quality gates": "Quality Gates"
        }

        for incorrect, correct in capitalization_rules.items():
            # Check for exact match with wrong capitalization
            if incorrect in line and correct not in line:
                issue = TerminologyIssue(
                    file_path=str(file_path),
                    line_number=line_num,
                    issue_type="capitalization",
                    incorrect_term=incorrect,
                    correct_term=correct,
                    context=line.strip(),
                    severity="suggestion",
                    suggestion=f"Use consistent capitalization: '{correct}'"
                )
                issues.append(issue)

    def _calculate_consistency_score(self, all_issues: List[TerminologyIssue],
                                   files_analyzed: int) -> float:
        """Calculate overall terminology consistency score"""
        if files_analyzed == 0:
            return 100.0

        # Weight issues by severity
        severity_weights = {"critical": 10, "warning": 5, "suggestion": 1}

        total_penalty = sum(
            severity_weights.get(issue.severity, 1)
            for issue in all_issues
        )

        # Calculate score (higher penalty = lower score)
        max_possible_penalty = files_analyzed * 10  # Assume max 10 critical issues per file
        score = max(0, 100 - (total_penalty / max_possible_penalty * 100))

        return round(score, 1)

    def _analyze_common_issues(self, all_issues: List[TerminologyIssue]) -> List[Tuple[str, int]]:
        """Identify most common terminology issues"""
        issue_counter = {}

        for issue in all_issues:
            key = f"{issue.issue_type}: {issue.incorrect_term} → {issue.correct_term}"
            issue_counter[key] = issue_counter.get(key, 0) + 1

        return sorted(issue_counter.items(), key=lambda x: x[1], reverse=True)[:10]

    def _calculate_terminology_coverage(self, files_analyzed: List[Path]) -> float:
        """Calculate how well framework terminology is covered in documentation"""
        # Simplified calculation - in real implementation would be more sophisticated
        terminology_files = [
            f for f in files_analyzed
            if any(term in str(f).lower() for term in ["glossary", "terminology", "definitions"])
        ]

        coverage = min(100, len(terminology_files) * 25)  # Simplified scoring
        return coverage

    def _generate_standardization_recommendations(self, all_issues: List[TerminologyIssue]) -> List[str]:
        """Generate recommendations for terminology standardization"""
        recommendations = []

        # Count critical issues
        critical_count = len([i for i in all_issues if i.severity == "critical"])
        if critical_count > 0:
            recommendations.append(f"Address {critical_count} critical terminology issues immediately")

        # Check for common patterns
        common_issues = self._analyze_common_issues(all_issues)
        if common_issues:
            top_issue = common_issues[0]
            recommendations.append(f"Focus on most common issue: {top_issue[0]} ({top_issue[1]} occurrences)")

        # General recommendations
        recommendations.extend([
            "Implement automated terminology validation in CI/CD pipeline",
            "Create terminology training materials for team members",
            "Establish terminology review process for new content",
            "Regular terminology consistency audits (monthly)"
        ])

        return recommendations

    def _identify_training_topics(self, all_issues: List[TerminologyIssue]) -> List[str]:
        """Identify topics that need training focus"""
        training_topics = []

        # Analyze issue patterns
        issue_types = {}
        for issue in all_issues:
            category = issue.issue_type
            issue_types[category] = issue_types.get(category, 0) + 1

        # Generate training topics based on common issues
        if issue_types.get("incorrect_term", 0) > 5:
            training_topics.append("Correct terminology usage and preferred terms")

        if issue_types.get("deprecated_term", 0) > 0:
            training_topics.append("Modern framework terminology (avoiding deprecated terms)")

        if issue_types.get("capitalization", 0) > 3:
            training_topics.append("Consistent capitalization standards")

        # Add general topics
        training_topics.extend([
            "Framework glossary navigation and usage",
            "Technology-agnostic language principles",
            "Enterprise-grade terminology standards"
        ])

        return training_topics

    def generate_terminology_report(self, report: TerminologyReport, output_file: str):
        """Generate comprehensive terminology consistency report"""

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"""# Framework Terminology Consistency Report

## Executive Summary
- **Analysis Date**: {report.analysis_date.strftime('%Y-%m-%d %H:%M:%S')}
- **Files Analyzed**: {report.files_analyzed}
- **Issues Found**: {report.issues_found}
- **Consistency Score**: {report.consistency_score:.1f}%
- **Terminology Coverage**: {report.terminology_coverage:.1f}%

## Issue Breakdown
- **Critical Issues**: {len(report.critical_issues)} (require immediate attention)
- **Warning Issues**: {len(report.warning_issues)} (should be addressed)
- **Suggestions**: {len(report.suggestion_issues)} (improvements)

## Most Common Issues
""")
            for issue, count in report.most_common_issues:
                f.write(f"- {issue}: {count} occurrences\n")

            f.write(f"""
## Critical Issues Requiring Immediate Attention
""")
            for issue in report.critical_issues:
                f.write(f"- **{Path(issue.file_path).name}:{issue.line_number}**: {issue.suggestion}\n")
                f.write(f"  Context: `{issue.context}`\n")

            f.write(f"""
## Standardization Recommendations
""")
            for rec in report.standardization_recommendations:
                f.write(f"- {rec}\n")

            f.write(f"""
## Training Topics Needed
""")
            for topic in report.training_topics:
                f.write(f"- {topic}\n")

            f.write(f"""
## Implementation Plan

### Phase 1: Critical Issues (Week 1)
- Fix all {len(report.critical_issues)} critical terminology issues
- Update deprecated terms throughout framework
- Establish terminology validation automation

### Phase 2: Warning Issues (Week 2-3)
- Address {len(report.warning_issues)} warning-level inconsistencies
- Standardize terminology across documentation
- Implement terminology training program

### Phase 3: Optimization (Week 4)
- Apply {len(report.suggestion_issues)} improvement suggestions
- Enhance terminology coverage
- Establish ongoing consistency monitoring

---
*Report generated by Claude Code Framework Terminology Checker*
""")

def main():
    """Main execution function"""
    framework_root = "/mnt/e/AI/my_name_is_claude"

    print("🚀 Starting Framework Terminology Analysis")
    print("=" * 60)

    # Initialize checker
    checker = TerminologyChecker(framework_root)

    # Perform analysis
    report = checker.analyze_framework_terminology()

    # Generate report
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_file = f"{framework_root}/.claude/monitoring/quality/terminology-consistency-{timestamp}.md"
    checker.generate_terminology_report(report, report_file)

    # Export JSON for automation
    json_file = f"{framework_root}/.claude/monitoring/quality/terminology-consistency-{timestamp}.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(asdict(report), f, indent=2, default=str)

    print(f"""
📁 Analysis Complete!
📊 Report Generated: {report_file}
📋 JSON Data: {json_file}
""")

    return report

if __name__ == "__main__":
    main()