import sys
import json
from definitions import TEARDOWN_FUNCTIONS, get_categories, get_functions_by_category
from snippets import CODE_SNIPPETS, FUNCTION_TEMPLATES, get_snippet_categories, is_snippet
from templates import BEGINNER_TEMPLATES, COMMON_PATTERNS, get_all_template_names, get_all_pattern_names
from themes import THEMES, DEFAULT_THEME_NAME
from styles import (
    build_app_stylesheet,
    build_documentation_stylesheet,
    build_function_button_style,
    build_snippet_button_style,
)
from validator import build_api_catalog, validate_script
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QPlainTextEdit, QTextEdit, QPushButton, QScrollArea,
                            QSplitter, QGroupBox, QLabel, QLineEdit, QComboBox,
                            QTabWidget, QMessageBox, QListWidget, QListWidgetItem,
                            QCheckBox)
from PyQt6.QtCore import Qt, QTimer, QSettings, QRect, QSize
from PyQt6.QtGui import QFont, QSyntaxHighlighter, QTextCharFormat, QColor, QAction, QKeySequence, QPainter, QTextFormat


class LineNumberArea(QWidget):
    """Widget that displays line numbers for the code editor"""
    def __init__(self, editor):
        super().__init__(editor)
        self.code_editor = editor

    def sizeHint(self):
        return QSize(self.code_editor.line_number_area_width(), 0)

    def paintEvent(self, event):
        self.code_editor.line_number_area_paint_event(event)


class CodeEditor(QPlainTextEdit):
    """Code editor with line numbers"""
    def __init__(self, parent=None):
        super().__init__(parent)

        # Store theme colors for line numbers (must be set before highlight_current_line)
        self.line_number_bg = "#2b2b2b"
        self.line_number_fg = "#858585"
        self.current_line_bg = "#323232"

        self.line_number_area = LineNumberArea(self)

        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)
        self.cursorPositionChanged.connect(self.highlight_current_line)

        self.update_line_number_area_width(0)
        self.highlight_current_line()

    def set_line_number_colors(self, bg_color, fg_color, current_line_color):
        """Update line number colors based on theme"""
        self.line_number_bg = bg_color
        self.line_number_fg = fg_color
        self.current_line_bg = current_line_color
        self.line_number_area.update()
        self.highlight_current_line()

    def line_number_area_width(self):
        digits = 1
        max_num = max(1, self.blockCount())
        while max_num >= 10:
            max_num //= 10
            digits += 1
        space = 10 + self.fontMetrics().horizontalAdvance('9') * digits
        return space

    def update_line_number_area_width(self, _):
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    def update_line_number_area(self, rect, dy):
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            self.line_number_area.update(0, rect.y(), self.line_number_area.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.line_number_area.setGeometry(QRect(cr.left(), cr.top(), 
                                                 self.line_number_area_width(), cr.height()))

    def highlight_current_line(self):
        extra_selections = []

        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            line_color = QColor(self.current_line_bg)
            selection.format.setBackground(line_color)
            selection.format.setProperty(QTextFormat.Property.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extra_selections.append(selection)

        self.setExtraSelections(extra_selections)

    def line_number_area_paint_event(self, event):
        painter = QPainter(self.line_number_area)
        painter.fillRect(event.rect(), QColor(self.line_number_bg))

        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = round(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + round(self.blockBoundingRect(block).height())

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.setPen(QColor(self.line_number_fg))
                painter.drawText(0, top, self.line_number_area.width() - 5, 
                               self.fontMetrics().height(),
                               Qt.AlignmentFlag.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + round(self.blockBoundingRect(block).height())
            block_number += 1


class LuaSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None, theme_colors=None):
        super().__init__(parent)
        self._highlighting_rules = []

        # Use theme colors or defaults
        if theme_colors is None:
            theme_colors = THEMES[DEFAULT_THEME_NAME]["syntax"]

        # Lua keywords
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor(theme_colors["keyword"]))
        keyword_format.setFontWeight(QFont.Weight.Bold)
        keywords = [
            "and", "break", "do", "else", "elseif", "end", "false", "for", 
            "function", "if", "in", "local", "nil", "not", "or", "repeat", 
            "return", "then", "true", "until", "while"
        ]
        for word in keywords:
            self._highlighting_rules.append((rf"\b{word}\b", keyword_format))

        # Function format
        function_format = QTextCharFormat()
        function_format.setForeground(QColor(theme_colors["function"]))
        self._highlighting_rules.append((rf"\b[a-zA-Z_][a-zA-Z0-9_]*\s*\(", function_format))

        # String format
        string_format = QTextCharFormat()
        string_format.setForeground(QColor(theme_colors["string"]))
        self._highlighting_rules.append((r'"[^"]*"', string_format))
        self._highlighting_rules.append((r"'[^']*'", string_format))

        # Comment format
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor(theme_colors["comment"]))
        self._highlighting_rules.append((r"--.*$", comment_format))
        self._highlighting_rules.append((r"--\[\[.*?\]\]", comment_format))

    def update_theme(self, theme_colors):
        """Update syntax highlighting colors for new theme"""
        self._highlighting_rules = []

        # Lua keywords
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor(theme_colors["keyword"]))
        keyword_format.setFontWeight(QFont.Weight.Bold)
        keywords = [
            "and", "break", "do", "else", "elseif", "end", "false", "for", 
            "function", "if", "in", "local", "nil", "not", "or", "repeat", 
            "return", "then", "true", "until", "while"
        ]
        for word in keywords:
            self._highlighting_rules.append((rf"\b{word}\b", keyword_format))

        # Function format
        function_format = QTextCharFormat()
        function_format.setForeground(QColor(theme_colors["function"]))
        self._highlighting_rules.append((rf"\b[a-zA-Z_][a-zA-Z0-9_]*\s*\(", function_format))

        # String format
        string_format = QTextCharFormat()
        string_format.setForeground(QColor(theme_colors["string"]))
        self._highlighting_rules.append((r'"[^"]*"', string_format))
        self._highlighting_rules.append((r"'[^']*'", string_format))

        # Comment format
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor(theme_colors["comment"]))
        self._highlighting_rules.append((r"--.*$", comment_format))
        self._highlighting_rules.append((r"--\[\[.*?\]\]", comment_format))

        # Rehighlight the document
        self.rehighlight()

    def highlightBlock(self, text):
        import re
        for pattern, format in self._highlighting_rules:
            for match in re.finditer(pattern, text):
                self.setFormat(match.start(), match.end() - match.start(), format)

