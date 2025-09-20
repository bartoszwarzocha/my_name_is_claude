# Backend Service Architecture Design and Implementation

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Design and implement scalable, maintainable backend service architectures adapted to project requirements defined in CLAUDE.md. Create comprehensive backend systems that support business logic, data persistence, external integrations, and operational requirements while ensuring performance, security, and maintainability across different technology stacks and business domains.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Architecture Design and Service Implementation
**Objective**: Analyze requirements and implement comprehensive service architecture with patterns

1. **Architecture Analysis and Technology Stack Discovery**
   - Analyze CLAUDE.md project configuration to extract backend technologies, business domain, and scalability requirements
   - Assess existing backend structure and identify service boundaries for microservices, monolith, or hybrid architecture
   - Evaluate performance and integration requirements including external APIs, databases, and third-party dependencies

2. **Service Architecture Design and Pattern Selection**
   - Define service architecture patterns (layered, hexagonal, microservices, event-driven) based on requirements
   - Design data access patterns with repository or domain-driven design for data management
   - Create API layer architecture with REST, GraphQL, or RPC interfaces and implement business logic organization

### Phase 2: Technology Integration and Quality Implementation
**Objective**: Implement technology-specific patterns and ensure performance, security, and quality

1. **Technology-Specific Implementation and Integration**
   - Implement technology-specific patterns applying framework conventions (Spring Boot, Express.js, FastAPI, ASP.NET)
   - Configure dependency injection with service containers and integrate data persistence layer with ORM/ODM
   - Implement external service integration with HTTP clients, message queues, and configure operational concerns

2. **Performance, Security, and Quality Implementation**
   - Implement performance optimizations with caching strategies, connection pooling, and resource management
   - Apply security patterns with authentication, authorization, input validation, and data protection measures
   - Create comprehensive testing strategies and configure monitoring with observability for architecture compliance validation

## 3. ✅ VALIDATION CRITERIA

### Backend Service Architecture Excellence
**Design and Technology Compatibility**: Confirmed technology stack adaptation to CLAUDE.md specifications, appropriately defined service boundaries with clear separation, addressed performance requirements supporting expected throughput, implemented integration patterns with proper error handling

**Implementation Quality**: Code organization following established patterns with clear layer separation, properly configured dependency injection with testable components, comprehensive error handling with consistent management, adequate testing coverage with service reliability

### Operational Readiness and Production
**Operational Excellence**: Functional health checks with dependency monitoring, operational performance monitoring with resource utilization tracking, passed security validation with authentication flows, ready deployment configuration with environment setup

**Scalability and Documentation**: Verified scalability patterns handling expected load with appropriate strategies, complete documentation covering service APIs and integration patterns

## 4. 📚 USAGE EXAMPLES

**Cross-Domain Service Architecture Examples**

**Microservices E-commerce**: Domain-driven microservices with API gateway and service discovery, database-per-service with event sourcing, Spring Boot with JPA/Hibernate and Kafka messaging

**Fintech Regulatory Compliance**: Layered architecture with strict audit logging and compliance validation, multi-factor authentication with encryption, .NET Core with Entity Framework and Azure Service Bus

**Healthcare HIPAA-Compliant**: Modular monolith with PHI data segregation and audit trails, HIPAA-compliant encryption with consent management, Python FastAPI with PostgreSQL encryption

**IoT Data Processing**: Event-driven architecture with stream processing and device management, time-series databases with real-time analytics, Node.js with MongoDB and Apache Kafka

**Enterprise SaaS Multi-Tenant**: Multi-tenant microservices with tenant isolation and shared services, tenant-per-database with row-level security, Java Spring Boot with PostgreSQL multi-tenancy

---

## 🎯 EXECUTION APPROACH

**Project-Adaptive Strategy**: CLAUDE.md configuration prioritization → business domain expertise application → technology stack optimization → scalability requirement fulfillment

**Quality-Focused Implementation**: Security-first design with domain-appropriate patterns, performance optimization integration with caching and resource management, testing strategy early adoption with dependency injection, operational readiness emphasis

**Cross-Functional Integration**: Frontend coordination with efficient API design, data engineering collaboration with analytics support, security engineering alignment with application architecture, deployment engineering preparation for containerization and monitoring