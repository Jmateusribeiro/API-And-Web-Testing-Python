# API Testing With Python

Goal: Show how one can develop BDD API tests with python 


#### API tests: The tests on this project were developed in BDD style

## Run Tests:

All tests of this project can be runned by executing the bat file 'run_tests.bat'
Each execution generates a html report inside 'reports' folder.

Note: Don't forget to run the bat file inside an environment with all requirements (requirements.txt) installed

    
## Final considerations:

- Pytest has a lot of useful side-packages. Examples: 
  - pytest-bdd: run tests written in BDD
  - pytest-html: generate html reports
  - pytest-xdist: run tests in parallel
- BDD test development make tests more readable;
- To run the same test with different data, scenario outline is the best option;


Hope you enjoyed!