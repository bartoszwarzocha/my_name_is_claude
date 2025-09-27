# RZECZYWISTA Instrukcja Pracy z Frameworkiem Claude Code
## Projekt: BWX_SDK - Advanced C++ wxWidgets Extension Library
### Technologie: Modern C++20, wxWidgets, OpenGL, CMake, vcpkg

---

## 🎯 Przegląd Projektu

**Typ projektu**: Advanced C++ Library Development - SDK Extension for wxWidgets
**Stack technologiczny**: C++20, wxWidgets 3.2+, OpenGL 4.5+, CMake 3.20+, vcpkg
**Cel biznesowy**: Rozwój zaawansowanego SDK rozszerzającego wxWidgets o funkcje 3D, matematykę wektorową, zaawansowane komponenty GUI i cross-platform utilities
**Repozytorium**: https://github.com/bartoszwarzocha/bwx_sdk

---

## 📋 KROK 1: Przygotowanie Istniejącego Projektu BWX_SDK

### 1.1 Klonowanie Istniejącego Repozytorium

```bash
# Sklonuj istniejące repozytorium BWX_SDK
cd /ścieżka/gdzie/chcesz/pracować
git clone https://github.com/bartoszwarzocha/bwx_sdk.git
cd bwx_sdk

# Sprawdź aktualną strukturę
ls -la
```

**Istniejąca struktura BWX_SDK:**
```
bwx_sdk/
├── CMakeLists.txt
├── vcpkg.json
├── src/
│   ├── bwx_core/
│   ├── bwx_gl/
│   ├── bwx_gui/
│   ├── bwx_utils/
│   └── bwx_adv/ (w przygotowaniu)
├── include/
├── tests/
├── examples/
├── docs/
└── scripts/
```

### 1.2 Kopiowanie Frameworka do Istniejącego Projektu

**NAJWAŻNIEJSZY KROK:** Framework musi być skopiowany do istniejącego projektu BWX_SDK:

```bash
# WAŻNE: Wykonaj backup przed kopiowaniem frameworka
git add . && git commit -m "Backup before framework integration"

# Kopiuj framework do BWX_SDK
/mnt/e/AI/my_name_is_claude/copy_framework_to_project.sh /ścieżka/do/bwx_sdk --backup

# LUB z wymuszeniem bez pytań:
/mnt/e/AI/my_name_is_claude/copy_framework_to_project.sh /ścieżka/do/bwx_sdk --force --backup
```

**Po skopiowaniu BWX_SDK będzie zawierał dodatkowo:**
```
bwx_sdk/
├── (existing BWX_SDK files...)
├── .ai-tools/          # AI Tools (bez venv/)
├── .claude/            # Agenci, prompty, hooks, templates
├── .mcp-tools/         # MCP tools configuration
├── ai-tools.sh         # Główne narzędzie AI
├── mcp-tools.sh        # Zarządzanie MCP tools
├── CLAUDE_template.md  # Template konfiguracji (DO EDYCJI!)
├── FRAMEWORK_README.md # Dokumentacja frameworka
├── FRAMEWORK_LICENSE   # Licencja frameworka
└── copy_framework_to_project.sh
```

---

## 📝 KROK 2: Konfiguracja BWX_SDK dla Frameworka

### 2.1 Tworzenie Specjalistycznego CLAUDE.md

```bash
# W katalogu bwx_sdk
cp CLAUDE_template.md CLAUDE.md

# Edytuj CLAUDE.md specjalnie dla BWX_SDK
nano CLAUDE.md  # lub Visual Studio Code
```

**Dostosuj CLAUDE.md dla zaawansowanego C++ SDK:**

