# Code Review Command

**Command**: `/code-review`
**Category**: Workflow Commands
**Description**: Multi-agent code review

## Usage

```
/code-review
/code-review --files="src/export/*.py"
/code-review --security-focus
/code-review --performance-focus
```

## Functionality

Initiates comprehensive multi-agent code review covering quality, security, performance, and architecture aspects.

### Review Process
1. **Code Analysis**: Automated code quality scanning
2. **Multi-Agent Review**: Parallel review by specialized agents
3. **Security Assessment**: Security-focused code analysis
4. **Performance Review**: Performance optimization opportunities
5. **Architecture Validation**: Design pattern and structure review
6. **Consolidated Report**: Unified findings and recommendations

### Output Format
```
🔍 MULTI-AGENT CODE REVIEW

Project: book_writing_app
Review Scope: Recent changes (23 files, 1,247 lines)
Review Team: 4 agents
Review Type: Comprehensive

📊 REVIEW SUMMARY:

Overall Score: 87/100 (Very Good)
Issues Found: 12 (3 High, 5 Medium, 4 Low)
Security Rating: 92/100 (Excellent)
Performance Rating: 83/100 (Good)

┌─ AGENT REVIEW RESULTS ──────────────────────────────────┐
│                                                         │
│ 🏗️ software-architect (Architecture Review)             │
│    Score: 89/100                                       │
│    ✅ Good separation of concerns                       │
│    ✅ Consistent design patterns                       │
│    ⚠️  Consider factory pattern for export formats     │
│    ⚠️  Some circular dependencies detected             │
│                                                         │
│ ⚙️ backend-engineer (Code Quality Review)              │
│    Score: 91/100                                       │
│    ✅ Clean Python code structure                      │
│    ✅ Good error handling                              │
│    ⚠️  Some functions exceed complexity limits         │
│    ❌ Missing type hints in 3 modules                  │
│                                                         │
│ 🔒 security-engineer (Security Review)                  │
│    Score: 92/100                                       │
│    ✅ No security vulnerabilities detected             │
│    ✅ Input validation properly implemented            │
│    ✅ Safe file handling practices                     │
│    ⚠️  Consider additional SQL injection protection    │
│                                                         │
│ ⚡ qa-engineer (Quality & Testing Review)               │
│    Score: 85/100                                       │
│    ✅ Good test coverage (88%)                         │
│    ✅ Well-structured test cases                       │
│    ⚠️  Integration tests need enhancement              │
│    ❌ Missing edge case tests for export edge cases    │
│                                                         │
└─────────────────────────────────────────────────────────┘

🚨 HIGH PRIORITY ISSUES:

Issue #1: Missing Type Hints (backend-engineer)
Files: src/export/pdf_exporter.py, src/export/docx_exporter.py
Impact: Maintainability, IDE support
Fix: Add complete type annotations
Estimate: 2 hours

Issue #2: Circular Dependencies (software-architect)
Files: src/models/document.py ↔ src/export/base_exporter.py
Impact: Architecture cleanliness, testing difficulty
Fix: Introduce dependency injection or interfaces
Estimate: 4 hours

Issue #3: Missing Edge Case Tests (qa-engineer)
Files: tests/export/ directory
Impact: Production reliability
Fix: Add comprehensive edge case testing
Estimate: 3 hours

⚠️ MEDIUM PRIORITY ISSUES:

• Complex function in src/export/docx_exporter.py:format_document()
• SQL injection protection in src/database/query_builder.py
• Integration test coverage for multi-format export
• Factory pattern for export format selection
• Performance optimization in large document handling

🔍 DETAILED FINDINGS:

Architecture Review (software-architect):
┌─────────────────────────────────────────────────────────┐
│ Strengths:                                              │
│ • Clean MVC architecture maintained                     │
│ • Good abstraction layers                              │
│ • Consistent naming conventions                        │
│                                                         │
│ Improvements:                                           │
│ • Implement factory pattern for exporters              │
│ • Consider command pattern for export operations       │
│ • Break circular dependencies                          │
└─────────────────────────────────────────────────────────┘

Code Quality (backend-engineer):
┌─────────────────────────────────────────────────────────┐
│ Metrics:                                                │
│ • Cyclomatic complexity: 6.2 (Target: <10) ✅          │
│ • Code duplication: 3.1% (Target: <5%) ✅              │
│ • Documentation coverage: 78% (Target: >80%) ⚠️        │
│                                                         │
│ Action Items:                                           │
│ • Add type hints to all public APIs                    │
│ • Refactor complex functions                           │
│ • Improve docstring coverage                           │
└─────────────────────────────────────────────────────────┘

Security Assessment (security-engineer):
┌─────────────────────────────────────────────────────────┐
│ Security Score: 92/100                                  │
│ • No critical vulnerabilities found ✅                 │
│ • Input validation comprehensive ✅                    │
│ • File operations secure ✅                           │
│ • Database queries parameterized ✅                   │
│                                                         │
│ Recommendations:                                        │
│ • Add additional SQL injection tests                   │
│ • Consider file type validation enhancement            │
└─────────────────────────────────────────────────────────┘

🔧 AUTOMATED FIXES AVAILABLE:

Auto-fixable (Run /code-review --auto-fix):
✅ Import statement organization
✅ Code formatting (black, isort)
✅ Basic linting issues (flake8)
✅ Documentation format standardization

Manual Review Required:
⚠️ Type hint additions
⚠️ Architecture refactoring
⚠️ Test case development
⚠️ Performance optimizations

📅 REVIEW ACTION PLAN:

Immediate (Today):
1. Apply automated fixes (/code-review --auto-fix)
2. Add missing type hints (backend-engineer)
3. Address high-priority security items

This Week:
4. Refactor circular dependencies (software-architect)
5. Enhance integration tests (qa-engineer)
6. Performance optimization review

Next Sprint:
7. Implement factory patterns
8. Comprehensive edge case testing
9. Architecture documentation update

✨ REVIEW COMPLETE!

Next Review: Scheduled for next Friday
Auto-Review: Enabled for all commits
Quality Gate: Passing (87/100 > 80 threshold)
```

## Integration

- Multi-agent coordination
- Automated code analysis tools
- Quality gate enforcement
- Performance monitoring integration