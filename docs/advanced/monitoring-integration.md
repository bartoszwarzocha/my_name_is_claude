# Monitoring Integration Guide

*Integrating monitoring, alerting, and observability systems with My Name Is Claude framework*

## 🎯 Overview

Complete guide for monitoring framework health, agent performance, and system observability using Prometheus, Grafana, and custom metrics.

---

## 📊 Prometheus Integration

### **Metrics Exporter**

```python
from prometheus_client import start_http_server, Counter, Histogram, Gauge, Info

# Define metrics
agent_executions_total = Counter(
    'agent_executions_total',
    'Total agent executions',
    ['agent_name', 'status']
)

agent_execution_duration = Histogram(
    'agent_execution_duration_seconds',
    'Agent execution duration',
    ['agent_name'],
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0, 60.0]
)

framework_memory_usage = Gauge(
    'framework_memory_usage_bytes',
    'Framework memory usage in bytes'
)

framework_info = Info('framework_info', 'Framework version and configuration')

# Start metrics server
start_http_server(8000)

# Record metrics
def execute_agent_with_metrics(agent_name, task):
    try:
        with agent_execution_duration.labels(agent_name=agent_name).time():
            result = execute_agent(agent_name, task)

        agent_executions_total.labels(agent_name=agent_name, status='success').inc()
        return result

    except Exception as e:
        agent_executions_total.labels(agent_name=agent_name, status='failure').inc()
        raise

# Update system metrics
import psutil
framework_memory_usage.set(psutil.Process().memory_info().rss)

# Set framework info
framework_info.info({
    'version': '3.3.0',
    'environment': 'production',
    'scale': 'enterprise'
})
```

### **Prometheus Configuration**

```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'my-name-is-claude'
    static_configs:
      - targets: ['localhost:8000']
    labels:
      environment: 'production'
      project: 'my-name-is-claude'
```

---

## 📈 Grafana Dashboards

Framework includes pre-built dashboards in `.claude/monitoring/dashboards/`:

- **executive-dashboard.json** - Business metrics and KPIs
- **operations-dashboard.json** - System health and performance
- **quality-dashboard.json** - Code quality and validation metrics

### **Custom Dashboard Example**

```json
{
  "dashboard": {
    "title": "Framework Performance",
    "panels": [
      {
        "title": "Agent Execution Rate",
        "targets": [
          {
            "expr": "rate(agent_executions_total[5m])"
          }
        ]
      },
      {
        "title": "Agent Response Time (p95)",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, agent_execution_duration_seconds_bucket)"
          }
        ]
      }
    ]
  }
}
```

---

## 🔔 Alerting

### **AlertManager Configuration**

```yaml
# alertmanager.yml
global:
  resolve_timeout: 5m

route:
  receiver: 'team-alerts'
  group_by: ['alertname', 'severity']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h

receivers:
  - name: 'team-alerts'
    slack_configs:
      - api_url: 'https://hooks.slack.com/services/YOUR/WEBHOOK/URL'
        channel: '#framework-alerts'
        title: 'Framework Alert'
        text: '{{ .CommonAnnotations.description }}'

    email_configs:
      - to: 'team@example.com'
        from: 'framework@example.com'
        smarthost: 'smtp.gmail.com:587'
```

### **Alert Rules**

```yaml
# alert_rules.yml
groups:
  - name: framework_alerts
    rules:
      - alert: HighErrorRate
        expr: rate(agent_executions_total{status="failure"}[5m]) > 0.1
        for: 10m
        labels:
          severity: critical
        annotations:
          summary: "High agent failure rate"
          description: "Agent failure rate is {{ $value }} per second"

      - alert: HighMemoryUsage
        expr: framework_memory_usage_bytes > 500 * 1024 * 1024
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Framework memory usage high"
          description: "Memory usage is {{ $value }} bytes"

      - alert: SlowAgentExecution
        expr: histogram_quantile(0.95, agent_execution_duration_seconds_bucket) > 10
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "Slow agent execution detected"
          description: "P95 latency is {{ $value }} seconds"
```

---

## 📝 Logging Integration

### **Structured Logging**

```python
import logging
import json
from datetime import datetime

class StructuredLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_agent_execution(self, agent_name, task, duration, status):
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'event': 'agent_execution',
            'agent_name': agent_name,
            'task': task,
            'duration_seconds': duration,
            'status': status
        }
        self.logger.info(json.dumps(log_entry))

# Usage
logger = StructuredLogger('framework')
logger.log_agent_execution('backend-engineer', 'Implement API', 45.2, 'success')
```

### **Log Aggregation (ELK Stack)**

```yaml
# filebeat.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/my-name-is-claude/*.log
    json.keys_under_root: true
    json.add_error_key: true

output.elasticsearch:
  hosts: ["localhost:9200"]
  index: "framework-%{+yyyy.MM.dd}"
```

---

## 🔍 Tracing (OpenTelemetry)

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, BatchSpanProcessor

# Setup tracing
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

span_processor = BatchSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

# Use tracing
def execute_agent_with_tracing(agent_name, task):
    with tracer.start_as_current_span("agent_execution") as span:
        span.set_attribute("agent.name", agent_name)
        span.set_attribute("task", task)

        result = execute_agent(agent_name, task)

        span.set_attribute("result.status", "success")
        return result
```

---

## 🔗 Related Documentation

- **[Monitoring & Analytics](monitoring-analytics.md)** - Framework monitoring guide
- **[Enterprise Deployment](enterprise-deployment.md)** - Production monitoring setup
- **[Performance Optimization](performance-optimization.md)** - Performance metrics

---

**Last Updated:** 2025-10-05 | **Version:** 3.3.0
