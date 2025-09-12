#!/bin/bash

# Agent Performance Monitor Hook
# Monitors performance and execution time of different agents
# Identifies bottlenecks in workflow and provides performance analytics

ACTION="${1:-start}"  # start, stop, report, analyze
AGENT_TYPE="${2:-unknown}"
TASK_ID="${3:-$(date +%Y%m%d_%H%M%S)}"

echo "⏱️ Agent Performance Monitor Hook - Action: $ACTION for $AGENT_TYPE..."

# Ensure work directory exists
mkdir -p work/performance

PERFORMANCE_FILE="work/performance/agent_performance.json"

# Initialize performance file if it doesn't exist
if [[ ! -f "$PERFORMANCE_FILE" ]]; then
    cat > "$PERFORMANCE_FILE" << 'EOF'
{
  "sessions": [],
  "agent_stats": {},
  "performance_history": []
}
EOF
fi

start_monitoring() {
    local agent="$1"
    local task_id="$2"
    
    echo "🚀 Starting performance monitoring for $agent (Task: $task_id)"
    
    # Create performance session record
    SESSION_FILE="work/performance/session_${task_id}.json"
    
    cat > "$SESSION_FILE" << EOF
{
  "task_id": "$task_id",
  "agent_type": "$agent",
  "start_time": "$(date -Iseconds)",
  "start_timestamp": $(date +%s),
  "end_time": null,
  "end_timestamp": null,
  "duration_seconds": null,
  "status": "running",
  "memory_usage": [],
  "cpu_usage": [],
  "deliverables_count": 0,
  "quality_score": null,
  "performance_notes": ""
}
EOF
    
    # Start background monitoring (if possible)
    if command -v ps >/dev/null 2>&1; then
        echo "📊 Collecting system metrics..."
        {
            while [[ -f "$SESSION_FILE" ]] && jq -e '.status == "running"' "$SESSION_FILE" > /dev/null 2>&1; do
                # Collect basic system metrics
                MEMORY_MB=$(free -m 2>/dev/null | awk 'NR==2{printf "%.2f", $3}' || echo "0")
                CPU_PERCENT=$(top -bn1 2>/dev/null | grep "Cpu(s)" | awk '{print $2}' | sed 's/%us,//' || echo "0")
                
                # Update session file with metrics
                tmp_file=$(mktemp)
                jq --arg mem "$MEMORY_MB" --arg cpu "$CPU_PERCENT" --arg time "$(date -Iseconds)" '
                    .memory_usage += [{"timestamp": $time, "memory_mb": ($mem | tonumber)}] |
                    .cpu_usage += [{"timestamp": $time, "cpu_percent": ($cpu | tonumber)}]
                ' "$SESSION_FILE" > "$tmp_file" && mv "$tmp_file" "$SESSION_FILE"
                
                sleep 30  # Collect metrics every 30 seconds
            done
        } &
        
        MONITOR_PID=$!
        echo "$MONITOR_PID" > "work/performance/monitor_${task_id}.pid"
    fi
    
    echo "📄 Performance session started: $SESSION_FILE"
}

