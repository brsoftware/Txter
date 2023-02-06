"""
This is a file of a project of the Bright Software Foundation.

======================= Project and File Information ===========================

Project Name:                           Txter

Project Name Identifier:                brTxter

Project Version (for This File):        0.8.0

Project Status (for This File):         Release candidates 1...

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


File Name:                              main.py

File Type:                              Source File

File Belongs To:                        Txter / brTxter

================================================================================

Bright Software Foundation 2022 - 2023
"""

#
# Importing packages and modules...
#


# PyQt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qsci import QsciPrinter
from PyQt5.QtPrintSupport import *

# Python builtins
import os
import sys
import traceback

# Modules
import dialogs
import editor
import tabs

#
# Defining the class(es)...
#


class MainWindow(QMainWindow):
    """
    This is the main class of Txter.

    Inherits QMainWindow class.
    """

    def __init__(self, parent=None):
        """
        This is the initializing method of the class.

        :param parent: parent of the widget.
        """

        # Super the class to the parent
        super().__init__(parent)

        # Supported file extensions for opening files
        self.__open_support = [
            "All files (*; *.*)",
            "Text files (*.txt)",
            "C++ source (*.cpp)",
            "C++ new-define source (*.cxx)",
            "C++ sources (*.cpp; *.cxx)",
            "C++ C-type header (*.h)",
            "C++ header (*.hpp)",
            "C++ new-define header (*.hxx)",
            "C++ header (*.h; *.hpp; *hxx)",
            "C++ files (*.cpp; *.cxx; *.h; *.hxx; *.hpp; *.hxx)",
            "CSS file (*.css)",
            "HTML source (*.html)",
            "HTML multimedia source (*.mhtml)",
            "HTML single package source (*.shtml)",
            "HTML files (*.html; *.mhtml; *.shtml)",
            "Java code (*.java)",
            "Java class archive (*.jar)",
            "Java files (*.java; *.jar)",
            "JavaScript file (*.js)",
            "Markdown file (*.md)",
            "Markdown file (*.markdown)",
            "Markdown files (*.md; *.markdown)",
            "PyInstaller files (*.spec)",
            "Python script (*.py)",
            "Python console-less scripts (*.pyw)",
            "Python scripts (*.py; *.pyw)",
            "Python cache file (*.pyc)",
            "Python informative documentations (*.pyi)",
            "Python bytecode optimized file (*.pyo)",
            "Python files (*.py; *.pyw; *.pyc; *.pyi; *.pyo; *.spec)"
        ]

        # Supported saving options for saving files
        self.__save_support = [
            "All files (*.*)",
            "Text files (*.txt)",
            "C++ source (*.cpp)",
            "C++ new-define source (*.cxx)",
            "C++ C-type header (*.h)",
            "C++ header (*.hpp)",
            "C++ new-define header (*.hxx)",
            "CSS file (*.css)",
            "HTML source (*.html)",
            "HTML multimedia source (*.mhtml)",
            "HTML single package source (*.shtml)",
            "Java code (*.java)",
            "Java class archive (*.jar)",
            "JavaScript file (*.js)",
            "Markdown file (*.md)",
            "Markdown file (*.markdown)",
            "PyInstaller files (*.spec)",
            "Python script (*.py)",
            "Python console-less scripts (*.pyw)",
            "Python cache file (*.pyc)",
            "Python informative documentations (*.pyi)",
            "Python bytecode optimized file (*.pyo)",
        ]

        # Original of the documents...
        self.original = [""]

        # Path of the current document...
        self.path = ""

        # Languages supported (lexers).
        self.lang = {
            "C++": "Language: C++ (C-Plus-Plus)",
            "CSS": "Language: CSS (Cascading StyleSheet)",
            "HTML": "Language: HTML (HyperText Markup Language)",
            "Java": "Language: Java",
            "JS": "Language: JS (JavaScript)",
            "Markdown": "Language: MD (MarkDown)",
            "Python": "Language: Python (Python 3)",
            "py2": "Language: Python (Python 2)",
            "No": "Language: None"
        }

        # Images there...
        self.__icon_self = QIcon("icon.ico")
        self.__image_c_plus_plus = QIcon("icons/file-c-plus-plus.png")
        self.__image_css = QIcon("icons/file-css.png")
        self.__image_html = QIcon("icons/file-html.png")
        self.__image_java = QIcon("icons/file-java.png")
        self.__image_js = QIcon("icons/file-js.png")
        self.__image_md = QIcon("icons/file-markdown.png")
        self.__image_normal = QIcon("icons/file-normal.png")
        self.__image_python = QIcon("icons/file-python.png")
        self.__image_text = QIcon("icons/file-text.png")

        # Images for macOS
        if sys.platform == "darwin":
            self.__image_normal = QFileIconProvider().icon(QFileIconProvider.File)
            self.__image_c_plus_plus = QIcon("images/file-c-plus-plus.png")
            self.__image_css = QIcon("images/file-css.png")
            self.__image_html = QIcon("images/file-html.png")
            self.__image_java = QIcon("images/file-java.png")
            self.__image_js = QIcon("images/file-js.png")
            self.__image_md = QIcon("images/file-markdown.png")
            self.__image_python = QIcon("images/file-python.png")
            self.__image_text = QIcon("images/file-text.png")

        # Initializing...
        self.__init_editor()
        self.__init_editor_tab()
        self.__init_bar_menu()
        self.__init_bar_status()
        self.__init_signals()
        self.__init_window()

    def __init_editor(self):
        """
        Initializing the editor.

        :return:
        """

        self.__ed = editor.Editor(self)
        self.__ed.set_lexer_none()
        # self.setCentralWidget(self.__ed)

    def __init_editor_tab(self):
        """
        Initializing the tab widget.

        :return: None
        """

        self.__tab_widget = tabs.TabWidget()
        self.__tab_widget.addTab(self.__ed, self.__image_normal, "Untitled")
        self.setCentralWidget(self.__tab_widget)

    def __init_bar_menu(self):
        """
        Initializing the menu bar.

        :return: None
        """

        # Constructing the menu bar.
        self.__menu_bar = QMenuBar()
        self.setMenuBar(self.__menu_bar)

        # Constructing the file menu.
        self.__file_menu = QMenu()
        self.__file_menu.setTitle("&File")
        self.__menu_bar.addMenu(self.__file_menu)

        # Constructing the new action.
        # It creates a new document.
        self.__action_file_new = QAction()
        self.__action_file_new.setText("&New")
        self.__action_file_new.setShortcut(QKeySequence.StandardKey.New)
        self.__action_file_new.setToolTip("New")
        self.__action_file_new.setStatusTip("New: creates a new document.")
        self.__file_menu.addAction(self.__action_file_new)

        # Constructing the open action.
        # It opens an existing document.
        self.__action_file_open = QAction()
        self.__action_file_open.setText("&Open...")
        self.__action_file_open.setShortcut(QKeySequence.StandardKey.Open)
        self.__action_file_open.setToolTip("Open")
        self.__action_file_open.setStatusTip("Open: opens an existing document.")
        self.__file_menu.addAction(self.__action_file_open)

        # Constructing the close action.
        # It closes an existing document
        self.__action_file_close = QAction()
        self.__action_file_close.setText("&Close")
        self.__action_file_close.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_W)
        self.__action_file_close.setToolTip("close")
        self.__action_file_close.setStatusTip("Close: closes an existing document.")
        self.__file_menu.addAction(self.__action_file_close)

        # Adding a separator...
        self.__file_menu.addSeparator()

        # Constructing the save action.
        # It saves an existing document.
        self.__action_file_save = QAction()
        self.__action_file_save.setText("&Save...")
        self.__action_file_save.setShortcut(QKeySequence.StandardKey.Save)
        self.__action_file_save.setToolTip("save")
        self.__action_file_save.setStatusTip("Save: saves an existing document.")
        self.__file_menu.addAction(self.__action_file_save)

        # Constructing the save as action.
        # It saves an existing document using a new path.
        self.__action_file_save_as = QAction()
        self.__action_file_save_as.setText("Save &as...")
        self.__action_file_save_as.setShortcut(Qt.Modifier.CTRL | Qt.Modifier.SHIFT | Qt.Key.Key_S)
        self.__action_file_save_as.setToolTip("Save as")
        self.__action_file_save_as.setStatusTip("Save as: saves an existing document using a new path.")
        self.__file_menu.addAction(self.__action_file_save_as)

        # Adding a separator...
        self.__file_menu.addSeparator()

        # Constructing the print action.
        # It prints the current document.
        self.__action_file_print = QAction()
        self.__action_file_print.setText("&Print")
        self.__action_file_print.setShortcut(QKeySequence.StandardKey.Print)
        self.__action_file_print.setToolTip("Print")
        self.__action_file_print.setStatusTip("Print: prints the current document.")
        self.__file_menu.addAction(self.__action_file_print)

        # Constructing the edit menu.
        self.__edit_menu = QMenu()
        self.__edit_menu.setTitle("&Edit")
        self.__menu_bar.addMenu(self.__edit_menu)

        # Constructing the undo action.
        # It undoes the last action you did.
        self.__action_edit_undo = QAction()
        self.__action_edit_undo.setText("&Undo")
        self.__action_edit_undo.setShortcut(QKeySequence.StandardKey.Undo)
        self.__action_edit_undo.setToolTip("Undo")
        self.__action_edit_undo.setStatusTip("Undo: undoes the last action you did.")
        self.__action_edit_undo.setEnabled(False)
        self.__edit_menu.addAction(self.__action_edit_undo)

        # Constructing the redo action.
        # It redoes the last action you did.
        self.__action_edit_redo = QAction()
        self.__action_edit_redo.setText("&Redo")
        self.__action_edit_redo.setShortcut(QKeySequence.StandardKey.Redo)
        self.__action_edit_redo.setToolTip("Redo")
        self.__action_edit_redo.setStatusTip("Redo: redoes the last action you did.")
        self.__action_edit_redo.setEnabled(False)
        self.__edit_menu.addAction(self.__action_edit_redo)

        # Adding a separator...
        self.__edit_menu.addSeparator()

        # Constructing the cut action.
        # It cuts the selected text.
        self.__action_edit_cut = QAction()
        self.__action_edit_cut.setText("&Cut")
        self.__action_edit_cut.setShortcut(QKeySequence.StandardKey.Cut)
        self.__action_edit_cut.setToolTip("Cut")
        self.__action_edit_cut.setStatusTip("Cut: cuts the selected text.")
        self.__action_edit_cut.setEnabled(False)
        self.__edit_menu.addAction(self.__action_edit_cut)

        # Constructing the copy action.
        # It copies the selected text.
        self.__action_edit_copy = QAction()
        self.__action_edit_copy.setText("C&opy")
        self.__action_edit_copy.setShortcut(QKeySequence.StandardKey.Copy)
        self.__action_edit_copy.setToolTip("Copy")
        self.__action_edit_copy.setStatusTip("Copy: copies the selected text.")
        self.__action_edit_copy.setEnabled(False)
        self.__edit_menu.addAction(self.__action_edit_copy)

        # Constructing the paste action.
        # It pastes the word in the system clipboard.
        self.__action_edit_paste = QAction()
        self.__action_edit_paste.setText("&Paste")
        self.__action_edit_paste.setShortcut(QKeySequence.StandardKey.Paste)
        self.__action_edit_paste.setToolTip("Paste")
        self.__action_edit_paste.setStatusTip("Paste: pastes the word in the system clipboard.")
        self.__edit_menu.addAction(self.__action_edit_paste)

        # Adding a separator...
        self.__edit_menu.addSeparator()

        # Constructing the find action.
        # It finds the occurrence word(s)
        self.__action_edit_find = QAction()
        self.__action_edit_find.setText("&Find")
        self.__action_edit_find.setShortcut(QKeySequence.StandardKey.Find)
        self.__action_edit_find.setToolTip("Find")
        self.__action_edit_find.setStatusTip("Find: finds the occurrence word(s).")
        self.__edit_menu.addAction(self.__action_edit_find)

        # Constructing the replacement action.
        # It replaces the occurrence word with another one.
        self.__action_edit_replace = QAction()
        self.__action_edit_replace.setText("&Replace")
        self.__action_edit_replace.setShortcut((Qt.Modifier.CTRL | Qt.Modifier.SHIFT | Qt.Key.Key_H)
                                               if sys.platform == "darwin" else QKeySequence.StandardKey.Replace)
        self.__action_edit_replace.setToolTip("Replace")
        self.__action_edit_replace.setStatusTip("Replace: replaces the occurrence word with another one.")
        self.__edit_menu.addAction(self.__action_edit_replace)

        # Constructing the goto action.
        # It goes to the specified line number.
        self.__action_edit_goto = QAction()
        self.__action_edit_goto.setText("&Goto")
        self.__action_edit_goto.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_G)
        self.__action_edit_goto.setToolTip("Goto")
        self.__action_edit_goto.setStatusTip("Goto: goes to the specified line number.")
        self.__edit_menu.addAction(self.__action_edit_goto)

        # Adding a separator...
        self.__edit_menu.addSeparator()

        # Constructing the select all action.
        # It selects all the text of the document.
        self.__action_edit_select_all = QAction()
        self.__action_edit_select_all.setText("Select &all")
        self.__action_edit_select_all.setShortcut(QKeySequence.StandardKey.SelectAll)
        self.__action_edit_select_all.setToolTip("Select all")
        self.__action_edit_select_all.setStatusTip("Select all: selects all the text of the document.")
        self.__edit_menu.addAction(self.__action_edit_select_all)

        # Constructing the view menu.
        self.__view_menu = QMenu()
        self.__view_menu.setTitle("&View")
        self.__menu_bar.addMenu(self.__view_menu)

        # Constructing the zoom in action.
        # It zooms the text in the document in.
        self.__action_view_zoom_in = QAction()
        self.__action_view_zoom_in.setText("Zoom &in")
        self.__action_view_zoom_in.setShortcut(QKeySequence.StandardKey.ZoomIn)
        self.__action_view_zoom_in.setToolTip("Zoom in")
        self.__action_view_zoom_in.setStatusTip("Zoom in: zooms the text in the document in.")
        self.__view_menu.addAction(self.__action_view_zoom_in)

        # Constructing the zoom out action.
        # It zooms the text in the document out. 
        self.__action_view_zoom_out = QAction()
        self.__action_view_zoom_out.setText("Zoom &out")
        self.__action_view_zoom_out.setShortcut(QKeySequence.StandardKey.ZoomOut)
        self.__action_view_zoom_out.setToolTip("Zoom out")
        self.__action_view_zoom_out.setStatusTip("Zoom out: zooms the text in the document out.")
        self.__view_menu.addAction(self.__action_view_zoom_out)

        # Adding a separator...
        self.__view_menu.addSeparator()

        # Constructing the tab menu, inside the view menu
        self.__view_tab_menu = QMenu()
        self.__view_tab_menu.setTitle("&Switching tabs")
        self.__view_menu.addMenu(self.__view_tab_menu)

        # Constructing the switch to tab 1 action.
        # It switches the current viewport to tab 1.
        self.__action_view_switch_tab_1 = QAction()
        self.__action_view_switch_tab_1.setText("Switch to tab &1")
        self.__action_view_switch_tab_1.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_1)
        self.__action_view_switch_tab_1.setToolTip("Switch to tab 1")
        self.__action_view_switch_tab_1.setStatusTip("Switch to tab 1: switches the current viewport to tab 1.")
        self.__view_tab_menu.addAction(self.__action_view_switch_tab_1)

        # Constructing the switch to tab 2 action.
        # It switches the current viewport to tab 2.
        self.__action_view_switch_tab_2 = QAction()
        self.__action_view_switch_tab_2.setText("Switch to tab &2")
        self.__action_view_switch_tab_2.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_2)
        self.__action_view_switch_tab_2.setToolTip("Switch to tab 2")
        self.__action_view_switch_tab_2.setStatusTip("Switch to tab 2: switches the current viewport to tab 2.")
        self.__view_tab_menu.addAction(self.__action_view_switch_tab_2)

        # Constructing the switch to tab 3 action.
        # It switches the current viewport to tab 3.
        self.__action_view_switch_tab_3 = QAction()
        self.__action_view_switch_tab_3.setText("Switch to tab &3")
        self.__action_view_switch_tab_3.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_3)
        self.__action_view_switch_tab_3.setToolTip("Switch to tab 3")
        self.__action_view_switch_tab_3.setStatusTip("Switch to tab 3: switches the current viewport to tab 3.")
        self.__view_tab_menu.addAction(self.__action_view_switch_tab_3)

        # Constructing the switch to tab 4 action.
        # It switches the current viewport to tab 4.
        self.__action_view_switch_tab_4 = QAction()
        self.__action_view_switch_tab_4.setText("Switch to tab &4")
        self.__action_view_switch_tab_4.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_4)
        self.__action_view_switch_tab_4.setToolTip("Switch to tab 4")
        self.__action_view_switch_tab_4.setStatusTip("Switch to tab 4: switches the current viewport to tab 4.")
        self.__view_tab_menu.addAction(self.__action_view_switch_tab_4)

        # Constructing the switch to tab 5 action.
        # It switches the current viewport to tab 5.
        self.__action_view_switch_tab_5 = QAction()
        self.__action_view_switch_tab_5.setText("Switch to tab &5")
        self.__action_view_switch_tab_5.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_5)
        self.__action_view_switch_tab_5.setToolTip("Switch to tab 5")
        self.__action_view_switch_tab_5.setStatusTip("Switch to tab 5: switches the current viewport to tab 5.")
        self.__view_tab_menu.addAction(self.__action_view_switch_tab_5)

        # Constructing the switch to tab 6 action.
        # It switches the current viewport to tab 6.
        self.__action_view_switch_tab_6 = QAction()
        self.__action_view_switch_tab_6.setText("Switch to tab &6")
        self.__action_view_switch_tab_6.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_6)
        self.__action_view_switch_tab_6.setToolTip("Switch to tab 6")
        self.__action_view_switch_tab_6.setStatusTip("Switch to tab 6: switches the current viewport to tab 6.")
        self.__view_tab_menu.addAction(self.__action_view_switch_tab_6)

        # Constructing the switch to tab 7 action.
        # It switches the current viewport to tab 7.
        self.__action_view_switch_tab_7 = QAction()
        self.__action_view_switch_tab_7.setText("Switch to tab &7")
        self.__action_view_switch_tab_7.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_7)
        self.__action_view_switch_tab_7.setToolTip("Switch to tab 7")
        self.__action_view_switch_tab_7.setStatusTip("Switch to tab 7: switches the current viewport to tab 7.")
        self.__view_tab_menu.addAction(self.__action_view_switch_tab_7)

        # Constructing the switch to tab 8 action.
        # It switches the current viewport to tab 8.
        self.__action_view_switch_tab_8 = QAction()
        self.__action_view_switch_tab_8.setText("Switch to tab &8")
        self.__action_view_switch_tab_8.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_8)
        self.__action_view_switch_tab_8.setToolTip("Switch to tab 8")
        self.__action_view_switch_tab_8.setStatusTip("Switch to tab 8: switches the current viewport to tab 8.")
        self.__view_tab_menu.addAction(self.__action_view_switch_tab_8)

        # Constructing the switch to tab 9 action.
        # It switches the current viewport to tab 9.
        self.__action_view_switch_tab_9 = QAction()
        self.__action_view_switch_tab_9.setText("Switch to tab &9")
        self.__action_view_switch_tab_9.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_9)
        self.__action_view_switch_tab_9.setToolTip("Switch to tab 9")
        self.__action_view_switch_tab_9.setStatusTip("Switch to tab 9: switches the current viewport to tab 9.")
        self.__view_tab_menu.addAction(self.__action_view_switch_tab_9)

        # Constructing the switch to tab 10 action.
        # It switches the current viewport to tab 10.
        self.__action_view_switch_tab_10 = QAction()
        self.__action_view_switch_tab_10.setText("Switch to tab 1&0")
        self.__action_view_switch_tab_10.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_0)
        self.__action_view_switch_tab_10.setToolTip("Switch to tab 10")
        self.__action_view_switch_tab_10.setStatusTip("Switch to tab 10: switches the current viewport to tab 10.")
        self.__view_tab_menu.addAction(self.__action_view_switch_tab_10)

        # Adding a separator...
        self.__view_tab_menu.addSeparator()

        # Constructing the switch to tab previous action.
        # It switches the current viewport to tab previous.
        self.__action_view_switch_tab_previous = QAction()
        self.__action_view_switch_tab_previous.setText("Switch to the &previous tab")
        self.__action_view_switch_tab_previous.setShortcut(Qt.Modifier.CTRL | Qt.Modifier.ALT | Qt.Key.Key_Left)
        self.__action_view_switch_tab_previous.setToolTip("Switch to the previous tab")
        self.__action_view_switch_tab_previous.setStatusTip("Switch to the previous tab: switches the current viewport "
                                                            "to the previous tab.")
        self.__view_tab_menu.addAction(self.__action_view_switch_tab_previous)

        # Constructing the switch to tab next action.
        # It switches the current viewport to tab next.
        self.__action_view_switch_tab_next = QAction()
        self.__action_view_switch_tab_next.setText("Switch to the &next tab")
        self.__action_view_switch_tab_next.setShortcut(Qt.Modifier.CTRL | Qt.Modifier.ALT | Qt.Key.Key_Right)
        self.__action_view_switch_tab_next.setToolTip("Switch to the next tab")
        self.__action_view_switch_tab_next.setStatusTip("Switch to the next tab: switches the current viewport to the "
                                                        "next tab.")
        self.__view_tab_menu.addAction(self.__action_view_switch_tab_next)

        # Adding a separator...
        self.__view_menu.addSeparator()

        # Constructing the full screen action.
        # It toggles viewport of full screen.
        self.__action_view_full_screen = QAction()
        self.__action_view_full_screen.setText("&Full screen")
        self.__action_view_full_screen.setShortcut(QKeySequence.StandardKey.FullScreen)
        self.__action_view_full_screen.setToolTip("Full screen")
        self.__action_view_full_screen.setStatusTip("Full screen: toggles viewport-full-screen.")
        self.__action_view_full_screen.setCheckable(True)
        self.__action_view_full_screen.setChecked(False)
        self.__view_menu.addAction(self.__action_view_full_screen)

        # Constructing the format menu.
        self.__format_menu = QMenu()
        self.__format_menu.setTitle("F&ormat")
        self.__menu_bar.addMenu(self.__format_menu)

        # Constructing the language menu inside the format menu.
        self.__format_lang_menu = QMenu()
        self.__format_lang_menu.setTitle("&Language")
        self.__format_menu.addMenu(self.__format_lang_menu)

        # Constructing the none language action.
        # It sets no syntax settings or deletes the previous settings.
        self.__action_format_lang_none = QAction()
        self.__action_format_lang_none.setText("&None")
        self.__action_format_lang_none.setToolTip("None")
        self.__action_format_lang_none.setStatusTip("None: sets no syntax settings or deletes the previous settings.")
        self.__action_format_lang_none.setCheckable(True)
        self.__action_format_lang_none.setChecked(True)
        self.__format_lang_menu.addAction(self.__action_format_lang_none)

        # Adding a separator...
        self.__format_lang_menu.addSeparator()

        # Constructing the C++ menu, inside the language menu.
        self.__format_lang_c_plus_plus_menu = QMenu()
        self.__format_lang_c_plus_plus_menu.setTitle("&C++")
        self.__format_lang_menu.addMenu(self.__format_lang_c_plus_plus_menu)

        # Constructing the C++ language action.
        # It sets the syntax settings as C++.
        self.__action_format_lang_c_plus_plus = QAction()
        self.__action_format_lang_c_plus_plus.setText("&C++")
        self.__action_format_lang_c_plus_plus.setToolTip("C++")
        self.__action_format_lang_c_plus_plus.setStatusTip("C++: sets the syntax settings as C++.")
        self.__action_format_lang_c_plus_plus.setCheckable(True)
        self.__action_format_lang_c_plus_plus.setChecked(False)
        self.__format_lang_c_plus_plus_menu.addAction(self.__action_format_lang_c_plus_plus)

        # Constructing the CSS menu, inside the language menu.
        self.__format_lang_css_menu = QMenu()
        self.__format_lang_css_menu.setTitle("C&SS")
        self.__format_lang_menu.addMenu(self.__format_lang_css_menu)

        # Constructing the CSS language action.
        # It sets the syntax settings as CSS.
        self.__action_format_lang_css = QAction()
        self.__action_format_lang_css.setText("&CSS")
        self.__action_format_lang_css.setToolTip("CSS")
        self.__action_format_lang_css.setStatusTip("CSS: sets the syntax settings as CSS.")
        self.__action_format_lang_css.setCheckable(True)
        self.__action_format_lang_css.setChecked(False)
        self.__format_lang_css_menu.addAction(self.__action_format_lang_css)

        # Constructing the HTML menu.
        self.__format_lang_html_menu = QMenu()
        self.__format_lang_html_menu.setTitle("&HTML")
        self.__format_lang_menu.addMenu(self.__format_lang_html_menu)

        # Constructing the HTML language action.
        # It sets the syntax settings as HTML.
        self.__action_format_lang_html = QAction()
        self.__action_format_lang_html.setText("&HTML")
        self.__action_format_lang_html.setToolTip("HTML")
        self.__action_format_lang_html.setStatusTip("HTML: sets the syntax settings as HTML.")
        self.__action_format_lang_html.setCheckable(True)
        self.__action_format_lang_html.setChecked(False)
        self.__format_lang_html_menu.addAction(self.__action_format_lang_html)

        # Adding a separator...
        self.__format_lang_html_menu.addSeparator()

        # Constructing the Django template of the HTML language action.
        # It sets the template settings as Django template of the HTML.
        self.__action_format_lang_html_django = QAction()
        self.__action_format_lang_html_django.setText("Set &Django template")
        self.__action_format_lang_html_django.setToolTip("Set Django template")
        self.__action_format_lang_html_django.setStatusTip("Set Django template: Set the HTML markup to Django.")
        self.__action_format_lang_html_django.setCheckable(True)
        self.__action_format_lang_html_django.setChecked(False)
        self.__format_lang_html_menu.addAction(self.__action_format_lang_html_django)

        # Constructing the Mako template of the HTML language action.
        # It sets the syntax settings as Mako template of the HTML.
        self.__action_format_lang_html_mako = QAction()
        self.__action_format_lang_html_mako.setText("Set &Mako template")
        self.__action_format_lang_html_mako.setToolTip("Set Mako template")
        self.__action_format_lang_html_mako.setStatusTip("Set Mako template: Set the HTML markup to Mako.")
        self.__action_format_lang_html_mako.setCheckable(True)
        self.__action_format_lang_html_mako.setChecked(False)
        self.__format_lang_html_menu.addAction(self.__action_format_lang_html_mako)

        # Constructing the HTML action group.
        # It sets the exclusion policy as exclusive optional.
        self.__action_group_format_lang_html = QActionGroup(self)
        self.__action_group_format_lang_html.setExclusionPolicy(QActionGroup.ExclusionPolicy.ExclusiveOptional)
        self.__action_group_format_lang_html.addAction(self.__action_format_lang_html_django)
        self.__action_group_format_lang_html.addAction(self.__action_format_lang_html_mako)

        # Constructing the Java menu, inside the language menu.
        self.__format_lang_java_menu = QMenu()
        self.__format_lang_java_menu.setTitle("&Java")
        self.__format_lang_menu.addMenu(self.__format_lang_java_menu)

        # Constructing the Java language action.
        # It sets the syntax settings as Java.
        self.__action_format_lang_java = QAction()
        self.__action_format_lang_java.setText("&Java")
        self.__action_format_lang_java.setToolTip("Java")
        self.__action_format_lang_java.setStatusTip("Java: sets the syntax settings as Java.")
        self.__action_format_lang_java.setCheckable(True)
        self.__action_format_lang_java.setChecked(False)
        self.__format_lang_java_menu.addAction(self.__action_format_lang_java)

        # Constructing the JavaScript menu, inside the language menu.
        self.__format_lang_js_menu = QMenu()
        self.__format_lang_js_menu.setTitle("Java&Script")
        self.__format_lang_menu.addMenu(self.__format_lang_js_menu)

        # Constructing the JavaScript language action.
        # It sets the syntax settings as JavaScript.
        self.__action_format_lang_js = QAction()
        self.__action_format_lang_js.setText("Java&Script")
        self.__action_format_lang_js.setToolTip("JavaScript")
        self.__action_format_lang_js.setStatusTip("JavaScript: sets the syntax settings as JavaScript.")
        self.__action_format_lang_js.setCheckable(True)
        self.__action_format_lang_js.setChecked(False)
        self.__format_lang_js_menu.addAction(self.__action_format_lang_js)

        # Constructing the Markdown menu, inside the language menu.
        self.__format_lang_md_menu = QMenu()
        self.__format_lang_md_menu.setTitle("&Markdown")
        self.__format_lang_menu.addMenu(self.__format_lang_md_menu)

        # Constructing the Markdown language action.
        # It sets the syntax settings as Markdown.
        self.__action_format_lang_md = QAction()
        self.__action_format_lang_md.setText("&Markdown")
        self.__action_format_lang_md.setToolTip("Markdown")
        self.__action_format_lang_md.setStatusTip("Markdown: sets the syntax settings as Markdown.")
        self.__action_format_lang_md.setCheckable(True)
        self.__action_format_lang_md.setChecked(False)
        self.__format_lang_md_menu.addAction(self.__action_format_lang_md)

        # Constructing the Python menu.
        self.__format_lang_python_menu = QMenu()
        self.__format_lang_python_menu.setTitle("&Python")
        self.__format_lang_menu.addMenu(self.__format_lang_python_menu)

        # Constructing the Python (2) language action.
        # It sets the syntax settings as Python (2).
        self.__action_format_lang_python_2 = QAction()
        self.__action_format_lang_python_2.setText("&Python 2")
        self.__action_format_lang_python_2.setToolTip("Python 2")
        self.__action_format_lang_python_2.setStatusTip("Python 2: sets the syntax settings as Python 2.")
        self.__action_format_lang_python_2.setCheckable(True)
        self.__action_format_lang_python_2.setChecked(False)
        self.__format_lang_python_menu.addAction(self.__action_format_lang_python_2)

        # Constructing the Python (3) language action.
        # It sets the syntax settings as Python (3).
        self.__action_format_lang_python = QAction()
        self.__action_format_lang_python.setText("&Python 3")
        self.__action_format_lang_python.setToolTip("Python 3")
        self.__action_format_lang_python.setStatusTip("Python 3: sets the syntax settings as Python 3.")
        self.__action_format_lang_python.setCheckable(True)
        self.__action_format_lang_python.setChecked(False)
        self.__format_lang_python_menu.addAction(self.__action_format_lang_python)

        # Constructing the action group of the language actions.
        # It sets the exclusion policy to exclusive.
        self.__action_group_format_lang = QActionGroup(self)
        self.__action_group_format_lang.setExclusionPolicy(QActionGroup.ExclusionPolicy.Exclusive)
        self.__action_group_format_lang.addAction(self.__action_format_lang_none)
        self.__action_group_format_lang.addAction(self.__action_format_lang_c_plus_plus)
        self.__action_group_format_lang.addAction(self.__action_format_lang_css)
        self.__action_group_format_lang.addAction(self.__action_format_lang_html)
        self.__action_group_format_lang.addAction(self.__action_format_lang_java)
        self.__action_group_format_lang.addAction(self.__action_format_lang_js)
        self.__action_group_format_lang.addAction(self.__action_format_lang_md)
        self.__action_group_format_lang.addAction(self.__action_format_lang_python)
        self.__action_group_format_lang.addAction(self.__action_format_lang_python_2)

        # Constructing the window menu.
        self.__window_menu = QMenu()
        self.__window_menu.setTitle("&Window")
        self.__menu_bar.addMenu(self.__window_menu)

        # Constructing the maximize action.
        # It maximizes the window.
        self.__action_window_maximize = QAction()
        self.__action_window_maximize.setText("M&aximize")
        self.__action_window_maximize.setToolTip("Maximize")
        self.__action_window_maximize.setStatusTip("Maximize: maximizes the window.")
        self.__window_menu.addAction(self.__action_window_maximize)

        # Constructing the minimize action.
        # It minimized the window.
        self.__action_window_minimize = QAction()
        self.__action_window_minimize.setText("M&inimize")
        self.__action_window_minimize.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_M)
        self.__action_window_minimize.setToolTip("Minimize")
        self.__action_window_minimize.setStatusTip("Minimize: minimizes the window.")
        self.__window_menu.addAction(self.__action_window_minimize)

    def __init_bar_status(self):
        """
        Initializing the status bar.

        :return: None
        """

        # Constructing the status bar.
        self.__status_bar = QStatusBar()
        self.setStatusBar(self.__status_bar)

        # Constructing the row label.
        # It displays the current row by the current document's cursor (starts from 1).
        self.__row_label = QLabel()
        self.__row_label.setText("Row: 1")
        self.__status_bar.addPermanentWidget(self.__row_label)

        # Constructing the column label.
        # It displays the current column by the current document's cursor (starts from 1).
        self.__col_label = QLabel()
        self.__col_label.setText("Column: 1")
        self.__status_bar.addPermanentWidget(self.__col_label)

        # Constructing the zoom label.
        # It displays the current zoom range (from 1% to 300%).
        self.__zoom_label = QLabel()
        self.__zoom_label.setText("Zoom: 100%")
        self.__status_bar.addPermanentWidget(self.__zoom_label)

        # Constructing the language label.
        # It displays the name of the current document's language (like Notepad++).
        self.__lang_label = QLabel()
        self.__lang_label.setText(self.lang["No"])
        self.__status_bar.addPermanentWidget(self.__lang_label)

        # Constructing the tab label.
        # It displays the current index document, and the number of the opened documents.
        self.__tab_label = QLabel()
        self.__tab_label.setText("Tab: 1 / 1")
        self.__status_bar.addPermanentWidget(self.__tab_label)

    def __init_signals(self):
        """
        Connecting the signals.

        :return: None
        """

        # Connecting the signals of the file menu.
        self.__action_file_new.triggered.connect(self.__slot_new)
        self.__action_file_open.triggered.connect(self.__slot_open)
        self.__action_file_close.triggered.connect(self.__slot_close)
        self.__action_file_save.triggered.connect(self.__slot_save)
        self.__action_file_save_as.triggered.connect(self.__slot_save_as)
        self.__action_file_print.triggered.connect(self.__slot_print)

        # Connecting the signals of the edit menu.
        self.__action_edit_undo.triggered.connect(self.__ed.undo)
        self.__action_edit_redo.triggered.connect(self.__ed.redo)
        self.__action_edit_cut.triggered.connect(self.__ed.cut)
        self.__action_edit_copy.triggered.connect(self.__ed.copy)
        self.__action_edit_paste.triggered.connect(self.__ed.paste)
        self.__action_edit_find.triggered.connect(self.__slot_find)
        self.__action_edit_replace.triggered.connect(self.__slot_replace)
        self.__action_edit_goto.triggered.connect(self.__slot_goto)
        self.__action_edit_select_all.triggered.connect(self.__ed.selectAll)

        # Connecting the signals of the view menu.
        self.__action_view_zoom_in.triggered.connect(self.__ed.zoom_in)
        self.__action_view_zoom_out.triggered.connect(self.__ed.zoom_out)
        # Connecting the signals of the switch menu.
        self.__action_view_switch_tab_1.triggered.connect(self.__slot_view_1)
        self.__action_view_switch_tab_2.triggered.connect(self.__slot_view_2)
        self.__action_view_switch_tab_3.triggered.connect(self.__slot_view_3)
        self.__action_view_switch_tab_4.triggered.connect(self.__slot_view_4)
        self.__action_view_switch_tab_5.triggered.connect(self.__slot_view_5)
        self.__action_view_switch_tab_6.triggered.connect(self.__slot_view_6)
        self.__action_view_switch_tab_7.triggered.connect(self.__slot_view_7)
        self.__action_view_switch_tab_8.triggered.connect(self.__slot_view_8)
        self.__action_view_switch_tab_9.triggered.connect(self.__slot_view_9)
        self.__action_view_switch_tab_10.triggered.connect(self.__slot_view_10)
        self.__action_view_switch_tab_previous.triggered.connect(self.__slot_view_previous)
        self.__action_view_switch_tab_next.triggered.connect(self.__slot_view_next)
        # Connecting the signals of the remaining view menu.
        self.__action_view_full_screen.triggered.connect(self.__slot_full_screen)

        # Connecting the signals of the format menu.
        # Connecting the signals of the language menu.
        self.__action_format_lang_none.triggered.connect(self.__slot_format_lang_none)
        self.__action_format_lang_c_plus_plus.triggered.connect(self.__slot_format_lang_c_plus_plus)
        self.__action_format_lang_css.triggered.connect(self.__slot_format_lang_css)
        self.__action_format_lang_html.triggered.connect(self.__slot_format_lang_html)
        self.__action_format_lang_html_django.triggered.connect(self.__ed.set_lexer_html_django)
        self.__action_format_lang_html_mako.triggered.connect(self.__ed.set_lexer_html_mako)
        self.__action_format_lang_java.triggered.connect(self.__slot_format_lang_java)
        self.__action_format_lang_js.triggered.connect(self.__slot_format_lang_js)
        self.__action_format_lang_md.triggered.connect(self.__slot_format_lang_md)
        self.__action_format_lang_python_2.triggered.connect(self.__slot_format_lang_python_2)
        self.__action_format_lang_python.triggered.connect(self.__slot_format_lang_python_3)

        # Connecting the signals of the window menu.
        self.__action_window_maximize.triggered.connect(self.showMaximized)
        self.__action_window_minimize.triggered.connect(self.showMinimized)

        # ---------------------------------------

        # Connecting the signals of the tab widget.
        self.__tab_widget.tabCloseRequested.connect(self.___slot_tab_close_requested)
        self.__tab_widget.currentChanged.connect(self.___slot_tab_changed)

        # ---------------------------------------

        # Connecting the signals of the editor.
        self.__ed.SCN_ZOOM.connect(self.___slot_zoom_changed)
        self.__ed.copyAvailable.connect(self.__action_edit_copy.setEnabled)
        self.__ed.copyAvailable.connect(self.__action_edit_cut.setEnabled)
        self.__ed.cursorPositionChanged.connect(self.___slot_pos_changed)
        self.__ed.selectionChanged.connect(self.___slot_pos_changed)

    def __init_window(self):
        """
        Initializing the window.
        :return: None
        """

        self.resize(QSize(600, 400))
        if sys.platform != "darwin":
            self.setWindowIcon(self.__icon_self)
        self.setWindowTitle(f"Untitled - Txter")
        self.showMaximized()

    def closeEvent(self, event):
        """
        Override.

        The close event of the application.

        :param event: QCloseEvent | Any | Parameter by the event handler
        :return: None. Close (accept) and do not close (ignore).
        """
        if self.__tab_widget.count() > 1:
            # Parse this function if the count is larger than 1.
            self.__slot_close()

        # Asking if save.
        is_save = self.___private_ask_if_save()

        if is_save is True:
            # "Save"

            if self.__slot_save():
                # "Save" and parsed.

                event.accept()
                # Closed.

            else:
                # "Cancel"

                event.ignore()
                # Do not close.

        elif is_save is False:
            # Saved already, or not modified.

            event.accept()
            # Closed.

        else:
            # Do not close.

            event.ignore()

    def ___private_ask_if_save(self):
        """
        Ask if save.

        Private method.

        :return: True if the user want to save.
                 False if the user do not want to save, or the document need not to save.
                 None if any other situations.
        """

        try:
            # Exception handler.

            if self.__ed:
                # If there's the editor (if self.__tab_widget.count() >= 1):

                if self.__ed.text() == self.original[self.__tab_widget.currentIndex()]:
                    # If the document has not modified.

                    return False

                # Ask by a message box.

                rst = QMessageBox.information(self, "Save", "This document has been modified. "
                                                            "Do you want to save the document?",
                                              QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
                if rst == QMessageBox.Cancel:
                    # If the user press "Cancel"

                    return None

                # Save or not?
                return rst == QMessageBox.Save
            else:
                # Or else, return False.
                return False

        except IndexError:
            # If there's index error, pass it.

            pass

    def ___private_new_tab(self):
        """
        Construct a new tab.

        Private method.

        :return: The new index of the tab.
        """

        # Constructing a new editor.
        new_ed = editor.Editor(self)
        new_ed.set_lexer_none()

        # Replacing the older editor with the new one.
        self.__ed = new_ed
        # !important

        # Constructing a new tab.
        index = self.__tab_widget.addTab(new_ed,  # New widget.
                                         self.__image_normal,  # New icon.
                                         f"Untitled {self.__tab_widget.count()}")
        # And new title.

        # Switch to the new tab automatically.
        self.__tab_widget.setCurrentIndex(index)

        try:
            # Exception handler.

            self.original[index] = ""
            # Sets the original index as new "".

        except IndexError:
            # If there's an index error, add an item to the list.

            self.original.append("")

        # Return the new index of the appended tab.
        return index

    def ___slot_pos_changed(self):
        """
        The inner slot that handling the position change of the editor.
        Mainly handling the status bar label and actions.

        Private method.
        Inner slot.

        :return: None
        """

        # Handling the actions.
        self.__action_edit_undo.setEnabled(self.__ed.isUndoAvailable())
        self.__action_edit_redo.setEnabled(self.__ed.isRedoAvailable())

        # Handling the labels.
        self.__col_label.setText(f"Row: {(self.__ed.getCursorPosition()[0]) + 1}")
        self.__row_label.setText(f"Col: {(self.__ed.getCursorPosition()[1]) + 1}")

    def ___slot_tab_changed(self, index):
        """
        The inner slot handles the tab changing.
        Updates a lot of things, such as window title, slots, icon, file name, etc.

        Private method.
        Inner slot.

        !Important

        :param index: int | Index of the new tab | Given by Qt.
        :return: None
        """

        # Retrieving the current editor (of the new tab).
        self.__ed = self.__tab_widget.currentWidget()

        if self.__ed:
            # If there's an editor (there is at least a tab).

            # Call the changing.
            self.___slot_pos_changed()
            self.___slot_zoom_changed()

            # Connecting the signals with new editor.
            self.__ed.SCN_ZOOM.connect(self.___slot_zoom_changed)
            self.__ed.copyAvailable.connect(self.__action_edit_copy.setEnabled)
            self.__ed.copyAvailable.connect(self.__action_edit_cut.setEnabled)
            self.__ed.cursorPositionChanged.connect(self.___slot_pos_changed)
            self.__ed.selectionChanged.connect(self.___slot_pos_changed)

            # The title.
            text = self.__tab_widget.tabText(index)

            # Setting the window title, with file name or "Untitled".
            self.setWindowTitle(f"{text} - Txter")

            try:
                # Exception handling.

                # Split the directory and the filename (with extension).
                tool_tip = os.path.split(text)[1]

            except:
                # If there's any error (except Exception:)

                # Tooltip is the text (splitting "Untitled")
                tool_tip = text

            # Setting the tab tooltip, of the current index.
            self.__tab_widget.setTabToolTip(index, tool_tip)

            # Retrieving the path or untitled.
            self.path = text

            if self.path.startswith("Untitled"):
                # "Untitled (x)"

                self.path = ""

            # Retrieving what lexer the editor use.

            # Using the variables.
            lexer_none = self.__ed.is_lexer_none()
            lexer_cpp = self.__ed.is_lexer_c_plus_plus()
            lexer_css = self.__ed.is_lexer_css()
            lexer_html = self.__ed.is_lexer_html()
            lexer_html_django = self.__ed.is_lexer_html_django()
            lexer_html_mako = self.__ed.is_lexer_html_mako()
            lexer_java = self.__ed.is_lexer_java()
            lexer_js = self.__ed.is_lexer_js()
            lexer_md = self.__ed.is_lexer_md()
            lexer_py = self.__ed.is_lexer_py()
            lexer_py2 = self.__ed.is_lexer_py2()

            # Checking the actions, with the variable declared.
            self.__action_format_lang_none.setChecked(lexer_none)
            self.__action_format_lang_c_plus_plus.setChecked(lexer_cpp)
            self.__action_format_lang_css.setChecked(lexer_css)
            self.__action_format_lang_html.setChecked(lexer_html)
            self.__action_format_lang_html_django.setChecked(lexer_html_django)
            self.__action_format_lang_html_mako.setChecked(lexer_html_mako)
            self.__action_format_lang_java.setChecked(lexer_java)
            self.__action_format_lang_js.setChecked(lexer_js)
            self.__action_format_lang_md.setChecked(lexer_md)
            self.__action_format_lang_python.setChecked(lexer_py)
            self.__action_format_lang_python_2.setChecked(lexer_py2)

            # Setting the language lexer.

            if lexer_none:
                # Language: None

                self.__lang_label.setText(self.lang["No"])

            elif lexer_cpp:
                # Language: C++ (C-plus-plus)

                self.__lang_label.setText(self.lang["C++"])

            elif lexer_css:
                # Language: CSS (Cascading StyleSheet)

                self.__lang_label.setText(self.lang["CSS"])

            elif lexer_html:
                # Language: HTML (HyperText Markup Language)

                self.__lang_label.setText(self.lang["HTML"])

            elif lexer_java:
                # Language: Java

                self.__lang_label.setText(self.lang["Java"])

            elif lexer_js:
                # Language JS (JavaScript)

                self.__lang_label.setText(self.lang["JS"])

            elif lexer_md:
                # Language MD (MarkDown)

                self.__lang_label.setText(self.lang["Markdown"])

            elif lexer_py:
                # Language Python (Python 3)

                self.__lang_label.setText(self.lang["Python"])

            elif lexer_py2:
                # Language Python (Python 2)

                self.__lang_label.setText(self.lang["py2"])

            # -UNUSED- # Changing the window icon.
            # if sys.platform == "darwin":
            # self.setWindowIcon(self.__tab_widget.tabIcon(index))

        # Updating the tab label (Tab: x / y).
        self.__tab_label.setText(f"Tab: {index + 1} / {self.__tab_widget.count()}")

    def ___slot_tab_close_requested(self, index):
        """
        This inner slot is worked when the user click the "close" icon on the tab.
        Mainly closing the tabs.

        Private method.
        Inner slot.

        :param index: int | Index of the closing tab | Given by Qt
        :return: None
        """

        # Setting current Index.
        self.__tab_widget.setCurrentIndex(index)

        # Asking if save.
        is_save = self.___private_ask_if_save()

        if is_save is True:
            # "Save"

            if self.__slot_save():
                # "Save" and file name entered

                self.__tab_widget.removeTab(index)

            else:
                # "Discard" or "Do not save"

                return

        elif is_save is False:
            # The document does not modify or saved already.

            self.__tab_widget.removeTab(index)

        else:
            # Any other situations.

            return

        if self.__tab_widget.count() <= 0:
            # Else if the tab count less than 0,

            self.close()

    def ___slot_zoom_changed(self):
        """
        This inner slot holds the zoom range change.
        Mainly updating the zoom label.

        Private method.
        Inner slot.

        :return: None
        """

        # Retrieving the zoom range (from -10 to +20).
        zoom = self.__ed.SendScintilla(self.__ed.SCI_GETZOOM)

        if sys.platform == "win32":
            # If it works on Windows,

            if zoom < 0:
                # -10 to -1:

                zoom = (11 - abs(zoom)) * 10

            elif zoom > 0:
                # +1 to +20

                zoom = abs(zoom) // 2 * 10 + 110

            else:
                # 0

                zoom = 100

        else:
            # When the application working on macOS or Linux (coming soon)

            zoom = zoom * 10 + 100

            if zoom == 0:
                # 0% -> 1%

                zoom = 1

        # Setting the text of the label (Zoom: 100%).
        self.__zoom_label.setText(f"Zoom: {zoom}%")

    def __slot_new(self):
        """
        This slot handles a new document.

        Actually, it's opening a new tab, and clears the older index, only.

        :return: None

        --------------- Unused code ---------------

        is_save = self.___private_ask_if_save()

        if is_save is True:

            if self.__slot_save():

                self.__ed.clear()
                self.setWindowTitle(f"Untitled - Txter")

        elif is_save is False:

            self.__ed.clear()
            self.setWindowTitle(f"Untitled - Txter")

        """

        # Adding a new tab.
        self.___private_new_tab()

    def __slot_open(self):
        """
        This slot opens a/some file(s),
        read their contents,
        parse their lexers,
        opens a new tab,
        etc.

        :return: None
        """

        try:
            # Exception handling.

            # Creating a dialog.
            dlg = QFileDialog(self)
            # Setting its window modality.
            dlg.setWindowModality(Qt.WindowModal)
            # Setting its window title. Does not take effects on macOS.
            dlg.setWindowTitle("Open - Txter")
            # Setting filters, just like {tkinter's (filetypes=[(),()])}.
            dlg.setNameFilter(";;".join(self.__open_support))
            # Open mode.
            dlg.setAcceptMode(QFileDialog.AcceptOpen)
            # Select one OR MORE file(s).
            dlg.setFileMode(QFileDialog.ExistingFiles)
            # Set the initial directory, as the document directory.
            dlg.setDirectory(QStandardPaths.standardLocations(QStandardPaths.DocumentsLocation)[0])
            # Execute it.
            dlg.exec()

            # Loop, because of one or more file selected.
            for item in dlg.selectedFiles():
                # Looping, inside.

                if item:
                    # If there's an item, but not blank (''),

                    # Retrieve the index from the private method -- new tab.
                    index = self.___private_new_tab()

                    with open(item, "rb") as file:
                        # Use Python's default file reader.

                        # Decode the text, as it's read in binary.
                        content = file.read().decode("utf-8-sig")

                        # Changing the original content list.
                        self.original[index] = content

                        # Close the file stream.
                        file.close()

                    # Set the text in the new editor.
                    self.__ed.setText(content)
                    # Changing the path.
                    self.path = item

                    # Detecting different types of lexers, or no lexer.

                    if dlg.selectedNameFilter() in ["C++ source (*.cpp)",
                                                    "C++ new-define source (*.cxx)",
                                                    "C++ sources (*.cpp; *.cxx)",
                                                    "C++ C-type header (*.h)",
                                                    "C++ header (*.hpp)",
                                                    "C++ new-define header (*.hxx)",
                                                    "C++ header (*.h; *.hpp; *hxx)",
                                                    "C++ files (*.cpp; *.cxx; *.h; *.hxx; *.hpp)"]:
                        # C++ files.
                        # .cpp;.cxx;.h;.hpp;.hxx

                        self.__ed.set_lexer_c_plus_plus()
                        self.__action_format_lang_c_plus_plus.setChecked(True)
                        self.__lang_label.setText(self.lang["C++"])

                    elif dlg.selectedNameFilter() == "CSS file (*.css)":
                        # CSS files.
                        # .css

                        self.__ed.set_lexer_cascading_style_sheet()
                        self.__action_format_lang_css.setChecked(True)
                        self.__lang_label.setText(self.lang["CSS"])

                    elif dlg.filter() in ["HTML source (*.html)",
                                          "HTML multimedia source (*.mhtml)",
                                          "HTML single package source (*.shtml)"]:
                        # HTML files.
                        # .html;.mhtml;.shtml

                        self.__ed.set_lexer_html()
                        self.__action_format_lang_html.setChecked(True)
                        self.__lang_label.setText(self.lang["HTML"])

                    elif dlg.selectedNameFilter() in ["Java code (*.java)",
                                                      "Java class archive (*.jar)",
                                                      "Java files (*.java; *.jar)"]:
                        # Java files.
                        # .java;.jar

                        self.__ed.set_lexer_java()
                        self.__action_format_lang_java.setChecked(True)
                        self.__lang_label.setText(self.lang["Java"])

                    elif dlg.selectedNameFilter() == "JavaScript file (*.js)":
                        # JavaScript files.
                        # .js

                        self.__ed.set_lexer_js()
                        self.__action_format_lang_js.setChecked(True)
                        self.__lang_label.setText(self.lang["JS"])

                    elif dlg.selectedNameFilter() in ["Markdown file (*.md)",
                                                      "Markdown file (*.markdown)",
                                                      "Markdown files (*.md; *.markdown)"]:
                        # Markdown files.
                        # .md;.markdown

                        self.__ed.set_lexer_markdown()
                        self.__action_format_lang_md.setChecked(True)
                        self.__lang_label.setText(self.lang["Markdown"])

                    elif dlg.selectedNameFilter() in ["PyInstaller files (*.spec)",
                                                      "Python script (*.py)",
                                                      "Python console-less scripts (*.pyw)",
                                                      "Python scripts (*.py; *.pyw)",
                                                      "Python cache file (*.pyc)",
                                                      "Python informative documentations (*.pyi)",
                                                      "Python bytecode optimized file (*.pyo)",
                                                      "Python files (*.py; *.pyw; *.pyc; *.pyi; *.pyo)"]:
                        # Python (2/3) files; PyInstaller files.
                        # .spec
                        # .py;.pyw;.pyc;.pyi;.pyo

                        # Set the default as Python 3.
                        self.__ed.set_lexer_python()
                        self.__action_format_lang_python.setChecked(True)
                        self.__lang_label.setText(self.lang["Python"])

                    else:
                        # If the user selects "All files (*.*)", we should still detect it/them.

                        if os.path.splitext(item)[1].lower() in (".cpp",
                                                                 ".cxx",
                                                                 ".h",
                                                                 ".hpp",
                                                                 ".hxx"):
                            # C++ files.

                            self.__ed.set_lexer_c_plus_plus()
                            self.__action_format_lang_c_plus_plus.setChecked(True)
                            self.__lang_label.setText(self.lang["C++"])

                        elif os.path.splitext(item)[1].lower() == ".css":
                            # CSS files.

                            self.__ed.set_lexer_cascading_style_sheet()
                            self.__action_format_lang_css.setChecked(True)
                            self.__lang_label.setText(self.lang["CSS"])

                        elif os.path.splitext(item)[1].lower() in (".html",
                                                                   ".mhtml",
                                                                   ".shtml"):
                            # HTML files.

                            self.__ed.set_lexer_html()
                            self.__action_format_lang_html.setChecked(True)
                            self.__lang_label.setText(self.lang["HTML"])

                        elif os.path.splitext(item)[1].lower() in (".java", ".jar"):
                            # Java files.

                            self.__ed.set_lexer_java()
                            self.__action_format_lang_java.setChecked(True)
                            self.__lang_label.setText(self.lang["Java"])

                        elif os.path.splitext(item)[1].lower() == ".js":
                            # JavaScript files.

                            self.__ed.set_lexer_js()
                            self.__action_format_lang_js.setChecked(True)
                            self.__lang_label.setText(self.lang["JS"])

                        elif os.path.splitext(item)[1].lower() in (".md",
                                                                   ".markdown"):
                            # Markdown files.

                            self.__ed.set_lexer_markdown()
                            self.__action_format_lang_md.setChecked(True)
                            self.__lang_label.setText(self.lang["Markdown"])

                        elif os.path.splitext(item)[1].lower() in (".py",
                                                                   ".pyw",
                                                                   ".pyc",
                                                                   ".pyi",
                                                                   ".pyo",
                                                                   ".spec"):
                            # Python files.
                            # PyInstaller files.

                            self.__ed.set_lexer_python()
                            self.__action_format_lang_python.setChecked(True)
                            self.__lang_label.setText(self.lang["Python"])

                        else:
                            # We cannot detect them, we still does not support them,
                            # Or it's only a plain text file (*.txt).

                            self.__ed.set_lexer_none()
                            self.__lang_label.setText(self.lang["No"])

                    # Set the tab title as the file name.
                    # Preventing "Untitled x", and non-detection.
                    self.__tab_widget.setTabText(index, item)

                    try:
                        # Exception handler.

                        # Split the directory and the file name.
                        tool_tip = os.path.split(self.__tab_widget.tabText(index))[1]

                    except:
                        # If there's any Exception happened,

                        # Then, set the title as "Untitled x", still.
                        tool_tip = self.__tab_widget.tabText(index)

                    # Set the tab tooltip.
                    self.__tab_widget.setTabToolTip(index, tool_tip)

                    # Setting a file info.
                    file_info = QFileInfo(item)

                    # Retrieving the system icon of the file.
                    icon = QFileIconProvider().icon(file_info)

                    # Setting the tab icon.
                    self.__tab_widget.setTabIcon(index, icon)

                    # -UNUSED- # Setting the window icon, as same as the tab icon.
                    # if sys.platform == "darwin":
                        # self.setWindowIcon(icon) # NOQA

        except IndexError:
            # If there's an index error: list()[1],

            # then pass it!
            pass

        except Exception as exc:
            # Except other type of exception,

            # Create a messagebox and report it.
            msg = QMessageBox(self)
            msg.setWindowModality(Qt.WindowModal)
            msg.setWindowTitle("Error")
            msg.setText(f"Cannot open the file. Reason: {str(exc)}")
            msg.setInformativeText("Txter cannot process the file.")
            msg.setDetailedText(traceback.format_exc())

            # Execute the message box.
            msg.exec()

        else:
            # If there's no exception,

            try:
                # Then set the window title.

                self.setWindowTitle(f"{item} - Txter")

            except:
                # Except other exception, again, ... :P

                # Pass it.
                pass
                # Our goal is no crashing apps!

    def open_through_argv(self, argv_list):
        """
        Open A FILE through sys.argv list.
        Same as open.

        :param argv_list: list[str] | sys.argv
        :return: None
        """

        try:

            item = argv_list[1]

            with open(item, "rb") as file:

                content = file.read().decode("utf-8-sig")
                self.original[0] = content
                file.close()

            self.__ed.setText(content)
            self.path = item

            if os.path.splitext(item)[1].lower() in (".cpp",
                                                     ".cxx",
                                                     ".h",
                                                     ".hpp",
                                                     ".hxx"):

                self.__ed.set_lexer_c_plus_plus()
                self.__action_format_lang_c_plus_plus.setChecked(True)
                self.__lang_label.setText(self.lang["C++"])

            elif os.path.splitext(item)[1].lower() == ".css":

                self.__ed.set_lexer_cascading_style_sheet()
                self.__action_format_lang_css.setChecked(True)
                self.__lang_label.setText(self.lang["CSS"])

            elif os.path.splitext(item)[1].lower() in (".html",
                                                       ".mhtml",
                                                       ".shtml"):

                self.__ed.set_lexer_html()
                self.__action_format_lang_html.setChecked(True)
                self.__lang_label.setText(self.lang["HTML"])

            elif os.path.splitext(item)[1].lower() in (".java", ".jar"):

                self.__ed.set_lexer_java()
                self.__action_format_lang_java.setChecked(True)
                self.__lang_label.setText(self.lang["Java"])

            elif os.path.splitext(item)[1].lower() == ".js":

                self.__ed.set_lexer_js()
                self.__action_format_lang_js.setChecked(True)
                self.__lang_label.setText(self.lang["JS"])

            elif os.path.splitext(item)[1].lower() in (".md",
                                                       ".markdown"):

                self.__ed.set_lexer_markdown()
                self.__action_format_lang_md.setChecked(True)
                self.__lang_label.setText(self.lang["Markdown"])

            elif os.path.splitext(item)[1].lower() in (".egg",
                                                       ".egg-info",
                                                       ".py",
                                                       ".pyw",
                                                       ".pyc",
                                                       ".pyi",
                                                       ".pyo",
                                                       ".spec"):

                self.__ed.set_lexer_python()
                self.__action_format_lang_python.setChecked(True)
                self.__lang_label.setText(self.lang["Python"])

            else:

                self.__ed.set_lexer_none()
                self.__lang_label.setText(self.lang["No"])

        except:

            pass

        else:

            self.setWindowTitle(f"{item} - Txter")

    def __slot_close(self):
        """
        Close the tab, or close the whole application.

        Same as {def closeEvent(self, event: QCloseEvent) -> None:}.

        :return: None
        """

        if self.__tab_widget.count() > 1:

            index = self.__tab_widget.currentIndex()
            is_save = self.___private_ask_if_save()

            if is_save is True:

                if self.__slot_save():

                    self.__tab_widget.removeTab(index)
                    self.original.pop(index)
                else:

                    return

            elif is_save is False:

                self.__tab_widget.removeTab(index)
                self.original.pop(index)

            else:

                return

        else:

            self.close()

    def __slot_save(self):
        """
        Save the file.

        If there's no path, save as the file first.

        :return: True if save successfully.
                 None if not successful.
        """

        if not self.path:
            # If there's no path,

            self.__slot_save_as()
            return

        # The item is the path.
        item = self.path

        with open(item, "wb") as file:
            # Using Python's default functionality to save the file.

            # Write to the file, using binary.
            file.write(self.__ed.text().encode("utf-8-sig"))

            # Changing the original.
            self.original[self.__tab_widget.currentIndex()] = self.__ed.text()

            # Close the file stream.
            file.close()

        # Return True if save successfully.
        return True

    def __slot_save_as(self):
        """
        Save the file with a dialog.

        :return: None
        """

        try:
            # Exception handler.

            # Creating a dialog.
            dlg = QFileDialog(self)
            # Setting its window modality.
            dlg.setWindowModality(Qt.WindowModal)
            # Setting the window title. It does not take any effect on macOS.
            dlg.setWindowTitle("Save as - Vocab")
            # Sets the filter.
            dlg.setNameFilter(";;".join(self.__save_support))
            # Sets as save mode.
            dlg.setAcceptMode(QFileDialog.AcceptSave)
            # Sets the default directory as document directory.
            dlg.setDirectory(QStandardPaths.standardLocations(QStandardPaths.DocumentsLocation)[0])
            # Set the default filter as text files (*.txt).
            dlg.selectNameFilter("Text files (*.txt)")

            if self.__action_format_lang_c_plus_plus.isChecked():
                # If the lexer is C++:

                dlg.selectNameFilter("C++ source (*.cpp)")

            elif self.__action_format_lang_css.isChecked():
                # If the lexer is CSS:

                dlg.selectNameFilter("CSS file (*.css)")

            elif self.__action_format_lang_html.isChecked():
                # If the lexer is HTML:

                dlg.selectNameFilter("HTML source (*.html)")

            elif self.__action_format_lang_java.isChecked():
                # If the lexer is Java:

                dlg.selectNameFilter("Java code (*.java)")

            elif self.__action_format_lang_js.isChecked():
                # If the lexer is JavaScript:

                dlg.selectNameFilter("JavaScript file (*.js)")

            elif self.__action_format_lang_md.isChecked():
                # If the lexer is MarkDown:

                dlg.selectNameFilter("Markdown file (*.md)")

            elif (self.__action_format_lang_python.isChecked()
                  | self.__action_format_lang_python_2.isChecked()):
                # If the lexer is either Python 2 or Python 3:

                dlg.selectNameFilter("Python script (*.py)")

            # Execute the dialog.
            dlg.exec()

            if dlg.selectedFiles()[0]:
                # If there's selected files,

                file_list = dlg.selectedFiles()
                item = file_list[0]

                with open(item, "wb") as file:
                    # Using Python's default file stream.

                    # Write the file as binary.
                    file.write(self.__ed.text().encode("utf-8-sig"))

                    # Updating the original text.
                    self.original[self.__tab_widget.currentIndex()] = self.__ed.text()

                    # Updating the path.
                    self.path = item

                    # Close the file stream.
                    file.close()

            else:
                # Else, return None, terminate the function.

                return

        except IndexError:
            # Except an index error,

            # Then pass it!
            pass

        except Exception as exc:
            # Except any other types of error,

            # We will create a message box to report them.

            msg = QMessageBox(self)
            msg.setWindowModality(Qt.WindowModal)
            msg.setWindowTitle("Error")
            msg.setText(f"Cannot save the file. Reason: {str(exc)}")
            msg.setInformativeText("Txter cannot process the file.")
            msg.setDetailedText(traceback.format_exc())

            # Execute the message box.
            msg.exec()

            # And terminate the method.
            return

        else:
            # If there's no error,

            # Update the window title.
            self.setWindowTitle(f"{item} - Txter")

    def __slot_save_all(self):
        """
        - UNUSED -

        Save all the opened files.

        :return: None
        """

        # Get the current index.
        index = self.__tab_widget.currentIndex()

        # Create an unsaved ("Untitled") list.
        unsaved = []

        # Switch to the first tab.
        self.__tab_widget.setCurrentIndex(0)

        # Create one while-loop,
        while self.__tab_widget.currentIndex() <= self.__tab_widget.count():
            # to save the files one-by-one.

            if not self.path:
                # If there's an "Untitled" file,

                # Append it to the list.
                unsaved.append(self.__tab_widget.tabName(self.__tab_widget.currentIndex))
                continue

            # Set the item equals to the path.
            item = self.path

            with open(item, "wb") as file:
                # Use the Python's default file stream to save the files.

                # Write the content into the file.
                file.write(self.__ed.text().encode("utf-8-sig"))

                # Updating the original list.
                self.original[self.__tab_widget.currentIndex()] = self.__ed.text()

                # Close the file stream.
                file.close()

            # Switch to the next tab.
            self.__slot_view_next()

        # Finally, switch to the initial tab.
        self.__tab_widget.setCurrentIndex(index)

        # If there's any "Untitled" files,
        if unsaved:
            # announce them by a message box.

            msg = QMessageBox(self)
            msg.setWindowModality(Qt.WindowModal)
            msg.setWindowTitle("Information")
            msg.setText(f"There are a/some file(s) that you've never save it/them before.")
            msg.setInformativeText("Click 'details' to view their name(s).")
            msg.setDetailedText("\n".join(unsaved))
            msg.exec()

    def __slot_print(self):
        """
        Print the document, by a printer.

        :return: None
        """

        # Creating a printer (QsciPrinter inherits QPrinter)
        prn = QsciPrinter(QPrinter.PrinterMode.HighResolution)

        # Creating a print dialog.
        dlg = dialogs.PrintDialog(prn, self.__ed)

        # And then execute the dialog.
        dlg.exec()

    def __slot_quit(self):
        """
        Quit the application.

        :return: None
        """

        # Quit by QApplication,
        qApp.quit()

        # And by closing the window.
        self.close()

    def __slot_find(self):
        """
        Summon the find dialog.

        :return: None
        """

        # Constructing the find dialog.
        dlg = dialogs.FindDialog(self.__ed)

        # Execute it.
        dlg.exec()

    def __slot_replace(self):
        """
        Summon the replace dialog.

        :return: None
        """

        # Constructing the replace dialog.
        dlg = dialogs.ReplaceDialog(self.__ed)

        # Execute it.
        dlg.exec()

    def __slot_goto(self):
        """
        Summon the goto dialog.

        :return: None
        """

        # Constructing the goto dialog.
        dlg = dialogs.GotoDialog(self.__ed)

        # Execute it.
        dlg.exec()

    def __slot_view_1(self):
        """
        Switch to tab one.

        :return: None
        """

        self.__tab_widget.setCurrentIndex(0)

    def __slot_view_2(self):
        """
        Switch to tab two.

        :return: None
        """

        self.__tab_widget.setCurrentIndex(1)

    def __slot_view_3(self):
        """
        Switch to tab three.

        :return: None
        """

        self.__tab_widget.setCurrentIndex(2)

    def __slot_view_4(self):
        """
        Switch to tab four.

        :return: None
        """

        self.__tab_widget.setCurrentIndex(3)

    def __slot_view_5(self):
        """
        Switch to tab five.

        :return: None
        """

        self.__tab_widget.setCurrentIndex(4)

    def __slot_view_6(self):
        """
        Switch to tab six.

        :return: None
        """

        self.__tab_widget.setCurrentIndex(5)

    def __slot_view_7(self):
        """
        Switch to tab seven.

        :return: None
        """

        self.__tab_widget.setCurrentIndex(6)

    def __slot_view_8(self):
        """
        Switch to tab eight.

        :return: None
        """

        self.__tab_widget.setCurrentIndex(7)

    def __slot_view_9(self):
        """
        Switch to tab nine.

        :return: None
        """

        self.__tab_widget.setCurrentIndex(8)

    def __slot_view_10(self):
        """
        Switch to tab ten.

        :return: None
        """

        self.__tab_widget.setCurrentIndex(9)

    def __slot_view_previous(self):
        """
        Switch to the previous tab.

        :return: None
        """

        self.__tab_widget.setCurrentIndex(self.__tab_widget.currentIndex() - 1)

    def __slot_view_next(self):
        """
        Switch to the next tab.

        :return: None
        """

        self.__tab_widget.setCurrentIndex(self.__tab_widget.currentIndex() + 1)

    def __slot_full_screen(self, is_checked=False):
        """
        Toggles full screen.

        :param is_checked: bool | Is the action checked | Given by Qt
        :return: None
        """

        if is_checked:
            # If the action checked

            self.showFullScreen()

        else:
            # Or else it has not checked

            self.showMaximized()

    def __slot_format_lang_none(self):
        """
        Change the lexer to no language.

        :return: None
        """

        self.__ed.set_lexer_none()
        self.__lang_label.setText(self.lang["No"])
        self.__tab_widget.setTabIcon(self.__tab_widget.currentIndex(), self.__image_normal)

    def __slot_format_lang_c_plus_plus(self):
        """
        Change the lexer to C++.

        :return: None
        """

        self.__ed.set_lexer_c_plus_plus()
        self.__lang_label.setText(self.lang["C++"])
        self.__tab_widget.setTabIcon(self.__tab_widget.currentIndex(), self.__image_c_plus_plus)

    def __slot_format_lang_css(self):
        """
        Change the lexer to CSS.

        :return: None
        """

        self.__ed.set_lexer_cascading_style_sheet()
        self.__lang_label.setText(self.lang["CSS"])
        self.__tab_widget.setTabIcon(self.__tab_widget.currentIndex(), self.__image_css)

    def __slot_format_lang_html(self):
        """
        Change the lexer to HTML.

        :return: None
        """

        self.__ed.set_lexer_html()
        self.__lang_label.setText(self.lang["HTML"])
        self.__tab_widget.setTabIcon(self.__tab_widget.currentIndex(), self.__image_html)

    def __slot_format_lang_java(self):
        """
        Change the lexer to Java.

        :return: None
        """

        self.__ed.set_lexer_java()
        self.__lang_label.setText(self.lang["Java"])
        self.__tab_widget.setTabIcon(self.__tab_widget.currentIndex(), self.__image_java)

    def __slot_format_lang_js(self):
        """
        Change the lexer to JavaScript.

        :return: None
        """

        self.__ed.set_lexer_js()
        self.__lang_label.setText(self.lang["JS"])
        self.__tab_widget.setTabIcon(self.__tab_widget.currentIndex(), self.__image_js)

    def __slot_format_lang_md(self):
        """
        Change the lexer to MarkDown.

        :return: None
        """

        self.__ed.set_lexer_markdown()
        self.__lang_label.setText(self.lang["Markdown"])
        self.__tab_widget.setTabIcon(self.__tab_widget.currentIndex(), self.__image_md)

    def __slot_format_lang_python_2(self):
        """
        Change the lexer to Python 2.

        :return: None
        """

        self.__ed.set_lexer_python_2()
        self.__lang_label.setText(self.lang["py2"])
        self.__tab_widget.setTabIcon(self.__tab_widget.currentIndex(), self.__image_python)

    def __slot_format_lang_python_3(self):
        """
        Change the lexer to Python 3
        (Python)

        :return: None
        """

        self.__ed.set_lexer_python()
        self.__lang_label.setText(self.lang["Python"])
        self.__tab_widget.setTabIcon(self.__tab_widget.currentIndex(), self.__image_python)

    #
    # -------------
    # Public method
    # -------------
    #

    def context_menu_list(self):
        return [
                self.__action_edit_undo,
                self.__action_edit_redo,
                None,
                self.__action_edit_cut,
                self.__action_edit_copy,
                self.__action_edit_paste,
                None,
                self.__action_edit_select_all
            ]

#
# Running the main script...
#


if __name__ == "__main__":
    # Run the script.

    # Constructing the QApplication, using the argv list.
    app = QApplication(sys.argv)

    try:
        # Exception handling.

        mw = MainWindow()
        mw.open_through_argv(sys.argv)
        mw.show()

    except BaseException as error:
        # Whenever happening a BaseException, we'll announce
        # a message box to report the error.

        # Constructing the messagebox...

        # Use "m" as the identifier,
        # and error as the exception class
        # because we don't want shadow definition.

        m = QMessageBox()
        m.setWindowModality(Qt.WindowModal)
        m.setWindowTitle("Error")
        m.setText(f"Error while running Txter. Reason: {str(error)}")
        m.setInformativeText("You may miscontrolled the application, or using the alpha/beta version of it which "
                             "may contain bugs. Please go to https://sourceforge.net/p/brtxter/discussion/bug-report/"
                             " for reporting bugs, or leave Txter.")
        m.setDetailedText(traceback.format_exc())

        # Execute the message box.
        m.exec()

    # finally: # We don't need it.
    sys.exit(app.exec())
