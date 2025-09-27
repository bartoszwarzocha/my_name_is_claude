# Framework Restore Command

**Command**: `/framework-restore [backup-id]`
**Category**: Framework Management
**Description**: Restore z backup frameworka

## Usage

```
/framework-restore fw-backup-a7f8d9e2
/framework-restore --latest
/framework-restore --list
/framework-restore --preview fw-backup-a7f8d9e2
```

## Functionality

Restores framework configuration from specified backup, with options for selective restoration and preview.

### Restoration Process
1. **Backup Validation**: Verify backup integrity
2. **Current State Backup**: Create safety backup before restore
3. **Selective Restoration**: Choose components to restore
4. **Configuration Merge**: Handle conflicts intelligently
5. **Agent Reactivation**: Restore agent states
6. **Validation**: Verify restoration success

### Output Format
```
🔄 FRAMEWORK RESTORATION

Backup ID: fw-backup-a7f8d9e2
Created: 2025-09-27 10:15:30
Size: 4.8 MB (15.2 MB uncompressed)
Integrity: ✅ VERIFIED

📋 RESTORATION PREVIEW:

Will Restore:
✅ Framework core files (.claude/, .ai-tools/)
✅ Agent configurations (12 agents)
✅ Custom prompts and hooks (8 custom items)
✅ Quality validation rules
✅ MCP Tools settings

Will Preserve (Current):
⚠️ CLAUDE.md (Modified since backup)
⚠️ Active TodoWrite sessions
⚠️ Recent agent contexts

Conflicts Detected:
🔄 Agent assignment changes (Auto-merge available)
🔄 Custom hook modifications (Manual review suggested)

[1/6] 💾 Creating safety backup...
✅ Current state backed up: safety-backup-20250927-123045

[2/6] 📦 Extracting backup...
✅ Backup extracted successfully
✅ File integrity verified

[3/6] 🔄 Restoring framework components...
✅ Core framework files restored
✅ Agent definitions loaded
✅ Tool configurations applied

[4/6] ⚙️ Resolving conflicts...
✅ Agent assignments merged automatically
⚠️ Custom hook conflicts require review
✅ Configuration overrides applied

[5/6] 🤖 Reactivating agents...
✅ Agent system reinitialized
✅ Agent contexts restored
✅ Multi-agent coordination resumed

[6/6] 🔍 Validating restoration...
✅ Framework integrity confirmed
✅ Agent functionality verified
✅ Tool integration operational

✨ RESTORATION COMPLETE!

Restored Components: 89 files
Merged Configurations: 3 items
Conflicts Resolved: 2 automatic, 1 manual review needed
Status: 🟢 SUCCESS

⚠️ MANUAL REVIEW REQUIRED:
• Custom hook in .claude/hooks/pre-commit-custom.sh
• Review and resolve conflicts manually

Next Steps:
• Review manual conflicts
• Run /ai-validate to verify functionality
• Test agent operations
```

## Options

### `--latest`
Restore from most recent backup

### `--list`
List all available backups for restoration

### `--preview [backup-id]`
Preview restoration without applying changes

### `--selective`
Choose specific components to restore

## Integration

- Backup system integration
- Conflict resolution system
- Agent state management
- Validation framework