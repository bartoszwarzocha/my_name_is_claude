# AI Setup Command

**Command**: `/ai-setup`
**Category**: AI-Tools Shortcuts
**Description**: Szybki setup AI tools bez interaktywnego menu

## Usage

```
/ai-setup
/ai-setup --force
/ai-setup --minimal
/ai-setup --advanced
```

## Functionality

Automatically configures AI Tools environment without requiring manual menu navigation.

### Setup Process
1. **Environment Validation**: Check Python, venv requirements
2. **Virtual Environment**: Create `.ai-tools/venv/` if needed
3. **Dependencies Installation**: Install required Python packages
4. **Agent Discovery**: Analyze CLAUDE.md and detect appropriate agents
5. **MCP Tools**: Basic MCP tools configuration
6. **Quality Gates**: Setup basic quality validation

### Output Format
```
🤖 AI TOOLS AUTOMATIC SETUP

Project: book_writing_app
Target: Full AI Tools Environment

[1/6] 🔍 Environment Validation...
✅ Python 3.9+ detected
✅ Virtual environment support available
✅ Required system packages present

[2/6] 🐍 Creating Virtual Environment...
✅ Virtual environment created at .ai-tools/venv/
✅ Virtual environment activated

[3/6] 📦 Installing Dependencies...
✅ Installing core AI tools packages...
✅ Installing project-specific packages...
✅ Installing quality tools...

[4/6] 🤖 Agent Discovery...
✅ CLAUDE.md analyzed
✅ Technology stack detected: Python, wxPython, SQLite
✅ Agents configured:
   • desktop-specialist (Primary)
   • backend-engineer (Core)
   • software-architect (Strategic)
   • qa-engineer (Quality)

[5/6] 🔌 MCP Tools Configuration...
✅ Basic MCP tools configured
✅ Serena project indexing ready
✅ Context7 analysis tools ready

[6/6] 🔍 Quality Gates Setup...
✅ Code quality tools configured
✅ Testing framework hooks installed
✅ Pre-commit hooks ready

✨ SETUP COMPLETE!

AI Tools Status: 🟢 FULLY OPERATIONAL
Active Agents: 4
MCP Tools: 2 configured
Quality Gates: Active

Next Steps:
• Run `/ai-validate` to verify setup
• Start development with agent assistance
• Use `/health-check` for ongoing monitoring
```

## Options

### `--force`
Overwrites existing configuration without prompts

### `--minimal`
Installs only essential components for basic functionality

### `--advanced`
Includes advanced features like performance monitoring, security scanning

## Integration

- ai-tools.sh automation
- CLAUDE.md configuration reading
- Automatic agent selection
- MCP tools integration
- Quality tools configuration