from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from utilities.settings import SCREENSHOT_PATH
from selenium.webdriver.chrome.options import Options

headless_options = Options()
headless_options.add_argument("--headless")

class WebBrowser:
    """
    Class representing a web browser instance.
    """

    def __init__(self, browser: str, implicit_wait: int = 3, screenshot_path: str = SCREENSHOT_PATH):
        """
        Initialize the WebBrowser instance.

        Args:
            browser (str): The browser to use.
            implicit_wait (int): The implicit wait time.
            screenshot_path (str): The path to save screenshots.
        """
        self.driver = self.initialize_browser(browser)
        self.implicit_wait = implicit_wait
        self.screenshot_path = screenshot_path

    def initialize_browser(self, browser: str) -> webdriver:
        """
        Initialize the WebDriver instance.

        Args:
            browser (str): The browser to initialize.

        Returns:
            webdriver: The WebDriver instance.
        """
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

    def open_browser(self, url: str) -> None:
        """
        Open the browser and navigate to the given URL.

        Args:
            url (str): The URL to navigate to.

        Returns:
            None
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def close_browser(self) -> None:
        """
        Close the browser.

        Returns:
            None
        """
        self.driver.quit()

    def get_element(self, by_locator: tuple):
        """
        Get the web element identified by the locator.

        Args:
            by_locator (tuple): The locator strategy and value.

        Returns:
            web element: The web element.
        """
        return WebDriverWait(self.driver, self.implicit_wait).until(EC.visibility_of_element_located(by_locator))

    def get_element_text(self, by_locator: tuple) -> str:
        """
        Get the text of the web element identified by the locator.

        Args:
            by_locator (tuple): The locator strategy and value.

        Returns:
            str: The text of the web element.
        """
        return self.get_element(by_locator).text

    def type_element(self, by_locator: tuple, text: str) -> None:
        """
        Type text into the web element identified by the locator.

        Args:
            by_locator (tuple): The locator strategy and value.
            text (str): The text to type into the web element.

        Returns:
            None
        """
        self.get_element(by_locator).send_keys(text)

    def click_element(self, by_locator: tuple) -> None:
        """
        Click on the web element identified by the locator.

        Args:
            by_locator (tuple): The locator strategy and value.

        Returns:
            None
        """
        self.get_element(by_locator).click()

    def send_keys(self, by_locator: tuple, key) -> None:
        """
        Send keys to the web element identified by the locator.

        Args:
            by_locator (tuple): The locator strategy and value.
            key: The keys to send.

        Returns:
            None
        """
        self.get_element(by_locator).send_keys(key)

    def is_element_visible(self, by_locator: tuple) -> bool:
        """
        Check if the web element identified by the locator is visible.

        Args:
            by_locator (tuple): The locator strategy and value.

        Returns:
            bool: True if the element is visible, False otherwise.
        """
        return self.get_element(by_locator).is_displayed()

    def check_if_element_exists(self, by_locator: tuple) -> bool:
        """
        Check if the web element identified by the locator exists.

        Args:
            by_locator (tuple): The locator strategy and value.

        Returns:
            bool: True if the element exists, False otherwise.
        """
        try:
            self.driver.find_element(*by_locator)
            return True

        except NoSuchElementException:
            return False

    def find_elements(self, by_locator: tuple):
        """
        Find all web elements identified by the locator.

        Args:
            by_locator (tuple): The locator strategy and value.

        Returns:
            list: List of web elements.
        """
        return self.driver.find_elements(*by_locator)

    def take_screenshot(self, name: str) -> None:
        """
        Take a screenshot and save it with the given name.

        Args:
            name (str): The name to save the screenshot.

        Returns:
            None
        """
        self.driver.save_screenshot(self.screenshot_path + name + '.png')
