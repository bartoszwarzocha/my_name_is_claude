# Troubleshooting Guide - My Name Is Claude

**Status:** Production Ready ✅

Comprehensive troubleshooting guide for resolving common issues with the Claude Code Multi-Agent Framework.

## 🎯 Overview

This guide provides systematic solutions for common issues with framework components including session management, agent activation, TodoWrite integration, and MCP tools coordination.

## 🔧 Session Management Issues

### Session Not Starting

**Symptoms:**
- Framework doesn't recognize project
- No agent recommendations provided
- Context analysis fails

**Diagnostic Steps:**
1. **Check CLAUDE.md exists and is valid**
   ```bash
   ls -la CLAUDE.md
   head -20 CLAUDE.md
   ```

2. **Verify project structure**
   ```bash
   ls -la .claude/
   find .claude/ -name "*.md" | head -10
   ```

3. **Check directory permissions**
   ```bash
   ls -la . | grep claude
   ```

**Solutions:**
- **Missing CLAUDE.md**: Create using `new-project.md` or `existing-project.md` prompts
- **Invalid CLAUDE.md**: Validate syntax and required sections
- **Permission issues**: Fix directory permissions with `chmod 755 .claude/`
- **Framework not detected**: Ensure `.claude/` directory exists with proper structure

### Context Recovery Failure

**Symptoms:**
- Previous work context not restored
- TODO progress lost
- Agent configurations reset

**Diagnostic Steps:**
1. **Check for session summary files**
   ```bash
   find . -name "SESSION_SUMMARY*.md" | head -5
   find . -name "*session*" -type f | head -10
   ```

2. **Verify .gitignore configuration**
   ```bash
   grep -E "(work/|session)" .gitignore
   ```

3. **Check temporary file locations**
   ```bash
   ls -la work/ 2>/dev/null || echo "Work directory not found"
   ```

**Solutions:**
- **Missing summaries**: Use `session-state-recovery.md` prompt for recovery
- **Gitignore issues**: Ensure temporary files aren't tracked in git
- **Manual restoration**: Restore from `SESSION_SUMMARY_CURRENT.md` if available
- **Complete rebuild**: Use `session-start-and-context-analysis.md` to rebuild context

### Serena Integration Issues

**Symptoms:**
- Serena commands not working
- Index updates failing
- Enhanced context not available

**Diagnostic Steps:**
1. **Check Serena directory**
   ```bash
   ls -la .serena/ 2>/dev/null || echo "Serena directory not found"
   ```

2. **Verify MCP tools installation**
   ```bash
   which serena 2>/dev/null || echo "Serena MCP not installed"
   ```

3. **Test basic Serena functionality**
   ```bash
   # Test if Serena responds (if installed)
   serena --version 2>/dev/null || echo "Serena not accessible"
   ```

**Solutions:**
- **Missing .serena directory**: Run Serena initialization if MCP tools are available
- **MCP tools not installed**: Framework works without Serena (graceful degradation)
- **Access issues**: Check Claude Code MCP configuration
- **Fallback mode**: Use standard session management without Serena enhancement

## 🤖 Agent Activation Issues

### Agent Not Activating

**Symptoms:**
- Prompts don't activate corresponding agents
- Generic responses instead of specialized agent behavior
- No agent-specific expertise applied

**Diagnostic Steps:**
1. **Verify prompt location**
   ```bash
   # Check if using agent-specific prompt from correct directory
   find .claude/prompts/agents/ -name "*.md" | grep [prompt-name]
   ```

2. **Check agent file exists**
   ```bash
   # Verify corresponding agent file exists
   find .claude/agents/ -name "*.md" | grep [agent-category]
   ```

3. **Validate prompt header**
   ```bash
   # Check for agent activation header in prompt
   head -10 .claude/prompts/agents/[category]/[prompt].md | grep "AGENT ACTIVATION"
   ```

**Solutions:**
- **Wrong directory**: Move prompt to correct `.claude/prompts/agents/[category]/` location
- **Missing agent**: Ensure corresponding agent exists in `.claude/agents/[category]/`
- **Incorrect header**: Add proper agent activation header to prompt
- **Manual activation**: Explicitly specify agent if automatic binding fails

### Agent Configuration Issues

**Symptoms:**
- Agent doesn't adapt to project technology stack
- Generic responses without project-specific context
- CLAUDE.md configuration ignored

**Diagnostic Steps:**
1. **Verify CLAUDE.md sections**
   ```bash
   grep -E "primary_language|business_domain|project_scale" CLAUDE.md
   ```

2. **Check agent CLAUDE.md integration**
   ```bash
   grep -i "claude.md" .claude/agents/[category]/[agent].md
   ```

