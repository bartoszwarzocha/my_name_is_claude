# Architecture Review Command

**Command**: `/architecture-review`
**Category**: Project Analysis
**Description**: Kompleksowy review architektury z software-architect

## Usage

```
/architecture-review
/architecture-review --detailed
/architecture-review --recommendations
/architecture-review --patterns
```

## Functionality

Activates software-architect agent for comprehensive architecture analysis, design pattern review, and improvement recommendations.

### Review Areas
- **System Architecture**: Overall system design and component organization
- **Design Patterns**: Applied patterns and anti-patterns identification
- **Modularity**: Code organization and module separation
- **Scalability**: Architecture scalability and extensibility
- **Maintainability**: Code maintainability and technical debt
- **Performance**: Architectural performance implications

### Output Format
```
🏢 ARCHITECTURE REVIEW REPORT

Project: book_writing_app
Reviewed by: software-architect
Architecture Pattern: MVC (Model-View-Controller)
Complexity Score: 6/10 (Moderate)

┌─ ARCHITECTURE OVERVIEW ───────────────────────────────┐
│                                                         │
│    GUI Layer (wxPython)                                │
│         │                                            │
│    ┌──────────────────────────────┐               │
│    │      Business Logic        │               │
│    │    (Controllers)          │               │
│    └──────────────────────────────┘               │
│         │                                            │
│    Data Layer (SQLite + Models)                        │
│                                                         │
└─────────────────────────────────────────────────────────┘

✅ ARCHITECTURAL STRENGTHS:
• Clear separation of concerns (MVC pattern)
• Appropriate technology choices for desktop app
• Simple and maintainable structure
• Good scalability for single-user application

🟡 AREAS FOR IMPROVEMENT:
• Add service layer for complex business logic
• Implement repository pattern for data access
• Consider dependency injection for better testability
• Add event system for loose coupling

🚨 ARCHITECTURAL ISSUES:
• Direct database access in GUI components
• Missing abstraction layers
• Limited error handling architecture

📈 DESIGN PATTERNS ANALYSIS:

Current Patterns:
✅ MVC - Well implemented
✅ Observer - Used in wxPython events
⚠️  Singleton - Overused, consider alternatives

Recommended Patterns:
💡 Repository - For data access abstraction
💡 Strategy - For different export formats
💡 Command - For undo/redo functionality
💡 Factory - For document type creation

🔧 REFACTORING RECOMMENDATIONS:

Immediate (High Priority):
1. Extract data access layer (Repository pattern)
2. Create service layer for business logic
3. Implement proper error handling architecture

Medium Priority:
4. Add dependency injection container
5. Implement plugin architecture for extensibility
6. Create event-driven communication system

Future Considerations:
7. Consider CQRS for complex data operations
8. Evaluate microservices for feature isolation

📊 METRICS:
• Cyclomatic Complexity: 6 (Acceptable)
• Coupling: Medium (Can be improved)
• Cohesion: High (Good)
• Maintainability Index: 75/100 (Good)
```

## Integration

- software-architect agent activation
- Code analysis tools integration
- Design pattern library access
- Refactoring guidance provision
- Technical debt assessment