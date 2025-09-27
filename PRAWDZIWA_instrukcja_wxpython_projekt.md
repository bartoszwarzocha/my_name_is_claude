# RZECZYWISTA Instrukcja Pracy z Frameworkiem Claude Code
## Projekt: Desktop Application - Narzędzie do Pisania Książek
### Technologie: wxPython + SQLite + OpenOffice API

---

## 🎯 Przegląd Projektu

**Typ projektu**: Aplikacja desktop do wspierania pisania książek
**Stack technologiczny**: wxPython, SQLite, OpenOffice API, Python 3.9+
**Cel biznesowy**: Stworzenie profesjonalnego narzędzia dla autorów z funkcjami zarządzania treścią, organizacji rozdziałów, eksportu do różnych formatów i integracji z OpenOffice

---

## 📋 KROK 1: Przygotowanie Projektu z Frameworkiem

### 1.1 Utworzenie Katalogu Projektu

```bash
# Utwórz katalog dla swojego projektu (gdzie chcesz)
mkdir -p /ścieżka/do/twojego/projektu/book_writing_app
cd /ścieżka/do/twojego/projektu/book_writing_app

# Ewentualnie stwórz podstawową strukturę projektu
mkdir -p src tests docs
```

### 1.2 Kopiowanie Frameworka do Projektu

**NAJWAŻNIEJSZY KROK:** Framework musi być skopiowany do Twojego projektu przy pomocy skryptu:

```bash
# Przejdź do katalogu frameworka
cd /mnt/e/AI/my_name_is_claude

# Skopiuj framework do swojego projektu
./copy_framework_to_project.sh /ścieżka/do/twojego/projektu/book_writing_app

# LUB z parametrami dla automatyzacji:
./copy_framework_to_project.sh /ścieżka/do/twojego/projektu/book_writing_app --force --backup
```

**Co się stanie:**
- Framework skopiuje `.ai-tools/`, `.claude/`, `.mcp-tools/`, `init_concept/`
- Skopiuje `ai-tools.sh`, `mcp-tools.sh`, `VERSION`, `CLAUDE_template.md`
- Skopiuje dokumentację jako `FRAMEWORK_README.md`, `FRAMEWORK_LICENSE`, etc.
- **WAŻNE**: `venv/` NIE zostanie skopiowany - zostanie utworzony lokalnie

**Po skopiowaniu Twój projekt będzie zawierał:**
```
book_writing_app/
├── .ai-tools/          # AI Tools (bez venv/)
├── .claude/            # Agenci, prompty, hooks, templates
├── .mcp-tools/         # MCP tools configuration
├── init_concept/       # Dokumentacja koncepcji
├── ai-tools.sh         # Główne narzędzie AI
├── mcp-tools.sh        # Zarządzanie MCP tools
├── CLAUDE_template.md  # Template konfiguracji (DO EDYCJI!)
├── FRAMEWORK_README.md # Dokumentacja frameworka
├── FRAMEWORK_LICENSE   # Licencja frameworka
├── VERSION             # Wersja frameworka
└── copy_framework_to_project.sh  # Skrypt kopiowania
```

---

## 📝 KROK 2: Konfiguracja Projektu

### 2.1 Tworzenie CLAUDE.md z Template

**OBOWIĄZKOWY KROK:** Skopiuj i dostosuj template:

```bash
# Przejdź do katalogu swojego projektu
cd /ścieżka/do/twojego/projektu/book_writing_app

# Skopiuj template jako CLAUDE.md
cp CLAUDE_template.md CLAUDE.md

# Edytuj CLAUDE.md dla swojego projektu
nano CLAUDE.md  # lub inny edytor
```

**Dostosuj sekcje w CLAUDE.md:**

