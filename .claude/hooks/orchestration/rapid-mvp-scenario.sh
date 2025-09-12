#!/bin/bash

# Rapid MVP Development Orchestration Scenario
# Optimized workflow for quick MVP development with minimal overhead
# Focus: Speed, essential features, iterative development

SCENARIO_NAME="Rapid MVP Development"
PROJECT_TYPE="${1:-startup}"  # startup, prototype, proof-of-concept
MVP_SCOPE="${2:-minimal}"     # minimal, extended, feature-rich

echo "🚀 $SCENARIO_NAME - Starting orchestration..."
echo "Project Type: $PROJECT_TYPE | MVP Scope: $MVP_SCOPE"

# Ensure work directory exists
mkdir -p work/orchestration

# Log orchestration start
ORCHESTRATION_LOG="work/orchestration/rapid-mvp-$(date +%Y%m%d_%H%M%S).log"

cat > "$ORCHESTRATION_LOG" << EOF
# Rapid MVP Orchestration Log

**Started:** $(date)
**Scenario:** $SCENARIO_NAME
**Project Type:** $PROJECT_TYPE
**MVP Scope:** $MVP_SCOPE

## Workflow Execution

EOF

echo "$(date): Rapid MVP orchestration started - Type: $PROJECT_TYPE, Scope: $MVP_SCOPE" >> "$ORCHESTRATION_LOG"

# Phase 1: Business Discovery (Streamlined)
echo "📋 Phase 1: Streamlined Business Discovery"
echo "### Phase 1: Streamlined Business Discovery" >> "$ORCHESTRATION_LOG"

# Business Analyst - Essential requirements only
./.claude/hooks/task-start-logger.sh "business-analyst" "Essential requirements gathering for MVP"
echo "- Started business-analyst for essential requirements" >> "$ORCHESTRATION_LOG"

# Product Manager - MVP scope definition
./.claude/hooks/task-start-logger.sh "product-manager" "MVP scope and user stories definition"
echo "- Started product-manager for MVP scope definition" >> "$ORCHESTRATION_LOG"

# Quick validation checkpoint
./.claude/hooks/quality-gate-checker.sh "business-analyst" "requirements-completeness"
PHASE1_RESULT=$?

if [[ $PHASE1_RESULT -ne 0 ]]; then
    echo "⚠️ Phase 1 quality gate failed - manual review required"
    echo "$(date): Phase 1 quality gate failed - exit code: $PHASE1_RESULT" >> "$ORCHESTRATION_LOG"
    exit 1
fi

echo "✅ Phase 1 completed - Requirements validated"
echo "$(date): Phase 1 completed successfully" >> "$ORCHESTRATION_LOG"

# Phase 2: Architecture & Design (Parallel + Simplified)
echo "🏗️ Phase 2: Simplified Architecture & Design (Parallel)"
echo "### Phase 2: Simplified Architecture & Design" >> "$ORCHESTRATION_LOG"

# Parallel execution for speed
{
    # Software Architect - MVP architecture
    ./.claude/hooks/task-start-logger.sh "software-architect" "MVP architecture with scalability considerations"
    echo "- Started software-architect for MVP architecture" >> "$ORCHESTRATION_LOG"
} &

{
    # UX Designer - Essential user flows
    ./.claude/hooks/task-start-logger.sh "ux-designer" "Essential user flows and wireframes for MVP"
    echo "- Started ux-designer for essential UX flows" >> "$ORCHESTRATION_LOG"
} &

# Wait for parallel tasks to complete
wait

# Quick architecture validation
./.claude/hooks/quality-gate-checker.sh "software-architect" "architecture-feasibility"
PHASE2_RESULT=$?

if [[ $PHASE2_RESULT -ne 0 ]]; then
    echo "⚠️ Phase 2 quality gate failed - architecture review required"
    echo "$(date): Phase 2 quality gate failed - exit code: $PHASE2_RESULT" >> "$ORCHESTRATION_LOG"
    exit 1
fi

echo "✅ Phase 2 completed - Architecture validated"
echo "$(date): Phase 2 completed successfully" >> "$ORCHESTRATION_LOG"

# Phase 3: MVP Development (Parallel)
echo "💻 Phase 3: MVP Development (Parallel Execution)"
echo "### Phase 3: MVP Development" >> "$ORCHESTRATION_LOG"

{
    # Frontend Engineer - Essential UI components
    ./.claude/hooks/task-start-logger.sh "frontend-engineer" "Essential UI components and user interactions"
    echo "- Started frontend-engineer for essential UI" >> "$ORCHESTRATION_LOG"
} &

{
    # API Engineer - Core API endpoints
    ./.claude/hooks/task-start-logger.sh "api-engineer" "Core API endpoints for MVP functionality"
    echo "- Started api-engineer for core APIs" >> "$ORCHESTRATION_LOG"
} &

# Wait for development tasks
wait

# QA Engineer - Essential testing
./.claude/hooks/task-start-logger.sh "qa-engineer" "Essential testing and validation for MVP"
echo "- Started qa-engineer for essential testing" >> "$ORCHESTRATION_LOG"

