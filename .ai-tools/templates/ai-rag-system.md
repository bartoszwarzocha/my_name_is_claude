# CLAUDE.md – AI RAG System

## Project Metadata
- **project_name**: "{{PROJECT_NAME}}"
- **project_description**: "{{PROJECT_DESCRIPTION}}"
- **project_version**: "1.0.0"
- **primary_language**: "python"
- **business_domain**: "{{BUSINESS_DOMAIN}}"
- **project_scale**: "{{PROJECT_SCALE}}"
- **development_stage**: "development"

## Project Overview
Advanced Retrieval-Augmented Generation (RAG) system built with Python, featuring document ingestion, vector embeddings, semantic search, and LLM integration. Optimized for enterprise-scale knowledge retrieval and AI-powered question answering.

**Core Capabilities**: Document processing and chunking, vector embeddings generation, semantic search, LLM integration, context-aware responses, multi-format document support, real-time indexing, conversation memory, enterprise security.

**Goals**: Accurate knowledge retrieval, contextual AI responses, scalable document processing, enterprise-grade security, production-ready deployment, comprehensive analytics, cost optimization.

## Technologies
**Frontend**: Streamlit/Gradio UI, React dashboard (optional), API documentation interface
**Backend**: Python 3.9+, FastAPI, LangChain/LlamaIndex, OpenAI/Anthropic APIs, Celery workers
**Database**: Vector databases (Chroma, Pinecone, Weaviate), PostgreSQL/MongoDB, Redis cache
**Testing**: pytest, RAG evaluation frameworks, LLM testing, vector search validation
**Deployment**: Docker, Kubernetes, cloud deployment, monitoring, auto-scaling

## Agents and Roles
**Strategy**: product-manager, business-analyst
**Architecture**: software-architect, ux-designer
**Development**: data-engineer, ai-engineer, backend-engineer, api-engineer
**Quality**: qa-engineer, security-engineer
**Operations**: deployment-engineer

## Integrations
**APIs**: LLM APIs (OpenAI, Anthropic, local models), document processing APIs, vector database APIs
**Development**: Git workflow, MLOps pipelines, model versioning, CI/CD for ML systems
**Monitoring**: LLM performance monitoring, vector search analytics, cost tracking, usage metrics

## Requirements
**Performance**: <2s search response time, efficient vector operations, optimized LLM calls
**Security**: Data encryption, API key management, user authentication, content filtering
**Scalability**: Multi-tenant architecture, horizontal scaling, efficient indexing, cost optimization

## Framework Guidelines
**Constraints**: LLM API rate limits, vector database performance, document processing efficiency
**Style**: Modular RAG architecture, clean data pipelines, comprehensive error handling, monitoring
**Testing**: RAG evaluation metrics, LLM response quality tests, vector search accuracy, integration tests

## TODO Management
**Core**: Feature-based task organization with TodoWrite integration
**Levels**: Epic (product-manager) → Feature (ai-engineer) → Component (ingestion/retrieval/generation) → Testing (qa-engineer)
**Templates**:
- **Startup**: Simple hierarchy, session tracking
- **SME**: Full hierarchy, milestone tracking
- **Enterprise**: Complete system + external integration

## Project Ownership
**Team**: AI/ML development team with RAG and LLM expertise
**Interface**: Modern AI system development with comprehensive MLOps and monitoring
**Governance**: Model performance monitoring, cost optimization, security compliance, ethical AI practices

## Command-Agent Mapping
**Core Commands**: Session (save/restore/start), Project (health check/new/release), Business (analysis/requirements), Product (planning/MVP), Development (frontend/backend/API), Quality (tests/security), Architecture (design/deployment)
**Rules**: Polish/English support, context awareness, CLAUDE.md adaptation, TodoWrite integration

---

*This configuration enables AI agents to automatically adapt their competencies to your AI RAG system requirements. All agents read this file to understand project context, technology stack, and business domain for optimal assistance.*