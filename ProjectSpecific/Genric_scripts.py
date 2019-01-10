from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from Results import Log_Script as log
from Datatable import Test_data_lib as TD
import os
from Testcase import Test_Case_lib

# global oBrowser
# oBrowser=webdriver.Chrome()
# oBrowser.maximize_window()
global FileName
#FileName=os.path.abspath(__file__+"/../PageObjects.xlsx")
FileName="C:/Users/sjanagonnavar/DJFW/Datatable/PageObjects.xlsx"
global SheetName
SheetName="PageObjects"

# FileName="C:/Users/Dell/PycharmProjects/DJFW/Datatable/PageObjects.xlsx"
# SheetName="PageObjects"
TD.load_Page_Objects(FileName,SheetName)
# pas=os.environ.get("Logout")
# print(pas)
def UserName():
    status="fail"
    try:
        #User_Name = TC1.oBrowser.find_element(By.XPATH, TD.get_pageObjects(FileName,SheetName,"UserName"))
        #User_Name = TC1.oBrowser.find_element(By.XPATH,'//input[@name="username"]')
        User_Name = Test_Case_lib.oBrowser.find_element(By.XPATH, os.environ.get("User_Name"))

    except Exception as e:
        log.writelogs("Unable to enter the data into UserName field")

    return User_Name


def PassWord():
    status="Fail"
    try:
        Pass_Word=Test_Case_lib.oBrowser.find_element(By.XPATH, TD.get_pageObjects(FileName, SheetName, "Pass_Word"))

    except Exception as e:
        log.writelogs("Unable to enter the data into Password field")

    return Pass_Word


def LogIn():
    status="Fail"
    try:
        Log_In=Test_Case_lib.oBrowser.find_element(By.XPATH, TD.get_pageObjects(FileName, SheetName, "Login"))
        status="Pass"

    except Exception as e:
        log.writelogs("Unable to click on logout link", "Error")

    return Log_In


def Logout():
    try:
        Log_out=Test_Case_lib.oBrowser.find_element(By.XPATH, TD.get_pageObjects(FileName, SheetName, "Logout"))

    except Exception as e:
        log.writelogs("Unable to click on logout Button")

    return Log_out