3. **Validate project metadata**
   ```bash
   head -50 CLAUDE.md | grep -E "project_|primary_|business_"
   ```

**Solutions:**
- **Missing metadata**: Complete CLAUDE.md project metadata sections
- **Agent not reading config**: Ensure agent includes CLAUDE.md adaptation instructions
- **Invalid configuration**: Validate CLAUDE.md syntax and structure
- **Manual configuration**: Explicitly provide project context if automatic detection fails

## 📋 TodoWrite Integration Issues

### TODO Tasks Not Creating

**Symptoms:**
- Agents don't create TODO items automatically
- Manual TODO management required
- No task coordination between agents

**Diagnostic Steps:**
1. **Check TODO management configuration**
   ```bash
   grep -A 10 "TODO Management Configuration" CLAUDE.md
   ```

2. **Verify agent TODO integration**
   ```bash
   grep -i "todo" .claude/agents/[category]/[agent].md
   ```

3. **Check TodoWrite tool availability**
   ```bash
   # Verify TodoWrite is available in Claude Code environment
   echo "Check if TodoWrite tool is accessible in current session"
   ```

**Solutions:**
- **Enable TODO management**: Set `todo_management_enabled: true` in CLAUDE.md Section 8
- **Configure auto-creation**: Set `auto_task_creation: true` in configuration
- **Update agent prompts**: Ensure agents include TodoWrite integration
- **Manual TODO creation**: Use TodoWrite tool manually if automatic creation fails

### Agent Handoffs Not Working

**Symptoms:**
- Tasks don't transfer between agents
- No coordination in multi-agent workflows
- Duplicate or conflicting work

**Diagnostic Steps:**
1. **Check coordination configuration**
   ```bash
   grep -E "(agent_coordination|task_handoffs)" CLAUDE.md
   ```

2. **Verify agent responsibility matrix**
   ```bash
   grep -A 20 "Agent TODO Responsibilities" CLAUDE.md
   ```

3. **Check for handoff protocols**
   ```bash
   find .claude/ -name "*handoff*" -o -name "*coordination*"
   ```

**Solutions:**
- **Enable coordination**: Set `agent_coordination: true` in CLAUDE.md
- **Configure handoffs**: Set `task_handoffs: true` in configuration
- **Review responsibility matrix**: Ensure clear agent ownership assignments
- **Manual coordination**: Explicitly coordinate agent transitions if automatic handoffs fail

### Hierarchy Levels Not Recognized

**Symptoms:**
- Flat TODO structure instead of hierarchical
- No Epic/Feature/Task/Subtask organization
- Limited project organization capabilities

**Diagnostic Steps:**
1. **Check hierarchy configuration**
   ```bash
   grep -E "(todo_hierarchy_level|epic_management|feature_breakdown)" CLAUDE.md
   ```

2. **Verify project scale setting**
   ```bash
   grep "project_scale" CLAUDE.md
   ```

3. **Check for hierarchy support**
   ```bash
   grep -E "(Epic|Feature|Task|Subtask)" CLAUDE.md
   ```

**Solutions:**
- **Enable hierarchy**: Set `todo_hierarchy_level: hierarchical` in CLAUDE.md
- **Configure Epic support**: Set `epic_management: true` for Epic-level planning
- **Enable Feature breakdown**: Set `feature_breakdown: true` for Feature organization
- **Update project scale**: Use appropriate scale (startup/sme/enterprise) for complexity level

## 🔗 Framework Integration Issues

### MCP Tools Integration

**Symptoms:**
- MCP tools not available
- Limited context analysis capabilities
- Basic session management only

**Diagnostic Steps:**
1. **Check MCP tools installation**
   ```bash
   # Look for MCP-related directories or tools
   ls -la | grep -E "(serena|context7|playwright)"
   ```

2. **Verify Claude Code MCP configuration**
   ```bash
   # Check Claude Code settings for MCP integration
   echo "Check Claude Code settings for MCP tools configuration"
   ```

**Solutions:**
- **Install MCP tools**: Follow MCP tools installation guide if needed
- **Configure Claude Code**: Enable MCP tools in Claude Code settings
- **Graceful degradation**: Framework works without MCP tools (reduced functionality)
- **Manual alternatives**: Use manual project analysis if MCP tools unavailable

### Directory Structure Issues

**Symptoms:**
- Framework components not found
- Broken internal links
- Missing prompt or agent files

**Diagnostic Steps:**
1. **Verify framework structure**
   ```bash
   tree .claude/ -L 3 2>/dev/null || find .claude/ -type d | sort
   ```

2. **Check for missing components**
   ```bash
   ls -la .claude/agents/ .claude/prompts/ .claude/hooks/
   ```

