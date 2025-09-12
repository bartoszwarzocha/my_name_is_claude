#!/bin/bash

# Orchestration Monitor
# Real-time monitoring and management of running orchestration processes
# Provides status tracking, intervention capabilities, and performance metrics

echo "📡 Orchestration Monitor - Starting surveillance..."

# Configuration
MONITOR_MODE="${1:-status}"  # status, watch, kill, metrics, logs
TARGET_SCENARIO="${2:-}"     # Optional: specific scenario to monitor
WATCH_INTERVAL="${3:-10}"    # Seconds between status updates

# Ensure work directory exists
mkdir -p work/orchestration

MONITOR_LOG="work/orchestration/monitor-$(date +%Y%m%d_%H%M%S).log"

# Function to get running orchestration processes
get_running_orchestrations() {
    echo "🔍 Scanning for running orchestration processes..."
    
    # Look for orchestration scenario processes
    local running_processes=()
    
    # Check for orchestration scenario scripts
    mapfile -t running_processes < <(pgrep -f "orchestration.*scenario\.sh" 2>/dev/null)
    
    if [[ ${#running_processes[@]} -eq 0 ]]; then
        echo "ℹ️ No active orchestration processes found"
        return 1
    fi
    
    echo "📊 Found ${#running_processes[@]} running orchestration process(es):"
    
    for pid in "${running_processes[@]}"; do
        if ps -p "$pid" > /dev/null 2>&1; then
            local cmd
            cmd=$(ps -p "$pid" -o command= 2>/dev/null | head -1)
            local start_time
            start_time=$(ps -p "$pid" -o lstart= 2>/dev/null)
            
            echo "  🚀 PID: $pid"
            echo "     Command: $cmd"
            echo "     Started: $start_time"
            echo "     Duration: $(ps -p "$pid" -o etime= 2>/dev/null | tr -d ' ')"
        fi
    done
    
    return 0
}

# Function to get orchestration status from logs
get_orchestration_status() {
    echo "📋 Checking orchestration status from logs..."
    
    # Find recent orchestration logs
    local log_files=()
    mapfile -t log_files < <(find work/orchestration -name "*.log" -mtime -1 2>/dev/null | sort -r)
    
    if [[ ${#log_files[@]} -eq 0 ]]; then
        echo "ℹ️ No recent orchestration logs found"
        return 1
    fi
    
    echo "📊 Recent Orchestration Activity:"
    
    for log_file in "${log_files[@]:0:5}"; do  # Show last 5 logs
        local basename_log
        basename_log=$(basename "$log_file")
        local file_age
        file_age=$(stat -c %Y "$log_file" 2>/dev/null || echo "0")
        local current_time
        current_time=$(date +%s)
        local age_minutes=$(( (current_time - file_age) / 60 ))
        
        echo "  📄 $basename_log (${age_minutes}m ago)"
        
        # Extract key status information
        if grep -q "completed successfully" "$log_file" 2>/dev/null; then
            echo "     Status: ✅ COMPLETED"
        elif grep -q "failed\|error\|exit.*[1-9]" "$log_file" 2>/dev/null; then
            echo "     Status: ❌ FAILED"
        elif [[ $age_minutes -lt 30 ]] && ! grep -q "completed\|Summary" "$log_file" 2>/dev/null; then
            echo "     Status: 🟡 IN PROGRESS"
        else
            echo "     Status: ❓ UNKNOWN"
        fi
        
        # Show current phase if available
        local current_phase
        current_phase=$(grep "Phase [0-9]" "$log_file" 2>/dev/null | tail -1)
        if [[ -n "$current_phase" ]]; then
            echo "     Phase: $current_phase"
        fi
        
        # Show agent activity
        local agent_count
        agent_count=$(grep -c "Started.*agent" "$log_file" 2>/dev/null)
        if [[ $agent_count -gt 0 ]]; then
            echo "     Agents: $agent_count agents involved"
        fi
    done
    
    return 0
}

# Function to show orchestration metrics
show_orchestration_metrics() {
    echo "📊 Orchestration Performance Metrics"
    
    # Ensure metrics directory exists
    mkdir -p work/orchestration/metrics
    
    local metrics_file="work/orchestration/metrics/metrics-$(date +%Y%m%d).md"
    
    # Calculate metrics from logs
    local total_orchestrations=0
    local successful_orchestrations=0
    local failed_orchestrations=0
    local avg_duration=0
    
    # Find all orchestration logs from today and yesterday
    mapfile -t recent_logs < <(find work/orchestration -name "*-report-*.md" -mtime -2 2>/dev/null)
    
    total_orchestrations=${#recent_logs[@]}
    
    for report in "${recent_logs[@]}"; do
        if grep -q "COMPLETED.*SUCCESSFULLY\|✅.*Status.*COMPLETED" "$report" 2>/dev/null; then
            successful_orchestrations=$((successful_orchestrations + 1))
        elif grep -q "FAILED\|❌.*Status.*FAILED" "$report" 2>/dev/null; then
            failed_orchestrations=$((failed_orchestrations + 1))
        fi
    done
    
    # Generate metrics report
    cat > "$metrics_file" << EOF
# Orchestration Metrics Report

**Generated:** $(date)
**Period:** Last 48 hours

## Overall Performance

| Metric | Value | Status |
|--------|-------|--------|
| Total Orchestrations | $total_orchestrations | $(if [[ $total_orchestrations -gt 0 ]]; then echo "📊 Active"; else echo "📭 No Activity"; fi) |
| Successful | $successful_orchestrations | $(if [[ $successful_orchestrations -eq $total_orchestrations && $total_orchestrations -gt 0 ]]; then echo "✅ Perfect"; elif [[ $successful_orchestrations -gt 0 ]]; then echo "🟢 Good"; else echo "🔴 Poor"; fi) |
| Failed | $failed_orchestrations | $(if [[ $failed_orchestrations -eq 0 ]]; then echo "✅ None"; else echo "⚠️ Review Needed"; fi) |
| Success Rate | $(if [[ $total_orchestrations -gt 0 ]]; then echo "scale=1; $successful_orchestrations * 100 / $total_orchestrations" | bc; else echo "N/A"; fi)% | $(if [[ $total_orchestrations -gt 0 ]] && [[ $((successful_orchestrations * 100 / total_orchestrations)) -ge 80 ]]; then echo "🎯 Excellent"; elif [[ $total_orchestrations -gt 0 ]]; then echo "⚠️ Needs Improvement"; else echo "📊 No Data"; fi) |

## Scenario Breakdown

EOF

    # Analyze by scenario type
    local mvp_count=0
    local security_count=0
    local data_count=0
    
    for report in "${recent_logs[@]}"; do
        if [[ "$report" == *"rapid-mvp"* ]]; then
            mvp_count=$((mvp_count + 1))
        elif [[ "$report" == *"enterprise-security"* ]]; then
            security_count=$((security_count + 1))
        elif [[ "$report" == *"data-driven"* ]]; then
            data_count=$((data_count + 1))
        fi
    done
    
    cat >> "$metrics_file" << EOF
### By Scenario Type

- **Rapid MVP:** $mvp_count orchestrations
- **Enterprise Security:** $security_count orchestrations  
- **Data-Driven:** $data_count orchestrations

## Quality Metrics

### Quality Gate Performance
$(
    # Calculate quality gate metrics from logs
    local total_gates=0
    local passed_gates=0
    
    for log in work/orchestration/*.log 2>/dev/null; do
        if [[ -f "$log" ]]; then
            local gates_in_log
            gates_in_log=$(grep -c "quality gate.*passed\|✅.*Phase.*completed" "$log" 2>/dev/null)
            local failed_gates_in_log
            failed_gates_in_log=$(grep -c "quality gate.*failed\|⚠️.*Phase.*failed" "$log" 2>/dev/null)
            
            total_gates=$((total_gates + gates_in_log + failed_gates_in_log))
            passed_gates=$((passed_gates + gates_in_log))
        fi
    done
    
    echo "- Total Quality Gates: $total_gates"
    echo "- Passed Gates: $passed_gates"
    if [[ $total_gates -gt 0 ]]; then
        echo "- Gate Success Rate: $(echo "scale=1; $passed_gates * 100 / $total_gates" | bc)%"
    fi
)

### Agent Utilization
$(
    # Count agent usage from activity logs
    if [[ -f "work/agent-activity.log" ]]; then
        echo "- Most Active Agents:"
        grep -o "Agent: [a-zA-Z-]*" work/agent-activity.log 2>/dev/null | sort | uniq -c | sort -nr | head -3 | while read count agent; do
            echo "  - ${agent#Agent: }: $count activities"
        done
    fi
)

## Recommendations

### Performance Optimization
$(
if [[ $failed_orchestrations -gt 0 ]]; then
    echo "- 🔍 **Review Failed Orchestrations:** Analyze failure patterns and root causes"
fi

if [[ $total_orchestrations -gt 5 ]] && [[ $((successful_orchestrations * 100 / total_orchestrations)) -lt 90 ]]; then
    echo "- ⚡ **Improve Success Rate:** Consider quality gate tuning and validation improvements"
fi

echo "- 📊 **Monitor Trends:** Regular metrics review for continuous improvement"
echo "- 🎯 **Optimize Scenarios:** Consider scenario-specific optimizations based on usage patterns"
)

### Next Actions
- Review orchestration reports for detailed analysis
- Consider automation improvements based on failure patterns
- Monitor resource usage and performance trends
- Plan scenario enhancements based on usage data

EOF

    echo "📊 Metrics report generated: $metrics_file"
    
    # Display summary
    echo ""
    echo "📈 Performance Summary:"
    echo "   Total Orchestrations: $total_orchestrations"
    echo "   Success Rate: $(if [[ $total_orchestrations -gt 0 ]]; then echo "scale=1; $successful_orchestrations * 100 / $total_orchestrations" | bc; else echo "N/A"; fi)%"
    echo "   Most Used Scenario: $(
        if [[ $mvp_count -ge $security_count && $mvp_count -ge $data_count ]]; then
            echo "Rapid MVP ($mvp_count)"
        elif [[ $security_count -ge $data_count ]]; then
            echo "Enterprise Security ($security_count)"
        else
            echo "Data-Driven ($data_count)"
        fi
    )"
}

# Function to watch orchestration in real-time
watch_orchestration() {
    echo "👀 Starting real-time orchestration monitoring..."
    echo "Press Ctrl+C to stop monitoring"
    
    while true; do
        clear
        echo "🔄 Orchestration Monitor - $(date)"
        echo "=================================="
        
        get_running_orchestrations
        echo ""
        get_orchestration_status
        
        # Show recent log tail if available
        local latest_log
        latest_log=$(find work/orchestration -name "*.log" -mtime -1 2>/dev/null | head -1)
        
        if [[ -n "$latest_log" ]]; then
            echo ""
            echo "📋 Latest Activity ($(basename "$latest_log")):"
            tail -3 "$latest_log" 2>/dev/null | sed 's/^/   /'
        fi
        
        echo ""
        echo "🔄 Refreshing in ${WATCH_INTERVAL}s... (Ctrl+C to exit)"
        sleep "$WATCH_INTERVAL"
    done
}

# Function to kill orchestration processes
kill_orchestration() {
    echo "🛑 Orchestration Process Termination"
    
    # Get running processes
    local running_pids=()
    mapfile -t running_pids < <(pgrep -f "orchestration.*scenario\.sh" 2>/dev/null)
    
    if [[ ${#running_pids[@]} -eq 0 ]]; then
        echo "ℹ️ No active orchestration processes to terminate"
        return 0
    fi
    
    echo "⚠️ Found ${#running_pids[@]} running orchestration process(es)"
    
    for pid in "${running_pids[@]}"; do
        local cmd
        cmd=$(ps -p "$pid" -o command= 2>/dev/null | head -1)
        echo "  🎯 PID: $pid - $cmd"
    done
    
    if [[ -n "$TARGET_SCENARIO" ]]; then
        echo "🎯 Targeting specific scenario: $TARGET_SCENARIO"
        # Filter PIDs for specific scenario
        local filtered_pids=()
        for pid in "${running_pids[@]}"; do
            if ps -p "$pid" -o command= 2>/dev/null | grep -q "$TARGET_SCENARIO"; then
                filtered_pids+=("$pid")
            fi
        done
        running_pids=("${filtered_pids[@]}")
    fi
    
    if [[ ${#running_pids[@]} -eq 0 ]]; then
        echo "ℹ️ No matching processes found for scenario: $TARGET_SCENARIO"
        return 0
    fi
    
    read -p "⚠️ Terminate ${#running_pids[@]} orchestration process(es)? (y/N): " -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        for pid in "${running_pids[@]}"; do
            echo "🛑 Terminating PID: $pid"
            kill "$pid" 2>/dev/null
            
            # Wait for graceful termination
            sleep 2
            
            # Force kill if still running
            if ps -p "$pid" > /dev/null 2>&1; then
                echo "💀 Force killing PID: $pid"
                kill -9 "$pid" 2>/dev/null
            fi
            
            if ! ps -p "$pid" > /dev/null 2>&1; then
                echo "✅ Successfully terminated PID: $pid"
                echo "$(date): Terminated orchestration PID: $pid" >> "$MONITOR_LOG"
            else
                echo "❌ Failed to terminate PID: $pid"
            fi
        done
    else
        echo "🚫 Termination cancelled"
    fi
}

# Function to show recent orchestration logs
show_orchestration_logs() {
    echo "📋 Recent Orchestration Logs"
    
    local log_type="${TARGET_SCENARIO:-all}"
    local pattern="*.log"
    
    if [[ "$TARGET_SCENARIO" != "all" && -n "$TARGET_SCENARIO" ]]; then
        pattern="*${TARGET_SCENARIO}*.log"
    fi
    
    mapfile -t log_files < <(find work/orchestration -name "$pattern" -mtime -1 2>/dev/null | sort -r)
    
    if [[ ${#log_files[@]} -eq 0 ]]; then
        echo "ℹ️ No recent orchestration logs found for: $log_type"
        return 0
    fi
    
    echo "📊 Found ${#log_files[@]} recent log file(s):"
    
    for i in "${!log_files[@]}"; do
        local log_file="${log_files[$i]}"
        local basename_log
        basename_log=$(basename "$log_file")
        
        echo ""
        echo "📄 [$((i+1))] $basename_log"
        echo "    Last modified: $(stat -c %y "$log_file" 2>/dev/null)"
        echo "    Size: $(stat -c %s "$log_file" 2>/dev/null) bytes"
        
        # Show last few lines
        echo "    Recent activity:"
        tail -3 "$log_file" 2>/dev/null | sed 's/^/      /'
        
        if [[ $i -ge 4 ]]; then  # Limit to 5 logs
            echo "    ... and $((${#log_files[@]} - i - 1)) more files"
            break
        fi
    done
    
    echo ""
    read -p "📖 View full log? Enter number (1-$((i+1))) or press Enter to exit: " -r selection
    
    if [[ "$selection" =~ ^[0-9]+$ ]] && [[ "$selection" -ge 1 && "$selection" -le $((i+1)) ]]; then
        local selected_log="${log_files[$((selection-1))]}"
        echo ""
        echo "📖 Full log: $(basename "$selected_log")"
        echo "=================================="
        cat "$selected_log"
    fi
}

# Main monitor logic
main() {
    echo "📡 Orchestration Monitor - Mode: $MONITOR_MODE"
    echo "$(date): Monitor started - Mode: $MONITOR_MODE" >> "$MONITOR_LOG"
    
    case "$MONITOR_MODE" in
        "status")
            get_running_orchestrations
            echo ""
            get_orchestration_status
            ;;
        "watch")
            watch_orchestration
            ;;
        "kill"|"stop"|"terminate")
            kill_orchestration
            ;;
        "metrics"|"performance")
            show_orchestration_metrics
            ;;
        "logs"|"log")
            show_orchestration_logs
            ;;
        *)
            echo "❓ Unknown monitor mode: $MONITOR_MODE"
            echo ""
            echo "Available modes:"
            echo "  status     - Show current orchestration status"
            echo "  watch      - Real-time monitoring"
            echo "  kill       - Terminate running orchestrations"
            echo "  metrics    - Show performance metrics"
            echo "  logs       - Show recent orchestration logs"
            echo ""
            echo "Usage examples:"
            echo "  $0 status"
            echo "  $0 watch rapid-mvp 5"
            echo "  $0 kill enterprise-security"
            echo "  $0 metrics"
            echo "  $0 logs data-driven"
            exit 1
            ;;
    esac
    
    echo "$(date): Monitor completed - Mode: $MONITOR_MODE" >> "$MONITOR_LOG"
}

# Handle Ctrl+C gracefully in watch mode
trap 'echo ""; echo "🛑 Monitor stopped"; exit 0' INT

# Execute main function
main "$@"