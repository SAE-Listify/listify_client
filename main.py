import logging
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QMessageBox,
    QTabWidget,
    QTextBrowser,
    QHBoxLayout,
    QMessageBox,
)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont, QCloseEvent

import ui_objects

DEBUG = True

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.WARNING)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Listify")
        self.setMinimumSize(1000, 500)
        self.mainWidget = Listify(self)
        self.setCentralWidget(self.mainWidget)
        self.show()

    def closeEvent(self, _e: QCloseEvent):
        QCoreApplication.exit(0)


class Listify(QWidget):
    def __init__(self, parent: MainWindow):
        super(QWidget, self).__init__()
        self.parent = parent
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)

        self.tabs = []
        self.tabWidget = QTabWidget()
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(False)  # to test, breaks closing ???
        self.tabWidget.tabCloseRequested.connect(self.__closeTab)

        self.__projects = []
        self.new_project("test1")
        self.new_project("tEsT2")

        # we need to load/create projects before loading the sidebar
        self.sidebarWidget = ui_objects.Sidebar(parent=self)
        # Add widgets to the main Listify Widget here
        # row: int, column: int, rowSpan: int, columnSpan: int
        self.layout.addWidget(self.sidebarWidget, 0, 0)
        self.layout.addWidget(self.tabWidget, 0, 1)

    def __openTab(self, project: ui_objects.Project):
        self.tabs.append(
            {
                "widget": QWidget(),
                "project": project,
                "label_test": QLabel("placeholder"),
                "button_test": QPushButton("placeholder"),
            }
        )
        current_tab = self.tabs[-1]

        self.tabWidget.addTab(current_tab["widget"], current_tab["project"].name_project)

        # CREATING LAYOUTS
        current_tab["widget"].__layout = QGridLayout()

        # SETTING LAYOUTS TODO is using .layout necessary??
        current_tab["widget"].setLayout(current_tab["widget"].__layout)

        # CREATING WIDGETS
        # row: int, column: int, rowSpan: int, columnSpan: int
        ### TESTING
        # current_tab["widget"].__layout.addWidget(current_tab["label_test"], 0, 0, 1, 1)
        # current_tab["widget"].__layout.addWidget(current_tab["button_test"], 1, 0, 1, 1)
        #
        # # SETTING
        # current_tab["label_test"].setText(f"project= {current_tab['project'].name_project}")

        current_tab["widget"].__layout.addWidget(current_tab["project"], 0, 0, 1, 1)

    def open_tab_by_project_index(self, index: int):
        if index <= len(self.__projects):
            self.__openTab(self.__projects[index])

    """
    Executed when a tab is closed by the user, takes the index as its argument
    """

    def __closeTab(self, index: int):
        logging.info(f"Closing Tab index {index}")

        self.tabs.pop(index)
        self.tabWidget.removeTab(index)
        logging.debug(f"tabs[] = {self.tabs}")

    """
    Create a new project
    """

    def new_project(self, name):
        new_project = ui_objects.Project(name_project=name)
        self.__projects.append(new_project)
        self.__openTab(self.__projects[-1])
        logging.info(f"new project created: {name}")
        logging.debug(f"projects: {self.__projects}")

    """
    Set the specified tab index
    """

    def goto_last_tab(self):
        self.tabWidget.setCurrentIndex(len(self.tabs) - 1)

    """
    Get projects list for sidebar
    """

    @property
    def projects(self):
        return self.__projects

    """
    Get opened projects
    """

    @property
    def opened_projects(self):
        opened_projects = []
        if self.tabs:
            for tab in self.tabs:
                opened_projects.append(tab["project"])
            return opened_projects
        else:
            return []

    def goto_tab(self, index: int):
        if 0 <= index < self.tabWidget.count():
            self.tabWidget.setCurrentIndex(index)
        else:
            logging.warning("attemped to go to tab index which is out of bounds.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
