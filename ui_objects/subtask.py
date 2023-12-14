from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QCheckBox,
    QPushButton,
    QInputDialog,
)
from PyQt5.QtCore import Qt


class Subtask(QWidget):
    """
    Subtask

    Project => Repository => Task => Subtask
    """

    def __init__(
            self,
            parent,
            name_subtask: str = 'Sous-Tâche',
            is_done: bool = False
    ):
        """
        creates the ui elements
        :param name_subtask:
        """
        super().__init__()
        self.__parent = parent
        self.__name_subtask = name_subtask
        self.__is_done = is_done

        # creating a widget (to return) and set layout
        self.__layout = QHBoxLayout()
        self.__layout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.__layout)

        self.__subtask_label = QLabel(self.__name_subtask)

        # Check box to check if the subtask is done
        self.__checkbox = QCheckBox("")
        self.__checkbox.stateChanged.connect(self.__on_checkbox_state_changed)
        # Check the subtask state
        self.__checkbox.setChecked(self.__is_done)

        # Rename button
        self.__rename_button = QPushButton("Renommer")
        self.__rename_button.clicked.connect(self.open_rename_window)

        # Rename button
        self.__rename_button = QPushButton("X")
        self.__rename_button.clicked.connect(self.__delete_self)

        # Adding widgets to the layout
        self.__layout.addWidget(self.__checkbox)
        self.__layout.addWidget(self.__subtask_label)
        self.__layout.addWidget(self.__rename_button, alignment=Qt.AlignRight)

    def __str__(self):
        """
        str to print the title of the subtask
        :return: str title of the subtask
        """
        return f"{self.__name_subtask}"

    def __on_checkbox_state_changed(self):
        """
        Executed on checkbox state change
        :return:
        """
        if self.__checkbox.isChecked():
            self.__subtask_label.setDisabled(True)
            self.__is_done = True
        else:
            self.__subtask_label.setDisabled(False)
            self.__is_done = False

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

    def __delete_self(self):
        self.__parent.delete_subtask(self)

    def to_dict(self):
        """
        exports the subtask to a dictionary for json serialization,
        called by the subtask's parent,
        :return: dict of the project
        """
        return {
            "name": self.__name_subtask,
            "is_done": self.__is_done,
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

    @property
    def is_done(self):
        return self.__is_done

    @is_done.setter
    def is_done(self, is_done):
        self.__is_done = is_done
        self.__checkbox.setChecked(is_done)
        self.__on_checkbox_state_changed()
