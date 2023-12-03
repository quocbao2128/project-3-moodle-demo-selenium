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


# INPUT DATA FILE
def login_data():
    # Đọc dữ liệu từ file Excel
    input_data = pd.read_excel(r'../test_data_level_1.xlsx', sheet_name='teacher_login').fillna('')

    # Chuyển đổi thành list của tuples
    data = input_data.to_records(index=False).tolist()

    return data


# test case login level 1
class TestProj3Level1:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.data = login_data()

    def teardown_method(self):
        self.driver.quit()

    def login(self, function, user_name, password):
        self.driver.get("https://school.moodledemo.net/?lang=en")
        self.driver.find_element(By.XPATH, "//*[@id=\"usernavigation\"]/div[5]/div/span/a").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys(user_name)
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()
        return self.driver.title

    # @pytest.mark.parametrize được sử dụng để chạy test case với mỗi dòng dữ liệu từ hàm login_data.
    @pytest.mark.parametrize('function, user_name, password, expected_result', login_data())
    def test_func_teacher_login(self, function, user_name, password, expected_result):
        expected = expected_result.split('|')[0]
        actual = self.login(function, user_name, password).split('|')[0]

        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert expected in actual