# Development quality gate
./.claude/hooks/quality-gate-checker.sh "frontend-engineer" "mvp-functionality"
PHASE3_RESULT=$?

if [[ $PHASE3_RESULT -ne 0 ]]; then
    echo "⚠️ Phase 3 quality gate failed - development review required"
    echo "$(date): Phase 3 quality gate failed - exit code: $PHASE3_RESULT" >> "$ORCHESTRATION_LOG"
    exit 1
fi

echo "✅ Phase 3 completed - MVP development validated"
echo "$(date): Phase 3 completed successfully" >> "$ORCHESTRATION_LOG"

# Phase 4: Rapid Deployment
echo "🚀 Phase 4: Rapid Deployment"
echo "### Phase 4: Rapid Deployment" >> "$ORCHESTRATION_LOG"

# Deployment Engineer - MVP deployment
./.claude/hooks/task-start-logger.sh "deployment-engineer" "Rapid MVP deployment with monitoring"
echo "- Started deployment-engineer for rapid deployment" >> "$ORCHESTRATION_LOG"

# Final deployment validation
./.claude/hooks/quality-gate-checker.sh "deployment-engineer" "mvp-deployment"
PHASE4_RESULT=$?

if [[ $PHASE4_RESULT -ne 0 ]]; then
    echo "⚠️ Phase 4 quality gate failed - deployment review required"
    echo "$(date): Phase 4 quality gate failed - exit code: $PHASE4_RESULT" >> "$ORCHESTRATION_LOG"
    exit 1
fi

echo "✅ Phase 4 completed - MVP deployed successfully"
echo "$(date): Phase 4 completed - MVP deployed" >> "$ORCHESTRATION_LOG"

# Generate success summary
cat >> "$ORCHESTRATION_LOG" << EOF

## Orchestration Summary

✅ **Status:** COMPLETED SUCCESSFULLY
🎯 **Result:** MVP ready for user testing and feedback
⏱️ **Duration:** $(date)
🔄 **Next Steps:** Monitor user feedback and plan iteration

### MVP Deliverables Created
- ✅ Essential business requirements
- ✅ MVP-focused architecture
- ✅ Core user experience flows
- ✅ Essential UI components
- ✅ Core API functionality
- ✅ Basic testing coverage
- ✅ Production deployment

### Recommended Follow-up Actions
1. Monitor user adoption and feedback
2. Track core business metrics
3. Plan next iteration based on data
4. Scale infrastructure as needed
5. Enhance features based on user needs

EOF

echo "🎉 Rapid MVP orchestration completed successfully!"
echo "📄 Full log: $ORCHESTRATION_LOG"

# Generate orchestration report
ORCHESTRATION_REPORT="work/orchestration/rapid-mvp-report-$(date +%Y%m%d_%H%M%S).md"

cat > "$ORCHESTRATION_REPORT" << EOF
# Rapid MVP Development - Orchestration Report

**Generated:** $(date)
**Scenario:** $SCENARIO_NAME
**Duration:** MVP development completed in single orchestration run

## Workflow Summary

### Phase Execution Overview

| Phase | Agents Involved | Execution Mode | Status |
|-------|----------------|----------------|---------|
| 1. Business Discovery | business-analyst, product-manager | Sequential | ✅ Completed |
| 2. Architecture & Design | software-architect, ux-designer | Parallel | ✅ Completed |
| 3. MVP Development | frontend-engineer, api-engineer, qa-engineer | Mixed | ✅ Completed |
| 4. Rapid Deployment | deployment-engineer | Sequential | ✅ Completed |

### Key Success Factors

1. **Parallel Execution:** Architecture and UX design in parallel
2. **Streamlined Validation:** Essential quality gates only
3. **MVP Focus:** Core functionality prioritized
4. **Rapid Feedback:** Quick deployment for user testing

### Performance Metrics

- **Total Agents Used:** 7 out of 11 available
- **Quality Gates Passed:** 4/4
- **Parallel Efficiency:** 2 parallel execution phases
- **Time to Market:** Optimized for speed

## Business Value Delivered

### Immediate Benefits
- ✅ Rapid market validation capability
- ✅ User feedback collection readiness
- ✅ Core functionality demonstration
- ✅ Technical feasibility proof

### Long-term Advantages
- 🚀 Foundation for iterative development
- 📊 Real user data collection
- 💰 Reduced time-to-market risk
- 🔄 Agile development foundation

## Next Iteration Recommendations

### Enhancement Opportunities
1. **Security Hardening:** Integrate security-engineer for production
2. **Data Analytics:** Add data-engineer for user behavior tracking
3. **Performance Optimization:** Enhance frontend and API performance
4. **Feature Expansion:** Based on user feedback and usage patterns

### Scaling Preparation
- Monitor system performance under real load
- Plan infrastructure scaling based on adoption
- Prepare feature roadmap based on user feedback
- Establish continuous integration/deployment pipeline

EOF

echo "📊 Orchestration report: $ORCHESTRATION_REPORT"

# Log the orchestration completion
echo "$(date): Rapid MVP orchestration completed successfully - Report: $ORCHESTRATION_REPORT" >> work/orchestration-activity.log

echo "🚀 Rapid MVP Development orchestration completed successfully!"
exit 0