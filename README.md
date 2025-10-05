# My Name Is Claude - Multi-Agent Framework

[![Version](https://img.shields.io/badge/Version-3.8.0-FF6B35?style=flat-square&logo=tag&logoColor=white)](CHANGELOG.md) [![Claude Code](https://img.shields.io/badge/Claude%20Code-Framework-FF6B35?style=flat-square&logo=anthropic&logoColor=white)](https://docs.anthropic.com/en/docs/claude-code) [![Fortune 500 Ready](https://img.shields.io/badge/Fortune%20500-Ready-00aa00?style=flat-square&logo=enterprise&logoColor=white)](#) [![Cost Optimized](https://img.shields.io/badge/Cost-50%25%20Savings-00aa00?style=flat-square&logo=dollar&logoColor=white)](#) [![MIT License](https://img.shields.io/badge/License-MIT-00aaff?style=flat-square)](https://opensource.org/licenses/MIT)

## Enterprise-Grade Multi-Agent Development Framework

Enterprise-grade development framework featuring **intelligent cost optimization** (50% API savings), **context-aware communication styles**, **advanced checkpoint architecture**, **parallel agent execution**, **background task management**, real-time monitoring, quality assurance systems, AI-powered agent selection, and comprehensive multi-agent coordination for Fortune 500 software development.

**Current Version:** 3.8.0 | **Release Date:** October 5, 2025

---

## 📚 Documentation

**📖 [Complete Documentation](docs/README.md)** - Start here for full framework guide

**Quick Links:**
- **⚡ [Quick Start](docs/getting-started/first-steps.md)** - 20-minute guided introduction
- **🛠️ [Installation](docs/getting-started/framework-installation.md)** - Complete setup instructions
- **🧠 [AI Agent Selection](docs/reference/ai-agent-selection.md)** - AI-powered features

---

## 🚀 Key Features

### 🤖 Specialized Agent System
- **45 Specialized Agents** with unified enterprise template standard
- **100/100 Quality Score** validated by automated assessment systems
- **Complete Agent Standardization** across all core, enterprise, and custom agents
- **Automatic Agent Activation** via directory-based prompt binding
- **Multi-Agent Coordination** through TodoWrite workflow integration

### 🧠 AI-Powered Agent Selection
- **Intelligent Project Analysis** across comprehensive technology stack (languages, frameworks, databases, cloud, AI/ML, and more)
- **Automated Agent Recommendations** with confidence scoring
- **Dynamic Workflow Generation** based on project context
- **50% Setup Time Reduction** through automation

### 🏢 Enterprise Capabilities
- **Fortune 500 Ready** with enterprise-scale deployment
- **Real-Time Monitoring System** - Prometheus + Grafana + AlertManager stack
- **Quality Assurance Framework** - Automated validation and compliance checking
- **Executive & Operations Dashboards** - Multi-stakeholder analytics and KPIs
- **Technology-Agnostic Design** adaptable to any development stack
- **Advanced Visualization Systems** - Architecture diagrams and workflow visualization

### 🧠 Intelligent Workflow Generation
- **AI-Powered Workflow Intelligence** with project analysis and template matching
- **Agent Selection Optimization** with capability matrix and coordination patterns
- **Phase-Based Development Guides** with quality gates and milestone tracking
- **Technology Stack Adaptation** for MERN, MEAN, React-Python, and custom stacks

### 🧙 Interactive Framework Setup Wizard
- **Zero-Configuration Project Setup** with professional 7-phase automation
- **AI-Enhanced Technology Detection** with ML-powered project analysis
- **Automated CLAUDE.md Generation** with project-specific configuration
- **Integrated Workflow Generation** with business impact predictions during setup

### 📋 Advanced Workflow Management
- **Session Management** with state recovery and context preservation
- **TodoWrite Integration** for hierarchical task management
- **MCP Tools Support** (Serena, Context7, Playwright)
- **Quality Gates Integration** with enterprise-grade validation
- **Framework Glossary** - Interactive terminology system with 50+ key terms
- **Template Validation Engine** - Automated compliance checking and reporting

### 🔄 Background Task Management (NEW in v3.5.0)
- **Non-Blocking Task Execution** with process isolation and intelligent scheduling
- **Multi-Channel Notifications** - Console, desktop, file, and email alerts
- **Comprehensive Analysis Engines** - Security scanning, performance profiling, code quality analysis
- **Auto-Triggering System** - File watching, git hooks, scheduled tasks
- **Smart Task Scheduling** - Priority-based queue with adaptive learning
- **Enterprise Reliability** - State persistence, crash recovery, resource monitoring

### 💰 Intelligent Model Configuration (NEW in v3.6.0)
- **AI-Powered Model Selection** - Automatic Opus/Sonnet/Haiku selection based on agent type and task complexity
- **Real-Time Cost Tracking** - Multi-dimensional tracking (agent, project, session, model, date)
- **Budget Management** - Daily/weekly/monthly budgets with configurable alert thresholds
- **Auto-Downgrade System** - Automatic model optimization when approaching budget limits
- **Advanced Analytics** - Real-time dashboards, ROI analysis, usage patterns, and optimization recommendations
- **50% Cost Reduction** - Intelligent model usage achieving significant API cost savings

---

## 🏗️ Project Structure

```text
my_name_is_claude/
├── .claude/                  # Framework core
│   ├── agents/                 # Agent definitions (45 agents)
│   │   ├── core/               # Core development agents
│   │   ├── enterprise/         # Enterprise operation agents
│   │   └── custom/             # Specialized technology agents
│   ├── prompts/              # Comprehensive prompt library
│   │   ├── agents/             # Agent-specific prompts
│   │   ├── workflows/          # Multi-agent orchestration
│   │   ├── init/               # Project initialization
│   │   └── tools/              # Framework automation tools
│   ├── commands/             # Slash commands system (28 specialized commands)
│   ├── config/               # Advanced configuration systems (v3.5.0)
│   │   ├── model-profiles.json      # Cost optimization profiles
│   │   ├── agent-model-mapping.json # Agent-to-model mappings
│   │   ├── cost-optimization.json   # Budget and optimization
│   │   ├── output-styles.json       # Communication styles
│   │   ├── checkpoint-system.json   # State management architecture
│   │   ├── parallel-agents.json     # Parallel execution framework
│   │   ├── background-tasks.json    # Background task management (v3.5.0)
│   │   └── INFO.md                  # Configuration guide pointer
│   ├── checkpoints/          # Checkpoint storage (gitignored)
│   ├── monitoring/           # Enterprise monitoring & analytics systems
│   │   ├── dashboards/         # Grafana dashboards (Executive, Operations, Quality)
│   │   ├── quality/            # Quality assessment and validation systems
│   │   ├── metrics/            # Metrics collection and monitoring
│   │   └── scripts/            # Monitoring setup and automation
│   ├── docs/                 # Framework documentation and glossary
│   ├── hooks/                  # Automation and event hooks
│   ├── templates/              # Configuration templates (unified agent standard)
│   └── assets/                 # Visual diagrams and assets
├── .ai-tools/                # AI-Powered Development Tools
│   ├── core/                   # AI agent selection and recommendations
│   ├── background/             # Background task management system (v3.5.0)
│   │   ├── core/               # Task execution, queue, notifications, analysis
│   │   └── background_task_manager.py  # Main orchestrator
│   ├── models/                 # ML models for recommendations
│   ├── integration/            # Framework integration
│   ├── data/                   # Training data and patterns
│   └── demo/                   # Demonstrations and examples
├── docs/                     # Comprehensive framework documentation
│   ├── getting-started/        # Installation and quick start guides
│   ├── ai-tools/               # AI tools step-by-step guides
│   ├── workflows/              # Development workflows
│   ├── advanced/               # Advanced configuration
│   ├── reference/              # Technical reference documentation
│   ├── examples/               # Real-world implementation examples
│   └── architecture/           # System architecture and design
├── project_archive/          # Project documents and research
│   ├── designs/                # Technical design documents
│   ├── implementations/        # Implementation summaries
│   ├── research/               # Research notes and sessions
│   └── roadmaps/               # Development roadmap archives
├── CLAUDE.md                 # Framework specification
├── CLAUDE_template.md        # Project template
├── FRAMEWORK_ROADMAP.md      # Development roadmap
├── CHANGELOG.md              # Version history and updates
├── mcp-tools.sh              # MCP tools setup automation
└── ai-tools.sh               # AI-powered development tools launcher
```

---

## 🚀 Quick Start

**🧙 New Projects**: Use the Interactive Framework Setup Wizard:
```bash
.ai-tools/setup/framework_wizard.sh
```
*Zero-configuration setup with AI-powered project analysis and automated workflow generation.*

**📚 Alternative Setup**:
1. **Documentation First**: Read [Complete Documentation](docs/README.md)
2. **Installation**: Follow [Installation Guide](docs/getting-started/framework-installation.md)
3. **Quick Start**: Try [First Steps Guide](docs/getting-started/first-steps.md)
4. **AI Features**: Explore [AI Agent Selection](docs/reference/ai-agent-selection.md)
5. **MCP Tools**: Setup [MCP Tools Manager](docs/reference/mcp-tools-usage.md) for advanced AI tools

For existing projects: Copy `CLAUDE_template.md` to your project as `CLAUDE.md` and customize.

---

## 🤝 Contributing

Contributions welcome! Please read our development guidelines in the [Advanced Configuration](docs/advanced/) and follow the standards defined in [CLAUDE.md](CLAUDE.md).

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

**Commercial Use:** Fully supported for enterprise applications
**Modification:** Encouraged with attribution
**Distribution:** Freely distributable

---

**Transform your development workflow with intelligent multi-agent coordination and AI-powered automation.**