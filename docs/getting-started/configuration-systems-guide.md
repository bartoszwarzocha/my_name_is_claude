# Configuration Systems Guide - v3.3.0 Features

**⚠️ WAŻNE**: Funkcjonalności opisane poniżej to **KONFIGURACJE I SPECYFIKACJE ARCHITEKTONICZNE**, nie automatyczne mechanizmy. Wymagają one implementacji w Claude Code CLI lub ręcznego zastosowania.

## Co dostałeś w v3.3.0?

Wprowadzone w v3.3.0 systemy to **szczegółowe plany i konfiguracje** pokazujące JAK powinny działać zaawansowane funkcje. Pomyśl o nich jak o **blueprintach dla przyszłej integracji z Claude Code**.

---

## 1. 💰 Model Configuration System (Konfiguracje Kosztów)

### Co to jest?
System trzech profili (Fast/Balanced/Quality) do optymalizacji kosztów API poprzez inteligentny wybór modelu Claude.

### Gdzie to znajdziesz?
```
.claude/config/
├── model-profiles.json          # Definicje profili
├── agent-model-mapping.json     # Mapowanie agentów
├── cost-optimization.json       # Ustawienia budżetu
├── README.md                    # Dokumentacja
└── integration-guide.md         # Przewodnik integracji
```

### Jak z tego korzystać TERAZ?

**Opcja A: Manualne stosowanie (dostępne teraz)**
1. Przeczytaj `.claude/config/README.md`
2. Zobacz które agenty używają jakich profili w `agent-model-mapping.json`
3. Ręcznie wybieraj profile przy pracy:
   - Proste zadania → Fast (Haiku)
   - Większość pracy → Balanced (Sonnet)
   - Krytyczne decyzje → Quality (Opus)

**Opcja B: Referencyjna wiedza**
- Używaj jako przewodnika do manualnej optymalizacji kosztów
- Oblicz potencjalne oszczędności z `work/model-config-tests/cost-calculator.sh`
- Ucz się pattern'ów optymalnego użycia modeli

**Przyszłość:** Gdy Claude Code CLI wspiera automatyczną selekcję modeli, te konfiguracje będą gotowe do użycia.

### Przykład użycia
```bash
# TERAZ - manualnie
"Potrzebuję prostej zmiany w dokumentacji" → użyj Fast/Haiku
"Projektuję architekturę systemu" → użyj Quality/Opus

# PRZYSZŁOŚĆ - automatycznie (gdy CLI wspiera)
claude code --profile fast "Update README"
claude code --profile quality "Design database schema"
```

---

## 2. 🎨 Output Styles System (Style Komunikacji)

### Co to jest?
Cztery wyspecjalizowane style komunikacji dla różnych odbiorców.

### Gdzie to znajdziesz?
```
.claude/config/
├── output-styles.json           # Definicje stylów
└── output-styles-guide.md       # Przewodnik szybki
```

### Style dostępne:
- **Technical** - Dla developerów (szczegółowy, z kodem)
- **Executive** - Dla zarządu (ROI, high-level)
- **Educational** - Dla uczących się (krok po kroku)
- **Code Review** - Dla reviewerów (zwięzły, actionable)

### Jak z tego korzystać TERAZ?

**Używaj jako wzorców komunikacji:**
1. Przeczytaj przykłady w `.claude/config/output-styles-guide.md`
2. Gdy komunikujesz się z różnymi stakeholderami, świadomie dobieraj styl:
   - Z developerami → Technical (dużo kodu, szczegóły)
   - Z managerem → Executive (ROI, timeline, biznes)
   - Przy nauce → Educational (wyjaśnienia, przykłady)
   - W code review → Code Review (konkretnie, przed/po)

**Przyszłość:** Automatyczna selekcja stylu bazująca na kontekście.

---

## 3. 🔄 Advanced Checkpoint System (System Punktów Kontrolnych)

### Co to jest?
Architektura wielopoziomowego systemu checkpoint'ów z semantycznym rollback'iem.

### Gdzie to znajdziesz?
```
.claude/config/
├── checkpoint-system.json       # Specyfikacja systemu
.claude/checkpoints/             # Struktura katalogów (gitignored)
├── agent_execution/             # Checkpointy per agent
├── quality_gate/                # Przed walidacją
├── commit_preparation/          # Przed commitami
└── manual/                      # Użytkownik

```

### Jak z tego korzystać TERAZ?

