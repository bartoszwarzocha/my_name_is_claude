# Epic Breakdown Orchestration and Hierarchical Task Management

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Transform high-level business initiatives into structured development work through systematic Epic→Feature→Task→Subtask decomposition with integrated TodoWrite management. Ensure complete requirement coverage, appropriate sizing, clear ownership assignments, dependency identification, and real-time progress tracking across all framework agents while maintaining quality gates and stakeholder alignment.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Epic Analysis and Business Context Establishment
1. **Conduct comprehensive business analysis** - Analyze epic requirements, stakeholder needs, success criteria, and business impact assessment
2. **Establish product strategy alignment** - Ensure epic alignment with product roadmap, user research data, and business objectives
3. **Design user experience mapping** - Define user experience requirements, interaction patterns, and accessibility considerations
4. **Implement epic validation and approval** - Validate epic scope with stakeholders and obtain formal approval for decomposition
5. **Create TodoWrite Epic-level tracking** - Initialize hierarchical TODO management with Epic-level tasks and agent assignments

### Phase 2: Technical Architecture Planning and Assessment
1. **Analyze system architecture impact** - Evaluate how epic requirements affect existing system architecture and component design
2. **Conduct security architecture review** - Assess security implications, compliance requirements, and threat modeling updates
3. **Plan data architecture changes** - Design database modifications, data flow changes, and analytics implementation requirements
4. **Create Feature-level TODO breakdown** - Decompose Epic into Features with TodoWrite tracking and agent coordination
5. **Establish technical specification framework** - Define technical boundaries, integration requirements, and API contracts

### Phase 3: Feature Decomposition and Specification Development
1. **Identify and scope individual features** - Break down Epic into discrete Features with clear boundaries and success criteria
2. **Create technical specifications per feature** - Define API contracts, database requirements, and integration specifications
3. **Develop UX specifications for each feature** - Create wireframes, user flows, and interaction design specifications
4. **Establish feature dependency mapping** - Identify inter-feature dependencies and critical path requirements
5. **Initialize Task-level TodoWrite tracking** - Create Task-level TODO hierarchy with technical component breakdown

### Phase 4: Task Breakdown, Assignment, and Coordination Setup
1. **Create development task breakdown** - Generate implementation tasks for api-engineer, frontend-engineer, and data-engineer
2. **Design quality and security task structure** - Define testing, security validation, and quality assurance tasks
3. **Plan infrastructure and deployment tasks** - Create deployment, monitoring, and operational readiness tasks
4. **Assign tasks with capacity consideration** - Allocate tasks based on agent expertise, capacity, and project timeline constraints
5. **Establish Subtask-level coordination** - Initialize detailed implementation tracking with dependencies and progress monitoring

## 3. ✅ VALIDATION CRITERIA

### Epic Decomposition Completeness and Quality
- **Complete requirement coverage achieved**: All epic requirements traced through to specific implementation tasks
- **Appropriate task sizing validated**: Epic→Feature→Task→Subtask hierarchy follows framework sizing guidelines and agent capacity
- **Clear ownership assignments established**: Every task level has designated agent ownership with accountability and success criteria
- **Comprehensive dependency mapping complete**: All inter-task dependencies identified with critical path analysis and blocking risk assessment
- **TodoWrite integration functional**: Hierarchical TODO management operational across all agents with real-time progress tracking

### Technical Architecture and Quality Planning Success
- **Architecture impact analysis thorough**: System changes properly analyzed with component modification plans and integration requirements
- **Security and compliance requirements addressed**: Security architecture review complete with threat modeling and compliance validation
- **Data architecture changes planned**: Database modifications, analytics requirements, and data flow changes properly specified
- **Quality gates defined at all levels**: Testing, validation, and acceptance criteria established for Epic, Feature, Task, and Subtask levels
- **Technical specifications complete**: API contracts, database schemas, and integration requirements fully documented

### Coordination and Execution Readiness Verification
- **Agent coordination protocols established**: Clear handoff procedures, communication patterns, and collaboration workflows defined
- **Resource allocation optimized**: Task assignments balance agent capacity, expertise, and project timeline requirements
- **Progress tracking mechanisms operational**: Real-time visibility into task completion, blocking issues, and milestone achievement
- **Stakeholder alignment maintained**: Epic decomposition maintains business value alignment with regular validation checkpoints
- **Execution readiness confirmed**: All necessary specifications, dependencies, and resources available for implementation commencement

## 4. 📚 USAGE EXAMPLES

