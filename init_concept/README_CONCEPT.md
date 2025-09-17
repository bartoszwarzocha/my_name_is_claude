# Init Concept - Project Initialization System

## 🎯 Purpose

The `init_concept` folder is a staging area for project conceptualization and automatic CLAUDE.md generation. This system allows you to describe your project idea in any format and have the framework automatically generate a properly formatted CLAUDE.md configuration file.

## 🔄 How It Works

### Step 1: Add Your Project Concept

Place any files describing your project concept in this folder:

- **Project descriptions** (any format: .md, .txt, .docx)
- **Business requirements** or user stories
- **Technical specifications** or architecture notes
- **Wireframes or mockups** (images, PDFs)
- **Existing code samples** or legacy system documentation
- **Meeting notes** or brainstorming sessions
- **Market research** or competitive analysis

### Step 2: Generate CLAUDE.md Configuration

Use the initialization prompt to automatically generate your project configuration:

```bash
# Navigate to your project
cd /path/to/your/project

# Launch Claude Code
claude-code

# Use the concept-to-CLAUDE.md generator prompt
# Located at: .claude/prompts/project/claude_md_from_concept.md
```

The prompt will:
1. **Analyze all files** in the `init_concept` folder
2. **Extract key information** about technology stack, business domain, scale
3. **Generate complete CLAUDE.md** following the framework template
4. **Backup original** CLAUDE.md as `CLAUDE_template.md`
5. **Ask for user decisions** on configuration options (TODO management, agent selection, etc.)

### Step 3: Generate Project Instructions

After CLAUDE.md is created, use the instruction generator:

```bash
# Use the project instruction generator prompt
# Located at: .claude/prompts/init/prepare_instruction.md
```

This will create a **custom project roadmap** with:
- Recommended agent sequence
- TODO configuration guidance
- Phase-by-phase workflow
- Specific prompt recommendations

## 📁 Example Concept Structure

```text
init_concept/
├── README_CONCEPT.md           # This file
├── project_idea.md             # Main project description
├── business_requirements.txt   # Business needs and goals
├── tech_stack_notes.md         # Technology preferences
├── wireframes/                 # UI mockups or designs
├── legacy_docs/               # Existing system documentation
└── meeting_notes/             # Brainstorming sessions
```

## 🎯 What Gets Generated

### Automatic CLAUDE.md Generation

The `claude_md_from_concept.md` prompt automatically populates:

- **Project Metadata** - Name, description, domain, scale
- **Technology Stack** - Detected from concept files
- **Agent Selection** - Recommended based on project complexity
- **TODO Configuration** - Suggested settings based on project scale
- **Integration Requirements** - Database, APIs, deployment needs

### Custom Project Instructions

The `prepare_instruction.md` prompt creates:

- **Step-by-step workflow** tailored to your project
- **Agent sequence** recommendations
- **Prompt selection** for each development phase
- **TODO management setup** specific to your needs
- **Timeline estimates** and milestones

## 🚀 Quick Start Example

1. **Add your concept:**
   ```bash
   echo "Mobile-first invoice management app for small businesses" > init_concept/project_idea.md
   echo "React Native + Node.js + PostgreSQL" > init_concept/tech_stack.md
   echo "MVP in 6 weeks, 50-100 users initially" > init_concept/requirements.md
   ```

2. **Generate CLAUDE.md:**
   - Use `.claude/prompts/init/claude_md_from_concept.md`
   - Answer configuration questions
   - Review and approve generated CLAUDE.md

3. **Get project instructions:**
   - Use `.claude/prompts/init/prepare_instruction.md`
   - Receive customized development roadmap
   - Follow recommended agent workflow

## ✨ Benefits

- **Zero Manual Configuration** - No need to understand CLAUDE.md format
- **Smart Detection** - Automatically identifies technology needs
- **Custom Workflows** - Tailored instructions for your specific project
- **Best Practices** - Framework experience built into recommendations
- **Fast Setup** - From concept to development-ready in minutes

## 🔧 Advanced Usage

### Multi-Project Concepts
- Create subfolders for different project variations
- Compare generated configurations
- Choose optimal approach

### Iterative Refinement
- Update concept files as requirements evolve
- Re-generate CLAUDE.md with new information
- Maintain concept history for reference

### Integration with Existing Projects
- Add existing code samples to init_concept
- Generate CLAUDE.md for legacy project modernization
- Use for project analysis and improvement recommendations

---

**Ready to start?** Add your project concept files to this folder and use the initialization prompts to automatically generate your development-ready configuration.