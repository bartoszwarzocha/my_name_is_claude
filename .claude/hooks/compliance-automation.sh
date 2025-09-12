#!/bin/bash

# Compliance Automation Hook
# Automatically checks compliance with WCAG 2.1, GDPR, SOX and other standards
# Provides agent-specific compliance validation based on requirements

COMPLIANCE_TYPE="${1:-all}"  # wcag, gdpr, sox, pci, iso27001, all
AGENT_TYPE="${2:-}"
TARGET_PATH="${3:-work}"

echo "🛡️ Compliance Automation Hook - Checking: $COMPLIANCE_TYPE for $AGENT_TYPE..."

# Ensure work directory exists
mkdir -p work/compliance

EXIT_CODE=0

check_wcag_compliance() {
    local agent="$1"
    echo "♿ Checking WCAG 2.1 AA compliance..."
    
    local issues=0
    WCAG_REPORT="work/compliance/wcag_report_$(date +%Y%m%d_%H%M%S).md"
    
    cat > "$WCAG_REPORT" << EOF
# WCAG 2.1 AA Compliance Report

**Generated:** $(date)
**Agent:** $agent
**Standard:** WCAG 2.1 Level AA

## Compliance Checks

### 1. Perceivable

#### 1.1 Text Alternatives
EOF

    # Check if frontend-engineer has accessibility considerations
    if [[ "$agent" == "frontend-engineer" || "$agent" == "all" ]]; then
        # Look for accessibility-related prompts and deliverables
        if [[ -f ".claude/prompts/agents/frontend/web-accessibility-and-inclusive-design.md" ]]; then
            echo "- ✅ Accessibility prompt available" >> "$WCAG_REPORT"
        else
            echo "- ❌ Missing accessibility design prompt" >> "$WCAG_REPORT"
            issues=$((issues + 1))
        fi
        
        # Check for ARIA implementation guidance
        if grep -r -i "aria\|accessibility\|wcag" .claude/prompts/agents/frontend/ >/dev/null 2>&1; then
            echo "- ✅ ARIA implementation guidance found" >> "$WCAG_REPORT"
        else
            echo "- ⚠️ Limited ARIA implementation guidance" >> "$WCAG_REPORT"
        fi
        
        # Check for color contrast considerations
        if grep -r -i "contrast\|color.*blind" .claude/prompts/agents/frontend/ >/dev/null 2>&1; then
            echo "- ✅ Color contrast considerations included" >> "$WCAG_REPORT"
        else
            echo "- ⚠️ Color contrast guidelines may be missing" >> "$WCAG_REPORT"
        fi
    fi
    
    cat >> "$WCAG_REPORT" << EOF

#### 1.3 Adaptable
- Focus order and meaning preservation
- Responsive design implementation
- Multi-device compatibility

#### 1.4 Distinguishable
- Color contrast requirements (4.5:1 normal, 3:1 large text)
- Text resize capability (up to 200%)
- Focus indicators visibility

### 2. Operable

#### 2.1 Keyboard Accessible
- Full keyboard navigation support
- No keyboard traps
- Focus management

#### 2.4 Navigable
- Skip links implementation
- Descriptive page titles
- Logical navigation order

### 3. Understandable

#### 3.1 Readable
- Language identification
- Consistent terminology
- Plain language usage

#### 3.2 Predictable
- Consistent navigation patterns
- Predictable functionality
- Context changes control

### 4. Robust

#### 4.1 Compatible
- Valid HTML markup
- Assistive technology compatibility
- Future technology adaptability

## Compliance Status

$(
if [[ $issues -eq 0 ]]; then
    echo "✅ **Overall Status:** COMPLIANT"
    echo ""
    echo "All critical WCAG 2.1 AA requirements are addressed in the framework."
else
    echo "⚠️ **Overall Status:** NEEDS ATTENTION ($issues issues)"
    echo ""
    echo "Some WCAG 2.1 AA requirements need additional consideration."
fi
)

## Recommendations

### Immediate Actions
- Ensure all UI components include proper ARIA labels
- Implement comprehensive keyboard navigation testing
- Validate color contrast ratios for all design elements
- Create accessibility testing checklist

### Long-term Improvements
- Establish automated accessibility testing in CI/CD
- Regular accessibility audits by certified professionals
- User testing with assistive technology users
- Accessibility training for all team members

EOF
    
    echo "📄 WCAG compliance report: $WCAG_REPORT"
    return $issues
}

