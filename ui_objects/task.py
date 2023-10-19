from . import subtask as sbts

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


class Task: #(QWidget):
    def __init__(self, name_task : str = 'Tache', subtask_list = None): #variable init
        #super(QWidget, self).__init__()
        if subtask_list is None: #creation of an empty list if none is given
            subtask_list = []
        self.__name_task = name_task
        self.__subtask_list = subtask_list

    def __str__(self): #str to print the tittle in the project
        return f"{self.__name_task}"

    def create_subtask(self, name_subtask : str = "Sous tache"): #create a subtask using the subtask file
        self.__subtask_list.append('') #add a new space to the list
        index = len(self.__subtask_list) #take the index of the new space
        self.__subtask_list[index-1] = sbts.Subtask(name_subtask) #create the object in the list
    def delete_subtask(self, num): #delete a subtask using the subtask file
        del self.__subtask_list[num]

    def changename_task(self, new_name): #change the name of the task
        self.__name_task = new_name

    @property
    def name_task(self):
        return self.__name_task

    @name_task.setter
    def name_task(self, name_task):
        self.__name_task = name_task

    @property
    def subtask_list(self):
        return self.__subtask_list

    @subtask_list.setter
    def subtask_list(self, subtask_list):
        self.__subtask_list = subtask_list