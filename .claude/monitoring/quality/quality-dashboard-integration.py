#!/usr/bin/env python3
"""
Quality Dashboard Integration for Claude Code Framework
Integrates quality metrics with Prometheus and Grafana monitoring
"""

import time
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any
from prometheus_client import Gauge, Counter, Histogram, Info, CollectorRegistry, write_to_textfile
import threading
import os
from quality_assessor import QualityAssessor, FrameworkQualityReport

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class QualityMetricsExporter:
    """Export quality metrics to Prometheus"""

    def __init__(self, framework_root: str):
        self.framework_root = framework_root
        self.registry = CollectorRegistry()
        self._setup_metrics()
        self.assessor = QualityAssessor(framework_root)

    def _setup_metrics(self):
        """Setup Prometheus metrics for quality tracking"""

        # Overall quality metrics
        self.overall_quality_score = Gauge(
            'claude_framework_quality_score',
            'Overall framework quality score',
            registry=self.registry
        )

        self.quality_grade_info = Info(
            'claude_framework_quality_grade',
            'Framework quality grade information',
            registry=self.registry
        )

        # Gate-specific metrics
        self.gate_scores = Gauge(
            'claude_quality_gate_score',
            'Quality gate scores',
            ['gate_name'],
            registry=self.registry
        )

        self.gate_status = Gauge(
            'claude_quality_gate_status',
            'Quality gate pass/fail status (1=pass, 0=fail)',
            ['gate_name'],
            registry=self.registry
        )

        # Component quality metrics
        self.agent_quality_score = Gauge(
            'claude_agent_quality_score',
            'Individual agent quality score',
            ['agent_name', 'category'],
            registry=self.registry
        )

        self.prompt_quality_score = Gauge(
            'claude_prompt_quality_score',
            'Individual prompt quality score',
            ['prompt_name', 'category'],
            registry=self.registry
        )

        # Quality trend metrics
        self.quality_improvement_rate = Gauge(
            'claude_quality_improvement_rate',
            'Quality improvement rate over time',
            ['component'],
            registry=self.registry
        )

        self.issues_detected = Gauge(
            'claude_quality_issues_detected',
            'Number of quality issues detected',
            ['severity', 'category'],
            registry=self.registry
        )

        # Assessment metrics
        self.assessment_duration = Histogram(
            'claude_quality_assessment_duration_seconds',
            'Time taken for quality assessment',
            buckets=[1.0, 5.0, 10.0, 30.0, 60.0, 120.0, 300.0],
            registry=self.registry
        )

        self.assessment_count = Counter(
            'claude_quality_assessments_total',
            'Total number of quality assessments performed',
            registry=self.registry
        )

        # Compliance metrics
        self.template_compliance_rate = Gauge(
            'claude_template_compliance_rate',
            'Template compliance rate percentage',
            ['template_type'],
            registry=self.registry
        )

        self.hardcoding_violations = Gauge(
            'claude_hardcoding_violations',
            'Number of hardcoding violations detected',
            ['violation_type'],
            registry=self.registry
        )

        # Business metrics
        self.framework_readiness_level = Gauge(
            'claude_framework_readiness_level',
            'Framework readiness level (0-4: Development/Near/Production/Enterprise)',
            registry=self.registry
        )

        self.quality_recommendations_count = Gauge(
            'claude_quality_recommendations',
            'Number of active quality recommendations',
            ['priority'],
            registry=self.registry
        )

    def perform_assessment_and_export(self) -> FrameworkQualityReport:
        """Perform quality assessment and export metrics"""
        start_time = time.time()

        try:
            # Perform assessment
            logger.info("Starting quality assessment...")
            report = self.assessor.assess_framework()

            # Export metrics
            self._export_report_metrics(report)

            # Record assessment metrics
            duration = time.time() - start_time
            self.assessment_duration.observe(duration)
            self.assessment_count.inc()

            logger.info(f"Quality assessment completed in {duration:.2f}s. Score: {report.overall_score:.1f}/100")
            return report

        except Exception as e:
            logger.error(f"Quality assessment failed: {e}")
            duration = time.time() - start_time
            self.assessment_duration.observe(duration)
            raise

    def _export_report_metrics(self, report: FrameworkQualityReport):
        """Export quality report metrics to Prometheus"""

        # Overall metrics
        self.overall_quality_score.set(report.overall_score)
        self.quality_grade_info.info({
            'grade': report.grade,
            'status': report.status,
            'version': report.framework_version,
            'assessment_date': report.assessment_date.isoformat()
        })

        # Readiness level mapping
        readiness_mapping = {
            'Enterprise Ready': 4,
            'Production Ready': 3,
            'Near Production': 2,
            'Development Ready': 1,
            'Needs Improvement': 0
        }
        self.framework_readiness_level.set(readiness_mapping.get(report.status, 0))

        # Gate-specific metrics
        for gate_result in report.gate_results:
            self.gate_scores.labels(gate_name=gate_result.gate_name).set(gate_result.overall_score)
            self.gate_status.labels(gate_name=gate_result.gate_name).set(
                1 if gate_result.status == 'pass' else 0
            )

        # Issues and recommendations
        self.issues_detected.labels(severity='critical', category='all').set(len(report.critical_issues))
        self.quality_recommendations_count.labels(priority='high').set(len(report.recommendations))

        # Template compliance (from agent assessment)
        agent_gate = next((g for g in report.gate_results if g.gate_name == 'agent_quality'), None)
        if agent_gate:
            compliance_metric = next((m for m in agent_gate.metrics if m.name == 'template_compliance'), None)
            if compliance_metric:
                self.template_compliance_rate.labels(template_type='agent').set(compliance_metric.score)

        # Hardcoding violations (from prompt assessment)
        prompt_gate = next((g for g in report.gate_results if g.gate_name == 'prompt_quality'), None)
        if prompt_gate:
            agnostic_metric = next((m for m in prompt_gate.metrics if m.name == 'technology_agnostic_design'), None)
            if agnostic_metric:
                # Inverse relationship: lower agnostic score = more violations
                violations = max(0, (100 - agnostic_metric.score) / 20)
                self.hardcoding_violations.labels(violation_type='path_hardcoding').set(violations)

        logger.info("Quality metrics exported to Prometheus")

    def export_to_file(self, filepath: str):
        """Export metrics to file for Prometheus scraping"""
        write_to_textfile(filepath, self.registry)
        logger.info(f"Quality metrics exported to file: {filepath}")

    def get_metrics_summary(self) -> Dict[str, Any]:
        """Get current quality metrics summary"""
        try:
            report = self.assessor.assess_framework()
            return {
                "overall_score": report.overall_score,
                "grade": report.grade,
                "status": report.status,
                "gate_scores": {
                    gate.gate_name: gate.overall_score
                    for gate in report.gate_results
                },
                "critical_issues_count": len(report.critical_issues),
                "recommendations_count": len(report.recommendations),
                "assessment_date": report.assessment_date.isoformat()
            }
        except Exception as e:
            logger.error(f"Failed to get quality metrics summary: {e}")
            return {"error": str(e)}

