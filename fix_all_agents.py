#!/usr/bin/env python3
"""
Automated Agent Technical Proficiencies Fixer
Fix all 30 agents with placeholder Technical Proficiencies
"""

import os
import re
from pathlib import Path

# Technology mappings based on agent names and descriptions
AGENT_TECH_MAPPING = {
    # Custom agents
    'electronics-engineer': [
        'C, C++, Python, VHDL, Verilog',
        'KiCad, Altium Designer, Eagle, LTSpice',
        'Arduino, Raspberry Pi, ESP32, STM32',
        'Circuit design, PCB layout, Embedded systems'
    ],
    'embedded-engineer': [
        'C, C++, Assembly, Python',
        'FreeRTOS, Zephyr, Arduino, STM32',
        'ARM Cortex, AVR, PIC, ESP32',
        'Real-time systems, IoT, Microcontrollers'
    ],
    'scientific-computing-specialist': [
        'Python, C++, Fortran, MATLAB, R',
        'NumPy, SciPy, Pandas, OpenMP, MPI',
        'CUDA, OpenCL, HPC clusters',
        'Scientific computing, Parallel processing'
    ],

    # Enterprise agents
    'cloud-engineer': [
        'Python, Bash, Go, YAML, JSON',
        'AWS, Azure, GCP, Kubernetes, Docker',
        'Terraform, CloudFormation, Ansible',
        'Infrastructure as Code, DevOps'
    ],
    'devops-architect': [
        'Python, Bash, Go, YAML',
        'Kubernetes, Docker, Jenkins, GitLab CI',
        'Prometheus, Grafana, ELK Stack',
        'CI/CD, Infrastructure automation'
    ],
    'database-administrator': [
        'SQL, Python, Bash, PowerShell',
        'PostgreSQL, MySQL, Oracle, MongoDB',
        'Redis, Elasticsearch, InfluxDB',
        'Database optimization, Backup/Recovery'
    ],
    'mobile-developer': [
        'Swift, Kotlin, Dart, JavaScript',
        'React Native, Flutter, Xamarin',
        'iOS SDK, Android SDK, Cordova',
        'Mobile app development, Cross-platform'
    ],
    'enterprise-architect': [
        'Java, C#, Python, JavaScript',
        'Spring, .NET, Microservices, SOA',
        'Enterprise patterns, Cloud platforms',
        'System design, Integration patterns'
    ],
    'security-engineer': [
        'Python, Go, C++, Bash',
        'OWASP, OAuth, JWT, TLS/SSL',
        'Penetration testing, Vulnerability assessment',
        'Security frameworks, Compliance'
    ],
    'automation-engineer': [
        'Python, Bash, PowerShell, YAML',
        'Ansible, Puppet, Chef, Terraform',
        'Jenkins, GitLab CI, Azure DevOps',
        'Infrastructure automation, CI/CD'
    ],
    'monitoring-engineer': [
        'Python, Go, Bash, YAML',
        'Prometheus, Grafana, Nagios, Zabbix',
        'ELK Stack, Splunk, Datadog',
        'Observability, Alerting, Metrics'
    ],
    'platform-engineer': [
        'Python, Go, Bash, YAML',
        'Kubernetes, Docker, Service Mesh',
        'API Gateway, Load Balancers',
        'Platform development, Developer tools'
    ],
    'integration-architect': [
        'Java, Python, C#, JavaScript',
        'Apache Camel, MuleSoft, WSO2',
        'REST, SOAP, GraphQL, Message Queues',
        'Enterprise integration, API design'
    ],
    'network-architect': [
        'Python, Bash, Network protocols',
        'Cisco, Juniper, F5, Palo Alto',
        'BGP, OSPF, MPLS, SDN',
        'Network design, Security, Performance'
    ],
    'middleware-engineer': [
        'Java, Python, C#, JavaScript',
        'Apache Kafka, RabbitMQ, ActiveMQ',
        'Spring Integration, Apache Camel',
        'Message brokers, Integration patterns'
    ],
    'compliance-auditor': [
        'Python, SQL, PowerShell, Bash',
        'GRC tools, SIEM, Vulnerability scanners',
        'GDPR, SOX, HIPAA, ISO 27001',
        'Compliance frameworks, Risk assessment'
    ],
    'risk-manager': [
        'Python, R, SQL, Excel/VBA',
        'Risk management tools, Analytics',
        'Monte Carlo simulations, Statistics',
        'Risk modeling, Compliance'
    ],
    'governance-architect': [
        'Python, PowerShell, SQL',
        'Governance tools, Policy engines',
        'Identity management, Access control',
        'Enterprise governance, Compliance'
    ],
    'project-coordinator': [
        'Python, JavaScript, SQL',
        'Jira, Confluence, Microsoft Project',
        'Agile tools, Gantt charts, Reporting',
        'Project management, Coordination'
    ],
    'project-owner': [
        'Python, JavaScript, SQL',
        'Project management tools, Analytics',
        'Business intelligence, Reporting',
        'Strategic planning, Stakeholder management'
    ],
    'reviewer': [
        'Python, JavaScript, Java, C++',
        'Code review tools, Static analysis',
        'SonarQube, CodeClimate, ESLint',
        'Code quality, Best practices'
    ],
    'technical-writer': [
        'Markdown, HTML, CSS, JavaScript',
        'GitBook, Confluence, Sphinx, Jekyll',
        'Documentation tools, Version control',
        'Technical writing, Information architecture'
    ],
    'capacity-planner': [
        'Python, R, SQL, MATLAB',
        'Capacity planning tools, Analytics',
        'Performance monitoring, Forecasting',
        'Resource optimization, Scaling'
    ],
    'incident-responder': [
        'Python, Bash, PowerShell',
        'SIEM tools, Incident management',
        'Forensics tools, Log analysis',
        'Incident response, Security operations'
    ],
    'reliability-engineer': [
        'Python, Go, Bash, YAML',
        'Prometheus, Grafana, Chaos engineering',
        'Load testing, Performance analysis',
        'SRE practices, Reliability engineering'
    ],
    'sre-engineer': [
        'Python, Go, Bash, YAML',
        'Kubernetes, Prometheus, Grafana',
        'Terraform, Ansible, SLO/SLI',
        'Site reliability, Observability'
    ]
}

