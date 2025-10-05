# Output Styles System

**Part of Claude Code Multi-Agent Framework v3.7.0**

Context-aware communication style system that automatically adapts Claude's output to match the audience, task type, and agent context. Ensures optimal communication with technical teams, executives, learners, and code reviewers.

## 🎯 Overview

The Output Styles System provides 4 professionally designed communication styles that automatically adapt based on context. Whether you're explaining code to developers, presenting to executives, teaching newcomers, or reviewing pull requests - the right style is automatically selected.

### Available Styles

| Style | Audience | Characteristics | Use Cases |
|-------|----------|----------------|-----------|
| **Technical** | Developers, Engineers | Detailed, code-first, high technicality | Implementation, architecture, debugging |
| **Executive** | C-level, Managers | Concise, business-focused, ROI-oriented | Status reports, strategic decisions, budgets |
| **Educational** | Learners, Junior Devs | Step-by-step, explanatory, encouraging | Tutorials, concept explanations, onboarding |
| **Code Review** | Reviewers, QA | Actionable, severity-based, constructive | PR reviews, quality assessment, audits |

## 🚀 Quick Start

### Automatic Style Selection

```python
from output_styles import OutputStylesManager, StyleContext, OutputStyle

# Initialize
manager = OutputStylesManager()

# Context-aware selection
context = StyleContext(
    agent_type="backend-engineer",
    audience="developer",
    task_type="implementation"
)

# Automatically selects appropriate style
style = manager.select_style(context)
# Returns: OutputStyle.TECHNICAL
```

### Generate Style Prompt

```python
# Get style-specific prompt for Claude
prompt = manager.get_style_prompt(OutputStyle.TECHNICAL)

# Or generate complete context-aware prompt
full_prompt = manager.generate_context_prompt(context)
```

## 📋 Style Descriptions

### 1. Technical Style

**Target Audience:** Developers, Engineers, Technical Leads

**Characteristics:**
- **Verbosity:** Detailed
- **Technicality:** High
- **Code Examples:** Abundant
- **Formality:** Informal

**Communication Patterns:**
- Bottom-up explanation style
- Comprehensive detail level
- Assumes high technical knowledge
- Encourages technical jargon
- Step-by-step implementation

**Content Guidelines:**
- ✅ Include: Code snippets, architecture diagrams, performance metrics
- ❌ Exclude: Business value, ROI, timelines

**Example Scenarios:**
- Code implementation explanation
- Technical architecture documentation
- API integration guide
- Performance optimization analysis
- Debugging walkthrough
- Algorithm explanation

### 2. Executive Style

**Target Audience:** Executives, Managers, Stakeholders, Business Owners

**Characteristics:**
- **Verbosity:** Concise
- **Technicality:** Low
- **Code Examples:** None
- **Formality:** Formal

**Communication Patterns:**
- Top-down explanation style
- High-level detail
- Assumes minimal technical knowledge
- Avoids technical jargon
- Direct to conclusions

**Content Guidelines:**
- ✅ Include: Business value, ROI, timelines, risk analysis, resources
- ❌ Exclude: Code snippets, architecture diagrams, technical metrics

**Example Scenarios:**
- Project status report
- Budget justification
- Strategic technology decisions
- Risk assessment summary
- ROI analysis
- Quarterly review

### 3. Educational Style

**Target Audience:** Learners, Students, Junior Developers, Newcomers

**Characteristics:**
- **Verbosity:** Expansive
- **Technicality:** Progressive (starts simple, builds up)
- **Code Examples:** Abundant with explanations
- **Formality:** Friendly

**Communication Patterns:**
- Scaffolded explanation style
- Comprehensive detail with context
- Assumes low technical knowledge
- Explains all jargon
- Step-by-step with encouragement

**Content Guidelines:**
- ✅ Include: Code snippets, diagrams, prerequisites, learning objectives, practice exercises, common mistakes
- ❌ Exclude: Performance metrics, business value, ROI

**Example Scenarios:**
- Getting started tutorial
- Concept explanation
- Best practices guide
- Troubleshooting guide
- Framework overview
- Technology comparison