3. **Validate file integrity**
   ```bash
   find .claude/ -name "*.md" -exec wc -l {} \; | sort -n
   ```

**Solutions:**
- **Restore missing directories**: Recreate standard framework structure
- **Repair broken links**: Update internal documentation links
- **Reinstall framework**: Use `existing-project.md` to restore framework integration
- **Validate structure**: Ensure all required components are present

## 🚀 Performance Optimization

### Large Project Performance

**Symptoms:**
- Slow context loading
- Long session startup times
- Memory usage issues

**Optimization Strategies:**
1. **Reduce context depth**
   ```yaml
   # In CLAUDE.md
   context_depth: focused  # instead of comprehensive
   ```

2. **Limit TODO granularity**
   ```yaml
   # In CLAUDE.md
   task_granularity: standard  # instead of detailed
   ```

3. **Selective agent activation**
   ```yaml
   # Only activate required agents
   auto_agent_activation: selective  # instead of comprehensive
   ```

### Distributed Team Performance

**Symptoms:**
- Session conflicts
- Coordination overhead
- Context synchronization issues

**Optimization Strategies:**
1. **Configure team settings**
   ```yaml
   # In CLAUDE.md
   team_coordination: enabled
   session_sharing: true
   conflict_resolution: automatic
   ```

2. **Use centralized session storage**
   ```yaml
   # Configure shared session management
   session_storage: centralized
   backup_frequency: hourly
   ```

## 📊 Diagnostic Commands

### Framework Health Check

```bash
#!/bin/bash
# Framework diagnostic script

echo "=== My Name Is Claude Diagnostic ==="

echo "1. Checking CLAUDE.md..."
[[ -f "CLAUDE.md" ]] && echo "✅ CLAUDE.md exists" || echo "❌ CLAUDE.md missing"

echo "2. Checking framework structure..."
[[ -d ".claude" ]] && echo "✅ .claude directory exists" || echo "❌ .claude directory missing"

echo "3. Checking agents..."
agent_count=$(find .claude/agents/ -name "*.md" 2>/dev/null | wc -l)
echo "📊 Found $agent_count agent files"

echo "4. Checking prompts..."
prompt_count=$(find .claude/prompts/ -name "*.md" 2>/dev/null | wc -l)
echo "📊 Found $prompt_count prompt files"

echo "5. Checking MCP integration..."
[[ -d ".serena" ]] && echo "✅ Serena MCP available" || echo "ℹ️ Serena MCP not detected (optional)"

echo "6. Checking TODO configuration..."
grep -q "todo_management_enabled: true" CLAUDE.md 2>/dev/null &&
  echo "✅ TODO management enabled" || echo "⚠️ TODO management not configured"

echo "=== Diagnostic Complete ==="
```

### Quick Fix Script

```bash
#!/bin/bash
# Quick framework repair script

echo "=== Framework Quick Fix ==="

# Fix directory permissions
chmod -R 755 .claude/ 2>/dev/null && echo "✅ Fixed .claude permissions"

# Create work directory if missing
mkdir -p work/ && echo "✅ Created work directory"

# Verify CLAUDE.md structure
if [[ -f "CLAUDE.md" ]]; then
    grep -q "## 8. TODO Management Configuration" CLAUDE.md ||
      echo "⚠️ CLAUDE.md missing TODO configuration section"
fi

# Check for session files
session_files=$(find . -name "SESSION_SUMMARY*.md" 2>/dev/null | wc -l)
echo "📊 Found $session_files session summary files"

echo "=== Quick Fix Complete ==="
```

## 🆘 Emergency Recovery

### Complete Framework Reset

If framework is severely corrupted:

1. **Backup current state**
   ```bash
   cp -r .claude/ .claude_backup_$(date +%Y%m%d)
   cp CLAUDE.md CLAUDE_backup_$(date +%Y%m%d).md
   ```

2. **Use existing-project.md prompt**
   - Reinstall framework integration
   - Regenerate CLAUDE.md if needed
   - Restore agent-prompt binding

3. **Restore session context**
   - Use `session-state-recovery.md` prompt
   - Manually reconstruct recent work if needed
   - Rebuild TODO hierarchy

### Contact and Support

For complex issues beyond this troubleshooting guide:

1. **Check framework documentation** - Complete docs in `docs/` directory
2. **Review agent-specific documentation** - Individual agent capabilities
3. **Verify latest framework version** - Ensure using current release
4. **Framework community resources** - Additional troubleshooting resources

---

**See also:**
- [Session Management](../core-features/session-management.md) - Detailed session troubleshooting
- [Agent System](../core-features/agent-system.md) - Agent activation and coordination
- [TODO Management](../core-features/todo-management.md) - TodoWrite integration issues