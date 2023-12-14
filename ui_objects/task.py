from . import subtask as sbts

from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
    QInputDialog,
    QSizePolicy,
)
from PyQt5.QtCore import Qt

PRIORITIES = ["Aucune", "Basse", "Moyenne", "Haute", "Urgente"]

class Task(QFrame):
    """
    Task

    Project => Repository => Task => Subtask
    """

    def __init__(self, name_task: str = 'Tache', subtask_list=None, is_done: bool = False, priority: str = "Aucune"):
        """
        create the task's ui elements, passing a subtask is optional
        :param name_task: name of task
        :param subtask_list: list of subtask
        """
        super().__init__()
        if subtask_list is None:  # creation of an empty list if none is given
            subtask_list = []
        self.__name_task = name_task
        self.__subtask_list = subtask_list
        self.__is_done = is_done
        if priority in PRIORITIES:
            self.__priority = priority
        else:
            self.__priority = "Aucune"

        self.setFrameStyle(QFrame.StyledPanel)

        # creating a widget and set layout
        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)
        self.__layout.setAlignment(Qt.AlignTop)

        self.__task_label = QLabel(self.__name_task)
        self.__task_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.__create_subtask_button = QPushButton("+")
        self.__create_subtask_button.clicked.connect(
            lambda: self.create_subtask("subtask_test")
        )

        if self.__subtask_list:
            for subtask_widget in self.__subtask_list:
                self.__layout.addWidget(subtask_widget)

        # Check box to check if the task is done
        self.__checkbox = QCheckBox("")
        self.__checkbox.stateChanged.connect(self.__on_checkbox_state_changed)

        # Priority list
        self.__priority_button = QPushButton("Priorité")
        self.__priority_button.clicked.connect(self.open_priority_window)
        self.__set_priority_button_text() # in case the task is created with a priority

        # Rename button
        self.__rename_button = QPushButton("Renommer")
        self.__rename_button.clicked.connect(self.open_rename_window)

        # Creating a HBox for the elements controls
        self.__controls_layout = QHBoxLayout()
        # Adding Widgets to the HBox
        self.__controls_layout.addWidget(self.__checkbox, alignment=Qt.AlignLeft)
        self.__controls_layout.addWidget(self.__task_label, stretch=1, alignment=Qt.AlignLeft)
        self.__controls_layout.addWidget(self.__priority_button, alignment=Qt.AlignRight)
        self.__controls_layout.addWidget(self.__rename_button, alignment=Qt.AlignRight)
        self.__controls_layout.addWidget(self.__create_subtask_button, alignment=Qt.AlignRight)

        # Adding elements to the main layout
        self.__layout.addLayout(self.__controls_layout)

    def __str__(self):  # str to print the title in the project
        """
        return the task's name when printing
        :return:
        """
        return f"{self.__name_task}"

    def create_subtask(self, name_subtask: str = "Sous tache"):
        """
        create a subtask with a name
        :param name_subtask: str
        :return:
        """
        created_subtask = sbts.Subtask(name_subtask)
        self.__subtask_list.append(created_subtask)  # create the object in the list
        self.__layout.addWidget(created_subtask)

    def delete_subtask(self, num):
        """
        delete the "num"th subtask
        :param num:
        :return:
        """
        del self.__subtask_list[num]

    def __on_checkbox_state_changed(self):
        """
        check if the task is done
        :return:
        """
        if self.__checkbox.isChecked():
            self.__task_label.setDisabled(True)
            self.__is_done = True
            # Set state for all subtask
            for subtask in self.__subtask_list:
                subtask.is_done = True
        else:
            self.__task_label.setDisabled(False)
            self.__is_done = False
            # set state for all subtask
            for subtask in self.__subtask_list:
                subtask.is_done = False

    def open_priority_window(self):
        """
        open a window to change the priority of the task
        :return:
        """
        priority = ["Aucune", "Basse", "Moyenne", "Haute", "Urgente"]
        item, ok = QInputDialog.getItem(
            self, "Priorité", "Choisissez la priorité de la tâche", priority, 0, False
        )
        if ok and item:
            self.__priority = item
            self.__set_priority_button_text()

    def __set_priority_button_text(self):
        if self.__priority == "Aucune":
            self.__priority_button.setText(f"Priorité")
        else:
            self.__priority_button.setText(f"Priorité : {self.__priority}")

    def open_rename_window(self):
        """
        open a window to rename the task
        :return:
        """
        new_name, ok = QInputDialog.getText(
            self, "Renommer", "Entrez le nouveau nom de la tâche"
        )
        if ok and new_name:
            self.__name_task = new_name
            self.__task_label.setText(self.__name_task)

    def to_dict(self):
        """
        exports the task to a dictionary for json serialization,
        called by the task's parent,
        it calls its children to_dict() methods
        :return: dict of the task
        """
        subtask_dicts = []
        for subtask in self.__subtask_list:
            subtask_dicts.append(subtask.to_dict())

        return {
            "name": self.__name_task,
            "is_done": self.__is_done,
            "priority": self.__priority,
            "subtasks": subtask_dicts,
        }

    @property
    def name_task(self):
        """
        returns the name of the task
        :return: str: name of the task
        """
        return self.__name_task

    @name_task.setter
    def name_task(self, name_task):
        """
        sets the name of the task
        :param name_task: str
        :return:
        """
        self.__name_task = name_task

    @property
    def subtask_list(self):
        """
        returns the list of subtasks
        :return: list
        """
        return self.__subtask_list

    @subtask_list.setter
    def subtask_list(self, subtask_list):
        """
        sets the list of subtasks
        :param subtask_list: list
        :return:
        """
        self.__subtask_list = subtask_list

    @property
    def priority(self):
        """
        get the prioriry
        :return: priority of the task
        """
        return self.__priority

    @property
    def is_done(self) -> bool:
        """
        get the state of the task
        :return: is_done: bool
        """
        return self.__is_done

    @is_done.setter
    def is_done(self, is_done: bool):
        """
        set the state of the task
        :param is_done: bool
        :return:
        """
        self.__task_label.setDisabled(is_done)
        self.__is_done = is_done
        # Set state for all subtask
        for subtask in self.__subtask_list:
            subtask.is_done = is_done