```markdown
# CLAUDE.md – BWX_SDK Advanced C++ Extension Library

## Project Metadata
- **project_name**: "bwx_sdk"
- **project_description**: "Advanced C++ SDK extending wxWidgets with 3D graphics, mathematical utilities, cross-platform components and professional development tools"
- **project_version**: "2.0.0"
- **primary_language**: "cpp"
- **business_domain**: "sdk_development"
- **project_scale**: "enterprise"
- **development_stage**: "advanced_development"

## Project Overview
Professional C++ SDK that extends wxWidgets with advanced capabilities:
- Modern C++20 architecture with template metaprogramming
- OpenGL 4.5+ integration for high-performance 3D graphics
- Mathematical libraries for vector operations and computational geometry
- Cross-platform desktop components with native performance
- Professional CAD-like utilities and advanced visualization tools

**Core Capabilities**:
- bwx_core: Fundamental utilities with modern C++ patterns
- bwx_gl: OpenGL 4.5+ wrapper with shader management
- bwx_gui: Advanced wxWidgets extensions and custom components
- bwx_utils: Cross-platform utilities and helper functions
- bwx_adv: Professional tools and CAD-like features (in development)
- bwx_math: Mathematical libraries for 3D graphics and algorithms

**Goals**:
- Provide professional-grade wxWidgets extensions
- Enable high-performance 3D graphics in wxWidgets applications
- Streamline cross-platform C++ desktop development
- Offer comprehensive mathematical and geometric utilities
- Support enterprise-level application development

## Technologies
**Core**: Modern C++20, STL containers, template metaprogramming, RAII patterns
**GUI Framework**: wxWidgets 3.2+, custom component architecture, event system extensions
**Graphics**: OpenGL 4.5+ core profile, GLEW, modern shader pipeline, GLM mathematics
**Build System**: CMake 3.20+, vcpkg dependency management, cross-platform builds
**Platforms**: Windows (MSVC 2019+), Linux (GCC 11+/Clang 12+), macOS (Clang 12+) with OpenGL limitations
**Libraries**: GLM for mathematics, JSON parsing utilities, i18n support, command-line parsing
**Quality**: Google Test framework, Doxygen documentation, GitHub Actions CI/CD, static analysis tools
**Performance**: Memory-efficient algorithms, GPU optimization, minimal overhead design

## Agents and Roles
**Specialized Development**: graphics-3d-engineer, desktop-specialist, math-specialist, cad-engineer
**Core Development**: backend-engineer, software-architect
**Quality & Operations**: qa-engineer, security-engineer, deployment-engineer
**Strategy**: product-manager, business-analyst (for SDK roadmap)

Agent competencies defined in `.claude/agents/` directory with specialized focus on:
- Advanced C++ development patterns
- OpenGL and 3D graphics programming
- Mathematical algorithm implementation
- wxWidgets extension development
- Cross-platform SDK architecture

## Specialized Requirements
**Graphics Programming**: OpenGL 4.5+ core profile, modern shader pipeline, 3D mathematics, GPU memory management
**SDK Architecture**: API stability, backward compatibility, extensible plugin system, minimal dependencies
**Mathematical Computing**: Linear algebra operations, computational geometry, optimization algorithms, precision mathematics
**Cross-Platform Development**: Platform abstraction layers, build system portability, native performance optimization
**Professional Tools**: CAD-like utilities, advanced visualization, industrial-grade components

## TODO Management
**Enabled**: true
**Hierarchy**: hierarchical
**Tracking**: enterprise
**Coordination**: true
**Specialized Tracking**:
- Module-based task organization (bwx_core, bwx_gl, bwx_gui, etc.)
- Cross-platform development coordination
- Performance optimization tracking
- API stability validation
```

### 2.2 Dostosowanie do Istniejącej Struktury BWX_SDK

**Dodaj sekcje specyficzne dla BWX_SDK:**

```markdown
## BWX_SDK Module Architecture
**bwx_core**: Fundamental C++ utilities, RAII wrappers, cross-platform abstractions
**bwx_gl**: OpenGL 4.5+ integration, shader management, 3D rendering pipeline
**bwx_gui**: wxWidgets extensions, custom components, advanced event handling
**bwx_utils**: Supplementary utilities, JSON parsing, command-line tools
**bwx_adv**: Professional CAD-like features, advanced modeling tools (in development)
**bwx_math**: Mathematical libraries, vector operations, computational geometry

## Cross-Platform Considerations
**Windows**: MSVC 2019+, DirectX interop possibilities, Windows-specific optimizations
**Linux**: GCC 11+/Clang 12+, X11/Wayland support, Linux packaging
**macOS**: Clang 12+, OpenGL deprecation handling, Metal future-proofing

## Performance Requirements
**Memory Management**: Efficient RAII patterns, minimal heap allocations, smart pointer usage
**Graphics Performance**: GPU optimization, efficient vertex buffer management, shader caching
**API Overhead**: Minimal function call overhead, template-based optimizations
**Build Performance**: Fast compilation with PCH, modular architecture
```

