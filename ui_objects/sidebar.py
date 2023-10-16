from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
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

        ## something that could maybe work:
        # for index, project in zip(self.parent.projects):
        #     # Project buttons
        #     self.__projects_buttons.append(QPushButton(project.name_project))
        #
        #     self.__projects_buttons[-1].clicked.connect(
        #         lambda: self.__open_project(index)
        #     )
        #
        #     self.layout.addWidget(self.__projects_buttons[-1])

    def __create_project(self):
        # Logic to handle project creation
        pass

    def __open_project(self, index: int):
        # Logic to open Project "index"
        pass
