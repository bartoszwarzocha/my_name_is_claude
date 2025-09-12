# Agent Usage Guide

## 🎯 When to Use Which Agent

### Starting a New Feature

1. **business-analyst** - Analyze requirements and stakeholder needs
2. **product-manager** - Define feature scope and success metrics
3. **ux-designer** - Create user flows and wireframes
4. **reviewer** - Validate requirements completeness

### Architecture & Design Phase

1. **software-architect** - Design system architecture and patterns
2. **ux-designer** - Create design system and prototypes  
3. **security-engineer** - Review security implications
4. **data-engineer** - Design data models and storage

### Development Phase

**Frontend Development:**
- **frontend-engineer** - UI implementation, responsive design
- **ux-designer** - Design validation and user testing
- **qa-engineer** - Frontend testing and accessibility

**Backend Development:**
- **api-engineer** - API design and microservices
- **data-engineer** - Database implementation and optimization
- **security-engineer** - Security controls and authentication
- **qa-engineer** - API testing and integration testing

### Quality & Deployment

1. **qa-engineer** - Comprehensive testing and quality validation
2. **security-engineer** - Security testing and vulnerability assessment
3. **deployment-engineer** - Infrastructure setup and CI/CD
4. **reviewer** - Final validation and sign-off

### Ongoing Operations

- **deployment-engineer** - Monitoring, scaling, incident response
- **security-engineer** - Security monitoring and compliance
- **qa-engineer** - Production quality monitoring
- **product-manager** - Success metrics and user feedback analysis

## 🚀 Agent Collaboration Patterns

### Parallel Work Opportunities

**Phase 2: Architecture & Design**
- Run `software-architect`, `ux-designer`, and `security-engineer` in parallel
- Each focuses on their domain while coordinating on interfaces

**Phase 3: Development**  
- Run `frontend-engineer`, `api-engineer`, `data-engineer` in parallel
- Use `qa-engineer` for continuous testing across all areas
- Engage `security-engineer` for security implementation

**Phase 5: Monitoring**
- All agents monitor their respective areas simultaneously
- Coordinate findings for comprehensive improvement plans

### Sequential Dependencies

1. **business-analyst** → **product-manager** (requirements → strategy)
2. **product-manager** → **ux-designer** (strategy → user research)
3. **software-architect** + **data-engineer** (architecture coordination)
4. **ux-designer** → **frontend-engineer** (design → implementation)
5. **api-engineer** → **frontend-engineer** (API → UI integration)

## 💡 Best Practices

### Multi-Agent Sessions

When running multiple agents:
1. Start with clear context and objectives
2. Use the `reviewer` agent to coordinate between specialists
3. Ensure each agent has access to current CLAUDE.md
4. Document decisions that affect other agents

### Single Agent Focus

For deep work in one area:
1. Use specialized agents for their expertise domains
2. Leverage their domain-specific knowledge and patterns
3. Ask for cross-functional impact analysis
4. Validate with `reviewer` before major changes

### Context Management

- Always provide current project context
- Reference relevant sections of CLAUDE.md
- Share decisions made by other agents
- Maintain consistency across agent interactions

## 🔄 Workflow Integration

Follow the 5-phase workflow in `.claude/docs/agent-sdlc-workflow.puml`:

1. **Discovery & Analysis** - Foundation setting
2. **Architecture & Design** - Technical and UX planning  
3. **Development & QA** - Implementation with continuous quality
4. **Deployment & Operations** - Production readiness
5. **Monitoring & Improvement** - Continuous optimization

Each phase has clear entry/exit criteria and quality gates managed by the `reviewer` agent.

## 📊 Success Metrics

Track agent effectiveness through:
- **Requirement Coverage** - All requirements addressed
- **Quality Gates** - All validation checkpoints passed
- **Delivery Speed** - Efficient parallel execution
- **Technical Quality** - Code, security, and performance standards met
- **User Satisfaction** - UX and business goals achieved