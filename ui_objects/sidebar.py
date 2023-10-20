from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Sidebar(QWidget):
    def __init__(self, parent: QWidget = None):
        self.parent = parent
        super(Sidebar, self).__init__(self.parent)

        self.setFixedWidth(150)  # Width of the sidebar

        self.__layout = QVBoxLayout(self)

        # init a list of buttons for project, we will add
        self.__projects_buttons = []

        self.__setup_projects()

    def __setup_projects(self):
        # Create button
        create_button = QPushButton("Create", self)
        create_button.clicked.connect(self.__create_project)  # Connect to a method to handle project creation
        self.__layout.addWidget(create_button)

        # Text box for project name
        self.project_name_textbox = QLineEdit(self)
        self.project_name_textbox.setPlaceholderText("Enter project name")
        self.__layout.addWidget(self.project_name_textbox)

    def __create_project(self):
        project_name = self.project_name_textbox.text()

        if not project_name:  # Check if the project name is not empty
            QMessageBox.warning(self, "Warning", "Project name cannot be empty!")
            return

        project_button = QPushButton(project_name, self)
        project_button.clicked.connect(self.__open_project)

        self.__projects_buttons.append(project_button)
        self.__layout.addWidget(project_button)
        pass

    def __open_project(self, index: int):
        # Identify which button was clicked
        clicked_button = self.sender()
        index = self.__projects_buttons.index(clicked_button)
        self.__switch_to_project_tab(index)
        pass

    def __switch_to_project_tab(self, index: int):
        # Switch to the tab
        self.parent.project_tab_widget.setCurrentIndex(index)
        pass
