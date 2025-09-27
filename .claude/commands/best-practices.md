# Best Practices Command

**Command**: `/best-practices [area]`
**Category**: Development Helpers
**Description**: Best practices dla obszaru rozwoju

## Usage

```
/best-practices python
/best-practices "gui development"
/best-practices security
/best-practices "database design"
```

## Functionality

Provides curated best practices, guidelines, and recommendations for specific development areas, technologies, or domains.

### Output Format
```
⭐ BEST PRACTICES: "python"

Practice Category: Programming Language
Technology Focus: Python 3.9+ Development
Project Context: Desktop Application
Agent Specialist: backend-engineer

┌─ CORE PYTHON PRINCIPLES ────────────────────────────────┐
│                                                         │
│ 🐍 The Zen of Python in Practice                       │
│                                                         │
│ 1. Beautiful is better than ugly                       │
│    → Use clear, readable code structure                │
│    → Follow PEP 8 style guidelines                     │
│    → Choose descriptive variable names                 │
│                                                         │
│ 2. Explicit is better than implicit                    │
│    → Use type hints for public APIs                    │
│    → Avoid magic numbers and strings                   │
│    → Make dependencies and assumptions clear           │
│                                                         │
│ 3. Simple is better than complex                       │
│    → Prefer built-in functions over custom ones        │
│    → Use standard library when possible                │
│    → Avoid premature optimization                      │
│                                                         │
│ 4. Readability counts                                   │
│    → Write self-documenting code                       │
│    → Use docstrings for public functions               │
│    → Comment the "why", not the "what"                 │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ CODE STRUCTURE & ORGANIZATION ─────────────────────────┐
│                                                         │
│ 📁 Project Structure Best Practices                    │
│                                                         │
│ ✅ DO:                                                  │
│ • Use meaningful package and module names              │
│ • Keep modules focused on single responsibility        │
│ • Separate business logic from presentation             │
│ • Use __init__.py for package initialization           │
│                                                         │
│ ❌ DON'T:                                               │
│ • Create god classes or modules                        │
│ • Mix different concerns in one file                   │
│ • Use overly nested directory structures               │
│ • Import using wildcard (*) imports                    │
│                                                         │
│ 📂 Recommended Structure:                               │
│ ```                                                     │
│ project/                                                │
│ ├── src/                    # Source code              │
│ │   ├── models/             # Data models              │
│ │   ├── views/              # UI components            │
│ │   ├── controllers/        # Business logic           │
│ │   └── utils/              # Helper functions         │
│ ├── tests/                  # Test files               │
│ ├── docs/                   # Documentation            │
│ ├── requirements.txt        # Dependencies             │
│ └── setup.py                # Package configuration    │
│ ```                                                     │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ ERROR HANDLING & ROBUSTNESS ───────────────────────────┐
│                                                         │
│ 🛡️ Exception Handling Best Practices                   │
│                                                         │
│ ✅ GOOD PRACTICES:                                      │
│                                                         │
│ ```python                                              │
│ # Be specific with exception types                     │
│ try:                                                    │
│     result = risky_operation()                         │
│ except FileNotFoundError:                              │
│     logger.error("Configuration file not found")       │
│     return default_config()                            │
│ except PermissionError:                                │
│     logger.error("Insufficient permissions")           │
│     raise ConfigurationError("Cannot access config")   │
│                                                         │
│ # Use finally for cleanup                              │
│ try:                                                    │
│     file = open("data.txt")                            │
│     process_file(file)                                 │
│ finally:                                               │
│     file.close()                                       │
│                                                         │
│ # Better: Use context managers                         │
│ with open("data.txt") as file:                         │
│     process_file(file)                                 │
│ ```                                                     │
│                                                         │
│ ❌ AVOID:                                               │
│ • Bare except clauses (except:)                        │
│ • Silently swallowing exceptions                       │
│ • Using exceptions for control flow                    │
│ • Raising generic Exception types                      │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ PERFORMANCE OPTIMIZATION ──────────────────────────────┐
│                                                         │
│ ⚡ Performance Best Practices                           │
│                                                         │
│ Data Structures:                                        │
│ • Use sets for membership testing (O(1) vs O(n))       │
│ • Use deque for frequent insertions/deletions          │
│ • Use dict.get() instead of key checking               │
│ • Prefer list comprehensions over loops when readable  │
│                                                         │
│ Memory Management:                                      │
│ • Use generators for large datasets                    │
│ • Close file handles and database connections          │
│ • Use weak references to avoid circular references     │
│ • Profile memory usage with memory_profiler            │
│                                                         │
│ Algorithm Efficiency:                                   │
│ ```python                                              │
│ # Good: Use built-in functions                         │
│ result = sum(numbers)                                  │
│                                                         │
│ # Avoid: Manual loops for built-in operations          │
│ total = 0                                              │
│ for num in numbers:                                    │
│     total += num                                       │
│                                                         │
│ # Good: Use enumerate instead of range(len())          │
│ for i, item in enumerate(items):                       │
│     process(i, item)                                   │
│                                                         │
│ # Good: Use zip for parallel iteration                 │
│ for name, age in zip(names, ages):                     │
│     print(f"{name} is {age} years old")                │
│ ```                                                     │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ TESTING & QUALITY ASSURANCE ───────────────────────────┐
│                                                         │
│ 🧪 Testing Best Practices                              │
│                                                         │
│ Test Structure:                                         │
│ • Follow AAA pattern: Arrange, Act, Assert             │
│ • Use descriptive test names                           │
│ • Test one thing per test function                     │
│ • Use fixtures for test data setup                     │
│                                                         │
│ ```python                                              │
│ import pytest                                          │
│                                                         │
│ class TestDocumentModel:                               │
│     def test_document_creation_with_valid_data(self):   │
│         # Arrange                                      │
│         title = "Test Document"                        │
│         content = "Sample content"                     │
│                                                         │
│         # Act                                          │
│         doc = Document(title=title, content=content)   │
│                                                         │
│         # Assert                                       │
│         assert doc.title == title                      │
│         assert doc.content == content                  │
│         assert doc.get_word_count() == 2               │
│                                                         │
│     def test_document_validation_fails_with_empty_title(self):│
│         # Arrange                                      │
│         doc = Document(title="", content="content")    │
│                                                         │
│         # Act                                          │
│         errors = doc.validate()                        │
│                                                         │
│         # Assert                                       │
│         assert "Title is required" in errors           │
│ ```                                                     │
│                                                         │
│ Coverage Goals:                                         │
│ • Unit tests: >90% coverage                           │
│ • Integration tests: >80% coverage                    │
│ • Critical paths: 100% coverage                       │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ SECURITY BEST PRACTICES ───────────────────────────────┐
│                                                         │
│ 🔒 Security Guidelines                                 │
│                                                         │
│ Input Validation:                                       │
│ ```python                                              │
│ def validate_filename(filename: str) -> str:           │
│     \"\"\"Validate and sanitize filename input.\"\"\"         │
│     # Remove dangerous characters                      │
│     safe_chars = re.sub(r'[^\\w\\-_\\.]', '', filename)  │
│                                                         │
│     # Prevent path traversal                           │
│     if '..' in safe_chars or safe_chars.startswith('/'):│
│         raise ValueError("Invalid filename")            │
│                                                         │
│     return safe_chars                                  │
│ ```                                                     │
│                                                         │
│ Database Security:                                      │
│ ```python                                              │
│ # Good: Use parameterized queries                      │
│ cursor.execute(                                        │
│     "SELECT * FROM documents WHERE id = ?", (doc_id,)  │
│ )                                                       │
│                                                         │
│ # Bad: String formatting (SQL injection risk)          │
│ cursor.execute(                                        │
│     f"SELECT * FROM documents WHERE id = {doc_id}"     │
│ )                                                       │
│ ```                                                     │
│                                                         │
│ File Operations:                                        │
│ • Validate file types before processing                │
│ • Use temporary directories for untrusted files        │
│ • Set appropriate file permissions                     │
│ • Scan for malicious content                          │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ DESKTOP APP SPECIFIC PRACTICES ────────────────────────┐
│                                                         │
│ 🖥️ wxPython & Desktop Development                      │
│                                                         │
│ GUI Threading:                                          │
│ ```python                                              │
│ # Good: Use CallAfter for thread-safe UI updates       │
│ def update_ui_from_thread(self, data):                 │
│     wx.CallAfter(self.update_display, data)            │
│                                                         │
│ # Good: Use threading for long operations              │
│ import threading                                       │
│                                                         │
│ def long_operation(self):                              │
│     def worker():                                      │
│         result = expensive_computation()               │
│         wx.CallAfter(self.on_operation_complete, result)│
│                                                         │
│     thread = threading.Thread(target=worker)           │
│     thread.daemon = True                               │
│     thread.start()                                     │
│ ```                                                     │
│                                                         │
│ Resource Management:                                    │
│ • Always call Destroy() on dialogs                    │
│ • Use context managers for database connections        │
│ • Implement proper shutdown procedures                 │
│ • Handle application exit gracefully                   │
│                                                         │
│ User Experience:                                        │
│ • Provide progress indicators for long operations      │
│ • Implement auto-save functionality                    │
│ • Show helpful error messages                         │
│ • Support keyboard shortcuts                          │
│                                                         │
└─────────────────────────────────────────────────────────┘

🎯 PROJECT-SPECIFIC RECOMMENDATIONS:

For Your Book Writing App:
┌─────────────────────────────────────────────────────────┐
│ Document Management:                                    │
│ • Implement auto-save every 30 seconds                 │
│ • Use transactions for database operations             │
│ • Provide export progress indicators                   │
│ • Handle large documents efficiently                   │
│                                                         │
│ Export System:                                          │
│ • Validate document structure before export            │
│ • Use streaming for large file exports                 │
│ • Provide format-specific error handling               │
│ • Implement export cancellation                        │
│                                                         │
│ User Interface:                                         │
│ • Use sizers instead of absolute positioning           │
│ • Implement responsive layout design                   │
│ • Provide dark/light theme support                     │
│ • Add accessibility features                           │
└─────────────────────────────────────────────────────────┘

🔗 RELATED BEST PRACTICES:

Technology Specific:
• /best-practices "sqlite" - Database optimization
• /best-practices "wxpython" - GUI development guidelines
• /best-practices "testing" - Comprehensive testing strategies

Domain Specific:
• /best-practices "security" - Security-focused development
• /best-practices "performance" - Performance optimization
• /best-practices "deployment" - Application distribution

🤖 AGENT SUPPORT:

Get Expert Guidance:
• backend-engineer: Python development best practices
• desktop-specialist: wxPython and GUI best practices
• security-engineer: Security implementation guidance
• qa-engineer: Testing and quality assurance practices

✨ BEST PRACTICES GUIDE COMPLETE!

Categories Covered: 6
Code Examples: 15
Security Guidelines: 8
Performance Tips: 12
Project-Specific Recommendations: 16
```

## Integration

- Agent expertise integration
- Project-specific recommendations
- Code example library
- Quality standard enforcement