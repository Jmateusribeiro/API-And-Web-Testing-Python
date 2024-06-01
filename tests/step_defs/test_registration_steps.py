import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import requests
from utilities.settings import HOST, REGISTRATION_ENDPOINT, CREDENTIALS_FILE
from dotenv import dotenv_values
from typing import Dict, Any

scenarios('../features/registration.feature')

# Given Step
@given(parsers.cfparse('email and password are definied as {email} and {password}'), target_fixture='payload')
def payload(email: str, password: str, log: 'CustomLogger') -> Dict[str, str]:
    """
    Define payload with email and password.

    Args:
        email (str): Email address.
        password (str): Password.
        log (CustomLogger): A logger object for logging messages.

    Returns:
        Dict[str, str]: Payload dictionary.
    """
    email = "" if email == "N/A" else email
    password = "" if password == "N/A" else password
    payload = {
        "email": email,
        "password": password
    }
    log.info(payload)
    return payload

# When Step
@when("registration is executed", target_fixture='registration')
def registration(payload: Dict[str, str]) -> requests.Response:
    """
    Execute registration.

    Args:
        payload (Dict[str, str]): Registration payload.

    Returns:
        requests.Response: Response object.
    """
    url = HOST + REGISTRATION_ENDPOINT
    body = payload

    response = requests.post(url, data=body, verify=False)
    return response

# Then Steps
@then(parsers.cfparse("registration is {status}"))
def assert_response_code(registration: requests.Response, status: str) -> None:
    """
    Assert registration response code.

    Args:
        registration (requests.Response): Registration response object.
        status (str): Expected status.
    """
    if status == "completed":
        assert registration.status_code == requests.codes.ok, registration.json()["error"]
    elif status == "not completed":
        assert registration.status_code == 400, "expected status code: '400'"
    else:
        pytest.fail(f"Status '{status}' not valid")

@then(parsers.cfparse("the correct token is returned"))
def returned_token(registration: requests.Response, payload: Dict[str, str]) -> None:
    """
    Assert the correct token is returned.

    Args:
        registration (requests.Response): Registration response object.
        payload (Dict[str, str]): Registration payload.
    """
    tokens_dict = dotenv_values(CREDENTIALS_FILE)
    email = payload["email"]
    expected_token = tokens_dict[email]
    token = registration.json()["token"]
    assert token == expected_token, f"Token returned {token} isn't the expected"

@then(parsers.cfparse("an {error_message} is returned"))
def returned_error_message(registration: requests.Response, error_message: str, log: 'CustomLogger') -> None:
    """
    Assert an error message is returned.

    Args:
        registration (requests.Response): Registration response object.
        error_message (str): Expected error message.
        log (CustomLogger): A logger object for logging messages.
    """
    assert registration.json()["error"] == error_message, f"expected error: {error_message}"
    log.info("expected error: " + registration.json()["error"])