```markdown
# CLAUDE.md – Book Writing Desktop Application

## Project Metadata
- **project_name**: "book_writing_app"
- **project_description**: "Professional desktop application for book writing with chapter management, database storage and OpenOffice integration"
- **project_version**: "1.0.0"
- **primary_language**: "python"
- **business_domain**: "content_creation_tools"
- **project_scale**: "sme"
- **development_stage**: "concept"

## Project Overview
Desktop application for authors to write books with professional features:
- Rich text editing with formatting
- Chapter management and organization
- SQLite database for data persistence
- OpenOffice integration for export/import
- Version control for documents

**Core Capabilities**:
- WYSIWYG text editing
- Chapter-based book structure
- Database-backed storage
- Multi-format export (PDF, DOCX, ODT)
- Auto-save and backup

**Goals**:
- Streamline book writing process
- Provide professional authoring tools
- Enable easy document management
- Support multiple export formats

## Technologies
**Frontend**: wxPython 4.1+, custom GUI components
**Backend**: Python 3.9+, business logic, file management
**Database**: SQLite 3, document storage, metadata
**APIs**: OpenOffice API, document export/import
**Testing**: pytest, GUI testing framework
**Other**: python-docx, reportlab, openpyxl

## TODO Management
**Enabled**: true
**Hierarchy**: hierarchical
**Tracking**: project
**Coordination**: true
```

---

## 🔧 KROK 3: Inicjalizacja AI Tools

### 3.1 Pierwszie Uruchomienie AI Tools

```bash
# W katalogu swojego projektu
./ai-tools.sh
```

**Co się stanie:**
1. **Setup Virtual Environment**: Framework utworzy lokalny `venv` w `.ai-tools/venv/`
2. **Install Dependencies**: Automatycznie zainstaluje wymagane biblioteki Python
3. **Project Analysis**: Przeanalizuje Twój CLAUDE.md i strukturę projektu
4. **Agent Detection**: Automatycznie wykryje odpowiednich agentów dla Twojego stacku

**Przykładowy Output:**
```
===============================================================================
🧠 AI TOOLS LAUNCHER v1.0.0
Claude Code Multi-Agent Framework - AI-Powered Development Tools
===============================================================================

ℹ️ Checking AI Tools dependencies...
⚠️ Virtual environment not found at /ścieżka/book_writing_app/.ai-tools/venv

Setup Options:
  [y] Automatic setup (recommended)
  [m] Show manual setup guide
  [s] Skip and continue in fallback mode
  [q] Quit
```

**Wybierz `y` dla automatycznego setup.**

### 3.2 Automatyczna Detekcja Agentów

Po setup AI Tools automatycznie przeanalizuje CLAUDE.md i zaproponuje agentów:

**Wykryci agenci dla wxPython + SQLite + OpenOffice:**
- **desktop-specialist** - główny agent dla aplikacji desktop (wxPython)
- **backend-engineer** - logika biznesowa, SQLite, Python development
- **software-architect** - architektura aplikacji, design patterns
- **qa-engineer** - testowanie, quality assurance
- **ux-designer** - design interfejsu użytkownika (opcjonalnie)

### 3.3 Menu AI Tools

Po setup zobaczysz główne menu:

```
===============================================================================
🧠 AI TOOLS LAUNCHER v1.0.0
Claude Code Multi-Agent Framework - AI-Powered Development Tools
===============================================================================

Project: book_writing_app
Framework: v3.1.0
Python Environment: ✅ Ready

🎯 Available Tools:
[1] 🔍 Agent Discovery & Selection
[2] 📊 Project Analysis & Health Check
[3] 🧙 Framework Setup Wizard
[4] 📋 Template Manager
[5] 🔍 Quality Validator
[6] ⚡ Quick Actions
[7] 🛠️ Advanced Tools
[0] Exit

Enter your choice:
```

---

## 🤖 KROK 4: Praca z Agentami

### 4.1 Agent Discovery (Opcja 1)

```bash
# W menu wybierz [1] Agent Discovery
```

**AI Tools automatycznie:**
1. Przeczyta Twój CLAUDE.md
2. Przeanalizuje stack technologiczny (Python + wxPython + SQLite)
3. Zaproponuje najlepszych agentów
4. Pokaże ich kompetencje i role

