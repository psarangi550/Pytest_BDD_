from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'open the Edge Browser')
def step_impl(context):
    context.driver = webdriver.Edge()


@when(u'open the Orange HRM Login Page')
def step_impl(context):
    context.driver.get("http://www.seleniumbymahesh.com/")


@when(u'Accessing the HMS Page on that so that we can access the Login')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT , "HMS").click()


@when(u'Enter the username as "{user}" and password as "{passwd}"')
def step_impl(context,user,passwd):
    context.driver.find_element(By.NAME,"username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(passwd)


@when(u'click on the Login button to access Dashboard Page')
def step_impl(context):
    context.driver.find_element(By.NAME, 'submit').click()


@then(u'check the Dashboard page displayed or not and close the Edge Browser')
def step_impl(context):
    try:
        status=context.driver.find_element(By.XPATH,"//h2[contains(text(),'Mahesh Hospital Management System')]").text
    except Exception:
        context.driver.close()
        assert False,"Test Failed"
    else:
        if status == "Mahesh Hospital Management System":
            context.driver.close()
            assert True,"Test Passed"


