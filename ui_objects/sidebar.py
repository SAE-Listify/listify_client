from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QMessageBox

class Sidebar(QWidget):
    def __init__(self, parent: QWidget = None):
        self.parent = parent
        super(Sidebar, self).__init__(self.parent)
        self.setFixedWidth(150)
        self.__layout = QVBoxLayout(self)

        self.__projects_layouts = []    # List to store QHBoxLayouts
        self.__projects_open_buttons = []  # List to store project buttons
        self.__projects_delete_buttons = []    # List to store delete buttons

        # Add create button and text box for project name
        create_button = QPushButton("Créer un projet", self)
        create_button.clicked.connect(self.__create_project)
        self.__layout.addWidget(create_button)
        self.project_name_textbox = QLineEdit(self)
        self.project_name_textbox.setPlaceholderText("Nom du projet")
        self.__layout.addWidget(self.project_name_textbox)

        # Load projects
        self.__load_projects()

    """
    This method creates the UI elements present on the sidebar for each project
    """
    def __init_project_list_ui_elements(self, project_name):
        project_hbox = QHBoxLayout()

        # Open Button
        project_button = QPushButton(project_name, self)
        project_button.clicked.connect(self.__open_project)
        project_hbox.addWidget(project_button)

        # Delete Button
        delete_button = QPushButton('X', self)
        delete_button.setFixedSize(20, 20)
        delete_button.clicked.connect(self.__delete_project)
        project_hbox.addWidget(delete_button)

        # maybe work on using dict
        self.__projects_open_buttons.append(project_button)
        self.__projects_delete_buttons.append(delete_button)
        self.__projects_layouts.append(project_hbox)
        self.__layout.addLayout(project_hbox)

    """
    This methods loads projects available in the main Listify class 
    """
    def __load_projects(self):
        for proj in self.parent.projects:
            self.__init_project_list_ui_elements(proj.name_project)

    """
    This method create the project, connected to "create_button"
    """
    def __create_project(self):
        # Create new project button and its associated delete button
        project_name = self.project_name_textbox.text()
        if not project_name:
            QMessageBox.warning(self, "Erreur", "Veuillez choisir un nom!")
            return

        self.__init_project_list_ui_elements(project_name)

        # Create the project using the parent (Listify class in main.py) method
        self.parent.new_project(project_name)

    def __delete_project(self):
        # Remove the project button and its associated delete button
        clicked_button = self.sender()  # Returns the button object of the clicked button
        index = self.__projects_delete_buttons.index(clicked_button)

        # first pop the objects from the lists, then properly delete them
        open_button_to_remove = self.__projects_open_buttons.pop(index)
        delete_button_to_remove = self.__projects_delete_buttons.pop(index)
        layout_to_remove = self.__projects_layouts.pop(index)
        open_button_to_remove.deleteLater()
        delete_button_to_remove.deleteLater()
        layout_to_remove.deleteLater()

    def __open_project(self):
        # Switch to the clicked project tab
        clicked_button = self.sender()
        index = self.__projects_open_buttons.index(clicked_button)
        if self.parent.projects[index] in self.parent.opened_projects:
            self.__switch_to_project_tab(index)
        else:
            self.parent.open_tab_by_project_index(index)

    def __switch_to_project_tab(self, index: int):
        # todo make the logic for later, quite complicated gonna need help for this one
        self.parent.goto_tab_index(index)
