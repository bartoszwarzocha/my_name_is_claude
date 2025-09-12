# CLAUDE.md – Project Description Template for Claude Code

## 0. Project Metadata

- **project_name**: [project name, e.g., "task-manager-app"]
- **project_description**: [brief description, e.g., "Web application supporting team task management"]
- **primary_language**: [main language: csharp, python, rust, java, typescript, go, cpp, ruby]
- **business_domain**: [domain: ecommerce, fintech, healthcare, saas, enterprise, iot, etc.]
- **project_scale**: [scale: startup, sme, enterprise]
- **development_stage**: [stage: concept, mvp, development, production, maintenance]

## 1. Project Description

[Fill in the general project description, e.g., "Web application supporting team task management."]

---

## 2. Domains and Goals

- Business domains: [e.g., project management, team communication, data analysis]
- Main project goals: [e.g., improve collaboration, process automation, reporting]

---

## 3. Technologies

- **Frontend – technologies and tools:** [fill in, e.g., React, Vue, TypeScript]
- **Backend – technologies and tools:** [fill in, e.g., Python, Node.js, FastAPI]
- **Deployment – infrastructure and tools:** [fill in, e.g., Docker, Kubernetes, AWS]
- **Database:** [e.g., PostgreSQL, MySQL, MongoDB]
- **Other:** [e.g., deployment automation, external service integrations]

---

## 4. Agents and Roles

The list of available agents and their competency scope is defined in files:

### Core Strategy and Planning

- **product-manager** - Product strategy, requirements gathering, stakeholder management
- **business-analyst** - Business process analysis, requirements documentation, stakeholder communication
- **reviewer** - Quality assurance, requirements validation, risk assessment

### Architecture and Design

- **software-architect** - System architecture, technology selection, scalability planning
- **ux-designer** - User experience design, design systems, accessibility, user research

### Development

- **frontend-engineer** - User interface development, responsive design, performance optimization
- **api-engineer** - API design, microservices, service integration, distributed systems
- **data-engineer** - Data architecture, ETL pipelines, analytics, database optimization

### Quality and Security

- **qa-engineer** - Test automation, quality processes, performance testing, continuous improvement
- **security-engineer** - Application security, threat modeling, compliance, security architecture

### Operations

- **deployment-engineer** - DevOps, CI/CD pipelines, infrastructure automation, monitoring

Each agent's competency scope is located in the corresponding file in the `.claude/agents` directory. If you want to add a new agent or modify a role, edit the appropriate agent file.

---

## 5. Integrations and Dependencies

- External APIs: [e.g., integration with external services]
- Services: [e.g., notification systems, authorization]
- Other dependencies: [e.g., libraries, supporting tools]

---

## 6. Non-functional Requirements

- Performance: [e.g., fast application operation]
- Security: [e.g., user data protection]
- Scalability: [e.g., system expansion capability]
- Availability: [e.g., high service availability]

---

## 7. Special Notes

- Technological constraints: [e.g., preferred open-source solutions]
- Coding style preferences: [e.g., readability, standards compliance]
- Special guidelines for agents: [e.g., communication language preferences]

---

## 8. Contact and Project Owners

- Main contact: [e.g., email, Slack, Teams]
- Business/technical owners: [e.g., name and surname, role]

---

## 9. Change History

- Creation date: [e.g., 2025-09-11]
- Major updates: [e.g., added new agents, changed requirements]

---

*Fill in the above sections according to project requirements. Claude Code agents will automatically adapt their competencies based on this file.*
