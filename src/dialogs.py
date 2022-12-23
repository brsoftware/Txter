"""

"""


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qsci import *
from PyQt5.QtPrintSupport import QPrintDialog

import traceback


class PrintDialog(QPrintDialog):
    def __init__(self, printer, parent):
        super().__init__(printer, parent)

        self.setWindowTitle("Print - Txter")
        self.setWindowModality(Qt.WindowModality.WindowModal)


class FindDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.__parent = parent

        self.setWindowTitle("Find - Txter")
        self.setWindowModality(Qt.WindowModality.WindowModal)

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
        self.__parent.findFirst(self.__find_entry.text(), True, True, True, True, True)


class ReplaceDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.__parent = parent

        self.setWindowTitle("Replace - Txter")
        self.setWindowModality(Qt.WindowModality.WindowModal)

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
        self.__parent.findFirst(self.__find_entry.text(), True, True, True, True, True)
        self.__parent.replace(self.__replace_entry.text())

    def ___inner_slot_replace_all(self):
        self.__parent.beginUndoAction()
        while self.__parent.findFirst(self.__find_entry.text(), True, True, True, True, True):
            self.__parent.replace(self.__replace_entry.text())
        self.__parent.endUndoAction()


class GotoDialog(QDialog):
    def __init__(self, parent=QsciScintilla):
        super().__init__(parent)

        self.__parent = parent

        self.setWindowTitle("Goto - Txter")
        self.setWindowModality(Qt.WindowModality.WindowModal)

        self.__layout = QVBoxLayout()

        self.__find_layout = QFormLayout()

        self.__find_label = QLabel()
        self.__find_label.setText("&Line: ")
        self.__find_entry = QLineEdit()
        self.__find_entry.setPlaceholderText("Enter line number")
        self.__find_label.setBuddy(self.__find_entry)
        self.__find_layout.addRow(self.__find_label, self.__find_entry)

        self.__layout.addLayout(self.__find_layout)

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
        try:
            self.__parent.setCursorPosition(int(self.__find_entry.text()) - 1, 0)
            if int(self.__find_entry.text()) > len(self.__parent.text().split("\n")):
                raise ValueError(f"The line numbered {self.__find_entry.text()} is overflowed.")
            self.close()
        except Exception as exc:
            msg = QMessageBox(self)
            msg.setWindowModality(Qt.WindowModal)
            msg.setWindowTitle("Error")
            msg.setText(f"Cannot goto that line. Reason: {str(exc)}")
            msg.setInformativeText("Txter cannot goto that line.")
            msg.setDetailedText(traceback.format_exc())
            msg.exec()
