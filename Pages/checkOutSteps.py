import time

from Pages import framework as fw
from . import addtoCart as ac
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

mydict = {
    "//input[@placeholder='First Name']": "Vamsi",
    "//input[@placeholder='Last Name']": "Krishna",
    "//input[@placeholder='Zip/Postal Code']": "560061"
}

def verifyStepOne(driver):
    fw.wait(driver)
    fw.verifyURL(driver, "https://www.saucedemo.com/checkout-step-one.html")
    fw.verifyText(driver, "//span[@class='title']", "Checkout: Your Information")
    fw.verifyElements(driver, "//div[@class='checkout_info']")
    fw.verifyElements(driver, "//div[@class='checkout_buttons']")

def addDetails(driver):
    for xpath, value in mydict.items():
        fw.sendInput(driver, xpath, value)
        time.sleep(1)

    try:
        time.sleep(2)
        fw.clickElements(driver, "//input[@type='submit']")
        WebDriverWait(driver, 5).until(
            EC.url_contains("checkout-step-two.html")
        )
        print("[addDetails] Form submitted, moved to Step Two.")
    except Exception as e:
        print("[addDetails] Exception occurred during form submission:", e)
        try:
            err_text = driver.find_element("class name", "error-message-container").text
            print(f"[addDetails] Page Error Message: {err_text}")
        except:
            print("[addDetails] No error message found.")

def verifyStepTwo(driver):
    fw.wait(driver)
    fw.verifyURL(driver, "https://www.saucedemo.com/checkout-step-two.html")
    fw.verifyText(driver, "//span[@class='title']", "Checkout: Overview")
    fw.verifyElements(driver, "//div[@class='summary_info']")


def performOperation(driver):
    try:
        # Click the Finish button
        finish_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "finish"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", finish_button)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "finish"))
        ).click()
        print("[StepTwo] Clicked 'Finish' button.")

        # ✅ WAIT and VERIFY that we're on the checkout-complete page
        WebDriverWait(driver, 10).until(
            EC.url_contains("checkout-complete.html")
        )
        print("[StepTwo] Navigated to Checkout Complete page.")

    except Exception as e:
        print("Error during Finish operation:", e)

def verifyStepThree(driver):
    fw.wait(driver)
    fw.verifyURL(driver, "https://www.saucedemo.com/checkout-complete.html")
    fw.verifyElements(driver, "//div[@id='checkout_complete_container']")

def performOperation_three(driver):
    try:
        time.sleep(1)
        fw.clickElements(driver, "//button[@id='back-to-products']")
        WebDriverWait(driver, 20).until(
            EC.url_contains("https://www.saucedemo.com/inventory.html")
        )
    except Exception as e:
        print("Exception is", e)