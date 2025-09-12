# Przykład 1: Aplikacja Desktop do Pisania Książek - Python/SQLite

**Data wykonania:** 2025-09-12  
**Commit:** 73a1009 (adaptative prompts)  
**Framework Version:** Claude Code Multi-Agent Framework v1.0 - Technology Adaptive

## Krótki Opis Aplikacji

Wieloplatformowa aplikacja desktop (Windows, Linux, macOS) do wspomagania procesu pisania książek. Aplikacja zapewnia kompletne środowisko pracy dla autorów z zaawansowanymi funkcjami organizacji treści, zarządzania źródłami i komunikacji z wydawnictwami.

## Kluczowe Założenia Technologiczne

- **Frontend:** Python + wxPython (cross-platform GUI)
- **Database:** SQLite (lokalna baza danych)
- **Architecture:** Desktop application z modularną architekturą
- **Platform Support:** Windows, Linux, macOS
- **Additional Technologies:** 
  - Export do różnych formatów (PDF, EPUB, DOCX)
  - Integracja z systemami kontroli wersji
  - Plugin system dla rozszerzeń

## Przykładowa Zawartość CLAUDE.md

```markdown
# CLAUDE.md – Book Writing Desktop Application

## 0. Project Metadata
- **project_name**: "book-writing-studio"
- **project_description**: "Cross-platform desktop application for book writing and publishing workflow"
- **primary_language**: python
- **business_domain**: publishing
- **project_scale**: sme
- **development_stage**: concept

## 1. Project Description
Cross-platform desktop application supporting complete book writing workflow from concept to publication, with advanced content organization, source management, and publisher communication features.

## 2. Domains and Goals
- Business domains: publishing, content creation, author workflow management
- Main project goals: streamline writing process, improve organization, facilitate publisher communication

## 3. Technologies
- **Frontend – technologies and tools:** Python, wxPython, cross-platform GUI
- **Backend – technologies and tools:** Python, SQLAlchemy, local file system
- **Database:** SQLite, local storage
- **Other:** PDF generation, EPUB export, DOCX integration, version control integration

## 4. Agents and Roles
[Standard agent configuration with focus on desktop development and publishing domain]

## 5. Integrations and Dependencies
- Export libraries: ReportLab (PDF), ebooklib (EPUB), python-docx (DOCX)
- GUI framework: wxPython
- Database ORM: SQLAlchemy
- File system operations: pathlib, os

## 6. Non-functional Requirements
- Performance: Fast text editing, responsive UI
- Security: Local data protection, backup mechanisms
- Scalability: Support for large manuscripts, multiple projects
- Availability: Offline-first design, data persistence

## 7. Special Notes
- Cross-platform compatibility essential
- Focus on writer-friendly UX/UI
- Robust data backup and recovery
- Plugin architecture for extensibility
```

## Sposób Zainicjowania Pracy z Projektem

### 1. Przygotowanie Środowiska

```bash
# Nawigacja do katalogu frameworku
cd /mnt/e/AI/my_name_is_claude

# Utworzenie katalogu projektu
mkdir book-writing-studio
cd book-writing-studio

# Skopiowanie frameworku
cp -r ../.claude .
cp ../CLAUDE.md .
cp ../DATABASE_CONNECTIONS.md .

# Dostosowanie CLAUDE.md do projektu
# [Edytuj plik CLAUDE.md zgodnie z powyższą zawartością]
```

### 2. Inicjalizacja Claude Code

```bash
# Uruchomienie Claude Code
claude-code

# Weryfikacja konfiguracji
# Sprawdź, czy .claude/agents/ zawiera wszystkich 11 agentów
# Sprawdź, czy prompty są dostępne w .claude/prompts/agents/
```

## Sposób Zainicjowania MCP

### Serena MCP (Analiza i Nawigacja Projektu)