### Enterprise SaaS Platform User Authentication Overhaul
**Epic Context**: Complete authentication system modernization with OAuth2, multi-factor authentication, and enhanced security
**Breakdown Approach**:
- Epic Level: "User Authentication System Overhaul" with business-analyst leading stakeholder requirements and success criteria
- Feature Level: OAuth2 Implementation, Multi-Factor Authentication, User Profile Management, Session Management, Authentication Analytics
- Task Level: OAuth2 Authorization Server Setup, JWT Token Management, MFA Integration, UI Component Development, Database Schema Updates
- Subtask Level: Specific implementation tasks distributed across api-engineer (authentication endpoints), frontend-engineer (login UI), data-engineer (user schema), security-engineer (security configuration)

### E-commerce Platform Mobile Payment Integration
**Epic Context**: Mobile payment system with Apple Pay, Google Pay, and cryptocurrency support for enhanced checkout experience
**Breakdown Approach**:
- Epic Level: "Mobile Payment Integration Platform" with product-manager driving user experience requirements and business case
- Feature Level: Apple Pay Integration, Google Pay Support, Cryptocurrency Payment Gateway, Payment Security Enhancement, Mobile Checkout Optimization
- Task Level: Payment SDK integration, mobile UI components, payment validation services, fraud detection implementation
- Subtask Level: Platform-specific implementations with frontend-engineer (mobile payment UI), api-engineer (payment processing), security-engineer (fraud detection)

### Financial Services Regulatory Compliance Update
**Epic Context**: PCI DSS 4.0 compliance implementation with audit trail expansion and automated reporting
**Breakdown Approach**:
- Epic Level: "PCI DSS 4.0 Compliance Implementation" with security-engineer leading regulatory analysis and compliance planning
- Feature Level: Enhanced Data Encryption, Audit Trail Expansion, Access Control Updates, Automated Compliance Reporting, Security Monitoring Enhancement
- Task Level: Encryption algorithm updates, audit logging system design, role-based access control implementation, compliance dashboard development
- Subtask Level: Specific compliance tasks with security-engineer (encryption), data-engineer (audit logs), frontend-engineer (compliance dashboard)

### Open Source Library API Version Migration
**Epic Context**: Breaking API changes for version 3.0 with backwards compatibility tools and community migration support
**Breakdown Approach**:
- Epic Level: "API v3.0 Migration with Community Support" with product-manager coordinating community impact and migration strategy
- Feature Level: New API Design, Legacy Compatibility Layer, Migration Tooling, Documentation Overhaul, Community Communication
- Task Level: API contract definition, compatibility shim development, automated migration scripts, comprehensive documentation updates
- Subtask Level: Implementation distributed across api-engineer (new API), qa-engineer (migration testing), reviewer (documentation validation)

### Healthcare Application HIPAA Compliance Enhancement
**Epic Context**: Enhanced patient data protection with advanced encryption, access logging, and compliance automation
**Breakdown Approach**:
- Epic Level: "HIPAA Compliance Enhancement Initiative" with security-engineer and business-analyst coordinating regulatory requirements
- Feature Level: Advanced Patient Data Encryption, Comprehensive Access Logging, Automated Compliance Monitoring, Staff Training System, Audit Preparation Tools
- Task Level: Encryption key management, access control implementation, compliance dashboard design, training content development
- Subtask Level: Security implementations with security-engineer (encryption), data-engineer (access logs), frontend-engineer (compliance UI)

---

## 🎯 EXECUTION APPROACH

**Systematic Epic Breakdown Methodology**:
1. **Business-value driven decomposition** - Start with business requirements and user value to ensure technical work aligns with objectives
2. **Progressive refinement strategy** - Begin with high-level Epic scope, then progressively refine into Features, Tasks, and Subtasks
3. **Agent expertise utilization** - Assign breakdown responsibilities based on agent competencies and domain knowledge
4. **Dependency-aware planning** - Identify and plan for dependencies early to minimize blocking issues during execution

**TodoWrite Integration Strategy**:
- **Hierarchical TODO creation** - Use TodoWrite at every level (Epic→Feature→Task→Subtask) with appropriate agent ownership
- **Progressive status tracking** - Track progress through pending→in_progress→completed status transitions with meaningful activeForm descriptions
- **Cross-agent coordination** - Use TODO status updates to coordinate handoffs between agents and maintain execution visibility
- **Quality gate integration** - Incorporate validation checkpoints into TODO workflows to ensure quality throughout decomposition

**Quality Assurance and Risk Management**:
- **Sizing validation** - Ensure Epic, Feature, Task, and Subtask sizing follows framework guidelines for agent capacity and delivery timelines
- **Completeness verification** - Validate that decomposition covers all Epic requirements without gaps or overlaps
- **Dependency risk mitigation** - Identify critical dependencies early and plan mitigation strategies for potential blocking issues
- **Stakeholder alignment maintenance** - Regular validation checkpoints ensure decomposition maintains business value alignment throughout process