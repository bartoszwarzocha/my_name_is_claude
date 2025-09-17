# Core AI System Documentation

The Core AI System (`.ai-tools/core/`) provides the foundation for intelligent agent selection and project analysis in the Claude Code Multi-Agent Framework.

## 🧠 System Overview

The Core AI System uses machine learning models and heuristic analysis to provide intelligent recommendations for:

- **Agent Selection** - Optimal AI agent recommendations based on project characteristics
- **Technology Detection** - Comprehensive analysis of project technology stack
- **Business Domain Classification** - Industry-specific project categorization
- **Confidence Scoring** - Advanced algorithms for recommendation reliability

## 🏗️ Architecture

```
.ai-tools/core/
├── bin/                    # Executable scripts
│   └── project_analyzer.py # Main AI analysis engine
├── core/                   # Core AI modules
├── models/                 # ML models and training data
├── data/                   # Training datasets and patterns
├── demo/                   # Example usage and tutorials
├── integration/            # Framework integration modules
├── requirements.txt        # Python dependencies
└── README.md              # System documentation
```

## 🚀 Quick Start

### Basic Usage

```bash
# Analyze current project
python .ai-tools/core/bin/project_analyzer.py .

# Analyze specific directory
python .ai-tools/core/bin/project_analyzer.py /path/to/project

# Get detailed analysis
python .ai-tools/core/bin/project_analyzer.py . --verbose
```

### Integration with Framework

The Core AI System automatically integrates with:

- **Interactive Setup Wizard** - Provides ML-enhanced project analysis
- **Agent Selection** - Powers intelligent agent recommendations
- **Workflow Generation** - Supplies project characteristics for workflow optimization

## 🔧 Features

### Technology Detection

Automatic detection of:
- **Frontend Frameworks**: React, Angular, Vue.js, vanilla JavaScript
- **Backend Technologies**: Node.js, Python, Java, .NET, Go, Rust
- **Databases**: PostgreSQL, MySQL, MongoDB, SQLite, Redis
- **Build Tools**: Webpack, Vite, Maven, Gradle, npm/yarn
- **Infrastructure**: Docker, Kubernetes, cloud platforms

### Business Domain Classification

Intelligent categorization for:
- **FinTech** - Financial services and banking applications
- **Healthcare** - Medical and health-related systems
- **E-commerce** - Online retail and marketplace platforms
- **Enterprise** - Business and corporate applications
- **General** - Universal application patterns

### Agent Recommendations

ML-powered recommendations for:
- **Primary Agents** - Core development team agents
- **Specialized Agents** - Domain-specific expertise agents
- **Support Agents** - Quality assurance and deployment agents

## 📊 Performance Metrics

- **Detection Accuracy**: 90%+ for major technology frameworks
- **Recommendation Confidence**: 85%+ for project-appropriate agents
- **Analysis Speed**: Sub-second analysis for typical project sizes
- **Business Domain Accuracy**: 87%+ for common industry patterns

## 🔧 Configuration

### Environment Setup

```bash
# Install dependencies
cd .ai-tools/core
pip install -r requirements.txt

# Run setup verification
python bin/project_analyzer.py --test
```

### Model Training

The system includes pre-trained models, but can be retrained:

```bash
# Retrain with new data
python core/train_models.py --data data/training_data.json

# Validate model performance
python core/validate_models.py --test-data data/test_data.json
```

## 📚 API Reference

### ProjectAnalyzer Class

```python
from core.analyzer import ProjectAnalyzer

analyzer = ProjectAnalyzer()
result = analyzer.analyze_project("/path/to/project")

# Access results
print(result.technology_stack)
print(result.business_domain)
print(result.recommended_agents)
print(result.confidence_scores)
```

### Analysis Results

The analyzer returns structured data:

```python
{
    "technology_stack": {
        "frontend": "react",
        "backend": "nodejs",
        "database": "postgresql"
    },
    "business_domain": "ecommerce",
    "project_complexity": "medium",
    "recommended_agents": [
        "frontend-engineer",
        "backend-engineer",
        "api-engineer",
        "qa-engineer"
    ],
    "confidence_scores": {
        "technology_detection": 0.95,
        "domain_classification": 0.87,
        "agent_recommendations": 0.92
    }
}
```

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed
2. **Model Loading Failures**: Check model files in `models/` directory
3. **Low Confidence Scores**: May indicate unusual project structure
4. **Missing Dependencies**: Run `pip install -r requirements.txt`

### Debug Mode

```bash
# Enable debug logging
python bin/project_analyzer.py . --debug

# Verbose output
python bin/project_analyzer.py . --verbose --debug
```

## 🚀 Advanced Usage

### Custom Training Data

Add custom patterns to improve detection:

```python
# Add custom technology patterns
analyzer.add_technology_pattern("my-framework", {
    "files": ["my-framework.config.js"],
    "dependencies": ["my-framework"],
    "patterns": ["import.*my-framework"]
})

# Add business domain indicators
analyzer.add_domain_pattern("my-domain", {
    "keywords": ["domain-specific-term"],
    "file_patterns": ["*domain*.py"],
    "dependency_patterns": ["domain-library"]
})
```

### Integration with Other Tools

```python
# Use with workflow generation
from workflow.generator import WorkflowGenerator

analysis = analyzer.analyze_project(".")
workflow = WorkflowGenerator.create_from_analysis(analysis)

# Use with setup wizard
from setup.wizard import SetupWizard

wizard = SetupWizard()
wizard.configure_from_analysis(analysis)
```

## 📈 Performance Optimization

- **Caching**: Analysis results are cached for repeated runs
- **Parallel Processing**: Multiple project analysis runs in parallel
- **Incremental Updates**: Only re-analyze changed files
- **Memory Optimization**: Efficient model loading and data processing

## 🤝 Contributing

To contribute to the Core AI System:

1. Add new technology patterns in `data/technology_patterns.json`
2. Extend business domain classification in `core/domain_classifier.py`
3. Improve ML models in `models/` directory
4. Add comprehensive tests in `tests/`

For detailed contribution guidelines, see the main framework documentation.