class FunctionButton(QPushButton):
    def __init__(self, friendly_name, actual_code, description=""):
        super().__init__(friendly_name)
        self.actual_code = actual_code
        self.description = description
        # Don't set stylesheet here - will be set by theme system
        self.setToolTip(description)

class TeardownCodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Everybody's Code - Teardown Script Editor")
        self.setGeometry(100, 100, 1400, 800)

        # Initialize theme system
        self.settings = QSettings("EverybodysCode", "TeardownEditor")
        self.current_theme = self.settings.value("theme", DEFAULT_THEME_NAME)
        if self.current_theme not in THEMES:
            self.current_theme = DEFAULT_THEME_NAME

        # Setup UI
        self.setup_ui()
        self.setup_function_categories()
        self.api_catalog = build_api_catalog(TEARDOWN_FUNCTIONS, CODE_SNIPPETS, FUNCTION_TEMPLATES)
        self.apply_theme(self.current_theme)
        
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout(central_widget)
        
        # Create splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        main_layout.addWidget(splitter)
        
        # Left panel - Function buttons
        self.left_panel = QWidget()
        left_layout = QVBoxLayout(self.left_panel)
        
        # Create tabs for different function types
        tab_widget = QTabWidget()
        left_layout.addWidget(tab_widget)

        # Functions tab (original functionality)
        functions_tab = QWidget()
        functions_layout = QVBoxLayout(functions_tab)

        # Search bar for functions
        search_layout = QHBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search functions...")
        self.search_bar.textChanged.connect(self.filter_functions)
        search_layout.addWidget(QLabel("Search:"))
        search_layout.addWidget(self.search_bar)
        functions_layout.addLayout(search_layout)

        # Category selector for functions
        self.category_combo = QComboBox()
        self.category_combo.currentTextChanged.connect(self.filter_by_category)
        functions_layout.addWidget(QLabel("Category:"))
        functions_layout.addWidget(self.category_combo)

        # Local keyword option
        self.use_local_checkbox = QCheckBox("Add 'local' to variables")
        self.use_local_checkbox.setChecked(True)  # Default to using local
        self.use_local_checkbox.setToolTip("When checked, variable declarations will include 'local' keyword")
        functions_layout.addWidget(self.use_local_checkbox)

        # Global search option for find functions
        self.use_global_search_checkbox = QCheckBox("Global search for Find functions")
        self.use_global_search_checkbox.setChecked(True)  # Default to global search
        self.use_global_search_checkbox.setToolTip("When checked, Find functions will include ', true' for global scene search")
        functions_layout.addWidget(self.use_global_search_checkbox)

        # Scroll area for function buttons
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.function_container = QWidget()
        self.function_layout = QVBoxLayout(self.function_container)
        scroll_area.setWidget(self.function_container)
        functions_layout.addWidget(scroll_area)

        tab_widget.addTab(functions_tab, "Functions")

        # Snippets tab (new functionality)
        snippets_tab = QWidget()
        snippets_layout = QVBoxLayout(snippets_tab)

        # Search bar for snippets
        snippet_search_layout = QHBoxLayout()
        self.snippet_search_bar = QLineEdit()
        self.snippet_search_bar.setPlaceholderText("Search code snippets...")
        self.snippet_search_bar.textChanged.connect(self.filter_snippets)
        snippet_search_layout.addWidget(QLabel("Search:"))
        snippet_search_layout.addWidget(self.snippet_search_bar)
        snippets_layout.addLayout(snippet_search_layout)

        # Category selector for snippets  
        self.snippet_category_combo = QComboBox()
        self.snippet_category_combo.currentTextChanged.connect(self.filter_snippets_by_category)
        snippets_layout.addWidget(QLabel("Category:"))
        snippets_layout.addWidget(self.snippet_category_combo)

        # Local keyword option for snippets (same checkbox reference)
        snippet_local_layout = QHBoxLayout()
        snippet_local_layout.addWidget(QLabel("Use same 'local' and 'global search' settings as Functions tab"))
        snippets_layout.addLayout(snippet_local_layout)

        # Scroll area for snippet buttons
        snippet_scroll_area = QScrollArea()
        snippet_scroll_area.setWidgetResizable(True)
        self.snippet_container = QWidget()
        self.snippet_layout = QVBoxLayout(self.snippet_container)
        snippet_scroll_area.setWidget(self.snippet_container)
        snippets_layout.addWidget(snippet_scroll_area)

        tab_widget.addTab(snippets_tab, "Code Snippets")

        # Templates tab (for complete project templates)
        templates_tab = QWidget()
        templates_layout = QVBoxLayout(templates_tab)

        templates_layout.addWidget(QLabel("Project Templates:"))
        self.template_list = QListWidget()
        for template_name in get_all_template_names():
            item = QListWidgetItem(template_name)
            item.setToolTip(f"Click to load the {template_name} template")
            self.template_list.addItem(item)
        self.template_list.itemClicked.connect(self.load_template)
        templates_layout.addWidget(self.template_list)

        templates_layout.addWidget(QLabel("Common Patterns:"))
        self.pattern_list = QListWidget()
        for pattern_name in get_all_pattern_names():
            item = QListWidgetItem(pattern_name)
            item.setToolTip(COMMON_PATTERNS[pattern_name]["description"])
            self.pattern_list.addItem(item)
        self.pattern_list.itemClicked.connect(self.insert_pattern)
        templates_layout.addWidget(self.pattern_list)

        tab_widget.addTab(templates_tab, "Templates")
        
        splitter.addWidget(self.left_panel)
        splitter.setSizes([400, 1000])
        
        # Right panel - Code editor and documentation
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        # Add a helpful toolbar with common actions
        toolbar_layout = QHBoxLayout()

        # Undo/Redo buttons
        self.undo_btn = QPushButton("↶ Undo")
        self.undo_btn.clicked.connect(self.undo_action)
        self.undo_btn.setToolTip("Undo last action (Ctrl+Z)")
        self.undo_btn.setEnabled(False)  # Initially disabled
        toolbar_layout.addWidget(self.undo_btn)

        self.redo_btn = QPushButton("↷ Redo")
        self.redo_btn.clicked.connect(self.redo_action)
        self.redo_btn.setToolTip("Redo last undone action (Ctrl+Y)")
        self.redo_btn.setEnabled(False)  # Initially disabled
        toolbar_layout.addWidget(self.redo_btn)

        # Separator
        separator_label = QLabel("|")
        separator_label.setStyleSheet("color: gray; font-weight: bold; margin: 0 5px;")
        toolbar_layout.addWidget(separator_label)

        # Quick action buttons
        new_mod_btn = QPushButton("🆕 New Mod")
        new_mod_btn.clicked.connect(self.new_mod)
        new_mod_btn.setToolTip("Start a fresh mod")
        toolbar_layout.addWidget(new_mod_btn)

        load_mod_btn = QPushButton("📂 Load Mod")
        load_mod_btn.clicked.connect(self.load_mod)
        load_mod_btn.setToolTip("Load a .lua script from a Teardown mod")
        toolbar_layout.addWidget(load_mod_btn)

        save_btn = QPushButton("💾 Save Code")
        save_btn.clicked.connect(self.save_code)
        save_btn.setToolTip("Save your code to a .lua file")
        toolbar_layout.addWidget(save_btn)

        help_btn = QPushButton("❓ Help")
        help_btn.clicked.connect(self.show_help)
        help_btn.setToolTip("Show help for beginners")
        toolbar_layout.addWidget(help_btn)

        validate_btn = QPushButton("✅ Validate")
        validate_btn.clicked.connect(self.run_validation)
        validate_btn.setToolTip("Validate the current script")
        toolbar_layout.addWidget(validate_btn)

        # Another separator
        separator_label2 = QLabel("|")
        separator_label2.setStyleSheet("color: gray; font-weight: bold; margin: 0 5px;")
        toolbar_layout.addWidget(separator_label2)

        # Theme selector
        theme_label = QLabel("Theme:")
        toolbar_layout.addWidget(theme_label)
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(list(THEMES.keys()))
        self.theme_combo.setCurrentText(self.current_theme)
        self.theme_combo.currentTextChanged.connect(self.change_theme)
        self.theme_combo.setToolTip("Choose a color theme")
        toolbar_layout.addWidget(self.theme_combo)

        toolbar_layout.addStretch()  # Push everything to the left
        right_layout.insertLayout(0, toolbar_layout)  # Insert at top

        # Code editor
        code_group = QGroupBox("Code Editor")
        code_layout = QVBoxLayout(code_group)
        self.code_editor = CodeEditor()
        self.code_editor.setFont(QFont("Consolas", 11))
        self.code_editor.setPlainText("-- Teardown Script\n-- Generated by Everybody's Code\n\n")

        # Enable undo/redo functionality
        self.code_editor.setUndoRedoEnabled(True)

        # Connect undo/redo availability signals
        self.code_editor.undoAvailable.connect(self.undo_btn.setEnabled)
        self.code_editor.redoAvailable.connect(self.redo_btn.setEnabled)

        # Add syntax highlighter
        self.highlighter = LuaSyntaxHighlighter(self.code_editor.document(), THEMES[self.current_theme]["syntax"])

        # Add keyboard shortcuts
        self.setup_keyboard_shortcuts()

        code_layout.addWidget(self.code_editor)
        right_layout.addWidget(code_group)

        # Documentation panel (scrollable)
        doc_group = QGroupBox("Function Documentation")
        doc_layout = QVBoxLayout(doc_group)
        self.documentation_text = QTextEdit()
        self.documentation_text.setReadOnly(True)
        self.documentation_text.setPlainText("Select a function to see documentation...")
        self.documentation_text.setStyleSheet("padding: 10px; background-color: #000000; border-radius: 4px;")
        self.documentation_text.setMinimumHeight(150)
        doc_layout.addWidget(self.documentation_text)
        right_layout.addWidget(doc_group)

        splitter.addWidget(right_panel)
        
    def setup_function_categories(self):
        # Initialize function buttons list
        self.function_buttons = []
        self.snippet_buttons = []

        # Setup main functions (original functionality)
        self.functions = TEARDOWN_FUNCTIONS
        categories = get_categories()
        self.category_combo.addItems(["All Categories"] + categories)

        # Create function buttons
        for friendly_name, func_data in self.functions.items():
            button = FunctionButton(friendly_name, func_data["code"], func_data["description"])
            button.clicked.connect(lambda checked, code=func_data["code"], desc=func_data["description"], name=friendly_name: 
                                 self.insert_code(code, desc, is_snippet=False))
            self.function_layout.addWidget(button)
            self.function_buttons.append((button, func_data["category"]))

        self.function_layout.addStretch()

        # Setup code snippets
        all_snippets = {**CODE_SNIPPETS, **FUNCTION_TEMPLATES}
        snippet_categories = get_snippet_categories()
        self.snippet_category_combo.addItems(["All Categories"] + snippet_categories)

        # Create snippet buttons
        for friendly_name, snippet_data in all_snippets.items():
            button = FunctionButton(friendly_name, snippet_data["code"], snippet_data["description"])
            # Styling will be applied by theme system
            button.clicked.connect(lambda checked, code=snippet_data["code"], desc=snippet_data["description"], name=friendly_name: 
                                 self.insert_code(code, desc, is_snippet=True))
            self.snippet_layout.addWidget(button)
            self.snippet_buttons.append((button, snippet_data["category"]))

        self.snippet_layout.addStretch()
        
    def analyze_cursor_context(self):
        """Analyze the context around the cursor to determine smart insertion behavior"""
        cursor = self.code_editor.textCursor()
        document = self.code_editor.document()

        # Get current line and surrounding context
        current_block = cursor.block()
        current_line = current_block.text().strip()
        line_number = current_block.blockNumber()

        # Look for function context by scanning backwards
        function_context = None
        indent_level = 0

        # Scan backwards to find if we're inside a function
        block = current_block
        while block.isValid():
            line = block.text().strip()
            if line.startswith('function ') and line.endswith(')'):
                function_context = line
                # Calculate indent level
                indent_level = len(block.text()) - len(block.text().lstrip())
                break
            elif line.startswith('end') and not line.startswith('--'):
                # We're outside any function
                break
            block = block.previous()

        return {
            'in_function': function_context is not None,
            'function_name': function_context,
            'current_line': current_line,
            'line_number': line_number,
            'indent_level': indent_level + 4 if function_context else 0
        }

    def extract_variables_from_code(self):
        """Extract declared variables from the current code for suggestions"""
        code = self.code_editor.toPlainText()
        import re

        # Find local variable declarations
        local_vars = re.findall(r'local\s+([a-zA-Z_][a-zA-Z0-9_]*)', code)
        # Find assignment variables
        assign_vars = re.findall(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=', code)

        return list(set(local_vars + assign_vars))

    def remove_local_keyword(self, code):
        """Remove 'local' keyword from variable declarations"""
        import re

        lines = code.split('\n')
        modified_lines = []

        for line in lines:
            # Remove 'local ' from the beginning of lines (preserving indentation)
            # This pattern matches: optional whitespace + 'local ' + rest of line
            modified_line = re.sub(r'^(\s*)local\s+', r'\1', line)
            modified_lines.append(modified_line)

        return '\n'.join(modified_lines)

    def add_global_search_parameter(self, code):
        """Add ', true' parameter to Find functions for global search"""
        import re

        lines = code.split('\n')
        modified_lines = []

        # List of find functions that support global search
        find_functions = [
            'FindBody', 'FindBodies', 'FindShape', 'FindShapes', 
            'FindLight', 'FindLights', 'FindVehicle', 'FindVehicles',
            'FindTrigger', 'FindTriggers'
        ]

        for line in lines:
            modified_line = line
            for func_name in find_functions:
                # Pattern to match: FunctionName("parameter") or FunctionName("param1", "param2")
                # But not if it already has ', true' or ', false'
                pattern = rf'({func_name}\s*\([^)]*?)(\))'
                match = re.search(pattern, modified_line)

                if match:
                    params_part = match.group(1)
                    closing_paren = match.group(2)

                    # Check if it already has a boolean parameter (true or false)
                    if not re.search(r',\s*(true|false)\s*$', params_part):
                        # Add ', true' before the closing parenthesis
                        if '(' in params_part and params_part.strip().endswith('('):
                            # No parameters yet: FunctionName()
                            modified_line = modified_line.replace(match.group(0), f'{params_part}"", true{closing_paren}')
                        elif params_part.strip().endswith(','):
                            # Already has comma: FunctionName("param",)
                            modified_line = modified_line.replace(match.group(0), f'{params_part} true{closing_paren}')
                        else:
                            # Has parameters: FunctionName("param")
                            modified_line = modified_line.replace(match.group(0), f'{params_part}, true{closing_paren}')

            modified_lines.append(modified_line)

        return '\n'.join(modified_lines)

    def change_theme(self, theme_name):
        """Change the application theme"""
        if theme_name in THEMES:
            self.current_theme = theme_name
            self.apply_theme(theme_name)
            # Save theme preference
            self.settings.setValue("theme", theme_name)
            self.documentation_text.setPlainText(f"Theme changed to: {theme_name}")

    def apply_theme(self, theme_name):
        """Apply theme styling to all components"""
        theme = THEMES[theme_name]

        # Update main window and panels
        self.setStyleSheet(build_app_stylesheet(theme_name))

        # Update documentation panel with theme colors
        self.documentation_text.setStyleSheet(build_documentation_stylesheet(theme_name))

        # Update function buttons
        self.update_function_button_styles(theme)

        # Update syntax highlighter
        if hasattr(self, 'highlighter'):
            self.highlighter.update_theme(theme["syntax"])

        # Update line number colors based on theme
        if hasattr(self, 'code_editor'):
            # Use panel background for line numbers, slightly darker for current line
            bg_color = theme.get("panel_background", "#2b2b2b")
            fg_color = theme.get("text", "#858585")
            # Create a slightly different shade for current line highlight
            current_line = theme.get("input_background", "#323232")
            self.code_editor.set_line_number_colors(bg_color, fg_color, current_line)

    def update_function_button_styles(self, theme):
        """Update all function and snippet button styles"""
        function_style = build_function_button_style(self.current_theme)

        snippet_style = build_snippet_button_style(self.current_theme)

        # Apply to function buttons
        if hasattr(self, 'function_buttons'):
            for button, category in self.function_buttons:
                button.setStyleSheet(function_style)

        # Apply to snippet buttons  
        if hasattr(self, 'snippet_buttons'):
            for button, category in self.snippet_buttons:
                button.setStyleSheet(snippet_style)

    def setup_keyboard_shortcuts(self):
        """Setup keyboard shortcuts for undo/redo"""
        # Undo shortcut (Ctrl+Z)
        undo_action = QAction(self)
        undo_action.setShortcut(QKeySequence.StandardKey.Undo)
        undo_action.triggered.connect(self.undo_action)
        self.addAction(undo_action)

        # Redo shortcut (Ctrl+Y)
        redo_action = QAction(self)
        redo_action.setShortcut(QKeySequence.StandardKey.Redo)
        redo_action.triggered.connect(self.redo_action)
        self.addAction(redo_action)

    def undo_action(self):
        """Perform undo operation"""
        if self.code_editor.document().isUndoAvailable():
            self.code_editor.undo()
            self.documentation_text.setPlainText("Undo performed. Continue editing or use Redo to reverse.")

    def redo_action(self):
        """Perform redo operation"""
        if self.code_editor.document().isRedoAvailable():
            self.code_editor.redo()
            self.documentation_text.setPlainText("Redo performed. Continue editing or use Undo to reverse.")

    def insert_code(self, code, description, is_snippet=False):
        """Smart code insertion based on context"""
        context = self.analyze_cursor_context()
        cursor = self.code_editor.textCursor()

        # Handle local keyword based on checkbox
        if not self.use_local_checkbox.isChecked():
            # Remove 'local' keyword if checkbox is unchecked
            code = self.remove_local_keyword(code)

        # Handle global search parameter for Find functions
        if self.use_global_search_checkbox.isChecked():
            # Add ', true' parameter to Find functions if checkbox is checked
            code = self.add_global_search_parameter(code)

        # Determine what to insert based on context
        if context['in_function'] and code.startswith('function '):
            # User is inside a function but trying to insert a function template
            # Ask if they want just the function body instead
            from PyQt6.QtWidgets import QMessageBox
            reply = QMessageBox.question(
                self, 'Smart Insertion',
                f"You're inside {context['function_name']}. Do you want to insert just the function body instead of the complete function?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )

            if reply == QMessageBox.StandardButton.Yes:
                # Extract just the function body
                lines = code.split('\n')
                body_lines = []
                for line in lines[1:-1]:  # Skip function declaration and end
                    if line.strip() and not line.strip().startswith('--'):
                        body_lines.append(line)

                if body_lines:
                    code = '\n'.join(body_lines)
                else:
                    code = '    -- Function body code here'

        # Apply proper indentation
        if context['in_function'] and not code.startswith('function '):
            # Add proper indentation for code inside functions
            indented_lines = []
            for line in code.split('\n'):
                if line.strip():  # Don't indent empty lines
                    indented_lines.append(' ' * context['indent_level'] + line.lstrip())
                else:
                    indented_lines.append('')
            code = '\n'.join(indented_lines)

        # Insert the code
        cursor.insertText('\n' + code + '\n')

        # Update documentation
        local_status = "with local" if self.use_local_checkbox.isChecked() else "without local"
        global_status = "with global search" if self.use_global_search_checkbox.isChecked() else "without global search"
        self.documentation_text.setPlainText(f"Function Documentation ({local_status}, {global_status}):\n\n{description}")

        # Show available variables if we're in a function
        if context['in_function']:
            variables = self.extract_variables_from_code()
            if variables:
                var_text = "\n\nAvailable variables: " + ", ".join(variables[:10])
                self.documentation_text.setPlainText(
                    self.documentation_text.toPlainText() + var_text
                )
        
    def filter_functions(self, search_text):
        search_text = search_text.lower()
        for button, category in self.function_buttons:
            should_show = search_text in button.text().lower()
            button.setVisible(should_show)

    def filter_by_category(self, category):
        for button, button_category in self.function_buttons:
            should_show = (category == "All Categories" or category == button_category)
            button.setVisible(should_show)

    def filter_snippets(self, search_text):
        search_text = search_text.lower()
        for button, category in self.snippet_buttons:
            should_show = search_text in button.text().lower()
            button.setVisible(should_show)

    def filter_snippets_by_category(self, category):
        for button, button_category in self.snippet_buttons:
            should_show = (category == "All Categories" or category == button_category)
            button.setVisible(should_show)

    def load_template(self, item):
        """Load a complete project template"""
        template_name = item.text()
        template_code = BEGINNER_TEMPLATES.get(template_name, "")

        if template_code:
            reply = QMessageBox.question(
                self, 'Load Template',
                f"This will replace all current code with the '{template_name}' template. Continue?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )

            if reply == QMessageBox.StandardButton.Yes:
                self.code_editor.setPlainText(template_code)
                self.documentation_text.setPlainText(f"Loaded template: {template_name}\n\nYou can now modify this code or add more functions to customize your mod!")

    def insert_pattern(self, item):
        """Insert a common code pattern"""
        pattern_name = item.text()
        pattern = COMMON_PATTERNS.get(pattern_name, {})

        if pattern:
            # Show explanation dialog
            msg = QMessageBox()
            msg.setWindowTitle("Code Pattern")
            msg.setText(f"Pattern: {pattern_name}")
            msg.setInformativeText(pattern["description"])
            msg.setDetailedText(f"Setup code:\n{pattern['setup_code']}\n\nUsage code:\n{pattern['usage_code']}\n\nExplanation:\n{pattern['explanation']}")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)

            if msg.exec() == QMessageBox.StandardButton.Ok:
                # Insert the pattern
                context = self.analyze_cursor_context()
                cursor = self.code_editor.textCursor()

                # Insert setup code at the top of the current function or file
                if context['in_function']:
                    # Insert at the beginning of the function
                    setup_text = f"\n    -- {pattern_name} setup\n    {pattern['setup_code']}\n"
                else:
                    # Insert at current position 
                    setup_text = f"\n-- {pattern_name} setup\n{pattern['setup_code']}\n"

                cursor.insertText(setup_text)

                # Insert usage code at current position
                usage_text = f"\n    -- {pattern_name} usage\n    {pattern['usage_code']}\n"
                cursor.insertText(usage_text)

                self.documentation_text.setPlainText(f"Pattern: {pattern_name}\n\n{pattern['description']}\n\n{pattern['explanation']}")

    def new_mod(self):
        """Start a new mod"""
        reply = QMessageBox.question(
            self, 'New Mod',
            "This will clear all current code. Are you sure?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.code_editor.setPlainText("-- Teardown Script\n-- Generated by Everybody's Code\n\n")
            # Clear undo/redo history for a fresh start
            self.code_editor.document().clearUndoRedoStacks()
            self.documentation_text.setPlainText("New mod started! Click on the Functions or Snippets tabs to add code.")

    def load_mod(self):
        """Load a .lua script from a Teardown mod"""
        from PyQt6.QtWidgets import QFileDialog
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Load Teardown Script",
            "",
            "Lua Files (*.lua);;All Files (*)"
        )

        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    code_content = f.read()

                # Ask if user wants to replace current code
                reply = QMessageBox.question(
                    self, 'Load Script',
                    f"Replace current code with script from:\n{filename}?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )

                if reply == QMessageBox.StandardButton.Yes:
                    self.code_editor.setPlainText(code_content)
                    self.code_editor.document().clearUndoRedoStacks()

                    # Extract filename for display
                    import os
                    short_name = os.path.basename(filename)
                    self.documentation_text.setPlainText(f"Loaded script: {short_name}\n\nYou can now edit this code and save it when ready.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to load file:\n{str(e)}")

    def save_code(self):
        """Save code to file"""
        from PyQt6.QtWidgets import QFileDialog
        filename, _ = QFileDialog.getSaveFileName(
            self, 
            "Save Teardown Script", 
            "my_mod.lua",
            "Lua Files (*.lua);;All Files (*)"
        )

        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.code_editor.toPlainText())
                QMessageBox.information(self, "Success", f"Code saved to {filename}")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to save file:\\n{str(e)}")

    def show_help(self):
        """Show beginner help dialog"""
        help_text = '''
        <h3>Everybody's Code - Help for Beginners</h3>

        <h4>How to use this tool:</h4>
        <ol>
        <li><b>Start with Templates:</b> Click the "Templates" tab and choose a project template to get started</li>
        <li><b>Add Functions:</b> Use the "Functions" tab to add complete function blocks</li>
        <li><b>Add Code:</b> Use the "Code Snippets" tab to add individual lines of code inside functions</li>
        <li><b>Smart Insertion:</b> The tool will automatically detect if you're inside a function and adjust what it inserts</li>
        </ol>

        <h4>Understanding the color coding:</h4>
        <ul>
        <li><span style="color: green;">Green buttons</span> = Complete function templates</li>
        <li><span style="color: blue;">Blue buttons</span> = Code snippets for inside functions</li>
        </ul>

        <h4>Local Variables Option:</h4>
        <ul>
        <li><b>Checked:</b> Variables will be declared with 'local' keyword (recommended for most cases)</li>
        <li><b>Unchecked:</b> Variables will be global (use when you need to access them from other functions)</li>
        </ul>

        <h4>Tips:</h4>
        <ul>
        <li>Start with a template, then add snippets inside the functions</li>
        <li>Use the search box to quickly find what you need</li>
        <li>Read the documentation panel when you click buttons</li>
        <li>Save your work often using the Save button</li>
        <li>Use 'local' variables most of the time - they're safer and faster</li>
        <li>Use Ctrl+Z to undo and Ctrl+Y to redo changes</li>
        <li>Choose a theme that's comfortable for your eyes from the Theme dropdown</li>
        </ul>

        <h4>Common beginner workflow:</h4>
        <ol>
        <li>Click "Templates" → "Basic Mod Structure"</li>
        <li>Click inside the server.tick() or client.tick() function</li>
        <li>Go to "Code Snippets" and add what you want your mod to do</li>
        <li>Save your code as a .lua file in your Teardown mod folder</li>
        </ol>
        '''

        msg = QMessageBox()
        msg.setWindowTitle("Help")
        msg.setTextFormat(Qt.TextFormat.RichText)
        msg.setText(help_text)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def run_validation(self):
        """Validate the current script and show issues"""
        diagnostics = validate_script(self.code_editor.toPlainText(), self.api_catalog)
        if not diagnostics:
            self.documentation_text.setPlainText("Validation passed: no issues found.")
            return

        # Separate diagnostics by level
        errors = [d for d in diagnostics if d['level'] == 'error']
        warnings = [d for d in diagnostics if d['level'] == 'warning']
        infos = [d for d in diagnostics if d['level'] == 'info']

        summary_lines = []

        # Show all errors first
        if errors:
            summary_lines.append(f"=== ERRORS ({len(errors)}) ===")
            for diag in errors:
                summary_lines.append(f"  Line {diag['line']}: {diag['message']}")
            summary_lines.append("")

        # Then all warnings
        if warnings:
            summary_lines.append(f"=== WARNINGS ({len(warnings)}) ===")
            for diag in warnings:
                summary_lines.append(f"  Line {diag['line']}: {diag['message']}")
            summary_lines.append("")

        # Then all info messages (custom functions, etc.)
        if infos:
            summary_lines.append(f"=== CUSTOM FUNCTIONS ({len(infos)}) ===")
            for diag in infos:
                summary_lines.append(f"  Line {diag['line']}: {diag['message']}")

        # Create header based on what was found
        if errors:
            header = "Validation found errors:\n\n"
        elif warnings:
            header = "Validation found warnings:\n\n"
        else:
            header = "Validation passed with notes:\n\n"

        self.documentation_text.setPlainText(header + "\n".join(summary_lines))

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    window = TeardownCodeEditor()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