class QualityMonitoringService:
    """Continuous quality monitoring service"""

    def __init__(self, framework_root: str, assessment_interval: int = 3600):
        self.framework_root = framework_root
        self.assessment_interval = assessment_interval  # 1 hour default
        self.exporter = QualityMetricsExporter(framework_root)
        self.is_running = False
        self.monitoring_thread = None

    def start_monitoring(self):
        """Start continuous quality monitoring"""
        logger.info(f"Starting quality monitoring service (interval: {self.assessment_interval}s)")

        self.is_running = True
        self.monitoring_thread = threading.Thread(target=self._monitoring_loop)
        self.monitoring_thread.start()

        logger.info("Quality monitoring started successfully")

    def stop_monitoring(self):
        """Stop quality monitoring"""
        self.is_running = False
        if self.monitoring_thread:
            self.monitoring_thread.join()
        logger.info("Quality monitoring stopped")

    def _monitoring_loop(self):
        """Main monitoring loop"""
        while self.is_running:
            try:
                # Perform assessment and export metrics
                report = self.exporter.perform_assessment_and_export()

                # Export to file for Prometheus
                metrics_file = f"{self.framework_root}/.claude/monitoring/metrics/quality_metrics.prom"
                os.makedirs(os.path.dirname(metrics_file), exist_ok=True)
                self.exporter.export_to_file(metrics_file)

                # Check for critical issues
                if report.overall_score < 75:
                    logger.warning(f"Framework quality below threshold: {report.overall_score:.1f}/100")

                # Sleep until next assessment
                time.sleep(self.assessment_interval)

            except Exception as e:
                logger.error(f"Error in quality monitoring loop: {e}")
                time.sleep(self.assessment_interval)

    def trigger_assessment(self) -> FrameworkQualityReport:
        """Trigger immediate quality assessment"""
        return self.exporter.perform_assessment_and_export()