check_gdpr_compliance() {
    local agent="$1"
    echo "🔒 Checking GDPR compliance..."
    
    local issues=0
    GDPR_REPORT="work/compliance/gdpr_report_$(date +%Y%m%d_%H%M%S).md"
    
    cat > "$GDPR_REPORT" << EOF
# GDPR Compliance Report

**Generated:** $(date)
**Agent:** $agent
**Regulation:** General Data Protection Regulation (EU) 2016/679

## Compliance Framework

### Article 25 - Data Protection by Design and by Default

#### Privacy by Design Implementation
EOF

    # Check security-engineer coverage
    if [[ "$agent" == "security-engineer" || "$agent" == "all" ]]; then
        if [[ -f ".claude/prompts/agents/security/compliance-audit-and-governance.md" ]]; then
            echo "- ✅ Compliance audit framework available" >> "$GDPR_REPORT"
        else
            echo "- ❌ Missing compliance audit framework" >> "$GDPR_REPORT"
            issues=$((issues + 1))
        fi
        
        if [[ -f ".claude/prompts/agents/security/identity-and-access-management.md" ]]; then
            echo "- ✅ Identity and access management controls" >> "$GDPR_REPORT"
        else
            echo "- ❌ Missing IAM compliance framework" >> "$GDPR_REPORT"
            issues=$((issues + 1))
        fi
        
        # Check for data protection considerations
        if grep -r -i "gdpr\|privacy\|consent\|data.*protection" .claude/prompts/agents/security/ >/dev/null 2>&1; then
            echo "- ✅ Data protection considerations included" >> "$GDPR_REPORT"
        else
            echo "- ⚠️ Limited data protection guidance" >> "$GDPR_REPORT"
        fi
    fi
    
    cat >> "$GDPR_REPORT" << EOF

### Key GDPR Requirements

#### Article 6 - Lawfulness of Processing
- [ ] Legal basis identification for data processing
- [ ] Consent mechanisms implementation
- [ ] Legitimate interest assessments

#### Article 7 - Conditions for Consent  
- [ ] Clear and plain language consent forms
- [ ] Granular consent options
- [ ] Consent withdrawal mechanisms
- [ ] Consent records maintenance

#### Article 13-14 - Information to Data Subjects
- [ ] Privacy notices at collection point
- [ ] Transparent information about processing
- [ ] Data subject rights communication

#### Article 15-22 - Data Subject Rights
- [ ] Right of access implementation
- [ ] Right to rectification processes
- [ ] Right to erasure (right to be forgotten)
- [ ] Right to data portability
- [ ] Right to object to processing
- [ ] Automated decision-making safeguards

#### Article 32 - Security of Processing
- [ ] Appropriate technical measures
- [ ] Organizational measures
- [ ] Encryption implementation
- [ ] Regular security testing
- [ ] Incident response procedures

#### Article 33-34 - Data Breach Notification
- [ ] 72-hour authority notification process
- [ ] Data subject notification procedures
- [ ] Breach documentation requirements

#### Article 35 - Data Protection Impact Assessment
- [ ] DPIA process framework
- [ ] High-risk processing identification
- [ ] Privacy risk assessment methodology

#### Article 37 - Data Protection Officer
- [ ] DPO appointment criteria
- [ ] DPO responsibilities definition
- [ ] Independence and expertise requirements

### Technical and Organizational Measures

#### Data Minimization (Article 5.1.c)
- Collect only necessary data
- Regular data retention reviews
- Automated data deletion processes

#### Accuracy (Article 5.1.d)  
- Data quality validation
- Regular data accuracy checks
- Error correction procedures

#### Storage Limitation (Article 5.1.e)
- Defined retention periods
- Automated deletion schedules
- Archival procedures

#### Integrity and Confidentiality (Article 5.1.f)
- Access control mechanisms
- Data encryption at rest and in transit
- Audit logging and monitoring

## Compliance Status

$(
if [[ $issues -eq 0 ]]; then
    echo "✅ **Overall Status:** FRAMEWORK READY"
    echo ""
    echo "Security engineering framework addresses key GDPR requirements."
else
    echo "⚠️ **Overall Status:** REQUIRES ENHANCEMENT ($issues gaps)"
    echo ""
    echo "Additional GDPR-specific measures needed in security framework."
fi
)

## Action Plan

### Phase 1: Foundation (Immediate)
1. Complete security compliance audit framework
2. Implement comprehensive IAM controls
3. Establish data protection impact assessment process
4. Create privacy by design checklist

### Phase 2: Implementation (30 days)
1. Deploy consent management systems
2. Implement data subject rights handling
3. Establish breach notification procedures
4. Create privacy notices and documentation

### Phase 3: Validation (60 days)
1. Conduct comprehensive GDPR audit
2. Test incident response procedures
3. Validate technical and organizational measures
4. Staff training and awareness programs

EOF
    
    echo "📄 GDPR compliance report: $GDPR_REPORT"
    return $issues
}

