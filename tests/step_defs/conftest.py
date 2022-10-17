import pytest
from tests.pages.todo_list_page import ToDOList
from utilities.settings import supported_browsers


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Headless Chrome", help="browser to run the test")

@pytest.fixture
def browser(request):
    browser = request.config.getoption('--browser')
    return browser


@pytest.fixture()
def todo_list(request, browser):

    if browser not in supported_browsers:
        raise Exception(f"Browser '{browser}' not supported; supported Browsers: {supported_browsers}")

    # Setup code
    todo_list = ToDOList(browser=browser)

    def teardown():
        # Teardown code
        print("\nClose browser")
        todo_list.close_browser()

    request.addfinalizer(teardown)

    return todo_list