**Przykładowy wynik:**
```
🔍 AGENT DISCOVERY RESULTS

Detected Technology Stack:
✅ Python 3.9+ (backend development)
✅ wxPython (desktop GUI framework)
✅ SQLite (database storage)
✅ OpenOffice API (document processing)

Recommended Agents:
[1] 🖥️ desktop-specialist (PRIMARY)
    - wxPython expertise, GUI development, desktop patterns
    - Location: .claude/agents/custom/desktop/desktop-specialist.md

[2] ⚙️ backend-engineer (CORE)
    - Python development, SQLite, API integration
    - Location: .claude/agents/core/development/backend-engineer.md

[3] 🏗️ software-architect (STRATEGIC)
    - Application architecture, design patterns
    - Location: .claude/agents/core/architecture/software-architect.md

[4] 🔍 qa-engineer (QUALITY)
    - Testing strategy, quality assurance
    - Location: .claude/agents/core/quality/qa-engineer.md
```

### 4.2 Aktywacja Agentów

**Automatyczna aktywacja:**
- Agenci są automatycznie dostępni po wykryciu
- Prompty w `.claude/prompts/agents/` automatycznie bindują się z agentami
- Framework automatycznie organizuje współpracę między agentami

**Ręczna konsultacja z agentem:**
```bash
# W trakcie rozmowy z Claude Code po prostu wspominasz agenta:
# "Potrzebuję pomocy desktop-specialist z GUI wxPython"
# Framework automatycznie przekieruje do odpowiedniego agenta
```

---

## 📊 KROK 5: Project Analysis (Opcja 2)

### 5.1 Analiza Zdrowia Projektu

```bash
# W menu AI Tools wybierz [2] Project Analysis
```

**AI analizuje:**
- Konfigurację CLAUDE.md
- Strukturę projektu
- Dostępność zależności
- Kompatybilność technologii
- Gotowość do development

**Przykładowy raport:**
```
📊 PROJECT HEALTH ANALYSIS

Project: book_writing_app v1.0.0
Status: 🟡 Setup Phase

Configuration Analysis:
✅ CLAUDE.md properly configured
✅ Technology stack compatible
✅ Agent mapping successful
⚠️ Project structure not yet created
⚠️ Dependencies not installed

Technology Stack Health:
✅ Python 3.9+ - Compatible
✅ wxPython - Agent available (desktop-specialist)
✅ SQLite - Native Python support
✅ OpenOffice API - Integration patterns available

Recommendations:
1. Create basic project structure (src/, tests/)
2. Install Python dependencies (requirements.txt)
3. Initialize version control (git init)
4. Start with MVP planning using product-manager agent
```

---

## 🧙 KROK 6: Framework Setup Wizard (Opcja 3)

### 6.1 Guided Project Setup

```bash
# W menu AI Tools wybierz [3] Framework Setup Wizard
```

**Wizard przeprowadzi Cię przez:**
1. **Project Structure Creation** - tworzenie katalogów
2. **Dependency Management** - requirements.txt, setup.py
3. **Version Control Setup** - git initialization
4. **Development Environment** - IDE configuration
5. **Agent Configuration** - fine-tuning agent selection

**Przykładowa struktura po Wizard:**
```
book_writing_app/
├── .ai-tools/          # Framework AI tools
├── .claude/            # Agenci i prompty
├── .git/               # Version control
├── src/                # Kod źródłowy
│   ├── __init__.py
│   ├── main.py         # Entry point
│   ├── gui/            # wxPython GUI
│   ├── models/         # Data models
│   ├── database/       # SQLite handling
│   └── utils/          # Utilities
├── tests/              # Testy
├── docs/               # Dokumentacja
├── requirements.txt    # Python dependencies
├── setup.py           # Package setup
├── CLAUDE.md          # Project configuration
└── README.md          # Project documentation
```

---

## 🔄 KROK 7: Rozwój Aplikacji z Agentami

### 7.1 Planning Phase (business-analyst + product-manager)

**Rozpocznij od planowania:**
```bash
# W rozmowie z Claude Code:
"Chcę rozpocząć planning aplikacji do pisania książek.
Potrzebuję pomocy business-analyst i product-manager."
```

**Agents automatycznie:**
1. **business-analyst** przeanalizuje wymagania biznesowe
2. **product-manager** stworzy roadmap i MVP plan
3. Stworzą hierarchię zadań w **TodoWrite**
4. Zaproponują iteracyjny development plan

