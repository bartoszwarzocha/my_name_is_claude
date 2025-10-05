# Output Styles System - Quick Reference Guide

**Version:** 1.0.0
**Quick Win #2:** Better stakeholder communication through context-aware output styles

## 🎯 Overview

Output Styles System provides **context-aware communication patterns** tailored to different stakeholders:

- **Technical** → Developers & Engineers (detailed, code-heavy)
- **Executive** → C-level & Management (high-level, ROI-focused)
- **Educational** → Learners & Juniors (step-by-step, explanatory)
- **Code Review** → Reviewers & QA (concise, actionable)

## 🚀 Quick Start

### Using Styles in Commands

```bash
# Technical style (default for engineers)
claude code "Implement OAuth2 authentication" --style technical

# Executive style (for stakeholders)
claude code "Project status report" --style executive

# Educational style (for learning)
claude code "Explain React hooks" --style educational

# Code Review style (for PR feedback)
claude code "Review authentication.ts" --style code_review
```

## 📋 Style Comparison

| Feature | Technical | Executive | Educational | Code Review |
|---------|-----------|-----------|-------------|-------------|
| **Verbosity** | Detailed | Concise | Expansive | Minimal |
| **Code Examples** | Abundant | None | With explanation | Targeted |
| **Business Context** | Minimal | Extensive | Contextual | None |
| **Technical Depth** | High | Low | Progressive | High |
| **Audience** | Developers | Management | Learners | Reviewers |

## 🎨 Style Examples

### Technical Style

**Input:** "Explain caching strategy"

**Output:**
```
## Caching Strategy Implementation

### Architecture Overview

```typescript
class CacheManager {
  private cache: Map<string, CacheEntry>;
  private ttl: number = 3600000; // 1 hour in ms

  async get<T>(key: string): Promise<T | null> {
    const entry = this.cache.get(key);
    if (!entry) return null;

    if (Date.now() - entry.timestamp > this.ttl) {
      this.cache.delete(key);
      return null;
    }

    return entry.value as T;
  }

  set(key: string, value: any): void {
    this.cache.set(key, {
      value,
      timestamp: Date.now()
    });
  }
}
```

**Technical Details:**
- In-memory Map-based cache for O(1) lookup
- TTL-based expiration (1 hour default)
- Generic types for type safety
- Lazy cleanup on access

**Performance:**
- Cache hit: <1ms
- Cache miss: 0ms (returns null)
- Memory: ~100 bytes per entry

**Next Steps:**
1. Add Redis integration for distributed caching
2. Implement cache warming strategies
3. Add metrics and monitoring
```

### Executive Style

**Input:** "Project status report"

**Output:**
```
# Executive Summary

**Objective:** Deliver user authentication system for Q4 launch

**Impact:** Enable 100K+ user registrations, reduce support tickets by 40%

**Timeline:** On track for Oct 31 delivery

---

## Key Points

✓ **Progress:** 75% complete (ahead of schedule by 1 week)
✓ **Budget:** $45K spent of $60K allocated (25% under budget)
✓ **Risk:** LOW - all critical paths on schedule
✓ **Quality:** 95% test coverage, zero critical bugs

## Return on Investment

- **Investment:** $60,000 (development + infrastructure)
- **Expected Return:** $240,000/year (reduced support costs + increased conversions)
- **Payback Period:** 3 months

---

**Recommendation:** PROCEED - Project is low-risk, on-budget, and delivering expected value
```

### Educational Style

**Input:** "Explain React hooks"

**Output:**
```
# Understanding React Hooks

## Learning Objectives

By the end of this guide, you will:
- Understand what hooks are and why they exist
- Use useState and useEffect confidently
- Know when to use different hooks

## Prerequisites

- Basic JavaScript knowledge
- Familiarity with React components
- Understanding of state and props

---

### Step 1: What are Hooks?

Hooks are special functions that let you "hook into" React features from function components.

**Why do they exist?**
Before hooks, you had to use class components for state. Hooks make function components more powerful!

```javascript
// ❌ OLD WAY (class components)
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }

  render() {
    return <div>{this.state.count}</div>;
  }
}

// ✅ NEW WAY (hooks)
function Counter() {
  const [count, setCount] = useState(0);
  return <div>{count}</div>;
}
```

**Why this works:** useState creates a "state variable" that persists between renders. Much simpler than classes!

### Step 2: Using useState

[... continues with step-by-step explanation ...]

## Practice Exercise

Create a counter that increments when you click a button. Use useState!

---

## Summary

**What you learned:**
- Hooks let function components have state
- useState creates state variables
- useEffect handles side effects

**Next steps:**
- Practice with useEffect
- Learn useContext
- Explore custom hooks
```

