# wxWidgets Desktop Application Development

## Context and Purpose
You are developing cross-platform desktop applications using wxWidgets with Python (wxPython) or C++. This prompt focuses on creating modern, native-looking GUI applications with advanced UI patterns, data management, threading, and platform-specific integrations for Windows, macOS, and Linux.

## Expertise Areas
- wxPython and wxWidgets C++ for cross-platform desktop development
- Advanced UI patterns and custom controls
- Data binding and MVC/MVP architecture patterns
- Threading and asynchronous operations in GUI applications
- Platform-specific integrations and native features
- Performance optimization and memory management
- Application packaging and distribution strategies

## Implementation Framework

### Phase 1: Advanced wxPython Application Architecture

**Comprehensive Desktop Application Framework:**
```python
import wx
import wx.lib.agw.aui as aui
import wx.lib.newevent
import wx.grid
import wx.html2
import asyncio
import threading
import logging
from typing import Dict, List, Optional, Callable, Any, TypeVar, Generic
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import sqlite3
from contextlib import contextmanager

# Advanced application architecture framework
class DesktopApplicationFramework:
    """
    Comprehensive framework for wxPython desktop applications with:
    - MVC/MVP architecture patterns
    - Advanced UI components and layouts
    - Threading and async operations
    - Data persistence and caching
    - Cross-platform compatibility
    """
    
    def __init__(self):
        self.controllers: Dict[str, 'BaseController'] = {}
        self.services: Dict[str, 'BaseService'] = {}
        self.event_manager = EventManager()
        self.config_manager = ConfigurationManager()
        self.thread_pool = ThreadPoolExecutor(max_workers=4)
        
    def register_controller(self, name: str, controller: 'BaseController'):
        """Register a controller in the application framework"""
        self.controllers[name] = controller
        controller.set_framework(self)
    
    def register_service(self, name: str, service: 'BaseService'):
        """Register a service in the application framework"""
        self.services[name] = service
        service.set_framework(self)
    
    def get_controller(self, name: str) -> Optional['BaseController']:
        """Get a registered controller"""
        return self.controllers.get(name)
    
    def get_service(self, name: str) -> Optional['BaseService']:
        """Get a registered service"""
        return self.services.get(name)

# Advanced main application class with modern patterns
class ModernDesktopApp(wx.App):
    """
    Modern wxPython application with advanced architecture:
    - Dependency injection container
    - Event-driven communication
    - Configuration management
    - Logging and error handling
    """
    
    def __init__(self, app_name: str = "ModernApp", **kwargs):
        self.app_name = app_name
        self.framework = DesktopApplicationFramework()
        super().__init__(**kwargs)
    
    def OnInit(self) -> bool:
        """Initialize the application with advanced setup"""
        try:
            # Setup logging
            self.setup_logging()
            
            # Load configuration
            self.framework.config_manager.load_config()
            
            # Initialize services
            self.initialize_services()
            
            # Create main window
            self.main_window = AdvancedMainWindow(
                title=self.app_name,
                framework=self.framework
            )
            
            # Setup global event handlers
            self.setup_global_events()
            
            # Show main window
            self.main_window.Show()
            self.SetTopWindow(self.main_window)
            
            return True
            
        except Exception as e:
            wx.MessageBox(
                f"Failed to initialize application: {str(e)}",
                "Startup Error",
                wx.OK | wx.ICON_ERROR
            )
            return False
    
    def setup_logging(self):
        """Configure application logging"""
        log_dir = Path.home() / f".{self.app_name.lower()}" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_dir / "app.log"),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger(self.app_name)
    
    def initialize_services(self):
        """Initialize all application services"""
        # Data service for persistence
        data_service = DataService()
        self.framework.register_service('data', data_service)
        
        # Settings service for user preferences
        settings_service = SettingsService()
        self.framework.register_service('settings', settings_service)
        
        # Network service for API communication
        network_service = NetworkService()
        self.framework.register_service('network', network_service)
    
    def setup_global_events(self):
        """Setup application-wide event handlers"""
        self.Bind(wx.EVT_CLOSE, self.on_exit)
        
        # Handle system events
        if wx.Platform == '__WXMSW__':
            self.setup_windows_events()
        elif wx.Platform == '__WXMAC__':
            self.setup_mac_events()
        elif wx.Platform == '__WXGTK__':
            self.setup_linux_events()
    
    def on_exit(self, event):
        """Handle application exit with cleanup"""
        try:
            # Save current state
            self.framework.config_manager.save_config()
            
            # Cleanup services
            for service in self.framework.services.values():
                service.cleanup()
            
            # Shutdown thread pool
            self.framework.thread_pool.shutdown(wait=True)
            
            self.logger.info("Application shutdown completed")
            
        except Exception as e:
            self.logger.error(f"Error during shutdown: {e}")
        
        finally:
            event.Skip()

# Advanced main window with AUI (Advanced User Interface)
class AdvancedMainWindow(wx.Frame):
    """
    Modern main window with advanced UI features:
    - AUI docking system
    - Menu and toolbar management
    - Status bar with multiple sections
    - Keyboard shortcuts and accelerators
    """
    
    def __init__(self, title: str, framework: DesktopApplicationFramework):
        super().__init__(None, title=title, size=(1200, 800))
        
        self.framework = framework
        self.aui_manager = aui.AuiManager(self)
        
        # Initialize UI components
        self.create_menu_bar()
        self.create_toolbar()
        self.create_status_bar()
        self.create_panels()
        self.setup_layout()
        self.setup_accelerators()
        
        # Bind events
        self.setup_events()
        
        # Center window
        self.Center()
    
    def create_menu_bar(self):
        """Create comprehensive menu system"""
        menubar = wx.MenuBar()
        
        # File menu
        file_menu = wx.Menu()
        
        new_item = file_menu.Append(wx.ID_NEW, "&New\tCtrl+N", "Create new document")
        open_item = file_menu.Append(wx.ID_OPEN, "&Open\tCtrl+O", "Open existing document")
        file_menu.AppendSeparator()
        
        save_item = file_menu.Append(wx.ID_SAVE, "&Save\tCtrl+S", "Save current document")
        save_as_item = file_menu.Append(wx.ID_SAVEAS, "Save &As\tCtrl+Shift+S", "Save with new name")
        file_menu.AppendSeparator()
        
        # Recent files submenu
        recent_menu = wx.Menu()
        self.recent_files = []  # Will be populated from settings
        file_menu.AppendSubMenu(recent_menu, "&Recent Files")
        
        file_menu.AppendSeparator()
        exit_item = file_menu.Append(wx.ID_EXIT, "E&xit\tCtrl+Q", "Exit application")
        
        menubar.Append(file_menu, "&File")
        
        # Edit menu
        edit_menu = wx.Menu()
        
        undo_item = edit_menu.Append(wx.ID_UNDO, "&Undo\tCtrl+Z", "Undo last action")
        redo_item = edit_menu.Append(wx.ID_REDO, "&Redo\tCtrl+Y", "Redo last undone action")
        edit_menu.AppendSeparator()
        
        cut_item = edit_menu.Append(wx.ID_CUT, "Cu&t\tCtrl+X", "Cut selection")
        copy_item = edit_menu.Append(wx.ID_COPY, "&Copy\tCtrl+C", "Copy selection")
        paste_item = edit_menu.Append(wx.ID_PASTE, "&Paste\tCtrl+V", "Paste from clipboard")
        edit_menu.AppendSeparator()
        
        find_item = edit_menu.Append(wx.ID_FIND, "&Find\tCtrl+F", "Find text")
        replace_item = edit_menu.Append(wx.ID_REPLACE, "&Replace\tCtrl+H", "Replace text")
        
        menubar.Append(edit_menu, "&Edit")
        
        # View menu
        view_menu = wx.Menu()
        
        # Toggle panels
        self.view_sidebar = view_menu.AppendCheckItem(1001, "&Sidebar\tF9", "Toggle sidebar visibility")
        self.view_toolbar = view_menu.AppendCheckItem(1002, "&Toolbar", "Toggle toolbar visibility")
        self.view_statusbar = view_menu.AppendCheckItem(1003, "Status &Bar", "Toggle status bar visibility")
        
        view_menu.AppendSeparator()
        
        # Zoom controls
        zoom_in = view_menu.Append(1004, "Zoom &In\tCtrl++", "Zoom in")
        zoom_out = view_menu.Append(1005, "Zoom &Out\tCtrl+-", "Zoom out")
        zoom_reset = view_menu.Append(1006, "&Reset Zoom\tCtrl+0", "Reset zoom to 100%")
        
        view_menu.AppendSeparator()
        fullscreen = view_menu.Append(1007, "&Full Screen\tF11", "Toggle full screen mode")
        
        menubar.Append(view_menu, "&View")
        
        # Tools menu
        tools_menu = wx.Menu()
        
        preferences = tools_menu.Append(wx.ID_PREFERENCES, "&Preferences\tCtrl+,", "Open preferences")
        tools_menu.AppendSeparator()
        
        # Custom tools
        tools_menu.Append(2001, "&Data Import", "Import data from file")
        tools_menu.Append(2002, "&Data Export", "Export data to file")
        tools_menu.AppendSeparator()
        tools_menu.Append(2003, "&Database Tools", "Database management tools")
        
        menubar.Append(tools_menu, "&Tools")
        
        # Help menu
        help_menu = wx.Menu()
        
        help_item = help_menu.Append(wx.ID_HELP, "&Help\tF1", "Show help documentation")
        help_menu.AppendSeparator()
        
        about_item = help_menu.Append(wx.ID_ABOUT, "&About", "About this application")
        
        menubar.Append(help_menu, "&Help")
        
        self.SetMenuBar(menubar)
    
    def create_toolbar(self):
        """Create modern toolbar with advanced controls"""
        toolbar = self.CreateToolBar(wx.TB_HORIZONTAL | wx.TB_FLAT | wx.TB_TEXT)
        toolbar.SetToolBitmapSize((24, 24))
        
        # Load icons (you would have actual icon files)
        new_bmp = wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, (24, 24))
        open_bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, (24, 24))
        save_bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, (24, 24))
        
        # File operations
        toolbar.AddTool(wx.ID_NEW, "New", new_bmp, "Create new document")
        toolbar.AddTool(wx.ID_OPEN, "Open", open_bmp, "Open existing document")
        toolbar.AddTool(wx.ID_SAVE, "Save", save_bmp, "Save current document")
        toolbar.AddSeparator()
        
        # Edit operations
        undo_bmp = wx.ArtProvider.GetBitmap(wx.ART_UNDO, wx.ART_TOOLBAR, (24, 24))
        redo_bmp = wx.ArtProvider.GetBitmap(wx.ART_REDO, wx.ART_TOOLBAR, (24, 24))
        
        toolbar.AddTool(wx.ID_UNDO, "Undo", undo_bmp, "Undo last action")
        toolbar.AddTool(wx.ID_REDO, "Redo", redo_bmp, "Redo last undone action")
        toolbar.AddSeparator()
        
        # Custom controls in toolbar
        search_ctrl = wx.SearchCtrl(toolbar, size=(200, -1))
        search_ctrl.ShowSearchButton(True)
        search_ctrl.ShowCancelButton(True)
        toolbar.AddControl(search_ctrl, "Search")
        
        toolbar.AddSeparator()
        
        # View toggle buttons
        toolbar.AddCheckTool(1001, "Sidebar", wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_TOOLBAR), shortHelp="Toggle sidebar")
        
        toolbar.Realize()
        self.toolbar = toolbar
    
    def create_status_bar(self):
        """Create advanced status bar with multiple sections"""
        statusbar = self.CreateStatusBar(4)
        
        # Set status bar field widths
        statusbar.SetStatusWidths([-2, -1, 100, 100])
        
        # Set initial text
        statusbar.SetStatusText("Ready", 0)
        statusbar.SetStatusText("", 1)
        statusbar.SetStatusText("Ln 1, Col 1", 2)
        statusbar.SetStatusText("100%", 3)
        
        self.statusbar = statusbar
    
    def create_panels(self):
        """Create application panels with advanced features"""
        
        # Main content panel with notebook
        self.content_notebook = aui.AuiNotebook(
            self, 
            agwStyle=aui.AUI_NB_DEFAULT_STYLE | aui.AUI_NB_CLOSE_ON_ACTIVE_TAB
        )
        
        # Create initial tab
        self.main_panel = MainContentPanel(self.content_notebook, self.framework)
        self.content_notebook.AddPage(self.main_panel, "Main", True)
        
        # Sidebar panel
        self.sidebar_panel = SidebarPanel(self, self.framework)
        
        # Properties panel
        self.properties_panel = PropertiesPanel(self, self.framework)
        
        # Output/Log panel
        self.output_panel = OutputPanel(self, self.framework)
    
    def setup_layout(self):
        """Setup AUI layout with dockable panels"""
        
        # Add panels to AUI manager
        self.aui_manager.AddPane(
            self.content_notebook,
            aui.AuiPaneInfo()
            .Name("content")
            .Caption("Content")
            .Center()
            .CloseButton(False)
            .MaximizeButton(True)
        )
        
        self.aui_manager.AddPane(
            self.sidebar_panel,
            aui.AuiPaneInfo()
            .Name("sidebar")
            .Caption("Explorer")
            .Left()
            .BestSize((250, -1))
            .MinSize((200, -1))
            .Layer(1)
            .CloseButton(True)
            .MaximizeButton(False)
        )
        
        self.aui_manager.AddPane(
            self.properties_panel,
            aui.AuiPaneInfo()
            .Name("properties")
            .Caption("Properties")
            .Right()
            .BestSize((300, -1))
            .MinSize((250, -1))
            .Layer(1)
            .CloseButton(True)
            .MaximizeButton(False)
        )
        
        self.aui_manager.AddPane(
            self.output_panel,
            aui.AuiPaneInfo()
            .Name("output")
            .Caption("Output")
            .Bottom()
            .BestSize((-1, 200))
            .MinSize((-1, 150))
            .Layer(1)
            .CloseButton(True)
            .MaximizeButton(False)
        )
        
        # Load saved perspective if available
        self.load_perspective()
        
        # Update the layout
        self.aui_manager.Update()
    
    def setup_accelerators(self):
        """Setup keyboard accelerators"""
        accel_entries = [
            wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('N'), wx.ID_NEW),
            wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('O'), wx.ID_OPEN),
            wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('S'), wx.ID_SAVE),
            wx.AcceleratorEntry(wx.ACCEL_CTRL | wx.ACCEL_SHIFT, ord('S'), wx.ID_SAVEAS),
            wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('Z'), wx.ID_UNDO),
            wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('Y'), wx.ID_REDO),
            wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('X'), wx.ID_CUT),
            wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('C'), wx.ID_COPY),
            wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('V'), wx.ID_PASTE),
            wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('F'), wx.ID_FIND),
            wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('H'), wx.ID_REPLACE),
            wx.AcceleratorEntry(wx.ACCEL_NORMAL, wx.WXK_F1, wx.ID_HELP),
            wx.AcceleratorEntry(wx.ACCEL_NORMAL, wx.WXK_F9, 1001),
            wx.AcceleratorEntry(wx.ACCEL_NORMAL, wx.WXK_F11, 1007),
        ]
        
        accel_table = wx.AcceleratorTable(accel_entries)
        self.SetAcceleratorTable(accel_table)
    
    def setup_events(self):
        """Bind window events"""
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Bind(wx.EVT_SIZE, self.on_size)
        
        # Menu events
        self.Bind(wx.EVT_MENU, self.on_new, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.on_open, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.on_save, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.on_exit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.on_about, id=wx.ID_ABOUT)
        
        # View menu events
        self.Bind(wx.EVT_MENU, self.on_toggle_sidebar, id=1001)
        self.Bind(wx.EVT_MENU, self.on_toggle_toolbar, id=1002)
        self.Bind(wx.EVT_MENU, self.on_toggle_statusbar, id=1003)
        self.Bind(wx.EVT_MENU, self.on_fullscreen, id=1007)
    
    # Event handlers
    def on_new(self, event):
        """Handle new file creation"""
        # Create new tab in notebook
        new_panel = MainContentPanel(self.content_notebook, self.framework)
        page_count = self.content_notebook.GetPageCount()
        self.content_notebook.AddPage(new_panel, f"Document {page_count + 1}", True)
        
        self.statusbar.SetStatusText("New document created", 0)
    
    def on_open(self, event):
        """Handle file opening with advanced dialog"""
        wildcard = (
            "All supported files (*.json;*.txt;*.csv)|*.json;*.txt;*.csv|"
            "JSON files (*.json)|*.json|"
            "Text files (*.txt)|*.txt|"
            "CSV files (*.csv)|*.csv|"
            "All files (*.*)|*.*"
        )
        
        dialog = wx.FileDialog(
            self,
            message="Open file",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        )
        
        if dialog.ShowModal() == wx.ID_OK:
            file_path = dialog.GetPath()
            self.load_file(file_path)
            
        dialog.Destroy()
    
    def on_save(self, event):
        """Handle file saving"""
        current_page = self.content_notebook.GetCurrentPage()
        if isinstance(current_page, MainContentPanel):
            current_page.save_content()
            self.statusbar.SetStatusText("File saved", 0)
    
    def on_toggle_sidebar(self, event):
        """Toggle sidebar visibility"""
        pane = self.aui_manager.GetPane("sidebar")
        pane.Show(not pane.IsShown())
        self.aui_manager.Update()
        
        # Update menu check state
        self.view_sidebar.Check(pane.IsShown())
    
    def on_fullscreen(self, event):
        """Toggle fullscreen mode"""
        self.ShowFullScreen(not self.IsFullScreen())
    
    def load_file(self, file_path: str):
        """Load file with appropriate handler"""
        try:
            # Create new tab for the file
            file_panel = MainContentPanel(self.content_notebook, self.framework)
            file_panel.load_file(file_path)
            
            file_name = Path(file_path).name
            self.content_notebook.AddPage(file_panel, file_name, True)
            
            # Add to recent files
            self.add_to_recent_files(file_path)
            
            self.statusbar.SetStatusText(f"Loaded: {file_name}", 0)
            
        except Exception as e:
            wx.MessageBox(
                f"Error loading file: {str(e)}",
                "Load Error",
                wx.OK | wx.ICON_ERROR
            )
    
    def save_perspective(self):
        """Save current AUI perspective"""
        perspective = self.aui_manager.SavePerspective()
        settings = self.framework.get_service('settings')
        if settings:
            settings.set('ui.perspective', perspective)
    
    def load_perspective(self):
        """Load saved AUI perspective"""
        settings = self.framework.get_service('settings')
        if settings:
            perspective = settings.get('ui.perspective')
            if perspective:
                self.aui_manager.LoadPerspective(perspective)
    
    def on_close(self, event):
        """Handle window closing with cleanup"""
        # Save current perspective
        self.save_perspective()
        
        # Cleanup AUI manager
        self.aui_manager.UnInit()
        
        event.Skip()

# Advanced content panel with rich editing capabilities
class MainContentPanel(wx.Panel):
    """
    Main content panel with advanced text editing and data visualization:
    - Rich text editing with syntax highlighting
    - Data grid for tabular data
    - Chart integration for data visualization
    - Search and replace functionality
    """
    
    def __init__(self, parent, framework: DesktopApplicationFramework):
        super().__init__(parent)
        self.framework = framework
        self.current_file = None
        
        self.create_controls()
        self.setup_layout()
        self.setup_events()
    
    def create_controls(self):
        """Create panel controls"""
        
        # Create notebook for different views
        self.notebook = wx.Notebook(self)
        
        # Text editor page
        self.text_editor = wx.stc.StyledTextCtrl(self.notebook)
        self.setup_text_editor()
        self.notebook.AddPage(self.text_editor, "Text Editor")
        
        # Data grid page
        self.data_grid = wx.grid.Grid(self.notebook)
        self.data_grid.CreateGrid(0, 0)
        self.notebook.AddPage(self.data_grid, "Data Grid")
        
        # Chart page (using matplotlib)
        try:
            import matplotlib
            matplotlib.use('WXAgg')
            from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
            from matplotlib.figure import Figure
            
            self.chart_panel = wx.Panel(self.notebook)
            self.figure = Figure()
            self.canvas = FigureCanvas(self.chart_panel, -1, self.figure)
            
            chart_sizer = wx.BoxSizer(wx.VERTICAL)
            chart_sizer.Add(self.canvas, 1, wx.EXPAND)
            self.chart_panel.SetSizer(chart_sizer)
            
            self.notebook.AddPage(self.chart_panel, "Charts")
            
        except ImportError:
            # Matplotlib not available
            pass
    
    def setup_text_editor(self):
        """Configure advanced text editor with syntax highlighting"""
        
        # Set lexer for syntax highlighting (example: Python)
        self.text_editor.SetLexer(wx.stc.STC_LEX_PYTHON)
        
        # Set font
        font = wx.Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.text_editor.StyleSetFont(wx.stc.STC_STYLE_DEFAULT, font)
        
        # Configure syntax highlighting colors
        self.text_editor.StyleSetForeground(wx.stc.STC_P_DEFAULT, wx.Colour(0, 0, 0))
        self.text_editor.StyleSetForeground(wx.stc.STC_P_COMMENTLINE, wx.Colour(0, 127, 0))
        self.text_editor.StyleSetForeground(wx.stc.STC_P_COMMENTBLOCK, wx.Colour(0, 127, 0))
        self.text_editor.StyleSetForeground(wx.stc.STC_P_NUMBER, wx.Colour(127, 127, 0))
        self.text_editor.StyleSetForeground(wx.stc.STC_P_STRING, wx.Colour(127, 0, 127))
        self.text_editor.StyleSetForeground(wx.stc.STC_P_WORD, wx.Colour(0, 0, 127))
        
        # Set keywords
        keywords = "and as assert break class continue def del elif else except exec finally for from global if import in is lambda not or pass print raise return try while with yield"
        self.text_editor.SetKeyWords(0, keywords)
        
        # Configure editor features
        self.text_editor.SetIndent(4)
        self.text_editor.SetUseTabs(False)
        self.text_editor.SetTabWidth(4)
        self.text_editor.SetBackSpaceUnIndents(True)
        
        # Show line numbers
        self.text_editor.SetMarginType(0, wx.stc.STC_MARGIN_NUMBER)
        self.text_editor.SetMarginWidth(0, 40)
        self.text_editor.SetMarginLineNumbers(0, True)
        
        # Enable folding
        self.text_editor.SetProperty("fold", "1")
        self.text_editor.SetMarginType(1, wx.stc.STC_MARGIN_SYMBOL)
        self.text_editor.SetMarginMask(1, wx.stc.STC_MASK_FOLDERS)
        self.text_editor.SetMarginWidth(1, 20)
        self.text_editor.SetMarginSensitive(1, True)
    
    def setup_layout(self):
        """Setup panel layout"""
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)
    
    def setup_events(self):
        """Bind panel events"""
        self.text_editor.Bind(wx.stc.EVT_STC_CHANGE, self.on_text_change)
        self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_page_changed)
    
    def on_text_change(self, event):
        """Handle text changes"""
        # Update status bar with cursor position
        pos = self.text_editor.GetCurrentPos()
        line = self.text_editor.LineFromPosition(pos) + 1
        col = self.text_editor.GetColumn(pos) + 1
        
        parent = self.GetTopLevelParent()
        if hasattr(parent, 'statusbar'):
            parent.statusbar.SetStatusText(f"Ln {line}, Col {col}", 2)
    
    def load_file(self, file_path: str):
        """Load file content based on file type"""
        self.current_file = file_path
        file_ext = Path(file_path).suffix.lower()
        
        try:
            if file_ext in ['.txt', '.py', '.js', '.html', '.css', '.md']:
                # Load as text
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.text_editor.SetText(content)
                    self.notebook.SetSelection(0)  # Switch to text editor
                    
            elif file_ext == '.csv':
                # Load as CSV into data grid
                self.load_csv_data(file_path)
                self.notebook.SetSelection(1)  # Switch to data grid
                
            elif file_ext == '.json':
                # Load JSON and display formatted
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    formatted = json.dumps(data, indent=2, ensure_ascii=False)
                    self.text_editor.SetText(formatted)
                    self.notebook.SetSelection(0)
        
        except Exception as e:
            wx.MessageBox(f"Error loading file: {str(e)}", "Load Error", wx.OK | wx.ICON_ERROR)
    
    def load_csv_data(self, file_path: str):
        """Load CSV data into the data grid"""
        import csv
        
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        if not rows:
            return
        
        # Clear existing grid
        if self.data_grid.GetNumberRows() > 0:
            self.data_grid.DeleteRows(0, self.data_grid.GetNumberRows())
        if self.data_grid.GetNumberCols() > 0:
            self.data_grid.DeleteCols(0, self.data_grid.GetNumberCols())
        
        # Set up grid dimensions
        headers = rows[0]
        data_rows = rows[1:]
        
        self.data_grid.AppendCols(len(headers))
        self.data_grid.AppendRows(len(data_rows))
        
        # Set column headers
        for i, header in enumerate(headers):
            self.data_grid.SetColLabelValue(i, header)
        
        # Fill data
        for row_idx, row_data in enumerate(data_rows):
            for col_idx, cell_value in enumerate(row_data):
                if col_idx < len(headers):
                    self.data_grid.SetCellValue(row_idx, col_idx, cell_value)
        
        self.data_grid.AutoSizeColumns()
    
    def save_content(self):
        """Save current content to file"""
        if not self.current_file:
            return
        
        current_page = self.notebook.GetSelection()
        
        try:
            if current_page == 0:  # Text editor
                content = self.text_editor.GetText()
                with open(self.current_file, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            elif current_page == 1:  # Data grid
                self.save_csv_data()
                
        except Exception as e:
            wx.MessageBox(f"Error saving file: {str(e)}", "Save Error", wx.OK | wx.ICON_ERROR)
    
    def save_csv_data(self):
        """Save data grid content as CSV"""
        import csv
        
        with open(self.current_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write headers
            headers = []
            for col in range(self.data_grid.GetNumberCols()):
                headers.append(self.data_grid.GetColLabelValue(col))
            writer.writerow(headers)
            
            # Write data
            for row in range(self.data_grid.GetNumberRows()):
                row_data = []
                for col in range(self.data_grid.GetNumberCols()):
                    row_data.append(self.data_grid.GetCellValue(row, col))
                writer.writerow(row_data)

# Advanced sidebar panel with tree control and custom features
class SidebarPanel(wx.Panel):
    """
    Advanced sidebar with:
    - File explorer tree
    - Project structure navigation
    - Bookmark management
    - Search functionality
    """
    
    def __init__(self, parent, framework: DesktopApplicationFramework):
        super().__init__(parent)
        self.framework = framework
        self.create_controls()
        self.setup_layout()
        self.setup_events()
    
    def create_controls(self):
        """Create sidebar controls"""
        
        # Create notebook for different sidebar views
        self.notebook = wx.Notebook(self)
        
        # File explorer page
        self.file_panel = wx.Panel(self.notebook)
        self.create_file_explorer(self.file_panel)
        self.notebook.AddPage(self.file_panel, "Explorer")
        
        # Bookmarks page
        self.bookmark_panel = wx.Panel(self.notebook)
        self.create_bookmarks(self.bookmark_panel)
        self.notebook.AddPage(self.bookmark_panel, "Bookmarks")
        
        # Search page
        self.search_panel = wx.Panel(self.notebook)
        self.create_search(self.search_panel)
        self.notebook.AddPage(self.search_panel, "Search")
    
    def create_file_explorer(self, parent):
        """Create file explorer with advanced tree control"""
        
        # Toolbar for file operations
        toolbar = wx.ToolBar(parent, style=wx.TB_HORIZONTAL | wx.TB_FLAT)
        toolbar.SetToolBitmapSize((16, 16))
        
        # Add toolbar buttons
        refresh_bmp = wx.ArtProvider.GetBitmap(wx.ART_REDO, wx.ART_TOOLBAR, (16, 16))
        home_bmp = wx.ArtProvider.GetBitmap(wx.ART_GO_HOME, wx.ART_TOOLBAR, (16, 16))
        up_bmp = wx.ArtProvider.GetBitmap(wx.ART_GO_UP, wx.ART_TOOLBAR, (16, 16))
        
        toolbar.AddTool(3001, "Refresh", refresh_bmp, "Refresh file list")
        toolbar.AddTool(3002, "Home", home_bmp, "Go to home directory")
        toolbar.AddTool(3003, "Up", up_bmp, "Go up one level")
        toolbar.Realize()
        
        # File tree control
        self.file_tree = wx.TreeCtrl(
            parent,
            style=wx.TR_DEFAULT_STYLE | wx.TR_EDIT_LABELS
        )
        
        # Set up tree with root
        self.populate_file_tree()
        
        # Layout for file panel
        file_sizer = wx.BoxSizer(wx.VERTICAL)
        file_sizer.Add(toolbar, 0, wx.EXPAND)
        file_sizer.Add(self.file_tree, 1, wx.EXPAND)
        parent.SetSizer(file_sizer)
    
    def populate_file_tree(self):
        """Populate file tree with directory structure"""
        
        # Clear existing items
        self.file_tree.DeleteAllItems()
        
        # Add root item
        root_path = Path.home()
        root_item = self.file_tree.AddRoot(str(root_path), data=root_path)
        
        # Add initial directories
        self.add_directory_items(root_item, root_path)
        
        # Expand root
        self.file_tree.Expand(root_item)
    
    def add_directory_items(self, parent_item, dir_path: Path, max_items: int = 50):
        """Add directory items to tree"""
        try:
            items = list(dir_path.iterdir())
            items.sort(key=lambda x: (not x.is_dir(), x.name.lower()))
            
            count = 0
            for item in items:
                if count >= max_items:
                    break
                
                if item.name.startswith('.'):
                    continue
                
                if item.is_dir():
                    tree_item = self.file_tree.AppendItem(
                        parent_item, 
                        item.name, 
                        data=item
                    )
                    
                    # Add dummy child for expandable appearance
                    self.file_tree.AppendItem(tree_item, "Loading...", data=None)
                    
                else:
                    self.file_tree.AppendItem(
                        parent_item,
                        item.name,
                        data=item
                    )
                
                count += 1
                
        except PermissionError:
            # Can't access directory
            pass
        except Exception as e:
            print(f"Error loading directory {dir_path}: {e}")

# Service classes for application architecture
class BaseService(ABC):
    """Base class for application services"""
    
    def __init__(self):
        self.framework: Optional[DesktopApplicationFramework] = None
    
    def set_framework(self, framework: DesktopApplicationFramework):
        """Set framework reference"""
        self.framework = framework
    
    @abstractmethod
    def cleanup(self):
        """Cleanup service resources"""
        pass

class DataService(BaseService):
    """Data persistence and management service"""
    
    def __init__(self):
        super().__init__()
        self.db_path = Path.home() / ".modernapp" / "data.db"
        self.db_path.parent.mkdir(exist_ok=True)
        self.init_database()
    
    def init_database(self):
        """Initialize SQLite database"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS documents (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    content TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS settings (
                    key TEXT PRIMARY KEY,
                    value TEXT
                )
            """)
            
            conn.commit()
    
    def save_document(self, name: str, content: str) -> int:
        """Save document to database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO documents (name, content) VALUES (?, ?)",
                (name, content)
            )
            conn.commit()
            return cursor.lastrowid
    
    def load_document(self, doc_id: int) -> Optional[Dict]:
        """Load document from database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT id, name, content, created_at, updated_at FROM documents WHERE id = ?",
                (doc_id,)
            )
            row = cursor.fetchone()
            
            if row:
                return {
                    'id': row[0],
                    'name': row[1],
                    'content': row[2],
                    'created_at': row[3],
                    'updated_at': row[4]
                }
            return None
    
    def list_documents(self) -> List[Dict]:
        """List all documents"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT id, name, created_at, updated_at FROM documents ORDER BY updated_at DESC"
            )
            
            return [
                {
                    'id': row[0],
                    'name': row[1],
                    'created_at': row[2],
                    'updated_at': row[3]
                }
                for row in cursor.fetchall()
            ]
    
    def cleanup(self):
        """Cleanup database connections"""
        pass

class SettingsService(BaseService):
    """User settings and preferences service"""
    
    def __init__(self):
        super().__init__()
        self.settings = {}
        self.settings_file = Path.home() / ".modernapp" / "settings.json"
        self.settings_file.parent.mkdir(exist_ok=True)
        self.load_settings()
    
    def load_settings(self):
        """Load settings from file"""
        if self.settings_file.exists():
            try:
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    self.settings = json.load(f)
            except Exception as e:
                print(f"Error loading settings: {e}")
                self.settings = {}
    
    def save_settings(self):
        """Save settings to file"""
        try:
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=2)
        except Exception as e:
            print(f"Error saving settings: {e}")
    
    def get(self, key: str, default=None):
        """Get setting value"""
        keys = key.split('.')
        value = self.settings
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value):
        """Set setting value"""
        keys = key.split('.')
        current = self.settings
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
        self.save_settings()
    
    def cleanup(self):
        """Cleanup settings service"""
        self.save_settings()

# Event management system
class EventManager:
    """Application-wide event management"""
    
    def __init__(self):
        self.listeners: Dict[str, List[Callable]] = {}
    
    def subscribe(self, event_type: str, callback: Callable):
        """Subscribe to an event"""
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(callback)
    
    def unsubscribe(self, event_type: str, callback: Callable):
        """Unsubscribe from an event"""
        if event_type in self.listeners:
            self.listeners[event_type].remove(callback)
    
    def emit(self, event_type: str, data=None):
        """Emit an event to all listeners"""
        if event_type in self.listeners:
            for callback in self.listeners[event_type]:
                try:
                    callback(data)
                except Exception as e:
                    print(f"Error in event handler: {e}")

# Configuration management
class ConfigurationManager:
    """Application configuration management"""
    
    def __init__(self):
        self.config = {}
        self.config_file = Path.home() / ".modernapp" / "config.json"
    
    def load_config(self):
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
            except Exception as e:
                print(f"Error loading config: {e}")
    
    def save_config(self):
        """Save configuration to file"""
        self.config_file.parent.mkdir(exist_ok=True)
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key: str, value):
        """Set configuration value"""
        self.config[key] = value

# Application entry point
def main():
    """Application entry point"""
    app = ModernDesktopApp("Modern Desktop App")
    app.MainLoop()

if __name__ == "__main__":
    main()
```

