# Concept-to-CLAUDE.md Configuration Generator

## 1. 🎯 FUNCTIONAL REQUIREMENTS

Generate a complete CLAUDE.md configuration file by analyzing project concept materials in the `init_concept` folder. Transform any format of project documentation (business requirements, technical notes, wireframes, code samples, meeting notes) into a properly structured CLAUDE.md following the framework template. Enable zero-configuration project setup by automatically detecting technology stack, business domain, project scale, and agent requirements.

## 2. 🔄 HIGH-LEVEL ALGORITHMS

### Phase 1: Concept Material Analysis
1. **Scan init_concept folder** - Read all files (.md, .txt, .docx, images, code samples, etc.)
2. **Extract project identity** - Identify project name, description, and core value proposition
3. **Analyze business domain** - Determine industry sector (ecommerce, fintech, healthcare, etc.)
4. **Assess project scale** - Evaluate complexity level (startup/MVP, SME, enterprise)
5. **Identify stakeholders** - Extract user types, business sponsors, and success criteria

### Phase 2: Technology Stack Detection
1. **Parse technical mentions** - Detect frameworks, languages, databases from documentation
2. **Analyze code samples** - Examine existing code for technology patterns
3. **Evaluate architecture notes** - Extract deployment, integration, and infrastructure requirements
4. **Identify constraints** - Find technology preferences, limitations, or existing system dependencies
5. **Recommend optimal stack** - Balance detected preferences with business requirements and project scale

### Phase 3: Agent Requirements Mapping
1. **Analyze project complexity** - Determine which agents are needed based on scope and requirements
2. **Map development phases** - Sequence agent involvement based on project timeline and dependencies
3. **Configure TODO management** - Set hierarchical complexity based on project scale and team size
4. **Define quality requirements** - Extract performance, security, scalability needs from concepts
5. **Establish integration needs** - Identify external systems, APIs, and data sources

### Phase 4: CLAUDE.md Generation and Validation
1. **Populate CLAUDE_template.md** - Fill all sections with extracted and derived information
2. **Generate project metadata** - Create complete Section 0 with all required fields
3. **Structure business goals** - Convert business requirements into measurable objectives
4. **Define technology sections** - Populate Sections 3 with detected and recommended technologies
5. **Configure agent selection** - Set Section 4 with optimal agent subset for project needs
6. **Validate completeness** - Ensure all template sections are properly filled
7. **Create backup** - Save original CLAUDE.md as CLAUDE_backup_[timestamp].md before replacement

## 3. ✅ VALIDATION CRITERIA

### Concept Analysis Completeness
- **All concept files processed**: Every file in init_concept folder has been analyzed
- **Business value extracted**: Core business problem and value proposition identified
- **Technology stack detected**: Primary language and supporting technologies determined
- **Project scale assessed**: Appropriate startup/sme/enterprise classification assigned
- **Success criteria defined**: Measurable business outcomes and technical deliverables specified

### CLAUDE.md Template Compliance
- **All metadata populated**: Section 0 completely filled with project-specific information
- **Business goals measurable**: Section 2 contains 3-5 specific, achievable objectives
- **Technology stack coherent**: Section 3 technologies work together and support business goals
- **Agent selection optimal**: Section 4 agents chosen specifically for project needs
- **Quality standards appropriate**: Non-functional requirements match project scale and domain

### Configuration Accuracy and Feasibility
- **Domain expertise alignment**: Selected technologies appropriate for business domain
- **Scale-complexity match**: Project scale aligns with described complexity and resource requirements
- **Timeline feasibility**: Technology choices support realistic development timelines
- **Integration viability**: External system integrations are technically feasible
- **Agent workflow optimization**: Selected agents enable effective coordination and handoffs

## 4. 📚 USAGE EXAMPLES

### E-commerce Startup Concept
**Input Files**:
- `project_idea.md`: "Mobile-first marketplace for handmade goods"
- `tech_preferences.md`: "React Native, Node.js, Stripe payments"
- `requirements.txt`: "MVP in 8 weeks, 100-500 users initially"

**Generated Configuration**:
- project_scale: "startup", primary_language: "typescript"
- business_domain: "ecommerce", agents: product-manager, frontend-engineer, api-engineer, security-engineer
- technologies: React Native, Node.js, Express, PostgreSQL, Stripe API, AWS

### Healthcare Enterprise Integration
**Input Files**:
- `legacy_system_docs.pdf`: "Existing patient management system in Java/Spring"
- `compliance_requirements.md`: "HIPAA compliance, audit trails, encryption"
- `integration_needs.txt`: "Connect with hospital management system via HL7"

**Generated Configuration**:
- project_scale: "enterprise", primary_language: "java"
- business_domain: "healthcare", agents: business-analyst, software-architect, security-engineer, qa-engineer
- technologies: Spring Boot, PostgreSQL, Docker, Kubernetes, OAuth2, HL7 FHIR

### Process Automation SME Project
**Input Files**:
- `current_process.md`: "Manual invoice processing taking 2 hours per invoice"
- `automation_goals.txt`: "Reduce to 5 minutes, integrate with accounting software"
- `technical_constraints.md`: "Python preferred, existing QuickBooks integration"

**Generated Configuration**:
- project_scale: "sme", primary_language: "python"
- business_domain: "business_process_automation", agents: business-analyst, backend-engineer, data-engineer
- technologies: FastAPI, pandas, PostgreSQL, QuickBooks API, Docker

### Educational Platform Concept
**Input Files**:
- `wireframes/`: UI mockups showing course interface
- `business_model.md`: "Coding bootcamp online learning platform"
- `feature_list.txt`: "Video streaming, progress tracking, interactive coding exercises"

**Generated Configuration**:
- project_scale: "sme", primary_language: "typescript"
- business_domain: "education", agents: ux-designer, frontend-engineer, backend-engineer, qa-engineer
- technologies: Next.js, PostgreSQL, Prisma, video streaming API, WebRTC

### Fintech Regulatory Platform
**Input Files**:
- `regulatory_requirements.pdf`: "Investment firm reporting requirements"
- `existing_infrastructure.md`: "Oracle database, Java ecosystem, high security"
- `compliance_checklist.txt`: "SOX, SEC reporting, real-time risk monitoring"

**Generated Configuration**:
- project_scale: "enterprise", primary_language: "java"
- business_domain: "financial_services", agents: business-analyst, software-architect, security-engineer, qa-engineer, deployment-engineer
- technologies: Spring Boot, Oracle, Apache Kafka, HashiCorp Vault, Jenkins, Kubernetes

---

## 🎯 EXECUTION APPROACH

**Workflow Process**:
1. **Analyze init_concept folder** - Process all concept files and extract business/technical information
2. **Apply technology detection algorithms** - Identify optimal technology stack based on requirements
3. **Generate agent recommendations** - Select optimal agent subset for project needs
4. **Create complete CLAUDE.md** - Fill CLAUDE_template.md with all extracted and derived information
5. **Validate and backup** - Ensure completeness and save original CLAUDE.md before replacement

**Output Deliverables**:
- **Complete CLAUDE.md file** - Ready-to-use configuration following framework template
- **Configuration rationale** - Explanation of key decisions and technology choices
- **Agent workflow recommendations** - Suggested sequence and coordination patterns
- **Next steps guidance** - Instructions for using prepare_instruction.md prompt

**Integration Points**:
- **CLAUDE_template.md** - Source template for configuration structure
- **init_concept folder** - Input source for all project concept materials
- **prepare_instruction.md** - Next prompt for generating development strategy