---

## 🔧 KROK 3: Inicjalizacja AI Tools dla C++ SDK

### 3.1 Setup AI Tools dla Zaawansowanego C++ Development

```bash
# W katalogu bwx_sdk
./ai-tools.sh
```

**AI Tools dla C++ SDK:**
1. **Automatic C++ Environment Detection**: Framework wykryje C++20, CMake, vcpkg
2. **Specialized Agent Selection**: Automatycznie dobierze agentów dla graphics, desktop, math
3. **Module-Based Analysis**: Przeanalizuje strukturę modułów BWX_SDK
4. **Cross-Platform Setup**: Skonfiguruje dla Windows/Linux/macOS development

**Przykładowy Output dla BWX_SDK:**
```
===============================================================================
🧠 AI TOOLS LAUNCHER v1.0.0
Claude Code Multi-Agent Framework - AI-Powered Development Tools
===============================================================================

Analyzing BWX_SDK Project...
✅ C++20 project detected
✅ CMake build system found
✅ vcpkg dependencies configured
✅ OpenGL integration detected
✅ wxWidgets extensions identified

Setting up specialized environment for C++ SDK development...
```

### 3.2 Automatyczna Detekcja Specjalistycznych Agentów

**Framework automatycznie wykryje i zaproponuje:**

1. **graphics-3d-engineer** (PRIMARY dla bwx_gl)
   - OpenGL 4.5+ core profile expertise
   - Modern shader pipeline development
   - 3D mathematics and GPU optimization
   - Graphics debugging and profiling

2. **desktop-specialist** (PRIMARY dla bwx_gui)
   - wxWidgets advanced components
   - Cross-platform GUI development
   - Event system extensions
   - Native platform integration

3. **math-specialist** (PRIMARY dla bwx_math)
   - Linear algebra algorithms
   - Computational geometry
   - Mathematical optimization
   - Precision mathematics

4. **backend-engineer** (CORE dla bwx_core)
   - Modern C++20 patterns
   - Template metaprogramming
   - Memory management optimization
   - Cross-platform abstraction

5. **cad-engineer** (ADVANCED dla bwx_adv)
   - CAD-like utilities development
   - Advanced 3D modeling tools
   - Professional visualization
   - Industrial-grade components

6. **software-architect** (STRATEGIC)
   - SDK architecture design
   - API stability and versioning
   - Plugin system development
   - Cross-module coordination

7. **qa-engineer** (QUALITY)
   - C++ testing strategies
   - Cross-platform validation
   - Performance benchmarking
   - API stability testing

**Agent Matrix dla BWX_SDK:**
```
Module Ownership:
bwx_core  → backend-engineer + software-architect
bwx_gl    → graphics-3d-engineer + math-specialist
bwx_gui   → desktop-specialist + software-architect
bwx_utils → backend-engineer
bwx_adv   → cad-engineer + graphics-3d-engineer
bwx_math  → math-specialist + backend-engineer

Cross-Module: software-architect + qa-engineer
```

---

## 📊 KROK 4: Project Analysis dla BWX_SDK

### 4.1 Zaawansowana Analiza SDK

```bash
# W menu AI Tools wybierz [2] Project Analysis
./ai-tools.sh → [2]
```

**Framework przeanalizuje specjalistyczne aspekty BWX_SDK:**

