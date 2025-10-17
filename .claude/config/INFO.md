# Configuration Systems - Quick Reference

**Version:** 3.9.0

## Configuration Files Overview

This directory contains configuration architectures and specifications for advanced Claude Code framework features:

- **model-profiles.json** - Three-tier model selection system (Fast/Balanced/Quality)
- **agent-model-mapping.json** - Agent-to-model profile mappings for all 45 agents
- **cost-optimization.json** - Budget tracking and cost optimization settings
- **output-styles.json** - Four communication styles (Technical/Executive/Educational/Code Review)
- **checkpoint-system.json** - Multi-level checkpoint system architecture
- **parallel-agents.json** - Parallel agent execution framework with team definitions
- **extended-thinking-config.json** - Extended Thinking Mode trigger conditions and configuration (NEW in 3.9.0)
- **diagnostic-framework-integration.json** - Extended Thinking integration with quality gates and diagnostics (NEW in 3.9.0)

## 📖 Complete Documentation

**For comprehensive guide, examples, and usage instructions:**

→ **[v3.3.0 Features Guide](../../docs/getting-started/v3.3.0-features-guide.md)**

This guide includes:
- Detailed feature descriptions
- How to use NOW vs. Future automatic implementation
- Testing & validation instructions
- FAQ and quick reference
- Cost calculation examples

## Quick Access

**Test & Validate:**
```bash
# Run comprehensive tests
./work/model-config-tests/test-suite.sh

# View usage examples
./work/model-config-tests/usage-examples.sh

# Calculate costs
./work/model-config-tests/cost-calculator.sh
```

**Learn More:**
- [Extended Thinking Mode Guide](../../docs/advanced/extended-thinking-mode.md) - Deep reasoning for complex decisions (NEW in 3.9.0)
- [CHANGELOG.md](../../CHANGELOG.md) - v3.3.0 release notes
- [FRAMEWORK_ROADMAP.md](../../FRAMEWORK_ROADMAP.md) - Roadmap and future plans
