import pytest
import time
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import read_write_excel as rwe


# level 1 - mỗi test case đều lấy data
# test case teacher login
class TestTeacherLoginLevel1:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        print('\n')

    def teardown_method(self):
        self.driver.quit()

    def test_teacher_login_success(self):
        input_data = rwe.read_from_excel('test_data.xlsx', 'teacher_login')
        data = input_data[0]

        self.driver.get(data[1])

        self.driver.find_element(By.XPATH, "//*[@id=\"usernavigation\"]/div[5]/div/span/a").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys(data[2])
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(data[3])
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(2)

        title = self.driver.title
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert data[4] in title

    def test_teacher_login_fail_1(self):
        input_data = rwe.read_from_excel('test_data.xlsx', 'teacher_login')
        data = input_data[1]

        self.driver.get(data[1])

        self.driver.find_element(By.XPATH, "//*[@id=\"usernavigation\"]/div[5]/div/span/a").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys(data[2])
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(data[3])
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(2)

        title = self.driver.title
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert data[4] in title

    def test_teacher_login_fail_2(self):
        input_data = rwe.read_from_excel('test_data.xlsx', 'teacher_login')
        data = input_data[2]

        self.driver.get(data[1])

        self.driver.find_element(By.XPATH, "//*[@id=\"usernavigation\"]/div[5]/div/span/a").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys(data[2])
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(data[3])
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(2)

        title = self.driver.title
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert data[4] in title

    def test_teacher_login_fail_3(self):
        input_data = rwe.read_from_excel('test_data.xlsx', 'teacher_login')
        data = input_data[3]

        self.driver.get(data[1])

        self.driver.find_element(By.XPATH, "//*[@id=\"usernavigation\"]/div[5]/div/span/a").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys(data[2])
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(data[3])
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(2)

        title = self.driver.title
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert data[4] in title

    def test_teacher_login_fail_4(self):
        input_data = rwe.read_from_excel('test_data.xlsx', 'teacher_login')
        data = input_data[4]

        self.driver.get(data[1])

        self.driver.find_element(By.XPATH, "//*[@id=\"usernavigation\"]/div[5]/div/span/a").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys(data[2])
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(data[3])
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(2)

        title = self.driver.title
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert data[4] in title

