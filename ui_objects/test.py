import project as pr
import json
import repository as repo
projet1 = pr.Project("Projet 1")
projet2 = pr.Project("Projet 2")
projet3 = pr.Project("Projet 3")



print(f"{projet1}, {projet2} et {projet3}")

projet1.changename_proj("Projet TEST 1")

print(f"{projet1}, {projet2} et {projet3}")



projet1.create_repository("A faire")
projet1.create_repository("En cours")
projet1.create_repository("Finis")
projet1.create_repository("TEST")

print('')
print(f"Liste des repos du projet {projet1} : ")
for rep in projet1.repository_list:
    print(rep.name_rep)

projet1.repository_list[3].changename_rep("Nouveau Repo")
print('')
print(f"Liste des repos du projet {projet1} : ")
for rep in projet1.repository_list:
    print(rep.name_rep)

projet1.delete_repository(3)
print('')
print(f"Liste des repos du projet {projet1} : ")
for rep in projet1.repository_list:
    print(rep.name_rep)



projet1.repository_list[0].create_task("Menage")
projet1.repository_list[0].create_task("Vaiselle")
projet1.repository_list[0].create_task("Cuisine")
projet1.repository_list[0].create_task("Tache test")

print('')
print(f"Liste des tache du repertoire {projet1.repository_list[0].name_rep} du projet {projet1} : ")
for task in projet1.repository_list[0].task_list:
    print(task.name_task)

print('')
projet1.repository_list[0].task_list[3].changename_task("Tache random")
print(f"Liste des tache du repertoire {projet1.repository_list[0].name_rep} du projet {projet1} : ")
for task in projet1.repository_list[0].task_list:
    print(task.name_task)

print('')
projet1.repository_list[0].delete_task(3)
print(f"Liste des tache du repertoire {projet1.repository_list[0].name_rep} du projet {projet1} : ")
for task in projet1.repository_list[0].task_list:
    print(task.name_task)


projet1.repository_list[0].task_list[0].create_subtask("Serpillere")
projet1.repository_list[0].task_list[0].create_subtask("Balais")
projet1.repository_list[0].task_list[0].create_subtask("Aspirateur")
projet1.repository_list[0].task_list[0].create_subtask("Sous-tache nulle")

print('')
print(f"Liste des sous taches de la tache {projet1.repository_list[0].task_list[0].name_task} du repertoire {projet1.repository_list[0].name_rep} du projet {projet1} : ")
for subtask in projet1.repository_list[0].task_list[0].subtask_list:
    print(subtask.name_subtask)

print('')
projet1.repository_list[0].task_list[0].subtask_list[3].changename_subtask("Sous tache trop bien")
print(f"Liste des sous taches de la tache {projet1.repository_list[0].task_list[0].name_task} du repertoire {projet1.repository_list[0].name_rep} du projet {projet1} : ")
for subtask in projet1.repository_list[0].task_list[0].subtask_list:
    print(subtask.name_subtask)

print('')
projet1.repository_list[0].task_list[0].delete_subtask(3)
print(f"Liste des sous taches de la tache {projet1.repository_list[0].task_list[0].name_task} du repertoire {projet1.repository_list[0].name_rep} du projet {projet1} : ")
for subtask in projet1.repository_list[0].task_list[0].subtask_list:
    print(subtask.name_subtask)

list_repo = projet1.list_of_all_repo()
def to_dict(self):  # subtask
    return {
        "name": self.__name_subtask,
    }


def to_dict(self):  # task
    subtask_dicts = []
    for subtask in self.__subtask_list:
        subtask_dicts.append(subtask.to_dict())

    return {
        "name": self.__name_task,
        "subtasks": subtask_dicts,
    }


def to_dict(self):  # repo
    task_dicts = []
    for task in self.__task_list:
        task_dicts.append(task.to_dict())

    return {
        "name": self.__name_rep,
        "tasks": task_dicts,
    }


def to_dict(self):  # project
    repo_dicts = []
    for repo in self.__repository_list:
        repo_dicts.append(repo.to_dict())

    return {
        "name_project": self.__name_project,
        "repositories": repo_dicts,
    }
# Serializing data in JSON
    json_data = json.dumps(repo_dicts)

    # Save JSON to a file
    with open("noms1.json", "w") as json_file:
            json_file.write(json_data)
