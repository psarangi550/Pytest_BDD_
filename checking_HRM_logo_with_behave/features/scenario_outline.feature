Feature: Login Functionality check of HRM using One and Multiple parameters

  Scenario: Login Functionality check of HRM using One parameters
    Given Launch the Edge Browser.
    When Open Orange HRM Home page.
    And Login using username "admin" and password "admin123"
    And click on the login button.
    Then check the Dashboard page option text and close the Browser.


  Scenario Outline:Login Functionality check of HRM using One parameters
    Given Launch the Edge Browser.
    When Open Orange HRM Home page.
    And Login using username "<username>" and password "<password>"
    And click on the login button.
    Then check the Dashboard page option text and close the Browser.

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin    | admin    |
      | user     | passwd   |
      | pratik   | sarangi  |
      | rika     | sarangi  |


