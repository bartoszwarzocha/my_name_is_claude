# SonarQube Code Quality Analysis

**Agent: reviewer**
**Purpose: Conduct comprehensive code quality analysis using SonarQube and establish quality gates**

---

## 🎯 Mission

Perform systematic code quality analysis using SonarQube to ensure maintainability, reliability, and security standards while establishing automated quality gates for continuous improvement.

## 📋 SonarQube Analysis Process

### Step 1: SonarQube Configuration Setup

**Quality Profile Configuration:**
```xml
<!-- sonar-project.properties -->
sonar.projectKey=myapp
sonar.projectName=MyApp
sonar.projectVersion=1.0

# Source code configuration
sonar.sources=src
sonar.tests=tests
sonar.exclusions=**/node_modules/**,**/dist/**,**/*.spec.js,**/*.test.js
sonar.test.exclusions=src/**

# Language-specific settings
sonar.javascript.lcov.reportPaths=coverage/lcov.info
sonar.typescript.lcov.reportPaths=coverage/lcov.info
sonar.python.coverage.reportPaths=coverage.xml
sonar.java.coveragePlugin=jacoco
sonar.jacoco.reportPaths=target/jacoco.exec

# Quality gate thresholds
sonar.qualitygate.wait=true
sonar.coverage.minimum=80
sonar.duplicated_lines_density.maximum=3
sonar.maintainability_rating.minimum=A
sonar.reliability_rating.minimum=A
sonar.security_rating.minimum=A
```

**Custom Quality Rules:**
```json
{
  "customRules": {
    "complexity": {
      "cyclomatic_complexity_per_function": 15,
      "cognitive_complexity_per_function": 15,
      "lines_per_function": 50,
      "parameters_per_function": 5
    },
    "maintainability": {
      "comment_density_minimum": 10,
      "documentation_coverage_minimum": 80,
      "code_duplication_maximum": 3,
      "technical_debt_ratio_maximum": 5
    },
    "reliability": {
      "bug_density_maximum": 1,
      "critical_issues_maximum": 0,
      "major_issues_maximum": 10
    },
    "security": {
      "security_hotspots_maximum": 0,
      "vulnerabilities_maximum": 0,
      "security_rating_minimum": "A"
    }
  }
}
```

### Step 2: Automated Analysis Integration

**CI/CD Pipeline Integration:**
```yaml
# .github/workflows/sonar-analysis.yml
name: SonarQube Analysis

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  sonarqube:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
      with:
        fetch-depth: 0  # Disable shallow clone for better analysis
        
    - name: Setup Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '18'
        
    - name: Install dependencies
      run: npm ci
      
    - name: Run tests with coverage
      run: npm run test:coverage
      
    - name: Run ESLint
      run: npm run lint -- --format json --output-file eslint-report.json
      
    - name: SonarQube Scan
      uses: sonarqube-quality-gate-action@master
      env:
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
        SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
        
    - name: Quality Gate Check
      run: |
        if [ "${{ steps.sonarqube.outputs.quality-gate-status }}" != "PASSED" ]; then
          echo "Quality gate failed. Check SonarQube dashboard for details."
          exit 1
        fi
```

### Step 3: Comprehensive Analysis Execution