**Ręcznie zarządzaj stanem:**
1. **Przed krytycznymi operacjami:**
   ```bash
   # Zrób kopię przed dużą zmianą
   cp -r src/ backups/before_refactoring_$(date +%Y%m%d_%H%M%S)/
   ```

2. **Git jako checkpoints:**
   ```bash
   # Frequent commits jako checkpoints
   git commit -m "Checkpoint: before implementing auth"
   git commit -m "Checkpoint: tests passing"
   ```

3. **Branch jako safety net:**
   ```bash
   # Nowy feature branch przed ryzykowną zmianą
   git checkout -b feature/risky-change
   ```

**Przyszłość:** Automatyczne checkpointy przed każdą operacją agenta.

---

## 4. ⚡ Parallel Agent Execution (Równoległe Agenty)

### Co to jest?
Framework dla równoległego wykonywania wielu agentów (3x przyspieszenie).

### Gdzie to znajdziesz?
```
.claude/config/
└── parallel-agents.json         # Definicje teamów
```

### Pre-configured Teams:
- **Full-Stack Team** (4 agenty) - 3x speed
- **Architecture Team** (3 agenty) - 2.5x speed
- **Compliance Team** (3 agenty) - 2x speed
- **Operations Team** (4 agenty) - 2.5x speed
- **Data Team** (3 agenty) - 2x speed

### Jak z tego korzystać TERAZ?

**Planuj pracę sekwencyjnie, ale świadomie:**
1. Zobacz team templates w `parallel-agents.json`
2. Planuj swoje zadania w oparciu o dependencies:
   ```
   Frontend + Backend (równolegle) → QA → Deployment
   ```
3. Wykonuj pracę sekwencyjnie, ale organizuj ją tak, jakby była parallel

**Przyszłość:** Prawdziwe równoległe wykonywanie agentów.

---

## Podsumowanie: Jak używać v3.3.0?

### ✅ CO MOŻESZ ROBIĆ TERAZ:

1. **Model Configuration**
   - Czytaj i ucz się optymalnych pattern'ów
   - Manualnie wybieraj odpowiednie modele
   - Obliczaj potencjalne oszczędności

2. **Output Styles**
   - Stosuj wzorce komunikacji dla różnych odbiorców
   - Świadomie dostosowuj ton i szczegółowość
   - Używaj template'ów z guide'a

3. **Checkpoint System**
   - Używaj Git jako checkpoints
   - Robić manualne backupy przed ryzykownymi zmianami
   - Planuj recovery strategy

4. **Parallel Execution**
   - Planuj zadania z dependency awareness
   - Organizuj workflow bazując na team templates
   - Przygotuj się do przyszłej parallel execution

### ❌ CO NIE DZIAŁA AUTOMATYCZNIE:

- ❌ Automatyczna selekcja modelu
- ❌ Automatyczna zmiana stylu komunikacji
- ❌ Automatyczne checkpointy
- ❌ Równoległe wykonywanie agentów

### 🎯 WARTOŚĆ v3.3.0:

**To są blueprinty i best practices**, które:
- Pokazują JAK optymalizować koszty (50% savings możliwe)
- Uczą KIEDY używać którego modelu
- Definiują STYLE komunikacji dla różnych stakeholderów
- Projektują SYSTEM ochrony przed błędami
- Planują STRUKTURĘ równoległej pracy

**Gdy Claude Code CLI wdroży wsparcie dla tych funkcji, będziesz gotowy!**

---

## Następne kroki

1. **Przeczytaj dokumentację:**
   - `.claude/config/README.md` - Model Configuration
   - `.claude/config/output-styles-guide.md` - Style komunikacji
   - `CHANGELOG.md` - Pełne release notes v3.3.0

2. **Przetestuj narzędzia:**
   ```bash
   # Sprawdź testy systemu
   ./work/model-config-tests/test-suite.sh

   # Zobacz przykłady użycia
   ./work/model-config-tests/usage-examples.sh

   # Oblicz swoje koszty
   ./work/model-config-tests/cost-calculator.sh
   ```

3. **Zastosuj w praktyce:**
   - Używaj manualnie pattern'ów z konfiguracji
   - Stosuj style komunikacji z guide'a
   - Planuj workflow z dependency awareness

---

**Pytania?** Zobacz `CHANGELOG.md` dla pełnych release notes lub `FRAMEWORK_ROADMAP.md` dla planu dalszego rozwoju.
