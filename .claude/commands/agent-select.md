# Agent Selection Command

**Command**: `/agent-select [technology]`
**Category**: Agent Management
**Description**: Automatyczny dobór agentów na podstawie stacku technologicznego

## Usage

```
/agent-select python
/agent-select "wxpython opengl"
/agent-select cpp
/agent-select "react typescript"
```

## Functionality

Analyzes the specified technology stack and automatically recommends the most suitable agents from the framework's agent pool.

### Technology Detection
- **Python Stack**: backend-engineer, qa-engineer
- **Desktop GUI**: desktop-specialist, ux-designer
- **Graphics/3D**: graphics-3d-engineer, math-specialist
- **C++**: backend-engineer, software-architect
- **Web Frontend**: frontend-engineer, ux-designer
- **Databases**: data-engineer, backend-engineer
- **DevOps**: deployment-engineer, sre-engineer

### Agent Pool Analysis
1. Scans `.claude/agents/` directory
2. Matches technology keywords with agent competencies
3. Ranks agents by relevance score
4. Provides coordination recommendations

### Output Format
```
🤖 AGENT SELECTION RESULTS

Technology Stack: [detected technologies]

Primary Agents:
• [agent-name] - [specialization] (Relevance: 95%)
• [agent-name] - [specialization] (Relevance: 87%)

Supporting Agents:
• [agent-name] - [specialization] (Relevance: 72%)

Coordination Pattern:
[recommended workflow between agents]
```

## Integration

- Integrates with CLAUDE.md project configuration
- Uses TodoWrite for agent task assignment
- Supports multi-agent workflow coordination
- Compatible with AI-Tools agent discovery system

## Examples

### Python Desktop Application
```
/agent-select "python wxpython sqlite"

Results:
• desktop-specialist (Primary - wxPython expertise)
• backend-engineer (Core - Python + SQLite)
• software-architect (Strategic - Application design)
• qa-engineer (Quality - Testing strategy)
```

### C++ Graphics SDK
```
/agent-select "cpp opengl wxwidgets"

Results:
• graphics-3d-engineer (Primary - OpenGL expertise)
• desktop-specialist (Core - wxWidgets)
• backend-engineer (Core - C++ development)
• math-specialist (Supporting - 3D mathematics)
```