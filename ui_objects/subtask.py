from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QCheckBox,
    QPushButton,
    QInputDialog,
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

        # Check box to check if the subtask is done
        self.__checkbox = QCheckBox("Sous-tâche terminée")
        self.__checkbox.stateChanged.connect(self.__subtask_label.setDisabled)
        self.__layout.addWidget(self.__checkbox)

        # Check the subtask state PROVISOIRE
        if self.__checkbox.isChecked():
            subtaskstate = True
        else:
            subtaskstate = False

        # Rename button
        self.__rename_button = QPushButton("Renommer")
        self.__rename_button.clicked.connect(self.open_rename_window)
        self.__layout.addWidget(self.__rename_button)

    def __str__(self):
        """
        str to print the title of the subtask
        :return: str title of the subtask
        """
        return f"{self.__name_subtask}"

    def open_rename_window(self):
        """
        open a window to rename the task
        :return:
        """
        new_name, ok = QInputDialog.getText(
            self, "Renommer", "Entrez le nouveau nom de la tâche"
        )
        if ok and new_name:
            self.__name_subtask = new_name
            self.__subtask_label.setText(self.__name_subtask)

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
