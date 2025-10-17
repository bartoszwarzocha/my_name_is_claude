# Extended Thinking Mode - Deep Reasoning for Complex Decisions

## Overview

Extended Thinking Mode is a framework capability that activates deep reasoning for complex agent decisions. When enabled, agents perform comprehensive analysis including alternative evaluation, trade-off analysis, and confidence assessment - with full transparency through structured thinking logs.

**Benefits:**
- **Better Decisions**: Systematic analysis reduces cognitive biases and oversight
- **Transparency**: Full reasoning trail available for review and continuous improvement
- **Risk Mitigation**: Confidence scores and assumptions explicitly documented
- **Learning**: Historical thinking logs enable pattern recognition and improvement

**Framework Version:** 3.9.0+

---

## When to Use Extended Thinking

### Automatic Activation

Extended Thinking automatically activates for:

1. **Critical Decisions** (Always)
   - Architecture pattern selection (monolithic vs microservices vs modular monolith)
   - Security threat modeling and vulnerability assessment
   - Technology stack selection (framework, language, database choices)
   - Cost-performance trade-offs with significant budget impact (>$100/month)

2. **High-Value Scenarios** (Selective)
   - Multi-agent conflict resolution (conflicting recommendations)
   - Performance optimization with multiple viable approaches
   - Quality gate failure root cause analysis
   - Complex debugging requiring hypothesis testing

3. **Experimental Triggers** (Optional, disabled by default)
   - Large code reviews (>500 lines affecting core systems)
   - Custom triggers defined in project configuration

### Manual Activation

Request Extended Thinking explicitly by including in your request:
- **"ultrathink"** - Request deep analysis (Polish: "użyj trybu ultrathink")
- **"deep analysis"** - Explicit request for comprehensive reasoning
- **"analyze alternatives"** - Request alternative evaluation

**Example:**
```
User: "Select optimal database for our e-commerce platform serving 5M users. ultrathink"
Agent: *Activates Extended Thinking Mode*
       *Analyzes 4 alternatives: PostgreSQL, MongoDB, DynamoDB, hybrid approach*
       *Generates detailed thinking log with trade-off analysis*
       *Provides recommendation with 0.88 confidence*
```

---

## How Extended Thinking Works

### 5-Phase Process

Extended Thinking follows a systematic 5-phase process:

**Phase 1: Problem Space Analysis**
- Understand the fundamental problem or decision
- Identify constraints (technical, business, timeline, budget)
- Validate assumptions
- Identify missing information
- Define success criteria

**Phase 2: Alternative Generation**
- Generate minimum 3 viable approaches
- Include conventional and creative options
- Consider hybrid approaches
- Document "no action" baseline for comparison

**Phase 3: Evaluation Framework**
For each alternative, analyze:
- Technical feasibility (complexity, risk, dependencies)
- Business value (goal impact, user value, competitive advantage)
- Resource impact (development time, cost, maintenance)
- Risk assessment (failure modes, mitigation, reversibility)
- Long-term implications (scalability, maintainability, technical debt)

**Phase 4: Trade-off Analysis**
- Create decision matrix with weighted criteria
- Identify Pareto-optimal solutions
- Analyze sensitivity to assumption changes
- Consider stakeholder preferences and context

**Phase 5: Recommendation & Confidence**
- Primary recommendation with clear rationale
- Confidence score (0.0-1.0) with justification
- Key assumptions that could invalidate decision
- Validation metrics for post-implementation
- Fallback plan if confidence threshold not met

### Thinking Log Generation

All reasoning is captured in structured JSON format:

```json
{
  "agent": "software-architect",
  "timestamp": "2025-10-17T16:00:00Z",
  "task_id": "epic-1-feature-3-task-12",
  "trigger": "architecture_pattern_selection",
  "problem_statement": "Select optimal architecture...",
  "alternatives": [
    {
      "name": "microservices",
      "description": "Decompose system into independent services",
      "pros": ["Independent scaling", "Team autonomy"],
      "cons": ["Operational complexity", "Distributed transactions"],
      "feasibility_score": 0.65,
      "value_score": 0.85,
      "risk_score": 0.72
    }
    // ... more alternatives
  ],
  "thinking_blocks": [
    {
      "sequence": 1,
      "phase": "problem_analysis",
      "content": "Analyzing constraints: 5M users requires..."
    }
    // ... more thinking blocks
  ],
  "decision": {
    "selected_alternative": "modular_monolith",
    "rationale": "Optimally balances team capabilities...",
    "confidence": 0.88,
    "key_assumptions": ["Team can maintain discipline..."],
    "validation_metrics": ["Deployment frequency >2x/week"],
    "fallback_plan": "If boundaries prove difficult..."
  },
  "execution_metadata": {
    "thinking_time_ms": 8500,
    "model_used": "claude-sonnet-4-5",
    "framework_version": "3.9.0+"
  }
}
```

