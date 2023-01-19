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


File Name:                              dialogs.py

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
from PyQt5.QtCore import *
from PyQt5.Qsci import *
from PyQt5.QtPrintSupport import QPrintDialog

# Python builtins
import traceback


class PrintDialog(QPrintDialog):
    """
    Print dialog.

    Through it, prints a document.
    """

    def __init__(self, printer, parent):
        """
        initializing method for PrintDialog.

        :param printer: QPrinter (must)
        :param parent: QWidget (must)
        """

        # Super the class to the parent.
        super().__init__(printer, parent)

        # Initializing settings...
        self.setWindowTitle("Print - Txter")
        self.setWindowModality(Qt.WindowModality.WindowModal)


class FindDialog(QDialog):
    """
    Find dialog.

    Through it, users can find a text easily, inside a document.
    """

    def __init__(self, parent):
        """
        Initializing method for FindDialog.

        :param parent: QWidget (must)
        """

        # Super the class to the parent.
        super().__init__(parent)

        # Defining variables
        self.__parent = parent

        # Setting window configures.
        self.setWindowTitle("Find - Txter")
        self.setWindowModality(Qt.WindowModality.WindowModal)

        # Creating the layouts.
        self.__layout = QVBoxLayout()

        self.__find_layout = QFormLayout()

        self.__find_label = QLabel()
        self.__find_label.setText("Find &what: ")
        self.__find_entry = QLineEdit()
        self.__find_entry.setPlaceholderText("Enter text")
        self.__find_label.setBuddy(self.__find_entry)
        self.__find_layout.addRow(self.__find_label, self.__find_entry)

        self.__layout.addLayout(self.__find_layout)

        self.__box = QDialogButtonBox()
        self.__ok = QPushButton()
        self.__ok.setText("&Find next")
        self.__ok.clicked.connect(self.___inner_slot_find)
        self.__box.addButton(self.__ok, QDialogButtonBox.AcceptRole)
        self.__cancel = QPushButton()
        self.__cancel.setText("&Cancel")
        self.__cancel.clicked.connect(self.close)
        self.__box.addButton(self.__cancel, QDialogButtonBox.RejectRole)

        self.__layout.addWidget(self.__box)

        self.setLayout(self.__layout)

    def ___inner_slot_find(self):
        """
        Find the text inside the document.

        :return: None
        """

        self.__parent.findFirst(self.__find_entry.text(), True, True, True, True, True)


class ReplaceDialog(QDialog):
    """
    Replace dialog.

    With it, users can replace a text with another easily.
    """

    def __init__(self, parent):
        """
        Initializing method for ReplaceDialog.

        :param parent: QWidget (must)
        """

        # Super the class to the parent.
        super().__init__(parent)

        # Defining variables.
        self.__parent = parent

        # Setting window configures.
        self.setWindowTitle("Replace - Txter")
        self.setWindowModality(Qt.WindowModality.WindowModal)

        # Creating layouts and widgets.
        self.__layout = QVBoxLayout()

        self.__find_layout = QFormLayout()

        self.__find_label = QLabel()
        self.__find_label.setText("&Target: ")
        self.__find_entry = QLineEdit()
        self.__find_entry.setPlaceholderText("Enter target")
        self.__find_label.setBuddy(self.__find_entry)
        self.__find_layout.addRow(self.__find_label, self.__find_entry)

        self.__replace_label = QLabel()
        self.__replace_label.setText("Replace &with:")
        self.__replace_entry = QLineEdit()
        self.__replace_entry.setPlaceholderText("Replace with")
        self.__replace_label.setBuddy(self.__replace_entry)
        self.__find_layout.addRow(self.__replace_label, self.__replace_entry)

        self.__layout.addLayout(self.__find_layout)

        self.__box = QDialogButtonBox()
        self.__ok = QPushButton()
        self.__ok.setText("&Replace")
        self.__ok.clicked.connect(self.___inner_slot_replace)
        self.__box.addButton(self.__ok, QDialogButtonBox.AcceptRole)
        self.__all = QPushButton()
        self.__all.setText("Replace &all")
        self.__all.clicked.connect(self.___inner_slot_replace_all)
        self.__box.addButton(self.__all, QDialogButtonBox.AcceptRole)
        self.__cancel = QPushButton()
        self.__cancel.setText("&Cancel")
        self.__cancel.clicked.connect(self.close)
        self.__box.addButton(self.__cancel, QDialogButtonBox.RejectRole)

        self.__layout.addWidget(self.__box)

        self.setLayout(self.__layout)

    def ___inner_slot_replace(self):
        """
        Replace once only.

        :return: None
        """

        self.__parent.findFirst(self.__find_entry.text(), True, True, True, True, True)
        self.__parent.replace(self.__replace_entry.text())

    def ___inner_slot_replace_all(self):
        """
        Replace all text.

        :return: None
        """

        # QTextCursor.beginEditBlock()
        self.__parent.beginUndoAction()

        while self.__parent.findFirst(self.__find_entry.text(), True, True, True, True, True):

            self.__parent.replace(self.__replace_entry.text())

        # QTextCursor.endEditBlock()
        self.__parent.endUndoAction()


class GotoDialog(QDialog):
    """
    Goto dialog.

    With it, users can goto a line number easily.
    """

    def __init__(self, parent):
        """
        Initializing method for Goto dialog.

        :param parent: QsciScintilla (must)
        """

        # Super the class to the parent.
        super().__init__(parent)

        # Defining variables...
        self.__parent = parent

        # Settings window configures.
        self.setWindowTitle("Goto - Txter")
        self.setWindowModality(Qt.WindowModality.WindowModal)

        # Setting layouts and widgets...
        self.__layout = QVBoxLayout()

        self.__line_entry_layout = QFormLayout()

        self.__line_number_label = QLabel()
        self.__line_number_label.setText("&Line: ")
        self.__line_number_entry = QLineEdit()
        self.__line_number_entry.setPlaceholderText("Enter line number")
        self.__line_number_label.setBuddy(self.__find_entry)
        self.__line_entry_layout.addRow(self.__line_number_label, self.__line_number_entry)

        self.__layout.addLayout(self.__line_entry_layout)

        self.__box = QDialogButtonBox()
        self.__ok = QPushButton()
        self.__ok.setText("&Go")
        self.__ok.clicked.connect(self.___inner_slot_goto)
        self.__box.addButton(self.__ok, QDialogButtonBox.AcceptRole)
        self.__cancel = QPushButton()
        self.__cancel.setText("&Cancel")
        self.__cancel.clicked.connect(self.close)
        self.__box.addButton(self.__cancel, QDialogButtonBox.RejectRole)

        self.__layout.addWidget(self.__box)

        self.setLayout(self.__layout)

    def ___inner_slot_goto(self):
        """
        Goto a line number

        :return: None
        """

        try:
            # Exception handling.

            self.__parent.setCursorPosition(int(self.__line_number_entry.text()) - 1, 0)

            if int(self.__find_entry.text()) > len(self.__parent.text().split("\n")):

                raise ValueError(f"The line numbered {self.__line_number_entry.text()} is overflowed.")

            self.close()

        except Exception as exc:
            # Except any exception

            # then create a message box to report it.

            msg = QMessageBox(self)
            msg.setWindowModality(Qt.WindowModal)
            msg.setWindowTitle("Error")
            msg.setText(f"Cannot goto that line. Reason: {str(exc)}")
            msg.setInformativeText("Txter cannot goto that line.")
            msg.setDetailedText(traceback.format_exc())

            # Execute the message box.
            msg.exec()
