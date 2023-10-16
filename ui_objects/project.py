import repository as repo

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
class Project(QWidget):
    def _init__(self, name_project : str = 'Project', repository_list : list = None):  # variable init
        if repository_list is None:  # creation of an empty list if none is given
            repository_list = ['']
        self.__name_project = name_project
        self.__repository_list = repository_list


    def __str__(self):  # str to print the tittle in the project
        return f"{self.__name_project}"

    def create_repository(self, name_repository):  # crate a repository with the file task.py
        self.__repository_list.append('')  # add a new space in the list
        index = len(self.__repository_list)  # take the index of the new place
        self.__repository_list[index - 1] = repo.Repository(f"{name_repository}")  # create the object in the list

    def delete_repository(self, name_repository):
        self.__repository_list.remove(self.__repository_list.index(name_repository.__name_repository))

    def change_name(self, new_name): #change the name
        self.__name_project = new_name

    @property
    def name_project(self):
        return self.__name_project

    @name_project.setter
    def name_project(self, name_project):
        self.__name_project = name_project

    @property
    def repository_list(self):
        return self.__repository_list

    @repository_list.setter
    def repository_list(self, repository_list):
        self.__repository_list = repository_list