from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from Testcase import Test_Case_lib



def Test_case1():
    Test_Case_lib.launch()
    sleep(2)
    Test_Case_lib.login()
    sleep(2)
    # TC1.ValidateUser()
    sleep(3)
    Test_Case_lib.logout()
    sleep(3)
    #status = "Pass"

#print(Test_case1())

# def Test_case2():
#     Test_Case_lib.launch()
#     sleep(2)
#     Test_Case_lib.login()
#     sleep(2)
#     # TC1.ValidateUser()
#     sleep(3)
#     Test_Case_lib.logout()
#     sleep(3)
#     #status = "Pass"
