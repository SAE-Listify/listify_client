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
class Subtask: #(QWidget):

    def __init__(self, name_subtask : str = 'Sous-Tâche', subtask_list : list = None): #variable init
        # super(QWidget, self).__init__()
        if subtask_list is None: #creation of an empty list if none is given
            subtask_list = []
        self.__name_subtask = name_subtask
        self.__subtask_list = subtask_list

    def __str__(self): #str to print the tittle in the project
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