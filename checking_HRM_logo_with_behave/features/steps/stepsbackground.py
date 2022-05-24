from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'Launch the Edge-Browser')
def step_impl(context):
    context.driver = webdriver.Edge()


@when(u'open  Orange-HRM Home page')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'click on the Orange-HRM logo')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@id='divLogo']//img").click()


@then(u'check the Logo displayed or not and close the Browser')
def step_impl(context):
    result = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert result is True
    context.driver.close()


@when(u'Enter username "{user}" and password "{passwd}"')
def step_impl(context,user,passwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(passwd)


@when(u'click on the login button to access Dashboard')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()


@then(u'check the Dashboard page coming or Not and close the Browser')
def step_impl(context):
    status = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Dashboard')]").text
    print("status is",status)
    assert status == "Dashboard"
    context.driver.close()