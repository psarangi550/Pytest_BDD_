from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options


@given(u'Launch the Edge Browser.')
def step_impl(context):
    # options = Options()
    # options.binary_location = "C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    # driver_loc = "C:\\Users\\611903295\\Downloads\\python_BDD_Testing\\chromedriver.exe"
    # context.driver = webdriver.Chrome(options=options, executable_path=driver_loc)
    # context.driver=webdriver.Edge(executable_path="/mnt/c/Users/611903295/Downloads/Pytest_Journey/msedgedriver.exe")
    context.driver=webdriver.Edge()


@when(u'Open Orange HRM Home page.')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")


@when(u'Login using username "{user}" and password "{passwd}"')
def step_impl(context, user, passwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(passwd)


@when(u'click on the login button.')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()


@then(u'check the Dashboard page option text and close the Browser.')
def step_impl(context):
    try:
        status = context.driver.find_element(By.XPATH,"//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert 0
    else:
        if status == "Dashboard":
            context.driver.close()
            assert 1

