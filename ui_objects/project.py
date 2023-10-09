import repository as repo


class Project:
    def _init__(self, name_project : str = 'Projet', repository_list : list = None): #variable init
        if repository_list is None: #creation of an empty list if none is given
            repository_list = []
        self.__name_project = name_project
        self.__repository_list = repository_list
        pass

    def __str__(self): #str to print the tittle in the project
        return f"{self.__name_project}"

