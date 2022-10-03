from pytest_bdd import scenarios, given, when, then, parsers
import requests
from utilities.settings import HOST, USER_LIST_ENDPOINT


scenarios('../features/user_list.feature')


@given("a completed user list is requested", target_fixture='get_users_list')
def get_users_list():

    url = HOST + USER_LIST_ENDPOINT
    page = 1
    params = {"page": page}

    response = requests.get(url, params=params)
    assert response.status_code == requests.codes.ok

    total_pages = response.json()["total_pages"]
    total_users = response.json()["total"]
    users_list = response.json()["data"]

    for page in range(2, total_pages + 1):
        response = requests.get(url, params=params)
        assert response.status_code == requests.codes.ok
        users_list = users_list + response.json()["data"]

    return users_list, total_users


@then("the complete list of users is given successfully")
def step_impl(get_users_list):

    users_list = get_users_list[0]
    nr_users = get_users_list[1]

    assert len(users_list) == nr_users, f"expected nr of users {nr_users}; nr of users saved {len(users_list)}"
    print(f"total nr of users: {nr_users}")
    print(f"users: {users_list}")