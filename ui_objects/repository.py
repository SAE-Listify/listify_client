import task as ts

import logging
import sys

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

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont, QCloseEvent
class Repository(QWidget):
    def __init__(self, name_rep : str = "Repertoire", task_list=None): #variable init
        super(QWidget,self).__init__()
        if task_list is None: #create an empty list if none is given
            task_list = ['']
        self.__name_rep = name_rep
        self.__task_list = task_list

    def __str__(self): #str to print the title in the project
        return f"{self.__name_rep}"

    def create_task(self, name_task): #crate a task with the file task.py
        self.__task_list.append('') #add a new space in the list
        index = len(self.__task_list) #take the index of the new place
        self.__task_list[index-1] = ts.Task(f"{name_task}") #create the object in the list

    def delete_task(self, name_task):
        self.__task_list.remove(self.__task_list.index(name_task.__name_task))

    def change_name(self, new_name): #change the name
        self.__name_rep = new_name

    @property
    def name_rep(self):
        return self.__name_rep

    @name_rep.setter
    def name_rep(self, name_rep):
        self.__name_rep = name_rep

    @property
    def task_list(self):
        return self.__task_list

    @task_list.setter
    def task_list(self, task_list):
        self.__task_list = task_list