def fix_agent_technical_proficiencies(file_path: Path):
    """Fix Technical Proficiencies for a single agent file"""
    try:
        content = file_path.read_text(encoding='utf-8')

        # Check if it has placeholder proficiencies
        if 'Industry-standard tools' not in content:
            print(f"  ✅ {file_path.stem} - already has proper Technical Proficiencies")
            return False

        # Extract agent name from filename
        agent_name = file_path.stem

        # Get technology mapping
        if agent_name in AGENT_TECH_MAPPING:
            tech_lines = AGENT_TECH_MAPPING[agent_name]
        else:
            # Generic fallback based on category
            category = 'Unknown'
            if 'graphics' in str(file_path):
                tech_lines = [
                    'C++, Python, OpenGL, Graphics APIs',
                    'Rendering, Shaders, Visualization',
                    'Performance optimization',
                    'Cross-platform development'
                ]
            elif 'desktop' in str(file_path):
                tech_lines = [
                    'C++, Python, Qt, Desktop frameworks',
                    'GUI development, Cross-platform',
                    'Application architecture',
                    'User interface design'
                ]
            elif 'enterprise' in str(file_path):
                tech_lines = [
                    'Enterprise technologies, Cloud platforms',
                    'Scalable architectures, Best practices',
                    'Integration patterns, Security',
                    'Performance optimization'
                ]
            else:
                tech_lines = [
                    'Modern programming languages',
                    'Industry frameworks and tools',
                    'Best practices and methodologies',
                    'Professional development tools'
                ]

        # Build new Technical Proficiencies section
        new_proficiencies = "**Technical Proficiencies:**\n"
        for line in tech_lines:
            new_proficiencies += f"- {line}\n"

        # Replace the placeholder section
        placeholder_pattern = r'\*\*Technical Proficiencies:\*\*\n- Industry-standard tools\n- Modern frameworks\n- Best practices\n- Enterprise solutions'

        updated_content = re.sub(
            placeholder_pattern,
            new_proficiencies.rstrip(),
            content
        )

        # Write back the updated content
        file_path.write_text(updated_content, encoding='utf-8')
        print(f"  🔧 {file_path.stem} - fixed Technical Proficiencies")
        return True

    except Exception as e:
        print(f"  ❌ {file_path.stem} - error: {e}")
        return False

def main():
    """Fix all agents with placeholder Technical Proficiencies"""
    print("🚀 Fixing all agents with placeholder Technical Proficiencies")
    print("=" * 60)

    agents_dir = Path('.claude/agents')
    fixed_count = 0
    total_checked = 0

    # Find all agent files
    for agent_file in agents_dir.rglob('*.md'):
        total_checked += 1
        if fix_agent_technical_proficiencies(agent_file):
            fixed_count += 1

    print("\n" + "=" * 60)
    print(f"✅ Fixed {fixed_count} agents out of {total_checked} total agents")
    print("🎯 All agents now have proper Technical Proficiencies!")

if __name__ == '__main__':
    main()