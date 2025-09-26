#!/usr/bin/env python3
"""
Claude Code Framework Agent Template Analyzer
Comprehensive analysis of all 45 agents for template standardization
"""

import os
import re
import json
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class AgentTemplateAnalysis:
    """Analysis result for individual agent template compliance"""
    agent_name: str
    file_path: str
    category: str
    subcategory: str

    # Template Structure Analysis
    has_title: bool
    has_core_competencies: bool
    has_approach: bool
    has_key_responsibilities: bool
    has_performance_standards: bool
    has_collaboration: bool
    has_integration: bool
    has_quality_gates: bool

    # Content Quality Analysis
    competency_detail_score: int  # 0-100
    approach_clarity_score: int   # 0-100
    responsibility_completeness: int  # 0-100
    integration_depth: int        # 0-100

    # Language and Format Compliance
    language_compliance: bool     # English only
    format_consistency: bool      # Markdown format
    section_ordering: bool        # Correct section order

    # Framework Integration
    todowrite_integration: bool
    claude_md_adaptation: bool
    mcp_tools_awareness: bool
    cross_agent_coordination: bool

    # Issues and Recommendations
    issues_detected: List[str]
    recommendations: List[str]
    compliance_score: float

@dataclass
class StandardizationReport:
    """Complete agent standardization analysis report"""
    analysis_date: datetime
    total_agents: int
    analyzed_agents: int

    # Category Breakdown
    core_agents: List[AgentTemplateAnalysis]
    enterprise_agents: List[AgentTemplateAnalysis]
    custom_agents: List[AgentTemplateAnalysis]

    # Overall Statistics
    average_compliance_score: float
    template_compliance_rate: float
    critical_issues_count: int

    # Standardization Recommendations
    unified_template_requirements: Dict[str, Any]
    standardization_plan: Dict[str, Any]
    validation_rules: List[str]

