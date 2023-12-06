from . import subtask as sbts

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFrame,
    QGridLayout,
    QLabel,
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


class Task(QFrame):
    def __init__(self, name_task : str = 'Tache', subtask_list = None): #variable init
        super(QFrame, self).__init__()
        if subtask_list is None: #creation of an empty list if none is given
            subtask_list = []
        self.__name_task = name_task
        self.__subtask_list = subtask_list

        self.setFrameStyle(QFrame.StyledPanel)

        # creating a widget and set layout
        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)

        self.__task_label = QLabel(self.__name_task)

        self.__layout.addWidget(self.__task_label)

        self.__create_subtask_button = QPushButton("Créer une sous-tâche")
        self.__create_subtask_button.clicked.connect(
            lambda: self.create_subtask("subtask_test")
        )
        self.__layout.addWidget(self.__create_subtask_button)

        if self.__subtask_list:
            for subtask_widget in self.__subtask_list:
                self.__layout.addWidget(subtask_widget)

    def __str__(self): #str to print the tittle in the project
        return f"{self.__name_task}"

    def create_subtask(self, name_subtask: str = "Sous tache"):  # create a subtask using the subtask file
        created_subtask = sbts.Subtask(name_subtask)
        self.__subtask_list.append(created_subtask)  # create the object in the list
        self.__layout.addWidget(created_subtask)


    def delete_subtask(self, num): #delete a subtask using the subtask file
        del self.__subtask_list[num]

    def changename_task(self, new_name): #change the name of the task
        self.__name_task = new_name

    def to_dict(self):  # task
        subtask_dicts = []
        for subtask in self.__subtask_list:
            subtask_dicts.append(subtask.to_dict())

        return {
            "name": self.__name_task,
            "subtasks": subtask_dicts,
        }
    @property
    def name_task(self):
        return self.__name_task

    @name_task.setter
    def name_task(self, name_task):
        self.__name_task = name_task

    @property
    def subtask_list(self):
        return self.__subtask_list

    @subtask_list.setter
    def subtask_list(self, subtask_list):
        self.__subtask_list = subtask_list