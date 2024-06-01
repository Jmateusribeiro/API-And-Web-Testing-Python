import pytest
from tests.pages.todo_list_page import ToDOList
from utilities.settings import SUPPORTED_BROWSERS, REPORT_DIR
from utilities.classes.log import CustomLogger

def pytest_addoption(parser: pytest.Parser) -> None:
    """
    Add custom command-line option for pytest.

    Args:
        parser (pytest.Parser): The pytest parser object.
    """
    parser.addoption("--Browser", action="store", default="Headless Chrome", help="browser to run the test")

@pytest.fixture()
def browser(request: pytest.FixtureRequest) -> str:
    """
    Fixture to retrieve the selected browser from the command-line option.

    Args:
        request (pytest.FixtureRequest): The pytest fixture request object.

    Returns:
        str: The selected browser.
    """
    return request.config.getoption('--Browser')

@pytest.fixture(scope='module')
def log() -> CustomLogger:
    """
    Fixture to create a CustomLogger instance.

    Returns:
        CustomLogger: A CustomLogger instance.
    """
    return CustomLogger(REPORT_DIR)

@pytest.fixture()
def todo_list(request: pytest.FixtureRequest, browser: str, log: CustomLogger) -> ToDOList:
    """
    Fixture to set up and tear down the ToDOList instance.

    Args:
        request (pytest.FixtureRequest): The pytest fixture request object.
        browser (str): The selected browser.
        log (CustomLogger): A CustomLogger instance.

    Returns:
        ToDOList: An instance of the ToDOList class.
    """
    log.info(f"browser selected: {browser}")
    if browser not in SUPPORTED_BROWSERS:
        raise Exception(f"Browser '{browser}' not supported; supported Browsers: {SUPPORTED_BROWSERS}")

    # Setup code
    todo_list = ToDOList(browser=browser)

    def teardown():
        # Teardown code
        log.info("Close browser")
        todo_list.close_browser()

    request.addfinalizer(teardown)

    return todo_list
