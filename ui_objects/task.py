from . import subtask as sbts

from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
    QInputDialog,
)


class Task(QFrame):
    """
    Task

    Project => Repository => Task => Subtask
    """

    def __init__(self, name_task: str = 'Tache', subtask_list=None):
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


        # Check box to check if the task is done
        self.__checkbox = QCheckBox("Tâche terminée")
        self.__checkbox.stateChanged.connect(self.validate_task)
        self.__layout.addWidget(self.__checkbox)

        # Priority list
        self.__priority_button = QPushButton(f"Priorité")
        self.__priority_button.clicked.connect(self.open_priority_window)
        self.__layout.addWidget(self.__priority_button)

        # Rename button
        self.__rename_button = QPushButton(f"Renommer")
        self.__rename_button.clicked.connect(self.open_rename_window)
        self.__layout.addWidget(self.__rename_button)

        # Positioning the buttons
        self.__button_layout = QHBoxLayout()
        self.__button_layout.addWidget(self.__priority_button)
        self.__button_layout.addWidget(self.__rename_button)
        self.__layout.addLayout(self.__button_layout)



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

    def validate_task(self):
        """
        check if the task is done
        :return:
        """
        if self.__checkbox.isChecked():
            self.__task_label.setDisabled(True)
            return True
        else:
            return False

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
            "subtasks": subtask_dicts,
            "state": self.__checkbox.isChecked(),
            "priority": self.__priority,
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
