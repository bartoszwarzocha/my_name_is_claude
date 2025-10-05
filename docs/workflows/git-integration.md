# Git Integration Workflow

*Integrating My Name Is Claude framework with Git workflows for enhanced version control and collaboration*

## 🎯 Overview

This guide covers Git integration best practices, automated workflows, and collaboration strategies when using My Name Is Claude framework.

---

## 🔄 Git Workflow Integration

### **Standard Development Workflow**

```bash
# 1. Start new feature
git checkout -b feature/new-api-endpoint

# 2. Use framework agents for development
# Execute backend-engineer agent for implementation

# 3. Regular commits during development
git add .
git commit -m "feat: implement user authentication API"

# 4. Quality checks before push
# Execute qa-engineer agent for testing

# 5. Push to remote
git push origin feature/new-api-endpoint

# 6. Create pull request
# Use reviewer agent for code review
```

---

## 🤖 Automated Git Operations

### **Pre-Commit Hooks**

**.git/hooks/pre-commit:**
```bash
#!/bin/bash

# Run framework quality checks
python3 .ai-tools/quality/framework_quality_assessor.py

if [ $? -ne 0 ]; then
    echo "❌ Quality checks failed. Commit aborted."
    exit 1
fi

# Run linting
npm run lint
if [ $? -ne 0 ]; then
    echo "❌ Linting failed. Commit aborted."
    exit 1
fi

echo "✅ Pre-commit checks passed"
exit 0
```

### **Commit Message Automation**

```bash
# Generate commit message using framework
python3 <<'EOF'
from ai_tools import get_git_diff, generate_commit_message

diff = get_git_diff()
message = generate_commit_message(diff)

print(message)
EOF

# Use generated message
git commit -m "$(python3 generate_commit_message.py)"
```

---

## 🔍 Code Review Integration

### **Automated Review Workflow**

```bash
# Create review using framework
./framework-review.sh pull-request/123

# Script executes:
# 1. reviewer agent → Code quality analysis
# 2. security-engineer agent → Security scan
# 3. qa-engineer agent → Test coverage check
# 4. Generate review comments

# Example output:
# - security-engineer: "Found SQL injection vulnerability in user_service.py:45"
# - reviewer: "Consider extracting this 50-line function into smaller units"
# - qa-engineer: "Missing test coverage for error handling"
```

---

## 🚀 CI/CD Pipeline Integration

### **GitHub Actions Example**

**.github/workflows/framework-quality.yml:**
```yaml
name: Framework Quality Check

on: [push, pull_request]

jobs:
  quality-check:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Framework
        run: |
          cd .ai-tools/setup
          ./install_dependencies.sh

      - name: Run Quality Assessment
        run: |
          python3 .ai-tools/quality/framework_quality_assessor.py

      - name: Agent Code Review
        run: |
          # Use reviewer agent for automated code review
          python3 .ai-tools/core/automated_review.py

      - name: Security Scan
        run: |
          # Use security-engineer agent
          python3 .ai-tools/core/security_scan.py
```

---

## 📊 Git Analytics

### **Track Development Metrics**

```python
import git

class GitAnalytics:
    def __init__(self, repo_path):
        self.repo = git.Repo(repo_path)

    def get_commit_stats(self, since_date):
        """Analyze commit patterns"""
        commits = list(self.repo.iter_commits(since=since_date))

        return {
            'total_commits': len(commits),
            'average_commits_per_day': len(commits) / 30,
            'contributors': len(set(c.author for c in commits)),
            'files_changed': sum(c.stats.total['files'] for c in commits),
            'lines_added': sum(c.stats.total['insertions'] for c in commits),
            'lines_deleted': sum(c.stats.total['deletions'] for c in commits)
        }

    def detect_patterns(self):
        """Detect development patterns using AI"""
        # Use data-scientist agent for pattern analysis
        commits = list(self.repo.iter_commits(max_count=100))

        patterns = {
            'frequent_commit_times': self.analyze_commit_times(commits),
            'most_modified_files': self.get_hotspots(commits),
            'commit_message_quality': self.assess_commit_messages(commits)
        }

        return patterns
```

---

## 🔗 Branch Management

### **Feature Branch Workflow**

```bash
# Create feature branch with framework
./framework-branch.sh create feature/user-dashboard

# Framework automatically:
# 1. Creates branch
# 2. Configures agents for feature
# 3. Sets up quality gates
# 4. Initializes checkpoint

# Development workflow
git checkout feature/user-dashboard

# Framework checkpoint: Before major changes
./framework-checkpoint.sh create "before implementing authentication"

# Make changes
# ...

# Framework checkpoint: After implementation
./framework-checkpoint.sh create "authentication implemented"

# Rewind if needed
./framework-checkpoint.sh rewind "before implementing authentication"
```

---

## 🔄 Merge Strategies

### **Framework-Enhanced Merge**

```bash
# Before merging, run framework validation
./framework-validate.sh feature/user-dashboard

# Framework executes:
# 1. qa-engineer → Full test suite
# 2. security-engineer → Security validation
# 3. performance-engineer → Performance check
# 4. reviewer → Final code review

# If all checks pass:
git checkout main
git merge --no-ff feature/user-dashboard
git push origin main
```

---

## 📚 Git Best Practices with Framework

### **1. Commit Frequency**
- ✅ Commit after each logical change
- ✅ Use framework checkpoints for major milestones
- ✅ Link commits to agent executions

### **2. Branch Naming**
- `feature/` - New features (use product-manager, developers)
- `fix/` - Bug fixes (use qa-engineer, backend-engineer)
- `refactor/` - Code improvements (use software-architect, reviewer)
- `docs/` - Documentation (use technical-writer)

### **3. Commit Messages**
```
<type>(<scope>): <subject>

<body>

<footer>

🤖 Generated with My Name Is Claude
Agent: backend-engineer
Task: Implement user authentication
```

**Types:**
- feat: New feature
- fix: Bug fix
- refactor: Code refactoring
- docs: Documentation
- test: Testing
- chore: Maintenance

---

## 🔗 Related Documentation

- **[Development Workflow](development-workflow.md)** - Standard development process
- **[Team Collaboration](team-collaboration.md)** - Team Git workflows
- **[Compliance Workflow](compliance-workflow.md)** - Compliance in Git

---

**Last Updated:** 2025-10-05 | **Version:** 3.3.0
