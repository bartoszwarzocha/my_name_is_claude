# Extended Thinking Mode Wrapper

## Purpose
Activate deep reasoning mode for complex agent decisions requiring comprehensive analysis, alternative evaluation, and confidence assessment. Generates structured thinking logs for transparency and continuous improvement.

## When to Use
- Complex architectural decisions (microservices vs monolithic, technology stack selection)
- Security threat modeling and vulnerability assessment
- Multi-agent conflict resolution requiring synthesis of competing recommendations
- Performance optimization with multiple viable approaches
- Quality gate failure root cause analysis
- Any decision meeting trigger conditions in `.claude/config/extended-thinking-config.json`

## Activation

This wrapper automatically activates when:
1. Agent detects trigger condition from extended-thinking-config.json
2. User explicitly requests deep analysis ("ultrathink", "deep analysis", "comprehensive reasoning")
3. Decision confidence falls below quality gate threshold (typically <0.70)
4. Multi-agent coordination detects conflicting recommendations

## Extended Thinking Process

**Phase 1: Problem Space Analysis**
Before jumping to solutions, deeply analyze:
- What is the fundamental problem or decision?
- What are the constraints (technical, business, timeline, budget)?
- What assumptions exist that need validation?
- What information is missing or uncertain?
- What are the success criteria?

**Phase 2: Alternative Generation**
Generate multiple viable approaches:
- Identify at least 3 alternative solutions
- Include both conventional and creative options
- Consider hybrid approaches combining strengths
- Document "no action" baseline for comparison

**Phase 3: Evaluation Framework**
For each alternative, analyze:
- **Technical Feasibility**: Implementation complexity, risk level, dependency requirements
- **Business Value**: Impact on goals, user value, competitive advantage
- **Resource Impact**: Development time, cost, maintenance burden
- **Risk Assessment**: Failure modes, mitigation strategies, reversibility
- **Long-term Implications**: Scalability, maintainability, technical debt

**Phase 4: Trade-off Analysis**
Deep comparison across alternatives:
- Create decision matrix with weighted criteria
- Identify Pareto-optimal solutions
- Analyze sensitivity to assumption changes
- Consider stakeholder preferences and organizational context

**Phase 5: Recommendation & Confidence**
Synthesize analysis into actionable recommendation:
- Primary recommendation with clear rationale
- Confidence score (0.0-1.0) with justification
- Key assumptions that could invalidate decision
- Monitoring metrics to validate decision post-implementation
- Alternative approach if confidence threshold not met

## Thinking Log Generation

**Automatic Capture:**
During Extended Thinking mode, the system captures:
- Each reasoning step with sequence numbering
- Alternatives considered with evaluation criteria
- Trade-off analysis and decision rationale
- Confidence scores and uncertainty factors
- Time spent in analysis (for performance optimization)

**Storage Format:**
```json
{
  "agent": "[agent-name]",
  "timestamp": "[ISO-8601]",
  "task_id": "[todowrite-task-id]",
  "trigger": "[trigger-condition-id]",
  "problem_statement": "[clear description]",
  "alternatives": [
    {
      "name": "[alternative-name]",
      "description": "[brief description]",
      "pros": ["[strength-1]", "[strength-2]"],
      "cons": ["[weakness-1]", "[weakness-2]"],
      "feasibility_score": 0.0-1.0,
      "value_score": 0.0-1.0,
      "risk_score": 0.0-1.0
    }
  ],
  "thinking_blocks": [
    {"sequence": 1, "phase": "problem_analysis", "content": "[reasoning]"},
    {"sequence": 2, "phase": "alternative_generation", "content": "[reasoning]"},
    {"sequence": 3, "phase": "evaluation", "content": "[reasoning]"}
  ],
  "decision": {
    "selected_alternative": "[name]",
    "rationale": "[why this choice]",
    "confidence": 0.0-1.0,
    "key_assumptions": ["[assumption-1]", "[assumption-2]"],
    "validation_metrics": ["[metric-1]", "[metric-2]"],
    "fallback_plan": "[if decision proves wrong]"
  },
  "execution_metadata": {
    "thinking_time_ms": 0,
    "model_used": "[haiku/sonnet/opus]",
    "framework_version": "3.9.0+"
  }
}
```

**Storage Location:**
- Path: `.claude/thinking-logs/{agent-category}/{agent-name}/`
- Filename: `{timestamp}-{decision-type-slug}.json`
- Example: `.claude/thinking-logs/core/software-architect/2025-10-17-143022-microservices-decision.json`

## Integration with Framework Components

**TodoWrite Integration:**
```markdown
Task: [task-description]
Status: in_progress
Extended Thinking: Yes
Thinking Log: .claude/thinking-logs/[path-to-log].json
Confidence: 0.87
Alternatives Considered: 4
Decision: [selected-alternative]
```

**Checkpoint Integration:**
Before creating checkpoint for major decision:
- Generate thinking log
- Include log reference in checkpoint metadata
- Enable semantic rollback: "revert to before architecture decision"

**Parallel Agent Coordination:**
When multiple agents analyze same problem:
- Each generates independent thinking log
- session-manager synthesizes logs for conflict resolution
- Combined analysis creates meta-thinking log

