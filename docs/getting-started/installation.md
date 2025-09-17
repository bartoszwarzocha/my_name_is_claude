# Instalacja Framework'a

## Wymagania Systemowe

### Minimalne Wymagania
- **Python**: 3.8 lub nowszy
- **System**: Windows 10+, macOS 10.15+, Linux (Ubuntu 18.04+)
- **Pamięć**: 4GB RAM
- **Dysk**: 2GB wolnego miejsca

### Rekomendowane
- **Python**: 3.11 lub nowszy
- **Pamięć**: 8GB+ RAM (dla AI features)
- **Dysk**: 5GB+ wolnego miejsca
- **Claude API**: Dostęp do Claude AI

## Instalacja Podstawowa

### 1. Klonowanie Framework'a

```bash
# Klonowanie repozytorium
git clone https://github.com/your-repo/claude-code-framework.git
cd claude-code-framework

# Sprawdzenie wersji
cat VERSION
```

### 2. Konfiguracja Python Environment

```bash
# Utworzenie virtual environment
python -m venv venv

# Aktywacja (Linux/macOS)
source venv/bin/activate

# Aktywacja (Windows)
venv\Scripts\activate
```

### 3. Instalacja Zależności (Opcjonalna)

```bash
# Podstawowe zależności (tylko jeśli potrzebne)
pip install psutil  # dla monitorowania systemu

# AI/ML zależności (opcjonalne, dla advanced features)
pip install numpy pandas scikit-learn
```

**Uwaga**: Framework został zaprojektowany tak, aby działać bez zewnętrznych zależności. Dodatkowe pakiety są opcjonalne.

## Instalacja AI Features

### Aktywacja AI-Powered Agent Selection

```bash
# Sprawdzenie dostępności AI tools
python .ai-tools/core/demo/demo_project_analyzer.py

# Testowanie podstawowych funkcjonalności
python -c "from ai_tools.core.data_collection_system import ProjectContextAnalyzer; print('AI Tools OK')"
```

### Konfiguracja CLAUDE.md

Skopiuj template konfiguracji:

```bash
cp CLAUDE_template.md CLAUDE.md
```

Dostosuj konfigurację w `CLAUDE.md`:

```yaml
# W sekcji Project Metadata
project_name: "your-project-name"
project_description: "Your project description"
primary_language: "python"  # lub typescript, java, etc.
business_domain: "web_development"  # lub fintech, healthcare, etc.
```

## Weryfikacja Instalacji

### Test Framework'a

```bash
# Test podstawowych funkcjonalności
python -c "
import sys
sys.path.append('.')
from ai_tools.core.testing_validation_framework import TestingValidationFramework
framework = TestingValidationFramework()
print('✅ Framework ready!')
"
```

### Test AI Capabilities

```bash
# Test AI agent selection
cd .ai-tools/core/demo
python demo_project_analyzer.py

# Powinno wyświetlić analizę projektu i rekomendacje agentów
```

### Health Check

```bash
# Test production deployment capabilities
python -c "
from ai_tools.core.production_deployment import ProductionDeploymentManager
manager = ProductionDeploymentManager()
health = manager.get_health_status()
print(f'System Status: {health[\"overall_status\"]}')
"
```

## Konfiguracja IDE

### VS Code

Zalecane rozszerzenia:

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-vscode.vscode-markdown",
    "streetsidesoftware.code-spell-checker"
  ]
}
```

### PyCharm

1. Otwórz katalog framework'a jako nowy projekt
2. Skonfiguruj Python interpreter na utworzony venv
3. Dodaj `ai_tools` do Python path

## Rozwiązywanie Problemów

### Problem: Błąd importu ai_tools

```bash
# Sprawdź ścieżkę Python
python -c "import sys; print('\n'.join(sys.path))"

# Dodaj framework root do PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Problem: Brak uprawnień do plików

```bash
# Linux/macOS
chmod +x .ai-tools/core/demo/demo_project_analyzer.py

# Windows - uruchom jako Administrator
```

### Problem: Błędy AI Features

```bash
# Sprawdź dostępność plików
ls -la .ai-tools/core/core/
ls -la .ai-tools/core/models/

# Test w trybie fallback
python -c "
from ai_tools.integration.ai_agent_selector import AIAgentSelector
selector = AIAgentSelector()
print('Fallback mode:', not selector.ai_enabled)
"
```

## Następne Kroki

Po zakończeniu instalacji:

1. **[Quick Start](quick-start.md)** - Pierwsze kroki z frameworkiem
2. **[First Project](first-project.md)** - Stwórz pierwszy projekt
3. **[User Guide](../user-guide/agents/overview.md)** - Poznaj agentów

## Wsparcie

Jeśli napotkasz problemy z instalacją:

- Sprawdź [Troubleshooting](../deployment/troubleshooting.md)
- Zgłoś problem na [GitHub Issues](https://github.com/your-repo/issues)
- Zadaj pytanie w [Community](../community.md)

---

*Ostatnia aktualizacja: 2025-09-16* | **Framework Version: 3.0.0**