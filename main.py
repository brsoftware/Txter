"""

"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qsci import QsciPrinter
from PyQt5.QtPrintSupport import *

import os
import sys
import traceback

import dialogs
import editor


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

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
            "Python script (*.py)",
            "Python console-less scripts (*.pyw)",
            "Python scripts (*.py; *.pyw)",
            "Python cache file (*.pyc)",
            "Python informative documentations (*.pyi)",
            "Python bytecode optimized file (*.pyo)",
            "Python files (*.py; *.pyw; *.pyc; *.pyi; *.pyo)"
        ]

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
            "Python script (*.py)",
            "Python console-less scripts (*.pyw)",
            "Python cache file (*.pyc)",
            "Python informative documentations (*.pyi)",
            "Python bytecode optimized file (*.pyo)",
        ]

        self.original = ""
        self.path = ""

        self.__init_editor()
        self.__init_bar_menu()
        self.__init_bar_status()
        self.__init_signals()
        self.__init_window()

    def __init_editor(self):
        self.__ed = editor.Editor()
        self.__ed.set_lexer_none()
        self.setCentralWidget(self.__ed)

    def __init_bar_menu(self):
        self.__menu_bar = QMenuBar()
        self.setMenuBar(self.__menu_bar)

        self.__file_menu = QMenu()
        self.__file_menu.setTitle("&File")
        self.__menu_bar.addMenu(self.__file_menu)

        self.__action_file_new = QAction()
        self.__action_file_new.setText("&New")
        self.__action_file_new.setShortcut(QKeySequence.StandardKey.New)
        self.__action_file_new.setToolTip("New")
        self.__action_file_new.setStatusTip("New: creates a new document.")
        self.__file_menu.addAction(self.__action_file_new)

        self.__action_file_open = QAction()
        self.__action_file_open.setText("&Open")
        self.__action_file_open.setShortcut(QKeySequence.StandardKey.Open)
        self.__action_file_open.setToolTip("Open")
        self.__action_file_open.setStatusTip("Open: opens an existing document.")
        self.__file_menu.addAction(self.__action_file_open)

        self.__action_file_close = QAction()
        self.__action_file_close.setText("&Close")
        self.__action_file_close.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_W)
        self.__action_file_close.setToolTip("close")
        self.__action_file_close.setStatusTip("Close: closes an existing document.")
        self.__file_menu.addAction(self.__action_file_close)

        self.__file_menu.addSeparator()

        self.__action_file_save = QAction()
        self.__action_file_save.setText("&Save")
        self.__action_file_save.setShortcut(QKeySequence.StandardKey.Save)
        self.__action_file_save.setToolTip("save")
        self.__action_file_save.setStatusTip("Save: saves an existing document.")
        self.__file_menu.addAction(self.__action_file_save)

        self.__action_file_save_as = QAction()
        self.__action_file_save_as.setText("Save &as")
        self.__action_file_save_as.setShortcut(Qt.Modifier.CTRL | Qt.Modifier.SHIFT | Qt.Key.Key_S)
        self.__action_file_save_as.setToolTip("Save as")
        self.__action_file_save_as.setStatusTip("Save as: saves an existing document using a new path.")
        self.__file_menu.addAction(self.__action_file_save_as)

        self.__file_menu.addSeparator()

        self.__action_file_print = QAction()
        self.__action_file_print.setText("&Print")
        self.__action_file_print.setShortcut(QKeySequence.StandardKey.Print)
        self.__action_file_print.setToolTip("Print")
        self.__action_file_print.setStatusTip("Print: prints this document.")
        self.__file_menu.addAction(self.__action_file_print)

        self.__file_menu.addSeparator()

        self.__action_file_quit = QAction()
        self.__action_file_quit.setText("&Quit")
        self.__action_file_quit.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_Q)
        self.__action_file_quit.setToolTip("Quit")
        self.__action_file_quit.setStatusTip("Quit: quites this application.")
        self.__file_menu.addAction(self.__action_file_quit)

        self.__edit_menu = QMenu()
        self.__edit_menu.setTitle("&Edit")
        self.__menu_bar.addMenu(self.__edit_menu)

        self.__action_edit_undo = QAction()
        self.__action_edit_undo.setText("&Undo")
        self.__action_edit_undo.setShortcut(QKeySequence.StandardKey.Undo)
        self.__action_edit_undo.setToolTip("Undo")
        self.__action_edit_undo.setStatusTip("Undo: undoes the last action you did.")
        self.__action_edit_undo.setEnabled(False)
        self.__edit_menu.addAction(self.__action_edit_undo)

        self.__action_edit_redo = QAction()
        self.__action_edit_redo.setText("&Redo")
        self.__action_edit_redo.setShortcut(QKeySequence.StandardKey.Redo)
        self.__action_edit_redo.setToolTip("Redo")
        self.__action_edit_redo.setStatusTip("Redo: redoes the last action you did.")
        self.__action_edit_redo.setEnabled(False)
        self.__edit_menu.addAction(self.__action_edit_redo)

        self.__edit_menu.addSeparator()

        self.__action_edit_cut = QAction()
        self.__action_edit_cut.setText("&Cut")
        self.__action_edit_cut.setShortcut(QKeySequence.StandardKey.Cut)
        self.__action_edit_cut.setToolTip("Cut")
        self.__action_edit_cut.setStatusTip("Cut: cuts the selected text.")
        self.__action_edit_cut.setEnabled(False)
        self.__edit_menu.addAction(self.__action_edit_cut)

        self.__action_edit_copy = QAction()
        self.__action_edit_copy.setText("C&opy")
        self.__action_edit_copy.setShortcut(QKeySequence.StandardKey.Copy)
        self.__action_edit_copy.setToolTip("Copy")
        self.__action_edit_copy.setStatusTip("Copy: copies the selected text.")
        self.__action_edit_copy.setEnabled(False)
        self.__edit_menu.addAction(self.__action_edit_copy)

        self.__action_edit_paste = QAction()
        self.__action_edit_paste.setText("&Paste")
        self.__action_edit_paste.setShortcut(QKeySequence.StandardKey.Paste)
        self.__action_edit_paste.setToolTip("Paste")
        self.__action_edit_paste.setStatusTip("Paste: pastes the word in the system clipboard.")
        self.__edit_menu.addAction(self.__action_edit_paste)

        self.__edit_menu.addSeparator()

        self.__action_edit_find = QAction()
        self.__action_edit_find.setText("&Find")
        self.__action_edit_find.setShortcut(QKeySequence.StandardKey.Find)
        self.__action_edit_find.setToolTip("Find")
        self.__action_edit_find.setStatusTip("Find: finds the last action you did.")
        self.__edit_menu.addAction(self.__action_edit_find)

        self.__action_edit_replace = QAction()
        self.__action_edit_replace.setText("&Replace")
        self.__action_edit_replace.setShortcut((Qt.Modifier.CTRL | Qt.Modifier.SHIFT | Qt.Key.Key_H)
                                               if sys.platform == "darwin" else QKeySequence.StandardKey.Replace)
        self.__action_edit_replace.setToolTip("Replace")
        self.__action_edit_replace.setStatusTip("Replace: replaces the last action you did.")
        self.__edit_menu.addAction(self.__action_edit_replace)

        self.__action_edit_goto = QAction()
        self.__action_edit_goto.setText("&Goto")
        self.__action_edit_goto.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_G)
        self.__action_edit_goto.setToolTip("Goto")
        self.__action_edit_goto.setStatusTip("Goto: goes to the last action you did.")
        self.__edit_menu.addAction(self.__action_edit_goto)

        self.__edit_menu.addSeparator()

        self.__action_edit_select_all = QAction()
        self.__action_edit_select_all.setText("Select &all")
        self.__action_edit_select_all.setShortcut(QKeySequence.StandardKey.SelectAll)
        self.__action_edit_select_all.setToolTip("Select all")
        self.__action_edit_select_all.setStatusTip("Select all: selects all text of the document.")
        self.__edit_menu.addAction(self.__action_edit_select_all)

        self.__view_menu = QMenu()
        self.__view_menu.setTitle("&View")
        self.__menu_bar.addMenu(self.__view_menu)

        self.__action_view_zoom_in = QAction()
        self.__action_view_zoom_in.setText("Zoom &in")
        self.__action_view_zoom_in.setShortcut(QKeySequence.StandardKey.ZoomIn)
        self.__action_view_zoom_in.setToolTip("Zoom in")
        self.__action_view_zoom_in.setStatusTip("Zoom in: zooms in the document.")
        self.__view_menu.addAction(self.__action_view_zoom_in)

        self.__action_view_zoom_out = QAction()
        self.__action_view_zoom_out.setText("Zoom &out")
        self.__action_view_zoom_out.setShortcut(QKeySequence.StandardKey.ZoomOut)
        self.__action_view_zoom_out.setToolTip("Zoom out")
        self.__action_view_zoom_out.setStatusTip("Zoom out: zooms out the document.")
        self.__view_menu.addAction(self.__action_view_zoom_out)

        self.__view_menu.addSeparator()

        self.__action_view_full_screen = QAction()
        self.__action_view_full_screen.setText("&Full screen")
        self.__action_view_full_screen.setShortcut(QKeySequence.StandardKey.FullScreen)
        self.__action_view_full_screen.setToolTip("Full screen")
        self.__action_view_full_screen.setStatusTip("Full screen: toggles viewport-full-screen.")
        self.__action_view_full_screen.setCheckable(True)
        self.__action_view_full_screen.setChecked(False)
        self.__view_menu.addAction(self.__action_view_full_screen)

        self.__format_menu = QMenu()
        self.__format_menu.setTitle("F&ormat")
        self.__menu_bar.addMenu(self.__format_menu)

        self.__format_lang_menu = QMenu()
        self.__format_lang_menu.setTitle("&Language")
        self.__format_menu.addMenu(self.__format_lang_menu)

        self.__action_format_lang_none = QAction()
        self.__action_format_lang_none.setText("&None")
        self.__action_format_lang_none.setToolTip("None")
        self.__action_format_lang_none.setStatusTip("None: sets no syntax settings or deletes the previous settings.")
        self.__action_format_lang_none.setCheckable(True)
        self.__action_format_lang_none.setChecked(True)
        self.__format_lang_menu.addAction(self.__action_format_lang_none)

        self.__format_lang_menu.addSeparator()

        self.__format_lang_c_plus_plus_menu = QMenu()
        self.__format_lang_c_plus_plus_menu.setTitle("&C++")
        self.__format_lang_menu.addMenu(self.__format_lang_c_plus_plus_menu)

        self.__action_format_lang_c_plus_plus = QAction()
        self.__action_format_lang_c_plus_plus.setText("&C++")
        self.__action_format_lang_c_plus_plus.setToolTip("C++")
        self.__action_format_lang_c_plus_plus.setStatusTip("C++: sets the syntax settings as C++.")
        self.__action_format_lang_c_plus_plus.setCheckable(True)
        self.__action_format_lang_c_plus_plus.setChecked(False)
        self.__format_lang_c_plus_plus_menu.addAction(self.__action_format_lang_c_plus_plus)

        self.__format_lang_css_menu = QMenu()
        self.__format_lang_css_menu.setTitle("C&SS")
        self.__format_lang_menu.addMenu(self.__format_lang_css_menu)

        self.__action_format_lang_css = QAction()
        self.__action_format_lang_css.setText("&CSS")
        self.__action_format_lang_css.setToolTip("CSS")
        self.__action_format_lang_css.setStatusTip("CSS: sets the syntax settings as CSS.")
        self.__action_format_lang_css.setCheckable(True)
        self.__action_format_lang_css.setChecked(False)
        self.__format_lang_css_menu.addAction(self.__action_format_lang_css)

        self.__format_lang_html_menu = QMenu()
        self.__format_lang_html_menu.setTitle("&HTML")
        self.__format_lang_menu.addMenu(self.__format_lang_html_menu)

        self.__action_format_lang_html = QAction()
        self.__action_format_lang_html.setText("&HTML")
        self.__action_format_lang_html.setToolTip("HTML")
        self.__action_format_lang_html.setStatusTip("HTML: sets the syntax settings as HTML.")
        self.__action_format_lang_html.setCheckable(True)
        self.__action_format_lang_html.setChecked(False)
        self.__format_lang_html_menu.addAction(self.__action_format_lang_html)

        self.__format_lang_html_menu.addSeparator()

        self.__action_format_lang_html_django = QAction()
        self.__action_format_lang_html_django.setText("Set &Django template")
        self.__action_format_lang_html_django.setToolTip("Set Django template")
        self.__action_format_lang_html_django.setStatusTip("Set Django template: Set the HTML markup to Django.")
        self.__action_format_lang_html_django.setCheckable(True)
        self.__action_format_lang_html_django.setChecked(False)
        self.__format_lang_html_menu.addAction(self.__action_format_lang_html_django)

        self.__action_format_lang_html_mako = QAction()
        self.__action_format_lang_html_mako.setText("Set &Mako template")
        self.__action_format_lang_html_mako.setToolTip("Set Mako template")
        self.__action_format_lang_html_mako.setStatusTip("Set Mako template: Set the HTML markup to Mako.")
        self.__action_format_lang_html_mako.setCheckable(True)
        self.__action_format_lang_html_mako.setChecked(False)
        self.__format_lang_html_menu.addAction(self.__action_format_lang_html_mako)

        self.__action_group_format_lang_html = QActionGroup(self)
        self.__action_group_format_lang_html.setExclusionPolicy(QActionGroup.ExclusionPolicy.ExclusiveOptional)
        self.__action_group_format_lang_html.addAction(self.__action_format_lang_html_django)
        self.__action_group_format_lang_html.addAction(self.__action_format_lang_html_mako)

        self.__format_lang_java_menu = QMenu()
        self.__format_lang_java_menu.setTitle("&Java")
        self.__format_lang_menu.addMenu(self.__format_lang_java_menu)

        self.__action_format_lang_java = QAction()
        self.__action_format_lang_java.setText("&Java")
        self.__action_format_lang_java.setToolTip("Java")
        self.__action_format_lang_java.setStatusTip("Java: sets the syntax settings as Java.")
        self.__action_format_lang_java.setCheckable(True)
        self.__action_format_lang_java.setChecked(False)
        self.__format_lang_java_menu.addAction(self.__action_format_lang_java)

        self.__format_lang_js_menu = QMenu()
        self.__format_lang_js_menu.setTitle("Java&Script")
        self.__format_lang_menu.addMenu(self.__format_lang_js_menu)

        self.__action_format_lang_js = QAction()
        self.__action_format_lang_js.setText("Java&Script")
        self.__action_format_lang_js.setToolTip("JavaScript")
        self.__action_format_lang_js.setStatusTip("JavaScript: sets the syntax settings as JavaScript.")
        self.__action_format_lang_js.setCheckable(True)
        self.__action_format_lang_js.setChecked(False)
        self.__format_lang_js_menu.addAction(self.__action_format_lang_js)

        self.__format_lang_python_menu = QMenu()
        self.__format_lang_python_menu.setTitle("&Python")
        self.__format_lang_menu.addMenu(self.__format_lang_python_menu)

        self.__action_format_lang_python_2 = QAction()
        self.__action_format_lang_python_2.setText("&Python 2")
        self.__action_format_lang_python_2.setToolTip("Python 2")
        self.__action_format_lang_python_2.setStatusTip("Python 2: sets the syntax settings as Python 2.")
        self.__action_format_lang_python_2.setCheckable(True)
        self.__action_format_lang_python_2.setChecked(False)
        self.__format_lang_python_menu.addAction(self.__action_format_lang_python_2)

        self.__action_format_lang_python = QAction()
        self.__action_format_lang_python.setText("&Python 3")
        self.__action_format_lang_python.setToolTip("Python 3")
        self.__action_format_lang_python.setStatusTip("Python 3: sets the syntax settings as Python 3.")
        self.__action_format_lang_python.setCheckable(True)
        self.__action_format_lang_python.setChecked(False)
        self.__format_lang_python_menu.addAction(self.__action_format_lang_python)

        self.__action_group_format_lang = QActionGroup(self)
        self.__action_group_format_lang.setExclusionPolicy(QActionGroup.ExclusionPolicy.Exclusive)
        self.__action_group_format_lang.addAction(self.__action_format_lang_none)
        self.__action_group_format_lang.addAction(self.__action_format_lang_c_plus_plus)
        self.__action_group_format_lang.addAction(self.__action_format_lang_css)
        self.__action_group_format_lang.addAction(self.__action_format_lang_html)
        self.__action_group_format_lang.addAction(self.__action_format_lang_java)
        self.__action_group_format_lang.addAction(self.__action_format_lang_js)
        self.__action_group_format_lang.addAction(self.__action_format_lang_python)
        self.__action_group_format_lang.addAction(self.__action_format_lang_python_2)

        self.__window_menu = QMenu()
        self.__window_menu.setTitle("&Window")
        self.__menu_bar.addMenu(self.__window_menu)

        self.__action_window_maximize = QAction()
        self.__action_window_maximize.setText("M&aximize")
        self.__action_window_maximize.setToolTip("Maximize")
        self.__action_window_maximize.setStatusTip("Maximize: maximizes the window.")
        self.__window_menu.addAction(self.__action_window_maximize)

        self.__action_window_minimize = QAction()
        self.__action_window_minimize.setText("M&inimize")
        self.__action_window_minimize.setShortcut(Qt.Modifier.CTRL | Qt.Key.Key_M)
        self.__action_window_minimize.setToolTip("Minimize")
        self.__action_window_minimize.setStatusTip("Minimize: minimizes the window.")
        self.__window_menu.addAction(self.__action_window_minimize)

    def __init_bar_status(self):
        self.__status_bar = QStatusBar()
        self.setStatusBar(self.__status_bar)

        self.__row_label = QLabel()
        self.__row_label.setText("Row: 1")
        self.__status_bar.addPermanentWidget(self.__row_label)

        self.__col_label = QLabel()
        self.__col_label.setText("Column: 1")
        self.__status_bar.addPermanentWidget(self.__col_label)

    def __init_signals(self):
        self.__action_file_new.triggered.connect(self.__slot_new)
        self.__action_file_open.triggered.connect(self.__slot_open)
        self.__action_file_close.triggered.connect(self.__slot_close)
        self.__action_file_save.triggered.connect(self.__slot_save)
        self.__action_file_save_as.triggered.connect(self.__slot_save_as)
        self.__action_file_print.triggered.connect(self.__slot_print)
        self.__action_file_quit.triggered.connect(self.__slot_quit)
        self.__action_edit_undo.triggered.connect(self.__ed.undo)
        self.__action_edit_redo.triggered.connect(self.__ed.redo)
        self.__action_edit_cut.triggered.connect(self.__ed.cut)
        self.__action_edit_copy.triggered.connect(self.__ed.copy)
        self.__action_edit_paste.triggered.connect(self.__ed.paste)
        self.__action_edit_find.triggered.connect(self.__slot_find)
        self.__action_edit_replace.triggered.connect(self.__slot_replace)
        self.__action_edit_goto.triggered.connect(self.__slot_goto)
        self.__action_edit_select_all.triggered.connect(self.__ed.selectAll)
        self.__action_view_zoom_in.triggered.connect(self.__ed.zoom_in)
        self.__action_view_zoom_out.triggered.connect(self.__ed.zoom_out)
        self.__action_view_full_screen.triggered.connect(self.__slot_full_screen)
        self.__action_format_lang_none.triggered.connect(self.__ed.set_lexer_none)
        self.__action_format_lang_c_plus_plus.triggered.connect(self.__ed.set_lexer_c_plus_plus)
        self.__action_format_lang_css.triggered.connect(self.__ed.set_lexer_cascading_style_sheet)
        self.__action_format_lang_html.triggered.connect(self.__ed.set_lexer_html)
        self.__action_format_lang_html_django.triggered.connect(self.__ed.set_lexer_html_django)
        self.__action_format_lang_html_mako.triggered.connect(self.__ed.set_lexer_html_mako)
        self.__action_format_lang_java.triggered.connect(self.__ed.set_lexer_java)
        self.__action_format_lang_js.triggered.connect(self.__ed.set_lexer_js)
        self.__action_format_lang_python_2.triggered.connect(self.__ed.set_lexer_python_2)
        self.__action_format_lang_python.triggered.connect(self.__ed.set_lexer_python)
        self.__action_window_maximize.triggered.connect(self.showMaximized)
        self.__action_window_minimize.triggered.connect(self.showMinimized)

        self.__ed.copyAvailable.connect(self.__action_edit_copy.setEnabled)
        self.__ed.copyAvailable.connect(self.__action_edit_cut.setEnabled)
        self.__ed.cursorPositionChanged.connect(self.___slot_pos_changed)
        self.__ed.selectionChanged.connect(self.___slot_pos_changed)

    def __init_window(self):
        self.setWindowTitle("Txter")
        self.showMaximized()

    def closeEvent(self, event):
        is_save = self.___private_ask_if_save()
        if is_save is True:
            if self.__slot_save():
                event.accept()
        elif is_save is False:
            event.accept()
        else:
            event.ignore()

    def ___private_ask_if_save(self):
        if self.__ed.text() == self.original:
            return False

        rst = QMessageBox.information(self, "Save", "This document has been modifier. "
                                                    "Do you want to save the document?",
                                      QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        if rst == QMessageBox.Cancel:
            return None

        return rst == QMessageBox.Save

    def ___slot_pos_changed(self):
        self.__action_edit_undo.setEnabled(self.__ed.isUndoAvailable())
        self.__action_edit_redo.setEnabled(self.__ed.isRedoAvailable())

        self.__col_label.setText(f"Row: {(self.__ed.getCursorPosition()[0]) + 1}")
        self.__row_label.setText(f"Col: {(self.__ed.getCursorPosition()[1]) + 1}")

    def __slot_new(self):
        is_save = self.___private_ask_if_save()
        if is_save is True:
            if self.__slot_save():
                self.__ed.clear()
        elif is_save is False:
            self.__ed.clear()

    def __slot_open(self):
        try:
            dlg = QFileDialog(self)
            dlg.setWindowModality(Qt.WindowModal)
            dlg.setWindowTitle("Open - Txter")
            dlg.setNameFilter(";;".join(self.__open_support))
            dlg.setAcceptMode(QFileDialog.AcceptOpen)
            dlg.setFileMode(QFileDialog.ExistingFile)
            dlg.exec()
            if dlg.selectedFiles()[0]:
                file_list = dlg.selectedFiles()
                item = file_list[0]
                with open(item, "rb") as file:
                    content = file.read().decode("utf-8-sig")
                    self.original = content
                    file.close()

                self.__ed.setText(content)
                self.path = item

                if dlg.selectedNameFilter() in ["C++ source (*.cpp)",
                                                "C++ new-define source (*.cxx)",
                                                "C++ sources (*.cpp; *.cxx)",
                                                "C++ C-type header (*.h)",
                                                "C++ header (*.hpp)",
                                                "C++ new-define header (*.hxx)",
                                                "C++ header (*.h; *.hpp; *hxx)",
                                                "C++ files (*.cpp; *.cxx; *.h; *.hxx; *.hpp; *.hxx)"]:
                    self.__ed.set_lexer_c_plus_plus()
                elif dlg.selectedNameFilter() == "CSS file (*.css)":
                    self.__ed.set_lexer_cascading_style_sheet()
                elif dlg.filter() in ["HTML source (*.html)",
                                      "HTML multimedia source (*.mhtml)",
                                      "HTML single package source (*.shtml)"]:
                    self.__ed.set_lexer_html()
                elif dlg.selectedNameFilter() in ["Java code (*.java)",
                                                  "Java class archive (*.jar)",
                                                  "Java files (*.java; *.jar)"]:
                    self.__ed.set_lexer_java()
                elif dlg.selectedNameFilter() == "JavaScript file (*.js)":
                    self.__ed.set_lexer_js()
                elif dlg.selectedNameFilter() in ["Python script (*.py)",
                                                  "Python console-less scripts (*.pyw)",
                                                  "Python scripts (*.py; *.pyw)",
                                                  "Python cache file (*.pyc)",
                                                  "Python informative documentations (*.pyi)",
                                                  "Python bytecode optimized file (*.pyo)",
                                                  "Python files (*.py; *.pyw; *.pyc; *.pyi; *.pyo)"]:
                    self.__ed.set_lexer_python()
                else:
                    if os.path.splitext(dlg.selectedFiles()[0])[1].lower() in (".cpp",
                                                                               ".cxx",
                                                                               ".h",
                                                                               ".hpp",
                                                                               ".hxx"):
                        self.__ed.set_lexer_c_plus_plus()
                    elif os.path.splitext(dlg.selectedFiles()[0])[1].lower() == ".css":
                        self.__ed.set_lexer_cascading_style_sheet()
                    elif os.path.splitext(dlg.selectedFiles()[0])[1].lower() in (".html",
                                                                                 ".mhtml",
                                                                                 ".shtml"):
                        self.__ed.set_lexer_html()
                    elif os.path.splitext(dlg.selectedFiles()[0])[1].lower() in (".java", ".jar"):
                        self.__ed.set_lexer_java()
                    elif os.path.splitext(dlg.selectedFiles()[0])[1].lower() == ".js":
                        self.__ed.set_lexer_none()
                    elif os.path.splitext(dlg.selectedFiles()[0])[1].lower() in (".py",
                                                                                 ".pyw",
                                                                                 ".pyc",
                                                                                 ".pyi",
                                                                                 ".pyo"):
                        self.__ed.set_lexer_python()
                    else:
                        self.__ed.set_lexer_none()

        except IndexError:
            pass
        
        except Exception as exc:
            msg = QMessageBox(self)
            msg.setWindowModality(Qt.WindowModal)
            msg.setWindowTitle("Error")
            msg.setText(f"Cannot open the file. Reason: {str(exc)}")
            msg.setInformativeText("Txter cannot process the file.")
            msg.setDetailedText(traceback.format_exc())
            msg.exec()

    def open_through_argv(self, argv_list):
        try:
            item = argv_list[1]
            with open(item, "rb") as file:
                content = file.read().decode("utf-8-sig")
                self.original = content
                file.close()

            self.__ed.setText(content)
            self.path = item

            if os.path.splitext(item)[1].lower() in (".cpp",
                                                     ".cxx",
                                                     ".h",
                                                     ".hpp",
                                                     ".hxx"):
                self.__ed.set_lexer_c_plus_plus()
            elif os.path.splitext(item)[1].lower() == ".css":
                self.__ed.set_lexer_cascading_style_sheet()
            elif os.path.splitext(item)[1].lower() in (".html",
                                                       ".mhtml",
                                                       ".shtml"):
                self.__ed.set_lexer_html()
            elif os.path.splitext(item)[1].lower() in (".java", ".jar"):
                self.__ed.set_lexer_java()
            elif os.path.splitext(item)[1].lower() == ".js":
                self.__ed.set_lexer_none()
            elif os.path.splitext(item)[1].lower() in (".py",
                                                       ".pyw",
                                                       ".pyc",
                                                       ".pyi",
                                                       ".pyo"):
                self.__ed.set_lexer_python()
            else:
                self.__ed.set_lexer_none()

        except:
            pass

    def __slot_close(self):
        self.close()

    def __slot_save(self):
        if not self.path:
            self.__slot_save_as()

    def __slot_save_as(self):
        try:
            dlg = QFileDialog(self)
            dlg.setWindowModality(Qt.WindowModal)
            dlg.setWindowTitle("Save as - Vocab")
            dlg.setNameFilter(";;".join(self.__save_support))
            dlg.setAcceptMode(QFileDialog.AcceptSave)
            if self.__action_format_lang_c_plus_plus.isChecked():
                dlg.selectNameFilter("C++ source (*.cpp)")
            elif self.__action_format_lang_css.isChecked():
                dlg.selectNameFilter("CSS file (*.css)")
            elif self.__action_format_lang_html.isChecked():
                dlg.selectNameFilter("HTML source (*.html)")
            elif self.__action_format_lang_java.isChecked():
                dlg.selectNameFilter("Java code (*.java)")
            elif self.__action_format_lang_js.isChecked():
                dlg.selectNameFilter("JavaScript file (*.js)")
            elif (self.__action_format_lang_python.isChecked()
                  | self.__action_format_lang_python_2.isChecked()):
                dlg.selectNameFilter("Python script (*.py)")
            if dlg.exec():
                file_list = dlg.selectedFiles()
                item = file_list[0]
                with open(item, "wb") as file:
                    file.write(item.encode("utf-8-sig"))
                    self.original = self.__ed.text()
                    self.path = item
                    file.close()

        except Exception as exc:
            msg = QMessageBox(self)
            msg.setWindowModality(Qt.WindowModal)
            msg.setWindowTitle("Error")
            msg.setText(f"Cannot save the file. Reason: {str(exc)}")
            msg.setInformativeText("Txter cannot process the file.")
            msg.setDetailedText(traceback.format_exc())
            msg.exec()

    def __slot_print(self):
        prn = QsciPrinter(QPrinter.PrinterMode.HighResolution)
        dlg = dialogs.PrintDialog(prn, self.__ed)
        dlg.exec()

    def __slot_quit(self):
        qApp.quit()

    def __slot_find(self):
        dlg = dialogs.FindDialog(self.__ed)
        dlg.exec()

    def __slot_replace(self):
        dlg = dialogs.ReplaceDialog(self.__ed)
        dlg.exec()

    def __slot_goto(self):
        dlg = dialogs.GotoDialog(self.__ed)
        dlg.exec()

    def __slot_full_screen(self, is_checked=False):
        if is_checked:
            self.showFullScreen()
        else:
            self.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.open_through_argv(sys.argv)
    mw.show()
    sys.exit(app.exec())
