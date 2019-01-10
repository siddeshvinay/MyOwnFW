from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from Results import Log_Script as log
from Datatable import Test_data_lib as TD
import os
from ProjectSpecific import Genric_scripts as GS
from Driver import Main_Driver as MD
from Datatable import Test_data_lib as TC_Data



global oBrowser
oBrowser=webdriver.Chrome()
oBrowser.maximize_window()

def getRowNum(rownum):
    x=rownum
    print(x)
    return x

#FileName=os.path.abspath(__file__+"/../ExcelSheet.xlsx")
FileName = "C:/Users/sjanagonnavar/DJFW/Datatable/ExcelSheet.xlsx"
SheetName = "TC1"


FileName = "C:/Users/sjanagonnavar/DJFW/Datatable/ExcelSheet.xlsx"
SheetName = "TC1"




TD.load_Data_OS(FileName,SheetName)

def launch():
    status="Fail"

    try:
        oBrowser.get(os.environ.get("URL"))
        log.writelogs("Successully launch the browswer","Info")
        sleep(1)

    except Exception as e:
        print(e)
        log.writelogs()

    return status


# def launch1():
#     status="Fail"
#
#     try:
#         TestURL=oBrowser.get(TD.getExcutiondata(FileName,SheetName,"UserName",0))
#         print(TestURL)
#         #log.writelogs("Successully launch the browswer","Info")
#         sleep(1)
#
#     except Exception as e:
#         print(e)
#         #log.writelogs()
#
#     return status




def login():
    status="Fail"

    try:
        GS.UserName().send_keys(os.environ.get("UserName",-1))

        log.writelogs("Successully enter the UserName", "Info")

        GS.PassWord().send_keys(os.environ.get("Password",-1))
        log.writelogs("Successully enter the Password", "Info")

        GS.LogIn().click()
        log.writelogs("navigate to Home page", "Info")

        wait = WebDriverWait(oBrowser, 10)
        status=wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='taskSearchControl_field']")))

    except Exception as e:
        print(e)
        log.writelogs("Unable to click on login button", "Error")

def logout():
    status = "Fail"

    try:
        GS.Logout().click()
        log.writelogs("Succesfully logout from the application","Info")

        status="Pass"
        sleep(1)
        return status

    except Exception as e:
        log.writelogs("Unable to logout form the application", "Error")

    finally:
        oBrowser.close()

def ValidateUser():
    status="Fail"
    try:
        #oBrowser.find_element_by_xpath("//input[@id='taskSearchControl_field'']").is_displayed()
        oBrowser.find_element_by_xpath("//input[@id='taskSearchControl_field']").send_keys("Testing")
        x=oBrowser.find_element_by_xpath("//input[@id='taskSearchControl_field']").get_attribute("value")
        x = oBrowser.find_element_by_xpath("//input[@id='taskSearchControl_field']").get_property("id")
        print(x)
    except Exception as e:
        print("unable to the value")







