Feature: Orange HRM Logo

  Scenario: Logo checking for orange HRM web page
    Given I Launch Microsoft-Edge Dev Browser
    When open the Orange HRM Home page
    And verify the Logo Present on Dashboard Page
    Then close the Browser