### Code Review Style

**Input:** "Review user-service.ts"

**Output:**
```
# Code Review Feedback

**Reviewed:** src/services/user-service.ts
**Reviewer:** security-engineer
**Date:** 2025-10-05

---

### CRITICAL: SQL Injection Vulnerability

**Location:** Line 45, getUserByEmail()

**Issue:**
Unsafe string concatenation in SQL query allows SQL injection attacks.

**Current:**
```typescript
const query = `SELECT * FROM users WHERE email = '${email}'`;
```

**Suggested:**
```typescript
const query = 'SELECT * FROM users WHERE email = $1';
const result = await db.query(query, [email]);
```

**Reasoning:** Parameterized queries prevent SQL injection by treating user input as data, not executable code.

---

### MAJOR: Password Hashing Missing Salt

**Location:** Line 78, hashPassword()

**Issue:**
Password hashing without salt makes rainbow table attacks possible.

**Current:**
```typescript
return crypto.createHash('sha256').update(password).digest('hex');
```

**Suggested:**
```typescript
import bcrypt from 'bcrypt';
return await bcrypt.hash(password, 10);
```

**Reasoning:** bcrypt automatically handles salting and is designed for password hashing.

---

## Summary

- Critical: 1
- Major: 1
- Minor: 3
- Suggestions: 2

**Overall Assessment:** Code has security vulnerabilities that MUST be fixed before merge.

---

**Action Required:** Address CRITICAL and MAJOR issues before approval.
```

## 🔧 Configuration

### Environment Variables

```bash
# Set default style
export CLAUDE_OUTPUT_STYLE="technical"

# Allow style override
export CLAUDE_ALLOW_STYLE_OVERRIDE="true"

# Cache style preferences
export CLAUDE_CACHE_STYLE_PREFS="true"
```

### Agent-Specific Defaults

Agents automatically use appropriate styles:

| Agent | Default Style |
|-------|---------------|
| software-architect | Technical |
| business-analyst | Executive |
| product-manager | Executive |
| technical-writer | Educational |
| qa-engineer | Code Review |
| reviewer | Code Review |

## 📊 When to Use Each Style

### Technical Style
✅ **Use for:**
- Implementation guides
- Architecture documentation
- API references
- Performance optimization
- Debugging guides

❌ **Don't use for:**
- Executive presentations
- Budget proposals
- Beginner tutorials
- Quick summaries

### Executive Style
✅ **Use for:**
- Status reports
- Budget justifications
- Strategic decisions
- Risk assessments
- ROI analysis

❌ **Don't use for:**
- Code documentation
- Technical specs
- Implementation details
- Debugging

### Educational Style
✅ **Use for:**
- Getting started guides
- Concept explanations
- Best practices
- Troubleshooting guides
- Framework overviews

❌ **Don't use for:**
- Executive summaries
- Code reviews
- Quick references
- Time-sensitive communication

### Code Review Style
✅ **Use for:**
- Pull request reviews
- Code quality assessments
- Security audits
- Performance reviews
- Refactoring suggestions

❌ **Don't use for:**
- Learning materials
- Executive communication
- General documentation
- Brainstorming

## 🎯 Best Practices

1. **Match audience** - Choose style based on who will read the output
2. **Be consistent** - Use same style throughout a document
3. **Override when needed** - Don't be afraid to change style mid-project
4. **Combine with Model Profiles** - Use Quality profile + Executive style for critical business decisions
5. **Test with stakeholders** - Verify style meets their needs

## 📚 Advanced Usage

### Custom Style Combinations

```bash
# High-quality executive summary
claude code "Q4 results" --profile quality --style executive

# Fast technical check
claude code "Quick code review" --profile fast --style code_review

# Comprehensive learning material
claude code "React tutorial" --profile balanced --style educational
```

### Context-Aware Auto-Selection

System automatically selects style based on:
- Agent type
- Task type
- Audience (if specified)
- Previous preferences

## 🔄 Updates & Maintenance

**Version:** 1.0.0
**Last Updated:** 2025-10-05
**Configuration:** `.claude/config/output-styles.json`

---

**Questions?** See main documentation in `.claude/config/README.md`
