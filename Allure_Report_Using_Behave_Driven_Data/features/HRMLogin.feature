Feature:Login Functionality check of HRM web page

  Scenario:checking login functionality of HRM web page
    Given open the Edge Browser
    When open the Orange HRM Login Page
    And Accessing the HMS Page on that so that we can access the Login
    And Enter the username as "admin" and password as "admin"
    And click on the Login button to access Dashboard Page
    Then check the Dashboard page displayed or not and close the Edge Browser

  Scenario Outline: checking login functionality of HRM web page with Multiple parameters
    Given open the Edge Browser
    When open the Orange HRM Login Page
    And Accessing the HMS Page on that so that we can access the Login
    And Enter the username as "<username>" and password as "<password>"
    And click on the Login button to access Dashboard Page
    Then check the Dashboard page displayed or not and close the Edge Browser
    Examples:
      | username | password |
      | admin    | admin    |
      | rika     | sarangi  |
      | pratik   | sarangi  |