**Storage Location:** `.claude/thinking-logs/{agent-category}/{agent-name}/{timestamp}-{decision-type}.json`

---

## Configuration

### Primary Configuration Files

**`.claude/config/extended-thinking-config.json`**
- Trigger conditions (critical/high-value/experimental)
- Confidence thresholds per decision type
- Performance limits (timeout, concurrency)
- Integration settings (TodoWrite, checkpoints, parallel agents)

**`.claude/config/diagnostic-framework-integration.json`**
- Quality gate failure analysis configuration
- Root cause investigation methodology
- Incident response integration
- Performance diagnostic triggers

### Customizing Triggers

Edit `.claude/config/extended-thinking-config.json` to customize:

```json
{
  "trigger_conditions": {
    "critical": {
      "enabled": true,
      "scenarios": [
        {
          "id": "architecture_pattern_selection",
          "agents": ["software-architect"],
          "trigger": "When selecting system architecture pattern",
          "min_confidence_threshold": 0.85
        }
      ]
    }
  }
}
```

**Adding Custom Trigger:**
1. Choose tier: `critical`, `high_value`, or `experimental`
2. Define trigger condition with unique ID
3. Specify applicable agents (or `"*"` for all)
4. Set minimum confidence threshold (0.0-1.0)
5. Document rationale for the trigger

---

## Real-World Examples

### Example 1: Architecture Decision

**Scenario:** Selecting system architecture for 5M user e-commerce platform

**Extended Thinking Analysis:**
- **Alternatives Evaluated:** 4 (microservices, monolithic, modular monolith, hybrid)
- **Thinking Blocks:** 12 (problem analysis → alternative generation → evaluation → trade-offs → recommendation)
- **Decision:** Modular monolith
- **Confidence:** 0.88
- **Rationale:** Balances team capabilities (medium DevOps maturity) with scalability needs while maintaining operational simplicity
- **Key Assumption:** 5M users achievable with monolithic deployment through optimization
- **Validation Metric:** Deployment frequency >2x/week, P95 <200ms
- **Fallback:** If module boundaries violate >20%, pivot to microservices

**Full Log:** `.claude/thinking-logs/core/software-architect/2025-10-17-160000-architecture-pattern-selection.json`

### Example 2: Security Vulnerability Assessment

**Scenario:** OAuth 2.0 vulnerability (missing PKCE) affecting 500K mobile users

**Extended Thinking Analysis:**
- **Alternatives Evaluated:** 4 (immediate hotfix, full redesign, phased mitigation, accept risk)
- **Thinking Blocks:** 14 (including CVSS scoring, compliance analysis, cost-benefit)
- **Decision:** Phased mitigation (interim controls + proper fix)
- **Confidence:** 0.92
- **Rationale:** Reduces risk immediately (rate limiting in 24h) while allowing proper PKCE implementation (2 weeks)
- **Key Assumption:** Rate limiting will deter opportunistic attackers
- **Validation Metric:** Zero exploits detected, <1% legitimate users affected by rate limiting
- **Fallback:** If active exploitation detected, escalate to emergency hotfix

**Full Log:** `.claude/thinking-logs/core/security-engineer/2025-10-17-161500-oauth-vulnerability-assessment.json`

### Example 3: Quality Gate Failure Analysis

**Scenario:** 15% flaky test failure rate blocking deployment pipeline

**Extended Thinking Analysis:**
- **Alternatives Evaluated:** 4 (increase timeouts, fix race conditions, improve test isolation, retry mechanism)
- **Thinking Blocks:** 15 (including cost analysis, ROI calculation)
- **Decision:** Hybrid approach (retry + race condition fix)
- **Confidence:** 0.87
- **Rationale:** Unblocks pipeline immediately (retry in 2h) while fixing root cause (race conditions in 3 days)
- **Key Assumption:** Race conditions fixable within 3-day window
- **Validation Metric:** Failure rate <1% after fix, retry rate <1%
- **Fallback:** If race conditions more complex, prioritize critical tests, defer others

**Full Log:** `.claude/thinking-logs/core/qa-engineer/2025-10-17-163000-integration-test-failure-analysis.json`

---

## Interpreting Thinking Logs

### Understanding Confidence Scores

Confidence scores indicate decision certainty:

- **0.90-1.00** (Very High): Strong evidence, clear winner, minimal uncertainty
- **0.80-0.89** (High): Good evidence, some trade-offs, minor uncertainties
- **0.70-0.79** (Medium): Reasonable evidence, significant trade-offs, moderate uncertainty
- **0.60-0.69** (Low): Weak evidence, unclear trade-offs, high uncertainty
- **<0.60** (Very Low): Insufficient information, major uncertainties, recommend gathering more data

