import logging
import sys
import sidebar #importing the sidebar.py :)
#Main.py is working, i'm gonna focus on the side bar now

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit,
    QPushButton, QComboBox, QMessageBox, QTabWidget, QTextBrowser,
    QHBoxLayout, QVBoxLayout, QFrame, QListWidget, QStackedLayout, QTextEdit
)
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QFont, QCloseEvent, QPixmap, QIcon # Ensure QIcon is here

DEBUG = True

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.WARNING)
class TaskListWidget(QWidget):
    def __init__(self, parent=None):
        super(TaskListWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)

        # Task input field
        self.taskInput = QTextEdit(self)
        self.layout.addWidget(self.taskInput)

        # Add task button
        self.addTaskButton = QPushButton("Add Task", self)
        self.addTaskButton.clicked.connect(self.add_task)
        self.layout.addWidget(self.addTaskButton)

        # List for tasks
        self.taskList = QListWidget(self)
        self.layout.addWidget(self.taskList)

        # Delete task button
        self.deleteTaskButton = QPushButton("Delete Task", self)
        self.deleteTaskButton.clicked.connect(self.delete_task)
        self.layout.addWidget(self.deleteTaskButton)

    def add_task(self):
        task = self.taskInput.toPlainText().strip()
        if task:
            self.taskList.addItem(task)
            self.taskInput.clear()

    def delete_task(self):
        # Remove the currently selected task
        current_item = self.taskList.currentItem()
        if current_item:
            row = self.taskList.row(current_item)
            self.taskList.takeItem(row)

class Listify(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window properties
        self.setWindowTitle("Listify - ToDo App")
        self.setGeometry(100, 100, 800, 600)  # x, y, z, moment

        # Create main layout
        main_layout = QHBoxLayout()

        # Sidebar
        self.sidebar = sidebar.Sidebar(self)
        main_layout.addWidget(self.sidebar)

        # Content frame
        self.contentFrame = QFrame(self)
        self.contentFrame.setFrameShape(QFrame.StyledPanel)
        main_layout.addWidget(self.contentFrame)

        # Placeholder
        self.contentLayout = QStackedLayout(self.contentFrame)

        # Create the TaskListWidget
        self.taskListWidget = TaskListWidget(self.contentFrame)
        self.contentLayout.addWidget(self.taskListWidget)
        self.contentLayout.setCurrentWidget(self.taskListWidget)

        # Set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication([])
    window = Listify()
    window.show()
    app.exec_()