stop_monitoring() {
    local agent="$1"
    local task_id="$2"
    
    echo "⏹️ Stopping performance monitoring for $agent (Task: $task_id)"
    
    SESSION_FILE="work/performance/session_${task_id}.json"
    PID_FILE="work/performance/monitor_${task_id}.pid"
    
    if [[ ! -f "$SESSION_FILE" ]]; then
        echo "❌ No performance session found for task: $task_id"
        return 1
    fi
    
    # Stop background monitoring
    if [[ -f "$PID_FILE" ]]; then
        MONITOR_PID=$(cat "$PID_FILE")
        if kill "$MONITOR_PID" 2>/dev/null; then
            echo "🛑 Background monitoring stopped (PID: $MONITOR_PID)"
        fi
        rm -f "$PID_FILE"
    fi
    
    # Update session with end time
    END_TIME=$(date -Iseconds)
    END_TIMESTAMP=$(date +%s)
    START_TIMESTAMP=$(jq -r '.start_timestamp' "$SESSION_FILE")
    DURATION=$((END_TIMESTAMP - START_TIMESTAMP))
    
    # Count deliverables (rough estimate based on files created)
    DELIVERABLES_COUNT=0
    if [[ -d "work" ]]; then
        DELIVERABLES_COUNT=$(find work -name "*.md" -newer "$SESSION_FILE" 2>/dev/null | wc -l)
    fi
    
    # Update session file
    tmp_file=$(mktemp)
    jq --arg end_time "$END_TIME" --arg end_ts "$END_TIMESTAMP" --arg duration "$DURATION" --arg deliverables "$DELIVERABLES_COUNT" '
        .end_time = $end_time |
        .end_timestamp = ($end_ts | tonumber) |
        .duration_seconds = ($duration | tonumber) |
        .deliverables_count = ($deliverables | tonumber) |
        .status = "completed"
    ' "$SESSION_FILE" > "$tmp_file" && mv "$tmp_file" "$SESSION_FILE"
    
    # Calculate performance metrics
    calculate_performance_score "$SESSION_FILE"
    
    # Update global performance stats
    update_global_stats "$agent" "$SESSION_FILE"
    
    echo "📊 Performance monitoring completed. Duration: ${DURATION}s"
}

calculate_performance_score() {
    local session_file="$1"
    
    # Calculate quality score based on various factors
    DURATION=$(jq -r '.duration_seconds' "$session_file")
    DELIVERABLES=$(jq -r '.deliverables_count' "$session_file")
    
    # Simple scoring algorithm (can be enhanced)
    SCORE=100
    
    # Penalize very long tasks (over 1 hour)
    if [[ $DURATION -gt 3600 ]]; then
        SCORE=$((SCORE - 20))
    fi
    
    # Reward deliverable creation
    if [[ $DELIVERABLES -gt 0 ]]; then
        SCORE=$((SCORE + DELIVERABLES * 5))
    fi
    
    # Cap score at 100
    if [[ $SCORE -gt 100 ]]; then
        SCORE=100
    fi
    
    # Update session file with score
    tmp_file=$(mktemp)
    jq --arg score "$SCORE" '.quality_score = ($score | tonumber)' "$session_file" > "$tmp_file" && mv "$tmp_file" "$session_file"
    
    echo "🏆 Performance score calculated: $SCORE/100"
}

