"""
This module contains all the settings required
"""
import os

HOST = 'https://reqres.in/'
REGISTRATION_ENDPOINT = 'api/register'
USER_LIST_ENDPOINT = 'api/users'
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
SCREENSHOT_PATH=f'{PROJECT_DIR}/reports/evidences/'
CREDENTIALS_FILE = f'{PROJECT_DIR}/credentials.env'
REPORT_DIR = f'{PROJECT_DIR}/reports'
REQUESTS_TIMEOUT=60

os.makedirs(SCREENSHOT_PATH, exist_ok=True)

SUPPORTED_BROWSERS = ['Headless Chrome', 'Edge', 'Chrome', 'Opera']
