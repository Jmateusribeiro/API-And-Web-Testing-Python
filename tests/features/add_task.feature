# Created by Admin at 16/10/2022
Feature: Add task

  Scenario Outline: Add New Task Successfully
    Given todo list page is open
    When <task_name> task is added
    Then the task is visible in todo list

    Examples:
      | task_name                  |
      | Challenge Harry Potter     |
      | Wand class                 |