```
📊 BWX_SDK PROJECT HEALTH ANALYSIS

Project: bwx_sdk v2.0.0
Type: Advanced C++ SDK
Status: 🟢 Active Development

Module Health Analysis:
✅ bwx_core: Stable, good C++20 patterns
✅ bwx_gl: OpenGL 4.5+ ready, needs shader optimization
⚠️ bwx_gui: wxWidgets 3.2+ compatible, needs more components
✅ bwx_utils: Stable utilities, JSON integration ready
⚠️ bwx_adv: In development, needs CAD features
🟡 bwx_math: Partially implemented, needs optimization

Technology Stack Assessment:
✅ C++20 Features: Proper concepts, ranges, coroutines ready
✅ CMake 3.20+: Modern CMake patterns
✅ vcpkg Integration: Dependency management working
✅ OpenGL 4.5+: Core profile compatible
⚠️ Cross-Platform: macOS OpenGL limitations detected
✅ wxWidgets 3.2+: Compatible with latest features

Build System Health:
✅ Windows (MSVC): Ready for development
✅ Linux (GCC/Clang): Cross-compilation configured
⚠️ macOS: OpenGL deprecation considerations needed

Recommended Agent Actions:
1. graphics-3d-engineer: Optimize OpenGL pipeline in bwx_gl
2. math-specialist: Complete mathematical utilities in bwx_math
3. cad-engineer: Implement advanced features in bwx_adv
4. software-architect: Review cross-module dependencies
5. qa-engineer: Setup cross-platform testing
```

### 4.2 Module-Specific Analysis

**Framework analizuje każdy moduł osobno:**

```bash
# Analiza modułu bwx_gl:
./ai-tools.sh → [2] → Module Analysis → bwx_gl

# graphics-3d-engineer provides detailed analysis:
- OpenGL context management
- Shader compilation pipeline
- Vertex buffer optimization
- Graphics debugging tools
- GPU memory management
```

---

## 🧙 KROK 5: Advanced C++ Development Workflows

### 5.1 Module Development Workflow

**Przykład: Rozwój bwx_gl modułu (graphics-3d-engineer lead)**

```bash
# Konsultacja z graphics-3d-engineer:
"Graphics-3d-engineer potrzebuję zaawansowany shader manager dla bwx_gl modułu."
```

**Agent guides przez:**
1. **Modern OpenGL Architecture Design**:
   ```cpp
   namespace bwx::gl {
       class ShaderManager {
           // RAII shader management
           // Hot-reload capabilities
           // Error handling with exceptions
           // GPU memory optimization
       };
   }
   ```

2. **C++20 Implementation Patterns**:
   ```cpp
   // Concepts dla type safety
   template<ShaderType T>
   class Shader { /* ... */ };

   // Ranges dla shader processing
   auto compile_shaders(const std::vector<ShaderSource>& sources)
       -> std::vector<CompiledShader>;
   ```

3. **Cross-Platform Optimization**:
   ```cpp
   #ifdef _WIN32
   // Windows-specific OpenGL optimizations
   #elif __linux__
   // Linux-specific optimizations
   #elif __APPLE__
   // macOS OpenGL compatibility layers
   #endif
   ```

### 5.2 Mathematical Algorithm Development (math-specialist lead)

```bash
# Konsultacja z math-specialist:
"Math-specialist implementuj zaawansowane operacje wektorowe dla bwx_math."
```

**Agent implementuje:**
```cpp
namespace bwx::math {
    // Modern C++20 mathematical utilities
    template<arithmetic T, size_t N>
    class Vector {
        // SIMD optimizations
        // Template specializations
        // Constexpr calculations
    };

    // Computational geometry algorithms
    class GeometryEngine {
        // Boolean operations
        // Mesh algorithms
        // Collision detection
    };
}
```

### 5.3 GUI Component Development (desktop-specialist lead)

```bash
# Zaawansowane komponenty wxWidgets:
"Desktop-specialist stwórz professional visualization panel dla bwx_gui."
```

**Agent tworzy:**
```cpp
namespace bwx::gui {
    class AdvancedVisualizationPanel : public wxPanel {
        // OpenGL integration z bwx_gl
        // Event handling extensions
        // Professional tools integration
        // Customizable interface
    };
}
```

---

## 🔄 KROK 6: Multi-Agent Coordination dla SDK

### 6.1 Cross-Module Feature Development

**Przykład: Zaawansowany 3D Viewer (multi-agent coordination)**

```
Feature: Professional 3D Model Viewer
Agents Coordination:
1. software-architect → Overall architecture design
2. graphics-3d-engineer → OpenGL rendering backend (bwx_gl)
3. math-specialist → 3D mathematics support (bwx_math)
4. desktop-specialist → wxWidgets UI integration (bwx_gui)
5. cad-engineer → Professional tools integration (bwx_adv)
6. qa-engineer → Cross-platform testing strategy
```

