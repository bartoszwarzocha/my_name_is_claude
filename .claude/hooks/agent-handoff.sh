#!/bin/bash

# Agent Handoff Hook
# Automates work handoff between agents in different phases
# Ensures proper workflow transitions: business-analyst → software-architect → frontend-engineer

FROM_AGENT="${1:-unknown}"
TO_AGENT="${2:-unknown}"
HANDOFF_DATA="${3:-No handoff data provided}"

echo "🔄 Agent Handoff Hook - Processing transition from $FROM_AGENT to $TO_AGENT..."

# Ensure work directory exists
mkdir -p work/handoffs

# Define phase-based agent relationships
declare -A AGENT_PHASES
AGENT_PHASES["business-analyst"]="Phase1-Discovery"
AGENT_PHASES["product-manager"]="Phase1-Discovery"
AGENT_PHASES["reviewer"]="Phase1-Discovery"
AGENT_PHASES["software-architect"]="Phase2-Architecture"
AGENT_PHASES["ux-designer"]="Phase2-Architecture"
AGENT_PHASES["security-engineer"]="Phase2-Architecture"
AGENT_PHASES["frontend-engineer"]="Phase3-Development"
AGENT_PHASES["api-engineer"]="Phase3-Development"
AGENT_PHASES["data-engineer"]="Phase3-Development"
AGENT_PHASES["qa-engineer"]="Phase3-Development"
AGENT_PHASES["deployment-engineer"]="Phase4-Deployment"

FROM_PHASE="${AGENT_PHASES[$FROM_AGENT]:-Unknown}"
TO_PHASE="${AGENT_PHASES[$TO_AGENT]:-Unknown}"

echo "📋 Handoff Details:"
echo "  From: $FROM_AGENT ($FROM_PHASE)"
echo "  To: $TO_AGENT ($TO_PHASE)"

# Validate handoff sequence
EXIT_CODE=0

# Check for valid phase transitions
case "$FROM_PHASE-$TO_PHASE" in
    "Phase1-Discovery-Phase2-Architecture"|"Phase2-Architecture-Phase3-Development"|"Phase3-Development-Phase4-Deployment")
        echo "✅ Valid phase transition detected"
        ;;
    "Phase1-Discovery-Phase1-Discovery"|"Phase2-Architecture-Phase2-Architecture"|"Phase3-Development-Phase3-Development")
        echo "🔄 Same-phase handoff (collaboration within phase)"
        ;;
    *)
        echo "⚠️ Unusual phase transition - please verify workflow"
        ;;
esac

# Create handoff record
HANDOFF_ID="$(date +%Y%m%d_%H%M%S)_${FROM_AGENT}_to_${TO_AGENT}"
HANDOFF_FILE="work/handoffs/${HANDOFF_ID}.md"

cat > "$HANDOFF_FILE" << EOF
# Agent Handoff Record

**Handoff ID:** $HANDOFF_ID
**Date:** $(date)
**From Agent:** $FROM_AGENT ($FROM_PHASE)
**To Agent:** $TO_AGENT ($TO_PHASE)

## Handoff Data

$HANDOFF_DATA

## Required Actions for Receiving Agent

$(case "$TO_AGENT" in
    "software-architect")
        echo "- Review business requirements and user stories"
        echo "- Create system architecture documentation"
        echo "- Define technology stack and patterns"
        echo "- Prepare technical specifications for development team"
        ;;
    "frontend-engineer")
        echo "- Review system architecture and design specifications"
        echo "- Analyze security requirements from security-engineer"
        echo "- Implement UI/UX designs following accessibility standards"
        echo "- Coordinate with api-engineer for integration requirements"
        ;;
    "security-engineer")
        echo "- Review business requirements for security implications"
        echo "- Conduct threat modeling based on system architecture"
        echo "- Define security controls and compliance requirements"
        echo "- Provide security guidelines for development team"
        ;;
    "api-engineer")
        echo "- Review system architecture and data models"
        echo "- Design API contracts and service boundaries"
        echo "- Coordinate with frontend-engineer for integration needs"
        echo "- Implement security requirements from security-engineer"
        ;;
    "deployment-engineer")
        echo "- Review application architecture and infrastructure needs"
        echo "- Setup CI/CD pipelines with quality gates"
        echo "- Configure monitoring and alerting systems"
        echo "- Implement security controls in deployment pipeline"
        ;;
    *)
        echo "- Review previous phase deliverables"
        echo "- Validate requirements alignment"
        echo "- Proceed with agent-specific tasks"
        ;;
esac)

## Collaboration Points

$(case "$FROM_AGENT-$TO_AGENT" in
    "business-analyst-software-architect")
        echo "- Validate technical feasibility of business requirements"
        echo "- Ensure architecture aligns with business goals"
        echo "- Review scalability and performance requirements"
        ;;
    "software-architect-frontend-engineer")
        echo "- Clarify technical specifications and patterns"
        echo "- Review API contracts and data flow"
        echo "- Validate technology stack decisions"
        ;;
    "security-engineer-frontend-engineer")
        echo "- Implement security controls in UI components"
        echo "- Follow secure coding practices"
        echo "- Validate authentication and authorization flow"
        ;;
    "frontend-engineer-qa-engineer")
        echo "- Review testing requirements and strategies"
        echo "- Validate accessibility compliance"
        echo "- Setup automated testing pipeline"
        ;;
    *)
        echo "- Maintain regular communication"
        echo "- Validate deliverable quality"
        echo "- Escalate blocking issues promptly"
        ;;
esac)

## Status

- [ ] Handoff initiated
- [ ] Receiving agent acknowledged
- [ ] Deliverables reviewed
- [ ] Work continued

## Notes

_Add any additional notes or context here_

EOF

# Log handoff activity
echo "$(date): Handoff from $FROM_AGENT to $TO_AGENT initiated" >> work/handoff-timeline.log

# Check for potential coordination needs
case "$TO_AGENT" in
    "frontend-engineer")
        echo "🎨 Frontend development starting - checking coordination needs..."
        if [[ -f "work/handoffs"/*security-engineer* ]]; then
            echo "🔐 Security requirements available - ensure compliance"
        fi
        if [[ -f "work/handoffs"/*api-engineer* ]]; then
            echo "🔌 API specifications available - review for integration"
        fi
        ;;
    "deployment-engineer")
        echo "🚀 Deployment phase starting - validating readiness..."
        if [[ ! -f "work/handoffs"/*frontend-engineer* ]] && [[ ! -f "work/handoffs"/*api-engineer* ]]; then
            echo "⚠️ Development artifacts may not be ready for deployment"
            EXIT_CODE=1
        fi
        ;;
esac

echo "📄 Handoff record created: $HANDOFF_FILE"
echo "✅ Agent Handoff Hook completed"

exit $EXIT_CODE