class AgentTemplateAnalyzer:
    """Main analyzer for agent template standardization"""

    def __init__(self, framework_root: str):
        self.framework_root = Path(framework_root)
        self.agents_dir = self.framework_root / ".claude/agents"

        # Template requirements based on current best practices
        self.required_sections = [
            "# Agent Name",
            "## Core Competencies",
            "## Approach",
            "## Key Responsibilities",
            "## Performance Standards",
            "## Collaboration",
            "## Integration",
            "## Quality Gates"
        ]

        self.integration_keywords = [
            "TodoWrite", "CLAUDE.md", "MCP tools", "agent coordination",
            "workflow", "session management", "quality gates"
        ]

    def analyze_all_agents(self) -> StandardizationReport:
        """Analyze all agents for template standardization"""
        print(f"🔍 Starting comprehensive agent template analysis...")

        # Discover all agents
        agent_files = self._discover_agent_files()
        print(f"📋 Found {len(agent_files)} agents to analyze")

        # Analyze each agent
        analyses = []
        for agent_file in agent_files:
            try:
                analysis = self._analyze_agent_file(agent_file)
                analyses.append(analysis)
                print(f"✅ Analyzed: {analysis.agent_name} (Score: {analysis.compliance_score:.1f}%)")
            except Exception as e:
                print(f"❌ Error analyzing {agent_file}: {e}")

        # Group by categories
        core_agents = [a for a in analyses if a.category == "core"]
        enterprise_agents = [a for a in analyses if a.category == "enterprise"]
        custom_agents = [a for a in analyses if a.category == "custom"]

        # Calculate statistics
        avg_compliance = sum(a.compliance_score for a in analyses) / len(analyses) if analyses else 0
        template_compliance = len([a for a in analyses if a.compliance_score >= 80]) / len(analyses) * 100 if analyses else 0
        critical_issues = sum(len(a.issues_detected) for a in analyses)

        # Generate standardization recommendations
        unified_template = self._create_unified_template_requirements(analyses)
        standardization_plan = self._create_standardization_plan(analyses)
        validation_rules = self._create_validation_rules()

        return StandardizationReport(
            analysis_date=datetime.now(),
            total_agents=len(agent_files),
            analyzed_agents=len(analyses),
            core_agents=core_agents,
            enterprise_agents=enterprise_agents,
            custom_agents=custom_agents,
            average_compliance_score=avg_compliance,
            template_compliance_rate=template_compliance,
            critical_issues_count=critical_issues,
            unified_template_requirements=unified_template,
            standardization_plan=standardization_plan,
            validation_rules=validation_rules
        )

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

    def _analyze_agent_file(self, agent_file: Path) -> AgentTemplateAnalysis:
        """Analyze individual agent file for template compliance"""

        # Extract metadata
        agent_name = agent_file.stem
        relative_path = agent_file.relative_to(self.agents_dir)
        category = relative_path.parts[0] if relative_path.parts else "unknown"
        subcategory = relative_path.parts[1] if len(relative_path.parts) > 1 else "general"

        # Read file content
        try:
            with open(agent_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            raise Exception(f"Failed to read agent file: {e}")

        # Analyze template structure
        structure_analysis = self._analyze_template_structure(content)

        # Analyze content quality
        quality_analysis = self._analyze_content_quality(content)

        # Analyze language and format
        format_analysis = self._analyze_format_compliance(content)

        # Analyze framework integration
        integration_analysis = self._analyze_framework_integration(content)

        # Identify issues and recommendations
        issues, recommendations = self._identify_issues_and_recommendations(
            content, structure_analysis, quality_analysis, format_analysis, integration_analysis
        )

        # Calculate compliance score
        compliance_score = self._calculate_compliance_score(
            structure_analysis, quality_analysis, format_analysis, integration_analysis
        )

        return AgentTemplateAnalysis(
            agent_name=agent_name,
            file_path=str(agent_file),
            category=category,
            subcategory=subcategory,
            **structure_analysis,
            **quality_analysis,
            **format_analysis,
            **integration_analysis,
            issues_detected=issues,
            recommendations=recommendations,
            compliance_score=compliance_score
        )

    def _analyze_template_structure(self, content: str) -> Dict[str, bool]:
        """Analyze template structure compliance"""
        return {
            "has_title": bool(re.search(r'^# .+', content, re.MULTILINE)),
            "has_core_competencies": "## Core Competencies" in content,
            "has_approach": "## Approach" in content,
            "has_key_responsibilities": "## Key Responsibilities" in content,
            "has_performance_standards": "## Performance Standards" in content,
            "has_collaboration": "## Collaboration" in content,
            "has_integration": "## Integration" in content,
            "has_quality_gates": "## Quality Gates" in content or "quality" in content.lower()
        }

    def _analyze_content_quality(self, content: str) -> Dict[str, int]:
        """Analyze content quality metrics"""

        # Competency detail score (based on depth and specificity)
        competency_section = self._extract_section(content, "Core Competencies")
        competency_score = min(100, len(competency_section.split()) * 2) if competency_section else 0

        # Approach clarity score
        approach_section = self._extract_section(content, "Approach")
        approach_score = min(100, len(approach_section.split()) * 3) if approach_section else 0

        # Responsibility completeness
        responsibility_section = self._extract_section(content, "Key Responsibilities")
        resp_score = min(100, len(responsibility_section.split()) * 2) if responsibility_section else 0

        # Integration depth
        integration_keywords_found = sum(1 for keyword in self.integration_keywords if keyword.lower() in content.lower())
        integration_score = min(100, integration_keywords_found * 15)

        return {
            "competency_detail_score": competency_score,
            "approach_clarity_score": approach_score,
            "responsibility_completeness": resp_score,
            "integration_depth": integration_score
        }

    def _analyze_format_compliance(self, content: str) -> Dict[str, bool]:
        """Analyze language and format compliance"""

        # Language compliance (check for non-English content patterns)
        # This is a simplified check - in reality would need more sophisticated detection
        non_english_patterns = [
            r'[ążśćęłóń]',  # Polish diacritics
            r'[àáâãäåæçèéêëìíîïñòóôõöøùúûüý]',  # Other European diacritics
        ]

        language_compliance = not any(re.search(pattern, content, re.IGNORECASE) for pattern in non_english_patterns)

        # Format consistency (proper markdown)
        format_consistency = (
            content.count('# ') >= 1 and  # Has title
            content.count('## ') >= 3 and  # Has multiple sections
            not re.search(r'^\s*[#]{4,}', content, re.MULTILINE)  # No excessive heading levels
        )

        # Section ordering (rough check)
        sections = re.findall(r'^## (.+)', content, re.MULTILINE)
        expected_order = ["Core Competencies", "Approach", "Key Responsibilities"]
        section_ordering = all(
            sections.index(section) if section in sections else -1
            for section in expected_order[:min(len(expected_order), len(sections))]
        ) if sections else False

        return {
            "language_compliance": language_compliance,
            "format_consistency": format_consistency,
            "section_ordering": section_ordering
        }

    def _analyze_framework_integration(self, content: str) -> Dict[str, bool]:
        """Analyze framework integration features"""

        content_lower = content.lower()

        return {
            "todowrite_integration": "todowrite" in content_lower,
            "claude_md_adaptation": "claude.md" in content_lower or "claude md" in content_lower,
            "mcp_tools_awareness": "mcp" in content_lower or "tools" in content_lower,
            "cross_agent_coordination": any(term in content_lower for term in ["coordination", "collaboration", "handoff", "workflow"])
        }

    def _extract_section(self, content: str, section_name: str) -> str:
        """Extract content of a specific section"""
        pattern = rf'## {re.escape(section_name)}(.*?)(?=## |\Z)'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        return match.group(1).strip() if match else ""

    def _identify_issues_and_recommendations(self, content: str, structure: Dict, quality: Dict,
                                           format_compliance: Dict, integration: Dict) -> Tuple[List[str], List[str]]:
        """Identify issues and generate recommendations"""

        issues = []
        recommendations = []

        # Structure issues
        if not structure["has_core_competencies"]:
            issues.append("Missing Core Competencies section")
            recommendations.append("Add comprehensive Core Competencies section with 10+ years expertise description")

        if not structure["has_approach"]:
            issues.append("Missing Approach section")
            recommendations.append("Add Approach section describing methodology and problem-solving strategy")

        if not structure["has_collaboration"]:
            issues.append("Missing Collaboration section")
            recommendations.append("Add Collaboration section with agent coordination patterns")

        # Quality issues
        if quality["competency_detail_score"] < 50:
            issues.append("Insufficient competency detail")
            recommendations.append("Expand competency descriptions with specific technical skills and experience levels")

        if quality["integration_depth"] < 30:
            issues.append("Limited framework integration")
            recommendations.append("Enhance integration with TodoWrite, CLAUDE.md adaptation, and MCP tools")

        # Format issues
        if not format_compliance["language_compliance"]:
            issues.append("Non-English content detected")
            recommendations.append("Ensure all content is in English per framework standards")

        if not format_compliance["format_consistency"]:
            issues.append("Inconsistent markdown formatting")
            recommendations.append("Standardize markdown format with proper heading hierarchy")

        # Integration issues
        if not integration["todowrite_integration"]:
            issues.append("Missing TodoWrite integration")
            recommendations.append("Add TodoWrite integration for task management")

        if not integration["claude_md_adaptation"]:
            issues.append("Missing CLAUDE.md adaptation")
            recommendations.append("Add CLAUDE.md adaptation capabilities for project configuration")

        return issues, recommendations

    def _calculate_compliance_score(self, structure: Dict, quality: Dict,
                                  format_compliance: Dict, integration: Dict) -> float:
        """Calculate overall compliance score"""

        # Structure score (40% weight)
        structure_items = ["has_core_competencies", "has_approach", "has_key_responsibilities",
                          "has_collaboration", "has_integration"]
        structure_score = sum(structure.get(item, False) for item in structure_items) / len(structure_items) * 100

        # Quality score (30% weight)
        quality_scores = [quality["competency_detail_score"], quality["approach_clarity_score"],
                         quality["responsibility_completeness"], quality["integration_depth"]]
        quality_score = sum(quality_scores) / len(quality_scores)

        # Format score (15% weight)
        format_items = ["language_compliance", "format_consistency", "section_ordering"]
        format_score = sum(format_compliance.get(item, False) for item in format_items) / len(format_items) * 100

        # Integration score (15% weight)
        integration_items = ["todowrite_integration", "claude_md_adaptation",
                           "mcp_tools_awareness", "cross_agent_coordination"]
        integration_score = sum(integration.get(item, False) for item in integration_items) / len(integration_items) * 100

        # Weighted average
        total_score = (
            structure_score * 0.40 +
            quality_score * 0.30 +
            format_score * 0.15 +
            integration_score * 0.15
        )

        return round(total_score, 1)

    def _create_unified_template_requirements(self, analyses: List[AgentTemplateAnalysis]) -> Dict[str, Any]:
        """Create unified template requirements based on analysis"""

        return {
            "mandatory_sections": [
                {
                    "name": "Agent Title",
                    "format": "# Agent Name",
                    "requirements": "Clear, descriptive agent name with role designation"
                },
                {
                    "name": "Core Competencies",
                    "format": "## Core Competencies",
                    "requirements": "10+ years expertise, specific technical skills, domain knowledge"
                },
                {
                    "name": "Approach",
                    "format": "## Approach",
                    "requirements": "Methodology, problem-solving strategy, decision-making framework"
                },
                {
                    "name": "Key Responsibilities",
                    "format": "## Key Responsibilities",
                    "requirements": "Specific deliverables, quality standards, collaboration requirements"
                },
                {
                    "name": "Performance Standards",
                    "format": "## Performance Standards",
                    "requirements": "Success metrics, quality gates, timeline expectations"
                },
                {
                    "name": "Collaboration",
                    "format": "## Collaboration",
                    "requirements": "Agent coordination patterns, handoff procedures, communication protocols"
                },
                {
                    "name": "Integration",
                    "format": "## Integration",
                    "requirements": "TodoWrite integration, CLAUDE.md adaptation, MCP tools usage"
                },
                {
                    "name": "Quality Gates",
                    "format": "## Quality Gates",
                    "requirements": "Validation criteria, testing requirements, compliance standards"
                }
            ],
            "content_standards": {
                "language": "English only",
                "format": "Markdown with proper heading hierarchy",
                "length": "Minimum 500 words per agent",
                "detail_level": "Enterprise-grade specificity"
            },
            "integration_requirements": {
                "todowrite": "Must include TodoWrite task management integration",
                "claude_md": "Must adapt to CLAUDE.md project configuration",
                "mcp_tools": "Must reference relevant MCP tools integration",
                "coordination": "Must specify cross-agent coordination patterns"
            },
            "quality_thresholds": {
                "minimum_compliance_score": 80,
                "competency_detail_minimum": 60,
                "integration_depth_minimum": 40,
                "structure_completeness": 100
            }
        }

    def _create_standardization_plan(self, analyses: List[AgentTemplateAnalysis]) -> Dict[str, Any]:
        """Create detailed standardization implementation plan"""

        # Identify agents needing attention
        critical_agents = [a for a in analyses if a.compliance_score < 60]
        moderate_agents = [a for a in analyses if 60 <= a.compliance_score < 80]
        good_agents = [a for a in analyses if a.compliance_score >= 80]

        return {
            "phase_1_critical": {
                "description": "Address critical compliance issues",
                "agents": [a.agent_name for a in critical_agents],
                "timeline": "Week 1-2",
                "focus": "Core template structure, mandatory sections",
                "estimated_effort": f"{len(critical_agents) * 4} hours"
            },
            "phase_2_moderate": {
                "description": "Improve moderate compliance agents",
                "agents": [a.agent_name for a in moderate_agents],
                "timeline": "Week 3-4",
                "focus": "Content quality, integration features",
                "estimated_effort": f"{len(moderate_agents) * 2} hours"
            },
            "phase_3_optimization": {
                "description": "Optimize well-compliant agents",
                "agents": [a.agent_name for a in good_agents],
                "timeline": "Week 5-6",
                "focus": "Advanced features, cross-references",
                "estimated_effort": f"{len(good_agents) * 1} hours"
            },
            "automation_requirements": {
                "template_validator": "Automated compliance checking",
                "content_generator": "Template-based content scaffolding",
                "quality_monitor": "Continuous compliance monitoring"
            },
            "success_metrics": {
                "target_compliance_rate": 95,
                "minimum_agent_score": 80,
                "template_consistency": 100,
                "integration_completeness": 90
            }
        }

    def _create_validation_rules(self) -> List[str]:
        """Create automated validation rules"""

        return [
            "All agents must have exactly 8 mandatory sections",
            "Core Competencies section must contain '10+ years' experience reference",
            "All content must be in English language",
            "Agent files must use proper markdown formatting",
            "Integration section must mention TodoWrite and CLAUDE.md",
            "Collaboration section must describe agent coordination",
            "Performance Standards must include measurable criteria",
            "Quality Gates must specify validation requirements",
            "Agent names must follow naming convention: [role]-[specialty]",
            "File paths must match agent categories in framework structure"
        ]

    def generate_report(self, report: StandardizationReport, output_file: str):
        """Generate comprehensive standardization report"""

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"""# Agent Template Standardization Analysis Report

## Executive Summary
- **Analysis Date**: {report.analysis_date.strftime('%Y-%m-%d %H:%M:%S')}
- **Total Agents Analyzed**: {report.analyzed_agents}/{report.total_agents}
- **Average Compliance Score**: {report.average_compliance_score:.1f}%
- **Template Compliance Rate**: {report.template_compliance_rate:.1f}%
- **Critical Issues Count**: {report.critical_issues_count}

## Category Breakdown

### Core Agents ({len(report.core_agents)} agents)
""")
            for agent in report.core_agents:
                f.write(f"- **{agent.agent_name}** ({agent.subcategory}): {agent.compliance_score:.1f}% compliance\n")

            f.write(f"""
### Enterprise Agents ({len(report.enterprise_agents)} agents)
""")
            for agent in report.enterprise_agents:
                f.write(f"- **{agent.agent_name}** ({agent.subcategory}): {agent.compliance_score:.1f}% compliance\n")

            f.write(f"""
### Custom Agents ({len(report.custom_agents)} agents)
""")
            for agent in report.custom_agents:
                f.write(f"- **{agent.agent_name}** ({agent.subcategory}): {agent.compliance_score:.1f}% compliance\n")

            f.write(f"""
## Compliance Analysis

### High Performers (>= 80% compliance)
""")
            high_performers = [a for a in (report.core_agents + report.enterprise_agents + report.custom_agents)
                             if a.compliance_score >= 80]
            for agent in high_performers:
                f.write(f"- {agent.agent_name}: {agent.compliance_score:.1f}%\n")

            f.write(f"""
### Needs Improvement (< 80% compliance)
""")
            needs_improvement = [a for a in (report.core_agents + report.enterprise_agents + report.custom_agents)
                               if a.compliance_score < 80]
            for agent in needs_improvement:
                f.write(f"- {agent.agent_name}: {agent.compliance_score:.1f}% - Issues: {len(agent.issues_detected)}\n")

            f.write(f"""
## Standardization Plan

### Phase 1: Critical Issues ({len([a for a in needs_improvement if a.compliance_score < 60])} agents)
""")
            for agent in [a for a in needs_improvement if a.compliance_score < 60]:
                f.write(f"- **{agent.agent_name}**: {', '.join(agent.issues_detected[:3])}\n")

            f.write(f"""
### Phase 2: Moderate Issues ({len([a for a in needs_improvement if 60 <= a.compliance_score < 80])} agents)
""")
            for agent in [a for a in needs_improvement if 60 <= a.compliance_score < 80]:
                f.write(f"- **{agent.agent_name}**: {', '.join(agent.issues_detected[:2])}\n")

            f.write(f"""
## Unified Template Requirements

### Mandatory Sections
""")
            for section in report.unified_template_requirements["mandatory_sections"]:
                f.write(f"- **{section['name']}**: {section['requirements']}\n")

            f.write(f"""
### Quality Thresholds
""")
            thresholds = report.unified_template_requirements["quality_thresholds"]
            for key, value in thresholds.items():
                f.write(f"- {key.replace('_', ' ').title()}: {value}\n")

            f.write(f"""
## Validation Rules
""")
            for rule in report.validation_rules:
                f.write(f"- {rule}\n")

            f.write(f"""
---
*Report generated by Claude Code Framework Agent Template Analyzer*
""")

def main():
    """Main execution function"""
    framework_root = "/mnt/e/AI/my_name_is_claude"

    print("🚀 Starting Agent Template Standardization Analysis")
    print("=" * 60)

    # Initialize analyzer
    analyzer = AgentTemplateAnalyzer(framework_root)

    # Perform analysis
    report = analyzer.analyze_all_agents()

    # Generate report
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_file = f"{framework_root}/.claude/monitoring/quality/agent-standardization-{timestamp}.md"
    analyzer.generate_report(report, report_file)

    # Export JSON for further processing
    json_file = f"{framework_root}/.claude/monitoring/quality/agent-standardization-{timestamp}.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(asdict(report), f, indent=2, default=str)

    print(f"""
🎯 Analysis Complete!
📊 Overall Results:
   • Average Compliance: {report.average_compliance_score:.1f}%
   • Template Compliance Rate: {report.template_compliance_rate:.1f}%
   • Critical Issues: {report.critical_issues_count}

📁 Reports Generated:
   • Detailed Report: {report_file}
   • JSON Data: {json_file}
""")

    return report

if __name__ == "__main__":
    main()