**TodoWrite Hierarchy:**
```
Epic: Professional 3D Model Viewer
├── Architecture Design (software-architect)
│   ├── ✅ Component interface design
│   ├── ✅ Module dependency analysis
│   └── 🔄 Plugin architecture specification
├── Graphics Backend (graphics-3d-engineer)
│   ├── ✅ OpenGL 4.5+ renderer implementation
│   ├── 🔄 Shader pipeline optimization
│   └── ⏳ GPU memory management
├── Mathematical Foundation (math-specialist)
│   ├── ✅ 3D transformation matrices
│   ├── 🔄 Projection calculations
│   └── ⏳ Optimization algorithms
├── GUI Integration (desktop-specialist)
│   ├── ⏳ wxWidgets OpenGL canvas
│   ├── ⏳ Professional toolbar design
│   └── ⏳ Event handling integration
├── Advanced Features (cad-engineer)
│   ├── ⏳ Model manipulation tools
│   ├── ⏳ Measurement utilities
│   └── ⏳ Export/import capabilities
└── Quality Assurance (qa-engineer)
    ├── ⏳ Cross-platform testing
    ├── ⏳ Performance benchmarking
    └── ⏳ Memory leak detection
```

### 6.2 Automatic Agent Handoffs

**Framework automatycznie przekazuje pracę:**

```
Workflow: OpenGL Feature Implementation
1. graphics-3d-engineer implements core OpenGL functionality
   ↓ (automatic handoff via TodoWrite)
2. math-specialist provides mathematical foundation
   ↓ (shared context)
3. desktop-specialist creates wxWidgets integration
   ↓ (dependency completion)
4. qa-engineer validates cross-platform compatibility
```

---

## 🔍 KROK 7: Quality Assurance dla C++ SDK

### 7.1 Advanced C++ Quality Gates

```bash
# Quality validation dla C++ SDK:
./ai-tools.sh → [5] Quality Validator
```

**Framework checks:**
- **Modern C++20 Compliance**: Concepts, ranges, coroutines usage
- **Memory Safety**: RAII patterns, smart pointer usage, leak detection
- **API Stability**: ABI compatibility, versioning compliance
- **Cross-Platform**: Build validation across Windows/Linux/macOS
- **Performance**: Benchmarking, profiling, optimization opportunities
- **Graphics Validation**: OpenGL error checking, shader compilation
- **Mathematical Accuracy**: Numerical precision, algorithm correctness

### 7.2 Specialized Testing Strategies (qa-engineer)

**C++ SDK Testing:**
```cpp
// Google Test framework integration
namespace bwx::test {
    class GraphicsTestSuite : public ::testing::Test {
        // OpenGL context setup
        // Graphics rendering validation
        // Performance benchmarking
    };

    class MathTestSuite : public ::testing::Test {
        // Numerical accuracy testing
        // Algorithm validation
        // Performance measurements
    };

    class GUITestSuite : public ::testing::Test {
        // wxWidgets component testing
        // Cross-platform validation
        // Event handling verification
    };
}
```

**Cross-Platform Testing Matrix:**
```bash
# Automated testing across platforms
./ai-tools.sh → Advanced Tools → Cross-Platform Testing

# Framework executes:
# Windows (MSVC): Full test suite + Windows-specific features
# Linux (GCC/Clang): Full test suite + Linux optimizations
# macOS (Clang): Test suite + OpenGL compatibility checks
```

---

## 🚀 KROK 8: Advanced SDK Features

### 8.1 Plugin Architecture Development (software-architect)

```bash
# Advanced SDK architecture:
"Software-architect design plugin system dla BWX_SDK extension."
```

**Plugin System Implementation:**
```cpp
namespace bwx::plugin {
    class PluginManager {
        // Dynamic loading capabilities
        // Version compatibility checking
        // Dependency resolution
        // Hot-swap functionality
    };

    template<typename Interface>
    class Plugin {
        // Type-safe plugin interface
        // Automatic registration
        // Lifecycle management
    };
}
```

### 8.2 Professional Tools Development (cad-engineer)

