# {project_name}

{project_description}

## 🏗️ Architecture

This project uses the **Claude Code Agent Framework** with 14 specialized agents organized in 5 development phases.

### 🤖 Agent Structure

**Phase 1: Business Discovery & Analysis**
- `business-analyst` - Requirements analysis and stakeholder management
- `product-manager` - Product strategy and feature prioritization  
- `ux-designer` - User research and experience design
- `reviewer` - Quality validation and risk assessment

**Phase 2: Architecture & UX Design**  
- `software-architect` - System architecture and technology selection
- `ux-designer` - Design systems and prototyping
- `security-engineer` - Security architecture and threat modeling
- `data-engineer` - Data architecture and analytics design

**Phase 3: Development & Continuous QA**
- `frontend-engineer` - User interface implementation
- `backend-engineer` - Server-side systems and performance
- `api-engineer` - API development and microservices
- `data-engineer` - Database and ETL implementation  
- `security-engineer` - Security controls implementation
- `qa-engineer` - Test automation and quality assurance

**Phase 4: Deployment & Operations**
- `deployment-engineer` - Infrastructure and CI/CD
- `security-engineer` - Production security hardening
- `qa-engineer` - Production readiness testing

**Phase 5: Monitoring & Continuous Improvement**
- All agents monitor their respective areas for optimization

## 🚀 Quick Start

### Prerequisites
- {language} {version_requirement}
- {additional_requirements}

### Development Setup

1. **Clone the repository**
   ```bash
   git clone {repository_url}
   cd {project_name}
   ```

2. **Install dependencies**
   ```bash
   {install_command}
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Initialize Serena (for AI development)**
   ```bash
   serena onboarding
   ```

5. **Run the application**
   ```bash
   {run_command}
   ```

## 📋 Project Configuration

The project configuration is managed in `CLAUDE.md` which defines:
- Business domains and project goals
- Technology stack and architecture decisions
- Agent roles and responsibilities
- Non-functional requirements
- Special guidelines and constraints

## 🧪 Testing

{testing_instructions}

## 🚀 Deployment

{deployment_instructions}

## 🤝 Contributing

This project follows the Agent-Driven Development Lifecycle:

1. **Business Analysis** - Use `business-analyst` for requirement gathering
2. **Architecture Design** - Use `software-architect` for system design
3. **Development** - Use specialized development agents
4. **Quality Assurance** - Use `qa-engineer` for testing
5. **Deployment** - Use `deployment-engineer` for infrastructure

See `.claude/docs/agent-sdlc-workflow.puml` for detailed workflow.

## 📚 Documentation

- `CLAUDE.md` - Project configuration and agent guidance
- `.claude/agents/` - Individual agent specifications  
- `.claude/docs/` - Workflow diagrams and documentation
- `{docs_directory}` - Additional project documentation

## 🛠️ Technology Stack

- **Frontend**: {frontend_tech}
- **Backend**: {backend_tech}
- **Database**: {database_tech}
- **Infrastructure**: {infrastructure_tech}

## 📄 License

{license_info}

---

**Built with Claude Code Agent Framework** 🚀