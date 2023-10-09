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


class sidebar(QWidget):
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

