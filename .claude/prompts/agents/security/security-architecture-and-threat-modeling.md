# Security Architecture and Threat Modeling

**Agent: security-engineer**
**Purpose: Design comprehensive security architecture and conduct thorough threat modeling**

---

## 🎯 Mission

Establish robust security controls and frameworks that protect applications, data, and infrastructure while enabling business operations and maintaining compliance requirements.

## 📋 Security Architecture Process

### Step 1: Security Requirements Analysis
**From business and architecture specifications:**
- **Regulatory compliance** requirements (GDPR, HIPAA, SOX, PCI-DSS)
- **Data classification** and sensitivity levels
- **Business risk tolerance** and security priorities
- **User access patterns** and authentication needs
- **Integration security** with external systems

### Step 2: Threat Modeling Framework

**STRIDE Threat Model:**
- **Spoofing** - Impersonating users or systems
- **Tampering** - Unauthorized modification of data
- **Repudiation** - Denying actions performed
- **Information Disclosure** - Unauthorized access to information
- **Denial of Service** - Preventing legitimate access
- **Elevation of Privilege** - Gaining unauthorized permissions

**Asset Identification:**
```
High-Value Assets:
├── User Authentication Data
│   ├── Passwords and credentials
│   ├── Session tokens and certificates
│   └── Multi-factor authentication secrets
├── Business Data
│   ├── Customer personal information
│   ├── Financial transaction data
│   └── Proprietary business logic
└── Infrastructure Components
    ├── Database servers and data
    ├── API endpoints and services
    └── Administrative access systems
```

### Step 3: Attack Surface Analysis

**External Attack Vectors:**
- **Web application** interfaces and APIs
- **Network services** and exposed ports
- **Third-party integrations** and dependencies
- **Social engineering** and phishing attacks
- **Supply chain** vulnerabilities

**Internal Attack Vectors:**
- **Privileged user** access and insider threats
- **Lateral movement** within network infrastructure
- **Data exfiltration** channels and methods
- **System vulnerabilities** and misconfigurations
- **Process weaknesses** and human error

## 🛡️ Security Controls Implementation

### Step 4: Authentication and Authorization

**Multi-Factor Authentication (MFA):**
```yaml
# Example MFA policy configuration
authentication_policy:
  mfa_required: true
  mfa_methods:
    - totp  # Time-based One-Time Password
    - sms   # SMS verification (backup only)
    - hardware_key  # FIDO2/WebAuthn
  
  session_management:
    timeout_idle: 30m
    timeout_absolute: 8h
    concurrent_sessions: 3
    
  password_policy:
    min_length: 12
    require_uppercase: true
    require_lowercase: true
    require_numbers: true
    require_special: true
    history_count: 12
    max_age_days: 90
```

**Role-Based Access Control (RBAC):**
```json
{
  "roles": {
    "admin": {
      "permissions": ["*"],
      "resources": ["*"]
    },
    "user_manager": {
      "permissions": ["read", "write"],
      "resources": ["users", "groups"]
    },
    "read_only": {
      "permissions": ["read"],
      "resources": ["users", "reports"]
    }
  },
  "policies": {
    "data_access": {
      "rules": [
        {
          "effect": "allow",
          "principal": "role:admin",
          "action": "*",
          "resource": "*"
        },
        {
          "effect": "allow", 
          "principal": "role:user_manager",
          "action": ["create", "read", "update"],
          "resource": "users/*"
        }
      ]
    }
  }
}
```

### Step 5: Data Protection and Encryption

**Encryption Strategy:**
- **Data at Rest** - Database encryption, file system encryption
- **Data in Transit** - TLS/SSL for all communications
- **Data in Processing** - Application-level encryption for sensitive fields
- **Key Management** - Hardware Security Modules (HSM) or cloud KMS
- **Certificate Management** - Automated certificate lifecycle management

**Implementation Example:**
```python
# Data encryption service
import cryptography
from cryptography.fernet import Fernet

class DataEncryption:
    def __init__(self, key_service):
        self.key_service = key_service
        
    def encrypt_pii(self, data, user_context):
        """Encrypt personally identifiable information"""
        key = self.key_service.get_encryption_key('pii', user_context)
        fernet = Fernet(key)
        
        encrypted_data = {}
        for field, value in data.items():
            if field in ['ssn', 'credit_card', 'email']:
                encrypted_data[field] = fernet.encrypt(value.encode())
            else:
                encrypted_data[field] = value
                
        return encrypted_data
        
    def decrypt_pii(self, encrypted_data, user_context):
        """Decrypt PII with proper authorization"""
        if not self.authorize_decrypt(user_context):
            raise UnauthorizedError("Insufficient privileges for PII access")
            
        key = self.key_service.get_encryption_key('pii', user_context)
        fernet = Fernet(key)
        
        # Decrypt and audit access
        self.audit_log.record_pii_access(user_context, encrypted_data.keys())
        return self._decrypt_fields(encrypted_data, fernet)
```

## 🔍 Security Monitoring and Incident Response

### Step 6: Security Information and Event Management (SIEM)

