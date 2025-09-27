# Dependency Check Command

**Command**: `/dependency-check`
**Category**: Project Analysis
**Description**: Sprawdzenie zależności i kompatybilności

## Usage

```
/dependency-check
/dependency-check --security
/dependency-check --outdated
/dependency-check --fix
```

## Functionality

Analyzes project dependencies for compatibility issues, security vulnerabilities, and update opportunities.

### Check Types
- **Compatibility**: Version conflicts and incompatibilities
- **Security**: Known vulnerabilities in dependencies
- **Updates**: Available updates and upgrade paths
- **Licensing**: License compatibility analysis
- **Performance**: Performance impact of dependencies

### Output Format
```
🔍 DEPENDENCY CHECK REPORT

Project: book_writing_app
Dependencies Analyzed: 15
Issues Found: 3 (1 Critical, 2 Warnings)

⚠️ CRITICAL ISSUES:
• requests==2.25.1 - Known security vulnerability (CVE-2023-xxx)
  🔒 Fix: Upgrade to requests>=2.28.0

🟡 WARNINGS:
• wxPython==4.1.0 - Update available (4.2.1)
  🔄 Recommendation: Test compatibility before upgrading
• sqlite3 - Consider SQLAlchemy for better ORM support
  💡 Enhancement: Improves maintainability

✅ HEALTHY DEPENDENCIES:
• Python 3.9.12 - Supported version
• numpy 1.21.0 - Compatible and stable
• python-docx 0.8.11 - Latest stable version

📊 DEPENDENCY GRAPH:
Python 3.9
├── wxPython 4.1.0
├── requests 2.25.1 ⚠️
├── python-docx 0.8.11
└── SQLite3 (built-in)

🔧 RECOMMENDED ACTIONS:
1. 🔴 URGENT: Update requests to fix security vulnerability
2. 🟡 MEDIUM: Consider wxPython update after testing
3. 🟢 LOW: Evaluate SQLAlchemy integration benefits
```

## Options

### `--security`
Focuses on security vulnerabilities only

### `--outdated`
Shows only outdated dependencies

### `--fix`
Attempts automatic fixes for safe updates

## Integration

- Package manager integration (pip, conda, etc.)
- Security vulnerability databases
- Agent recommendations for updates
- CI/CD pipeline integration