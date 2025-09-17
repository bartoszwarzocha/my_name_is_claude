# CLAUDE.md – Python Application

## Project Metadata
- **project_name**: "{{PROJECT_NAME}}"
- **project_description**: "{{PROJECT_DESCRIPTION}}"
- **project_version**: "1.0.0"
- **primary_language**: "python"
- **business_domain**: "{{BUSINESS_DOMAIN}}"
- **project_scale**: "{{PROJECT_SCALE}}"
- **development_stage**: "development"

## Project Overview
Modern Python application with clean architecture, comprehensive testing, and production-ready deployment. Features modular design, robust error handling, and scalable architecture patterns.

**Core Capabilities**: Python 3.9+, clean architecture, dependency injection, comprehensive testing, API development, database integration, async/await support, production deployment.

**Goals**: Maintainable codebase, high test coverage, scalable architecture, robust error handling, efficient development workflow, production stability.

## Technologies
**Frontend**: Optional web interface (Jinja2 templates, React/Vue integration)
**Backend**: Python 3.9+, FastAPI/Django/Flask, Pydantic, SQLAlchemy/Django ORM, Alembic
**Database**: PostgreSQL/MySQL (primary), Redis (caching), SQLite (development/testing)
**Testing**: pytest, unittest, coverage.py, factory_boy, httpx (async testing), Faker
**Deployment**: Docker, Docker Compose, Poetry/pip-tools, CI/CD pipelines, monitoring

## Agents and Roles
**Strategy**: product-manager, business-analyst
**Architecture**: software-architect, ux-designer
**Development**: backend-engineer, api-engineer, data-engineer
**Quality**: qa-engineer, security-engineer
**Operations**: deployment-engineer

## Integrations
**APIs**: External service integration, third-party APIs, microservices communication
**Development**: Git workflow, virtual environments, dependency management, CI/CD pipelines
**Monitoring**: Logging (structlog), metrics collection, error tracking, health checks

## Requirements
**Performance**: <200ms API response times, efficient database queries, async processing for I/O
**Security**: Input validation, SQL injection prevention, authentication/authorization, secure headers
**Scalability**: Horizontal scaling support, stateless design, caching strategies

## Framework Guidelines
**Constraints**: PEP 8 compliance, type hints, clean architecture principles, comprehensive testing
**Style**: Modular design, dependency injection, clear separation of concerns, documented code
**Testing**: Unit tests, integration tests, API tests, test-driven development approach

## TODO Management
**Core**: Feature-based task organization with TodoWrite integration
**Levels**: Epic (product-manager) → Feature (backend-engineer) → Module (detailed implementation) → Testing (qa-engineer)
**Templates**:
- **Startup**: Simple hierarchy, session tracking
- **SME**: Full hierarchy, milestone tracking
- **Enterprise**: Complete system + external integration

## Project Ownership
**Team**: Backend development team with Python expertise
**Interface**: Modern Python development with FastAPI/Django and comprehensive testing
**Governance**: Code review, performance monitoring, security audits, database optimization

## Command-Agent Mapping
**Core Commands**: Session (save/restore/start), Project (health check/new/release), Business (analysis/requirements), Product (planning/MVP), Development (frontend/backend/API), Quality (tests/security), Architecture (design/deployment)
**Rules**: Polish/English support, context awareness, CLAUDE.md adaptation, TodoWrite integration

---

*This configuration enables AI agents to automatically adapt their competencies to your Python project requirements. All agents read this file to understand project context, technology stack, and business domain for optimal assistance.*