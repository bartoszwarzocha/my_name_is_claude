# MCP Tools Manager - Przewodnik Użytkownika

## 🚀 Wprowadzenie

**MCP Tools Manager v2.0.0** to zaawansowany system zarządzania narzędziami MCP (Model Context Protocol) dla Claude Code Multi-Agent Framework. Umożliwia łatwe instalowanie, konfigurowanie i zarządzanie 32+ profesjonalnymi narzędziami MCP.

## 📋 Wymagania Systemowe

### Obowiązkowe
- **Bash** (wersja 4.0+)
- **jq** (do przetwarzania JSON)
- **curl/wget** (do pobierania pakietów)

### Opcjonalne (zależnie od narzędzi)
- **Docker** (dla Context7 i narzędzi dockerowych)
- **Node.js/npm** (dla narzędzi npm)
- **Git** (dla Serena i narzędzi git)
- **Python/uv** (dla Serena)

## 🔧 Pierwszy Setup

### 1. Sprawdzenie i Naprawa Registry

Jeśli widzisz pusty ekran, prawdopodobnie brakuje pliku registry:

```bash
# Sprawdź czy registry istnieje
ls ~/.mcp-tools/registry/

# Jeśli brakuje extended.json, skopiuj z projektu:
cp .mcp-tools/registry/extended.json ~/.mcp-tools/registry/
```

### 2. Instalacja jq (jeśli brakuje)

```bash
# Ubuntu/Debian
sudo apt install jq

# MacOS
brew install jq

# Windows (WSL)
sudo apt install jq
```

## 🎯 Uruchamianie

```bash
./mcp-tools.sh
```

## 📱 Interfejs Użytkownika

### Główne Menu

Po uruchomieniu zobaczysz:

```
════════════ MCP TOOLS MANAGER ════════════
Version: 2.0.0 | Framework: Claude Code Multi-Agent v2.1.0
Mode: FULL (All features available)
Project: my_name_is_claude
Path: /mnt/e/AI/my_name_is_claude
═══════════════════════════════════════════

CONFIGURATION MANAGEMENT:
 [g] ⚙️ Global MCP Configuration
 [p] 🔧 Project-specific MCP Configuration
 [a] 🏥 View Active MCP Status

SMART RECOMMENDATIONS (Based on detected: nodejs react):
 [s] Serena - Code Navigation & Project Analysis
 [c] Context7 - Advanced Code Generation & Documentation
 [g] GitHub - Repository Management & Git Operations

MCP TOOLS BY CATEGORY:
 [1] 🚀 Development & Code
 [2] 🎯 Testing & Quality
 [3] ⚙️ Database & APIs
 [4] 🔧 Cloud & Infrastructure
 [5] ⚡ AI & Machine Learning
 [6] 🏥 Productivity & System Tools

SYSTEM OPERATIONS:
 [h] 🏥 System Health Check
 [u] 🚀 Update All MCP Tools
 [0] Exit
═══════════════════════════════════════════
```

### Opcje Menu

#### Zarządzanie Konfiguracją
- **[g]** - Konfiguracja globalna MCP
- **[p]** - Konfiguracja specyficzna dla projektu
- **[a]** - Status aktywnych narzędzi MCP

#### Inteligentne Rekomendacje
System automatycznie wykrywa technologie w projekcie i rekomenduje odpowiednie narzędzia:
- **React/Node.js** → Serena, Context7, GitHub
- **Python** → Serena, PostgreSQL, Brave Search
- **Docker** → Context7, K8s tools

#### Kategorie Narzędzi
1. **Development & Code** - Serena, Context7, GitHub, Brave Search
2. **Testing & Quality** - Playwright, Jest, Puppeteer
3. **Database & APIs** - PostgreSQL, SQLite, Fetch
4. **Cloud & Infrastructure** - AWS, Google Cloud, Docker
5. **AI & Machine Learning** - Time, Memory tools
6. **Productivity & System** - Calendar, File operations

## 🛠️ Najważniejsze Narzędzia

### 🔍 Serena (Rekomendowane)
**Opis**: Nawigacja po kodzie i analiza projektów
**Instalacja**: Automatyczna via git+uv
**Technologie**: Python, TypeScript, Java, Rust, Go, C++