```bash
# Instalacja i konfiguracja Serena
../mcp_tools.sh

# Wybór opcji 2: Serena MCP
# Konfiguracja z parametrami:
# - Port: 3001
# - Directory: ./book-writing-studio
# - Auto-indexing: enabled

# Weryfikacja w Claude Code settings:
# "mcpServers": {
#   "serena": {
#     "command": "npx",
#     "args": ["-y", "@tinytranzistor/serena", "--port", "3001", "--path", "./book-writing-studio"],
#     "env": {}
#   }
# }
```

### Context7 MCP (Dokumentacja i Generacja)

```bash
# Uruchomienie Context7 MCP
# Opcja 1: Context7 MCP
# Konfiguracja Docker-based deployment

# Weryfikacja integracji:
# Sprawdź dostępność narzędzi context7 w Claude Code
```

## Szczegółowa Instrukcja Krok po Kroku

### Faza 1: Analiza Biznesowa i Wymagania (1-2 godziny)

#### Krok 1.1: Analiza Wymagań Stakeholderów

**Prompt:** `.claude/prompts/agents/business/stakeholder-requirements-gathering.md`

**Oczekiwane efekty:**
- Kompletna analiza potrzeb autorów (primary stakeholders)
- Identyfikacja wymagań wydawców (secondary stakeholders)
- Mapowanie user journey dla procesu pisania książek
- Priorytetyzacja funkcjonalności (edytor → biblioteka źródeł → komunikacja)

**Jak reagować na opcje:**
- **Jeśli agent poprosi o więcej szczegółów:** Podaj informacje o różnych typach autorów (fikcja/non-fikcja, początkujący/doświadczeni)
- **Jeśli zaproponuje dodatkowe funkcje:** Oceń w kontekście MVP vs. przyszłych wersji
- **Przy pytaniach o konkurencję:** Wskaż Scrivener, yWriter jako referencje

#### Krok 1.2: Analiza Procesów Biznesowych

**Prompt:** `.claude/prompts/agents/business/current-state-process-analysis.md`

**Oczekiwane efekty:**
- Mapowanie obecnego workflow pisania książek
- Identyfikacja pain pointów w tradycyjnych metodach
- Propozycje optymalizacji procesów poprzez automatyzację
- Integracja z istniejącymi narzędziami autorskimi

#### Krok 1.3: Kreacja User Stories

**Prompt:** `.claude/prompts/agents/product/user-story-creation-and-prioritization.md`

**Oczekiwane efekty:**
- Kompletny backlog user stories dla wszystkich trzech modułów
- Priorytetyzacja według value/effort matrix
- Acceptance criteria dla kluczowych funkcji
- Roadmapa rozwoju produktu

### Faza 2: Architektura i Design UX (2-3 godziny)

#### Krok 2.1: Architektura Systemu Desktop

**Prompt:** `.claude/prompts/agents/architecture/system-architecture-design.md`

**Oczekiwane efekty:**
- Framework automatycznie wykryje Python/wxPython z CLAUDE.md
- Otrzymasz architekturę modularną dla aplikacji desktop
- Wzorce projektowe: MVC/MVP dla GUI, Repository pattern dla danych
- Specyfikacje integracji z SQLite i systemem plików

**Jak reagować na opcje:**
- **Plugin Architecture:** Zatwierdź - ważne dla rozszerzalności
- **Export System:** Priorytetyzuj PDF → EPUB → DOCX
- **Backup Strategy:** Akceptuj propozycje automatic backup

#### Krok 2.2: Architektura Desktop

**Prompt:** `.claude/prompts/agents/frontend/desktop-application-architecture.md`

**Oczekiwane efekty:**
- Szczegółowa architektura wxPython z konkretnym kodem
- Layout manager strategies dla responsywnego UI
- Event handling patterns dla desktop apps
- Threading model dla operacji I/O

#### Krok 2.3: Design UX dla Autorów

**Prompt:** `.claude/prompts/agents/design/user-research-and-persona-development.md`