**Quality Gates:**
Extended Thinking automatically activates when:
- Confidence score below threshold (config: min_confidence_for_implementation)
- Quality gate failure requires root cause analysis
- Performance/security metrics breach thresholds

## Agent Instructions

**When Extended Thinking Mode Activates:**

1. **Acknowledge Mode**: Briefly state "Using Extended Thinking for [decision-type]"

2. **Follow 5-Phase Process**: Complete all phases systematically, don't skip to recommendation

3. **Think Out Loud**: Express reasoning explicitly, including:
   - Hypotheses and how you test them
   - Why you reject certain options
   - What uncertainties remain
   - What information would increase confidence

4. **Generate Thinking Log**: Create structured JSON log following schema above

5. **Save Thinking Log**: Write log to appropriate directory based on agent category

6. **Update TodoWrite**: Add thinking log reference to current task

7. **Provide Summary**: Give user concise summary of analysis + recommendation

8. **Confidence Check**: If confidence < threshold, recommend gathering more information or escalation

## Quality Standards

**Thinking Log Quality:**
- Minimum 3 alternatives considered
- Clear rationale for each phase
- Confidence score justified by analysis depth
- Assumptions explicitly stated
- Validation metrics actionable

**Analysis Completeness:**
- Problem space fully explored
- Constraints identified and validated
- Trade-offs explicitly compared
- Risk assessment comprehensive
- Long-term implications considered

**Performance:**
- Extended Thinking completes within timeout (config: max_thinking_time_seconds)
- Log file size reasonable (<1MB typical, <10MB maximum)
- No duplicate analysis (check cache if enabled)

## Example Usage Scenarios

**Scenario 1: Architecture Decision**
```
Trigger: software-architect selecting system architecture for 10M user platform
Decision: Microservices vs Monolithic vs Modular Monolith
Thinking Focus:
- Team size and expertise (15 developers, varied experience)
- Deployment complexity tolerance (CI/CD maturity: medium)
- Performance requirements (99.9% uptime, <200ms p95)
- Budget constraints ($50K/month infrastructure)
Result: Modular Monolith (confidence: 0.88) - balances team capability with scalability needs
```

**Scenario 2: Security Threat Analysis**
```
Trigger: security-engineer analyzing OAuth implementation vulnerability
Decision: Risk severity and mitigation priority
Thinking Focus:
- Attack vector feasibility (requires user interaction: medium)
- Impact scope (user data exposure: high)
- Exploitation complexity (requires technical skill: medium)
- Mitigation options (5 alternatives ranging from quick patch to redesign)
Result: High severity, immediate patching + long-term redesign (confidence: 0.92)
```

**Scenario 3: Performance Optimization**
```
Trigger: performance-engineer addressing 450ms API response time
Decision: Optimization strategy selection
Thinking Focus:
- Bottleneck identification (database N+1 queries: 60% of time)
- Alternative approaches (caching, query optimization, async processing, database upgrade)
- Cost-benefit analysis (development time vs performance gain)
- Risk assessment (breaking changes, cache invalidation complexity)
Result: Query optimization + selective caching (confidence: 0.85)
```

## Configuration Reference

**Primary Config:** `.claude/config/extended-thinking-config.json`
- Trigger conditions (critical/high-value/experimental)
- Confidence thresholds per decision type
- Performance limits (timeout, concurrency)
- Integration settings (TodoWrite, checkpoints, parallel agents)

**Diagnostic Integration:** `.claude/config/diagnostic-framework-integration.json`
- Quality gate failure analysis
- Root cause investigation methodology
- Incident response integration
- Performance diagnostic triggers

## Validation Checklist

Before considering Extended Thinking complete:
- [ ] All 5 phases completed systematically
- [ ] Minimum 3 alternatives generated and evaluated
- [ ] Trade-off analysis documented with criteria
- [ ] Confidence score calculated with justification
- [ ] Thinking log generated in valid JSON format
- [ ] Log saved to correct directory
- [ ] TodoWrite task updated with log reference
- [ ] User summary provided with recommendation
- [ ] Quality gates checked (confidence threshold, alternatives count)

## Troubleshooting

**Issue: Thinking log not generated**
- Check agent has write permissions to `.claude/thinking-logs/`
- Verify JSON schema validation (no syntax errors)
- Check storage quota (logs compressed after 7 days per config)

**Issue: Confidence score too low (<0.70)**
- Identify missing information causing uncertainty
- Recommend gathering additional data
- Consider prototype/spike to reduce uncertainty
- Document assumptions that need validation
- Escalate decision if information unavailable

**Issue: Extended Thinking timeout**
- Check timeout setting (config: max_thinking_time_seconds)
- Consider reducing scope (break decision into smaller parts)
- Use standard analysis mode with explicit assumption documentation
- Increase timeout for exceptionally complex decisions

---

**Framework Version:** 3.9.0+
**Template Version:** 1.0
**Last Updated:** 2025-10-17
**Integration:** TodoWrite, Checkpoints, Parallel Agents, Quality Gates