**Log Collection Strategy:**
```yaml
# Security logging configuration
logging:
  security_events:
    - authentication_attempts
    - authorization_failures  
    - privilege_escalations
    - data_access_patterns
    - configuration_changes
    - network_anomalies
    
  log_sources:
    - application_logs
    - web_server_access_logs
    - database_audit_logs
    - system_security_logs
    - network_device_logs
    
  retention:
    security_logs: 7_years
    audit_logs: 10_years
    access_logs: 1_year
    debug_logs: 30_days
```

**Automated Threat Detection:**
```python
# Security monitoring rules
class SecurityMonitoring:
    def detect_brute_force(self, login_attempts):
        """Detect brute force login attempts"""
        failed_attempts = self.count_failed_logins(
            window_minutes=5,
            threshold=5
        )
        
        if failed_attempts > 5:
            return {
                'threat_type': 'brute_force',
                'severity': 'high',
                'recommended_action': 'block_ip_temporary',
                'duration_minutes': 30
            }
    
    def detect_privilege_escalation(self, user_actions):
        """Detect unusual privilege usage"""
        baseline = self.get_user_baseline(user_actions.user_id)
        
        if user_actions.permissions_used > baseline.max_permissions * 1.5:
            return {
                'threat_type': 'privilege_escalation',
                'severity': 'critical',
                'recommended_action': 'require_additional_auth'
            }
```

### Step 7: Vulnerability Management

**Security Testing Framework:**
- **Static Application Security Testing (SAST)** - Code analysis
- **Dynamic Application Security Testing (DAST)** - Runtime testing
- **Interactive Application Security Testing (IAST)** - Hybrid approach
- **Dependency Scanning** - Third-party vulnerability detection
- **Infrastructure Scanning** - System and network vulnerabilities

**Continuous Security Integration:**
```yaml
# Security testing in CI/CD pipeline
name: Security Scan

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2
      
    - name: SAST Scan
      uses: securecodewarrior/github-action-add-sarif@v1
      with:
        sarif-file: 'sast-results.sarif'
        
    - name: Dependency Check
      run: |
        npm audit --audit-level high
        safety check -r requirements.txt
        
    - name: Container Security Scan
      run: |
        trivy image --exit-code 1 --severity HIGH,CRITICAL myapp:latest
        
    - name: Infrastructure Security Scan
      run: |
        checkov -d ./terraform --framework terraform
```

## 🚨 Incident Response and Recovery

### Step 8: Security Incident Management

**Incident Response Plan:**
```yaml
incident_response:
  phases:
    preparation:
      - incident_response_team_defined
      - communication_plan_established
      - tools_and_resources_available
      - regular_training_conducted
      
    identification:
      - security_monitoring_active
      - alert_triage_procedures
      - incident_classification_criteria
      - escalation_triggers_defined
      
    containment:
      - isolation_procedures
      - evidence_preservation
      - damage_assessment
      - communication_protocols
      
    eradication:
      - root_cause_analysis
      - vulnerability_remediation
      - system_hardening
      - security_improvement
      
    recovery:
      - system_restoration
      - monitoring_enhancement
      - validation_testing
      - business_continuity
      
    lessons_learned:
      - post_incident_review
      - process_improvement
      - documentation_update
      - training_enhancement
```

**Incident Classification:**
- **P0 - Critical** - Data breach, system compromise affecting production
- **P1 - High** - Unauthorized access, significant security control failure
- **P2 - Medium** - Policy violation, minor security incident
- **P3 - Low** - Security awareness issue, procedural non-compliance

## 📊 Compliance and Governance

### Step 9: Compliance Framework

**GDPR Compliance Controls:**
```json
{
  "gdpr_controls": {
    "data_protection_by_design": {
      "privacy_impact_assessments": "required",
      "data_minimization": "enforced",
      "purpose_limitation": "implemented"
    },
    "individual_rights": {
      "right_to_access": "automated_portal",
      "right_to_rectification": "self_service",
      "right_to_erasure": "workflow_based",
      "right_to_portability": "data_export_api"
    },
    "breach_notification": {
      "detection_time": "72_hours",
      "authority_notification": "automated",
      "individual_notification": "risk_based"
    }
  }
}
```

**Security Governance:**
- **Security policies** and procedures documentation
- **Risk assessment** and management procedures
- **Security awareness** training and certification
- **Vendor security** assessment and management
- **Regular security** audits and compliance reviews

## 📤 Deliverables

- **Security Architecture Document** with controls and frameworks
- **Threat Model Report** with risk assessment and mitigation strategies
- **Security Policies** and procedures documentation
- **Incident Response Plan** with roles, responsibilities, and procedures
- **Compliance Framework** with controls and audit procedures
- **Security Monitoring Setup** with SIEM configuration and alerting
- **Vulnerability Management** program and remediation procedures

## 🤝 Collaboration Points

**With software-architect:** Security architecture integration and technical controls
**With deployment-engineer:** Infrastructure security and deployment pipeline security
**With data-engineer:** Data protection, encryption, and access controls
**With api-engineer:** API security, authentication, and authorization
**With qa-engineer:** Security testing integration and vulnerability validation

---
*Comprehensive security architecture protects business assets while enabling secure, compliant operations and building stakeholder trust.*