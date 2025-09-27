# Health Check Command

**Command**: `/health-check`
**Category**: Project Analysis
**Description**: Szybki kompleksowy health check projektu

## Usage

```
/health-check
/health-check --quick
/health-check --detailed
/health-check --fix-issues
```

## Functionality

Performs comprehensive analysis of project health across multiple dimensions including configuration, dependencies, agent setup, and development environment.

### Analysis Areas

#### 1. Framework Integration
- Framework version compatibility
- Essential files presence (.claude/, .ai-tools/, etc.)
- Configuration completeness (CLAUDE.md)
- Agent availability and configuration

#### 2. Project Configuration
- CLAUDE.md validity and completeness
- Technology stack consistency
- Project metadata accuracy
- Business requirements clarity

#### 3. Development Environment
- Dependencies installation status
- Build system configuration
- Testing framework setup
- Development tools availability

#### 4. Agent Ecosystem
- Agent assignment appropriateness
- Multi-agent coordination setup
- TodoWrite integration status
- Workflow optimization opportunities

#### 5. Quality Standards
- Code quality configuration
- Testing coverage setup
- Security scanning configuration
- Performance monitoring readiness

### Output Format
```
🏥 PROJECT HEALTH CHECK

Project: book_writing_app v1.0.0
Framework: Claude Code Multi-Agent v3.1.0
Timestamp: 2025-09-27 12:30:00

┌─ OVERALL HEALTH: 🟢 HEALTHY (87/100) ──────────────────┐
│                                                         │
│ ✅ Framework Integration    (95%) - Excellent           │
│ ✅ Project Configuration   (90%) - Very Good           │
│ ⚠️  Development Environment (75%) - Good               │
│ ✅ Agent Ecosystem         (92%) - Excellent           │
│ ⚠️  Quality Standards      (70%) - Needs Attention     │
│                                                         │
└─────────────────────────────────────────────────────────┘

🔍 DETAILED ANALYSIS:

Framework Integration ✅
├── ✅ Framework files present and up-to-date
├── ✅ AI Tools configured correctly
├── ✅ Agent definitions loaded (12 agents available)
└── ✅ MCP tools integration ready

Project Configuration ✅
├── ✅ CLAUDE.md properly configured
├── ✅ Technology stack clearly defined (Python, wxPython, SQLite)
├── ✅ Project scale appropriate (SME)
└── ⚠️  Business requirements could be more detailed

Development Environment ⚠️
├── ✅ Python 3.9+ environment active
├── ✅ Virtual environment configured
├── ⚠️  Some dependencies not installed (requirements.txt needed)
└── ❌ Testing framework not configured

Agent Ecosystem ✅
├── ✅ Appropriate agents detected for stack
├── ✅ desktop-specialist activated for wxPython
├── ✅ backend-engineer ready for Python/SQLite
└── ✅ TodoWrite integration operational

Quality Standards ⚠️
├── ❌ Code quality tools not configured
├── ❌ Testing framework missing
├── ⚠️  Security scanning not setup
└── ❌ Performance monitoring not configured

🔧 RECOMMENDED ACTIONS:

High Priority:
1. Setup testing framework (pytest recommended)
2. Create requirements.txt file
3. Configure code quality tools (flake8, black)

Medium Priority:
4. Expand business requirements in CLAUDE.md
5. Setup security scanning tools
6. Configure performance monitoring

💡 OPTIMIZATION OPPORTUNITIES:

• Consider adding ux-designer agent for UI/UX guidance
• Setup automated quality gates with pre-commit hooks
• Implement continuous integration workflow
• Add documentation generation tools
```

## Options

### `--quick`
Performs basic health check focusing on critical issues only

### `--detailed`
Includes comprehensive analysis with performance metrics and optimization suggestions

### `--fix-issues`
Automatically attempts to fix detected issues where possible

### `--json`
Outputs results in JSON format for CI/CD integration

## Integration

- AI Tools validation system
- Agent competency verification
- TodoWrite health monitoring
- MCP tools status checking
- Framework version compatibility