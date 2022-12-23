"""

"""


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *

import sys

import lexers


class Editor(QsciScintilla):
    def __init__(self, parent=None):
        super().__init__(parent)

        #
        # Declaring variables
        #

        # Caret foreground color
        self.__caret_foreground_color = QColor()
        self.__caret_foreground_color.setNamedColor("blue")

        # Caret line background color
        self.__caret_line_background_color = QColor()
        self.__caret_line_background_color.setRgb(0x00, 0x00, 0x00, 80)

        # Character color
        self.__char_color = self.color()

        # Indentation width
        self.__indentation_width = 4

        # Lexer None
        self.__lexer_none = lexers.LexerNone()

        # Lexer C++
        self.__lexer_c_plus_plus = lexers.LexerCPlusPlus()

        # Lexer CSS
        self.__lexer_cascading_style_sheet = lexers.LexerCSS()

        # Lexer HTML
        self.__lexer_html = lexers.LexerHTML()

        # Lexer Java
        self.__lexer_java = lexers.LexerJava()

        # Lexer JavaScript
        self.__lexer_js = lexers.LexerJavaScript()

        # Lexer Python
        self.__lexer_python = lexers.LexerPython3()

        # Lexer Python 2
        self.__lexer_python_2 = lexers.LexerPython2()

        # Margin background color
        self.__margin_background_color = QColor()
        self.__margin_background_color.setNamedColor("#999999")

        # Margin foreground color
        self.__margin_foreground_color = QColor()
        self.__margin_foreground_color.setNamedColor("#000000")

        # Font
        self.__font = QFont()
        self.__font.setFamily("Courier New")
        self.__font.setFixedPitch(True)
        self.__font.setPointSize(12)
        self.__font.setStyleHint(QFont.StyleHint.TypeWriter)

        #
        # Initializing settings
        #

        # A
        self.setAcceptDrops(True)

        # B
        self.setBackspaceUnindents(True)

        # C
        self.setCaretForegroundColor(self.__caret_foreground_color)
        self.setCaretLineBackgroundColor(self.__caret_line_background_color)
        self.setCaretLineVisible(True)

        # E
        self.setEolMode(QsciScintilla.EolUnix)

        # F
        self.setFolding(QsciScintilla.FoldStyle.BoxedTreeFoldStyle)
        self.setFont(self.__font)

        # L
        self.setLexer(self.__lexer_none)

        # M
        self.setMargins(1)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsFont(self.__font)

        # S
        self.SendScintilla(QsciScintilla.SCI_SETSCROLLWIDTHTRACKING, 1)
        self.SendScintilla(QsciScintilla.SCI_SETMULTIPLESELECTION, True)
        self.SendScintilla(QsciScintilla.SCI_SETMULTIPASTE, 1)
        self.SendScintilla(
            QsciScintilla.SCI_SETADDITIONALSELECTIONTYPING, True)

        # U
        self.setUtf8(True)

        # W
        self.setWrapMode(QsciScintilla.WrapMode.WrapWord)

        #
        # Connecting signals and slots
        #

        self.cursorPositionChanged.connect(self.___inner_slot_pos_changed)
        self.selectionChanged.connect(self.___inner_slot_pos_changed)

    def ___inner_slot_pos_changed(self):
        self.___inner_adjust_margins()

    def ___inner_adjust_margins(self):
        margin = len(self.text().split("\n"))
        self.setMarginWidth(0, QFontMetrics(self.__font).width(str(margin)) + 30)

    def zoom_in(self):
        self.zoomIn(1)

    def zoom_out(self):
        self.zoomOut(1)

    def set_lexer_none(self, is_checked=True):
        if is_checked:
            self.setLexer(self.__lexer_none)
            self.setAutoIndent(False)
            self.setIndentationGuides(False)
            self.setIndentationWidth(0)
            self.setIndentationsUseTabs(False)
        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

    def set_lexer_c_plus_plus(self, is_checked=True):
        if is_checked:
            self.setLexer(self.__lexer_c_plus_plus)
            self.setAutoIndent(True)
            self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
            self.setIndentationGuides(True)
            self.setIndentationWidth(self.__indentation_width)
        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

    def set_lexer_cascading_style_sheet(self, is_checked=True):
        if is_checked:
            self.setLexer(self.__lexer_cascading_style_sheet)
            self.setAutoIndent(True)
            self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
            self.setIndentationGuides(True)
            self.setIndentationWidth(self.__indentation_width)
        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

    def set_lexer_html(self, is_checked=True):
        if is_checked:
            self.setLexer(self.__lexer_html)
            self.setAutoIndent(True)
            self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
            self.setIndentationGuides(True)
            self.setIndentationWidth(self.__indentation_width)
        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

    def set_lexer_html_django(self, is_checked=True):
        self.__lexer_html.setDjangoTemplates(is_checked)

    def set_lexer_html_mako(self, is_checked=True):
        self.__lexer_html.setMakoTemplates(is_checked)

    def set_lexer_java(self, is_checked=True):
        if is_checked:
            self.setLexer(self.__lexer_java)
            self.setAutoIndent(True)
            self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
            self.setIndentationGuides(True)
            self.setIndentationWidth(self.__indentation_width)
        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

    def set_lexer_js(self, is_checked=True):
        if is_checked:
            self.setLexer(self.__lexer_js)
            self.setAutoIndent(True)
            self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
            self.setIndentationGuides(True)
            self.setIndentationWidth(self.__indentation_width)
        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

    def set_lexer_python(self, is_checked=True):
        if is_checked:
            self.setLexer(self.__lexer_python)
            self.setAutoIndent(True)
            self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
            self.setIndentationGuides(True)
            self.setIndentationWidth(self.__indentation_width)
            self.setIndentationsUseTabs(False)
        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

    def set_lexer_python_2(self, is_checked=True):
        if is_checked:
            self.setLexer(self.__lexer_python_2)
            self.setAutoIndent(True)
            self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
            self.setIndentationGuides(True)
            self.setIndentationWidth(self.__indentation_width)
            self.setIndentationsUseTabs(False)
        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = Editor()
    editor.show()
    sys.exit(app.exec())
