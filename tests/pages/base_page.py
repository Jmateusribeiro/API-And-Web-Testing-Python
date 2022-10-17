from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from utilities.settings import SCREENSHOT_PATH
from selenium.webdriver.chrome.options import Options


headless_options = Options()
headless_options.add_argument("--headless")


class WebBrowser:

    def __init__(self, browser, implicit_wait=3, screenshot_path=SCREENSHOT_PATH ):
        self.driver = self.initialize_browser(browser)
        self.implicit_wait = implicit_wait
        self.screenshot_path = screenshot_path

    def initialize_browser(self, browser):
        # Initialize the WebDriver instance
        if browser == 'Chrome':
            return webdriver.Chrome()
        elif browser == 'Edge':
            return webdriver.Edge()
        elif browser == 'Headless Chrome':
            return webdriver.Chrome(options=headless_options)
        elif browser == 'Opera':
            options = Options()
            options.add_experimental_option("w3c", True)
            return webdriver.Opera(options=options)
        else:
            raise Exception(f'Browser "{browser}" is not supported')

    def open_browser(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def close_browser(self):
        self.driver.quit()

    def get_element(self, by_locator):
        return WebDriverWait(self.driver, self.implicit_wait).until(EC.visibility_of_element_located(by_locator))

    def get_element_text(self, by_locator):
        return self.get_element(by_locator).text

    def type_element(self, by_locator, text):
        self.get_element(by_locator).send_keys(text)

    def click_element(self, by_locator):
        self.get_element(by_locator).click()

    def send_keys(self, by_locator, key):
        self.get_element(by_locator).send_keys(key)

    def is_element_visible(self, by_locator):
        return self.get_element(by_locator).is_displayed()

    def check_if_element_exists(self, by_locator):
        try:
            self.driver.find_element(*by_locator)
            return True

            # NoSuchElementException thrown if not present
        except NoSuchElementException:
            return False

    def find_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def take_screenshot(self, name):
        # take screenshot
        self.driver.save_screenshot(self.screenshot_path + name + '.png')
