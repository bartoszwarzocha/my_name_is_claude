# AI Validate Command

**Command**: `/ai-validate`
**Category**: AI-Tools Shortcuts
**Description**: Szybka walidacja quality bez pełnego menu

## Usage

```
/ai-validate
/ai-validate --fix
/ai-validate --strict
```

## Functionality

Runs comprehensive quality validation through AI Tools quality validator without menu navigation.

### Validation Areas
- Code quality standards
- Agent configuration compliance
- Framework integration health
- Testing coverage
- Security compliance
- Performance baselines

### Output Format
```
🔍 AI TOOLS QUALITY VALIDATION

Project: book_writing_app
Validation Level: Standard
Framework Compliance: Required

┌─ VALIDATION RESULTS ─────────────────────────────────────┐
│                                                         │
│ ✅ Code Quality        (92%) - Excellent               │
│ ✅ Agent Configuration (95%) - Excellent               │
│ ⚠️  Framework Integration (78%) - Good                │
│ ✅ Testing Coverage    (85%) - Very Good              │
│ ⚠️  Security Compliance (72%) - Needs Attention       │
│ ✅ Performance        (88%) - Very Good               │
│                                                         │
│ Overall Score: 85/100 (🟢 PASSING)                     │
└─────────────────────────────────────────────────────────┘

📈 DETAILED FINDINGS:

Code Quality ✅
• Python style compliance: 95%
• Documentation coverage: 88%
• Complexity metrics: Within limits

Agent Configuration ✅
• All required agents present
• Agent competencies properly defined
• Multi-agent coordination configured

Framework Integration ⚠️
• Core components: Operational
• MCP tools: Partially configured
• Quality gates: Missing pre-commit hooks

Testing Coverage ✅
• Unit tests: 85% coverage
• Integration tests: Present
• Test automation: Configured

Security Compliance ⚠️
• Dependency scanning: Not configured
• Secret scanning: Missing
• Security linting: Partially configured

Performance ✅
• Code efficiency: Good
• Memory usage: Optimal
• Startup time: Acceptable

🔧 ACTION ITEMS:

High Priority:
1. Configure dependency scanning tools
2. Setup pre-commit hooks
3. Implement secret scanning

Medium Priority:
4. Complete MCP tools configuration
5. Enhance security linting rules

✨ VALIDATION COMPLETE
```

## Integration

- Quality validator tools
- Framework compliance checking
- Agent validation system
- Automated fix suggestions