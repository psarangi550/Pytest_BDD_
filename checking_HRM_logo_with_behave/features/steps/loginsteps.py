from selenium import webdriver
from behave import *


@given(u'launch the Edge Browser')
def step_impl(context):
    context.driver=webdriver.Edge(executable_path="/mnt/c/Users/611903295/Downloads/Pytest_Journey/msedgedriver.exe")


@when(u'accessing the login page with username as "{user}" and password as "{password}"')
def step_impl(context,user,password):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(password)


@when(u'click on the login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()


@when(u'accessing the Dashboard Page')
def step_impl(context):
    status=context.driver.find_element_by_xpath("//b[normalize-space()='Dashboard']").text
    # pass


@when(u'check that we are accessing the Dashboard page')
def step_impl(context):
    status=context.driver.find_element_by_css_selector("div.menu:nth-child(2) ul.main-menu-first-level-unordered-list.main-menu-first-level-unordered-list-width li.current.main-menu-first-level-list-item:nth-child(8) a.firstLevelMenu:nth-child(1) > b:nth-child(1)").text
    assert status == "Dashboard"
