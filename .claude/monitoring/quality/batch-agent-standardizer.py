#!/usr/bin/env python3
"""
Batch Agent Standardization Tool
Automatically converts all 45 agents to unified template standard
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

class AgentStandardizer:
    """Automated agent standardization engine"""

    def __init__(self, framework_root: str):
        self.framework_root = Path(framework_root)
        self.agents_dir = self.framework_root / ".claude/agents"
        self.template_file = self.framework_root / ".claude/templates/agent_template.md"

        # Load template
        self.template_content = self._load_template()

        # Agent metadata mapping
        self.agent_metadata = self._create_agent_metadata_mapping()

    def _load_template(self) -> str:
        """Load the unified agent template"""
        try:
            with open(self.template_file, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            raise Exception(f"Failed to load template: {e}")

    def _create_agent_metadata_mapping(self) -> Dict[str, Dict[str, Any]]:
        """Create comprehensive metadata mapping for all agents"""
        return {
            # Core Agents - Architecture
            "software-architect": {
                "type": "Core", "category": "Architecture", "subcategory": "System Design",
                "title": "Software Architect - Enterprise Systems Design",
                "domain_focus": "Enterprise architecture, microservices, cloud-native systems",
                "primary_skills": ["Enterprise Architecture Design", "Scalability Engineering", "Security Architecture", "Technical Leadership"],
                "technologies": ["Java, Python, TypeScript, Go, C#", "Spring Boot, .NET Core, React, Angular", "AWS, Azure, Google Cloud, Kubernetes", "Domain-Driven Design, CQRS, Event Sourcing"]
            },
            "ux-designer": {
                "type": "Core", "category": "Architecture", "subcategory": "User Experience Design",
                "title": "UX Designer - User-Centered Design Excellence",
                "domain_focus": "User experience strategy, design systems, accessibility",
                "primary_skills": ["User Experience Strategy", "Interface Design", "Design Systems", "Accessibility Leadership"],
                "technologies": ["Figma, Sketch, Adobe Creative Suite", "React, Vue, Angular design integration", "WCAG 2.1, accessibility tools", "User research, analytics, prototyping"]
            },

            # Core Agents - Development
            "frontend-engineer": {
                "type": "Core", "category": "Development", "subcategory": "Frontend Engineering",
                "title": "Frontend Engineer - Modern Web Applications",
                "domain_focus": "React, Vue, Angular, TypeScript, performance optimization",
                "primary_skills": ["Frontend Architecture", "Performance Optimization", "Responsive Design", "State Management"],
                "technologies": ["React, Vue.js, Angular, TypeScript", "Webpack, Vite, ESBuild, Parcel", "Redux, Zustand, Pinia, NgRx", "Jest, Cypress, Testing Library"]
            },
            "backend-engineer": {
                "type": "Core", "category": "Development", "subcategory": "Backend Engineering",
                "title": "Backend Engineer - Scalable Server Systems",
                "domain_focus": "API development, microservices, database optimization",
                "primary_skills": ["Backend Architecture", "API Development", "Database Design", "Microservices"],
                "technologies": ["Node.js, Python, Java, Go", "Express, FastAPI, Spring Boot", "PostgreSQL, MongoDB, Redis", "Docker, Kubernetes, AWS"]
            },
            "api-engineer": {
                "type": "Core", "category": "Development", "subcategory": "API Engineering",
                "title": "API Engineer - Enterprise Integration",
                "domain_focus": "REST, GraphQL, microservices, API management",
                "primary_skills": ["API Design", "Integration Architecture", "Performance Optimization", "Security Implementation"],
                "technologies": ["REST, GraphQL, gRPC", "OpenAPI, Swagger, Postman", "API Gateway, rate limiting", "OAuth, JWT, security"]
            },

            # Core Agents - Data
            "data-engineer": {
                "type": "Core", "category": "Data", "subcategory": "Data Engineering",
                "title": "Data Engineer - Data Pipeline Architecture",
                "domain_focus": "Data pipelines, ETL, analytics, big data",
                "primary_skills": ["Data Pipeline Architecture", "ETL Development", "Big Data Processing", "Analytics Engineering"],
                "technologies": ["Python, Scala, SQL", "Apache Spark, Kafka, Airflow", "AWS Redshift, Snowflake, BigQuery", "dbt, Pandas, NumPy"]
            },

            # Core Agents - Management
            "session-manager": {
                "type": "Core", "category": "Management", "subcategory": "Session Management",
                "title": "Session Manager - Context Preservation",
                "domain_focus": "Session management, context preservation, state recovery",
                "primary_skills": ["Session Lifecycle Management", "Context Preservation", "State Recovery", "Multi-Session Coordination"],
                "technologies": ["Session storage, state serialization", "Context analysis, recovery algorithms", "Multi-session coordination", "Framework integration"]
            },

            # Core Agents - Operations
            "deployment-engineer": {
                "type": "Core", "category": "Operations", "subcategory": "Deployment Engineering",
                "title": "Deployment Engineer - CI/CD Excellence",
                "domain_focus": "CI/CD, infrastructure automation, deployment strategies",
                "primary_skills": ["CI/CD Pipeline Design", "Infrastructure Automation", "Deployment Strategies", "Monitoring Integration"],
                "technologies": ["Jenkins, GitHub Actions, GitLab CI", "Docker, Kubernetes, Helm", "Terraform, CloudFormation", "Prometheus, Grafana, ELK"]
            },

            # Core Agents - Quality
            "qa-engineer": {
                "type": "Core", "category": "Quality", "subcategory": "Quality Assurance",
                "title": "QA Engineer - Quality Excellence",
                "domain_focus": "Test automation, quality assurance, performance testing",
                "primary_skills": ["Test Automation", "Quality Assurance", "Performance Testing", "Security Testing"],
                "technologies": ["Selenium, Cypress, Playwright", "Jest, PyTest, JUnit", "JMeter, K6, LoadRunner", "SonarQube, OWASP tools"]
            },
            "security-engineer": {
                "type": "Core", "category": "Quality", "subcategory": "Security Engineering",
                "title": "Security Engineer - Application Security",
                "domain_focus": "Application security, threat modeling, compliance",
                "primary_skills": ["Application Security", "Threat Modeling", "Compliance Management", "Security Architecture"],
                "technologies": ["OWASP, security scanners", "Penetration testing, vulnerability assessment", "SIEM, security monitoring", "Compliance frameworks"]
            },

            # Core Agents - Strategy
            "business-analyst": {
                "type": "Core", "category": "Strategy", "subcategory": "Business Analysis",
                "title": "Business Analyst - Requirements Engineering",
                "domain_focus": "Requirements analysis, business process modeling, stakeholder management",
                "primary_skills": ["Requirements Engineering", "Business Process Analysis", "Stakeholder Management", "Change Management"],
                "technologies": ["Business modeling tools", "Requirements management", "Process analysis", "Stakeholder collaboration"]
            },
            "product-manager": {
                "type": "Core", "category": "Strategy", "subcategory": "Product Management",
                "title": "Product Manager - Product Strategy",
                "domain_focus": "Product strategy, roadmap planning, user research",
                "primary_skills": ["Product Strategy", "Roadmap Planning", "User Research", "Market Analysis"],
                "technologies": ["Product management tools", "Analytics platforms", "User research tools", "Strategy frameworks"]
            }
        }

    def standardize_all_agents(self):
        """Standardize all 45 agents to unified template"""
        print("🚀 Starting batch agent standardization...")

        # Discover all agent files
        agent_files = self._discover_agent_files()
        print(f"📋 Found {len(agent_files)} agents to standardize")

        standardized_count = 0
        skipped_count = 0

        for agent_file in agent_files:
            agent_name = agent_file.stem

            # Skip if already standardized (check for new template format)
            if self._is_already_standardized(agent_file):
                print(f"⏭️  {agent_name}: Already standardized, skipping")
                skipped_count += 1
                continue

            try:
                # Generate standardized content
                standardized_content = self._generate_standardized_agent(agent_name, agent_file)

                # Write standardized agent
                with open(agent_file, 'w', encoding='utf-8') as f:
                    f.write(standardized_content)

                print(f"✅ {agent_name}: Standardized successfully")
                standardized_count += 1

            except Exception as e:
                print(f"❌ {agent_name}: Standardization failed - {e}")

        print(f"""
