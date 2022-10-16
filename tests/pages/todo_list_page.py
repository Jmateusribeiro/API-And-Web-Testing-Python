from selenium.webdriver.common.by import By
from tests.pages.base_page import WebBrowser
from selenium.webdriver.common.keys import Keys

class ToDoListLocators:
    todo_list_url = 'http://webdriveruniversity.com/To-Do-List/index.html'
    title = 'WebDriver | To Do List'
    input_element = (By.XPATH, '//input[@placeholder="Add new todo" and not(@style="display: none;")]')
    tasks_list = (By.TAG_NAME, 'li')
    plus_icon = (By.ID, 'plus-icon')


class ToDOList(WebBrowser):

    def open_page(self):

        self.open_browser(ToDoListLocators.todo_list_url)
        assert self.driver.title == ToDoListLocators.title

    def validate_if_task_exist(self, task_name):

        task_exist_flag = False
        tasks_list_elements = self.find_elements(ToDoListLocators.tasks_list)
        for task in tasks_list_elements:
            if task.text != task_name:
                task_exist_flag = True
                break

        return task_exist_flag

    def validate_if_task_marked(self, task_name):

        locator = (By.XPATH, f'//li[text()="{task_name}" and @class="completed"]')
        return self.check_if_element_exists(locator)

    def add_new_task(self, task_name):

        # validate in input field is visible
        if self.check_if_element_exists(ToDoListLocators.input_element) is False:
            self.click_element(ToDoListLocators.plus_icon)

        self.type_element(ToDoListLocators.input_element, task_name)
        self.send_keys(ToDoListLocators.input_element, Keys.ENTER)

        #take screenshot
        self.take_screenshot(f'{task_name}_task_added')


    def mark_task_as_completed(self, task_name):

        locator = (By.XPATH, f'//li[text()="{task_name}"]')
        self.click_element(locator)

        # take screenshot
        #self.browser.save_screenshot(self.path + task + '_task_marked.png')

        # validate task was marked
        #assert self.validate_if_task_marked(task_name) is True, f"Task '{task_name}' not marked"

    def unmark_task_as_completed(self, task_name):

        locator = (By.XPATH, f'//li[text()="{task_name}" and @class="completed"]')
        #COLOCAR TRATAMENTO DE ERRO AQUI
        self.click_element(locator)

        # take screenshot
        #self.browser.save_screenshot(self.path + task + '_task_unmarked.png')

        # validate task was unmarked
        #assert self.validate_if_task_marked(task_name) is False, f"Task '{task_name}' still marked"

    def delete_task(self, task_name):

        locator = (By.XPATH, f'//li[text()="{task_name}"]/span')
        "COLOCAR TRATAMENTO DE ERRO AQUI"
        self.click_element(locator)

        # take screenshot
        #self.browser.save_screenshot(self.path + task + '_task_deleted.png')

        # validate task was deleted
        #assert self.validate_if_task_exist(task_name) is False, f"Task '{task_name}' not deleted"