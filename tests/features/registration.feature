Feature: Registration


  Scenario Outline: Successful Registration
    Given email and password are definied as <email> and <password>
    When registration is executed
    Then registration is completed
    And the correct <token> is returned

    Examples:
      | email                      | password | token             |
      | eve.holt@reqres.in         | xpto     | QpwL5tke4Pnpja7X4 |
      | michael.lawson@reqres.in   | xpto     | QpwL5tke4Pnpja7X7 |
      | lindsay.ferguson@reqres.in | xpto     | QpwL5tke4Pnpja7X8 |


  Scenario Outline: Unsuccessful Registration
    Given email and password are definied as <email> and <password>
    When registration is executed
    Then registration is not completed
    And an <error_message> is returned

    Examples:
      | email              | password | error_message                                 |
      | eve.holt@reqres.in | N/A      | Missing password                              |
      | N/A                | xpto     | Missing email or username                     |
      | teste@teste.com    | xpto     | Note: Only defined users succeed registration |