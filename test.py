import pytest
import sys
from ui_objects.repository import Repository
from ui_objects.sidebar import Sidebar
from ui_objects.project import Project
from ui_objects.task import Task as ts
from PyQt5.QtWidgets import QApplication, QWidget


@pytest.fixture(scope="module")
def test_app():
    app = QApplication(sys.argv)
    yield app
    app.quit()


# testing repository
def test_repository_initialization(test_app):
    repository = Repository()
    assert repository.name_rep == "Repertoire"
    assert repository.task_list == []


def test_repository_add_task(test_app):
    repository = Repository()
    repository.create_task("Test Task")
    assert len(repository.task_list) == 1
    assert repository.task_list[0].name_task == "Test Task"


# testing task
def test_task_initialization(test_app):
    task = ts()
    assert task.name_task == "Tache"
    assert task.subtask_list == []


# testing subtask
def test_task_create_subtask(test_app):
    task = ts()
    task.create_subtask("Subtask 1")
    assert len(task.subtask_list) == 1
    assert task.subtask_list[0].name_subtask == "Subtask 1"

# testing to_dict
def test_project_to_dict(test_app):
    project = Project("TheProject")
    project.create_repository("Repo1")
    project.repository_list[0].create_task("Task1")
    project.repository_list[0].task_list[0].create_subtask("Subtask1")

    expected_dict = {
        "name_project": "TheProject",
        "repositories": [
            {
                "name": "Repo1",
                "tasks": [
                    {
                        "name": "Task1",
                        "subtasks": [
                            {"name": "Subtask1"}
                        ]
                    }
                ]
            }
        ]
    }

    assert project.to_dict() == expected_dict


# testing sidebar
def test_sidebar_button_click(test_app, qtbot):
    class MockParent(QWidget):
        def __init__(self):
            super().__init__()
            self.projects = []

    parent_mock = MockParent()
    sidebar = Sidebar(parent_mock)
    qtbot.addWidget(sidebar)
