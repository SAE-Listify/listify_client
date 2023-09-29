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

DEBUG = True

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.WARNING)


# mainwindow class ouvre une tab de 1000x500 nommée Listify
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Listify")
        self.setMinimumSize(1000, 500)
        self.tab = Tab(self)
        self.setCentralWidget(self.tab)
        self.show()
    def closeEvent(self, _e: QCloseEvent):
        QCoreApplication.exit(0)

#Tab class est la tab ouverte par mainwindow
class Tab(QWidget):
    def __init__(self, parent: MainWindow):
        super(QWidget, self).__init__()
        self.parent = parent
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)

        self.mainBackground = Tab.main_bg()
        self.layout.addWidget(self.mainBackground)

        # Create Tab Widget
        self.tabWidget = QTabWidget()

        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.tabCloseRequested.connect(self.__closeTab)

        self.tabs = []

        self.layout.addWidget(self.tabWidget)

        # Open test tab
        self.__openTab("Projet Test")
        self.__openTab("Projet Test2")

    def __openTab(self, name: str):
        self.tabs.append(
            {
                "widget": QWidget(),
                "label_test": QLabel("placeholder"),
                "button_test": QPushButton("placeholder"),
            }
        )

        current_tab = self.tabs[-1]

        # ADDING TAB TO TAB WIDGET

        self.tabWidget.addTab(current_tab["widget"], name)

        # CREATING LAYOUTS
        current_tab["widget"].layout = QGridLayout()

        # SETTING LAYOUTS TODO is using .layout necessary??
        current_tab["widget"].setLayout(current_tab["widget"].layout)

        # CREATING WIDGETS
        # row: int, column: int, rowSpan: int, columnSpan: int
        ### TESTING
        current_tab["widget"].layout.addWidget(current_tab["label_test"], 0, 0, 1, 1)
        current_tab["widget"].layout.addWidget(current_tab["button_test"], 1, 0, 1, 1)



        # SETTING
        current_tab["label_test"].setText(f"Test {len(self.tabs)}")


    """
    Executed when a tab is closed by the user, takes the index as its argument
    """
    def __closeTab(self, index: int):
        logging.info(f"Closing Tab index {index}")

        self.tabs.pop(index)
        self.tabWidget.removeTab(index)

    # main_bg class est le background de la tab de la sidebar
    class main_bg(QWidget):
        def __init__(self):
            super().__init__()

            self.layout = QGridLayout()
            self.setLayout(self.layout)

            self.side_panel = QLabel("Side Panel")
            self.button_createProject = QPushButton("Create Project")
            self.button_display = QPushButton("Display")
            self.button_delete = QPushButton("Delete")

            self.layout.addWidget(self.side_panel, 0, 0, 4, 1)

            self.layout.addWidget(self.button_createProject, 0, 1)
            self.layout.addWidget(self.button_display, 1, 1)
            self.layout.addWidget(self.button_delete, 2, 1)
            #stretching
            self.layout.setColumnStretch(2, 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()