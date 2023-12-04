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
# test case teacher logout
class TestTeacherLogoutLevel1:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        print('\n')

    def teardown_method(self):
        self.driver.quit()

    def test_teacher_logout(self):
        input_data = rwe.read_from_excel(r'../test_data.xlsx', 'teacher_logout')
        data = input_data[0]

        # login
        self.driver.get(data[1])
        wait_element = WebDriverWait(self.driver, 10)
        try:
            wait_element.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"usernavigation\"]/div[5]/div/span/a")))
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@id=\"usernavigation\"]/div[5]/div/span/a").click()

            wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-container")))
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()

            wait_element.until(EC.element_to_be_clickable((By.ID, "username")))
            time.sleep(2)
            self.driver.find_element(By.ID, "username").send_keys(data[2])

            wait_element.until(EC.element_to_be_clickable((By.ID, "password")))
            time.sleep(2)
            self.driver.find_element(By.ID, "password").send_keys(data[3])

            wait_element.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
            time.sleep(2)
            self.driver.find_element(By.ID, "loginbtn").click()

            # logout
            wait_element.until(EC.element_to_be_clickable((By.ID, "user-menu-toggle")))
            time.sleep(2)
            self.driver.find_element(By.ID, "user-menu-toggle").click()

            wait_element.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"carousel-item-main\"]/a[9]")))
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@id=\"carousel-item-main\"]/a[9]").click()

            wait_element.until(EC.title_contains("Home"))
            time.sleep(2)
            title = self.driver.title

            # value_to_write = self.driver.title.split
            rwe.write_to_excel(r'../test_data.xlsx', 'teacher_logout', 5, 1, str(title))

            # ketQuaMongDoi so sanh voi ketQuaChayThucTe
            assert data[4] in title

        except Exception as e:
            rwe.write_to_excel(r'../test_data.xlsx', 'teacher_logout', 5, 1, str(e))
