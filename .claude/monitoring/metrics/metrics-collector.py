#!/usr/bin/env python3
"""
Claude Code Framework Metrics Collector
Collects performance metrics from framework components and exports to monitoring systems
"""

import time
import json
import psutil
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from prometheus_client import Counter, Histogram, Gauge, Info, start_http_server
import threading
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class AgentExecutionMetric:
    """Metrics for individual agent execution"""
    agent_name: str
    execution_time: float
    success: bool
    task_type: str
    user_id: str
    timestamp: datetime
    memory_usage: float
    cpu_usage: float
    error_message: Optional[str] = None

@dataclass
class FrameworkMetric:
    """High-level framework metrics"""
    active_users: int
    total_executions: int
    average_response_time: float
    error_rate: float
    uptime: float
    memory_usage: float
    cpu_usage: float
    timestamp: datetime

@dataclass
class QualityMetric:
    """Code quality and validation metrics"""
    quality_score: float
    test_coverage: float
    code_complexity: float
    security_score: float
    compliance_score: float
    issues_detected: int
    timestamp: datetime

class PrometheusMetrics:
    """Prometheus metrics definitions"""

    def __init__(self):
        # Agent metrics
        self.agent_executions = Counter(
            'claude_agent_executions_total',
            'Total number of agent executions',
            ['agent_name', 'success', 'user_id']
        )

        self.agent_execution_time = Histogram(
            'claude_agent_execution_duration_seconds',
            'Time spent executing agents',
            ['agent_name', 'task_type'],
            buckets=[0.1, 0.5, 1.0, 2.5, 5.0, 10.0, 25.0, 50.0, 100.0]
        )

        self.agent_memory_usage = Gauge(
            'claude_agent_memory_usage_bytes',
            'Memory usage by agent',
            ['agent_name']
        )

        # Framework metrics
        self.framework_uptime = Gauge(
            'claude_framework_uptime_seconds',
            'Framework uptime in seconds'
        )

        self.framework_active_users = Gauge(
            'claude_framework_active_users',
            'Number of active users'
        )

        self.framework_error_rate = Gauge(
            'claude_framework_error_rate',
            'Framework error rate percentage'
        )

        self.framework_response_time = Histogram(
            'claude_framework_response_time_seconds',
            'Framework response time',
            buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0]
        )

        # Quality metrics
        self.code_quality_score = Gauge(
            'claude_code_quality_score',
            'Code quality score',
            ['user_id', 'project_id']
        )

        self.test_coverage = Gauge(
            'claude_test_coverage_percentage',
            'Test coverage percentage',
            ['user_id', 'project_id']
        )

        # AI Tools metrics
        self.ai_tool_accuracy = Gauge(
            'claude_ai_tool_accuracy',
            'AI tool accuracy percentage',
            ['tool_name']
        )

        self.ai_tool_response_time = Histogram(
            'claude_ai_tool_response_time_seconds',
            'AI tool response time',
            ['tool_name'],
            buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0]
        )

        # MCP Tools metrics
        self.mcp_tool_availability = Gauge(
            'claude_mcp_tool_availability',
            'MCP tool availability percentage',
            ['tool_name']
        )

        self.mcp_tool_usage = Counter(
            'claude_mcp_tool_usage_total',
            'Total MCP tool usage',
            ['tool_name', 'user_id']
        )

