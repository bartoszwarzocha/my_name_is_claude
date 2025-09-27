# Find Agent Command

**Command**: `/find-agent [skill]`
**Category**: Development Helpers
**Description**: Znajdź agenta z konkretną umiejętnością

## Usage

```
/find-agent opengl
/find-agent "database optimization"
/find-agent testing
/find-agent "user interface design"
```

## Functionality

Advanced search through agent competencies database to find specialists for specific skills, technologies, or problem domains.

### Search Capabilities
- **Technology Keywords**: python, cpp, opengl, react, etc.
- **Skill Areas**: testing, optimization, security, design
- **Problem Domains**: performance, scalability, user experience
- **Experience Levels**: junior, senior, expert, specialist
- **Cross-Domain Skills**: full-stack, devops, architecture

### Output Format
```
🔍 AGENT SEARCH: "database optimization"

Search Results: 4 agents found
Relevance Threshold: 75%
Search Scope: All agent categories

┌─ PRIMARY MATCHES (95%+ relevance) ──────────────────────┐
│                                                         │
│ ⚙️ backend-engineer                                     │
│    Relevance: 98%                                      │
│    Specialization: Database design, SQL optimization   │
│    Experience: 10+ years enterprise database systems   │
│    Key Skills:                                          │
│    • Advanced SQL query optimization                   │
│    • Database indexing strategies                      │
│    • Performance tuning and profiling                  │
│    • NoSQL and SQL database expertise                  │
│    Location: .claude/agents/core/development/          │
│    Current Status: Available                           │
│                                                         │
│ 📊 data-engineer                                        │
│    Relevance: 96%                                      │
│    Specialization: Big data, ETL pipelines, analytics  │
│    Experience: 8+ years data infrastructure            │
│    Key Skills:                                          │
│    • Large-scale data processing                       │
│    • Database performance optimization                 │
│    • Data pipeline optimization                        │
│    • Analytics database design                         │
│    Location: .claude/agents/core/data/                 │
│    Current Status: Available                           │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ SUPPORTING MATCHES (75-95% relevance) ─────────────────┐
│                                                         │
│ 🏗️ software-architect (87%)                            │
│    Focus: Database architecture design                 │
│    Skills: System-level optimization, scalability      │
│                                                         │
│ ⚡ performance-engineer (82%)                           │
│    Focus: Application performance optimization         │
│    Skills: Profiling, bottleneck analysis              │
│                                                         │
└─────────────────────────────────────────────────────────┘

💡 AGENT RECOMMENDATIONS:

For Your Current Project (book_writing_app):
┌─────────────────────────────────────────────────────────┐
│ 🎯 BEST MATCH: backend-engineer                         │
│                                                         │
│ Why this agent:                                         │
│ • Perfect fit for SQLite optimization                  │
│ • Extensive experience with desktop app databases      │
│ • Proven track record with Python + SQLite             │
│ • Can optimize export performance bottlenecks          │
│                                                         │
│ Recommended Tasks:                                      │
│ • Analyze current database query performance           │
│ • Implement indexing strategy for large documents      │
│ • Optimize export data retrieval                       │
│ • Setup performance monitoring                         │
│                                                         │
│ Collaboration Opportunities:                            │
│ • Work with qa-engineer on performance testing         │
│ • Coordinate with desktop-specialist on UI performance │
│ • Support software-architect with scalability planning │
└─────────────────────────────────────────────────────────┘

🔄 ALTERNATIVE SEARCH SUGGESTIONS:

Related Skills You Might Need:
• "performance optimization" → performance-engineer, backend-engineer
• "sql query tuning" → data-engineer, backend-engineer
• "database design" → software-architect, data-engineer
• "sqlite optimization" → backend-engineer (perfect match)

Broader Categories:
• "performance" → 6 agents with performance expertise
• "optimization" → 8 agents with optimization skills
• "database" → 4 agents with database specialization

🤖 AGENT ACTIVATION:

To work with backend-engineer:
1. Simply mention in conversation: "backend-engineer help with database optimization"
2. Use direct agent consultation: "/agent-handoff current backend-engineer"
3. Include in feature planning: "/start-feature 'Database Optimization' --agents=backend-engineer"

Agent Availability: ✅ AVAILABLE
Estimated Response Time: Immediate
Workload: Medium (good capacity for new tasks)

🔍 SEARCH TIPS:

More Specific Searches:
• Use quotes for exact phrases: "memory optimization"
• Combine skills: "python database performance"
• Specify experience level: "senior database architect"
• Technology-specific: "postgresql optimization"

Common Search Categories:
• Languages: python, cpp, javascript, rust, go
• Frameworks: react, django, wxpython, opengl
• Skills: testing, security, performance, design
• Domains: frontend, backend, database, devops
• Levels: junior, senior, lead, architect

✨ SEARCH COMPLETE!

Found: 4 relevant agents
Best Match: backend-engineer (98% relevance)
Ready for: Immediate collaboration
```

## Integration

- Agent competency database search
- Current project context awareness
- Agent availability checking
- Collaboration recommendations