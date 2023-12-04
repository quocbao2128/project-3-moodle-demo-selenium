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


# level 2 - test case nhận data dưới dạng tham số truyền vào
# test case teacher logout
class TestTeacherLogoutLevel2:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()

    def teardown_method(self):
        self.driver.quit()

    def logout(self, url, user_name, password):
        wait_element = WebDriverWait(self.driver, 10)

        # login
        self.driver.get(url)

        wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-container")))
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()

        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys(user_name)
        time.sleep(1)
        self.driver.find_element(By.ID, "password").send_keys(password)

        wait_element.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
        time.sleep(1)
        self.driver.find_element(By.ID, "loginbtn").click()

        # logout
        wait_element.until(EC.element_to_be_clickable((By.ID, "user-menu-toggle")))
        time.sleep(1)
        self.driver.find_element(By.ID, "user-menu-toggle").click()

        wait_element.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"carousel-item-main\"]/a[9]")))
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id=\"carousel-item-main\"]/a[9]").click()

        wait_element.until(EC.title_contains("Home"))
        time.sleep(2)
        return self.driver.title

    # @pytest.mark.parametrize được sử dụng để chạy test case, data có n dòng thì test case chạy n lần.
    @pytest.mark.parametrize('function, url, user_name, password, expected_result',
                             rwe.read_from_excel(r'../test_data.xlsx', 'teacher_logout'))
    def test_func_teacher_logout(self, function, url, user_name, password, expected_result):
        expected = expected_result.split('|')[0]
        actual = self.logout(url, user_name, password).split('|')[0]

        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert expected in actual

