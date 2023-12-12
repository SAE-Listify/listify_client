from . import task as ts

from PyQt5.QtWidgets import (
    QLabel,
    QFrame,
    QPushButton,
    QVBoxLayout,
    QInputDialog,
)

from PyQt5.QtCore import (
    Qt,
)


class Repository(QFrame):
    """
    Repository

    Project => Repository => Task => Subtask
    """

    def __init__(self, name_rep: str = "Repertoire", task_list=None):
        """
        creates the ui elements, passing a task list is optional
        :param name_rep: str
        :param task_list: list of tasks
        """
        super().__init__()
        if task_list is None:  # create an empty list if none is given
            task_list = []
        self.__name_rep = name_rep
        self.__task_list = task_list

        self.setFrameStyle(QFrame.StyledPanel)
        self.setFixedWidth(400)

        # creating a widget (to return) and set layout
        self.__layout = QVBoxLayout()
        self.__layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.__layout)

        self.__repo_label = QLabel(self.__name_rep)
        # TOD : Change name of repo on dbl click
        # self.__repo_label.mouseDoubleClickEvent()
        self.__layout.addWidget(self.__repo_label)

        self.__create_task_button = QPushButton("Créer une tâche")
        self.__create_task_button.clicked.connect(
            lambda: self.create_task()
        )
        self.__layout.addWidget(self.__create_task_button)

        if self.__task_list:
            for task_widget in self.__task_list:
                self.__layout.addWidget(task_widget)

    def __str__(self):
        """
        str to print the title in the project
        :return: name of project
        """
        return f"{self.__name_rep}"

    def create_task(self, name_task: str = "Tache"):  #
        """
        create a task with the file task.py
        :param name_task:
        :return:
        """
        name_task, ok = QInputDialog.getText(self, 'Nom de la tache', 'Entrez le nom de la tache:')
        if not ok:
            return  # exit if the user cancel
        created_task = ts.Task(name_task)
        self.__task_list.append(created_task)  # create the object in the list
        self.__layout.addWidget(created_task)

    def delete_task(self, num: int):
        """
        delete the "num"th task
        """
        del self.__task_list[num]

    def to_dict(self):
        """
        exports the repo to a dictionary for json serialization,
        called by the repo parent,
        it calls its children to_dict() methods
        :return: dict of the repo
        """
        task_dicts = []
        for task in self.__task_list:
            task_dicts.append(task.to_dict())

        return {
            "name": self.__name_rep,
            "tasks": task_dicts,
        }

    @property
    def name_rep(self):
        """
        returns the name of the repo
        :return: name of the repo
        """
        return self.__name_rep

    @name_rep.setter
    def name_rep(self, name_rep):
        """
        sets the name of the repo
        :param name_rep: str
        :return:
        """
        self.__name_rep = name_rep

    @property
    def task_list(self):
        """
        returns the list of tasks
        :return: task list
        """
        return self.__task_list

    @task_list.setter
    def task_list(self, task_list):
        """
        set the list of tasks
        :param task_list: list
        :return:
        """
        self.__task_list = task_list
