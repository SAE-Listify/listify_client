import task as ts

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


class Repository:  # (QWidget):
    def __init__(self, name_rep: str = "Repertoire", task_list=None, task_list_name = None):  # variable init
        # super(QWidget,self).__init__()
        if task_list is None:  # create an empty list if none is given
            task_list = []
        if task_list_name is None:
            task_list_name = []
        self.__name_rep = name_rep
        self.__task_list = task_list
        self.__task_list_name = task_list_name

    def __str__(self):  # str to print the title in the project
        return f"{self.__name_rep}"

    def create_task(self, name_task: str = "Tache"):  # crawte a task with the file task.py
        self.__task_list.append('')  # add a new space in the list
        index = len(self.__task_list)  # take the index of the new place
        self.__task_list[index - 1] = ts.Task(name_task)  # create the object in the list

    def delete_task(self, num: int):
        del self.__task_list[num]

    def changename_rep(self, new_name):  # change the name
        self.__name_rep = new_name

    def export_task_name(self):
        for task in self.__task_list:
            self.__task_list_name.append(task.name_task)
        return self.__task_list_name

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

    @property
    def task_list_name(self):
        return self.__task_list_name

    @task_list_name.setter
    def task_list_name(self, task_list_name):
        self.__task_list_name = task_list_name