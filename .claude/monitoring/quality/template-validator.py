#!/usr/bin/env python3
"""
Claude Code Framework Template Validator
Automated validation system for agent template compliance
"""

import os
import re
import json
import yaml
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class ValidationResult:
    """Result of template validation for a single agent"""
    agent_name: str
    file_path: str
    is_compliant: bool
    compliance_score: float

    # Section validation
    missing_sections: List[str]
    incomplete_sections: List[str]
    malformed_sections: List[str]

    # Content validation
    content_issues: List[str]
    format_issues: List[str]
    integration_issues: List[str]

    # Recommendations
    critical_fixes: List[str]
    improvements: List[str]

    # Metadata
    validation_date: datetime
    template_version: str

@dataclass
class ValidationSummary:
    """Summary of validation results across all agents"""
    total_agents: int
    compliant_agents: int
    compliance_rate: float
    average_score: float

    critical_issues: int
    warning_issues: int
    info_issues: int

    validation_date: datetime
    template_version: str

    category_results: Dict[str, Dict[str, Any]]
    top_issues: List[Tuple[str, int]]  # (issue_type, count)

class TemplateValidator:
    """Main template validation engine"""

    def __init__(self, framework_root: str):
        self.framework_root = Path(framework_root)
        self.agents_dir = self.framework_root / ".claude/agents"
        self.template_file = self.framework_root / ".claude/templates/agent_template.md"

        # Load validation rules
        self.validation_rules = self._load_validation_rules()
        self.template_version = "1.0"

        # Required sections from unified template
        self.required_sections = [
            "Core Competencies",
            "Approach",
            "Key Responsibilities",
            "Performance Standards",
            "Collaboration",
            "Integration",
            "Quality Gates"
        ]

        # Required subsections for comprehensive validation
        self.required_subsections = {
            "Core Competencies": ["Primary Expertise", "Domain Knowledge", "Technical Proficiencies"],
            "Approach": ["Methodology Framework", "Decision-Making Framework"],
            "Key Responsibilities": ["Primary Deliverables", "Quality Assurance", "Collaboration Requirements"],
            "Performance Standards": ["Success Metrics", "Timeline Expectations", "Quality Gates"],
            "Collaboration": ["Agent Coordination Patterns", "Handoff Procedures"],
            "Integration": ["TodoWrite Integration", "CLAUDE.md Adaptation", "MCP Tools Integration"],
            "Quality Gates": ["Input Validation", "Process Quality", "Output Validation"]
        }

        # Critical integration keywords
        self.integration_keywords = {
            "todowrite": ["TodoWrite", "task management", "hierarchical task"],
            "claude_md": ["CLAUDE.md", "project configuration", "project metadata"],
            "mcp_tools": ["MCP tools", "Serena", "Context7", "Playwright"],
            "agent_coordination": ["agent coordination", "handoff", "collaboration", "cross-agent"]
        }

    def _load_validation_rules(self) -> Dict[str, Any]:
        """Load validation rules from configuration"""
        return {
            "minimum_compliance_score": 80,
            "minimum_section_word_count": 50,
            "required_experience_mention": "10+ years",
            "required_language": "english",
            "max_heading_levels": 3,
            "required_integration_features": 4,
            "minimum_competencies": 3,
            "minimum_deliverables": 3
        }

    def validate_all_agents(self) -> ValidationSummary:
        """Validate all agents against the unified template"""
        print("🔍 Starting comprehensive template validation...")

        # Discover all agent files
        agent_files = self._discover_agent_files()
        print(f"📋 Found {len(agent_files)} agents to validate")

        # Validate each agent
        validation_results = []
        for agent_file in agent_files:
            try:
                result = self.validate_agent(agent_file)
                validation_results.append(result)

                status = "✅ PASS" if result.is_compliant else "❌ FAIL"
                print(f"{status} {result.agent_name}: {result.compliance_score:.1f}% ({len(result.critical_fixes)} critical issues)")

            except Exception as e:
                print(f"❌ ERROR validating {agent_file}: {e}")

        # Generate summary
        summary = self._generate_validation_summary(validation_results)

        print(f"""
🎯 Validation Complete!
📊 Results Summary:
   • Compliant Agents: {summary.compliant_agents}/{summary.total_agents} ({summary.compliance_rate:.1f}%)
   • Average Score: {summary.average_score:.1f}%
   • Critical Issues: {summary.critical_issues}
   • Warning Issues: {summary.warning_issues}
""")

        return summary

    def validate_agent(self, agent_file: Path) -> ValidationResult:
        """Validate a single agent file against the template"""

        agent_name = agent_file.stem

        # Read agent content
        try:
            with open(agent_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            raise Exception(f"Failed to read agent file: {e}")

        # Initialize validation tracking
        missing_sections = []
        incomplete_sections = []
        malformed_sections = []
        content_issues = []
        format_issues = []
        integration_issues = []
        critical_fixes = []
        improvements = []

        # Validate structure
        structure_score = self._validate_structure(
            content, missing_sections, incomplete_sections, malformed_sections
        )

        # Validate content quality
        content_score = self._validate_content_quality(
            content, content_issues, improvements
        )

        # Validate format compliance
        format_score = self._validate_format_compliance(
            content, format_issues, critical_fixes
        )

        # Validate integration features
        integration_score = self._validate_integration_features(
            content, integration_issues, critical_fixes
        )

        # Calculate overall compliance score
        compliance_score = (
            structure_score * 0.40 +
            content_score * 0.30 +
            format_score * 0.15 +
            integration_score * 0.15
        )

        # Determine compliance status
        is_compliant = (
            compliance_score >= self.validation_rules["minimum_compliance_score"] and
            len(critical_fixes) == 0
        )

        return ValidationResult(
            agent_name=agent_name,
            file_path=str(agent_file),
            is_compliant=is_compliant,
            compliance_score=compliance_score,
            missing_sections=missing_sections,
            incomplete_sections=incomplete_sections,
            malformed_sections=malformed_sections,
            content_issues=content_issues,
            format_issues=format_issues,
            integration_issues=integration_issues,
            critical_fixes=critical_fixes,
            improvements=improvements,
            validation_date=datetime.now(),
            template_version=self.template_version
        )

    def _validate_structure(self, content: str, missing_sections: List[str],
                          incomplete_sections: List[str], malformed_sections: List[str]) -> float:
        """Validate template structure compliance"""

        section_scores = []

        # Check for agent title
        if not re.search(r'^# .+', content, re.MULTILINE):
            missing_sections.append("Agent Title")
            section_scores.append(0)
        else:
            section_scores.append(100)

        # Check required sections
        for section in self.required_sections:
            section_pattern = rf'^## {re.escape(section)}'

            if not re.search(section_pattern, content, re.MULTILINE):
                missing_sections.append(section)
                section_scores.append(0)
                continue

            # Extract section content
            section_content = self._extract_section_content(content, section)

            # Check if section has sufficient content
            word_count = len(section_content.split())
            min_words = self.validation_rules["minimum_section_word_count"]

            if word_count < min_words:
                incomplete_sections.append(f"{section} ({word_count} words, minimum {min_words})")
                section_scores.append(50)
            else:
                section_scores.append(100)

            # Check for required subsections
            if section in self.required_subsections:
                for subsection in self.required_subsections[section]:
                    if subsection not in section_content:
                        malformed_sections.append(f"{section} missing {subsection}")

        return sum(section_scores) / len(section_scores) if section_scores else 0

    def _validate_content_quality(self, content: str, content_issues: List[str],
                                improvements: List[str]) -> float:
        """Validate content quality and depth"""

        quality_score = 100

        # Check for experience requirement
        if "10+ years" not in content and "decade" not in content.lower():
            content_issues.append("Missing 10+ years experience requirement")
            quality_score -= 20

        # Check for specific technical skills
        competencies_section = self._extract_section_content(content, "Core Competencies")
        if competencies_section:
            # Count specific technologies/skills mentioned
            tech_patterns = [
                r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b',  # Technology names
                r'\b[A-Z]{2,}\b',  # Acronyms
            ]

            tech_count = sum(len(re.findall(pattern, competencies_section)) for pattern in tech_patterns)

            if tech_count < 5:
                content_issues.append(f"Insufficient technical details ({tech_count} items, minimum 5)")
                quality_score -= 15

        # Check for measurable criteria in Performance Standards
        performance_section = self._extract_section_content(content, "Performance Standards")
        if performance_section:
            measurable_indicators = ["metric", "measure", "KPI", "target", "benchmark", "%", "seconds", "hours"]
            measurable_count = sum(1 for indicator in measurable_indicators if indicator.lower() in performance_section.lower())

            if measurable_count < 3:
                content_issues.append("Performance Standards lack measurable criteria")
                quality_score -= 10

        # Check for enterprise-grade language
        enterprise_indicators = ["enterprise", "scalable", "production", "compliance", "governance"]
        enterprise_count = sum(1 for indicator in enterprise_indicators if indicator.lower() in content.lower())

        if enterprise_count < 2:
            improvements.append("Add more enterprise-focused language and concepts")
            quality_score -= 5

        return max(0, quality_score)

    def _validate_format_compliance(self, content: str, format_issues: List[str],
                                  critical_fixes: List[str]) -> float:
        """Validate format and language compliance"""

        format_score = 100

        # Check language compliance (simplified)
        non_english_patterns = [
            r'[ążśćęłóń]',  # Polish diacritics
            r'[àáâãäåæçèéêëìíîïñòóôõöøùúûüý]',  # Other diacritics
        ]

        for pattern in non_english_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                critical_fixes.append("Convert all content to English")
                format_score -= 30
                break

        # Check heading hierarchy
        headings = re.findall(r'^(#{1,6})', content, re.MULTILINE)
        max_heading_level = max(len(h) for h in headings) if headings else 0

        if max_heading_level > self.validation_rules["max_heading_levels"]:
            format_issues.append(f"Excessive heading levels ({max_heading_level}, maximum {self.validation_rules['max_heading_levels']})")
            format_score -= 10

        # Check for proper markdown formatting
        if content.count('**') % 2 != 0:
            format_issues.append("Unmatched bold formatting markers")
            format_score -= 5

        if content.count('*') % 2 != 0:
            format_issues.append("Unmatched italic formatting markers")
            format_score -= 5

        # Check for proper list formatting
        if re.search(r'^\d+\.\s', content, re.MULTILINE) and not re.search(r'^-\s', content, re.MULTILINE):
            improvements.append("Consider using bullet points for better readability")

        return max(0, format_score)

    def _validate_integration_features(self, content: str, integration_issues: List[str],
                                     critical_fixes: List[str]) -> float:
        """Validate framework integration features"""

        integration_score = 0
        content_lower = content.lower()

        # Check each integration category
        for category, keywords in self.integration_keywords.items():
            found = any(keyword.lower() in content_lower for keyword in keywords)

            if found:
                integration_score += 25
            else:
                integration_issues.append(f"Missing {category.replace('_', ' ')} integration")

                if category in ["todowrite", "claude_md"]:
                    critical_fixes.append(f"Add {category.replace('_', ' ')} integration section")

        # Bonus points for comprehensive integration
        if "framework ecosystem" in content_lower:
            integration_score += 10

        if "session management" in content_lower:
            integration_score += 10

        return min(100, integration_score)

    def _extract_section_content(self, content: str, section_name: str) -> str:
        """Extract content of a specific section"""
        pattern = rf'## {re.escape(section_name)}(.*?)(?=## |\Z)'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        return match.group(1).strip() if match else ""

    def _discover_agent_files(self) -> List[Path]:
        """Discover all agent markdown files"""
        agent_files = []

        if not self.agents_dir.exists():
            return agent_files

        for root, dirs, files in os.walk(self.agents_dir):
            for file in files:
                if file.endswith('.md'):
                    agent_files.append(Path(root) / file)

        return sorted(agent_files)

    def _generate_validation_summary(self, results: List[ValidationResult]) -> ValidationSummary:
        """Generate comprehensive validation summary"""

        total_agents = len(results)
        compliant_agents = len([r for r in results if r.is_compliant])
        compliance_rate = (compliant_agents / total_agents * 100) if total_agents > 0 else 0
        average_score = sum(r.compliance_score for r in results) / total_agents if total_agents > 0 else 0

        # Count issues by severity
        critical_issues = sum(len(r.critical_fixes) for r in results)
        warning_issues = sum(len(r.content_issues) + len(r.format_issues) + len(r.integration_issues) for r in results)
        info_issues = sum(len(r.improvements) for r in results)

        # Analyze by category
        category_results = {}
        for result in results:
            category = self._get_agent_category(Path(result.file_path))

            if category not in category_results:
                category_results[category] = {
                    "count": 0,
                    "compliant": 0,
                    "average_score": 0,
                    "scores": []
                }

            category_results[category]["count"] += 1
            category_results[category]["scores"].append(result.compliance_score)

            if result.is_compliant:
                category_results[category]["compliant"] += 1

        # Calculate category averages
        for category in category_results:
            scores = category_results[category]["scores"]
            category_results[category]["average_score"] = sum(scores) / len(scores)
            category_results[category]["compliance_rate"] = (
                category_results[category]["compliant"] / category_results[category]["count"] * 100
            )

        # Identify top issues
        issue_counter = {}
        for result in results:
            for issue in result.critical_fixes + result.content_issues + result.integration_issues:
                issue_counter[issue] = issue_counter.get(issue, 0) + 1

        top_issues = sorted(issue_counter.items(), key=lambda x: x[1], reverse=True)[:10]

        return ValidationSummary(
            total_agents=total_agents,
            compliant_agents=compliant_agents,
            compliance_rate=compliance_rate,
            average_score=average_score,
            critical_issues=critical_issues,
            warning_issues=warning_issues,
            info_issues=info_issues,
            validation_date=datetime.now(),
            template_version=self.template_version,
            category_results=category_results,
            top_issues=top_issues
        )

    def _get_agent_category(self, agent_path: Path) -> str:
        """Extract agent category from file path"""
        relative_path = agent_path.relative_to(self.agents_dir)
        return relative_path.parts[0] if relative_path.parts else "unknown"

    def generate_validation_report(self, summary: ValidationSummary, results: List[ValidationResult],
                                 output_file: str):
        """Generate comprehensive validation report"""

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"""# Agent Template Validation Report

## Executive Summary
- **Validation Date**: {summary.validation_date.strftime('%Y-%m-%d %H:%M:%S')}
- **Template Version**: {summary.template_version}
- **Total Agents**: {summary.total_agents}
- **Compliant Agents**: {summary.compliant_agents} ({summary.compliance_rate:.1f}%)
- **Average Compliance Score**: {summary.average_score:.1f}%

## Issue Summary
- **Critical Issues**: {summary.critical_issues} (require immediate fix)
- **Warning Issues**: {summary.warning_issues} (should be addressed)
- **Improvement Suggestions**: {summary.info_issues} (nice to have)

## Category Performance
""")

            for category, data in summary.category_results.items():
                f.write(f"""
### {category.title()} Category
- **Agents**: {data['count']}
- **Compliant**: {data['compliant']} ({data['compliance_rate']:.1f}%)
- **Average Score**: {data['average_score']:.1f}%
""")

            f.write(f"""
## Top Issues Across All Agents
""")
            for issue, count in summary.top_issues:
                f.write(f"- **{issue}**: {count} agents affected\n")

            f.write(f"""
## Individual Agent Results

### Compliant Agents (>= 80% score)
""")
            compliant = [r for r in results if r.is_compliant]
            for result in sorted(compliant, key=lambda x: x.compliance_score, reverse=True):
                f.write(f"- **{result.agent_name}**: {result.compliance_score:.1f}%\n")

            f.write(f"""
### Non-Compliant Agents (< 80% score)
""")
            non_compliant = [r for r in results if not r.is_compliant]
            for result in sorted(non_compliant, key=lambda x: x.compliance_score):
                f.write(f"- **{result.agent_name}**: {result.compliance_score:.1f}% - {len(result.critical_fixes)} critical issues\n")

                if result.critical_fixes:
                    for fix in result.critical_fixes[:3]:  # Show top 3 critical issues
                        f.write(f"  - ❌ {fix}\n")

                    if len(result.critical_fixes) > 3:
                        f.write(f"  - ... and {len(result.critical_fixes) - 3} more issues\n")

            f.write(f"""
## Standardization Recommendations

### Immediate Actions Required
""")
            critical_agents = [r for r in results if len(r.critical_fixes) > 0]
            f.write(f"Fix critical issues in {len(critical_agents)} agents:\n")
            for result in critical_agents:
                f.write(f"- {result.agent_name}: {len(result.critical_fixes)} critical fixes needed\n")

            f.write(f"""
### Quality Improvements
""")
            improvement_agents = [r for r in results if len(r.improvements) > 0]
            f.write(f"Enhance quality in {len(improvement_agents)} agents:\n")
            for result in improvement_agents[:10]:  # Show top 10
                f.write(f"- {result.agent_name}: {len(result.improvements)} improvements suggested\n")

            f.write(f"""
### Next Steps
1. **Phase 1**: Fix all critical issues ({summary.critical_issues} total)
2. **Phase 2**: Address content and format warnings ({summary.warning_issues} total)
3. **Phase 3**: Implement quality improvements ({summary.info_issues} total)
4. **Phase 4**: Establish automated validation in CI/CD pipeline

---
*Report generated by Claude Code Framework Template Validator*
""")

def main():
    """Main execution function"""
    framework_root = "/mnt/e/AI/my_name_is_claude"

    print("🚀 Starting Template Validation System")
    print("=" * 60)

    # Initialize validator
    validator = TemplateValidator(framework_root)

    # Run validation
    summary = validator.validate_all_agents()

    # Generate detailed report
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_file = f"{framework_root}/.claude/monitoring/quality/template-validation-{timestamp}.md"

    # We need to run validation again to get individual results for the report
    agent_files = validator._discover_agent_files()
    results = []
    for agent_file in agent_files:
        try:
            result = validator.validate_agent(agent_file)
            results.append(result)
        except Exception as e:
            print(f"Error validating {agent_file}: {e}")

    validator.generate_validation_report(summary, results, report_file)

    # Export JSON for automation
    json_file = f"{framework_root}/.claude/monitoring/quality/template-validation-{timestamp}.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            "summary": asdict(summary),
            "results": [asdict(r) for r in results]
        }, f, indent=2, default=str)

    print(f"""
📁 Validation Complete!
📊 Report Generated: {report_file}
📋 JSON Data: {json_file}
""")

    return summary, results

if __name__ == "__main__":
    main()