### 4. Code Review Style

**Target Audience:** Developers, Code Reviewers, Quality Engineers

**Characteristics:**
- **Verbosity:** Minimal
- **Technicality:** High
- **Code Examples:** Targeted (before/after)
- **Formality:** Professional

**Communication Patterns:**
- Direct explanation style
- Precise detail level
- Assumes high technical knowledge
- Uses standard technical terms
- Constructive tone

**Content Guidelines:**
- ✅ Include: Code snippets, performance metrics, severity levels, recommendations, alternatives
- ❌ Exclude: Architecture diagrams, business value, ROI

**Severity Levels:**
- **Critical:** Security vulnerabilities, data loss risks, system crashes
- **Major:** Performance issues, architectural problems, maintainability concerns
- **Minor:** Code style, naming conventions, documentation improvements
- **Suggestion:** Optimization opportunities, alternative approaches

**Example Scenarios:**
- Pull request review
- Code quality assessment
- Security audit
- Performance review
- Best practices validation
- Refactoring suggestions

## 🎯 Context-Aware Selection

The system automatically selects the appropriate style based on context rules:

### Selection Rules

1. **Agent Defaults** - Each agent has a default style
   ```
   software-architect → technical
   backend-engineer → technical
   business-analyst → executive
   product-manager → executive
   technical-writer → educational
   qa-engineer → code_review
   ```

2. **Contextual Rules** (override agent defaults)
   ```
   audience === 'executive' → executive
   task_type === 'code_review' → code_review
   audience === 'learner' → educational
   audience === 'developer' → technical
   ```

3. **Default Fallback** - Technical style if no match

### Selection Examples

```python
# Example 1: Backend Engineer (default: technical)
context = StyleContext(agent_type="backend-engineer")
style = manager.select_style(context)
# Result: TECHNICAL

# Example 2: Override with executive audience
context = StyleContext(
    agent_type="backend-engineer",
    audience="executive"
)
style = manager.select_style(context)
# Result: EXECUTIVE (contextual rule overrides agent default)

# Example 3: QA Engineer doing code review
context = StyleContext(
    agent_type="qa-engineer",
    task_type="code_review"
)
style = manager.select_style(context)
# Result: CODE_REVIEW
```

## 🛠️ Advanced Usage

### Custom Context

```python
# Full context specification
context = StyleContext(
    agent_type="software-architect",
    audience="developer",
    role="senior_engineer",
    task_type="architecture_design",
    experience_level="senior",
    language="en"
)

style = manager.select_style(context)
```

### Style Templates

```python
# Get specific template
header_template = manager.get_style_template(
    OutputStyle.TECHNICAL,
    template_type="header"
)

code_block_template = manager.get_style_template(
    OutputStyle.TECHNICAL,
    template_type="codeBlock"
)
```

### Style Configuration

```python
# Get full style configuration
config = manager.get_style_config(OutputStyle.EXECUTIVE)

print(f"Name: {config['name']}")
print(f"Target Audience: {config['targetAudience']}")
print(f"Characteristics: {config['characteristics']}")
```

### Content Validation

```python
# Validate content against style guidelines
validation = manager.validate_style_usage(
    OutputStyle.TECHNICAL,
    content="Your generated content here"
)

if not validation['valid']:
    print("Errors:")
    for error in validation['errors']:
        print(f"  - {error}")

if validation['warnings']:
    print("Warnings:")
    for warning in validation['warnings']:
        print(f"  - {warning}")
```

## 🌍 Multi-Language Support

Output Styles work across both English and Polish:

```python
# English context
context = StyleContext(
    agent_type="backend-engineer",
    language="en"
)

# Polish context
context = StyleContext(
    agent_type="backend-engineer",
    language="pl"
)

# Style principles preserved across languages
```

## ⚙️ Configuration

Configuration is stored in `.claude/config/output-styles.json`:

