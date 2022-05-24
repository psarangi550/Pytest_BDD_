Feature: Login functionality of Orange HRM

  Scenario: I login in to the Orange HRM Login page
    Given launch the Edge Browser
    When accessing the login page with username as "admin" and password as "admin123"
    And click on the login button
    And accessing the Dashboard Page
    And check that we are accessing the Dashboard page
    Then close the Browser
