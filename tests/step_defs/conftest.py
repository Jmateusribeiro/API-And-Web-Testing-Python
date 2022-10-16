import pytest
from tests.pages.todo_list_page import ToDOList



@pytest.fixture(scope="class")
def todo_list(request):

    # Setup code
    todo_list = ToDOList(browser='Chrome')

    def teardown():
        # Teardown code
        print("\nClose browser")
        todo_list.close_browser()

    request.addfinalizer(teardown)

    return todo_list