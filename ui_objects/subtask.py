import subtask as sbts

class Subtask:

    def _init__(self, name_subtask : str = 'Sous-Tâche', subtask_list : list = None): #variable init
        if subtask_list is None: #creation of an empty list if none is given
            subtask_list = []
        self.__name_subtask = name_subtask
        self.__subtask_list = subtask_list
        pass

    def __str__(self): #str to print the tittle in the project
        return f"{self.__name_subtask}"

    def create_subtask(self, name_subtask : str): #create a subtask using the subtask file
        name_subtask = sbts.subtask(f"{name_subtask}")
        self.__subtask_list.append(name_subtask) #add the subtask to the list