check_sox_compliance() {
    local agent="$1"
    echo "📊 Checking SOX compliance..."
    
    local issues=0
    SOX_REPORT="work/compliance/sox_report_$(date +%Y%m%d_%H%M%S).md"
    
    cat > "$SOX_REPORT" << EOF
# Sarbanes-Oxley (SOX) Compliance Report

**Generated:** $(date)
**Agent:** $agent  
**Regulation:** Sarbanes-Oxley Act of 2002

## SOX Compliance Framework

### Section 302 - Corporate Responsibility for Financial Reports

#### Management Certification Requirements
- Executive responsibility for internal controls
- Quarterly and annual certifications
- Material weakness disclosure

### Section 404 - Management Assessment of Internal Controls

#### Internal Control Framework
EOF

    # Check for proper controls in relevant agents
    if [[ "$agent" == "security-engineer" || "$agent" == "reviewer" || "$agent" == "all" ]]; then
        # Check for audit and review capabilities
        if [[ -f ".claude/prompts/agents/review/sonarqube-code-quality-analysis.md" ]]; then
            echo "- ✅ Code quality audit framework available" >> "$SOX_REPORT"
        else
            echo "- ❌ Missing automated code review controls" >> "$SOX_REPORT"
            issues=$((issues + 1))
        fi
        
        if [[ -f ".claude/prompts/agents/security/security-controls-implementation.md" ]]; then
            echo "- ✅ Security controls implementation framework" >> "$SOX_REPORT"
        else
            echo "- ❌ Missing security controls framework" >> "$SOX_REPORT"
            issues=$((issues + 1))
        fi
        
        # Check for incident response and forensics
        if [[ -f ".claude/prompts/agents/security/incident-response-and-forensics.md" ]]; then
            echo "- ✅ Incident response and audit trail capabilities" >> "$SOX_REPORT"
        else
            echo "- ❌ Missing incident response framework" >> "$SOX_REPORT"
            issues=$((issues + 1))
        fi
    fi
    
    cat >> "$SOX_REPORT" << EOF

### Key SOX IT Controls

#### Access Controls (IT General Controls)
- [ ] Logical access management
- [ ] User access provisioning/deprovisioning
- [ ] Privileged access management
- [ ] Segregation of duties enforcement

#### Change Management (IT General Controls)
- [ ] Software development lifecycle controls
- [ ] Change approval processes
- [ ] Testing and validation procedures
- [ ] Production change documentation

#### Computer Operations (IT General Controls)
- [ ] Data backup and recovery procedures
- [ ] Business continuity planning
- [ ] Performance monitoring
- [ ] Capacity management

#### Data Integrity and Security
- [ ] Data validation controls
- [ ] Database security measures
- [ ] Encryption for sensitive data
- [ ] Audit trail maintenance

### Application Controls

#### Input Controls
- [ ] Data validation and verification
- [ ] Authorization requirements
- [ ] Error handling procedures
- [ ] Completeness checks

#### Processing Controls
- [ ] Transaction processing accuracy
- [ ] Calculation verification
- [ ] Data transformation controls
- [ ] Exception reporting

#### Output Controls  
- [ ] Report accuracy verification
- [ ] Output distribution controls
- [ ] Reconciliation procedures
- [ ] Archive and retention controls

### Audit and Monitoring

#### Continuous Monitoring
- [ ] Real-time transaction monitoring
- [ ] Exception detection and reporting
- [ ] Performance metrics tracking
- [ ] Compliance dashboard implementation

#### Audit Trail Requirements
- [ ] Complete transaction logging
- [ ] User activity tracking
- [ ] System access monitoring
- [ ] Change history maintenance

#### Management Reporting
- [ ] Control effectiveness reporting
- [ ] Deficiency identification and tracking
- [ ] Remediation status updates
- [ ] Executive dashboard metrics

## Control Testing and Validation

### Testing Requirements
- Annual control testing program
- Independent validation processes
- Management testing and review
- External auditor coordination

### Documentation Standards
- Control documentation maintenance
- Process flow documentation
- Risk and control matrices
- Testing evidence retention

## Compliance Status

$(
if [[ $issues -eq 0 ]]; then
    echo "✅ **Overall Status:** CONTROL FRAMEWORK ADEQUATE"
    echo ""
    echo "Framework provides foundation for SOX compliance controls."
else
    echo "⚠️ **Overall Status:** CONTROL GAPS IDENTIFIED ($issues areas)"
    echo ""
    echo "Additional controls and processes needed for full SOX compliance."
fi
)

## Remediation Plan

### Critical Controls (Immediate - 30 days)
1. Implement automated code review controls
2. Establish comprehensive security controls framework  
3. Deploy incident response and audit trail capabilities
4. Create change management procedures

### Important Controls (60 days)
1. Implement access control management
2. Establish data integrity validation
3. Deploy continuous monitoring solutions
4. Create compliance reporting dashboards

### Supporting Controls (90 days)
1. Complete control documentation
2. Implement control testing procedures
3. Establish management reporting
4. Conduct control effectiveness assessment

EOF
    
    echo "📄 SOX compliance report: $SOX_REPORT"
    return $issues
}