update_global_stats() {
    local agent="$1"
    local session_file="$2"
    
    # Read session data
    DURATION=$(jq -r '.duration_seconds' "$session_file")
    SCORE=$(jq -r '.quality_score' "$session_file")
    DELIVERABLES=$(jq -r '.deliverables_count' "$session_file")
    
    # Update global performance file
    tmp_file=$(mktemp)
    jq --arg agent "$agent" --arg duration "$DURATION" --arg score "$SCORE" --arg deliverables "$DELIVERABLES" --arg timestamp "$(date -Iseconds)" '
        # Add to performance history
        .performance_history += [{
            "agent": $agent,
            "timestamp": $timestamp,
            "duration_seconds": ($duration | tonumber),
            "quality_score": ($score | tonumber),
            "deliverables_count": ($deliverables | tonumber)
        }] |
        
        # Update agent stats
        .agent_stats[$agent] = {
            "total_sessions": ((.agent_stats[$agent].total_sessions // 0) + 1),
            "total_duration": ((.agent_stats[$agent].total_duration // 0) + ($duration | tonumber)),
            "average_duration": (((.agent_stats[$agent].total_duration // 0) + ($duration | tonumber)) / ((.agent_stats[$agent].total_sessions // 0) + 1)),
            "average_score": (((.agent_stats[$agent].average_score // 0) * (.agent_stats[$agent].total_sessions // 0) + ($score | tonumber)) / ((.agent_stats[$agent].total_sessions // 0) + 1)),
            "total_deliverables": ((.agent_stats[$agent].total_deliverables // 0) + ($deliverables | tonumber)),
            "last_activity": $timestamp
        }
    ' "$PERFORMANCE_FILE" > "$tmp_file" && mv "$tmp_file" "$PERFORMANCE_FILE"
    
    echo "📈 Global performance stats updated for $agent"
}

generate_performance_report() {
    local agent_filter="${1:-all}"
    
    echo "📋 Generating performance report for: $agent_filter"
    
    REPORT_FILE="work/performance/performance_report_$(date +%Y%m%d_%H%M%S).md"
    
    cat > "$REPORT_FILE" << EOF
# Agent Performance Report

**Generated:** $(date)
**Filter:** $agent_filter

## Executive Summary

EOF

    # Add summary statistics
    if [[ "$agent_filter" == "all" ]]; then
        cat >> "$REPORT_FILE" << EOF
### Overall Performance Metrics

$(
if [[ -f "$PERFORMANCE_FILE" ]]; then
    TOTAL_SESSIONS=$(jq -r '.performance_history | length' "$PERFORMANCE_FILE")
    if [[ $TOTAL_SESSIONS -gt 0 ]]; then
        AVERAGE_DURATION=$(jq -r '.performance_history | map(.duration_seconds) | add / length' "$PERFORMANCE_FILE")
        AVERAGE_SCORE=$(jq -r '.performance_history | map(.quality_score) | add / length' "$PERFORMANCE_FILE")
        
        echo "- **Total Sessions:** $TOTAL_SESSIONS"
        echo "- **Average Task Duration:** ${AVERAGE_DURATION%.*} seconds"
        echo "- **Average Quality Score:** ${AVERAGE_SCORE%.*}/100"
    else
        echo "- **Status:** No performance data available yet"
    fi
else
    echo "- **Status:** Performance monitoring not initialized"
fi
)

### Agent Performance Breakdown

$(
if [[ -f "$PERFORMANCE_FILE" ]] && jq -e '.agent_stats | keys | length > 0' "$PERFORMANCE_FILE" >/dev/null 2>&1; then
    echo "| Agent | Sessions | Avg Duration | Avg Score | Total Deliverables |"
    echo "|-------|----------|--------------|-----------|-------------------|"
    
    jq -r '.agent_stats | to_entries[] | [.key, .value.total_sessions, (.value.average_duration | floor), (.value.average_score | floor), .value.total_deliverables] | @tsv' "$PERFORMANCE_FILE" | while IFS=$'\t' read -r agent sessions duration score deliverables; do
        echo "| $agent | $sessions | ${duration}s | ${score}/100 | $deliverables |"
    done
else
    echo "No agent performance data available."
fi
)

EOF
    fi
    
    # Add recent activity
    cat >> "$REPORT_FILE" << EOF

## Recent Activity

$(
if [[ -f "$PERFORMANCE_FILE" ]]; then
    echo "### Last 10 Sessions"
    echo ""
    echo "| Agent | Start Time | Duration | Score | Deliverables |"
    echo "|-------|------------|----------|-------|--------------|"
    
    jq -r '.performance_history | sort_by(.timestamp) | reverse | limit(10; .[]) | [.agent, .timestamp, .duration_seconds, .quality_score, .deliverables_count] | @tsv' "$PERFORMANCE_FILE" | while IFS=$'\t' read -r agent timestamp duration score deliverables; do
        formatted_time=$(date -d "$timestamp" "+%Y-%m-%d %H:%M" 2>/dev/null || echo "$timestamp")
        echo "| $agent | $formatted_time | ${duration}s | ${score}/100 | $deliverables |"
    done
else
    echo "No recent activity data available."
fi
)

## Performance Insights

### Top Performers
$(
if [[ -f "$PERFORMANCE_FILE" ]] && jq -e '.agent_stats | keys | length > 0' "$PERFORMANCE_FILE" >/dev/null 2>&1; then
    echo ""
    echo "**Fastest Average Execution:**"
    jq -r '.agent_stats | to_entries | sort_by(.value.average_duration) | limit(3; .[]) | "- " + .key + ": " + (.value.average_duration | floor | tostring) + "s average"' "$PERFORMANCE_FILE"
    
    echo ""
    echo "**Highest Quality Scores:**"
    jq -r '.agent_stats | to_entries | sort_by(.value.average_score) | reverse | limit(3; .[]) | "- " + .key + ": " + (.value.average_score | floor | tostring) + "/100 average"' "$PERFORMANCE_FILE"
    
    echo ""
    echo "**Most Productive (Deliverables):**"
    jq -r '.agent_stats | to_entries | sort_by(.value.total_deliverables) | reverse | limit(3; .[]) | "- " + .key + ": " + (.value.total_deliverables | tostring) + " total deliverables"' "$PERFORMANCE_FILE"
else
    echo "Insufficient data for performance insights."
fi
)

### Recommendations

#### Performance Optimization
- Monitor agents with consistently long execution times
- Investigate quality score patterns and improvement opportunities
- Consider workload distribution based on agent strengths

#### Workflow Enhancement  
- Standardize high-performing agent workflows
- Implement performance benchmarks for each agent type
- Create performance-based task assignment strategies

## Performance Trends

$(
if [[ -f "$PERFORMANCE_FILE" ]] && jq -e '.performance_history | length > 5' "$PERFORMANCE_FILE" >/dev/null 2>&1; then
    echo "### Recent Trend Analysis"
    echo ""
    
    RECENT_AVG=$(jq -r '.performance_history | sort_by(.timestamp) | reverse | limit(5; .[]) | map(.quality_score) | add / length' "$PERFORMANCE_FILE")
    OLDER_AVG=$(jq -r '.performance_history | sort_by(.timestamp) | reverse | .[5:10] | map(.quality_score) | add / length' "$PERFORMANCE_FILE")
    
    if [[ "$RECENT_AVG" != "null" && "$OLDER_AVG" != "null" ]]; then
        if (( $(echo "$RECENT_AVG > $OLDER_AVG" | bc -l) )); then
            echo "📈 **Quality Trend:** Improving (Recent: ${RECENT_AVG%.*}, Previous: ${OLDER_AVG%.*})"
        elif (( $(echo "$RECENT_AVG < $OLDER_AVG" | bc -l) )); then
            echo "📉 **Quality Trend:** Declining (Recent: ${RECENT_AVG%.*}, Previous: ${OLDER_AVG%.*})"
        else
            echo "📊 **Quality Trend:** Stable (Recent: ${RECENT_AVG%.*})"
        fi
    fi
else
    echo "Insufficient data for trend analysis."
fi
)

EOF

    echo "📄 Performance report generated: $REPORT_FILE"
}

# Main execution logic
case "$ACTION" in
    "start")
        start_monitoring "$AGENT_TYPE" "$TASK_ID"
        echo "Task ID for stopping: $TASK_ID"
        ;;
        
    "stop")
        stop_monitoring "$AGENT_TYPE" "$TASK_ID"
        ;;
        
    "report")
        generate_performance_report "$AGENT_TYPE"
        ;;
        
    "analyze")
        echo "📊 Performance Analysis Summary:"
        if [[ -f "$PERFORMANCE_FILE" ]]; then
            TOTAL_SESSIONS=$(jq -r '.performance_history | length' "$PERFORMANCE_FILE")
            if [[ $TOTAL_SESSIONS -gt 0 ]]; then
                echo "  Total monitored sessions: $TOTAL_SESSIONS"
                echo "  Active agents: $(jq -r '.agent_stats | keys | length' "$PERFORMANCE_FILE")"
                echo "  Average session duration: $(jq -r '.performance_history | map(.duration_seconds) | add / length' "$PERFORMANCE_FILE" | cut -d. -f1)s"
                echo "  Average quality score: $(jq -r '.performance_history | map(.quality_score) | add / length' "$PERFORMANCE_FILE" | cut -d. -f1)/100"
            else
                echo "  No performance data available"
            fi
        else
            echo "  Performance monitoring not yet initialized"
        fi
        ;;
        
    *)
        echo "❌ Unknown action: $ACTION"
        echo "Available actions: start, stop, report, analyze"
        exit 1
        ;;
esac

# Log activity
echo "$(date): Agent performance monitoring $ACTION for $AGENT_TYPE (Task: $TASK_ID)" >> work/performance-activity.log

echo "✅ Agent Performance Monitor Hook completed"