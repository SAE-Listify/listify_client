from . import repository as repo

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QScrollArea,
    QInputDialog,
)
from PyQt5.QtCore import Qt


class Project(QWidget):
    """
    Project

    Project => Repository => Task => Subtask
    """

    def __init__(self, name_project: str = 'Project', repository_list: list = None):  # variable init
        """
        Creates the ui objects, passing a repo list is optional
        :param name_project: str
        :param repository_list: list
        """
        super().__init__()

        if repository_list is None:  # creation of an empty list if none is given
            repository_list = []
        self.__name_project = name_project
        self.__repository_list = repository_list

        # Creating layouts and widgets
        self.__layout = QVBoxLayout()
        self.__layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.__layout)

        # creating a widget & its layout to put in QScrollArea for the repos
        self.__layout_repo = QHBoxLayout()
        self.__layout_repo.setAlignment(Qt.AlignLeft)   # do not center the repos
        self.__scrollable_widget = QWidget()
        self.__scrollable_widget.setLayout(self.__layout_repo)

        # creating the QScrollArea
        self.__scroll_area = QScrollArea()
        self.__scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.__scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.__scroll_area.setWidgetResizable(True)
        self.__scroll_area.setWidget(self.__scrollable_widget)

        self.__create_repo_button = QPushButton("Créer un repository")
        self.__create_repo_button.clicked.connect(self.__create_repository_popup)

        # Delete button for the repository
        self.__delete_button = QPushButton("X")
        self.__delete_button.clicked.connect(self.__delete_repository)

        # adding the button and the repos layout to the main project layout
        self.__layout.addWidget(self.__create_repo_button)
        self.__layout.addWidget(self.__scroll_area)

        if self.__repository_list:
            for repo_widget in self.__repository_list:
                self.__layout_repo.addWidget(repo_widget)

    def __str__(self):
        """
        str to print the title in the project
        :return: name of the project
        """
        return f"{self.__name_project}"

    def __create_repository_popup(self):
        """
        Creates the popup to choose a name for new repository
        :return:
        """
        name_repository, ok = QInputDialog.getText(self, 'Nom du repository', 'Entrez le nom du repository:')
        if not ok:
            return  # exit if the user cancel

        # Set repo name to a placeholder if user input is empty
        if name_repository == "":
            name_repository = "Repertoire"

        self.create_repository(name_repository)

    def create_repository(self, name_repository):
        """
        create a repository
        :param name_repository: str
        :return:
        """
        repo_created = repo.Repository(self, name_repository)
        self.__repository_list.append(repo_created)  # create the object in the list
        self.__layout_repo.addWidget(repo_created)

    def delete_repository(self, num: int):
        """
        delete the "num"th repository from the project
        :param num:
        :return:
        """
        repo.deleteLater()
        self.repository_list.remove(repo)
        logging.debug(f"Deleted repository {repo} / Remaining repositories: {len(self.repository_list)}")

    def to_dict(self):
        """
        exports the project to a dictionary for json serialization,
        it calls its children to_dict() methods
        :return: dict of the project
        """
        repo_dicts = []

        for repo in self.__repository_list:
            repo_dicts.append(repo.to_dict())

        return {
            "name_project": self.__name_project,
            "repositories": repo_dicts,
        }

    @property
    def name_project(self):
        """
        returns the name of the project
        :return: name of the project
        """
        return self.__name_project

    @name_project.setter
    def name_project(self, name_project):
        """
        sets the name of the project
        :param name_project: str
        :return:
        """
        self.__name_project = name_project

    @property
    def repository_list(self):
        """
        returns the list of repositories
        :return: list of repos
        """
        return self.__repository_list

    @repository_list.setter
    def repository_list(self, repository_list):
        """
        sets the list of repositories
        :param repository_list:
        :return:
        """
        self.__repository_list = repository_list
