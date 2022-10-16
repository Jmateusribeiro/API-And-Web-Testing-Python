import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages.todo_list_page import ToDOList


scenarios('../features/add_task.feature')


# Given Step
@given('todo list page is open')
def open_todo_list_page(todo_list):

    todo_list.open_page()

# When Step
@when(parsers.cfparse("{task_name} task is added"), target_fixture='task_name')
def add_task(todo_list, task_name):

    todo_list.add_new_task(task_name)

    return task_name

# Then Steps
@then('the task is visible in todo list')
def validate_task_was_added(todo_list, task_name):

    assert todo_list.validate_if_task_exist(task_name) is True, f"Task: '{task_name}' not created"