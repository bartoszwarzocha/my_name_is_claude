# Framework Sync Command

**Command**: `/framework-sync`
**Category**: Framework Management
**Description**: Sync z głównym framework repo

## Usage

```
/framework-sync
/framework-sync --pull-only
/framework-sync --agents-only
/framework-sync --dry-run
```

## Functionality

Synchronizes project framework with main framework repository, updating agents, prompts, and tools while preserving project-specific configurations.

### Sync Components
- **Agent Definitions**: Latest agent capabilities and competencies
- **Prompt Library**: New and updated prompts
- **Framework Tools**: Core utilities and helpers
- **Quality Standards**: Updated validation rules
- **Documentation**: Framework documentation updates

### Output Format
```
🔄 FRAMEWORK SYNCHRONIZATION

Source: /mnt/e/AI/my_name_is_claude (Main Framework)
Target: Current Project
Sync Strategy: Selective (Preserve project config)

📊 SYNC ANALYSIS:

Changes Available:
• 🤖 3 agent definitions updated
• 📝 5 new prompts available
• 🔧 2 tool enhancements
• 📚 Documentation updates

Project-Specific (Preserved):
• ✅ CLAUDE.md configuration
• ✅ Custom agent assignments
• ✅ Local settings and overrides
• ✅ Project-specific hooks

🔄 SYNCHRONIZING:

[1/4] 🤖 Syncing agent definitions...
✅ graphics-3d-engineer updated (Enhanced OpenGL support)
✅ math-specialist updated (New algorithms)
✅ qa-engineer updated (Additional testing strategies)

[2/4] 📝 Syncing prompt library...
✅ 5 new prompts added to collection
✅ 3 existing prompts enhanced
✅ Prompt categories reorganized

[3/4] 🔧 Syncing framework tools...
✅ AI Tools performance improvements
✅ MCP integration enhancements

[4/4] 📚 Syncing documentation...
✅ Framework documentation updated
✅ Agent usage guides refreshed

✨ SYNC COMPLETE!

Updated Components: 13
Preserved Configurations: 8
Sync Status: 🟢 SUCCESS

Next Steps:
• Review updated agent capabilities
• Explore new prompt library additions
• Test enhanced framework tools
```

## Integration

- Git-based synchronization
- Selective component updates
- Configuration preservation
- Version conflict resolution