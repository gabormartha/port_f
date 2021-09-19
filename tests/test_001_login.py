from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://www.saucedemo.com/"

driver.get(URL)
time.sleep(3)

# Elements
input_username = driver.find_element_by_id("user-name")
input_password = driver.find_element_by_id("password")
bt_login = driver.find_element_by_id("login-button")

# Test data
test_data_tc01 = ['standard_user', 'secret_sauce']

# input elemek kiuritese


def clear_inputs():
    input_username.clear()
    input_password.clear()


def test_tc01():
    time.sleep(1)
    input_username.send_keys(test_data_tc01[0])
    time.sleep(1)
    input_password.send_keys(test_data_tc01[1])
    time.sleep(1)
    bt_login.click()

    def check_cookies():
        # cookies = driver.get_cookies()
        # for coo in cookies:
        #     print(coo)
        print(driver.get_cookie("session-username"))

    check_cookies()


