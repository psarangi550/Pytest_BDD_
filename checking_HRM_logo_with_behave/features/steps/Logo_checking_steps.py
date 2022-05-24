from behave import given,when,then
from selenium import webdriver


@given("I Launch Microsoft-Edge Dev Browser")
def launch_browser(context):
    context.driver=webdriver.Edge()


@when("open the Orange HRM Home page")
def open_home(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when("verify the Logo Present on Dashboard Page")
def check_logo(context):
    status=context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True


@then("close the Browser")
def close_browser(context):
    context.driver.close()
