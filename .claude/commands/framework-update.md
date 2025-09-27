# Framework Update Command

**Command**: `/framework-update`
**Category**: Framework Management
**Description**: Update frameworka w projekcie

## Usage

```
/framework-update
/framework-update --check-only
/framework-update --force
/framework-update --backup
```

## Functionality

Updates framework components in current project to latest version from main framework repository.

### Update Process
1. **Version Check**: Compare current vs latest framework version
2. **Backup Creation**: Automatic backup of current configuration
3. **Component Update**: Update framework files selectively
4. **Configuration Migration**: Migrate CLAUDE.md and settings
5. **Agent Update**: Update agent definitions and capabilities
6. **Validation**: Verify update success and compatibility

### Output Format
```
🔄 FRAMEWORK UPDATE

Current Version: 3.1.0
Latest Version: 3.2.0
Update Available: YES

📊 UPDATE ANALYSIS:

Components to Update:
• 🤖 AI Tools core (3.1.0 → 3.2.0)
• 🔌 MCP Tools integration (2.0.0 → 2.1.0)
• 👥 Agent definitions (5 agents updated)
• 📋 Quality tools (Enhanced validation)
• 🔧 Framework utilities (Performance improvements)

Breaking Changes: None
Migration Required: Automatic

[1/6] 💾 Creating backup...
✅ Backup created: .framework-backup-20250927-123045/

[2/6] 📦 Downloading updates...
✅ Framework components downloaded
✅ Agent updates retrieved
✅ Tool updates ready

[3/6] 🔄 Updating components...
✅ AI Tools updated to v3.2.0
✅ MCP Tools updated to v2.1.0
✅ Agent definitions refreshed
✅ Quality tools enhanced

[4/6] ⚙️ Migrating configuration...
✅ CLAUDE.md preserved
✅ Custom settings migrated
✅ Agent assignments maintained

[5/6] 🔍 Validating update...
✅ Framework integrity verified
✅ Agent functionality confirmed
✅ Tool integration validated

[6/6] 🎉 Finalizing update...
✅ Cache cleared
✅ Dependencies updated
✅ Update log created

✨ UPDATE COMPLETE!

Framework Version: 3.2.0
Update Status: 🟢 SUCCESS
Backup Location: .framework-backup-20250927-123045/

🎆 NEW FEATURES:
• Enhanced agent coordination algorithms
• Improved performance monitoring
• Advanced quality validation rules
• Extended MCP tools support
• Better cross-platform compatibility

Next Steps:
• Run `/ai-validate` to verify functionality
• Review new features documentation
• Consider testing new agent capabilities
```

## Options

### `--check-only`
Checks for updates without applying them

### `--force`
Forces update even if no version change detected

### `--backup`
Creates backup even for minor updates

## Integration

- Framework version management
- Automatic backup system
- Configuration migration
- Agent definition updates