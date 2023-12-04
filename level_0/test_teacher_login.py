import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# level 0 - hard code data vào từng test case, không lấy data bên ngoài vào
# test case teacher login
class TestTeacherLoginLevel0:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()

    def teardown_method(self):
        self.driver.quit()

    def test_teacher_login_success(self):
        self.driver.get("https://school.moodledemo.net/login/index.php?lang=en")

        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys("moodle")
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(2)

        title = self.driver.title
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert "My courses | Mount Orange School" in title

    def test_teacher_login_fail_1(self):
        self.driver.get("https://school.moodledemo.net/login/index.php?lang=en")

        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(1)
        # self.driver.find_element(By.ID, "username").send_keys("teacher")
        # time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys("moodle")
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(2)

        title = self.driver.title
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert "Log in to the site | Mount Orange School" in title

    def test_teacher_login_fail_2(self):
        self.driver.get("https://school.moodledemo.net/login/index.php?lang=en")

        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        time.sleep(2)
        # self.driver.find_element(By.ID, "password").send_keys("moodle")
        # time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(2)

        title = self.driver.title
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert "Log in to the site | Mount Orange School" in title

    def test_teacher_login_fail_3(self):
        self.driver.get("https://school.moodledemo.net/login/index.php?lang=en")

        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(1)
        # self.driver.find_element(By.ID, "username").send_keys("teacher")
        # time.sleep(2)
        # self.driver.find_element(By.ID, "password").send_keys("moodle")
        # time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(2)

        title = self.driver.title
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert "Log in to the site | Mount Orange School" in title
