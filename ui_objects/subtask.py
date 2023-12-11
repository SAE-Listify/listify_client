from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)


class Subtask(QWidget):
    """
    Subtask

    Project => Repository => Task => Subtask
    """

    def __init__(self, name_subtask: str = 'Sous-Tâche'):
        """
        creates the ui elements
        :param name_subtask:
        """
        super().__init__()
        self.__name_subtask = name_subtask

        # creating a widget (to return) and set layout
        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)
        self.__subtask_label = QLabel(self.__name_subtask)

        self.__layout.addWidget(self.__subtask_label)

    def __str__(self):
        """
        str to print the title of the subtask
        :return: str title of the subtask
        """
        return f"{self.__name_subtask}"

    def to_dict(self):
        """
        exports the subtask to a dictionary for json serialization,
        called by the subtask's parent,
        :return: dict of the project
        """
        return {
            "name": self.__name_subtask,
        }

    @property
    def name_subtask(self):
        """
        returns the name of the subtask
        :return: name of the subtask
        """
        return self.__name_subtask

    @name_subtask.setter
    def name_subtask(self, name_subtask):
        """
        sets the name of the subtask
        :param name_subtask:
        :return:
        """
        self.__name_subtask = name_subtask