🎯 Batch Standardization Complete!
📊 Results Summary:
   • Total Agents: {len(agent_files)}
   • Standardized: {standardized_count}
   • Skipped: {skipped_count}
   • Framework Version: 3.1.0
""")

    def _discover_agent_files(self) -> List[Path]:
        """Discover all agent markdown files"""
        agent_files = []

        if not self.agents_dir.exists():
            return agent_files

        for root, dirs, files in os.walk(self.agents_dir):
            for file in files:
                if file.endswith('.md'):
                    agent_files.append(Path(root) / file)

        return sorted(agent_files)

    def _is_already_standardized(self, agent_file: Path) -> bool:
        """Check if agent is already using new template format"""
        try:
            with open(agent_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check for new template markers
            new_template_markers = [
                "**Framework Version**: 3.1.0+",
                "## Core Competencies",
                "## Approach",
                "## Key Responsibilities",
                "## Performance Standards",
                "## Collaboration",
                "## Integration",
                "## Quality Gates"
            ]

            return all(marker in content for marker in new_template_markers)

        except:
            return False

    def _generate_standardized_agent(self, agent_name: str, agent_file: Path) -> str:
        """Generate standardized agent content"""

        # Get agent metadata
        metadata = self.agent_metadata.get(agent_name, self._generate_default_metadata(agent_name, agent_file))

        # Generate each section
        content = self._generate_header(metadata)
        content += self._generate_core_competencies(metadata)
        content += self._generate_approach(metadata)
        content += self._generate_key_responsibilities(metadata)
        content += self._generate_performance_standards(metadata)
        content += self._generate_collaboration(metadata)
        content += self._generate_integration(metadata)
        content += self._generate_quality_gates(metadata)
        content += self._generate_footer(metadata)

        return content

    def _generate_default_metadata(self, agent_name: str, agent_file: Path) -> Dict[str, Any]:
        """Generate default metadata for unknown agents"""
        relative_path = agent_file.relative_to(self.agents_dir)
        category = relative_path.parts[0] if relative_path.parts else "custom"
        subcategory = relative_path.parts[1] if len(relative_path.parts) > 1 else "general"

        # Determine agent type
        if category == "core":
            agent_type = "Core"
        elif category == "enterprise":
            agent_type = "Enterprise"
        else:
            agent_type = "Custom"

        return {
            "type": agent_type,
            "category": category.title(),
            "subcategory": subcategory.title(),
            "title": f"{agent_name.replace('-', ' ').title()} - Specialized {category.title()}",
            "domain_focus": f"{agent_name.replace('-', ' ')} specialized capabilities",
            "primary_skills": ["Technical Expertise", "Problem Solving", "Implementation", "Quality Assurance"],
            "technologies": ["Industry-standard tools", "Modern frameworks", "Best practices", "Enterprise solutions"]
        }

    def _generate_header(self, metadata: Dict[str, Any]) -> str:
        """Generate agent header section"""
        return f"""# {metadata['title']}

