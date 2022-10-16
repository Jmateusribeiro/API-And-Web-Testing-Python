"""
This module contains all the settings required
"""
import os

HOST = 'https://reqres.in/'
REGISTRATION_ENDPOINT = 'api/register'
USER_LIST_ENDPOINT = 'api/users'
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
SCREENSHOT_PATH=f'{PROJECT_DIR}//reports//evidences//'

os.makedirs(SCREENSHOT_PATH, exist_ok=True)