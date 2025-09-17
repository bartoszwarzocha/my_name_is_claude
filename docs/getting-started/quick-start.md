# Quick Start Guide

Szybkie wprowadzenie do Claude Code Multi-Agent Framework z AI-Powered Agent Selection.

## 🎯 Cel

W tym przewodniku nauczysz się:
- Jak zainicjalizować framework w projekcie
- Jak używać AI agent selection
- Jak zarządzać sesjami pracy
- Jak wykorzystać automatyczne workflow

## 📋 Wymagania

- ✅ Framework [zainstalowany](installation.md)
- ✅ Python 3.8+
- ✅ Dostęp do Claude AI

## 🚀 Pierwszy Start

### 1. Inicjalizacja Frameworka

```bash
# Przejdź do katalogu swojego projektu
cd /path/to/your/project

# Skopiuj konfigurację frameworka
cp /path/to/claude-framework/CLAUDE_template.md ./CLAUDE.md
```

### 2. Konfiguracja Projektu

Edytuj `CLAUDE.md` dla swojego projektu:

```markdown
## 0. Project Metadata

- **project_name**: "my-awesome-app"
- **project_description**: "Modern web application with React and Node.js"
- **project_version**: "1.0.0"
- **primary_language**: "typescript"
- **business_domain**: "web_development"
- **project_scale**: "startup"  # startup, sme, enterprise
```

### 3. Test AI Agent Selection

```bash
# Uruchom analizę projektu
python /path/to/framework/.ai-tools/core/demo/demo_project_analyzer.py .

# Wynik: analiza technologii + rekomendacje agentów
```

## 🤖 Używanie AI Agent Selection

### Automatyczna Analiza Projektu

Framework automatycznie analizuje:

- **Technology Stack**: React, Node.js, TypeScript, Docker, etc.
- **Business Domain**: Web development, FinTech, Healthcare, etc.
- **Project Complexity**: Startup, SME, Enterprise scale
- **Team Context**: Git patterns, collaboration indicators

### Przykład Rezultatu

```
🎯 PROJECT ANALYSIS
Technology Stack: React + Node.js + PostgreSQL
Complexity: SME (Score: 0.58)
Domain: E-commerce with GDPR/PCI-DSS compliance

🤖 AI AGENT RECOMMENDATIONS
Core Project Management:
  ✅ project-owner (confidence: 0.95)
  ✅ session-manager (confidence: 0.90)

Development:
  ✅ frontend-engineer (confidence: 0.92)
  ✅ backend-engineer (confidence: 0.88)
  ✅ api-engineer (confidence: 0.90)

Quality & Security:
  ✅ qa-engineer (confidence: 0.83)
  ✅ security-engineer (confidence: 0.84)
```

## 📝 Zarządzanie Sesjami

### Rozpoczęcie Nowej Sesji

```bash
# Komenda w Claude Code CLI
"rozpocznij sesję"
```

Framework automatycznie:
1. Analizuje kontekst projektu
2. Rekomenduje odpowiednich agentów
3. Generuje plan pracy
4. Rozpoczyna sesję z wybranym agentem

### Przywracanie Sesji

```bash
# Kontynuacja pracy
"kontynuuj sesję"

# Odzyskiwanie po przerwaniu
"odzyskaj sesję"
```

### Synchronizacja z Serena MCP

Jeśli masz Serena MCP:

```bash
# Synchronizacja z indeksem projektu
"serena sync"
```

## ⚡ Automatyczne Workflow

### Generowanie Workflow

Framework generuje inteligentne workflow na podstawie:

- **Project Context**: Rodzaj projektu i technologie
- **Recommended Agents**: AI-wybrani agenci
- **Business Requirements**: Wymagania domeny biznesowej
- **Compliance Needs**: Wymagania zgodności (GDPR, HIPAA, etc.)

### Przykład Workflow

```
🚀 Initialization: project-owner → business-analyst
🏗️ Architecture: software-architect → security-engineer
💻 Development: frontend-engineer → backend-engineer → api-engineer
🧪 Quality: qa-engineer
🚀 Deployment: deployment-engineer → cloud-engineer
```

### Optymalizacja Wykonania

- **Parallel Execution**: Zadania równoległe gdzie to możliwe
- **Dependency Resolution**: Automatyczne zarządzanie zależnościami
- **Resource Optimization**: Balansowanie obciążenia agentów
- **Risk Mitigation**: Plany awaryjne dla krytycznych faz

## 🎯 Przykładowe Sesje Pracy

### Scenario 1: Nowy Projekt React

```markdown
User: "Chcę stworzyć nową aplikację React z TypeScript"

AI Analysis:
- Technology: React + TypeScript
- Complexity: Startup
- Agents: frontend-engineer, backend-engineer, qa-engineer

Workflow:
1. project-owner: Setup project structure
2. frontend-engineer: React + TypeScript setup
3. backend-engineer: API backend (if needed)
4. qa-engineer: Testing setup
```

### Scenario 2: Enterprise Migration

```markdown
User: "Migruję legacy system na microservices"

AI Analysis:
- Technology: Legacy → Microservices
- Complexity: Enterprise
- Agents: enterprise-architect, integration-architect, security-engineer

Workflow:
1. enterprise-architect: Migration strategy
2. integration-architect: API design
3. security-engineer: Security assessment
4. deployment-engineer: Infrastructure
```

## 📊 Monitorowanie Postępu

### TodoWrite Integration

Framework automatycznie śledzi:

```
✅ [completed] Project analysis and agent selection
🔄 [in_progress] Frontend component development
⏳ [pending] API integration
⏳ [pending] Testing and deployment
```

### Performance Metrics

```
Response Time: 1.2s (target: <2s)
Accuracy: 87% agent recommendations
Setup Time: 8 min (50% reduction achieved)
```

## 🔧 Dostosowanie

### Custom Agent Selection

```bash
# Force specific agents
"Użyj frontend-engineer i security-engineer dla tego projektu"
```

### Workflow Customization

```bash
# Custom workflow priorities
"Priorytet na security w tym projekcie fintech"
```

### Manual Overrides

```bash
# Manual agent change
"Zmień na api-engineer zamiast backend-engineer"
```

## ⚠️ Troubleshooting

### Problem: AI nie działa

```bash
# Check AI status
python -c "
from ai_tools.integration.ai_agent_selector import AIAgentSelector
selector = AIAgentSelector()
print('AI Enabled:', selector.ai_enabled)
"

# Fallback to rule-based
# Framework automatycznie przełączy się na rule-based selection
```

### Problem: Błędne rekomendacje

```bash
# Force re-analysis
"Przeanalizuj projekt ponownie"

# Manual agent selection
"Chcę użyć [agent-name]"
```

## 📚 Następne Kroki

Po opanowaniu podstaw:

1. **[First Project](first-project.md)** - Stwórz kompletny projekt
2. **[Agents Overview](../user-guide/agents/overview.md)** - Poznaj wszystkich agentów
3. **[AI Features](../user-guide/ai-features/agent-selection.md)** - Zaawansowane AI features
4. **[Custom Workflows](../examples/custom-workflows.md)** - Twórz własne workflow

## 💡 Wskazówki

- **Start Small**: Zacznij od prostych projektów
- **Trust AI**: Pozwól AI rekomendować agentów
- **Customize Gradually**: Dostosowuj framework stopniowo
- **Monitor Performance**: Śledź metryki i optymalizuj

---

*Gratulacje! Możesz teraz efektywnie używać Claude Code Multi-Agent Framework z AI-Powered Agent Selection.*