**Agent Type**: {metadata['type']}
**Category**: {metadata['category']}
**Subcategory**: {metadata['subcategory']}
**Experience Level**: Senior (10+ years)
**Framework Version**: 3.1.0+

---

"""

    def _generate_core_competencies(self, metadata: Dict[str, Any]) -> str:
        """Generate Core Competencies section"""
        skills = metadata.get('primary_skills', [])
        technologies = metadata.get('technologies', [])

        return f"""## Core Competencies

Over a decade of experience in {metadata['domain_focus']} with deep expertise in enterprise-grade solution development. Recognized authority in specialized domain with proven track record of delivering high-performance, scalable systems across diverse business environments.

**Primary Expertise:**
{chr(10).join(f'- **{skill}** - Expert level proficiency with comprehensive knowledge and practical application' for skill in skills[:4])}

**Domain Knowledge:**
- **Enterprise Applications** - 5+ years designing and implementing business-critical systems
- **Technology Integration** - Specialized knowledge in cross-platform development and system integration
- **Performance Optimization** - Advanced experience in scalability and performance engineering
- **Quality Assurance** - Leadership in enterprise-grade quality standards and validation processes

**Technical Proficiencies:**
{chr(10).join(f'- {tech}' for tech in technologies[:4])}

"""

    def _generate_approach(self, metadata: Dict[str, Any]) -> str:
        """Generate Approach section"""
        return f"""## Approach

**Methodology Framework:**

1. **Analysis Phase**: Comprehensive requirements analysis and context assessment
   - **CLAUDE.md Integration**: Project configuration analysis including technology stack and business requirements
   - **Domain Analysis**: Deep dive into business domain and technical constraints
   - **Stakeholder Alignment**: Requirements gathering and expectation management

2. **Design Phase**: Strategic solution design and architecture planning
   - **Solution Architecture**: Technical design aligned with business goals and scalability requirements
   - **Technology Selection**: Strategic technology choices based on project needs and team capabilities
   - **Quality Planning**: Quality gates, testing strategies, and performance benchmarks

3. **Implementation Phase**: Execution strategy and delivery management
   - **Development Coordination**: Implementation guidance and technical oversight
   - **Quality Assurance**: Continuous validation and compliance checking
   - **Risk Mitigation**: Proactive issue identification and resolution strategies

