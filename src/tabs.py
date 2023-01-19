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


File Name:                              tabs.py

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

# Python builtins
import sys


class TabWidget(QTabWidget):
    """
    A tabbed widget which allows Multiple-Document Interface (MDI).
    """

    def __init__(self, parent=None):
        """
        Initializing method for the Tab Widget.

        :param parent: QWidget | None
        """

        # Super the class to the parent.
        super().__init__(parent)

        # Set document mode. Will be beautiful when it works on macOS.
        self.setDocumentMode(True)
        # Set elide mode "...".
        self.setElideMode(Qt.TextElideMode.ElideRight)
        # Set if the tabs are closable. Default is False. I toggled it.
        self.setTabsClosable(True)
        # Set if the scroll buttons are on-duty.
        self.setUsesScrollButtons(True)


if __name__ == "__main__":
    # Try the tabs.

    # Constructing the QApplication.
    app = QApplication(sys.argv)

    # Constructing the tab widget.
    tabs = TabWidget()

    # Adding a tab.
    tabs.addTab(QWidget(), "Testing")

    # Show the tab widget.
    tabs.show()

    # Execute the application, and exit-after-close.
    sys.exit(app.exec_())
