from selenium import webdriver
from selenium.webdriver.common.by import By

def application(driver,url):
    driver.get(url)

def verifyURL(driver, givenURL):
    current = driver.current_url
    print(f"[verifyURL] Expected: {givenURL} | Actual: {current}")
    assert current == givenURL, f"User in wrong Application(Wrong URL): Expected '{givenURL}', Got '{current}'"

def verifyTitle(driver,givenTitle):
    assert driver.title.__eq__(givenTitle),"User in wrong Application(Wrong Title)"

def verifyText(driver, xpath, givenText):
    txtval = driver.find_element(By.XPATH, xpath).text
    print(f"[verifyText] Expected: '{givenText}' | Actual: '{txtval}'")
    assert txtval == givenText, f"Text does not match. Expected: '{givenText}', Got: '{txtval}'"

def verifyElements(driver,xpath):
    assert driver.find_element(By.XPATH,xpath),"Eleemnt not found"

def verifyMultipleElements(driver,xpath):
    assert driver.find_elements(By.XPATH,xpath)

def sendInput(driver,xpath,send_value):
    driver.find_element(By.XPATH,xpath).send_keys(send_value)

def clickElements(driver,xpath):
    driver.find_element(By.XPATH,xpath).click()

def wait(driver):
    driver.implicitly_wait(20)


