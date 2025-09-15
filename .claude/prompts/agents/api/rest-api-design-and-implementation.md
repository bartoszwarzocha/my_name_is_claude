**🤖 AGENT ACTIVATION:** This prompt automatically activates the `api-engineer` agent.
**📋 AGENT CONTEXT:** The activated agent will read CLAUDE.md and adapt to project requirements.
**🔄 TODO INTEGRATION:** All tasks will be managed through the agent's TodoWrite workflow.

# REST API Design and Implementation Excellence

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Design and implement scalable, secure REST APIs that serve as the backbone for applications and external integrations. Create robust API architecture following RESTful principles, industry standards, and framework-specific best practices. Ensure comprehensive API documentation, security implementation, performance optimization, and seamless integration capabilities while adapting to detected technology stack and project requirements.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: API Requirements Analysis and Architecture Planning
1. **Analyze business domain and functional requirements** - Extract business entities, workflows, and integration needs from architecture specifications
2. **Assess performance and scalability requirements** - Define load expectations, response time targets, and throughput requirements
3. **Evaluate security and compliance requirements** - Determine authentication, authorization, and regulatory compliance needs
4. **Identify integration patterns** - Plan external system integrations, frontend coordination, and microservice architecture
5. **Select appropriate architectural patterns** - Choose between monolithic, microservices, or serverless approaches based on project scale

### Phase 2: RESTful API Contract Design and Resource Modeling
1. **Design resource-oriented API structure** - Model business entities as API resources with proper URL hierarchies and relationships
2. **Define comprehensive HTTP method mappings** - Implement standard CRUD operations with appropriate HTTP verbs and status codes
3. **Create consistent request and response schemas** - Design JSON structures with validation rules and error handling patterns
4. **Plan API versioning and backward compatibility** - Establish versioning strategy and migration paths for API evolution
5. **Design pagination, filtering, and search capabilities** - Implement efficient data retrieval patterns with proper query parameters

### Phase 3: Technology-Adaptive Implementation Strategy
1. **Detect and adapt to project technology stack** - Analyze CLAUDE.md configuration for backend framework, database, and integration requirements
2. **Apply framework-specific architectural patterns** - Implement appropriate design patterns based on detected technology (MVC, Clean Architecture, etc.)
3. **Implement data access and persistence layer** - Design repository patterns, ORM integration, and database optimization strategies
4. **Create comprehensive validation and error handling** - Implement input validation, business rule enforcement, and standardized error responses
5. **Integrate security and authentication mechanisms** - Implement authentication, authorization, and security controls appropriate for project requirements

### Phase 4: API Quality, Documentation, and Integration Excellence
1. **Generate comprehensive API documentation** - Create OpenAPI/Swagger specifications with interactive documentation and testing capabilities
2. **Implement monitoring and observability** - Add logging, metrics collection, health checks, and distributed tracing for production readiness
3. **Create automated testing suite** - Develop unit tests, integration tests, contract tests, and performance tests for continuous quality assurance
4. **Validate API security and compliance** - Conduct security testing, vulnerability assessments, and compliance validation based on project requirements
5. **Establish deployment and maintenance procedures** - Create deployment pipelines, monitoring dashboards, and maintenance workflows for production operations

## 3. ✅ VALIDATION CRITERIA

### API Design and Architecture Excellence
- **RESTful compliance validated** - API follows REST principles with proper resource modeling, HTTP method usage, and status codes
- **Comprehensive documentation generated** - OpenAPI/Swagger documentation with complete endpoint coverage, examples, and interactive testing
- **Security implementation validated** - Authentication, authorization, input validation, and security controls implemented according to project requirements
- **Performance benchmarks achieved** - Response times, throughput, and scalability requirements met with load testing validation

### Technology Integration and Adaptation Success
- **Framework-specific patterns implemented** - Architecture follows best practices for detected technology stack (Node.js, Python, Java, etc.)
- **Database integration optimized** - Data access patterns, query optimization, and ORM integration aligned with performance requirements
- **Error handling standardized** - Consistent error responses, logging, and monitoring across all API endpoints
- **Integration capabilities validated** - Frontend integration, external service communication, and microservice coordination tested and documented

### Production Readiness and Operational Excellence
- **Automated testing coverage achieved** - Unit tests (>80%), integration tests, contract tests, and performance tests implemented
- **Monitoring and observability implemented** - Logging, metrics, health checks, and distributed tracing configured for production operations
- **Documentation and maintenance procedures established** - API documentation, deployment procedures, and operational runbooks created
- **Compliance and security validation completed** - Security testing, vulnerability assessment, and regulatory compliance validation performed

## 4. 📋 USAGE EXAMPLES

### Enterprise E-commerce API Development
**Context:** Large-scale e-commerce platform requiring comprehensive product, order, and customer management APIs
**Approach:** Design microservices-based API architecture with product catalog service, order processing service, and customer management service
**Key Features:** Advanced search and filtering, real-time inventory updates, payment processing integration, and multi-tenant architecture
**Technology Adaptation:** Implement using detected stack (Node.js/Express, Python/FastAPI, or Java/Spring Boot) with appropriate database patterns

### FinTech API Security and Compliance
**Context:** Financial services API requiring strict security, audit trails, and regulatory compliance
**Approach:** Implement zero-trust security architecture with comprehensive authentication, authorization, and audit logging
**Key Features:** Multi-factor authentication, encryption at rest and in transit, comprehensive audit trails, and regulatory compliance validation
**Technology Adaptation:** Apply security patterns appropriate for detected technology stack with industry-specific compliance requirements

### Healthcare API Integration and Interoperability
**Context:** Healthcare system APIs requiring FHIR compliance, patient data protection, and clinical workflow integration
**Approach:** Design HIPAA-compliant APIs with secure patient data handling, clinical decision support integration, and interoperability standards
**Key Features:** HL7 FHIR compliance, patient consent management, clinical workflow integration, and medical device interoperability
**Technology Adaptation:** Implement healthcare-specific patterns using detected technology stack with appropriate security and compliance measures

### SaaS Platform API Development
**Context:** Multi-tenant SaaS platform requiring scalable APIs for subscription management, user administration, and feature access control
**Approach:** Design multi-tenant architecture with tenant isolation, feature flagging, and subscription-based access control
**Key Features:** Multi-tenant data isolation, subscription management, usage analytics, and developer portal with API documentation
**Technology Adaptation:** Apply SaaS patterns using detected technology stack with appropriate scalability and tenant management strategies

### IoT and Real-time Data API Implementation
**Context:** IoT platform requiring high-throughput data ingestion, real-time processing, and device management APIs
**Approach:** Design event-driven architecture with real-time data streaming, device management, and analytics capabilities
**Key Features:** High-throughput data ingestion, real-time analytics, device management, and scalable event processing
**Technology Adaptation:** Implement real-time patterns using detected technology stack with appropriate streaming and analytics technologies