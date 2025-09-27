# Framework Backup Command

**Command**: `/framework-backup`
**Category**: Framework Management
**Description**: Backup aktualnej konfiguracji frameworka

## Usage

```
/framework-backup
/framework-backup --name="pre-update-backup"
/framework-backup --compress
/framework-backup --cloud
```

## Functionality

Creates comprehensive backup of current framework configuration, agent settings, and project-specific customizations.

### Backup Components
- Framework configuration files
- Agent definitions and assignments
- Custom prompts and hooks
- AI Tools configuration
- MCP Tools settings
- Quality validation rules
- Project-specific overrides

### Output Format
```
💾 FRAMEWORK BACKUP

Project: book_writing_app
Backup Type: Complete Framework State
Compression: Enabled

📦 BACKUP CONTENTS:

Framework Core:
✅ .claude/ directory (45 files)
✅ .ai-tools/ configuration (12 files)
✅ .mcp-tools/ settings (3 files)
✅ Framework scripts and utilities

Project Configuration:
✅ CLAUDE.md with customizations
✅ Agent assignments and overrides
✅ Custom hooks and automation
✅ Quality gate configurations

Session State:
✅ Active agent contexts
✅ TodoWrite hierarchies
✅ Workflow configurations
✅ Performance baselines

📊 BACKUP STATISTICS:

Total Files: 127
Total Size: 15.2 MB
Compressed Size: 4.8 MB
Compression Ratio: 68.5%

💾 BACKUP CREATED:

Location: .framework-backups/backup-20250927-123045.tar.gz
Backup ID: fw-backup-a7f8d9e2
Created: 2025-09-27 12:30:45
Integrity: ✅ VERIFIED

✨ BACKUP COMPLETE!

Backup Details:
• Full framework state preserved
• Project customizations included
• Restoration ready
• Integrity verified

Commands:
• Restore: /framework-restore fw-backup-a7f8d9e2
• List backups: /framework-backup --list
• Verify: /framework-backup --verify fw-backup-a7f8d9e2
```

## Options

### `--name="custom-name"`
Specify custom backup name

### `--compress`
Enable compression for smaller backup size

### `--list`
List all available backups

### `--verify [backup-id]`
Verify backup integrity

## Integration

- Automatic backup before updates
- Version control integration
- Cloud storage support
- Restoration system integration