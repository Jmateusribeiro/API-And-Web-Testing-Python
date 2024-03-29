import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import requests
from utilities.settings import HOST, REGISTRATION_ENDPOINT, CREDENTIALS_FILE
from dotenv import dotenv_values


scenarios('../features/registration.feature')


# Given Step
@given(parsers.cfparse('email and password are definied as {email} and {password}'), target_fixture='payload')
def payload(email, password):
    email = "" if email == "N/A" else email
    password = "" if password == "N/A" else password
    payload = {
        "email": email,
        "password": password
    }
    print(payload)
    return payload


# When Step
@when("registration is executed", target_fixture='registration')
def registration(payload):
    url = HOST + REGISTRATION_ENDPOINT
    body = payload

    response = requests.post(url, data=body, verify=False)
    return response


# Then Steps
@then(parsers.cfparse("registration is {status}"))
def assert_response_code(registration, status):
    if status == "completed":
        assert registration.status_code == requests.codes.ok, registration.json()["error"]
    elif status == "not completed":
        assert registration.status_code == 400, "expected status code: '400'"
    else:
        pytest.fail(f"Status '{status}' not valid")


@then(parsers.cfparse("the correct token is returned"))
def returned_token(registration, payload):

    tokens_dict = dotenv_values(CREDENTIALS_FILE)
    email = payload["email"]
    expected_token = tokens_dict[email]
    token = registration.json()["token"]
    assert token == expected_token, f"Token returned {token} isn't the expected"


@then(parsers.cfparse("an {error_message} is returned"))
def returned_error_message(registration, error_message):
    assert registration.json()["error"] == error_message, f"expected error: {error_message}"
    print("expected error: " + registration.json()["error"])