```json
{
  "styles": {
    "technical": {
      "name": "Technical Style",
      "characteristics": {
        "verbosity": "detailed",
        "technicality": "high"
      }
    }
  },

  "contextualSelection": {
    "enabled": true,
    "defaultStyle": "technical"
  },

  "agentDefaults": {
    "software-architect": "technical",
    "business-analyst": "executive"
  },

  "customization": {
    "allowUserOverride": true,
    "allowAgentSpecific": true,
    "cachePreferences": true
  }
}
```

## 📊 Quality Guidelines

Each style has specific quality requirements:

### Technical Style
- Minimum 2 code examples
- Maximum 150 words per paragraph
- Code comments required
- Diagrams optional

### Executive Style
- Maximum 500 words total
- Executive summary required
- ROI analysis required
- Timeline required

### Educational Style
- Learning objectives required
- Examples required
- Practice exercises optional
- Complexity level: intermediate maximum

### Code Review Style
- Severity levels required
- Action items required
- Maximum 20 issues per review
- Before/after comparisons required

## 🎯 Use Cases

### Use Case 1: Technical Documentation

```python
# Context for technical documentation
context = StyleContext(
    agent_type="software-architect",
    audience="developer",
    task_type="documentation"
)

# Generates technical style with code examples, diagrams, implementation details
prompt = manager.generate_context_prompt(context)
```

### Use Case 2: Executive Presentation

```python
# Context for executive presentation
context = StyleContext(
    agent_type="product-manager",
    audience="executive",
    task_type="status_report"
)

# Generates executive style with business focus, ROI, timelines
prompt = manager.generate_context_prompt(context)
```

### Use Case 3: Onboarding Tutorial

```python
# Context for onboarding
context = StyleContext(
    agent_type="technical-writer",
    audience="learner",
    experience_level="junior",
    task_type="tutorial"
)

# Generates educational style with step-by-step, explanations, exercises
prompt = manager.generate_context_prompt(context)
```

### Use Case 4: Pull Request Review

```python
# Context for PR review
context = StyleContext(
    agent_type="qa-engineer",
    task_type="code_review"
)

# Generates code review style with severity levels, actionable feedback
prompt = manager.generate_context_prompt(context)
```

## 📝 Best Practices

1. **Let context drive selection** - Provide rich context for accurate style selection
2. **Use agent defaults** - Leverage pre-configured agent-style mappings
3. **Validate output** - Use quality validation to ensure style compliance
4. **Cache preferences** - Enable caching for consistent style in long sessions
5. **Override when needed** - Use explicit style selection for special cases
6. **Review quality guidelines** - Ensure output meets style requirements
7. **Adapt across languages** - Trust style principles to work in Polish/English

## 🔧 Integration with Framework

### With Checkpoint System

```python
from checkpoint import CheckpointEngine
from output_styles import OutputStylesManager, StyleContext

# Create checkpoint with appropriate style
engine = CheckpointEngine()
styles = OutputStylesManager()

context = StyleContext(agent_type="backend-engineer")
style = styles.select_style(context)

# Use style for checkpoint descriptions
checkpoint_id = engine.create_checkpoint(
    label="refactoring_checkpoint",
    description="Technical style description with code context"
)
```

### With Multi-Agent System

```python
# Each agent gets appropriate style
agents = {
    "software-architect": StyleContext(agent_type="software-architect"),
    "business-analyst": StyleContext(agent_type="business-analyst"),
    "qa-engineer": StyleContext(agent_type="qa-engineer")
}

for agent_type, context in agents.items():
    style = styles.select_style(context)
    print(f"{agent_type} → {style.value}")
    # software-architect → technical
    # business-analyst → executive
    # qa-engineer → code_review
```

## 📚 API Reference

See module documentation:
- `OutputStylesManager` - Main manager (.ai-tools/output_styles/output_styles_manager.py:38)
- `OutputStyle` - Style enumeration
- `StyleContext` - Context dataclass

## 🔄 Future Enhancements

- Dynamic style blending (e.g., technical + executive)
- User preference learning
- Style transition smoothness
- Real-time style adaptation
- Custom style creation
- Style performance analytics

---

**Version:** 3.7.0
**License:** MIT
**Part of:** Claude Code Multi-Agent Framework
