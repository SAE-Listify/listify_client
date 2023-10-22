from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QMessageBox

class Sidebar(QWidget):
    def __init__(self, parent: QWidget = None):
        self.parent = parent
        super(Sidebar, self).__init__(self.parent)
        self.setFixedWidth(150)
        self.__layout = QVBoxLayout(self)
        self.__projects_buttons = []  # List to store project buttons
        self.__delete_buttons = []    # List to store delete buttons
        self.__setup_projects()

    def __setup_projects(self):
        # Add create button and text box for project name
        create_button = QPushButton("Create", self)
        create_button.clicked.connect(self.__create_project)
        self.__layout.addWidget(create_button)
        self.project_name_textbox = QLineEdit(self)
        self.project_name_textbox.setPlaceholderText("Enter project name")
        self.__layout.addWidget(self.project_name_textbox)

    def __create_project(self):
        # Create new project button and its associated delete button
        project_name = self.project_name_textbox.text()
        if not project_name:
            QMessageBox.warning(self, "Warning!!!", "please enter project name ?")
            return
        project_hbox = QHBoxLayout()
        project_button = QPushButton(project_name, self)
        project_button.clicked.connect(self.__open_project)
        project_hbox.addWidget(project_button)
        delete_button = QPushButton('X', self)
        delete_button.setFixedSize(20, 20)
        delete_button.clicked.connect(self.__delete_project)
        project_hbox.addWidget(delete_button)
        self.__projects_buttons.append(project_button)
        self.__delete_buttons.append(delete_button)
        self.__layout.addLayout(project_hbox)

    def __delete_project(self):
        # Remove the project button and its associated delete button
        clicked_button = self.sender()
        index = self.__delete_buttons.index(clicked_button)
        button_to_remove = self.__projects_buttons.pop(index)
        delete_button_to_remove = self.__delete_buttons.pop(index)
        button_to_remove.deleteLater()
        delete_button_to_remove.deleteLater()

    def __open_project(self):
        # Switch to the clicked project tab
        clicked_button = self.sender()
        index = self.__projects_buttons.index(clicked_button)
        self.__switch_to_project_tab(index)

    def __switch_to_project_tab(self, index: int):
        # todo make the logic for later, quite complicated gonna need help for this one
        self.parent.project_tab_widget.setCurrentIndex(index)
