import logging
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLabel,
    QPushButton,
    QTabWidget,
)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QCloseEvent

import ui_objects

DEBUG = True

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.WARNING)


class MainWindow(QMainWindow):
    """
    Listify main window

    Used to initialize the Listify QWidget
    """

    def __init__(self) -> None:
        """
        Sets the Listify widget as the mainWidget of the window.
        """
        super().__init__()
        self.setWindowTitle("Listify")
        self.setMinimumSize(1000, 500)
        self.mainWidget = Listify(self)
        self.setCentralWidget(self.mainWidget)
        self.show()

    def closeEvent(self, _e: QCloseEvent):
        """
        closes the listify window
        :param _e:
        :return:
        """
        QCoreApplication.exit(0)


class Listify(QWidget):
    """
    Main Listify QWidget

    It handles the list of projects, the opening of new projects.
    It also create the QTabWidget and the Sidebar (sidebar.py).
    """

    def __init__(self, parent: MainWindow):
        """
        The __init__ method creates the main Listify widgets and add them to the Main Window
        :param parent:
        """
        super().__init__()
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
        """
        __openTab() takes a project as an argument and opens it in a new tab
        :param project: ui_objects.Project
        :return:
        """
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
        """
        Used by the sidebar to open a tab by its index in the list
        :param index: int
        :return:
        """
        if index <= len(self.__projects):
            self.__openTab(self.__projects[index])

    def __closeTab(self, index: int):
        """
        Executed when a tab is closed by the user, takes the index as its argument
        """
        logging.info(f"Closing Tab index {index}")

        self.tabs.pop(index)
        self.tabWidget.removeTab(index)
        logging.debug(f"tabs[] = {self.tabs}")

    def new_project(self, name):
        """
        Create a new project
        """
        new_project = ui_objects.Project(name_project=name)
        self.__projects.append(new_project)
        self.__openTab(self.__projects[-1])
        logging.info(f"new project created: {name}")
        logging.debug(f"projects: {self.__projects}")

    def delete_project_by_index(self, index: int):
        if index < len(self.__projects):
            if self.__projects[index] in self.opened_projects:
                self.tabWidget.removeTab(self.opened_projects.index(self.__projects[index]))

            self.__projects.pop(index)
            logging.debug(f"deleted project index {index}")

    def goto_last_tab(self):
        """
        Show the last tab, used on project creation by the sidebar
        """
        self.tabWidget.setCurrentIndex(len(self.tabs) - 1)

    @property
    def projects(self):
        """
        Get projects list for sidebar
        """
        return self.__projects

    @property
    def opened_projects(self):
        """
        Get opened projects for sidebar (to either switch to the tab or open the project)
        """
        opened_projects = []
        if self.tabs:
            for tab in self.tabs:
                opened_projects.append(tab["project"])
            return opened_projects
        else:
            return []

    def goto_tab(self, index: int):
        """
        Goto the tab at the given index
        :param index: int
        :return:
        """
        if 0 <= index < self.tabWidget.count():
            self.tabWidget.setCurrentIndex(index)
        else:
            logging.warning("attempted to go to tab index which is out of bounds.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