**Code Quality Metrics Analysis:**
```python
# sonar_analysis.py - Custom analysis script
import requests
import json
from datetime import datetime

class SonarQubeAnalyzer:
    def __init__(self, sonar_url, token, project_key):
        self.sonar_url = sonar_url
        self.token = token
        self.project_key = project_key
        self.headers = {'Authorization': f'Bearer {token}'}
    
    def get_quality_gate_status(self):
        """Get current quality gate status"""
        url = f"{self.sonar_url}/api/qualitygates/project_status"
        params = {'projectKey': self.project_key}
        
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
    
    def get_metrics(self):
        """Retrieve comprehensive project metrics"""
        metrics = [
            'lines', 'lines_to_cover', 'coverage', 'line_coverage',
            'uncovered_lines', 'duplicated_lines_density', 'duplicated_lines',
            'bugs', 'vulnerabilities', 'security_hotspots', 'code_smells',
            'sqale_rating', 'reliability_rating', 'security_rating',
            'complexity', 'cognitive_complexity', 'technical_debt',
            'sqale_index', 'sqale_debt_ratio'
        ]
        
        url = f"{self.sonar_url}/api/measures/component"
        params = {
            'component': self.project_key,
            'metricKeys': ','.join(metrics)
        }
        
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
    
    def analyze_trends(self, days=30):
        """Analyze quality trends over time"""
        url = f"{self.sonar_url}/api/measures/search_history"
        params = {
            'component': self.project_key,
            'metrics': 'coverage,bugs,vulnerabilities,code_smells',
            'from': f'{days}d'
        }
        
        response = requests.get(url, headers=self.headers, params=params)
        history = response.json()
        
        return self._calculate_trends(history)
    
    def generate_quality_report(self):
        """Generate comprehensive quality report"""
        quality_gate = self.get_quality_gate_status()
        metrics = self.get_metrics()
        trends = self.analyze_trends()
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'project': self.project_key,
            'quality_gate': quality_gate,
            'metrics': self._format_metrics(metrics),
            'trends': trends,
            'recommendations': self._generate_recommendations(metrics)
        }
        
        return report
```

### Step 4: Issue Classification and Prioritization

**Issue Severity Analysis:**
```yaml
# Issue classification framework
issue_classification:
  blocker:
    description: "Critical issues that prevent production deployment"
    examples:
      - Security vulnerabilities (SQL injection, XSS)
      - Critical bugs causing system crashes
      - Major performance issues
    action_required: "Must fix before deployment"
    
  critical:
    description: "Issues that significantly impact functionality"
    examples:
      - High-severity bugs affecting core features
      - Security hotspots requiring immediate attention
      - Major code quality violations
    action_required: "Fix within 24 hours"
    
  major:
    description: "Important issues affecting maintainability"
    examples:
      - Code smells reducing maintainability
      - Performance issues in non-critical paths
      - Missing test coverage in important functions
    action_required: "Fix within sprint"
    
  minor:
    description: "Issues that should be addressed for best practices"
    examples:
      - Minor code style violations
      - Documentation improvements
      - Non-critical code duplication
    action_required: "Fix in subsequent sprints"
```

## 📊 Quality Gate Management

### Step 5: Custom Quality Gates

**Project-Specific Quality Gates:**
```json
{
  "qualityGates": {
    "production": {
      "name": "Production Ready",
      "conditions": [
        {
          "metric": "coverage",
          "operator": "GT",
          "threshold": 85,
          "error": true
        },
        {
          "metric": "duplicated_lines_density",
          "operator": "LT", 
          "threshold": 3,
          "error": true
        },
        {
          "metric": "maintainability_rating",
          "operator": "GT",
          "threshold": 1,
          "error": true
        },
        {
          "metric": "reliability_rating",
          "operator": "GT",
          "threshold": 1,
          "error": true
        },
        {
          "metric": "security_rating",
          "operator": "GT",
          "threshold": 1,
          "error": true
        }
      ]
    },
    "development": {
      "name": "Development Quality",
      "conditions": [
        {
          "metric": "coverage",
          "operator": "GT",
          "threshold": 70,
          "error": false
        },
        {
          "metric": "bugs",
          "operator": "GT",
          "threshold": 0,
          "error": true
        },
        {
          "metric": "vulnerabilities",
          "operator": "GT",
          "threshold": 0,
          "error": true
        }
      ]
    }
  }
}
```

### Step 6: Remediation Guidelines

