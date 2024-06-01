from typing import Any
from pytest_bdd import scenarios, given, when, then, parsers
import pytest

scenarios('../features/add_task.feature')

# Given Step
@pytest.mark.usefixtures("todo_list")
@given('todo list page is open')
def open_todo_list_page(todo_list: "ToDOList") -> None:
    """
    Open the todo list page.

    Args:
        todo_list (ToDOList): The fixture for the todo list, an instance of ToDOList class.
    """
    todo_list.open_page()

# When Step
@when(parsers.cfparse("{task_name} task is added"), target_fixture='task_name')
def add_task(todo_list: "ToDOList", task_name: str) -> str:
    """
    Add a task to the todo list.

    Args:
        todo_list (ToDOList): The fixture for the todo list, an instance of ToDOList class.
        task_name (str): The name of the task to add.

    Returns:
        str: The name of the added task.
    """
    todo_list.add_new_task(task_name)
    return task_name

# Then Steps
@then('the task is visible in todo list')
def validate_task_was_added(todo_list: "ToDOList", task_name: str) -> None:
    """
    Validate that the task is visible in the todo list.

    Args:
        todo_list (ToDOList): The fixture for the todo list, an instance of ToDOList class.
        task_name (str): The name of the task to validate.
    """
    assert todo_list.validate_if_task_exist(task_name) is True, f"Task: '{task_name}' not created"
