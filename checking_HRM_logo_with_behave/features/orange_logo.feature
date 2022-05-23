Feature: Orange HRM Logo

  Scenario: Logo checking for orange HRM web page
    Given open Microsoft-Edge Browser Driver
    When open the Orange HRM Home page
    And verify the Logo Present on Dashboard Page
    Then close the Browser