#!/usr/bin/env python3
"""
AI Tools Integration for Framework Quality Systems
Integrates monitoring, quality assessment, and validation with AI agent selection
"""

import sys
import os
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime

# Add framework quality tools to path
framework_root = Path(__file__).parent.parent.parent
quality_tools_path = framework_root / ".claude/monitoring/quality"
sys.path.append(str(quality_tools_path))

try:
    from quality_assessor import QualityAssessor, FrameworkQualityReport
    from template_validator import TemplateValidator, ValidationSummary
    from agent_template_analyzer import AgentTemplateAnalyzer, StandardizationReport
    from terminology_checker import TerminologyChecker, TerminologyReport
except ImportError as e:
    print(f"Warning: Could not import quality tools: {e}")

class FrameworkQualityIntegration:
    """Integration layer between AI Tools and Framework Quality Systems"""

    def __init__(self, framework_root: str = None):
        if framework_root is None:
            framework_root = str(Path(__file__).parent.parent.parent)

        self.framework_root = Path(framework_root)
        self.quality_tools_available = self._check_quality_tools_availability()

    def _check_quality_tools_availability(self) -> bool:
        """Check if quality assessment tools are available"""
        required_tools = [
            ".claude/monitoring/quality/quality-assessor.py",
            ".claude/monitoring/quality/template-validator.py",
            ".claude/monitoring/quality/agent-template-analyzer.py",
            ".claude/monitoring/quality/terminology-checker.py"
        ]

        for tool in required_tools:
            if not (self.framework_root / tool).exists():
                return False

        return True

    def get_framework_quality_status(self) -> Dict[str, Any]:
        """Get current framework quality status for AI agent selection"""
        if not self.quality_tools_available:
            return {
                "status": "quality_tools_unavailable",
                "overall_score": 0,
                "compliance_rate": 0,
                "recommendations": ["Install framework quality assessment tools"]
            }

        try:
            # Run quality assessment
            assessor = QualityAssessor(str(self.framework_root))
            quality_report = assessor.assess_framework()

            # Run template validation
            validator = TemplateValidator(str(self.framework_root))
            validation_summary = validator.validate_all_agents()

            # Compile status
            status = {
                "status": "quality_assessment_available",
                "timestamp": datetime.now().isoformat(),
                "overall_score": quality_report.overall_score,
                "quality_grade": quality_report.grade,
                "framework_status": quality_report.status,
                "template_compliance": {
                    "compliant_agents": validation_summary.compliant_agents,
                    "total_agents": validation_summary.total_agents,
                    "compliance_rate": validation_summary.compliance_rate,
                    "average_score": validation_summary.average_score
                },
                "critical_issues": len(quality_report.critical_issues),
                "recommendations": quality_report.recommendations[:5],  # Top 5
                "quality_thresholds": {
                    "enterprise_ready": 95,
                    "production_ready": 90,
                    "development_ready": 75
                }
            }

            return status

        except Exception as e:
            return {
                "status": "quality_assessment_error",
                "error": str(e),
                "overall_score": 0,
                "recommendations": ["Check quality assessment tool configuration"]
            }

    def get_agent_quality_scores(self) -> Dict[str, float]:
        """Get individual agent quality scores for selection optimization"""
        if not self.quality_tools_available:
            return {}

        try:
            analyzer = AgentTemplateAnalyzer(str(self.framework_root))
            report = analyzer.analyze_all_agents()

            # Combine all agents into score dictionary
            agent_scores = {}

            for agent in report.core_agents + report.enterprise_agents + report.custom_agents:
                agent_scores[agent.agent_name] = agent.compliance_score

            return agent_scores

        except Exception as e:
            print(f"Error getting agent quality scores: {e}")
            return {}

    def get_recommended_agents_by_quality(self, min_score: float = 80.0) -> List[str]:
        """Get list of agents meeting quality threshold"""
        agent_scores = self.get_agent_quality_scores()

        recommended = [
            agent_name for agent_name, score in agent_scores.items()
            if score >= min_score
        ]

        # Sort by score (highest first)
        recommended.sort(key=lambda x: agent_scores[x], reverse=True)

        return recommended

    def get_quality_insights_for_agent_selection(self, task_context: Dict[str, Any]) -> Dict[str, Any]:
        """Provide quality insights to enhance AI agent selection"""
        quality_status = self.get_framework_quality_status()
        agent_scores = self.get_agent_quality_scores()

        insights = {
            "framework_health": {
                "overall_score": quality_status.get("overall_score", 0),
                "status": quality_status.get("framework_status", "unknown"),
                "compliance_rate": quality_status.get("template_compliance", {}).get("compliance_rate", 0)
            },
            "agent_recommendations": {
                "high_quality_agents": self.get_recommended_agents_by_quality(80.0),
                "enterprise_ready_agents": self.get_recommended_agents_by_quality(90.0),
                "agents_needing_improvement": [
                    agent for agent, score in agent_scores.items() if score < 70.0
                ]
            },
            "quality_considerations": {
                "prefer_high_compliance": quality_status.get("compliance_rate", 0) < 80,
                "framework_mature": quality_status.get("overall_score", 0) >= 90,
                "critical_issues_present": quality_status.get("critical_issues", 0) > 0
            },
            "recommendations": quality_status.get("recommendations", [])
        }

        return insights

    def trigger_quality_assessment(self) -> Dict[str, Any]:
        """Trigger comprehensive quality assessment and return results"""
        if not self.quality_tools_available:
            return {"error": "Quality assessment tools not available"}

        try:
            results = {}

            # Run framework quality assessment
            print("🔍 Running framework quality assessment...")
            quality_cmd = [
                "python3",
                str(self.framework_root / ".claude/monitoring/quality/quality-assessor.py")
            ]
            quality_result = subprocess.run(quality_cmd, capture_output=True, text=True, cwd=self.framework_root)
            results["quality_assessment"] = {
                "status": "completed" if quality_result.returncode == 0 else "failed",
                "output": quality_result.stdout,
                "error": quality_result.stderr if quality_result.returncode != 0 else None
            }

            # Run template validation
            print("📋 Running template validation...")
            template_cmd = [
                "python3",
                str(self.framework_root / ".claude/monitoring/quality/template-validator.py")
            ]
            template_result = subprocess.run(template_cmd, capture_output=True, text=True, cwd=self.framework_root)
            results["template_validation"] = {
                "status": "completed" if template_result.returncode == 0 else "failed",
                "output": template_result.stdout,
                "error": template_result.stderr if template_result.returncode != 0 else None
            }

            # Run agent standardization analysis
            print("🎯 Running agent standardization analysis...")
            standardization_cmd = [
                "python3",
                str(self.framework_root / ".claude/monitoring/quality/agent-template-analyzer.py")
            ]
            standard_result = subprocess.run(standardization_cmd, capture_output=True, text=True, cwd=self.framework_root)
            results["standardization_analysis"] = {
                "status": "completed" if standard_result.returncode == 0 else "failed",
                "output": standard_result.stdout,
                "error": standard_result.stderr if standard_result.returncode != 0 else None
            }

            # Compile summary
            results["summary"] = {
                "timestamp": datetime.now().isoformat(),
                "tools_executed": 3,
                "successful_assessments": sum(1 for r in results.values()
                                            if isinstance(r, dict) and r.get("status") == "completed"),
                "framework_status": self.get_framework_quality_status()
            }

            return results

        except Exception as e:
            return {
                "error": f"Quality assessment execution failed: {str(e)}",
                "timestamp": datetime.now().isoformat()
            }

    def integrate_with_agent_selector(self, agent_selector_data: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance agent selector with quality data"""
        quality_insights = self.get_quality_insights_for_agent_selection(agent_selector_data)

        # Enhance agent recommendations with quality scores
        if "agent_recommendations" in agent_selector_data:
            enhanced_recommendations = []
            agent_scores = self.get_agent_quality_scores()

            for agent_rec in agent_selector_data["agent_recommendations"]:
                if isinstance(agent_rec, dict):
                    agent_name = agent_rec.get("agent_name", "")
                    quality_score = agent_scores.get(agent_name, 0)

                    agent_rec["quality_metrics"] = {
                        "compliance_score": quality_score,
                        "quality_tier": self._get_quality_tier(quality_score),
                        "enterprise_ready": quality_score >= 90
                    }

                enhanced_recommendations.append(agent_rec)

            agent_selector_data["agent_recommendations"] = enhanced_recommendations

        # Add quality context
        agent_selector_data["quality_context"] = quality_insights

        return agent_selector_data

    def _get_quality_tier(self, score: float) -> str:
        """Determine quality tier based on score"""
        if score >= 95:
            return "enterprise_grade"
        elif score >= 90:
            return "production_ready"
        elif score >= 80:
            return "development_ready"
        elif score >= 70:
            return "needs_improvement"
        else:
            return "requires_attention"

    def get_monitoring_status(self) -> Dict[str, Any]:
        """Check if monitoring systems are running"""
        monitoring_status = {
            "prometheus": self._check_service_status("prometheus", 9090),
            "grafana": self._check_service_status("grafana", 3000),
            "metrics_collector": self._check_process_status("metrics-collector.py"),
            "dashboards_available": self._check_dashboards_availability()
        }

        monitoring_status["overall_status"] = (
            "operational" if all(monitoring_status.values()) else "partial"
        )

        return monitoring_status

    def _check_service_status(self, service_name: str, port: int) -> bool:
        """Check if a service is running on specified port"""
        try:
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('localhost', port))
            sock.close()
            return result == 0
        except:
            return False

    def _check_process_status(self, process_name: str) -> bool:
        """Check if a process is running"""
        try:
            result = subprocess.run(
                ["pgrep", "-f", process_name],
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except:
            return False

    def _check_dashboards_availability(self) -> bool:
        """Check if dashboard files exist"""
        dashboard_files = [
            ".claude/monitoring/dashboards/executive-dashboard.json",
            ".claude/monitoring/dashboards/operations-dashboard.json",
            ".claude/monitoring/dashboards/developer-dashboard.json",
            ".claude/monitoring/dashboards/quality-dashboard.json"
        ]

        return all((self.framework_root / dashboard).exists() for dashboard in dashboard_files)

def main():
    """CLI interface for quality integration"""
    integration = FrameworkQualityIntegration()

    if len(sys.argv) < 2:
        print("""
Framework Quality Integration Commands:

    status          - Get framework quality status
    agents          - List agent quality scores
    assess          - Run comprehensive quality assessment
    monitor         - Check monitoring systems status
    insights        - Get quality insights for agent selection

Examples:
    python3 framework_quality_integration.py status
    python3 framework_quality_integration.py assess
""")
        return

    command = sys.argv[1]

    if command == "status":
        status = integration.get_framework_quality_status()
        print(json.dumps(status, indent=2))

    elif command == "agents":
        scores = integration.get_agent_quality_scores()
        for agent, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
            print(f"{agent}: {score:.1f}%")

    elif command == "assess":
        results = integration.trigger_quality_assessment()
        print(json.dumps(results, indent=2))

    elif command == "monitor":
        monitoring = integration.get_monitoring_status()
        print(json.dumps(monitoring, indent=2))

    elif command == "insights":
        insights = integration.get_quality_insights_for_agent_selection({})
        print(json.dumps(insights, indent=2))

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()