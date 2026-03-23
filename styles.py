# Styling helpers for Everybody's Code

from themes import THEMES


def build_app_stylesheet(theme_name):
    theme = THEMES[theme_name]
    return f"""
        QMainWindow {{
            background-color: {theme['background']};
            color: {theme['text']};
        }}
        QWidget {{
            background-color: {theme['background']};
            color: {theme['text']};
        }}
        QGroupBox {{
            font-weight: bold;
            border: 2px solid {theme['input_border']};
            border-radius: 4px;
            margin-top: 1ex;
            background-color: {theme['panel_background']};
        }}
        QGroupBox::title {{
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px 0 5px;
            background-color: {theme['panel_background']};
        }}
        QLineEdit {{
            background-color: {theme['input_background']};
            border: 1px solid {theme['input_border']};
            border-radius: 4px;
            padding: 4px;
            color: {theme['text']};
        }}
        QComboBox {{
            background-color: {theme['input_background']};
            border: 1px solid {theme['input_border']};
            border-radius: 4px;
            padding: 4px 24px 4px 8px;
            color: {theme['text']};
            min-width: 6em;
        }}
        QComboBox:hover {{
            border: 1px solid {theme['function_button_hover']};
        }}
        QComboBox:focus {{
            border: 1px solid {theme['snippet_button']};
            outline: none;
        }}
        QComboBox:on {{
            border: 1px solid {theme['snippet_button']};
        }}
        QComboBox::drop-down {{
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 20px;
            border: none;
            background-color: transparent;
        }}
        QComboBox::down-arrow {{
            border-left: 3px solid transparent;
            border-right: 3px solid transparent;
            border-top: 5px solid {theme['text']};
            width: 0px;
            height: 0px;
        }}
        QComboBox QAbstractItemView {{
            border: 1px solid {theme['input_border']};
            background-color: {theme['input_background']};
            color: {theme['text']};
            selection-background-color: {theme['snippet_button']};
            selection-color: white;
            outline: none;
        }}
        QComboBox QAbstractItemView::item {{
            padding: 4px;
            border: none;
            min-height: 20px;
        }}
        QComboBox QAbstractItemView::item:hover {{
            background-color: {theme['toolbar_button_hover']};
        }}
        QComboBox QAbstractItemView::item:selected {{
            background-color: {theme['snippet_button']};
            color: white;
        }}
        QTextEdit {{
            background-color: {theme['input_background']};
            border: 1px solid {theme['input_border']};
            border-radius: 4px;
            color: {theme['text']};
        }}
        QScrollArea {{
            background-color: {theme['panel_background']};
            border: none;
        }}
        QListWidget {{
            background-color: {theme['input_background']};
            border: 1px solid {theme['input_border']};
            border-radius: 4px;
            color: {theme['text']};
        }}
        QListWidget::item {{
            padding: 4px;
            border-bottom: 1px solid {theme['input_border']};
        }}
        QListWidget::item:hover {{
            background-color: {theme['toolbar_button_hover']};
        }}
        QListWidget::item:selected {{
            background-color: {theme['snippet_button']};
            color: white;
        }}
        QCheckBox {{
            color: {theme['text']};
        }}
        QLabel {{
            color: {theme['text']};
        }}
    """


def build_documentation_stylesheet(theme_name):
    theme = THEMES[theme_name]
    return f"""
        padding: 10px;
        background-color: {theme['doc_background']};
        color: {theme['doc_text']};
        border-radius: 4px;
    """


def build_function_button_style(theme_name):
    theme = THEMES[theme_name]
    return f"""
        QPushButton {{
            background-color: {theme['function_button']};
            color: white;
            border: none;
            padding: 8px;
            text-align: left;
            border-radius: 4px;
            font-size: 12px;
        }}
        QPushButton:hover {{
            background-color: {theme['function_button_hover']};
        }}
        QPushButton:pressed {{
            background-color: {theme['function_button_pressed']};
        }}
    """


def build_snippet_button_style(theme_name):
    theme = THEMES[theme_name]
    return f"""
        QPushButton {{
            background-color: {theme['snippet_button']};
            color: white;
            border: none;
            padding: 8px;
            text-align: left;
            border-radius: 4px;
            font-size: 12px;
        }}
        QPushButton:hover {{
            background-color: {theme['snippet_button_hover']};
        }}
        QPushButton:pressed {{
            background-color: {theme['snippet_button_pressed']};
        }}
    """
