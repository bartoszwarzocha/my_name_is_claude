# Example Code Command

**Command**: `/example-code [pattern]`
**Category**: Development Helpers
**Description**: Przykłady kodu dla wzorców

## Usage

```
/example-code "mvc pattern"
/example-code "database connection"
/example-code "export functionality"
/example-code "error handling"
```

## Functionality

Provides curated code examples, patterns, and templates relevant to current project technology stack and requirements.

### Output Format
```
💻 CODE EXAMPLES: "mvc pattern"

Pattern Category: Architecture
Technology Context: Python + wxPython + SQLite
Complexity: Intermediate
Agent Specialist: software-architect

┌─ PATTERN OVERVIEW ──────────────────────────────────────┐
│                                                         │
│ 🏗️ Model-View-Controller (MVC) Pattern                 │
│                                                         │
│ Purpose: Separate business logic, UI, and data         │
│ Benefits: Maintainability, testability, modularity     │
│ Use Case: Desktop applications with complex UI         │
│                                                         │
│ Components:                                             │
│ • Model: Data and business logic                       │
│ • View: User interface (wxPython)                      │
│ • Controller: Coordination between Model and View      │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ COMPLETE IMPLEMENTATION ───────────────────────────────┐
│                                                         │
│ 📁 File Structure:                                      │
│ ```                                                     │
│ src/                                                    │
│ ├── models/                                             │
│ │   ├── __init__.py                                     │
│ │   ├── document.py          # Document model          │
│ │   └── database.py          # Database abstraction    │
│ ├── views/                                              │
│ │   ├── __init__.py                                     │
│ │   ├── main_window.py       # Main application window │
│ │   └── dialogs.py           # Dialog windows          │
│ ├── controllers/                                        │
│ │   ├── __init__.py                                     │
│ │   ├── document_controller.py # Document operations   │
│ │   └── export_controller.py   # Export functionality  │
│ └── main.py                   # Application entry point│
│ ```                                                     │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ MODEL IMPLEMENTATION ──────────────────────────────────┐
│                                                         │
│ 📄 models/document.py                                   │
│ ```python                                              │
│ from dataclasses import dataclass                      │
│ from typing import Optional, List                      │
│ from datetime import datetime                          │
│                                                         │
│ @dataclass                                             │
│ class Document:                                         │
│     \"\"\"Document model with business logic.\"\"\"           │
│     id: Optional[int] = None                           │
│     title: str = ""                                    │
│     content: str = ""                                  │
│     created_at: Optional[datetime] = None              │
│     modified_at: Optional[datetime] = None             │
│                                                         │
│     def update_content(self, new_content: str) -> None: │
│         \"\"\"Update document content with timestamp.\"\"\"    │
│         self.content = new_content                     │
│         self.modified_at = datetime.now()              │
│                                                         │
│     def get_word_count(self) -> int:                   │
│         \"\"\"Calculate word count for document.\"\"\"         │
│         return len(self.content.split())               │
│                                                         │
│     def validate(self) -> List[str]:                   │
│         \"\"\"Validate document data.\"\"\"                   │
│         errors = []                                    │
│         if not self.title.strip():                     │
│             errors.append("Title is required")         │
│         if len(self.title) > 200:                      │
│             errors.append("Title too long")            │
│         return errors                                  │
│ ```                                                     │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ VIEW IMPLEMENTATION ───────────────────────────────────┐
│                                                         │
│ 🖥️ views/main_window.py                                │
│ ```python                                              │
│ import wx                                              │
│ from wx.richtext import RichTextCtrl                   │
│ from typing import Callable, Optional                  │
│                                                         │
│ class MainWindow(wx.Frame):                            │
│     \"\"\"Main application view using wxPython.\"\"\"         │
│                                                         │
│     def __init__(self):                                │
│         super().__init__(None, title="Book Writer")    │
│         self.controller = None                         │
│         self.setup_ui()                                │
│         self.setup_events()                            │
│                                                         │
│     def setup_ui(self):                                │
│         \"\"\"Create user interface components.\"\"\"          │
│         panel = wx.Panel(self)                         │
│                                                         │
│         # Title input                                  │
│         self.title_ctrl = wx.TextCtrl(panel)           │
│                                                         │
│         # Content editor                               │
│         self.content_ctrl = RichTextCtrl(              │
│             panel, style=wx.WANTS_CHARS                │
│         )                                              │
│                                                         │
│         # Status bar                                   │
│         self.status_bar = self.CreateStatusBar()       │
│                                                         │
│         # Layout                                       │
│         sizer = wx.BoxSizer(wx.VERTICAL)               │
│         sizer.Add(wx.StaticText(panel, label="Title:"))│
│         sizer.Add(self.title_ctrl, 0, wx.EXPAND)       │
│         sizer.Add(self.content_ctrl, 1, wx.EXPAND)     │
│         panel.SetSizer(sizer)                          │
│                                                         │
│     def setup_events(self):                            │
│         \"\"\"Bind UI events to handlers.\"\"\"               │
│         self.title_ctrl.Bind(wx.EVT_TEXT, self.on_title_change)│
│         self.content_ctrl.Bind(wx.EVT_TEXT, self.on_content_change)│
│                                                         │
│     def set_controller(self, controller):               │
│         \"\"\"Set the controller for MVC coordination.\"\"\"    │
│         self.controller = controller                   │
│                                                         │
│     def update_display(self, document):                │
│         \"\"\"Update view with document data.\"\"\"            │
│         self.title_ctrl.SetValue(document.title)       │
│         self.content_ctrl.SetValue(document.content)   │
│         self.update_status_bar(document)               │
│                                                         │
│     def update_status_bar(self, document):             │
│         \"\"\"Update status bar with document statistics.\"\"\" │
│         word_count = document.get_word_count()         │
│         self.status_bar.SetStatusText(                 │
│             f"Words: {word_count}"                     │
│         )                                              │
│                                                         │
│     def on_title_change(self, event):                  │
│         \"\"\"Handle title change events.\"\"\"               │
│         if self.controller:                            │
│             self.controller.update_title(              │
│                 self.title_ctrl.GetValue()             │
│             )                                          │
│                                                         │
│     def on_content_change(self, event):                │
│         \"\"\"Handle content change events.\"\"\"             │
│         if self.controller:                            │
│             self.controller.update_content(            │
│                 self.content_ctrl.GetValue()           │
│             )                                          │
│ ```                                                     │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ CONTROLLER IMPLEMENTATION ─────────────────────────────┐
│                                                         │
│ 🎮 controllers/document_controller.py                   │
│ ```python                                              │
│ from models.document import Document                   │
│ from models.database import DocumentRepository         │
│ from typing import Optional                            │
│                                                         │
│ class DocumentController:                              │
│     \"\"\"Controller coordinating Document model and View.\"\"\"│
│                                                         │
│     def __init__(self, view, repository: DocumentRepository):│
│         self.view = view                               │
│         self.repository = repository                   │
│         self.current_document: Optional[Document] = None│
│         self.view.set_controller(self)                 │
│                                                         │
│     def new_document(self):                            │
│         \"\"\"Create a new document.\"\"\"                    │
│         self.current_document = Document()             │
│         self.view.update_display(self.current_document)│
│                                                         │
│     def load_document(self, document_id: int):         │
│         \"\"\"Load document from repository.\"\"\"            │
│         document = self.repository.get_by_id(document_id)│
│         if document:                                   │
│             self.current_document = document           │
│             self.view.update_display(document)         │
│         else:                                          │
│             self.show_error("Document not found")      │
│                                                         │
│     def save_document(self):                           │
│         \"\"\"Save current document to repository.\"\"\"       │
│         if not self.current_document:                  │
│             return                                     │
│                                                         │
│         errors = self.current_document.validate()      │
│         if errors:                                     │
│             self.show_error("\\n".join(errors))          │
│             return                                     │
│                                                         │
│         try:                                           │
│             self.repository.save(self.current_document)│
│             self.show_success("Document saved")        │
│         except Exception as e:                         │
│             self.show_error(f"Save failed: {e}")       │
│                                                         │
│     def update_title(self, new_title: str):            │
│         \"\"\"Handle title updates from view.\"\"\"           │
│         if self.current_document:                      │
│             self.current_document.title = new_title    │
│             self.view.update_status_bar(               │
│                 self.current_document                  │
│             )                                          │
│                                                         │
│     def update_content(self, new_content: str):        │
│         \"\"\"Handle content updates from view.\"\"\"         │
│         if self.current_document:                      │
│             self.current_document.update_content(new_content)│
│             self.view.update_status_bar(               │
│                 self.current_document                  │
│             )                                          │
│                                                         │
│     def show_error(self, message: str):                │
│         \"\"\"Show error message to user.\"\"\"               │
│         wx.MessageBox(message, "Error", wx.OK | wx.ICON_ERROR)│
│                                                         │
│     def show_success(self, message: str):              │
│         \"\"\"Show success message to user.\"\"\"             │
│         wx.MessageBox(message, "Success", wx.OK | wx.ICON_INFORMATION)│
│ ```                                                     │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─ APPLICATION ENTRY POINT ───────────────────────────────┐
│                                                         │
│ 🚀 main.py                                             │
│ ```python                                              │
│ import wx                                              │
│ from views.main_window import MainWindow               │
│ from controllers.document_controller import DocumentController│
│ from models.database import DocumentRepository         │
│                                                         │
│ class BookWriterApp(wx.App):                           │
│     \"\"\"Main application class.\"\"\"                       │
│                                                         │
│     def OnInit(self):                                  │
│         \"\"\"Initialize application components.\"\"\"          │
│         # Create view                                  │
│         main_window = MainWindow()                     │
│                                                         │
│         # Create repository                            │
│         repository = DocumentRepository("documents.db")│
│                                                         │
│         # Create controller                            │
│         controller = DocumentController(               │
│             main_window, repository                    │
│         )                                              │
│                                                         │
│         # Setup initial state                          │
│         controller.new_document()                      │
│                                                         │
│         # Show main window                             │
│         main_window.Show()                             │
│         return True                                    │
│                                                         │
│ if __name__ == "__main__":                             │
│     app = BookWriterApp()                              │
│     app.MainLoop()                                     │
│ ```                                                     │
│                                                         │
└─────────────────────────────────────────────────────────┘

🎯 USAGE GUIDELINES:

Best Practices:
• Keep models pure - no UI dependencies
• Views should only handle UI logic
• Controllers coordinate but don't implement business logic
• Use dependency injection for testability

Testing Strategy:
• Unit test models independently
• Mock dependencies in controller tests
• Use pytest-qt for view testing
• Integration tests for full workflow

Performance Tips:
• Use wx.CallAfter for thread-safe UI updates
• Implement lazy loading for large documents
• Cache frequently accessed data
• Debounce rapid UI events

📚 RELATED PATTERNS:

Architecture Patterns:
• /example-code "mvvm pattern" - Model-View-ViewModel variant
• /example-code "observer pattern" - Event-driven updates
• /example-code "command pattern" - Undo/redo functionality

Integration Patterns:
• /example-code "repository pattern" - Data access abstraction
• /example-code "dependency injection" - Loose coupling
• /example-code "event bus" - Decoupled communication

✨ PATTERN IMPLEMENTATION READY!

Total Code Lines: 200+
Complexity: Intermediate
Testing: Unit test ready
Agent Support: software-architect + desktop-specialist
```

## Integration

- Pattern library database
- Technology-specific examples
- Project context awareness
- Agent collaboration support