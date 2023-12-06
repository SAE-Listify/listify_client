from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)


class Subtask(QWidget):
    def __init__(self, name_subtask: str = 'Sous-Tâche'):  # variable init
        super(QWidget, self).__init__()
        self.__name_subtask = name_subtask

        # creating a widget (to return) and set layout
        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)
        self.__subtask_label = QLabel(self.__name_subtask)

        self.__layout.addWidget(self.__subtask_label)

    def __str__(self):  # str to print the tittle in the project
        return f"{self.__name_subtask}"

    def to_dict(self):  # subtask
        return {
            "name": self.__name_subtask,
        }

    def changename_subtask(self, new_name):
        self.__name_subtask = new_name

    @property
    def name_subtask(self):
        return self.__name_subtask

    @name_subtask.setter
    def name_subtask(self, name_subtask):
        self.__name_subtask = name_subtask
