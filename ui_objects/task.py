import subtask as sbts


class Task:
    def _init__(self, name_task : str = 'Tâche', subtask_list : list = None): #variable init
        if subtask_list is None: #creation of an empty list if none is given
            subtask_list = []
        self.__name_task = name_task
        self.__subtask_list = subtask_list
        pass

    def __str__(self): #str to print the tittle in the project
        return f"{self.__name_task}"

    def create_subtask(self, name_subtask : str): #create a subtasj using the subtask file
        name_subtask = sbts.SubTask(f"{name_subtask}")
        self.__subtask_list.append(name_subtask) #add the subtask to the list