def create_quality_dashboard_config():
    """Create Grafana dashboard configuration for quality metrics"""

    dashboard_config = {
        "dashboard": {
            "id": None,
            "title": "Claude Code Framework - Quality Dashboard",
            "tags": ["claude-code", "quality", "metrics"],
            "timezone": "browser",
            "panels": [
                {
                    "id": 1,
                    "title": "Overall Quality Score",
                    "type": "stat",
                    "targets": [
                        {
                            "expr": "claude_framework_quality_score",
                            "legendFormat": "Quality Score"
                        }
                    ],
                    "fieldConfig": {
                        "defaults": {
                            "color": {"mode": "thresholds"},
                            "thresholds": {
                                "steps": [
                                    {"color": "red", "value": 0},
                                    {"color": "yellow", "value": 75},
                                    {"color": "green", "value": 90}
                                ]
                            },
                            "unit": "percent",
                            "min": 0,
                            "max": 100
                        }
                    },
                    "gridPos": {"h": 8, "w": 12, "x": 0, "y": 0}
                },
                {
                    "id": 2,
                    "title": "Quality Gate Scores",
                    "type": "bargauge",
                    "targets": [
                        {
                            "expr": "claude_quality_gate_score",
                            "legendFormat": "{{gate_name}}"
                        }
                    ],
                    "fieldConfig": {
                        "defaults": {
                            "color": {"mode": "continuous-GrYlRd"},
                            "min": 0,
                            "max": 100,
                            "unit": "percent"
                        }
                    },
                    "gridPos": {"h": 8, "w": 12, "x": 12, "y": 0}
                },
                {
                    "id": 3,
                    "title": "Framework Readiness Level",
                    "type": "stat",
                    "targets": [
                        {
                            "expr": "claude_framework_readiness_level",
                            "legendFormat": "Readiness Level"
                        }
                    ],
                    "fieldConfig": {
                        "defaults": {
                            "mappings": [
                                {"options": {"0": {"text": "Needs Improvement"}}},
                                {"options": {"1": {"text": "Development Ready"}}},
                                {"options": {"2": {"text": "Near Production"}}},
                                {"options": {"3": {"text": "Production Ready"}}},
                                {"options": {"4": {"text": "Enterprise Ready"}}}
                            ]
                        }
                    },
                    "gridPos": {"h": 6, "w": 8, "x": 0, "y": 8}
                },
                {
                    "id": 4,
                    "title": "Quality Issues Detected",
                    "type": "stat",
                    "targets": [
                        {
                            "expr": "claude_quality_issues_detected",
                            "legendFormat": "{{severity}} issues"
                        }
                    ],
                    "fieldConfig": {
                        "defaults": {
                            "color": {"mode": "thresholds"},
                            "thresholds": {
                                "steps": [
                                    {"color": "green", "value": 0},
                                    {"color": "yellow", "value": 1},
                                    {"color": "red", "value": 5}
                                ]
                            }
                        }
                    },
                    "gridPos": {"h": 6, "w": 8, "x": 8, "y": 8}
                },
                {
                    "id": 5,
                    "title": "Template Compliance Rate",
                    "type": "stat",
                    "targets": [
                        {
                            "expr": "claude_template_compliance_rate",
                            "legendFormat": "{{template_type}} compliance"
                        }
                    ],
                    "fieldConfig": {
                        "defaults": {
                            "unit": "percent",
                            "min": 0,
                            "max": 100
                        }
                    },
                    "gridPos": {"h": 6, "w": 8, "x": 16, "y": 8}
                },
                {
                    "id": 6,
                    "title": "Quality Trends",
                    "type": "graph",
                    "targets": [
                        {
                            "expr": "claude_framework_quality_score",
                            "legendFormat": "Overall Quality"
                        },
                        {
                            "expr": "claude_quality_gate_score",
                            "legendFormat": "{{gate_name}}"
                        }
                    ],
                    "yAxes": [
                        {"label": "Score", "min": 0, "max": 100}
                    ],
                    "gridPos": {"h": 8, "w": 24, "x": 0, "y": 14}
                }
            ],
            "time": {
                "from": "now-24h",
                "to": "now"
            },
            "refresh": "5m"
        }
    }

    return dashboard_config

def main():
    """Main execution function"""
    framework_root = "/mnt/e/AI/my_name_is_claude"

    # Create quality dashboard configuration
    dashboard_config = create_quality_dashboard_config()
    dashboard_file = f"{framework_root}/.claude/monitoring/dashboards/quality-dashboard.json"
    os.makedirs(os.path.dirname(dashboard_file), exist_ok=True)

    with open(dashboard_file, 'w') as f:
        json.dump(dashboard_config, f, indent=2)

    logger.info(f"Quality dashboard configuration created: {dashboard_file}")

    # Initialize and start quality monitoring
    monitoring_service = QualityMonitoringService(framework_root, assessment_interval=3600)

    try:
        # Perform initial assessment
        initial_report = monitoring_service.trigger_assessment()
        logger.info(f"Initial quality assessment completed: {initial_report.overall_score:.1f}/100")

        # Start continuous monitoring
        monitoring_service.start_monitoring()

        logger.info("Quality monitoring service started. Press Ctrl+C to stop.")
        while True:
            time.sleep(10)

    except KeyboardInterrupt:
        logger.info("Stopping quality monitoring service...")
        monitoring_service.stop_monitoring()
    except Exception as e:
        logger.error(f"Error in quality monitoring: {e}")
        monitoring_service.stop_monitoring()

if __name__ == "__main__":
    main()