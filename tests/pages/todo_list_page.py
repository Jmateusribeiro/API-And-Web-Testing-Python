"""
Module containing classes and locators for interacting with the ToDoList page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.pages.base_page import WebBrowser

class ToDoListLocators:
    """
    Locators for elements on the ToDoList page.
    """
    todo_list_url: str = 'http://webdriveruniversity.com/To-Do-List/index.html'
    title: str = 'WebDriver | To Do List'
    input_element: tuple = (By.XPATH,
            '//input[@placeholder="Add new todo" and not(@style="display: none;")]')
    tasks_list: tuple = (By.TAG_NAME, 'li')
    plus_icon: tuple = (By.ID, 'plus-icon')

class ToDOList(WebBrowser):
    """
    Class representing the ToDoList page.
    """

    def open_page(self) -> None:
        """
        Open the ToDoList page and verify the title.

        Returns:
            None
        """
        self.open_browser(ToDoListLocators.todo_list_url)
        assert self.driver.title == ToDoListLocators.title

    def validate_if_task_exist(self, task_name: str) -> bool:
        """
        Validate if a task exists in the tasks list.

        Args:
            task_name (str): The name of the task to validate.

        Returns:
            bool: True if the task exists, False otherwise.
        """
        task_exist_flag: bool = False
        tasks_list_elements = self.find_elements(ToDoListLocators.tasks_list)
        for task in tasks_list_elements:
            if task.text != task_name:
                task_exist_flag = True
                break

        return task_exist_flag

    def validate_if_task_marked(self, task_name: str) -> bool:
        """
        Validate if a task is marked as completed.

        Args:
            task_name (str): The name of the task to validate.

        Returns:
            bool: True if the task is marked as completed, False otherwise.
        """
        locator = (By.XPATH, f'//li[text()="{task_name}" and @class="completed"]')
        return self.check_if_element_exists(locator)

    def add_new_task(self, task_name: str) -> None:
        """
        Add a new task to the ToDoList.

        Args:
            task_name (str): The name of the task to add.

        Returns:
            None
        """
        if self.check_if_element_exists(ToDoListLocators.input_element) is False:
            self.click_element(ToDoListLocators.plus_icon)

        self.type_element(ToDoListLocators.input_element, task_name)
        self.send_keys(ToDoListLocators.input_element, Keys.ENTER)

        self.take_screenshot(f'{task_name}_task_added')

    def mark_task_as_completed(self, task_name: str) -> None:
        """
        Mark a task as completed.

        Args:
            task_name (str): The name of the task to mark as completed.

        Returns:
            None
        """
        locator = (By.XPATH, f'//li[text()="{task_name}"]')
        self.click_element(locator)

    def unmark_task_as_completed(self, task_name: str) -> None:
        """
        Unmark a completed task.

        Args:
            task_name (str): The name of the task to unmark.

        Returns:
            None
        """
        locator = (By.XPATH, f'//li[text()="{task_name}" and @class="completed"]')
        self.click_element(locator)

    def delete_task(self, task_name: str) -> None:
        """
        Delete a task from the ToDoList.

        Args:
            task_name (str): The name of the task to delete.

        Returns:
            None
        """
        locator = (By.XPATH, f'//li[text()="{task_name}"]/span')
        self.click_element(locator)