```bash
# CAD-like features dla bwx_adv:
"CAD-engineer implement professional modeling tools dla bwx_adv module."
```

**Professional Tools Implementation:**
```cpp
namespace bwx::cad {
    class ModelingToolkit {
        // Boolean operations on meshes
        // Parametric modeling support
        // Constraint solving
        // History-based operations
    };

    class MeasurementTools {
        // Precision measurements
        // Annotation system
        // Drawing tools
        // Export capabilities
    };
}
```

### 8.3 Performance Optimization (multi-agent)

**Performance-focused development:**
```bash
# Performance optimization session:
"Graphics-3d-engineer + math-specialist optimize rendering performance."
```

**Optimization Areas:**
- **GPU Optimization**: Vertex buffer streaming, shader caching
- **CPU Optimization**: SIMD instructions, template optimizations
- **Memory Optimization**: Pool allocators, cache-friendly data structures
- **Algorithm Optimization**: Spatial data structures, culling algorithms

---

## 📦 KROK 9: SDK Distribution & Packaging

### 9.1 CMake Packaging Enhancement

```bash
# Advanced packaging configuration:
"Software-architect + deployment-engineer setup professional SDK packaging."
```

**Professional CMake Setup:**
```cmake
# Modern CMake 3.20+ patterns
find_package(PkgConfig REQUIRED)
find_package(wxWidgets REQUIRED COMPONENTS core base gl)
find_package(OpenGL REQUIRED)
find_package(glfw3 REQUIRED)

# SDK export configuration
include(CMakePackageConfigHelpers)
export(TARGETS bwx_core bwx_gl bwx_gui bwx_utils bwx_math
       FILE "${CMAKE_CURRENT_BINARY_DIR}/bwx_sdkTargets.cmake")

# vcpkg integration
set(CMAKE_TOOLCHAIN_FILE "${VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake")
```

### 9.2 Cross-Platform Distribution

**Multi-Platform Packages:**
```bash
# Framework-assisted packaging:
./ai-tools.sh → Advanced Tools → SDK Distribution

# Generates:
# Windows: .lib/.dll packages + NuGet packages
# Linux: .so packages + .deb/.rpm packages
# macOS: .dylib packages + Homebrew formula
# Source: Header-only distribution option
```

---

## 🔄 KROK 10: Continuous Development & Evolution

### 10.1 SDK Roadmap Management

**Framework-assisted roadmap:**
```bash
# Long-term SDK planning:
"Product-manager + software-architect create BWX_SDK 3.0 roadmap."
```

**Evolution Areas:**
- **Vulkan Integration**: Modern graphics API support
- **Metal Support**: macOS high-performance graphics
- **WebAssembly**: Browser-based SDK applications
- **AI Integration**: ML-powered CAD features
- **Cloud Integration**: Collaborative modeling tools

### 10.2 Community & Open Source

**Professional Open Source Management:**
```bash
# Community-ready SDK:
./ai-tools.sh → Advanced Tools → Open Source Preparation

# Framework assists with:
# - Documentation generation
# - Example project creation
# - Contribution guidelines
# - Issue template creation
# - Release automation
```

### 10.3 Enterprise Features

**Enterprise SDK Extensions:**
- **Professional Support**: Technical consulting with agent assistance
- **Custom Modules**: Specialized industry modules
- **Integration Services**: Enterprise application integration
- **Training Programs**: BWX_SDK development training

---

## 🔧 BWX_SDK Specific Commands & Workflows

### Essential BWX_SDK Commands
```bash
# Framework setup for existing BWX_SDK:
/mnt/e/AI/my_name_is_claude/copy_framework_to_project.sh /path/to/bwx_sdk --backup

# Setup specialized C++ environment:
cp CLAUDE_template.md CLAUDE.md
# Edit CLAUDE.md with BWX_SDK specific configuration

# Initialize AI Tools dla C++ SDK:
./ai-tools.sh

# Module-specific development:
# AI Tools automatically detects module context and assigns appropriate agents

# Advanced C++ analysis:
./ai-tools.sh → [2] Project Analysis → Advanced C++ Analysis

# Cross-platform testing:
./ai-tools.sh → Advanced Tools → Cross-Platform Testing

# Performance profiling:
./ai-tools.sh → Advanced Tools → Performance Analysis
```