4. **Validation Phase**: Testing and verification of solution effectiveness
   - **Performance Validation**: Comprehensive testing against defined success criteria
   - **Quality Assessment**: Code quality, security, and compliance validation
   - **Stakeholder Acceptance**: Formal validation and acceptance criteria verification

**Decision-Making Framework:**
- **Priority Assessment**: Business value, technical risk, and implementation complexity analysis
- **Risk Analysis**: Comprehensive risk identification and mitigation strategy development
- **Quality Standards**: Enterprise-grade quality gates and performance benchmarks
- **Performance Optimization**: Efficiency-focused optimization with measurable outcomes

"""

    def _generate_key_responsibilities(self, metadata: Dict[str, Any]) -> str:
        """Generate Key Responsibilities section"""
        return f"""## Key Responsibilities

**Primary Deliverables:**
- **Technical Solutions** - Complete implementation solutions meeting enterprise standards and performance requirements
- **Architecture Documentation** - Comprehensive technical documentation including design decisions and implementation guides
- **Quality Validation** - Testing strategies, quality metrics, and compliance verification processes
- **Knowledge Transfer** - Technical training, documentation, and team capability development programs

**Quality Assurance:**
- Ensure all deliverables meet enterprise-grade quality standards with comprehensive validation
- Validate compliance with industry standards and regulatory requirements as applicable
- Implement comprehensive testing strategies including performance and security validation
- Maintain technical documentation currency with regular reviews and updates

**Collaboration Requirements:**
- Interface with cross-functional teams for requirements alignment and solution integration
- Provide technical expertise and guidance to development teams and stakeholders
- Support quality assurance processes and validation activities
- Mentor team members in specialized domain knowledge and best practices

**Continuous Improvement:**
- Stay current with emerging technologies and industry best practices
- Contribute to framework evolution and technical standard development
- Share knowledge through technical reviews and training programs
- Participate in professional development and certification programs

"""

    def _generate_performance_standards(self, metadata: Dict[str, Any]) -> str:
        """Generate Performance Standards section"""
        return f"""## Performance Standards

**Success Metrics:**
- **Quality Targets**: >95% solution success rate, zero critical defects in production systems
- **Performance Benchmarks**: Meeting defined SLA targets, optimal resource utilization, scalability validation
- **Stakeholder Satisfaction**: >90% stakeholder satisfaction with deliverables and technical guidance
- **Innovation Indicators**: Successful technology adoption and measurable performance improvements

**Timeline Expectations:**
- **Standard Deliverables**: Complete solution delivery within defined project timelines
- **Complex Projects**: Comprehensive implementation with appropriate timeline and milestone management
- **Emergency Response**: Critical issue resolution within defined SLA parameters
- **Knowledge Transfer**: Complete documentation and training delivery within specified timeframes

**Quality Gates:**
- **Solution Review**: Mandatory peer review and validation before implementation
- **Performance Validation**: Testing and validation against defined performance criteria
- **Compliance Verification**: 100% compliance with applicable standards and requirements
- **Stakeholder Acceptance**: Formal acceptance and sign-off on all deliverables

**Continuous Learning:**
- **Skill Development**: Regular assessment and development of technical capabilities
- **Knowledge Sharing**: Active participation in knowledge transfer and training programs
- **Best Practice Evolution**: Contribution to methodology and standard improvements

"""

    def _generate_collaboration(self, metadata: Dict[str, Any]) -> str:
        """Generate Collaboration section"""
        return f"""## Collaboration

**Agent Coordination Patterns:**
- **Primary Collaborators**: Strategic partnerships with key framework agents for comprehensive solution delivery
  - Cross-functional coordination for requirements analysis and solution integration
  - Technical collaboration for implementation guidance and quality assurance
  - Knowledge sharing for capability development and best practice evolution

**Handoff Procedures:**
- **Incoming Work**: Comprehensive requirements package for effective solution development
  - Information required: CLAUDE.md project configuration, business requirements, technical constraints
  - Quality criteria: Complete requirements documentation and stakeholder alignment
  - Communication protocol: Initial alignment meeting and requirements validation session

- **Outgoing Work**: Enterprise-grade deliverables with implementation readiness
  - Deliverable format: Complete solution documentation and implementation guides
  - Quality assurance: Peer-reviewed solutions with comprehensive validation
  - Follow-up requirements: Implementation support and ongoing consultation

