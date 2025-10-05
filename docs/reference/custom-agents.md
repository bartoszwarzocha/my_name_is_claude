# Custom Agents Reference

*Complete reference for Custom Technology Stack Agents in My Name Is Claude framework*

## 🎯 Overview

Custom agents provide specialized expertise for specific technology stacks and domains, including graphics (2D/3D), hardware (embedded, electronics), desktop applications, and scientific computing.

For general development agents, see [Core Agents](core-agents.md).

---

## 🎨 Graphics & Visualization Agents

### **1. Graphics 3D Engineer** (`graphics-3d-engineer`)

**Expertise:** OpenGL, Vulkan, real-time rendering, game engines
**Model Profile:** Balanced (Sonnet)
**Use Cases:**
- 3D rendering engines
- Game development
- Real-time visualization
- GPU programming

**Location:** `.claude/agents/custom/graphics/graphics-3d-engineer.md`

---

### **2. Graphics 2D Engineer** (`graphics-2d-engineer`)

**Expertise:** Image processing, vector graphics, digital art tools
**Model Profile:** Balanced (Sonnet)
**Use Cases:**
- 2D graphics engines
- Image processing applications
- Vector graphics tools
- Digital art software

**Location:** `.claude/agents/custom/graphics/graphics-2d-engineer.md`

---

### **3. Math Specialist** (`math-specialist`)

**Expertise:** Numerical algorithms, scientific simulations, mathematical modeling
**Model Profile:** Balanced (Sonnet)
**Use Cases:**
- Mathematical libraries
- Scientific simulations
- Numerical analysis
- Algorithm optimization

**Location:** `.claude/agents/custom/graphics/math-specialist.md`

---

## ⚡ Hardware & Embedded Agents

### **4. Electronics Engineer** (`electronics-engineer`)

**Expertise:** Embedded hardware, PCB layouts, sensor integration, IoT
**Model Profile:** Balanced (Sonnet)
**Use Cases:**
- PCB design
- Sensor integration
- IoT device development
- Hardware prototyping

**Location:** `.claude/agents/custom/hardware/electronics-engineer.md`

---

### **5. Embedded Engineer** (`embedded-engineer`)

**Expertise:** Firmware, real-time systems, microcontroller programming
**Model Profile:** Balanced (Sonnet)
**Use Cases:**
- Firmware development
- Real-time operating systems
- Microcontroller programming
- Hardware-software integration

**Location:** `.claude/agents/custom/hardware/embedded-engineer.md`

---

## 🖥️ Desktop Application Agents

### **6. Desktop Specialist** (`desktop-specialist`)

**Expertise:** Cross-platform applications (wxWidgets, Qt, Electron)
**Model Profile:** Balanced (Sonnet)
**Use Cases:**
- Desktop application development
- Cross-platform UIs
- Native system integration
- Application packaging

**Location:** `.claude/agents/custom/desktop/desktop-specialist.md`

---

### **7. CAD Engineer** (`cad-engineer`)

**Expertise:** Precision engineering tools, parametric modeling, technical drawing
**Model Profile:** Balanced (Sonnet)
**Use Cases:**
- CAD software development
- Parametric modeling tools
- Technical drawing automation
- Engineering analysis tools

**Location:** `.claude/agents/custom/desktop/cad-engineer.md`

---

### **8. 3D Addon Developer** (`3d-addon-developer`)

**Expertise:** Blender extensions, Maya plugins, 3D workflow automation
**Model Profile:** Balanced (Sonnet)
**Use Cases:**
- Blender addon development
- Maya plugin creation
- 3D workflow automation
- Tool integration

**Location:** `.claude/agents/custom/desktop/3d-addon-developer.md`

---

## 🔬 Scientific Computing Agent

### **9. Scientific Computing Specialist** (`scientific-computing-specialist`)

**Expertise:** Research software, data analysis tools, high-performance computing
**Model Profile:** Balanced (Sonnet)
**Use Cases:**
- Scientific research software
- Data analysis applications
- HPC solutions
- Academic software

**Location:** `.claude/agents/custom/scientific/scientific-computing-specialist.md`

---

## 📊 Agent Selection by Technology

### **Graphics & Visualization**
- **3D Rendering** → graphics-3d-engineer, math-specialist
- **2D Graphics** → graphics-2d-engineer
- **Scientific Visualization** → scientific-computing-specialist, math-specialist

### **Hardware Development**
- **IoT Devices** → electronics-engineer, embedded-engineer
- **Firmware** → embedded-engineer
- **PCB Design** → electronics-engineer

### **Desktop Applications**
- **Cross-Platform Apps** → desktop-specialist
- **CAD Software** → cad-engineer, math-specialist
- **3D Tool Extensions** → 3d-addon-developer, graphics-3d-engineer

### **Scientific Computing**
- **Research Software** → scientific-computing-specialist
- **Numerical Analysis** → math-specialist, scientific-computing-specialist
- **HPC Applications** → scientific-computing-specialist, math-specialist

---

## 🔗 Related Documentation

- **[Core Agents](core-agents.md)** - Core development agents
- **[Enterprise Agents](enterprise-agents.md)** - Enterprise operation agents
- **[Agents Overview](agents-overview.md)** - Complete agent system
- **[AI Agent Selection](ai-agent-selection.md)** - AI-powered recommendations

---

**Last Updated:** 2025-10-05 | **Version:** 3.3.0
