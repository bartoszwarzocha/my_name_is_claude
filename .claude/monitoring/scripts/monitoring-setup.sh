#!/bin/bash

# =============================================================================
# Claude Code Framework Monitoring Setup Script
# =============================================================================

set -e

# =============================================================================
# CONFIGURATION
# =============================================================================

readonly SCRIPT_VERSION="1.0.0"
readonly MONITORING_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
readonly DASHBOARDS_DIR="$MONITORING_DIR/dashboards"
readonly METRICS_DIR="$MONITORING_DIR/metrics"
readonly SCRIPTS_DIR="$MONITORING_DIR/scripts"

# Colors for output
readonly COLOR_RED=$(tput setaf 1)
readonly COLOR_GREEN=$(tput setaf 2)
readonly COLOR_YELLOW=$(tput setaf 3)
readonly COLOR_BLUE=$(tput setaf 4)
readonly COLOR_CYAN=$(tput setaf 6)
readonly COLOR_RESET=$(tput sgr0)

# Icons
readonly ICON_SUCCESS="✅"
readonly ICON_ERROR="❌"
readonly ICON_WARNING="⚠️"
readonly ICON_INFO="ℹ️"
readonly ICON_ROCKET="🚀"

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

print_header() {
    echo ""
    echo "${COLOR_BLUE}===============================================================================${COLOR_RESET}"
    echo "${COLOR_BLUE}${ICON_ROCKET} Claude Code Framework Monitoring Setup v${SCRIPT_VERSION}${COLOR_RESET}"
    echo "${COLOR_CYAN}Complete monitoring and analytics dashboard setup${COLOR_RESET}"
    echo "${COLOR_BLUE}===============================================================================${COLOR_RESET}"
    echo ""
}

print_status() {
    local status="$1"
    local message="$2"
    case "$status" in
        "success") echo "${ICON_SUCCESS} ${COLOR_GREEN}${message}${COLOR_RESET}" ;;
        "error")   echo "${ICON_ERROR} ${COLOR_RED}${message}${COLOR_RESET}" ;;
        "warning") echo "${ICON_WARNING} ${COLOR_YELLOW}${message}${COLOR_RESET}" ;;
        "info")    echo "${ICON_INFO} ${COLOR_CYAN}${message}${COLOR_RESET}" ;;
        *)         echo "${message}" ;;
    esac
}