class MetricsCollector:
    """Main metrics collection engine"""

    def __init__(self, collection_interval: int = 30):
        self.collection_interval = collection_interval
        self.metrics = PrometheusMetrics()
        self.start_time = datetime.now()
        self.is_running = False
        self.collection_thread = None

        # Framework state tracking
        self.active_users = set()
        self.total_executions = 0
        self.total_errors = 0
        self.execution_times = []

    def start_collection(self, port: int = 8000):
        """Start metrics collection and Prometheus HTTP server"""
        logger.info(f"Starting metrics collection on port {port}")

        # Start Prometheus HTTP server
        start_http_server(port)

        # Start collection thread
        self.is_running = True
        self.collection_thread = threading.Thread(target=self._collection_loop)
        self.collection_thread.start()

        logger.info("Metrics collection started successfully")

    def stop_collection(self):
        """Stop metrics collection"""
        self.is_running = False
        if self.collection_thread:
            self.collection_thread.join()
        logger.info("Metrics collection stopped")

    def record_agent_execution(self, metric: AgentExecutionMetric):
        """Record individual agent execution metrics"""
        # Update Prometheus metrics
        self.metrics.agent_executions.labels(
            agent_name=metric.agent_name,
            success=str(metric.success),
            user_id=metric.user_id
        ).inc()

        self.metrics.agent_execution_time.labels(
            agent_name=metric.agent_name,
            task_type=metric.task_type
        ).observe(metric.execution_time)

        self.metrics.agent_memory_usage.labels(
            agent_name=metric.agent_name
        ).set(metric.memory_usage)

        # Update internal tracking
        self.active_users.add(metric.user_id)
        self.total_executions += 1
        if not metric.success:
            self.total_errors += 1
        self.execution_times.append(metric.execution_time)

        # Keep only last 1000 execution times for performance
        if len(self.execution_times) > 1000:
            self.execution_times = self.execution_times[-1000:]

        logger.debug(f"Recorded agent execution: {metric.agent_name} - {metric.execution_time}s")

    def record_quality_metrics(self, metric: QualityMetric, user_id: str, project_id: str):
        """Record code quality metrics"""
        self.metrics.code_quality_score.labels(
            user_id=user_id,
            project_id=project_id
        ).set(metric.quality_score)

        self.metrics.test_coverage.labels(
            user_id=user_id,
            project_id=project_id
        ).set(metric.test_coverage)

        logger.debug(f"Recorded quality metrics for {user_id}/{project_id}")

    def record_ai_tool_metrics(self, tool_name: str, accuracy: float, response_time: float):
        """Record AI tool performance metrics"""
        self.metrics.ai_tool_accuracy.labels(tool_name=tool_name).set(accuracy)
        self.metrics.ai_tool_response_time.labels(tool_name=tool_name).observe(response_time)

        logger.debug(f"Recorded AI tool metrics: {tool_name}")

    def record_mcp_tool_metrics(self, tool_name: str, availability: float, user_id: str):
        """Record MCP tool metrics"""
        self.metrics.mcp_tool_availability.labels(tool_name=tool_name).set(availability)
        self.metrics.mcp_tool_usage.labels(tool_name=tool_name, user_id=user_id).inc()

        logger.debug(f"Recorded MCP tool metrics: {tool_name}")

    def _collection_loop(self):
        """Main collection loop"""
        while self.is_running:
            try:
                self._collect_system_metrics()
                self._collect_framework_metrics()
                time.sleep(self.collection_interval)
            except Exception as e:
                logger.error(f"Error in collection loop: {e}")
                time.sleep(self.collection_interval)

    def _collect_system_metrics(self):
        """Collect system-level metrics"""
        # System resource usage
        cpu_percent = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        # Update Prometheus metrics (these would be framework-specific gauges)
        logger.debug(f"System metrics - CPU: {cpu_percent}%, Memory: {memory.percent}%, Disk: {disk.percent}%")

    def _collect_framework_metrics(self):
        """Collect framework-level metrics"""
        # Calculate uptime
        uptime = (datetime.now() - self.start_time).total_seconds()
        self.metrics.framework_uptime.set(uptime)

        # Update active users
        self.metrics.framework_active_users.set(len(self.active_users))

        # Calculate error rate
        error_rate = (self.total_errors / max(self.total_executions, 1)) * 100
        self.metrics.framework_error_rate.set(error_rate)

        logger.debug(f"Framework metrics - Uptime: {uptime}s, Users: {len(self.active_users)}, Error rate: {error_rate}%")

    def get_metrics_summary(self) -> Dict[str, Any]:
        """Get current metrics summary"""
        uptime = (datetime.now() - self.start_time).total_seconds()
        error_rate = (self.total_errors / max(self.total_executions, 1)) * 100
        avg_response_time = sum(self.execution_times) / len(self.execution_times) if self.execution_times else 0

        return {
            "framework": {
                "uptime_seconds": uptime,
                "active_users": len(self.active_users),
                "total_executions": self.total_executions,
                "error_rate": error_rate,
                "average_response_time": avg_response_time
            },
            "system": {
                "cpu_percent": psutil.cpu_percent(),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage('/').percent
            },
            "timestamp": datetime.now().isoformat()
        }

class MetricsExporter:
    """Export metrics to various backends"""

    def __init__(self, collector: MetricsCollector):
        self.collector = collector

    def export_to_json(self, filepath: str):
        """Export current metrics to JSON file"""
        metrics = self.collector.get_metrics_summary()
        with open(filepath, 'w') as f:
            json.dump(metrics, f, indent=2)
        logger.info(f"Metrics exported to {filepath}")

    def export_to_csv(self, filepath: str):
        """Export metrics to CSV format"""
        import csv
        metrics = self.collector.get_metrics_summary()

        with open(filepath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['metric', 'value', 'timestamp'])

            for category, values in metrics.items():
                if isinstance(values, dict):
                    for key, value in values.items():
                        writer.writerow([f"{category}.{key}", value, metrics['timestamp']])
                else:
                    writer.writerow([category, values, metrics['timestamp']])

        logger.info(f"Metrics exported to CSV: {filepath}")

def main():
    """Main execution function"""
    # Initialize metrics collector
    collector = MetricsCollector(collection_interval=30)

    try:
        # Start collection
        collector.start_collection(port=8000)

        # Example usage - simulate some agent executions
        import random
        agents = ['frontend-engineer', 'backend-engineer', 'security-engineer', 'qa-engineer']

        logger.info("Simulating agent executions for demonstration...")
        for i in range(10):
            metric = AgentExecutionMetric(
                agent_name=random.choice(agents),
                execution_time=random.uniform(0.5, 5.0),
                success=random.choice([True, True, True, False]),  # 75% success rate
                task_type="development",
                user_id=f"user_{random.randint(1, 5)}",
                timestamp=datetime.now(),
                memory_usage=random.uniform(100, 500),
                cpu_usage=random.uniform(10, 80)
            )
            collector.record_agent_execution(metric)
            time.sleep(1)

        # Keep running
        logger.info("Metrics collector running. Press Ctrl+C to stop.")
        while True:
            time.sleep(10)

    except KeyboardInterrupt:
        logger.info("Stopping metrics collection...")
        collector.stop_collection()
    except Exception as e:
        logger.error(f"Error in main: {e}")
        collector.stop_collection()

if __name__ == "__main__":
    main()