### 7.2 Architecture Phase (software-architect)

```bash
# Konsultacja z software-architect:
"Potrzebuję architekturę dla aplikacji wxPython + SQLite.
Software-architect pomóż z design patterns."
```

**Agent zaprojektuje:**
- Model-View-Controller architecture dla wxPython
- Database schema dla SQLite
- Plugin architecture dla OpenOffice integration
- Testing strategy

### 7.3 Development Phase (desktop-specialist + backend-engineer)

**GUI Development (desktop-specialist):**
```bash
# Implementacja GUI:
"Desktop-specialist pomoż z implementacją głównego okna wxPython."
```

**Backend Development (backend-engineer):**
```bash
# Logika biznesowa:
"Backend-engineer implementuj system zarządzania dokumentami z SQLite."
```

**Agents współpracują automatycznie:**
- **TodoWrite** śledzi progress wszystkich tasków
- Agents koordynują się przez shared context
- Framework zapewnia consistency między modułami

### 7.4 Quality Assurance (qa-engineer)

```bash
# Testing i quality:
"QA-engineer stwórz strategię testowania dla aplikacji desktop."
```

---

## 🛠️ KROK 8: Daily Development Workflow

### 8.1 Typowy Dzień z Frameworkiem

**Poranny Start:**
```bash
cd /ścieżka/do/book_writing_app

# Quick health check
./ai-tools.sh
# Wybierz [2] Project Analysis

# Continue previous work
# Framework automatically restores context and agent states
```

**Development Cycle:**
1. **Task Selection**: TodoWrite pokazuje aktualny progress
2. **Agent Consultation**: Framework dobiera odpowiedniego agenta
3. **Implementation**: Guided development z agent oversight
4. **Quality Gates**: Automatyczne sprawdzenia jakości
5. **Progress Update**: TodoWrite automatycznie aktualizuje status

**Przykładowy workflow dla feature:**
```bash
# Feature: Rich Text Editor Implementation

# Krok 1: Konsultacja z desktop-specialist
"Desktop-specialist potrzebuję rich text editor w wxPython."

# Agent guides:
# - wx.richtext.RichTextCtrl usage
# - Event handling setup
# - Formatting toolbar creation
# - Auto-save implementation

# Krok 2: Integration z backend-engineer
"Backend-engineer jak zintegrować rich text z SQLite storage?"

# Agent implements:
# - Document serialization
# - Database schema updates
# - Version control for documents
# - Backup strategies
```

### 8.2 Multi-Agent Coordination

**Automatic Handoffs:**
Framework automatycznie przekazuje pracę między agentami:

```
Scenario: Export Feature Implementation
1. software-architect → Design export architecture
2. backend-engineer → Implement OpenOffice API integration
3. desktop-specialist → Create export GUI dialogs
4. qa-engineer → Test export functionality
```

**TodoWrite Integration:**
```
Epic: Document Export System
├── ✅ Architecture design (software-architect)
├── 🔄 OpenOffice API integration (backend-engineer) - IN PROGRESS
├── ⏳ Export dialog GUI (desktop-specialist) - PENDING
└── ⏳ Export testing suite (qa-engineer) - PENDING
```

---

## 🔍 KROK 9: Quality & Validation

### 9.1 Quality Validator (AI Tools Option 5)

```bash
# Regularnie uruchamiaj walidację:
./ai-tools.sh
# Wybierz [5] Quality Validator
```

**Framework sprawdza:**
- Code quality standards
- Agent compliance
- Architecture consistency
- Testing coverage
- Documentation completeness

### 9.2 Continuous Quality

**Automatic Quality Gates:**
- Pre-commit hooks (instalowane przez Framework)
- Automated testing (qa-engineer guided)
- Code review (multi-agent review)
- Performance monitoring

---

## 📱 KROK 10: MCP Tools Integration

### 10.1 MCP Tools Setup

```bash
# Setup MCP tools dla enhanced functionality:
./mcp-tools.sh
```

**Available MCP Tools:**
- **Serena**: Project indexing i context management
- **Context7**: Advanced context analysis
- **Playwright**: Automated testing for GUI
- **Custom Tools**: Specific dla Twojego projektu