check_dependencies() {
    print_status "info" "Checking system dependencies..."

    local missing_deps=()

    # Check for required commands
    for cmd in python3 docker docker-compose curl jq; do
        if ! command -v "$cmd" >/dev/null 2>&1; then
            missing_deps+=("$cmd")
        fi
    done

    if [[ ${#missing_deps[@]} -gt 0 ]]; then
        print_status "error" "Missing dependencies: ${missing_deps[*]}"
        echo ""
        echo "${COLOR_YELLOW}Please install missing dependencies:${COLOR_RESET}"
        echo "  ${COLOR_WHITE}Ubuntu/Debian: sudo apt update && sudo apt install python3 docker.io docker-compose curl jq${COLOR_RESET}"
        echo "  ${COLOR_WHITE}macOS: brew install python3 docker docker-compose curl jq${COLOR_RESET}"
        return 1
    fi

    print_status "success" "All dependencies found"
    return 0
}

setup_python_environment() {
    print_status "info" "Setting up Python monitoring environment..."

    # Create virtual environment for monitoring
    if [[ ! -d "$METRICS_DIR/venv" ]]; then
        python3 -m venv "$METRICS_DIR/venv"
        print_status "success" "Created Python virtual environment"
    fi

    # Activate virtual environment
    source "$METRICS_DIR/venv/bin/activate"

    # Install required packages
    pip install --quiet --upgrade pip
    pip install --quiet prometheus-client psutil flask requests

    print_status "success" "Python environment configured"
}

create_monitoring_config() {
    print_status "info" "Creating monitoring configuration files..."

    # Create Prometheus configuration
    cat > "$MONITORING_DIR/prometheus.yml" << EOF
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - "alerts.yml"

scrape_configs:
  - job_name: 'claude-framework'
    static_configs:
      - targets: ['localhost:8000']
    scrape_interval: 5s
    metrics_path: /metrics

  - job_name: 'claude-agents'
    static_configs:
      - targets: ['localhost:8001']
    scrape_interval: 10s

  - job_name: 'claude-ai-tools'
    static_configs:
      - targets: ['localhost:8002']
    scrape_interval: 30s

alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - alertmanager:9093
EOF

    # Create alert rules
    cat > "$MONITORING_DIR/alerts.yml" << EOF
groups:
  - name: claude-framework-alerts
    rules:
      - alert: HighErrorRate
        expr: claude_framework_error_rate > 5
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "High error rate detected"
          description: "Framework error rate is {{ \$value }}% for more than 2 minutes"

      - alert: LowAgentPerformance
        expr: rate(claude_agent_execution_duration_seconds[5m]) > 10
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Agent performance degradation"
          description: "Agent {{ \$labels.agent_name }} execution time is above 10 seconds"

      - alert: SystemResourceHigh
        expr: claude_framework_cpu_usage > 80
        for: 3m
        labels:
          severity: warning
        annotations:
          summary: "High system resource usage"
          description: "CPU usage is {{ \$value }}% for more than 3 minutes"

      - alert: FrameworkDown
        expr: up{job="claude-framework"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Claude Framework is down"
          description: "Framework has been down for more than 1 minute"
EOF

    # Create Docker Compose for monitoring stack
    cat > "$MONITORING_DIR/docker-compose.yml" << EOF
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    container_name: claude-prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - ./alerts.yml:/etc/prometheus/alerts.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
      - '--storage.tsdb.retention.time=200h'
      - '--web.enable-lifecycle'
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    container_name: claude-grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=claude-admin
      - GF_USERS_ALLOW_SIGN_UP=false
    volumes:
      - grafana_data:/var/lib/grafana
      - ./dashboards:/etc/grafana/provisioning/dashboards
      - ./datasources:/etc/grafana/provisioning/datasources
    restart: unless-stopped

  alertmanager:
    image: prom/alertmanager:latest
    container_name: claude-alertmanager
    ports:
      - "9093:9093"
    volumes:
      - ./alertmanager.yml:/etc/alertmanager/alertmanager.yml
      - alertmanager_data:/alertmanager
    restart: unless-stopped

volumes:
  prometheus_data:
  grafana_data:
  alertmanager_data:
EOF

    # Create Grafana datasource configuration
    mkdir -p "$MONITORING_DIR/datasources"
    cat > "$MONITORING_DIR/datasources/datasources.yml" << EOF
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://prometheus:9090
    isDefault: true
    editable: true
EOF

    # Create Grafana dashboard provisioning
    mkdir -p "$MONITORING_DIR/dashboards"
    cat > "$MONITORING_DIR/dashboards/dashboards.yml" << EOF
apiVersion: 1

providers:
  - name: 'claude-dashboards'
    orgId: 1
    folder: 'Claude Code Framework'
    type: file
    disableDeletion: false
    editable: true
    updateIntervalSeconds: 10
    allowUiUpdates: true
    options:
      path: /etc/grafana/provisioning/dashboards
EOF

    # Create AlertManager configuration
    cat > "$MONITORING_DIR/alertmanager.yml" << EOF
global:
  smtp_smarthost: 'localhost:587'
  smtp_from: 'alerts@claude-framework.local'

route:
  group_by: ['alertname']
  group_wait: 10s
  group_interval: 10s
  repeat_interval: 1h
  receiver: 'web.hook'

receivers:
  - name: 'web.hook'
    webhook_configs:
      - url: 'http://localhost:5001/webhook'
        send_resolved: true
EOF

    print_status "success" "Monitoring configuration files created"
}

setup_monitoring_stack() {
    print_status "info" "Setting up monitoring stack with Docker..."

    cd "$MONITORING_DIR"

    # Pull required images
    docker-compose pull

    # Start the monitoring stack
    docker-compose up -d

    # Wait for services to start
    sleep 10

    # Check if services are running
    if docker-compose ps | grep -q "Up"; then
        print_status "success" "Monitoring stack started successfully"
        echo ""
        echo "${COLOR_CYAN}Access points:${COLOR_RESET}"
        echo "  ${COLOR_GREEN}Grafana:${COLOR_RESET}     http://localhost:3000 (admin/claude-admin)"
        echo "  ${COLOR_GREEN}Prometheus:${COLOR_RESET}  http://localhost:9090"
        echo "  ${COLOR_GREEN}AlertManager:${COLOR_RESET} http://localhost:9093"
    else
        print_status "error" "Failed to start monitoring stack"
        return 1
    fi
}

start_metrics_collector() {
    print_status "info" "Starting metrics collector..."

    cd "$METRICS_DIR"
    source venv/bin/activate

    # Start metrics collector in background
    nohup python3 metrics-collector.py > collector.log 2>&1 &
    echo $! > collector.pid

    # Wait a moment and check if it's running
    sleep 2
    if kill -0 "$(cat collector.pid)" 2>/dev/null; then
        print_status "success" "Metrics collector started (PID: $(cat collector.pid))"
    else
        print_status "error" "Failed to start metrics collector"
        return 1
    fi
}

import_grafana_dashboards() {
    print_status "info" "Importing Grafana dashboards..."

    # Wait for Grafana to be ready
    local retries=30
    while ! curl -s http://localhost:3000/api/health >/dev/null 2>&1; do
        if [[ $retries -eq 0 ]]; then
            print_status "error" "Grafana not ready after 30 attempts"
            return 1
        fi
        sleep 1
        ((retries--))
    done

    # Copy dashboard JSON files to Grafana provisioning directory
    docker cp "$DASHBOARDS_DIR/executive-dashboard.json" claude-grafana:/etc/grafana/provisioning/dashboards/
    docker cp "$DASHBOARDS_DIR/operations-dashboard.json" claude-grafana:/etc/grafana/provisioning/dashboards/
    docker cp "$DASHBOARDS_DIR/developer-dashboard.json" claude-grafana:/etc/grafana/provisioning/dashboards/

    # Restart Grafana to reload dashboards
    docker-compose restart grafana

    print_status "success" "Dashboards imported to Grafana"
}

create_monitoring_service() {
    print_status "info" "Creating monitoring management script..."

    cat > "$SCRIPTS_DIR/monitor.sh" << 'EOF'
#!/bin/bash

MONITORING_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

case "$1" in
    start)
        echo "Starting Claude Code Framework monitoring..."
        cd "$MONITORING_DIR"
        docker-compose up -d
        cd "$MONITORING_DIR/metrics"
        source venv/bin/activate
        nohup python3 metrics-collector.py > collector.log 2>&1 &
        echo $! > collector.pid
        echo "Monitoring started successfully"
        ;;
    stop)
        echo "Stopping Claude Code Framework monitoring..."
        cd "$MONITORING_DIR"
        docker-compose down
        if [[ -f "$MONITORING_DIR/metrics/collector.pid" ]]; then
            kill $(cat "$MONITORING_DIR/metrics/collector.pid") 2>/dev/null || true
            rm -f "$MONITORING_DIR/metrics/collector.pid"
        fi
        echo "Monitoring stopped"
        ;;
    restart)
        $0 stop
        sleep 2
        $0 start
        ;;
    status)
        echo "Checking monitoring status..."
        cd "$MONITORING_DIR"
        docker-compose ps
        if [[ -f "$MONITORING_DIR/metrics/collector.pid" ]]; then
            if kill -0 $(cat "$MONITORING_DIR/metrics/collector.pid") 2>/dev/null; then
                echo "Metrics collector: Running (PID: $(cat "$MONITORING_DIR/metrics/collector.pid"))"
            else
                echo "Metrics collector: Not running"
            fi
        else
            echo "Metrics collector: Not running"
        fi
        ;;
    logs)
        echo "Showing monitoring logs..."
        cd "$MONITORING_DIR"
        docker-compose logs -f
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status|logs}"
        exit 1
        ;;
