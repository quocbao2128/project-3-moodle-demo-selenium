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


# level 1 - test case nhận data dưới dạng đối số (argument) truyền vào
# test case teacher login
class TestTeacherLoginLevel1:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()

    def teardown_method(self):
        self.driver.quit()
        print('\n')

    def login(self, url, user_name, password):
        wait_element = WebDriverWait(self.driver, 10)

        self.driver.get(url)

        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a').click()

        wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-container")))
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()

        wait_element.until(EC.element_to_be_clickable((By.ID, "username")))
        time.sleep(2)
        self.driver.find_element(By.ID, "username").send_keys(user_name)

        wait_element.until(EC.element_to_be_clickable((By.ID, "password")))
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(password)

        wait_element.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()

        return self.driver.title

    # @pytest.mark.parametrize được sử dụng để chạy test case, data có n dòng thì test case chạy n lần.
    @pytest.mark.parametrize('function, url, user_name, password, expected_result',
                             rwe.read_from_excel(r'../test_data.xlsx', 'teacher_login'))
    def test_func_teacher_login(self, function, url, user_name, password, expected_result):
        expected = expected_result.split('|')[0]
        actual = self.login(url, user_name, password).split('|')[0]

        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert expected in actual

