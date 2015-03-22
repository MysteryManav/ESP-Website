from selenium.webdriver.support.ui import WebDriverWait
import time

def noActiveAjaxJQuery(driver):
    return driver.execute_script("return $j.active == 0")
def waitForAjaxJQuery(driver):
    while(not noActiveAjaxJQuery(driver)):
        time.sleep(1)
def noActiveAjaxForms(driver):
    return driver.execute_script("return numAjaxConnections == 0")
def waitForAjaxForms(driver):
    while(not noActiveAjaxForms(driver)):
        time.sleep(1)

def try_login(driver, username, password):
    elem = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_name("username"))
    elem.send_keys(username)
    elem = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_name("password"))
    elem.send_keys(password)
    elem.submit()

def try_normal_login(driver, username, password):
    try_login(driver, username, password)
    driver.open_url("/")

def try_ajax_login(driver, username, password):
    try_login(driver, username, password)
    try:
        WebDriverWait(driver, 10).until(noActiveAjaxForms)
    except Exception as exc:
        exc_type = type(exc)
        message = exc.message
        if message:
            message += "\n"
        message += "Wait for ajax login timed out."
        raise exc_type(message)
    driver.open_url("/")

def logout(driver):
    driver.open_url("/myesp/signout/")
    driver.open_url("/")
