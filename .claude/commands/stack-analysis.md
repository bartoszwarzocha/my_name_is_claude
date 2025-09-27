# Stack Analysis Command

**Command**: `/stack-analysis`
**Category**: Project Analysis
**Description**: Szczegółowa analiza stacku technologicznego projektu

## Usage

```
/stack-analysis
/stack-analysis --recommendations
/stack-analysis --compatibility
/stack-analysis --alternatives
```

## Functionality

Analyzes current technology stack, identifies compatibility issues, performance bottlenecks, and suggests optimizations.

### Analysis Components
- **Technology Detection**: Automatic detection of used technologies
- **Version Compatibility**: Cross-technology version compatibility analysis
- **Performance Assessment**: Stack performance characteristics
- **Security Analysis**: Known vulnerabilities and security considerations
- **Scalability Review**: Scalability limitations and opportunities
- **Alternative Suggestions**: Better technology alternatives when applicable

### Output Format
```
📊 TECHNOLOGY STACK ANALYSIS

Project: book_writing_app
Detected Technologies: 8
Compatibility Score: 92/100

┌─ CORE STACK ────────────────────────────────────────────┐
│ 🐍 Python 3.9+                        ✅ Current       │
│    Status: Fully supported                              │
│    Recommendation: Consider upgrade to 3.11 for perf   │
│                                                         │
│ 🖥️  wxPython 4.1+                     ✅ Latest        │
│    Status: Excellent choice for desktop GUI            │
│    Compatibility: Perfect with Python 3.9+             │
│                                                         │
│ 🗄️  SQLite 3                          ✅ Stable        │
│    Status: Ideal for local desktop storage             │
│    Performance: Excellent for single-user apps         │
└─────────────────────────────────────────────────────────┘

🔍 COMPATIBILITY MATRIX:

              Python  wxPython  SQLite  OpenOffice
Python 3.9+      ✅       ✅       ✅         ✅
wxPython 4.1+    ✅       ✅       ✅         ✅
SQLite 3         ✅       ✅       ✅         ✅
OpenOffice API   ✅       ✅       ✅         ✅

⚡ PERFORMANCE CHARACTERISTICS:
• Desktop Responsiveness: Excellent (wxPython native performance)
• Database Performance: Very Good (SQLite local access)
• Memory Usage: Low to Medium (Python + wxPython)
• Startup Time: Fast (native desktop application)

🔒 SECURITY CONSIDERATIONS:
• Python Dependencies: Regular security updates needed
• SQLite: File-based security (encryption recommended)
• OpenOffice API: Document parsing security

📈 SCALABILITY ASSESSMENT:
• User Concurrency: Single-user (SQLite limitation)
• Data Volume: Good (SQLite handles GB-scale efficiently)
• Feature Expansion: Excellent (modular Python architecture)

💡 RECOMMENDATIONS:

Immediate:
• Setup dependency vulnerability scanning
• Implement SQLite encryption for sensitive data
• Consider Python 3.11 migration for performance

Future Considerations:
• PostgreSQL migration if multi-user needed
• Electron alternative for web technology integration
• Native compilation options (PyInstaller/Nuitka)
```

## Integration

- CLAUDE.md technology configuration
- Agent expertise matching
- Dependency management analysis
- Performance profiling integration