### Specialized Agent Workflows dla BWX_SDK
```bash
# Graphics development (graphics-3d-engineer):
"Graphics-3d-engineer optimize OpenGL rendering pipeline dla bwx_gl"

# Mathematical development (math-specialist):
"Math-specialist implement SIMD-optimized vector operations dla bwx_math"

# GUI development (desktop-specialist):
"Desktop-specialist create professional toolbar system dla bwx_gui"

# CAD development (cad-engineer):
"CAD-engineer implement Boolean operations dla bwx_adv"

# Architecture review (software-architect):
"Software-architect review API stability across all BWX_SDK modules"

# Quality assurance (qa-engineer):
"QA-engineer setup comprehensive testing dla cross-platform SDK validation"
```

### Module-Specific Development Sessions
```bash
# Module ownership coordination:
# bwx_core  → backend-engineer lead
# bwx_gl    → graphics-3d-engineer lead
# bwx_gui   → desktop-specialist lead
# bwx_utils → backend-engineer lead
# bwx_adv   → cad-engineer lead
# bwx_math  → math-specialist lead

# Cross-module features automatically coordinate multiple agents
# Framework ensures API consistency across modules
```

---

## 📚 BWX_SDK Advanced Resources

### Specialized Documentation
```bash
# Framework-generated BWX_SDK docs:
# FRAMEWORK_README.md - Complete framework integration guide
# .claude/agents/custom/graphics/ - Graphics development agents
# .claude/agents/custom/desktop/ - Desktop application agents
# .claude/agents/custom/hardware/ - CAD and professional tools agents
# .claude/prompts/agents/cpp/ - C++ development prompts
# .claude/prompts/agents/graphics/ - Graphics programming prompts
```

### Performance & Profiling Tools
```bash
# Framework-integrated profiling:
./ai-tools.sh → Advanced Tools → Performance Profiling
./ai-tools.sh → Advanced Tools → Memory Analysis
./ai-tools.sh → Advanced Tools → Graphics Debugging

# Cross-platform build validation:
./ai-tools.sh → Advanced Tools → Build Matrix Testing
```

### MCP Integration dla C++ SDK
```bash
# Enhanced C++ development with MCP tools:
./mcp-tools.sh setup

# Serena for code indexing and context management
# Context7 for advanced C++ code analysis
# Custom MCP tools dla specialized C++ workflows
```

---

## 🎯 BWX_SDK Summary

**Rzeczywisty Advanced C++ SDK Workflow:**
1. **Framework Integration**: `copy_framework_to_project.sh` do istniejącego BWX_SDK
2. **Specialized Configuration**: CLAUDE.md dostosowany dla advanced C++ SDK development
3. **Multi-Agent Coordination**: Specialized agents dla graphics, math, CAD, desktop development
4. **Module-Based Development**: Agent ownership per module z cross-module coordination
5. **Professional Quality**: Enterprise-grade testing, cross-platform validation, performance optimization
6. **SDK Evolution**: Continuous improvement z agent-guided development

**Kluczowe różnice dla zaawansowanego C++ SDK:**
- ✅ Specialized agents dla graphics programming, mathematical computing, CAD development
- ✅ Module-based agent assignment z cross-module coordination
- ✅ Advanced C++20 patterns i template metaprogramming guidance
- ✅ Cross-platform development z platform-specific optimizations
- ✅ Professional SDK architecture z API stability focus
- ✅ Performance-focused development z GPU optimization
- ✅ Enterprise-grade quality assurance i testing strategies

BWX_SDK jest teraz gotowy do enterprise-level development z pełnym wsparciem frameworka Claude Code Multi-Agent!

---

**Wersja Instrukcji**: 2.0 (RZECZYWISTA dla BWX_SDK)
**Framework Version**: 3.1.0
**BWX_SDK Target Version**: 2.0.0+
**Data**: Wrzesień 2025
**Status**: Advanced C++ SDK Ready

---

*Ta instrukcja bazuje na rzeczywistym działaniu frameworka z istniejącym projektem BWX_SDK i została dostosowana dla zaawansowanego C++ SDK development.*