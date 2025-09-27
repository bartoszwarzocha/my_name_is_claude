# Quick Docs Command

**Command**: `/quick-docs [topic]`
**Category**: Development Helpers
**Description**: Szybki dostęp do dokumentacji

## Usage

```
/quick-docs wxpython
/quick-docs "sqlite optimization"
/quick-docs framework
/quick-docs agents
```

## Functionality

Provides instant access to relevant documentation, code examples, and best practices for any technology or framework topic.

### Documentation Sources
- **Framework Documentation**: Claude Code Multi-Agent Framework docs
- **Agent Guides**: Agent-specific usage documentation
- **Technology References**: External technology documentation
- **Code Examples**: Pattern library and example repository
- **Best Practices**: Curated best practice collections

### Output Format
```
📚 QUICK DOCUMENTATION: "wxpython"

Topic Category: GUI Framework
Relevance: High (Used in current project)
Documentation Sources: 3

┌─ FRAMEWORK INTEGRATION ─────────────────────────────────┐
│                                                         │
│ 🔧 Claude Code Framework Support                       │
│                                                         │
│ Agent Specialist: desktop-specialist                   │
│ Location: .claude/agents/custom/desktop/               │
│ Integration Level: Full Support                        │
│                                                         │
│ Framework Features:                                     │
│ • Automatic wxPython project detection                 │
│ • GUI testing framework integration                    │
│ • Cross-platform development support                   │
│ • Performance optimization guidelines                  │
│                                                         │
│ Quick Start:                                            │
│ 1. Ensure CLAUDE.md includes "wxpython" in tech stack  │
│ 2. Run /agent-select to activate desktop-specialist    │
│ 3. Use "/start-feature 'GUI Feature'" for new features │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ CORE CONCEPTS ─────────────────────────────────────────┐
│                                                         │
│ 🎯 wxPython Fundamentals                               │
│                                                         │
│ Key Components:                                         │
│ • wx.Frame: Main application windows                   │
│ • wx.Panel: Container for controls                     │
│ • wx.Sizer: Layout management                          │
│ • wx.Event: Event handling system                      │
│                                                         │
│ Essential Patterns:                                     │
│ • MVC Architecture: Separate GUI from business logic   │
│ • Event-Driven Programming: Use Bind() for events      │
│ • Layout Management: Use sizers, not absolute position │
│ • Resource Management: Proper Destroy() calls          │
│                                                         │
│ Performance Tips:                                       │
│ • Use Freeze/Thaw for bulk updates                     │
│ • Implement virtual controls for large datasets        │
│ • Minimize Layout() calls                              │
│ • Use CallAfter() for thread safety                    │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ CODE EXAMPLES ─────────────────────────────────────────┐
│                                                         │
│ 🔨 Common wxPython Patterns                            │
│                                                         │
│ Basic Window Setup:                                     │
│ ```python                                              │
│ import wx                                              │
│                                                         │
│ class MainFrame(wx.Frame):                             │
│     def __init__(self):                                │
│         super().__init__(None, title="App")            │
│         self.init_ui()                                 │
│                                                         │
│     def init_ui(self):                                 │
│         panel = wx.Panel(self)                         │
│         sizer = wx.BoxSizer(wx.VERTICAL)               │
│         # Add controls here                            │
│         panel.SetSizer(sizer)                          │
│ ```                                                     │
│                                                         │
│ Event Handling:                                         │
│ ```python                                              │
│ def setup_events(self):                                │
│     self.Bind(wx.EVT_MENU, self.on_exit, id=wx.ID_EXIT)│
│     self.Bind(wx.EVT_CLOSE, self.on_close)             │
│                                                         │
│ def on_exit(self, event):                              │
│     self.Close()                                       │
│ ```                                                     │
│                                                         │
│ Rich Text Editor:                                       │
│ ```python                                              │
│ from wx.richtext import RichTextCtrl                   │
│                                                         │
│ editor = RichTextCtrl(panel, style=wx.WANTS_CHARS)     │
│ editor.SetValue("Sample text")                         │
│ ```                                                     │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ PROJECT-SPECIFIC GUIDANCE ─────────────────────────────┐
│                                                         │
│ 📝 For Your Book Writing App                           │
│                                                         │
│ Recommended Components:                                 │
│ • wx.richtext.RichTextCtrl: Main text editor           │
│ • wx.TreeCtrl: Chapter/section navigation              │
│ • wx.StatusBar: Document statistics and status         │
│ • wx.ToolBar: Formatting and action buttons            │
│ • wx.SplitterWindow: Multi-panel layout                │
│                                                         │
│ Integration Points:                                     │
│ • SQLite via wx.CallAfter for thread-safe updates     │
│ • Export progress with wx.ProgressDialog               │
│ • Preferences with wx.PropertyGrid                     │
│ • File operations with wx.FileDialog                   │
│                                                         │
│ Agent Consultation:                                     │
│ • "desktop-specialist implement wxPython main window"  │
│ • "desktop-specialist add rich text editing features"  │
│ • "desktop-specialist optimize GUI performance"        │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ EXTERNAL RESOURCES ────────────────────────────────────┐
│                                                         │
│ 🌐 Official Documentation                              │
│                                                         │
│ • wxPython Official Docs: https://docs.wxpython.org/   │
│ • wxPython Tutorials: https://wxpython.org/pages/docs/ │
│ • API Reference: Complete class and method reference   │
│                                                         │
│ 📖 Learning Resources                                   │
│                                                         │
│ • "wxPython in Action" - Comprehensive guide           │
│ • wxPython Demo - Interactive examples                 │
│ • Real Python wxPython Tutorial                        │
│                                                         │
│ 🛠️ Development Tools                                    │
│                                                         │
│ • wxGlade: Visual GUI designer                         │
│ • wxFormBuilder: Alternative GUI designer              │
│ • PyQt Designer: Cross-reference for concepts          │
│                                                         │
└─────────────────────────────────────────────────────────┘

🔗 RELATED TOPICS:

Similar Technologies:
• /quick-docs tkinter - Alternative Python GUI framework
• /quick-docs pyqt - More complex GUI framework
• /quick-docs kivy - Modern UI framework

Integration Topics:
• /quick-docs "wxpython sqlite" - Database integration
• /quick-docs "wxpython testing" - GUI testing strategies
• /quick-docs "wxpython packaging" - Application distribution

Framework Topics:
• /quick-docs agents - Agent system documentation
• /quick-docs "desktop development" - Desktop app patterns
• /quick-docs "gui optimization" - Performance best practices

⚡ QUICK ACTIONS:

Get Agent Help:
• /find-agent "wxpython" - Find wxPython specialists
• /agent-select "desktop gui" - Activate GUI development agents

Start Development:
• /start-feature "Main Window" - Begin GUI feature development
• /code-review - Review existing wxPython code
• /testing-strategy --gui - Setup GUI testing

✨ DOCUMENTATION READY!

Total Sections: 6
External Links: 8
Code Examples: 3
Agent Integration: Full support available
```

## Integration

- Framework documentation database
- Agent expertise linking
- Project-specific guidance
- External resource aggregation