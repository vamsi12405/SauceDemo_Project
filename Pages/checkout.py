import time

from Pages import framework as fw
from . import homepage as hp
from . import addtoCart as ac

def verifyBasic(driver):
    fw.wait(driver)
    fw.verifyURL(driver,"https://www.saucedemo.com/cart.html")
    fw.verifyTitle(driver,"Swag Labs")
    fw.verifyText(driver,"//span[@class='title']","Your Cart")
    fw.verifyElements(driver,"//div[@class='cart_item']")
    fw.verifyElements(driver,"//button[@class='btn btn_action btn_medium checkout_button ']")
    fw.verifyElements(driver,"//button[@class='btn btn_secondary back btn_medium']")

def performOperation(driver):
    try:
        time.sleep(1)
        fw.clickElements(driver,"//button[@class='btn btn_action btn_medium checkout_button ']")
    except Exception as e:
        print("Exception is",e)

