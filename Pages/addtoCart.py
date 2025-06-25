import time

from Pages import framework as fw
from . import homepage as hp

def verifyMain(driver):
    fw.wait(driver)
    fw.verifyURL(driver,"https://www.saucedemo.com/inventory.html")
    fw.verifyText(driver,"//span[@class='title']","Products")
    fw.verifyMultipleElements(driver,"//div[@class='inventory_item']")
    fw.verifyElements(driver,"//a[@class='shopping_cart_link']")

def addtoCart(driver):
    time.sleep(1)
    fw.clickElements(driver,"//button[@data-test='add-to-cart-sauce-labs-backpack']")
    try:
        fw.clickElements(driver,"//a[@class='shopping_cart_link']")
    except Exception as e:
        print("Error is",e)