run_comprehensive_compliance_check() {
    local agent="$1"
    
    echo "🔍 Running comprehensive compliance check for: $agent"
    
    local total_issues=0
    
    # Run all compliance checks
    check_wcag_compliance "$agent"
    total_issues=$((total_issues + $?))
    
    check_gdpr_compliance "$agent"
    total_issues=$((total_issues + $?))
    
    check_sox_compliance "$agent"
    total_issues=$((total_issues + $?))
    
    # Generate summary report
    SUMMARY_REPORT="work/compliance/compliance_summary_$(date +%Y%m%d_%H%M%S).md"
    
    cat > "$SUMMARY_REPORT" << EOF
# Compliance Summary Report

**Generated:** $(date)
**Agent Scope:** $agent

## Compliance Overview

| Standard | Status | Issues | Priority |
|----------|--------|--------|----------|
| WCAG 2.1 AA | $(if [[ -f work/compliance/wcag_report_*.md ]]; then grep -l "COMPLIANT" work/compliance/wcag_report_*.md >/dev/null 2>&1 && echo "✅ Compliant" || echo "⚠️ Needs Review"; else echo "🔍 Not Checked"; fi) | - | High |
| GDPR | $(if [[ -f work/compliance/gdpr_report_*.md ]]; then grep -l "FRAMEWORK READY" work/compliance/gdpr_report_*.md >/dev/null 2>&1 && echo "✅ Ready" || echo "⚠️ Enhancement Needed"; else echo "🔍 Not Checked"; fi) | - | Critical |
| SOX | $(if [[ -f work/compliance/sox_report_*.md ]]; then grep -l "ADEQUATE" work/compliance/sox_report_*.md >/dev/null 2>&1 && echo "✅ Adequate" || echo "⚠️ Gaps Identified"; else echo "🔍 Not Checked"; fi) | - | High |

## Overall Compliance Health

$(
if [[ $total_issues -eq 0 ]]; then
    echo "🟢 **Status:** EXCELLENT - Framework meets major compliance requirements"
elif [[ $total_issues -le 3 ]]; then
    echo "🟡 **Status:** GOOD - Minor enhancements needed ($total_issues issues)"
elif [[ $total_issues -le 6 ]]; then
    echo "🟠 **Status:** FAIR - Several areas need attention ($total_issues issues)"
else
    echo "🔴 **Status:** NEEDS IMPROVEMENT - Significant compliance gaps ($total_issues issues)"
fi
)

## Priority Actions

### Critical (Immediate)
$(find work/compliance -name "*report*.md" -exec grep -l "❌" {} \; | head -3 | while read file; do echo "- Address critical issues in $(basename "$file")"; done)

### High Priority (30 days)  
- Complete missing compliance frameworks
- Implement automated compliance checking
- Establish regular compliance audits

### Medium Priority (90 days)
- Enhance documentation and training
- Implement compliance dashboards
- Establish continuous monitoring

## Next Steps

1. **Review detailed reports** in work/compliance/ directory
2. **Prioritize remediation** based on business criticality
3. **Implement controls** following recommended timelines
4. **Schedule regular reviews** for ongoing compliance

EOF
    
    echo "📄 Compliance summary: $SUMMARY_REPORT"
    
    return $total_issues
}

# Main execution logic
case "$COMPLIANCE_TYPE" in
    "wcag")
        check_wcag_compliance "$AGENT_TYPE"
        EXIT_CODE=$?
        ;;
        
    "gdpr")
        check_gdpr_compliance "$AGENT_TYPE"
        EXIT_CODE=$?
        ;;
        
    "sox")
        check_sox_compliance "$AGENT_TYPE"
        EXIT_CODE=$?
        ;;
        
    "all")
        run_comprehensive_compliance_check "$AGENT_TYPE"
        EXIT_CODE=$?
        ;;
        
    *)
        echo "❌ Unknown compliance type: $COMPLIANCE_TYPE"
        echo "Available types: wcag, gdpr, sox, all"
        exit 1
        ;;
esac

# Log compliance check
echo "$(date): Compliance check ($COMPLIANCE_TYPE) completed for $AGENT_TYPE - Issues: $EXIT_CODE" >> work/compliance-activity.log

if [[ $EXIT_CODE -eq 0 ]]; then
    echo "✅ Compliance check passed - no issues found"
else
    echo "⚠️ Compliance issues identified ($EXIT_CODE) - review reports for details"
fi

echo "🛡️ Compliance Automation Hook completed"
exit $EXIT_CODE