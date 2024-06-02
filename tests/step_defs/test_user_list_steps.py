"""
steps to scenarios of user_list feature
"""
from typing import List, Tuple
import requests
from pytest_bdd import parsers, given, then, scenarios
from utilities.settings import HOST, USER_LIST_ENDPOINT, REQUESTS_TIMEOUT

scenarios('../features/user_list.feature')

@given("a completed user list is requested", target_fixture='users_list')
def get_users_list() -> Tuple[List[dict], int]:
    """
    Fixture to retrieve the complete user list from the API.

    Returns:
        Tuple[List[dict], int]: A tuple containing the list of users and the total number of users.
    """
    url = HOST + USER_LIST_ENDPOINT
    page = 1
    params = {"page": page}

    response = requests.get(url, params=params, timeout=REQUESTS_TIMEOUT)
    assert response.status_code == requests.codes.ok

    total_pages = response.json()["total_pages"]
    total_users = response.json()["total"]
    users_list = response.json()["data"]

    for page in range(2, total_pages + 1):
        response = requests.get(url, params=params, timeout=REQUESTS_TIMEOUT)
        assert response.status_code == requests.codes.ok
        users_list = users_list + response.json()["data"]

    return users_list, total_users

@then(parsers.parse("the complete list of users is given successfully"))
def step_impl(users_list: Tuple[List[dict], int], log: 'CustomLogger') -> None:
    """
    Validate the complete list of users obtained from the API.

    Args:
        users_list (Tuple[List[dict], int]): A tuple containing the 
            list of users and the total number of users.
        log (CustomLogger): A logger object for logging messages.
    """
    users = users_list[0]
    nr_users = users_list[1]

    error_msg = f"""Expected number of users: {nr_users}; 
    Actual number of users: {len(users)}"""
    assert len(users) == nr_users, error_msg
    log.info(f"Total number of users: {nr_users}")
    log.info(f"Users: {users}")
