# API and Web Testing With Python

[![Pylint](https://github.com/Jmateusribeiro/API-And-Web-Testing-Python/actions/workflows/pylint.yml/badge.svg)](https://github.com/Jmateusribeiro/API-And-Web-Testing-Python/actions/workflows/pylint.yml)

Goal: Show how one can develop BDD API and Web (selenium) tests with python (pytest)


#### The tests on this project were developed in BDD style

## Run Tests:

All tests of this project can be runned by executing the bat file 'run_tests.bat'
Each execution generates a html report inside 'reports' folder.
Inside the batch file, one can define the browser where web tests will run setting the variable 'browser'

Note: Don't forget to run the bat file inside an environment with all requirements (requirements.txt) installed

## API tests:

  Tested API: https://reqres.in

  This API fakes a user list where you can perform multiple actions on that list
  
  Implemented tests:
  - Successful Registration
  - Unsuccessful Registration
  - Get User List

## Web tests:

  Tested website: http://webdriveruniversity.com/To-Do-List/index.html

  This website represents a ToDO list where one can add, remove and mark as completed different tasks

  Supported Browsers:
  - Chrome (tested on version: 106.0.5249.119; Webdriver:  106.0.5249.61
  - Edge (tested on version: 106.0.1370.47; Webdriver:  106.0.1370.42)
  - Opera (tested on version: 91.0.4516.77; Webdriver:  0.31.0)
  - Headless Chrome
  
  Implemented tests:
  - Add New Task Successfully

**Note:**

  When running tests on a specific browser, if one have the following error: 
      
    AttributeError: 'dict' object has no attribute 'send_keys'

  Should add the following code:

  ```python
  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
  
  options = Options()
  options.add_experimental_option("w3c", True)
  # should add w3c option to the browser where get the error
  # example with Opera:
  driver = webdriver.Opera(options=options)
  ```
    
## Final considerations:

- Pytest has a lot of useful side-packages. Examples: 
  - pytest-bdd: run tests written in BDD
  - pytest-html: generate html reports
  - pytest-xdist: run tests in parallel
- BDD test development make tests more readable;
- To run the same test with different data, scenario outline is the best option;

  The .env file is committed because this project is only to demonstration purposes.
  In real projects the .env file, containing critical info, must be add to .gitignore

Hope you enjoyed!

  