**Oczekiwane efekty:**
- Persony autorów: Fiction Writer, Non-Fiction Author, Academic Writer
- User journey maps dla complete writing workflow
- Wireframes dla kluczowych screen flows
- Accessibility requirements dla długotrwałej pracy

### Faza 3: Development & Implementacja (6-8 godzin)

#### Krok 3.1: Implementacja GUI Desktop

**Prompt:** `.claude/prompts/agents/frontend/wxwidgets-desktop-development.md`

**Oczekiwane efekty:**
- Kompletny kod wxPython dla głównego okna aplikacji
- Implementation panels dla wszystkich trzech modułów
- Menu system z keyboard shortcuts
- Status bar z progress indicators

**Reakcje na output:**
- **Kod Python:** Zapisz w odpowiednich plikach modułowych
- **Requirements:** Dodaj do requirements.txt
- **Tests:** Zaplanuj dla następnej fazy

#### Krok 3.2: Integracja z Bazą Danych

**Prompt:** `.claude/prompts/agents/frontend/desktop-database-integration.md`

**Oczekiwane efekty:**
- SQLAlchemy models dla książek, rozdziałów, źródeł, wydawców
- Database migration strategies
- CRUD operations z proper error handling
- Backup/restore funkcjonalność

#### Krok 3.3: Design Bazy Danych

**Prompt:** `.claude/prompts/agents/data/database-design-and-etl-implementation.md`

**Oczekiwane efekty:**
- Framework wykryje SQLite z CLAUDE.md
- Otrzymasz schema design dla publishing domain
- ETL processes dla import/export data
- Performance optimization dla large texts

### Faza 4: Testowanie i Jakość (3-4 godziny)

#### Krok 4.1: Automatyzacja Testów

**Prompt:** `.claude/prompts/agents/qa/test-automation-and-quality-assurance.md`

**Oczekiwane efekty:**
- Framework wykryje Python i zaproponuje pytest
- Unit tests dla core business logic
- GUI testing strategies z wxPython
- Integration tests dla database operations

#### Krok 4.2: Review Kodu

**Prompt:** `.claude/prompts/agents/review/sonarqube-code-quality-analysis.md`

**Oczekiwane efekty:**
- Code quality analysis setup
- Static analysis configuration
- Performance profiling guidelines
- Security review dla local data

### Faza 5: Deployment i Packaging (2-3 godziny)

#### Krok 5.1: Packaging Desktop

**Prompt:** `.claude/prompts/agents/frontend/desktop-deployment-and-packaging.md`

**Oczekiwane efekty:**
- PyInstaller configuration dla wszystkich platform
- Cross-platform build scripts
- Installer creation (Windows MSI, macOS DMG, Linux deb/rpm)
- Auto-update mechanism

#### Krok 5.2: CI/CD Setup

**Prompt:** `.claude/prompts/agents/deployment/ci-cd-pipeline-and-infrastructure-setup.md`

**Oczekiwane efekty:**
- GitHub Actions workflow dla multi-platform builds
- Automated testing w pipeline
- Release management strategy
- Distribution channels setup

## Wykorzystanie Orkiestracji i Hooks

### Automatyczna Orkiestracja

```bash
# Automatyczny wybór scenariusza dla desktop app
./.claude/hooks/orchestration-trigger.sh

# Lub wybór konkretnego scenariusza:
./.claude/hooks/orchestration-trigger.sh "$(pwd)" "desktop"

# Monitoring postępu orkiestracji
./.claude/hooks/orchestration-monitor.sh "watch"
```

**Oczekiwane zachowanie orkiestracji:**
1. **Automatic Scenario Detection:** System wykryje desktop app Python/SQLite
2. **Multi-Agent Coordination:** Automatyczna koordynacja business-analyst → architect → frontend-engineer → qa-engineer
3. **Phase Gates:** Walidacja między fazami z approval points
4. **Conflict Resolution:** Automatic handling conflicts między GUI design a database schema

