# API and Web Testing With Python

Goal: Show how one can develop BDD API and Web tests with python 


#### The tests on this project were developed in BDD style

## Run Tests:

All tests of this project can be runned by executing the bat file 'run_tests.bat'
Each execution generates a html report inside 'reports' folder.

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

  At the moment, only Chrome is supported!
  
  Implemented tests:
  - Add New Task Successfully

    
## Final considerations:

- Pytest has a lot of useful side-packages. Examples: 
  - pytest-bdd: run tests written in BDD
  - pytest-html: generate html reports
  - pytest-xdist: run tests in parallel
- BDD test development make tests more readable;
- To run the same test with different data, scenario outline is the best option;

Hope you enjoyed!
