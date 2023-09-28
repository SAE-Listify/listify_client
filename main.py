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


class Tab(QWidget):
    def __init__(self, parent: MainWindow):
        super(QWidget, self).__init__()
        self.parent = parent
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
