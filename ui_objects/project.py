from . import repository as repo

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,

)
from PyQt5.QtCore import Qt

class Project(QWidget):
    """
    Project

    Project => Repository => Task => Subtask
    """
    def __init__(self, name_project: str = 'Project', repository_list: list = None):  # variable init
        super().__init__()

        if repository_list is None:  # creation of an empty list if none is given
            repository_list = []
        self.__name_project = name_project
        self.__repository_list = repository_list

        # Creating layouts and widgets
        self.__layout = QVBoxLayout()
        self.__layout .setAlignment(Qt.AlignTop)
        self.setLayout(self.__layout)

        self.__layout_repo = QHBoxLayout()
        self.__layout_repo.setAlignment(Qt.AlignLeft)


        self.__project_label = QLabel(self.__name_project)

        self.__create_repo_button = QPushButton("Créer un repository")
        self.__create_repo_button.clicked.connect(
            lambda: self.create_repository("repo_test")
        )

        # adding the button and the repos layout to the main project layout
        self.__layout.addWidget(self.__create_repo_button)
        self.__layout.addLayout(self.__layout_repo)

        if self.__repository_list:
            for repo_widget in self.__repository_list:
                self.__layout_repo.addWidget(repo_widget)

    def __str__(self):  # str to print the tittle in the project
        return f"{self.__name_project}"

    def create_repository(self, name_repository):  # crate a repository with the file task.py
        repo_created = repo.Repository(f"{name_repository}")
        self.__repository_list.append(repo_created)  # create the object in the list
        self.__layout_repo.addWidget(repo_created)

    def delete_repository(self, num: int):  # delete the repository from the project
        del self.__repository_list[num]

    def changename_proj(self, new_name):  # change the name
        self.__name_project = new_name

    def to_dict(self, name_base="data"):  # project
        repo_dicts = []

        for repo in self.__repository_list:
            repo_dicts.append(repo.to_dict())

        return {
            "name_project": self.__name_project,
            "repositories": repo_dicts,
        }

    @property
    def name_project(self):
        return self.__name_project

    @name_project.setter
    def name_project(self, name_project):
        self.__name_project = name_project

    @property
    def repository_list(self):
        return self.__repository_list

    @repository_list.setter
    def repository_list(self, repository_list):
        self.__repository_list = repository_list