### Wykorzystanie Hooks

#### Performance Monitoring

```bash
# Monitoring wydajności GUI development
./.claude/hooks/agent-performance-monitor.sh "start" "frontend-engineer"

# Sprawdzanie bottlenecks w desktop development
./.claude/hooks/agent-performance-monitor.sh "analyze" "desktop"
```

#### Dependency Tracking

```bash
# Walidacja zależności przed desktop development
./.claude/hooks/cross-agent-dependency-tracker.sh "validate" "frontend-engineer"

# Sprawdzenie gotowości do packaging
./.claude/hooks/cross-agent-dependency-tracker.sh "check" "deployment-engineer"
```

#### Quality Assurance

```bash
# Compliance check dla desktop application standards
./.claude/hooks/compliance-automation.sh "desktop" "frontend-engineer"

# Accessibility validation dla długotrwałego użycia
./.claude/hooks/compliance-automation.sh "accessibility" "design"
```

## Realny Przypadek Użycia - Kompletny Proces Produkcyjny

### Dzień 1-2: Koncepcja i Planning
1. **Stakeholder Analysis** - Identyfikacja potrzeb autorów różnych gatunków
2. **Competitive Research** - Analiza Scrivener, yWriter, Ulysses
3. **Technical Feasibility** - Wybór Python/wxPython vs. alternatives
4. **MVP Definition** - Core features vs. nice-to-have

### Dzień 3-4: Architektura i Design
1. **System Architecture** - Modular design z plugin support
2. **Database Design** - Flexible schema dla różnych typów contentu
3. **UX Research** - Writer-focused interface design
4. **Technical Prototyping** - Proof of concepts dla key features

### Dzień 5-8: Core Development
1. **GUI Implementation** - Main editor, source library, publisher comm
2. **Database Layer** - SQLAlchemy models z migration support
3. **Core Features** - Text editing, project organization, export system
4. **Integration Testing** - Cross-module functionality validation

### Dzień 9-10: Quality & Polish
1. **Performance Optimization** - Large document handling, memory usage
2. **User Testing** - Beta testing z real authors
3. **Bug Fixes** - Issue resolution i stability improvements
4. **Documentation** - User manuals, developer docs

### Dzień 11-12: Deployment
1. **Multi-platform Builds** - Windows, macOS, Linux packages
2. **Distribution Setup** - Download sites, auto-updaters
3. **Release Management** - Version control, release notes
4. **Post-launch Support** - Monitoring, feedback collection

## Oczekiwane Rezultaty Końcowe

### Deliverables Techniczne
- ✅ **Fully Functional Desktop App** - Cross-platform Python/wxPython application
- ✅ **Complete Database Schema** - SQLite z comprehensive book writing data model
- ✅ **Export System** - PDF, EPUB, DOCX generation capabilities
- ✅ **Installation Packages** - Native installers dla wszystkich platform
- ✅ **Documentation** - Technical i user documentation

### Deliverables Biznesowe
- ✅ **Market-Ready Product** - Competitive feature set vs. existing solutions
- ✅ **User Experience** - Writer-optimized interface z accessibility features
- ✅ **Extensible Architecture** - Plugin system dla future enhancements
- ✅ **Support Infrastructure** - Update mechanism, feedback channels

### Metrics Sukcesu
- **Development Time:** 12 days vs. traditional 8-12 weeks
- **Code Quality:** 90%+ test coverage, zero critical bugs
- **Performance:** <2s startup time, smooth editing 1M+ characters
- **User Satisfaction:** Writer workflow improvement >50%
- **Technical Debt:** Maintainable, extensible codebase architecture

---

**Status:** Ready for implementation - Complete step-by-step blueprint dla desktop book writing application development używając Claude Code Multi-Agent Framework.

This example demonstrates pełny production workflow od concept do deployment, wykorzystując wszystkie możliwości frameworku including technology adaptation, multi-agent orchestration, i comprehensive quality assurance.