# My Name Is Claude
## Claude Code Multi Agent Project Template

A comprehensive workspace template for Claude Code projects, optimized for efficient multi-agent collaboration and parallel work.

Inspired by: [Claude AI](https://claude.ai), [Serena](https://serena.ai), [Context7](https://context7.ai), https://github.com/coleam00/context-engineering-intro.git and https://github.com/lausena/my_awesome_crm.git

## 📋 Project Description

This repository contains a ready-to-use set of configuration files and templates that can be used as a starting point for new Claude Code projects. The main goal is to provide an efficient and organized workspace that maximizes the potential of multi-agent mode and parallel work.

## 🎯 Main Goals

- **Efficiency**: Maximizing productivity when working with Claude Code
- **Organization**: Well-structured workspace with clear agent roles
- **Scalability**: Easy adaptation to projects of different sizes
- **Standardization**: Consistent approach to project management
- **Flexibility**: Support for projects across different domains and technologies

## 🏗️ Project Structure

```text
my_claude/
├── .claude/                           # Claude Code configuration
│   └── agents/                        # Agent definitions
│       ├── architecture/              # Software architect
│       ├── api/                       # API engineer
│       ├── backend/                   # Backend engineer (legacy)
│       ├── business/                  # Business analyst
│       ├── data/                      # Data engineer
│       ├── deployment/                # Deployment engineer
│       ├── design/                    # UX/UI designer
│       ├── frontend/                  # Frontend engineer
│       ├── planner/                   # Product manager and reviewer
│       ├── quality/                   # QA engineer
│       └── security/                  # Security engineer
├── CLAUDE.md                          # Main project configuration file
├── DATABASE_CONNECTIONS.md            # Standard database connection configurations
├── DATABASE_CONNECTIONS_TEMPLATE.md   # Database connections template
└── README.md                          # This file
```

## 🤖 Available Agents

### 📋 Core Strategy and Planning

#### **Product Manager**
- **Role**: Product strategy and requirements
- **Competencies**: Market analysis, UX research, roadmaps, stakeholder management
- **Focus**: Business value and user-centric solutions

#### **Business Analyst**
- **Role**: Requirements analysis and process optimization
- **Competencies**: Stakeholder management, process modeling, requirements documentation
- **Focus**: Business process excellence and stakeholder alignment

#### **Reviewer**
- **Role**: Quality assurance and validation
- **Competencies**: Requirements validation, risk analysis, compliance verification
- **Focus**: Completeness, quality, and business alignment

### 🏗️ Architecture and Design

#### **Software Architect**
- **Role**: System architecture design
- **Competencies**: Scalable solutions, architectural patterns, technology selection
- **Focus**: Long-term maintainability, performance, and scalability

#### **UX/UI Designer**
- **Role**: User experience and interface design
- **Competencies**: User research, design systems, accessibility, prototyping
- **Focus**: User-centered design and inclusive experiences

### 💻 Development

#### **Frontend Engineer**
- **Role**: User interface development
- **Competencies**: Modern frameworks, responsive design, performance optimization
- **Focus**: User experience, accessibility, and technical excellence

#### **API Engineer**
- **Role**: API and microservices development
- **Competencies**: RESTful APIs, GraphQL, microservices, service integration
- **Focus**: API excellence, service reliability, and integration quality

#### **Data Engineer**
- **Role**: Data architecture and analytics
- **Competencies**: Database design, ETL pipelines, data processing, business intelligence
- **Focus**: Data reliability, performance optimization, and analytics

### 🔒 Quality and Security

#### **QA Engineer**
- **Role**: Quality assurance and test automation
- **Competencies**: Test automation, performance testing, quality processes
- **Focus**: Quality-first development and continuous improvement

#### **Security Engineer**
- **Role**: Application security and compliance
- **Competencies**: Security architecture, threat modeling, compliance frameworks
- **Focus**: Security-first development and regulatory compliance

### 🚀 Operations

#### **Deployment Engineer**
- **Role**: DevOps and infrastructure management
- **Competencies**: CI/CD, cloud infrastructure, monitoring, automation
- **Focus**: Zero-downtime deployments and enterprise reliability

## 🛠️ Features

### ⚡ Parallel Work

- Optimized for executing multiple tasks simultaneously
- Clear role division between agents
- Minimized conflicts and work duplication

### 🔄 Multi-Agent Mode

- Each agent has specialized competencies
- Ability to run agents concurrently
- Efficient inter-agent communication

### 🌐 Universal Support

- Adaptable to different business domains
- Technology stack flexibility
- Easy adaptation to various projects

### 🗃️ Database Management

- Predefined connection configurations
- Support for different environments (WSL, Docker, cloud)
- Standard connection patterns

## 🚀 Getting Started

### 1. Copy Template

```bash
# Copy the entire folder as a base for a new project
cp -r my_claude/ my_new_project/
cd my_new_project/
```

### 2. Customize CLAUDE.md

Edit the `CLAUDE.md` file to match your project:

- Fill in the technology sections
- Define project goals
- Add specific requirements

### 3. Configure Database Connections

If using databases, customize `DATABASE_CONNECTIONS.md`

### 4. Start Working with Claude Code

```bash
# Launch Claude Code in the project directory
claude-code
```

## 📝 Example Usage Scenarios

### New Web Project

1. Product Manager defines requirements and roadmap
2. Architect designs system structure
3. Backend Engineer implements APIs
4. Frontend Engineer creates interfaces
5. Deployment Engineer configures CI/CD
6. Reviewer validates everything

### Data Migration

1. Architect analyzes existing systems
2. Backend Engineer prepares migration scripts
3. Deployment Engineer plans deployment
4. Everything happens in parallel using multiple agents

## ⚙️ Advanced Configuration

### Agent Customization

Each agent can be customized by editing files in the `.claude/agents/` directory

### CI/CD System Integration

- GitHub Actions
- GitLab CI
- Azure DevOps
- Jenkins

### Support for Different Technologies

The template is flexible and can be adapted to:

- React/Vue/Angular (Frontend)
- Node.js/Python/Java (Backend)
- AWS/Azure/GCP (Cloud)
- Docker/Kubernetes (Containerization)

## 🤝 Best Practices

### Work Organization

- Use todo lists to track progress
- Run agents in parallel when possible
- Regularly validate progress with Reviewer

### Code Management

- Use version control (Git)
- Regular commits with descriptive messages
- Code review before merging

### Documentation

- Update CLAUDE.md as the project evolves
- Document architectural decisions
- Keep README up to date

## 🔧 Troubleshooting

### Database Connection Issues

Check the `DATABASE_CONNECTIONS_TEMPLATE.md` file for ready solutions

### Agent Conflicts

Use Reviewer to validate and resolve conflicts

### Performance Issues

Make sure to run tasks in parallel where possible

## 📚 Additional Resources

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Agent Guide](/.claude/agents/)
- [Project Templates](./templates/)

## 🤝 Contributing and Development

This template is open to improvements. If you have suggestions:

1. Create an issue describing the problem/suggestion
2. Fork the repository
3. Make changes
4. Create a Pull Request

## 📄 License

MIT License - you can freely use, modify, and distribute this template.

## 🎉 Summary

This template is a starting point for efficient work with Claude Code. It uses modern approaches to project organization, provides clear role division, and maximizes the potential of parallel work with multiple agents.

**Happy coding with Claude Code!** 🚀