```bash
# Wybierz [s] w menu głównym lub [1] -> wybierz Serena
```

### 🧠 Context7 (Rekomendowane)
**Opis**: Zaawansowana generacja kodu i dokumentacji
**Instalacja**: Docker
**Technologie**: Node.js, TypeScript, Python, React, Angular, Vue

```bash
# Wybierz [c] w menu głównym lub [1] -> wybierz Context7
```

### 📁 GitHub
**Opis**: Zarządzanie repositoriami i operacje Git
**Instalacja**: npm
**Użycie**: Operacje na GitHub API

## 🔧 Instalacja Narzędzi

### Automatyczna Instalacja
1. Uruchom `./mcp-tools.sh`
2. Wybierz narzędzie z menu
3. System automatycznie:
   - Sprawdzi zależności
   - Pobierze i zainstaluje narzędzie
   - Skonfiguruje dla Claude

### Ręczna Instalacja (przykład Serena)

```bash
# 1. Klonowanie repository
git clone https://github.com/oraios/serena ~/tools/serena

# 2. Instalacja (wymaga uv)
cd ~/tools/serena
uv install

# 3. Test
uv run serena-mcp-server --help
```

## 📊 Diagnostyka

### Health Check
```bash
# W menu wybierz [h]
```

Sprawdzi:
- ✅ Status zainstalowanych narzędzi
- ✅ Konfigurację Claude
- ✅ Zależności systemowe
- ✅ Wykryte technologie projektu

### System Status
```
MCP Tools Status:
serena          ❌ NOT INST   Code Navigation & Project Analysis
context7        ❌ NOT INST   Advanced Code Generation & Documentation
github          ✅ INSTALLED  Repository Management & Git Operations

Project Analysis:
  📁 Project: my_name_is_claude
  📍 Path: /mnt/e/AI/my_name_is_claude
  🔧 Detected Technologies:
     • nodejs
     • react
     • python
```

## 🚨 Rozwiązywanie Problemów

### Problem: Pusty ekran w menu
**Przyczyna**: Brak pliku registry extended.json
**Rozwiązanie**:
```bash
cp .mcp-tools/registry/extended.json ~/.mcp-tools/registry/
```

### Problem: "Limited Mode"
**Przyczyna**: Brak jq
**Rozwiązanie**:
```bash
sudo apt install jq  # Ubuntu/Debian
brew install jq       # MacOS
```

### Problem: Docker errors dla Context7
**Przyczyna**: Docker nie jest uruchomiony
**Rozwiązanie**:
```bash
sudo systemctl start docker  # Linux
# lub uruchom Docker Desktop
```

### Problem: "Command not found" dla npm narzędzi
**Przyczyna**: Brak Node.js/npm
**Rozwiązanie**:
```bash
# Instalacja Node.js
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Problem: Serena nie instaluje się
**Przyczyna**: Brak uv (Python package manager)
**Rozwiązanie**:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 💡 Najlepsze Praktyki

### 1. Rozpocznij od Podstawowych Narzędzi
- **Serena** - dla nawigacji po kodzie
- **Context7** - dla generacji kodu
- **GitHub** - dla operacji git

### 2. Dopasuj do Technologii
- **React/Vue** → Context7, Playwright
- **Python** → Serena, PostgreSQL
- **APIs** → Fetch, Brave Search

### 3. Sprawdzaj Health Check
Regularnie uruchamiaj `[h]` aby monitorować status narzędzi.

### 4. Wykorzystaj Smart Recommendations
System automatycznie sugeruje najlepsze narzędzia dla twojego projektu.

## 🔗 Linki i Zasoby

- **Serena**: https://github.com/oraios/serena
- **MCP Specification**: https://modelcontextprotocol.io/
- **Claude Code Framework**: [docs/README.md](../README.md)

## 📝 Notatki Końcowe

MCP Tools Manager jest integralną częścią Claude Code Multi-Agent Framework. Wszystkie narzędzia są automatycznie konfigurowane do współpracy z agentami framework'a dla maksymalnej efektywności.

Jeśli masz problemy nie opisane w tym przewodniku, sprawdź logi w `~/.mcp-tools/logs/` lub uruchom health check.