Feature:Login Logo functionality of Orange HRM

  Background:background for both scenario
    Given Launch the Edge-Browser
    When open  Orange-HRM Home page

  Scenario: Logo of Orange HRM displayed
    When click on the Orange-HRM logo
    Then check the Logo displayed or not and close the Browser

  Scenario: Dashboard displayed on Orange HRM login
    When Enter username "admin" and password "admin123"
    And click on the login button to access Dashboard
    Then check the Dashboard page coming or Not and close the Browser