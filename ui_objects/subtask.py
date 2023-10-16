from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QMessageBox,
    QTabWidget,
    QTextBrowser,
    QHBoxLayout,
    QMessageBox,
)
class Subtask:

    def _init__(self, name_subtask : str = 'Sous-Tâche', subtask_list : list = None): #variable init
        if subtask_list is None: #creation of an empty list if none is given
            subtask_list = []
        self.__name_subtask = name_subtask
        self.__subtask_list = subtask_list
        pass

    def __str__(self): #str to print the tittle in the project
        return f"{self.__name_subtask}"

    def changename_task(self, new_name):
        self.__name_task = new_name

    @property
    def name_task(self):
        return self.__name_task

    @name_task.setter
    def name_task(self, name_task):
        self.__name_task = name_task