**Quality Gate:** Framework default minimum confidence for implementation is 0.70. Below this, agent should recommend information gathering or escalation.

### Analyzing Trade-offs

Each alternative includes three scores:

1. **Feasibility Score** (0.0-1.0)
   - 0.9-1.0: Easy to implement, low risk, clear path
   - 0.7-0.89: Achievable with moderate effort, some risks
   - 0.5-0.69: Challenging, significant risks or unknowns
   - <0.5: Very difficult or impractical with current constraints

2. **Value Score** (0.0-1.0)
   - 0.9-1.0: High business value, significant impact
   - 0.7-0.89: Good value, meaningful impact
   - 0.5-0.69: Moderate value, some benefit
   - <0.5: Low value, questionable benefit

3. **Risk Score** (0.0-1.0)
   - 0.9-1.0: Very high risk, major failure potential
   - 0.7-0.89: High risk, significant concerns
   - 0.5-0.69: Moderate risk, manageable concerns
   - <0.5: Low risk, minor concerns only

**Optimal Decision:** High feasibility + High value + Low risk
**Common Trade-off:** High value + Medium feasibility + Medium risk (requires mitigation)

### Validation Metrics

Each decision includes validation metrics for post-implementation monitoring:

**Good Metrics Characteristics:**
- **Measurable**: Quantitative with clear threshold
- **Timely**: Observable within reasonable timeframe
- **Actionable**: Clear response if threshold violated
- **Relevant**: Directly validates key assumptions

**Example:**
```json
"validation_metrics": [
  "Deployment frequency >2x/week",  // Measurable, timely, relevant
  "P95 response time <200ms",       // Quantitative threshold
  "Error rate <0.1%"                // Actionable if violated
]
```

---

## Integration with Framework

### TodoWrite Integration

Thinking logs automatically integrate with TodoWrite tasks:

```markdown
Task: Select database architecture
Status: completed
Extended Thinking: Yes
Thinking Log: .claude/thinking-logs/core/software-architect/2025-10-17-160000-architecture-decision.json
Confidence: 0.88
Decision: PostgreSQL with read replicas
```

### Checkpoint Integration

Before creating checkpoint for major decision:
- Thinking log generated automatically
- Log reference included in checkpoint metadata
- Enables semantic rollback: "revert to before architecture decision"

**Checkpoint Metadata:**
```json
{
  "checkpoint_id": "checkpoint-47",
  "timestamp": "2025-10-17T16:05:00Z",
  "thinking_log": ".claude/thinking-logs/core/software-architect/2025-10-17-160000-architecture-decision.json",
  "decision": "modular_monolith",
  "confidence": 0.88
}
```

### Parallel Agent Coordination

When multiple agents analyze same problem:
1. Each generates independent thinking log
2. session-manager synthesizes logs for conflict resolution
3. Combined analysis creates meta-thinking log
4. Final decision reflects multi-perspective analysis

**Example:** frontend-engineer and backend-engineer disagree on API design
- Both generate thinking logs with their analysis
- session-manager evaluates both perspectives
- Meta-thinking log documents synthesis
- Coordinated decision maximizes both frontend UX and backend efficiency

---

## Best Practices

### When to Request Extended Thinking

**DO Request Extended Thinking When:**
- Making irreversible or high-impact decisions
- Multiple viable alternatives exist with unclear winner
- Stakeholder alignment needed on decision rationale
- Decision involves significant risk or uncertainty
- Learning from decision process valuable for future

**DON'T Request Extended Thinking When:**
- Decision is trivial or obvious
- Only one viable option exists
- Time pressure requires immediate action (use standard decision + document assumptions)
- Cost of analysis exceeds value of improved decision

### Reviewing Thinking Logs

**Regular Review:**
- Review thinking logs for major decisions monthly
- Validate actual outcomes against predicted confidence scores
- Calibrate trigger thresholds based on decision quality
- Share exemplary thinking logs with team for learning

**Decision Retrospectives:**
After major decisions, conduct retrospective:
1. Review thinking log assumptions
2. Compare predicted vs actual outcomes
3. Identify what was overlooked in analysis
4. Update trigger conditions if needed
5. Document lessons learned

### Improving Decision Quality

**Feedback Loop:**
1. Track decision outcomes against confidence scores
2. If low-confidence decisions succeed more than expected → triggers too conservative
3. If high-confidence decisions fail → missing risk factors in analysis
4. Adjust trigger thresholds and evaluation criteria accordingly

**Confidence Calibration:**
Target: 90% of 0.90-confidence decisions should succeed
- If success rate <80%: Overconfident, increase scrutiny
- If success rate >95%: Underconfident, reduce analysis overhead