esac
EOF

    chmod +x "$SCRIPTS_DIR/monitor.sh"
    print_status "success" "Monitoring management script created"
}

# =============================================================================
# MAIN EXECUTION
# =============================================================================

main() {
    print_header

    # Check if running as root (not recommended)
    if [[ $EUID -eq 0 ]]; then
        print_status "warning" "Running as root is not recommended"
        read -p "Continue anyway? (y/N): " -r
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi

    echo "${COLOR_CYAN}This script will set up comprehensive monitoring for Claude Code Framework:${COLOR_RESET}"
    echo "  • Prometheus metrics collection"
    echo "  • Grafana dashboards (Executive, Operations, Developer)"
    echo "  • AlertManager for notifications"
    echo "  • Python metrics collector"
    echo ""

    read -p "Continue with monitoring setup? (Y/n): " -r
    if [[ $REPLY =~ ^[Nn]$ ]]; then
        echo "Setup cancelled."
        exit 0
    fi

    echo ""

    # Execute setup steps
    if ! check_dependencies; then
        exit 1
    fi

    setup_python_environment || exit 1
    create_monitoring_config || exit 1
    setup_monitoring_stack || exit 1
    start_metrics_collector || exit 1
    import_grafana_dashboards || exit 1
    create_monitoring_service || exit 1

    echo ""
    print_status "success" "Claude Code Framework monitoring setup completed!"
    echo ""
    echo "${COLOR_CYAN}${ICON_ROCKET} Quick Start:${COLOR_RESET}"
    echo "  ${COLOR_GREEN}View Dashboards:${COLOR_RESET}   http://localhost:3000"
    echo "  ${COLOR_GREEN}Monitor Metrics:${COLOR_RESET}   http://localhost:9090"
    echo "  ${COLOR_GREEN}Manage Service:${COLOR_RESET}    $SCRIPTS_DIR/monitor.sh {start|stop|status}"
    echo ""
    echo "${COLOR_YELLOW}Login Credentials:${COLOR_RESET}"
    echo "  ${COLOR_WHITE}Username: admin${COLOR_RESET}"
    echo "  ${COLOR_WHITE}Password: claude-admin${COLOR_RESET}"
    echo ""
    echo "${COLOR_CYAN}Available Dashboards:${COLOR_RESET}"
    echo "  • Executive Dashboard - High-level KPIs and business metrics"
    echo "  • Operations Dashboard - Technical performance and system health"
    echo "  • Developer Dashboard - Personal productivity and learning progress"
    echo ""
}

# Run main function
main "$@"