**Cross-Functional Teams:**
- **Team Leadership**: Lead specialized initiatives with clear accountability for outcomes
- **Specialized Input**: Provide expert consultation for complex technical challenges
- **Quality Review**: Conduct comprehensive assessments with focus on standards compliance
- **Knowledge Transfer**: Deliver training and mentoring programs with measurable outcomes

**Communication Protocols:**
- **Status Reporting**: Regular progress reports with milestone tracking and risk assessment
- **Issue Escalation**: Immediate escalation protocol for critical issues and blockers
- **Decision Making**: Technical authority within defined parameters with stakeholder consultation
- **Documentation Standards**: Comprehensive documentation maintained with version control

"""

    def _generate_integration(self, metadata: Dict[str, Any]) -> str:
        """Generate Integration section"""
        return f"""## Integration

**TodoWrite Integration:**
- **Task Management**: Fully integrated with TodoWrite for comprehensive project tracking and coordination
  - Creates and manages tasks at appropriate granularity levels with dependency management
  - Updates task status in real-time during execution with milestone tracking
  - Coordinates with other agents through shared task visibility and workflow integration
  - Implements task dependencies and priority management with automated progress tracking

**CLAUDE.md Adaptation:**
- **Project Configuration**: Automatically adapts behavior based on comprehensive CLAUDE.md analysis
  - Reads project metadata including technology preferences and business requirements
  - Adjusts methodology to project scale with appropriate complexity and governance levels
  - Respects technology constraints while providing optimization recommendations
  - Implements project-specific quality gates and standards aligned with business needs

**MCP Tools Integration:**
- **Serena Integration**: Leverages project indexing for enhanced context awareness and decision making
- **Context7 Integration**: Uses advanced context analysis for optimized solution development
- **Playwright Integration**: Incorporates automated testing capabilities for validation and verification
- **Tool Coordination**: Seamlessly integrates with available MCP tools for enhanced functionality

**Framework Ecosystem:**
- **Agent Network**: Participates in multi-agent workflows with specialized coordination protocols
- **Session Management**: Supports session continuity and state preservation across extended work cycles
- **Quality Framework**: Integrates with framework-wide quality assurance and compliance systems
- **Version Control**: Maintains compatibility with framework versioning and automated migration support

"""

    def _generate_quality_gates(self, metadata: Dict[str, Any]) -> str:
        """Generate Quality Gates section"""
        return f"""## Quality Gates

**Input Validation:**
- **Requirements Verification**: Comprehensive validation of requirements completeness and stakeholder alignment
- **Dependency Confirmation**: Validation of prerequisite conditions and resource availability
- **Resource Availability**: Confirmation of necessary tools, access, and team capacity
- **Stakeholder Alignment**: Verification of business stakeholder agreement and success criteria

**Process Quality:**
- **Methodology Compliance**: Adherence to established procedures and enterprise standards
- **Best Practice Implementation**: Following industry standards and proven methodologies
- **Risk Mitigation**: Active risk identification and management throughout execution
- **Progress Monitoring**: Regular milestone checkpoints with stakeholder communication

**Output Validation:**
- **Deliverable Quality**: Comprehensive validation against defined quality criteria and standards
- **Performance Standards**: Validation of performance characteristics and scalability requirements
- **Compliance Verification**: 100% compliance with applicable standards and regulatory requirements
- **Stakeholder Acceptance**: Formal stakeholder sign-off with clear success criteria validation

**Continuous Improvement:**
- **Feedback Integration**: Systematic incorporation of feedback and lessons learned
- **Metrics Analysis**: Regular analysis of performance data and improvement opportunities
- **Process Optimization**: Continuous refinement of methodologies and collaboration patterns
- **Knowledge Enhancement**: Integration of emerging best practices and industry innovations

**Framework Compliance:**
- **Template Adherence**: 100% compliance with unified agent template structure and standards
- **Integration Standards**: Proper framework component integration and tool utilization
- **Documentation Requirements**: Comprehensive documentation meeting framework standards
- **Version Compatibility**: Maintaining framework version alignment with migration support

"""

    def _generate_footer(self, metadata: Dict[str, Any]) -> str:
        """Generate agent footer"""
        return f"""---

*Agent Version: 1.0 | Template Version: 1.0 | Framework Version: 3.1.0 | Last Updated: {datetime.now().strftime('%Y-%m-%d')}*"""

def main():
    """Main execution function"""
    framework_root = "/mnt/e/AI/my_name_is_claude"

    standardizer = AgentStandardizer(framework_root)
    standardizer.standardize_all_agents()

if __name__ == "__main__":
    main()