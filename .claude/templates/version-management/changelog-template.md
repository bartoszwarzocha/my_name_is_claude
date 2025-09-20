# CHANGELOG Entry Template

## 📝 Standard Changelog Entry Format

```markdown
## [X.X.X] - YYYY-MM-DD

### Added
- New feature or component descriptions
- New agents, tools, or capabilities
- New documentation sections

### Changed
- Modifications to existing features
- Updated documentation or templates
- Improved processes or workflows

### Fixed
- Bug fixes and error corrections
- Documentation corrections
- Setup or configuration fixes

### Removed
- Deprecated features or components
- Obsolete documentation
- Unused files or configurations

### Infrastructure
- Version updates and maintenance
- Build system changes
- Development process improvements
```

## 🎯 Category Guidelines

### **Added** 📦
**Use for:**
- New agents or specializations
- New features or capabilities
- New documentation sections
- New templates or examples
- New tools or integrations

**Examples:**
```markdown
### Added
- New `graphics-3d-engineer` agent for OpenGL/Vulkan development
- AI-powered agent selection system with intelligent recommendations
- Comprehensive MCP Tools Manager documentation
- Interactive framework setup wizard for zero-configuration deployment
```

### **Changed** 🔄
**Use for:**
- Improvements to existing features
- Updated documentation or content
- Modified templates or configurations
- Enhanced workflows or processes

**Examples:**
```markdown
### Changed
- Enhanced agent competency descriptions for better clarity
- Updated framework installation documentation with troubleshooting
- Improved README.md structure and navigation
- Optimized TodoWrite integration for better task tracking
```

### **Fixed** 🐛
**Use for:**
- Bug fixes and error corrections
- Documentation corrections
- Setup or installation issues
- Configuration problems

**Examples:**
```markdown
### Fixed
- Empty screen issue in MCP Tools Manager menu options
- Missing extended.json file in home directory setup
- Broken documentation links in agent reference
- Version synchronization across README.md and CLAUDE.md
```

### **Removed** 🗑️
**Use for:**
- Deprecated or obsolete features
- Unused files or directories
- Outdated documentation
- Legacy components

**Examples:**
```markdown
### Removed
- Deprecated agent templates from v2.x
- Obsolete docs_backup directory from repository
- Legacy configuration files no longer used
- Outdated installation scripts
```

### **Infrastructure** 🔧
**Use for:**
- Version management and maintenance
- Development process changes
- Build system updates
- Repository organization

**Examples:**
```markdown
### Infrastructure
- Updated version management system with automated validation
- Standardized commit message format across repository
- Improved git workflow with proper branch management
- Enhanced documentation organization and structure
```

## 📋 Template Examples by Version Type

### PATCH Release Example (3.0.0 → 3.0.1)
```markdown
## [3.0.1] - 2025-09-20

### Added
- Comprehensive MCP Tools Manager user guide with setup instructions
- Troubleshooting section for common MCP tools installation issues

### Fixed
- Empty screen issue in mcp-tools.sh menu due to missing registry file
- Setup instructions for proper MCP tools configuration

### Infrastructure
- Documentation improvements for user setup experience
- No code changes - configuration and documentation only
```

### MINOR Release Example (3.0.1 → 3.1.0)
```markdown
## [3.1.0] - 2025-09-25

### Added
- New `ai-workflow-optimizer` agent for intelligent task automation
- Interactive project analysis tool with technology detection
- Enhanced agent selection system with confidence scoring

### Changed
- Improved framework setup wizard with better user guidance
- Updated agent competency matrix for clearer role definitions
- Enhanced TodoWrite integration with hierarchical task management

### Fixed
- Agent selection algorithm accuracy improvements
- Documentation synchronization across multiple README files

### Infrastructure
- Automated version management system with validation scripts
- Standardized release process with comprehensive checklists
```

### MAJOR Release Example (3.1.0 → 4.0.0)
```markdown
## [4.0.0] - 2025-10-15

### Added
- Revolutionary AI-driven code generation with context awareness
- Real-time collaboration system for multi-developer teams
- Advanced security framework with automated vulnerability scanning

### Changed
- **BREAKING**: New CLAUDE.md specification format (v4.0)
- **BREAKING**: Restructured agent system with new competency model
- **BREAKING**: Updated prompt format for improved AI interaction

### Fixed
- Complete overhaul of session management for improved reliability
- Enhanced error handling across all framework components

### Removed
- **BREAKING**: Deprecated v3.x agent format no longer supported
- **BREAKING**: Legacy configuration files removed
- Obsolete documentation and examples from v3.x

### Infrastructure
- Complete framework architecture redesign for scalability
- New testing framework with comprehensive validation
- Migration tools for upgrading from v3.x to v4.0
```

## ✅ Changelog Quality Checklist

- [ ] **Clear categorization** - Each item in appropriate section
- [ ] **User-focused language** - Describes impact, not implementation
- [ ] **Consistent formatting** - Following established patterns
- [ ] **Complete coverage** - All significant changes included
- [ ] **Breaking changes marked** - Use **BREAKING** prefix for major versions
- [ ] **Date format** - YYYY-MM-DD format
- [ ] **Version format** - [X.X.X] with brackets
- [ ] **Grammar and spelling** - Professional presentation

## 🚫 What NOT to Include

- Internal code refactoring without user impact
- Minor typo fixes (unless significant)
- Development debugging or testing changes
- Personal notes or temporary modifications
- Implementation details users don't need

---

**Framework Rule:** Use this template for all CHANGELOG.md entries to maintain consistency and provide clear communication to users about framework evolution.