### Phase 2: Advanced Threading and Async Operations

**Threading and Background Processing Framework:**
```python
import asyncio
import concurrent.futures
from threading import Thread, Event, Lock
from queue import Queue, Empty
import time
from typing import Callable, Any, Optional

class ThreadingFramework:
    """
    Advanced threading framework for wxPython applications:
    - Background task execution
    - Progress reporting
    - Thread-safe GUI updates
    - Async/await integration
    """
    
    def __init__(self, app_framework: DesktopApplicationFramework):
        self.app_framework = app_framework
        self.background_tasks = {}
        self.task_counter = 0
        self.gui_update_queue = Queue()
        self.setup_gui_updater()
    
    def setup_gui_updater(self):
        """Setup GUI update mechanism from background threads"""
        
        # Custom event for GUI updates
        self.UpdateUIEvent, EVT_UPDATE_UI = wx.lib.newevent.NewEvent()
        
        # Timer to process GUI updates
        self.update_timer = wx.Timer()
        self.update_timer.Bind(wx.EVT_TIMER, self.process_gui_updates)
        self.update_timer.Start(50)  # 20 FPS update rate
    
    def process_gui_updates(self, event):
        """Process queued GUI updates"""
        try:
            while True:
                update_func = self.gui_update_queue.get_nowait()
                wx.CallAfter(update_func)
        except Empty:
            pass
    
    def run_background_task(
        self,
        task_func: Callable,
        on_complete: Optional[Callable] = None,
        on_progress: Optional[Callable] = None,
        on_error: Optional[Callable] = None,
        task_name: str = None
    ) -> str:
        """Run a function in background thread with progress reporting"""
        
        task_id = f"task_{self.task_counter}"
        self.task_counter += 1
        
        if task_name is None:
            task_name = f"Background Task {task_id}"
        
        # Progress tracking
        progress_tracker = ProgressTracker(task_id, task_name)
        
        def wrapped_task():
            try:
                result = task_func(progress_tracker)
                
                if on_complete:
                    self.gui_update_queue.put(lambda: on_complete(result))
                    
            except Exception as e:
                if on_error:
                    self.gui_update_queue.put(lambda: on_error(e))
                else:
                    # Default error handling
                    self.gui_update_queue.put(
                        lambda: wx.MessageBox(
                            f"Background task error: {str(e)}",
                            "Task Error",
                            wx.OK | wx.ICON_ERROR
                        )
                    )
            finally:
                # Cleanup task reference
                if task_id in self.background_tasks:
                    del self.background_tasks[task_id]
        
        # Create and start thread
        thread = Thread(target=wrapped_task, daemon=True)
        self.background_tasks[task_id] = {
            'thread': thread,
            'progress_tracker': progress_tracker,
            'name': task_name
        }
        
        thread.start()
        
        # Setup progress updates if callback provided
        if on_progress:
            def progress_updater():
                while task_id in self.background_tasks:
                    progress = progress_tracker.get_progress()
                    self.gui_update_queue.put(lambda p=progress: on_progress(p))
                    time.sleep(0.1)
            
            Thread(target=progress_updater, daemon=True).start()
        
        return task_id
    
    def cancel_task(self, task_id: str):
        """Cancel a background task"""
        if task_id in self.background_tasks:
            task_info = self.background_tasks[task_id]
            task_info['progress_tracker'].cancel()
    
    def get_active_tasks(self) -> List[Dict]:
        """Get list of active background tasks"""
        return [
            {
                'id': task_id,
                'name': info['name'],
                'progress': info['progress_tracker'].get_progress()
            }
            for task_id, info in self.background_tasks.items()
        ]

class ProgressTracker:
    """Thread-safe progress tracking for background tasks"""
    
    def __init__(self, task_id: str, task_name: str):
        self.task_id = task_id
        self.task_name = task_name
        self.progress = 0.0
        self.status = "Starting..."
        self.cancelled = Event()
        self.lock = Lock()
    
    def update_progress(self, progress: float, status: str = None):
        """Update task progress"""
        with self.lock:
            self.progress = max(0.0, min(1.0, progress))
            if status:
                self.status = status
    
    def get_progress(self) -> Dict:
        """Get current progress information"""
        with self.lock:
            return {
                'task_id': self.task_id,
                'task_name': self.task_name,
                'progress': self.progress,
                'status': self.status,
                'cancelled': self.cancelled.is_set()
            }
    
    def is_cancelled(self) -> bool:
        """Check if task was cancelled"""
        return self.cancelled.is_set()
    
    def cancel(self):
        """Cancel the task"""
        self.cancelled.set()

# Advanced progress dialog with cancellation
class ProgressDialog(wx.Dialog):
    """
    Advanced progress dialog with:
    - Real-time progress updates
    - Task cancellation
    - Detailed status information
    - Multiple task monitoring
    """
    
    def __init__(self, parent, title="Progress", style=wx.DEFAULT_DIALOG_STYLE):
        super().__init__(parent, title=title, style=style)
        
        self.task_id = None
        self.threading_framework = None
        self.cancelled = False
        
        self.create_controls()
        self.setup_layout()
        self.setup_events()
    
    def create_controls(self):
        """Create dialog controls"""
        
        # Task name label
        self.task_label = wx.StaticText(self, label="Task:")
        
        # Progress gauge
        self.progress_gauge = wx.Gauge(self, range=100, size=(400, 25))
        
        # Progress text
        self.progress_text = wx.StaticText(self, label="0%")
        
        # Status text
        self.status_text = wx.StaticText(self, label="Preparing...")
        
        # Detailed log (expandable)
        self.detail_button = wx.Button(self, label="Details >>")
        self.log_text = wx.TextCtrl(
            self,
            style=wx.TE_MULTILINE | wx.TE_READONLY,
            size=(400, 150)
        )
        self.log_text.Hide()
        
        # Buttons
        self.cancel_button = wx.Button(self, wx.ID_CANCEL, "Cancel")
        self.close_button = wx.Button(self, wx.ID_CLOSE, "Close")
        self.close_button.Enable(False)
    
    def setup_layout(self):
        """Setup dialog layout"""
        
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Task info
        main_sizer.Add(self.task_label, 0, wx.EXPAND | wx.ALL, 10)
        
        # Progress
        progress_sizer = wx.BoxSizer(wx.HORIZONTAL)
        progress_sizer.Add(self.progress_gauge, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
        progress_sizer.Add(self.progress_text, 0, wx.ALIGN_CENTER_VERTICAL)
        
        main_sizer.Add(progress_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        
        # Status
        main_sizer.Add(self.status_text, 0, wx.EXPAND | wx.ALL, 10)
        
        # Details button
        main_sizer.Add(self.detail_button, 0, wx.ALIGN_RIGHT | wx.RIGHT | wx.BOTTOM, 10)
        
        # Log (hidden initially)
        main_sizer.Add(self.log_text, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)
        
        # Buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(self.cancel_button, 0, wx.RIGHT, 10)
        button_sizer.Add(self.close_button, 0)
        
        main_sizer.Add(button_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
        
        self.SetSizer(main_sizer)
        self.Fit()
    
    def setup_events(self):
        """Bind dialog events"""
        self.detail_button.Bind(wx.EVT_BUTTON, self.on_toggle_details)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)
        self.close_button.Bind(wx.EVT_BUTTON, self.on_close)
        self.Bind(wx.EVT_CLOSE, self.on_close)
    
    def start_task(
        self,
        threading_framework: ThreadingFramework,
        task_func: Callable,
        task_name: str = "Task"
    ):
        """Start monitoring a background task"""
        
        self.threading_framework = threading_framework
        self.task_label.SetLabel(f"Task: {task_name}")
        
        # Start the task
        self.task_id = threading_framework.run_background_task(
            task_func,
            on_complete=self.on_task_complete,
            on_progress=self.on_progress_update,
            on_error=self.on_task_error,
            task_name=task_name
        )
        
        # Setup progress monitoring
        self.progress_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_progress, self.progress_timer)
        self.progress_timer.Start(100)  # Update every 100ms
    
    def update_progress(self, event):
        """Update progress display"""
        if not self.threading_framework or not self.task_id:
            return
        
        if self.task_id not in self.threading_framework.background_tasks:
            # Task completed or cancelled
            self.progress_timer.Stop()
            return
        
        task_info = self.threading_framework.background_tasks[self.task_id]
        progress_info = task_info['progress_tracker'].get_progress()
        
        # Update progress bar
        progress_percent = int(progress_info['progress'] * 100)
        self.progress_gauge.SetValue(progress_percent)
        self.progress_text.SetLabel(f"{progress_percent}%")
        
        # Update status
        self.status_text.SetLabel(progress_info['status'])
        
        # Add to log
        self.log_text.AppendText(f"{time.strftime('%H:%M:%S')} - {progress_info['status']}\n")
    
    def on_progress_update(self, progress_info):
        """Handle progress update from task"""
        # This is called from the GUI thread
        pass  # Updates handled by timer
    
    def on_task_complete(self, result):
        """Handle task completion"""
        self.progress_gauge.SetValue(100)
        self.progress_text.SetLabel("100%")
        self.status_text.SetLabel("Completed successfully")
        
        self.cancel_button.Enable(False)
        self.close_button.Enable(True)
        
        self.log_text.AppendText(f"{time.strftime('%H:%M:%S')} - Task completed\n")
    
    def on_task_error(self, error):
        """Handle task error"""
        self.status_text.SetLabel(f"Error: {str(error)}")
        
        self.cancel_button.Enable(False)
        self.close_button.Enable(True)
        
        self.log_text.AppendText(f"{time.strftime('%H:%M:%S')} - Error: {str(error)}\n")
    
    def on_toggle_details(self, event):
        """Toggle details visibility"""
        if self.log_text.IsShown():
            self.log_text.Hide()
            self.detail_button.SetLabel("Details >>")
        else:
            self.log_text.Show()
            self.detail_button.SetLabel("<< Details")
        
        self.Layout()
        self.Fit()
    
    def on_cancel(self, event):
        """Handle cancel button"""
        if self.threading_framework and self.task_id:
            self.threading_framework.cancel_task(self.task_id)
            self.cancelled = True
            
            self.cancel_button.Enable(False)
            self.status_text.SetLabel("Cancelling...")
    
    def on_close(self, event):
        """Handle dialog close"""
        if self.task_id and not self.cancelled:
            # Ask for confirmation if task is still running
            if wx.MessageBox(
                "Task is still running. Cancel and close?",
                "Confirm Close",
                wx.YES_NO | wx.ICON_QUESTION
            ) == wx.YES:
                if self.threading_framework:
                    self.threading_framework.cancel_task(self.task_id)
                event.Skip()
        else:
            event.Skip()

# Example usage of advanced threading
class DataProcessingTask:
    """Example of a complex background task"""
    
    @staticmethod
    def process_large_dataset(progress_tracker: ProgressTracker):
        """Simulate processing a large dataset"""
        
        total_items = 1000
        processed = 0
        
        for i in range(total_items):
            # Check for cancellation
            if progress_tracker.is_cancelled():
                return "Task cancelled"
            
            # Simulate work
            time.sleep(0.01)
            
            processed += 1
            progress = processed / total_items
            
            # Update progress
            progress_tracker.update_progress(
                progress,
                f"Processing item {processed}/{total_items}"
            )
        
        return f"Processed {processed} items successfully"

# Integration example
def show_progress_task_example(parent):
    """Example of using the progress dialog with background task"""
    
    dialog = ProgressDialog(parent, "Data Processing")
    
    # Get threading framework from application
    app = wx.GetApp()
    if hasattr(app, 'framework'):
        threading_framework = ThreadingFramework(app.framework)
        
        dialog.start_task(
            threading_framework,
            DataProcessingTask.process_large_dataset,
            "Large Dataset Processing"
        )
        
        dialog.ShowModal()
        dialog.Destroy()
```

## Success Criteria

1. **Desktop Application Excellence:**
   - Cross-platform compatibility across Windows, macOS, and Linux
   - Native look and feel with platform-specific integrations
   - Advanced UI patterns with docking, tabbed interfaces, and custom controls

2. **Performance and Responsiveness:**
   - Non-blocking UI with proper threading for background operations
   - Efficient memory management and resource cleanup
   - Smooth animations and responsive user interactions

3. **Data Management:**
   - Robust data persistence with SQLite integration
   - User settings and configuration management
   - Import/export capabilities for various file formats

4. **Developer Experience:**
   - Clean MVC/MVP architecture with separation of concerns
   - Comprehensive error handling and logging
   - Extensible plugin architecture for custom functionality

## Deliverables

- **Application Framework:** Complete wxPython architecture with modern patterns
- **UI Component Library:** Advanced controls and custom widgets
- **Threading Framework:** Background processing with progress reporting
- **Data Services:** Persistence layer with database integration
- **Testing Framework:** Unit and integration testing for desktop applications
- **Packaging Solutions:** Cross-platform distribution and installer creation
- **Documentation:** Complete development guide with best practices and deployment strategies