# Agent Expertise Command

**Command**: `/agent-expertise [domain]`
**Category**: Agent Management
**Description**: Znajdź ekspertów w określonej dziedzinie

## Usage

```
/agent-expertise opengl
/agent-expertise "database design"
/agent-expertise security
/agent-expertise "performance optimization"
```

## Functionality

Searches through all available agents to find specialists in specific domains or technologies.

### Search Domains
- **Technologies**: python, cpp, javascript, opengl, vulkan, etc.
- **Specializations**: security, performance, testing, deployment
- **Business Areas**: fintech, healthcare, ecommerce, enterprise
- **Methodologies**: agile, devops, microservices, clean-architecture

### Agent Analysis
- Scans agent competency definitions
- Analyzes experience levels and specializations
- Ranks by expertise depth and relevance
- Includes cross-domain capabilities

### Output Format
```
🔍 EXPERTISE SEARCH: "opengl"

Primary Experts (10+ years):
┌─────────────────────────────────────────────────────────┐
│ 🎮 graphics-3d-engineer                                 │
│    • OpenGL 4.5+ Core Profile (Expert)                 │
│    • Modern Shader Pipeline (Expert)                   │
│    • GPU Optimization (Advanced)                       │
│    • Location: .claude/agents/custom/graphics/         │
│                                                         │
│ 🧮 math-specialist                                      │
│    • 3D Mathematics for OpenGL (Expert)                │
│    • Matrix Transformations (Expert)                   │
│    • Computational Geometry (Advanced)                 │
│    • Location: .claude/agents/custom/graphics/         │
└─────────────────────────────────────────────────────────┘

Supporting Experts (5+ years):
• desktop-specialist - OpenGL integration with wxWidgets
• software-architect - Graphics architecture patterns

Recommended Coordination:
Primary: graphics-3d-engineer
Mathematical Support: math-specialist
Integration: desktop-specialist
Architecture: software-architect
```

## Advanced Features

### Cross-Domain Search
```
/agent-expertise "python gui performance"
```

### Minimum Experience Filter
```
/agent-expertise security --min-experience=senior
```

### Project Context Integration
Automatically considers current project's CLAUDE.md configuration to prioritize relevant expertise.

## Integration

- Agent competency database
- Project technology stack analysis
- Multi-agent workflow planning
- Knowledge base integration