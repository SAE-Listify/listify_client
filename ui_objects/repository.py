from . import task as ts

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLabel,
    QFrame,
    QLineEdit,
    QPushButton,
    QComboBox,
    QMessageBox,
    QTabWidget,
    QTextBrowser,
    QHBoxLayout,
    QVBoxLayout,
    QMessageBox,
)

from PyQt5.QtCore import (
    Qt,
)

class Repository(QFrame):
    def __init__(self, name_rep: str = "Repertoire", task_list=None):  # variable init
        super(QFrame, self).__init__()
        if task_list is None:  # create an empty list if none is given
            task_list = []
        self.__name_rep = name_rep
        self.__task_list = task_list

        self.setFrameStyle(QFrame.StyledPanel)

        # creating a widget (to return) and set layout
        self.__layout = QVBoxLayout()
        self.__layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.__layout)

        self.__repo_label = QLabel(self.__name_rep)
        self.__layout.addWidget(self.__repo_label)

        self.__create_task_button = QPushButton("Créer une tâche")
        self.__create_task_button.clicked.connect(
            lambda: self.create_task("task_test")
        )
        self.__layout.addWidget(self.__create_task_button)

        if self.__task_list:
            for task_widget in self.__task_list:
                self.__layout.addWidget(task_widget)

    def __str__(self):  # str to print the title in the project
        return f"{self.__name_rep}"

    def create_task(self, name_task: str = "Tache"):  # crawte a task with the file task.py
        created_task = ts.Task(name_task)
        self.__task_list.append(created_task)  # create the object in the list
        self.__layout.addWidget(created_task)

    def delete_task(self, num: int):
        del self.__task_list[num]

    def changename_rep(self, new_name):  # change the name
        self.__name_rep = new_name

    def to_dict(self):  # repo
        task_dicts = []
        for task in self.__task_list:
            task_dicts.append(task.to_dict())

        return {
            "name": self.__name_rep,
            "tasks": task_dicts,
        }



    @property
    def name_rep(self):
        return self.__name_rep

    @name_rep.setter
    def name_rep(self, name_rep):
        self.__name_rep = name_rep

    @property
    def task_list(self):
        return self.__task_list

    @task_list.setter
    def task_list(self, task_list):
        self.__task_list = task_list