**Issue Remediation Strategies:**
```markdown
## Code Quality Issues Remediation

### High Complexity Issues
**Problem:** Functions/methods with high cyclomatic complexity
**Impact:** Difficult to understand, test, and maintain
**Solution:**
- Break down complex functions into smaller, focused functions
- Use early returns to reduce nesting
- Extract complex conditions into well-named variables
- Consider design patterns like Strategy or Command

### Code Duplication
**Problem:** Duplicated code blocks detected
**Impact:** Maintenance overhead, inconsistent changes
**Solution:**
- Extract common code into reusable functions/classes
- Use inheritance or composition for related functionality
- Create utility functions for common operations
- Implement shared libraries for cross-project duplication

### Security Vulnerabilities
**Problem:** Security issues detected by analysis
**Impact:** Potential security breaches and data exposure
**Solution:**
- Input validation and sanitization
- Proper authentication and authorization
- Secure coding practices
- Regular security training and code reviews

### Poor Test Coverage
**Problem:** Low test coverage in critical code paths
**Impact:** Higher risk of undetected bugs
**Solution:**
- Add unit tests for uncovered functions
- Implement integration tests for critical workflows
- Use mutation testing to validate test quality
- Set up automated coverage reporting
```

## 🔄 Continuous Quality Improvement

### Step 7: Quality Metrics Dashboard

**Quality Dashboard Configuration:**
```json
{
  "dashboard": {
    "widgets": [
      {
        "type": "quality_gate",
        "title": "Quality Gate Status",
        "project": "myapp"
      },
      {
        "type": "metric",
        "title": "Code Coverage",
        "metric": "coverage",
        "format": "percent"
      },
      {
        "type": "metric",
        "title": "Technical Debt",
        "metric": "sqale_index",
        "format": "work_duration"
      },
      {
        "type": "timeline",
        "title": "Quality Trends",
        "metrics": ["coverage", "bugs", "vulnerabilities", "code_smells"],
        "period": "30d"
      },
      {
        "type": "issues",
        "title": "Recent Issues",
        "filters": ["OPEN", "REOPENED"],
        "limit": 10
      }
    ]
  }
}
```

### Step 8: Team Quality Coaching

**Quality Review Meeting Agenda:**
```markdown
## Weekly Quality Review Meeting

### Agenda (45 minutes)
1. **Quality Gate Status** (10 minutes)
   - Current project quality gate status
   - Any failed gates and impact assessment
   - Immediate action items

2. **Metrics Review** (15 minutes)
   - Coverage trends and targets
   - Technical debt accumulation
   - Bug and vulnerability trends
   - Code complexity analysis

3. **Issue Prioritization** (10 minutes)
   - New critical/blocker issues
   - Long-standing issues requiring attention
   - Resource allocation for remediation

4. **Process Improvement** (10 minutes)
   - Quality process effectiveness
   - Tool configuration updates
   - Team feedback and suggestions
   - Training needs identification

### Action Items Template
- [ ] Issue: [Description]
- [ ] Owner: [Team member]
- [ ] Priority: [Critical/High/Medium/Low]
- [ ] Due Date: [Date]
- [ ] Status: [Not Started/In Progress/Done]
```

## 📤 Deliverables

- **SonarQube Configuration** with custom rules and quality gates
- **CI/CD Integration** with automated quality checks
- **Quality Analysis Reports** with metrics and trends
- **Issue Remediation Plan** with prioritized action items
- **Quality Dashboard** with real-time metrics visualization
- **Team Quality Guidelines** with best practices and procedures
- **Quality Review Process** with regular assessment cadence

## 🤝 Collaboration Points

**With all development agents:** Quality standards enforcement and remediation guidance
**With deployment-engineer:** Quality gate integration in CI/CD pipelines
**With security-engineer:** Security vulnerability analysis and remediation
**With qa-engineer:** Test coverage analysis and improvement strategies
**With software-architect:** Technical debt assessment and architectural quality

---
*Systematic code quality analysis ensures maintainable, reliable, and secure software through continuous monitoring and improvement.*