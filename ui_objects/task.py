import logging
from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
    QInputDialog,
    QSizePolicy,
    QInputDialog,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics
from datetime import datetime
from PyQt5.QtCore import QTimer

from ui_objects import subtask as sbts

PRIORITIES = ["Aucune", "Basse", "Moyenne", "Haute", "Urgente"]


class Task(QFrame):
    """
    Task

    Project => Repository => Task => Subtask
    """

    def __init__(
            self,
            parent,
            name_task: str = 'Tache',
            subtask_list: list = None,
            is_done: bool = False,
            priority: str = "Aucune",
            assignee: str = None,
            due_date: datetime = None
    ):
        """
        create the task's ui elements, passing a subtask is optional
        :param name_task: name of task
        :param subtask_list: list of subtask
        """
        super().__init__()
        self.__parent = parent
        if subtask_list is None:  # creation of an empty list if none is given
            subtask_list = []
        self.__name_task = name_task
        self.__subtask_list = subtask_list
        self.__is_done = is_done
        if priority in PRIORITIES:
            self.__priority = priority
        else:
            self.__priority = "Aucune"

        self.__assignee = assignee
        self.__due_date = due_date

        self.setFrameStyle(QFrame.StyledPanel)

        # creating a widget and set layout
        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)
        self.__layout.setAlignment(Qt.AlignTop)

        self.__task_label = QLabel(self.__name_task)
        self.__task_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)

        # Check box to check if the task is done
        self.__checkbox = QCheckBox("")
        self.__checkbox.stateChanged.connect(self.__on_checkbox_state_changed)

        # Priority list
        self.__priority_button = QPushButton("Priorité")
        self.__priority_button.clicked.connect(self.open_priority_window)
        self.__set_priority_button_text()  # in case the task is created with a priority

        # Rename button
        self.__rename_button = QPushButton("Renommer")
        self.__rename_button.clicked.connect(self.open_rename_window)

        # Create button
        self.__create_subtask_button = QPushButton("+")
        self.__create_subtask_button.clicked.connect(self.__create_subtask_popup)
        self.__create_subtask_button.setFixedWidth(30)

        # Delete button
        self.__delete_button = QPushButton("X")
        self.__delete_button.clicked.connect(self.__delete_self)
        self.__delete_button.setFixedWidth(30)

        # Assign button
        self.__assign_button = QPushButton("Assigner")
        self.__assign_button.clicked.connect(self.open_assignment_window)

        # Due date button
        self.__due_date_button = QPushButton("Date")
        self.__due_date_button.clicked.connect(self.due_date_window)

        # Countdown label
        self.__countdown_label = QLabel()
        self.__countdown_timer = QTimer(self)
        self.__countdown_timer.timeout.connect(self.__countdow)
        self.__countdown_timer.start(1000)

        # Creating a HBox for the elements controls
        self.__controls_layout = QHBoxLayout()
        # Adding Widgets to the HBox
        self.__controls_layout.addWidget(self.__checkbox, alignment=Qt.AlignLeft)
        self.__controls_layout.addWidget(self.__priority_button, alignment=Qt.AlignRight)
        self.__controls_layout.addWidget(self.__rename_button, alignment=Qt.AlignRight)
        self.__controls_layout.addWidget(self.__assign_button, alignment=Qt.AlignRight)
        self.__controls_layout.addWidget(self.__due_date_button, alignment=Qt.AlignRight)
        self.__controls_layout.addWidget(self.__create_subtask_button, alignment=Qt.AlignRight)
        self.__controls_layout.addWidget(self.__delete_button, alignment=Qt.AlignRight)

        # Adding elements to the main layout
        self.__layout.addWidget(self.__task_label, alignment=Qt.AlignLeft)
        self.__layout.addLayout(self.__controls_layout)
        self.__layout.addWidget(self.__countdown_label, alignment=Qt.AlignRight)

        if self.__subtask_list:
            for subtask_widget in self.__subtask_list:
                self.__layout.addWidget(subtask_widget)

        self.__update_task_label()

    def __str__(self):  # str to print the title in the project
        """
        return the task's name when printing
        :return:
        """
        return f"{self.__name_task}"

    def __create_subtask_popup(self):
        name_subtask, ok = QInputDialog.getText(
            self,
            'Nom du repository',
            'Entrez le nom de la sous-tâche:'
        )
        if not ok:
            return  # exit if the user cancel

        # Set name to a placeholder if user input is empty
        if name_subtask == "":
            name_subtask = "Sous-Tâche"

        self.create_subtask(name_subtask)

    def __delete_self(self):
        self.__parent.delete_task(self)

    def create_subtask(self, name_subtask: str = "Sous-tâche"):
        """
        create a subtask with a name
        :param name_subtask: str
        :return:
        """
        created_subtask = sbts.Subtask(self, name_subtask)
        self.__subtask_list.append(created_subtask)  # create the object in the list
        self.__layout.addWidget(created_subtask)

    def delete_subtask(self, sbts: sbts.Subtask):
        """
        delete the "num"th subtask
        :param num:
        :return:
        """
        sbts.deleteLater()
        self.__subtask_list.remove(sbts)
        logging.debug(f"deleted subtask {sbts} / remaining sbts: {len(self.__subtask_list)}")

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
            self.__priority_button.setStyleSheet("background-color: None")
        elif self.__priority == "Basse":
            self.__priority_button.setText(f"{self.__priority}")
            self.__priority_button.setStyleSheet("background-color: green")
        elif self.__priority == "Moyenne":
            self.__priority_button.setText(f"{self.__priority}")
            self.__priority_button.setStyleSheet("background-color: yellow")
        elif self.__priority == "Haute":
            self.__priority_button.setText(f"{self.__priority}")
            self.__priority_button.setStyleSheet("background-color: orange")
        elif self.__priority == "Urgente":
            self.__priority_button.setText(f"{self.__priority}")
            self.__priority_button.setStyleSheet("background-color: red")

    def open_rename_window(self):
        """
        open a window to rename the task
        """
        new_name, ok = QInputDialog.getText(
            self, "Renommer", "Entrez le nouveau nom de la tâche"
        )
        if ok and new_name:
            self.__name_task = new_name
            self.__task_label.setText(self.__name_task)

    def open_assignment_window(self):
        """
        open a window to assign the task to a user
        """
        assignee, ok = QInputDialog.getText(
            self, "Assigner une tâche", "Entrez le prénom de la personne à qui assigner la tâche:"
        )
        if ok and assignee:
            self.__assignee = assignee
            self.__update_task_label()

    def due_date_window(self):
        """
        open a window to set the due date of the task
        """
        due_date, ok = QInputDialog.getText(
            self, "Date d'échéance", "Entrez la date d'échéance de la tâche: (sous forme dd/mm/yyyy)"
        )
        if ok and due_date:
            try:
                self.__due_date = datetime.strptime(due_date, "%d/%m/%Y")
                self.__update_task_label()
            except ValueError as e:
                logging.error(f"Error while parsing due date: {e}")

    def __update_task_label(self):
        """
        update the task label
        """
        if self.__assignee and not self.__due_date:
            self.__task_label.setText(f"{self.__name_task} \nAssignée à: {self.__assignee}")
        elif not self.__assignee and self.__due_date:
            self.__task_label.setText(f"{self.__name_task} \nPour le: {self.__due_date}")
        elif self.__assignee and self.__due_date:
            self.__task_label.setText(
                f"{self.__name_task} \nAssignée à: {self.__assignee} \nPour le: {self.__due_date.strftime('%d/%m/%Y')}")

    def __countdow(self):
        """
        calculate the time left before the due date
        """
        if self.__due_date:
            try:
                time_left = self.__due_date - datetime.now()
                self.__countdown_label.setText(f"{time_left.days} jours restants")
            except ValueError as e:
                logging.error(f"Error while calculating the remaining time: {e}")

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
            "assignee": self.__assignee,
            "due_date": self.__due_date.strftime("%Y-%m-%d"),
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
