import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium import webdriver
from Pages import framework as fw
from Pages import homepage as hp
from Pages import addtoCart as ac
from Pages import checkout as ck
from Pages import checkOutSteps as cs

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_full_user_flow(driver):
    fw.application(driver, "https://www.saucedemo.com/")
    hp.verifymain(driver)
    hp.verifyAllelemts(driver)
    time.sleep(2)
    hp.performOperation(driver)


    ac.verifyMain(driver)
    ac.addtoCart(driver)

    ck.verifyBasic(driver)
    ck.performOperation(driver)

    cs.verifyStepOne(driver)
    cs.addDetails(driver)
    cs.verifyStepTwo(driver)
    cs.performOperation(driver)
    cs.verifyStepThree(driver)
    cs.performOperation_three(driver)
