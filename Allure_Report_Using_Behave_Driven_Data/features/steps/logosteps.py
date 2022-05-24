from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'open Edge Browser')
def step_impl(context):
    context.driver=webdriver.Edge()


@when(u'Open the Orange HRM Home page')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")


@when(u'click on the logo of the Orange HRM')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//body/div[@id='wrapper']/div[@id='content']/div[@id='divLogin']/div[@id='divLogo']/img[1]").click()


@then(u'check the logo displayed on the web page or not and close the Browser')
def step_impl(context):
    status = context.driver.find_element(By.XPATH,"//body/div[@id='wrapper']/div[@id='content']/div[@id='divLogin']/div[@id='divLogo']/img[1]").is_displayed()
    assert status is True
    context.driver.close()