---

## Troubleshooting

### Issue: Extended Thinking Not Activating

**Diagnosis:**
1. Check if trigger condition matches in `.claude/config/extended-thinking-config.json`
2. Verify agent is listed for the trigger scenario
3. Confirm trigger tier is enabled (`"enabled": true`)

**Solution:**
- Add custom trigger for your scenario
- Use manual activation: "ultrathink" or "deep analysis"
- Lower confidence threshold if triggering too rarely

### Issue: Thinking Logs Not Generated

**Diagnosis:**
1. Check write permissions on `.claude/thinking-logs/` directory
2. Verify thinking log directory structure exists
3. Check for JSON syntax errors in generated logs

**Solution:**
```bash
# Recreate directory structure
mkdir -p .claude/thinking-logs/{core,enterprise,custom}
chmod -R u+w .claude/thinking-logs/

# Validate existing logs
python3 work/validate-thinking-logs.py
```

### Issue: Low Confidence Scores (<0.70)

**Diagnosis:**
- Missing information causing uncertainty
- High complexity with many unknowns
- Conflicting evidence or trade-offs
- Insufficient historical data

**Solution:**
1. Identify specific uncertainties from thinking log
2. Gather missing information (user research, technical spikes, prototypes)
3. Consider phased approach (interim solution while gathering data)
4. Escalate decision if information unavailable
5. Document assumptions explicitly and monitor closely

### Issue: Extended Thinking Timeout

**Diagnosis:**
- Analysis too complex for timeout limit (default: 30s)
- Multiple sequential analyses needed
- Large search space for alternatives

**Solution:**
1. Break decision into smaller sub-decisions
2. Increase timeout in config (use judiciously)
3. Use standard analysis with explicit assumptions
4. Consider human consultation for exceptionally complex decisions

---

## Advanced Usage

### Custom Thinking Log Analysis

Extract insights from historical thinking logs:

```python
import json
from pathlib import Path

# Load all thinking logs
logs_dir = Path('.claude/thinking-logs')
logs = [json.load(open(f)) for f in logs_dir.rglob('*.json')]

# Analyze confidence calibration
decisions_by_confidence = {}
for log in logs:
    confidence = log['decision']['confidence']
    bucket = round(confidence, 1)
    if bucket not in decisions_by_confidence:
        decisions_by_confidence[bucket] = []
    decisions_by_confidence[bucket].append(log)

# Compare predicted vs actual outcomes
# (Requires tracking actual outcomes - implement in your workflow)
```

### Integration with External Tools

**Export to Decision Log System:**
```bash
# Export thinking logs to external decision tracking system
for log in .claude/thinking-logs/**/*.json; do
  curl -X POST https://decision-tracker.company.com/api/decisions \
    -H "Content-Type: application/json" \
    -d @"$log"
done
```

**Dashboards and Visualization:**
- Track decision velocity (decisions per week)
- Monitor confidence score distribution
- Analyze most common trigger types
- Identify agents with highest decision quality

---

## FAQ

**Q: Does Extended Thinking slow down agent responses?**

A: Extended Thinking adds 5-15 seconds to decision-making. For critical decisions (architecture, security), this investment yields 10-100x ROI through better outcomes. For routine tasks, Extended Thinking doesn't activate.

**Q: Can I disable Extended Thinking entirely?**

A: Yes. Set `"enabled": false` for all trigger tiers in `.claude/config/extended-thinking-config.json`. However, this removes valuable transparency and quality assurance.

**Q: How much storage do thinking logs consume?**

A: Typical thinking log is 10-50KB. Assuming 10 critical decisions per week, annual storage ~25MB. Logs auto-compress after 7 days and auto-delete after 90 days (configurable).

**Q: Can thinking logs expose sensitive information?**

A: Thinking logs may contain business logic, architectural details, security considerations. They're gitignored by default. Review `.gitignore` and implement access controls appropriate for your security requirements.

**Q: How do I share thinking logs with stakeholders?**

A: Thinking logs are technical artifacts. For stakeholder communication, use agent-generated summaries that translate technical analysis into business terms. Consider using the Executive output style for stakeholder-facing summaries.

---

## See Also

- Model Configuration - Smart model selection for Extended Thinking (`.claude/config/model-profiles.json`)
- Output Styles - Context-aware communication (`.claude/config/output-styles.json`)
- Checkpoint System - State management with thinking logs (`.claude/config/checkpoint-system.json`)
- [Agent Template](../../.claude/templates/agent_template.md) - Agent structure and integration points
- [Extended Thinking Wrapper](../../.claude/prompts/tools/extended-thinking-wrapper.md) - Technical implementation details

---

**Framework Version:** 3.9.0+
**Last Updated:** 2025-10-17
**Status:** Production Ready
