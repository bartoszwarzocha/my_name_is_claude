# Model Configuration System - Integration Guide

**Target Audience:** Framework Developers, DevOps Engineers, System Integrators
**Complexity:** Intermediate to Advanced
**Estimated Integration Time:** 2-4 hours

## 📋 Table of Contents

1. [Integration Overview](#integration-overview)
2. [Prerequisites](#prerequisites)
3. [Step-by-Step Integration](#step-by-step-integration)
4. [Configuration Validation](#configuration-validation)
5. [Testing & Verification](#testing--verification)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Integration](#advanced-integration)

## 🎯 Integration Overview

The Model Configuration System integrates with Claude Code framework through:

1. **Environment Configuration** - Setting up environment variables
2. **Agent Integration** - Connecting agents to model profiles
3. **Cost Tracking** - Implementing usage monitoring
4. **Workflow Integration** - Embedding in development workflows

### Integration Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Claude Code Framework                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐    ┌──────────────────────────┐    │
│  │   Agents     │───▶│  Model Configuration     │    │
│  │  (45 total)  │    │      System              │    │
│  └──────────────┘    └──────────────────────────┘    │
│         │                      │                      │
│         │                      ▼                      │
│         │            ┌──────────────────┐            │
│         │            │ Profile Selector │            │
│         │            └──────────────────┘            │
│         │                      │                      │
│         │                      ▼                      │
│         │            ┌──────────────────┐            │
│         └───────────▶│  Claude API      │            │
│                      │  (Opus/Sonnet/   │            │
│                      │   Haiku)         │            │
│                      └──────────────────┘            │
│                               │                       │
│                               ▼                       │
│                      ┌──────────────────┐            │
│                      │  Cost Tracker    │            │
│                      └──────────────────┘            │
└─────────────────────────────────────────────────────────┘
```

## ✅ Prerequisites

Before integrating the Model Configuration System:

### 1. Framework Requirements

- **Claude Code Framework** v3.2.1 or higher
- **MCP Tools** properly configured (Serena, Context7)
- **Git** repository initialized
- **bash** shell (Linux, macOS, or WSL on Windows)

### 2. Environment Setup

```bash
# Verify framework installation
claude --version

# Check configuration directory
ls -la .claude/config/

# Verify agent structure
ls -la .claude/agents/
```

### 3. API Access

- Valid Claude API key
- API rate limits understood
- Billing account configured

## 🔧 Step-by-Step Integration

### Step 1: Environment Configuration

Create `.env` file in project root (or use existing):

```bash
# .env
# Model Configuration System Settings

# Default profile for all agents (fast, balanced, quality)
CLAUDE_DEFAULT_PROFILE="balanced"

# Project scale determines budget and optimization strategy
CLAUDE_PROJECT_SCALE="startup"  # or "sme", "enterprise"

# Enable cost optimization features
CLAUDE_COST_OPTIMIZATION="true"

# Budget limits (USD)
CLAUDE_DAILY_BUDGET="50"
CLAUDE_WEEKLY_BUDGET="300"
CLAUDE_MONTHLY_BUDGET="1000"

# Auto-downgrade when approaching budget limits
CLAUDE_AUTO_DOWNGRADE="true"

# Budget warning thresholds (0.0 to 1.0)
CLAUDE_WARNING_THRESHOLD="0.75"
CLAUDE_CRITICAL_THRESHOLD="0.90"

# Cost tracking
CLAUDE_TRACK_COSTS="true"
CLAUDE_COST_LOG_FILE=".claude/logs/cost-tracking.json"

# Caching (for cost optimization)
CLAUDE_ENABLE_CACHE="true"
CLAUDE_CACHE_DURATION="24h"

# Alert channels
CLAUDE_ALERT_CONSOLE="true"
CLAUDE_ALERT_LOG="true"
CLAUDE_ALERT_EMAIL="false"
```

Load environment variables:

```bash
# Add to your shell profile (.bashrc, .zshrc, etc.)
export $(cat .env | grep -v '^#' | xargs)

# Or source it explicitly
source .env
```

### Step 2: Agent Configuration

Each agent in `.claude/agents/` automatically uses the profile defined in `agent-model-mapping.json`.

**Verify agent configuration:**

```bash
# Check agent profile assignment
cat .claude/config/agent-model-mapping.json | jq '.agentMappings["software-architect"]'

# Expected output:
# {
#   "defaultProfile": "quality",
#   "reasoning": "Architecture decisions require maximum quality...",
#   ...
# }
```

**Custom agent integration:**

If you have custom agents, add them to `agent-model-mapping.json`:

```json
{
  "agentMappings": {
    "your-custom-agent": {
      "defaultProfile": "balanced",
      "reasoning": "Your reasoning for profile selection",
      "taskSpecificOverrides": {
        "complex_task": "quality",
        "simple_task": "fast"
      },
      "estimatedCostImpact": "moderate",
      "businessValue": "high"
    }
  }
}
```

### Step 3: Workflow Integration

Integrate model configuration into your development workflows.

**Example: Pre-commit Hook**

Create `.claude/hooks/pre-commit-model-check.sh`:

```bash
#!/bin/bash
# Pre-commit hook to check model configuration

# Source configuration
source .env

# Check budget status
current_usage=$(claude config cost-report --period today --format json | jq '.utilization')

if (( $(echo "$current_usage > $CLAUDE_CRITICAL_THRESHOLD" | bc -l) )); then
    echo "⚠️  WARNING: Daily budget at ${current_usage}%"
    echo "Consider using Fast profile for remaining tasks"
fi

# Suggest profile based on commit type
commit_msg=$(cat "$1")

if [[ $commit_msg =~ ^(feat|feature): ]]; then
    echo "💡 Suggested profile: balanced (feature development)"
elif [[ $commit_msg =~ ^(fix|hotfix): ]]; then
    echo "💡 Suggested profile: fast (bug fix)"
elif [[ $commit_msg =~ ^(arch|refactor): ]]; then
    echo "💡 Suggested profile: quality (architecture change)"
fi

exit 0
```

Make it executable:

```bash
chmod +x .claude/hooks/pre-commit-model-check.sh
```

### Step 4: Cost Tracking Setup

Enable cost tracking and create log directory:

```bash
# Create logs directory
mkdir -p .claude/logs

# Initialize cost tracking file
echo '{"sessions": []}' > .claude/logs/cost-tracking.json

# Set up log rotation (optional)
cat > .claude/logs/rotate-costs.sh << 'EOF'
#!/bin/bash
# Rotate cost logs monthly
log_file=".claude/logs/cost-tracking.json"
archive_dir=".claude/logs/archive"
mkdir -p "$archive_dir"

# Archive previous month's data
month=$(date -d "last month" +%Y-%m)
jq ".sessions[] | select(.date | startswith(\"$month\"))" "$log_file" > "$archive_dir/costs-$month.json"

# Keep only current month in main log
current_month=$(date +%Y-%m)
jq ".sessions[] | select(.date | startswith(\"$current_month\"))" "$log_file" > "$log_file.tmp"
echo "{\"sessions\": $(cat $log_file.tmp | jq -s .)}" > "$log_file"
rm "$log_file.tmp"
EOF

chmod +x .claude/logs/rotate-costs.sh
```

### Step 5: Dashboard Integration (Optional)

Create simple cost dashboard:

```bash
# Create dashboard script
cat > .ai-tools/cost-dashboard.sh << 'EOF'
#!/bin/bash
# Simple cost tracking dashboard

source .env

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Claude Code - Cost Dashboard"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Today's costs
echo "📊 Today's Usage:"
claude config cost-report --period today

echo ""
echo "📈 This Week:"
claude config cost-report --period week

echo ""
echo "📅 This Month:"
claude config cost-report --period month --projection

echo ""
echo "🎯 Budget Status:"
echo "  Daily:   $CLAUDE_DAILY_BUDGET USD"
echo "  Monthly: $CLAUDE_MONTHLY_BUDGET USD"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
EOF

chmod +x .ai-tools/cost-dashboard.sh
```

Run dashboard:

```bash
.ai-tools/cost-dashboard.sh
```

## ✅ Configuration Validation

### Validate Configuration Files

```bash
# Validate JSON syntax
jq empty .claude/config/model-profiles.json && echo "✓ model-profiles.json valid"
jq empty .claude/config/agent-model-mapping.json && echo "✓ agent-model-mapping.json valid"
jq empty .claude/config/cost-optimization.json && echo "✓ cost-optimization.json valid"

# Check all agents have profile mappings
agents_count=$(ls -1 .claude/agents/*/*.md 2>/dev/null | wc -l)
mappings_count=$(jq '.agentMappings | length' .claude/config/agent-model-mapping.json)

echo "Agents: $agents_count, Mappings: $mappings_count"
```

### Test Profile Selection

```bash
# Test profile retrieval for different agents
claude config get-profile --agent software-architect
# Expected: quality

claude config get-profile --agent frontend-engineer
# Expected: balanced

claude config get-profile --agent qa-engineer --task quick_check
# Expected: fast
```

## 🧪 Testing & Verification

### Test Suite

Create test script `.ai-tools/test-model-config.sh`:

```bash
#!/bin/bash
# Test Model Configuration System

echo "🧪 Testing Model Configuration System..."

# Test 1: Environment variables
echo "Test 1: Environment Variables"
if [ -z "$CLAUDE_DEFAULT_PROFILE" ]; then
    echo "❌ CLAUDE_DEFAULT_PROFILE not set"
    exit 1
else
    echo "✓ Environment configured"
fi

# Test 2: Configuration files exist
echo "Test 2: Configuration Files"
for file in model-profiles.json agent-model-mapping.json cost-optimization.json; do
    if [ ! -f ".claude/config/$file" ]; then
        echo "❌ Missing: $file"
        exit 1
    fi
done
echo "✓ All configuration files present"

# Test 3: JSON validity
echo "Test 3: JSON Validity"
for file in .claude/config/*.json; do
    if ! jq empty "$file" 2>/dev/null; then
        echo "❌ Invalid JSON: $file"
        exit 1
    fi
done
echo "✓ All JSON files valid"

# Test 4: Profile retrieval
echo "Test 4: Profile Retrieval"
profile=$(jq -r '.profiles.balanced.primaryModel' .claude/config/model-profiles.json)
if [ -z "$profile" ]; then
    echo "❌ Cannot retrieve profile"
    exit 1
fi
echo "✓ Profile retrieval working: $profile"

# Test 5: Agent mapping
echo "Test 5: Agent Mapping"
agent_profile=$(jq -r '.agentMappings["software-architect"].defaultProfile' .claude/config/agent-model-mapping.json)
if [ "$agent_profile" != "quality" ]; then
    echo "❌ Incorrect agent mapping"
    exit 1
fi
echo "✓ Agent mapping correct"

echo ""
echo "✅ All tests passed!"
```

Run tests:

```bash
chmod +x .ai-tools/test-model-config.sh
.ai-tools/test-model-config.sh
```

## 🔍 Troubleshooting

### Common Issues

**Issue 1: Environment variables not loaded**

```bash
# Solution: Source .env file
source .env

# Verify
echo $CLAUDE_DEFAULT_PROFILE
```

**Issue 2: JSON syntax errors**

```bash
# Find and fix JSON errors
for file in .claude/config/*.json; do
    echo "Checking $file"
    jq . "$file" > /dev/null || echo "Error in $file"
done
```

**Issue 3: Cost tracking not working**

```bash
# Check log file permissions
ls -la .claude/logs/cost-tracking.json

# Recreate if needed
mkdir -p .claude/logs
echo '{"sessions": []}' > .claude/logs/cost-tracking.json
chmod 664 .claude/logs/cost-tracking.json
```

**Issue 4: Budget alerts not showing**

```bash
# Verify alert configuration
jq '.alertConfiguration.enabled' .claude/config/cost-optimization.json

# Check alert channels
jq '.alertConfiguration.channels' .claude/config/cost-optimization.json
```

## 🚀 Advanced Integration

### Integration with CI/CD

**GitHub Actions Example:**

```yaml
# .github/workflows/cost-check.yml
name: Cost Optimization Check

on: [push, pull_request]

jobs:
  cost-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Check Model Configuration
        run: |
          source .env
          .ai-tools/test-model-config.sh

      - name: Validate Budget
        run: |
          usage=$(claude config cost-report --period month --format json | jq '.utilization')
          if (( $(echo "$usage > 0.9" | bc -l) )); then
            echo "::warning::Monthly budget at ${usage}%"
          fi
```

### Custom Profile Logic

Create custom profile selection logic:

```bash
# .ai-tools/custom-profile-selector.sh
#!/bin/bash

# Custom logic for profile selection
select_profile() {
    local task_type=$1
    local complexity=$2
    local budget_remaining=$3

    # Custom rules
    if [ "$budget_remaining" -lt "0.1" ]; then
        echo "fast"  # Low budget: use fast profile
    elif [ "$complexity" = "high" ] && [ "$task_type" = "architecture" ]; then
        echo "quality"  # Critical tasks: use quality
    else
        echo "balanced"  # Default: balanced
    fi
}

# Usage
profile=$(select_profile "feature" "medium" "0.65")
echo "Selected profile: $profile"
```

### Monitoring Integration

**Prometheus Metrics Export:**

```bash
# .ai-tools/export-prometheus-metrics.sh
#!/bin/bash

# Export cost metrics for Prometheus
cat > /var/lib/prometheus/claude_costs.prom << EOF
# HELP claude_daily_cost Daily Claude API costs in USD
# TYPE claude_daily_cost gauge
claude_daily_cost $(jq '.sessions[-1].cost' .claude/logs/cost-tracking.json)

# HELP claude_profile_usage Profile usage distribution
# TYPE claude_profile_usage gauge
claude_profile_usage{profile="fast"} $(jq '[.sessions[-7:][].profile] | map(select(. == "fast")) | length' .claude/logs/cost-tracking.json)
claude_profile_usage{profile="balanced"} $(jq '[.sessions[-7:][].profile] | map(select(. == "balanced")) | length' .claude/logs/cost-tracking.json)
claude_profile_usage{profile="quality"} $(jq '[.sessions[-7:][].profile] | map(select(. == "quality")) | length' .claude/logs/cost-tracking.json)
EOF
```

## 📚 Next Steps

After integration:

1. **Monitor Usage** - Track costs for first week
2. **Optimize Profiles** - Adjust agent mappings based on actual usage
3. **Set Alerts** - Configure budget alerts for your team
4. **Train Team** - Share best practices with developers
5. **Iterate** - Continuously improve configuration

## 🔗 Resources

- [Main Documentation](README.md)
- [Framework Configuration](../../CLAUDE.md)
- [Agent Documentation](../.claude/agents/)
- [Cost Optimization Guide](cost-optimization.json)

---

**Questions?** Check the main documentation or contact the framework team.
