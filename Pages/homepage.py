import time

from Pages import framework as fw
import random

xpaths = ["//input[@placeholder='Username']","//input[@placeholder='Password']","//input[@type='submit']"]

usernames= ["standard_user","locked_out_user","problem_user","performance_glitch_user","error_user","visual_user"]

def verifymain(driver):
    fw.wait(driver)
    fw.verifyURL(driver,"https://www.saucedemo.com/")
    fw.verifyTitle(driver,"Swag Labs")
    fw.verifyText(driver,"//div[@class='login_logo']","Swag Labs")

def verifyAllelemts(driver):
    for i in xpaths:
        fw.verifyElements(driver,i)

def performOperation(driver):
    fw.sendInput(driver,xpaths[0],"standard_user")
    fw.sendInput(driver,xpaths[1],"secret_sauce")
    time.sleep(1)
    try:
        fw.clickElements(driver,xpaths[2])
    except Exception as e:
        print("Exception is",e)