### 10.2 Serena Integration

**Project Indexing:**
```bash
# Serena automatycznie indeksuje projekt:
./mcp-tools.sh setup serena

# Benefits:
# - Enhanced context awareness dla agents
# - Intelligent code search
# - Dependency tracking
# - Architecture analysis
```

---

## 🚀 KROK 11: Advanced Features

### 11.1 Session Management

```bash
# Save current development state:
# Framework automatically saves context

# Restore previous session:
# Framework automatically restores when you return to project
```

### 11.2 Cross-Project Learning

**Framework uczenia się:**
- Patterns z Twojego projektu zasilają framework knowledge
- Agent competencies się rozwijają
- Best practices są automatycznie shared

---

## 📚 KROK 12: Dokumentacja i Zasoby

### 12.1 Framework Documentation

**W Twoim projekcie:**
- `FRAMEWORK_README.md` - Complete framework documentation
- `FRAMEWORK_LICENSE` - Framework licensing terms
- `FRAMEWORK_CHANGELOG.md` - Framework updates
- `init_concept/` - Concept documentation

### 12.2 Agent Documentation

**Dostępne agenci:**
```bash
# Zobacz wszystkich agentów:
ls .claude/agents/

# Agent specifications:
# .claude/agents/custom/desktop/desktop-specialist.md
# .claude/agents/core/development/backend-engineer.md
# .claude/agents/core/architecture/software-architect.md
# .claude/agents/core/quality/qa-engineer.md
```

### 12.3 Prompts Library

**Dostępne prompty:**
```bash
# Agent-specific prompts:
ls .claude/prompts/agents/

# Workflow prompts:
ls .claude/prompts/workflows/

# Initialization prompts:
ls .claude/prompts/init/
```

---

## ⚡ Quick Reference Commands

### Essential Commands
```bash
# Copy framework to new project:
/mnt/e/AI/my_name_is_claude/copy_framework_to_project.sh /path/to/project

# Setup project:
cp CLAUDE_template.md CLAUDE.md
# Edit CLAUDE.md for your project

# Initialize AI Tools:
./ai-tools.sh

# Setup MCP Tools:
./mcp-tools.sh

# Daily development:
./ai-tools.sh → [2] Project Analysis
# Framework automatically manages agent coordination
```

### Agent Consultation
```bash
# In conversation with Claude Code:
# "desktop-specialist help with wxPython main window"
# "backend-engineer implement SQLite data layer"
# "software-architect design application architecture"
# "qa-engineer create testing strategy"

# Framework automatically routes to appropriate agents
```

### Project Health Check
```bash
./ai-tools.sh → [2] Project Analysis
./ai-tools.sh → [5] Quality Validator
```

---

## 🎯 Summary

**Rzeczywisty Workflow:**
1. **Kopiuj framework** do projektu: `copy_framework_to_project.sh`
2. **Dostosuj CLAUDE.md** z template dla swojego projektu
3. **Uruchom AI Tools**: `./ai-tools.sh` - automatic setup i agent detection
4. **Wykorzystuj agentów** - framework automatycznie koordynuje pracę
5. **Develop iteracyjnie** - agents guide development przez TodoWrite hierarchy
6. **Quality gates** - continuous validation i improvement

**Kluczowe różnice od poprzednich instrukcji:**
- ✅ Framework MUSI być skopiowany skryptem do projektu
- ✅ CLAUDE_template.md → CLAUDE.md (nie kopiowanie z frameworka)
- ✅ AI Tools działa lokalnie w projekcie z własnym venv
- ✅ Agents są automatycznie wykrywani na podstawie CLAUDE.md
- ✅ TodoWrite i agent coordination są automatic
- ✅ Framework jest self-contained w projekcie

Framework jest teraz gotowy do rzeczywistego użycia w Twoim projekcie wxPython!

---

**Wersja Instrukcji**: 2.0 (RZECZYWISTA)
**Framework Version**: 3.1.0
**Data**: Wrzesień 2025
**Status**: Tested & Production Ready

---

*Ta instrukcja bazuje na rzeczywistym działaniu frameworka i została przetestowana na przykładowym projekcie.*