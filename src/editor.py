"""
This is a file of a project of the Bright Software Foundation.

======================= Project and File Information ===========================

Project Name:                           Txter

Project Name Identifier:                brTxter

Project Version (for This File):        0.5.0

Project Status (for This File):         beta testing...

Project Start Date:                     Dec 23, 2022 UTC

Project Start Version:                  0.2.0 [alpha]

Project End Date:                       --None--

Project End Version:                    --None--

Project Activate State:                 Remains Activate

Project Type:                           Freeware

Project Copyright:                      Copyleft

Project License:                        Bright Software License

Project Developer:                      Bright Software Foundation Development Team

Project Creator:                        Bright Software Foundation

Project Used Programming Language(s):   Python 3

Project Download Mirror:                https://sourceforge.net/projects/brtxter

Project Source Hosting Mirror:          https://github.com/brsoftware/txter


File Name:                              editor.py

File Type:                              Source File

File Belongs To:                        Txter / brTxter

================================================================================

Bright Software Foundation 2022 - 2023
"""


#
# Importing packages and modules...
#


# PyQt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *

# Python builtins
import sys

# Modules
import lexers


class Editor(QsciScintilla):
    """
    The editor class.

    Enables users edit it.
    """

    def __init__(self, parent=None):
        """
        Initializing method for the editor.

        :param parent: QWidget | None
        """

        # Super the class to the parent.
        super().__init__(parent)

        # Defining variables

        # Caret foreground color
        self.__caret_foreground_color = QColor()
        self.__caret_foreground_color.setNamedColor("blue")

        # Caret line background color
        self.__caret_line_background_color = QColor()
        self.__caret_line_background_color.setRgb(0x00, 0x00, 0x00, 80)

        # Character color
        self.__char_color = self.color()

        # Font
        self.__font = QFont()
        self.__font.setFamily("Courier New")
        self.__font.setFixedPitch(True)
        self.__font.setPointSize(12)
        self.__font.setStyleHint(QFont.StyleHint.TypeWriter)

        # Indentation width
        self.__indentation_width = 4

        # Lexer None
        self.__lexer_none = lexers.LexerNone(self.__font)

        # Lexer C++
        self.__lexer_c_plus_plus = lexers.LexerCPlusPlus(self.__font)

        # Lexer CSS
        self.__lexer_cascading_style_sheet = lexers.LexerCSS(self.__font)

        # Lexer HTML
        self.__lexer_html = lexers.LexerHTML(self.__font)

        # Lexer Java
        self.__lexer_java = lexers.LexerJava(self.__font)

        # Lexer JavaScript
        self.__lexer_js = lexers.LexerJavaScript(self.__font)

        # Lexer Python
        self.__lexer_python = lexers.LexerPython3(self.__font)

        # Lexer Python 2
        self.__lexer_python_2 = lexers.LexerPython2(self.__font)

        # Lexer _vars
        self.__lexer_html_var = "none"
        self.__lexer_var = "none"

        # Margin background color
        self.__margin_background_color = QColor()
        self.__margin_background_color.setNamedColor("#999999")

        # Margin foreground color
        self.__margin_foreground_color = QColor()
        self.__margin_foreground_color.setNamedColor("#000000")

        # Initializing settings

        # A
        self.setAcceptDrops(True)
        self.setAutoIndent(True)

        # B
        self.setBackspaceUnindents(True)
        self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)

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

        # Connecting signals and slots

        self.cursorPositionChanged.connect(self.___inner_slot_pos_changed)
        self.selectionChanged.connect(self.___inner_slot_pos_changed)

    def ___inner_slot_pos_changed(self):
        """
        This inner slot handles when the position changed.

        Private method.
        Inner slot.

        :return: None
        """

        # Adjust the margins.
        self.___inner_adjust_margins()

    def ___inner_adjust_margins(self):
        """
        Adjust the margins when the document changed.

        :return: None
        """

        # -UNUSED- Handles nothing.

        margin = len(self.text().split("\n"))
        self.setMarginWidth(0, QFontMetrics(self.__font).width(str(margin)) + 30)

        # pass

    def zoom_in(self):
        """
        Zooms in the editor.

        :return: None
        """

        # Zooms in 1 point.
        self.zoomIn(1)

    def zoom_out(self):
        """
        Zooms out the editor.

        :return: None
        """

        # Zooms out 1 point.
        self.zoomOut(1)

    def set_lexer_none(self, is_checked=True):
        """
        LexerNone

        :param is_checked: True always
        :return: None
        """

        if is_checked:
            # QAction.checked

            self.setLexer(self.__lexer_none)
            self.setAutoIndent(True)
            self.setIndentationGuides(False)
            self.setIndentationWidth(0)
            self.setIndentationsUseTabs(False)

        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

        self.__lexer_var = "none"

    def set_lexer_c_plus_plus(self, is_checked=True):
        """
        LexerCPlusPlus

        :param is_checked: True always
        :return: None
        """

        if is_checked:
            # QAction.checked

            self.setLexer(self.__lexer_c_plus_plus)
            self.setAutoIndent(True)
            self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
            self.setIndentationGuides(True)
            self.setIndentationWidth(self.__indentation_width)

        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

        self.__lexer_var = "cpp"

    def set_lexer_cascading_style_sheet(self, is_checked=True):
        """
        LexerCSS

        :param is_checked: True always
        :return: None
        """

        if is_checked:
            # QAction.checked

            self.setLexer(self.__lexer_cascading_style_sheet)
            self.setAutoIndent(True)
            self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
            self.setIndentationGuides(True)
            self.setIndentationWidth(self.__indentation_width)

        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

        self.__lexer_var = "css"

    def set_lexer_html(self, is_checked=True):
        """
        LexerHTML

        :param is_checked: True always
        :return: None
        """

        if is_checked:
            # QAction.checked

            self.setLexer(self.__lexer_html)
            self.setAutoIndent(True)
            self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
            self.setIndentationGuides(True)
            self.setIndentationWidth(self.__indentation_width)

        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

        self.__lexer_var = "html"

    def set_lexer_html_django(self, is_checked=True):
        """
        LexerHTML.setDjangoTemplates

        :param is_checked: True always
        :return: None
        """

        self.__lexer_html.setDjangoTemplates(is_checked)

        self.__lexer_html_var = ("django" if is_checked else "none")

    def set_lexer_html_mako(self, is_checked=True):
        """
        LexerHTML.setMakoTemplates

        :param is_checked: True always
        :return: None
        """

        self.__lexer_html.setMakoTemplates(is_checked)

        self.__lexer_html_var = ("mako" if is_checked else "none")

    def set_lexer_java(self, is_checked=True):
        """
        LexerJava

        :param is_checked: True always
        :return: None
        """

        if is_checked:
            # QAction.checked

            self.setLexer(self.__lexer_java)
            self.setAutoIndent(True)
            self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
            self.setIndentationGuides(True)
            self.setIndentationWidth(self.__indentation_width)

        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

        self.__lexer_var = "java"

    def set_lexer_js(self, is_checked=True):
        """
        LexerJavaScript

        :param is_checked: True always
        :return: none
        """

        if is_checked:
            # QAction.checked

            self.setLexer(self.__lexer_js)
            self.setAutoIndent(True)
            self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
            self.setIndentationGuides(True)
            self.setIndentationWidth(self.__indentation_width)

        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

        self.__lexer_var = "js"

    def set_lexer_python(self, is_checked=True):
        """
        LexerPython3

        :param is_checked: True always
        :return: None
        """

        if is_checked:
            # QAction.checked

            self.setLexer(self.__lexer_python)
            self.setAutoIndent(True)
            self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
            self.setIndentationGuides(True)
            self.setIndentationWidth(self.__indentation_width)

            # !important
            self.setIndentationsUseTabs(False)

        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

        self.__lexer_var = "py"

    def set_lexer_python_2(self, is_checked=True):
        """
        LexerPython2

        :param is_checked: True always
        :return: None
        """

        if is_checked:
            # QAction.checked

            self.setLexer(self.__lexer_python_2)
            self.setAutoIndent(True)
            self.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
            self.setIndentationGuides(True)
            self.setIndentationWidth(self.__indentation_width)

            # !important
            self.setIndentationsUseTabs(False)

        self.setFont(self.__font)
        self.setMarginsFont(self.__font)
        self.setMarginsBackgroundColor(self.__margin_background_color)
        self.setMarginsForegroundColor(self.__margin_foreground_color)

        self.__lexer_var = "py2"

    def is_lexer_none(self):
        """
        Is LexerNone in use?

        :return: True if yes and False if not.
        """

        return self.__lexer_var == "none"

    def is_lexer_c_plus_plus(self):
        """
        Is LexerCPlusPlus in use?

        :return: True if yes and False if not.
        """

        return self.__lexer_var == "cpp"

    def is_lexer_css(self):
        """
        Is LexerCSS in use?

        :return: True if yes and False if not.
        """

        return self.__lexer_var == "css"

    def is_lexer_html(self):
        """
        Is LexerHTML in use?

        :return: True if yes and False if not.
        """

        return self.__lexer_var == "html"

    def is_lexer_html_django(self):
        """
        Is LexerHTML.djangoTemplates in use?

        :return: True if yes and False if not.
        """

        return self.__lexer_html_var == "django"

    def is_lexer_html_mako(self):
        """
        Is LexerHTML.makoTemplates in use?

        :return: True if yes and False if not.
        """

        return self.__lexer_html_var == "mako"

    def is_lexer_html_none(self):
        """
        Is both LexerHTML Templates not in use?

        :return: True if yes and False if not.
        """

        return self.__lexer_html_var == "none"

    def is_lexer_java(self):
        """
        Is LexerJava in use?

        :return: True if yes and False if not.
        """

        return self.__lexer_var == "java"

    def is_lexer_js(self):
        """
        Is LexerJavaScript in use?

        :return: True if yes and False if not.
        """

        return self.__lexer_var == "js"

    def is_lexer_py2(self):
        """
        Is LexerPython2 in use?

        :return: True if yes and False if not.
        """

        return self.__lexer_var == "py2"

    def is_lexer_py(self):
        """
        Is LexerPython in use?

        :return: True if yes and False if not.
        """

        return self.__lexer_var == "py"


if __name__ == "__main__":
    # Testing use.

    # Constructing the QApplication.
    app = QApplication(sys.argv)

    # Constructing the editor.
    editor = Editor()

    # Show the editor.
    editor.show()

    # Execute the QApplication and exit-after-close.
    sys.exit(app.exec())
