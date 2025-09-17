# CLAUDE.md – Node.js API

## Project Metadata
- **project_name**: "{{PROJECT_NAME}}"
- **project_description**: "{{PROJECT_DESCRIPTION}}"
- **project_version**: "1.0.0"
- **primary_language**: "typescript"
- **business_domain**: "{{BUSINESS_DOMAIN}}"
- **project_scale**: "{{PROJECT_SCALE}}"
- **development_stage**: "development"

## Project Overview
Modern Node.js API with TypeScript, featuring RESTful architecture, comprehensive validation, and production-ready deployment. Optimized for performance, scalability, and maintainability.

**Core Capabilities**: Express.js/Fastify framework, TypeScript integration, database ORM, authentication/authorization, API documentation, comprehensive testing, monitoring and logging.

**Goals**: High-performance API, scalable architecture, comprehensive error handling, security best practices, efficient development workflow, production stability.

## Technologies
**Frontend**: API documentation (Swagger/OpenAPI), optional admin interface
**Backend**: Node.js 18+, TypeScript, Express.js/Fastify, Prisma/TypeORM/Sequelize, Helmet
**Database**: PostgreSQL/MySQL (primary), MongoDB (document store), Redis (caching/sessions)
**Testing**: Jest, Supertest, ts-jest, Faker.js, Test containers, MSW (mocking)
**Deployment**: Docker, PM2, ESLint, Prettier, Husky, CI/CD pipelines

## Agents and Roles
**Strategy**: product-manager, business-analyst
**Architecture**: software-architect, ux-designer
**Development**: backend-engineer, api-engineer, data-engineer
**Quality**: qa-engineer, security-engineer
**Operations**: deployment-engineer

## Integrations
**APIs**: External service integration, microservices communication, third-party APIs
**Development**: Git workflow, npm/yarn package management, CI/CD pipelines
**Monitoring**: APM tools, logging aggregation, metrics collection, error tracking

## Requirements
**Performance**: <100ms API response times, connection pooling, caching strategies, async processing
**Security**: Input validation, SQL injection prevention, CORS, rate limiting, secure headers
**Scalability**: Stateless design, horizontal scaling, load balancing, rate limiting

## Framework Guidelines
**Constraints**: TypeScript strict mode, Express.js best practices, RESTful API design, comprehensive testing
**Style**: Modular architecture, middleware patterns, clean separation of concerns, documented endpoints
**Testing**: Unit tests, integration tests, API endpoint tests, test-driven development

## TODO Management
**Core**: Feature-based task organization with TodoWrite integration
**Levels**: Epic (product-manager) → Feature (api-engineer) → Endpoint (detailed implementation) → Testing (qa-engineer)
**Templates**:
- **Startup**: Simple hierarchy, session tracking
- **SME**: Full hierarchy, milestone tracking
- **Enterprise**: Complete system + external integration

## Project Ownership
**Team**: API development team with Node.js and TypeScript expertise
**Interface**: Modern Node.js API development with comprehensive testing and monitoring
**Governance**: Code review, API versioning, performance monitoring, security audits

## Command-Agent Mapping
**Core Commands**: Session (save/restore/start), Project (health check/new/release), Business (analysis/requirements), Product (planning/MVP), Development (frontend/backend/API), Quality (tests/security), Architecture (design/deployment)
**Rules**: Polish/English support, context awareness, CLAUDE.md adaptation, TodoWrite integration

---

*This configuration enables AI agents to automatically adapt their competencies to your Node.js API project requirements. All agents read this file to understand project context, technology stack, and business domain for optimal assistance.*