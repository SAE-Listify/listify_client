from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QCheckBox,
)
from PyQt5.QtCore import Qt


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
        self.__layout = QHBoxLayout()
        self.__layout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.__layout)

        self.__subtask_label = QLabel(self.__name_subtask)

        # Check box to check if the subtask is done
        self.__checkbox = QCheckBox("")
        self.__checkbox.stateChanged.connect(self.__subtask_label.setDisabled)

        # Adding widgets to the layout
        self.__layout.addWidget(self.__checkbox)
        self.__layout.addWidget(self.__subtask_label)

        #Check the subtask state PROVISOIRE
        if self.__checkbox.isChecked():
            subtaskstate = True
        else:
            subtaskstate = False



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
            "state": self.__checkbox.isChecked(),
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
