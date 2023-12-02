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


class TestProj3:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()

    def teardown_method(self):
        self.driver.quit()

    def test_teacher_login_success(self):
        self.driver.get("https://school.moodledemo.net/?lang=en")
        self.driver.find_element(By.XPATH, "//*[@id=\"usernavigation\"]/div[5]/div/span/a").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys("moodle")
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()

        title = self.driver.title
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert "My courses | Mount Orange School" in title

    def test_teacher_login_fail_1(self):
        self.driver.get("https://school.moodledemo.net/?lang=en")
        self.driver.find_element(By.XPATH, "//*[@id=\"usernavigation\"]/div[5]/div/span/a").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(1)
        # self.driver.find_element(By.ID, "username").send_keys("teacher")
        # time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys("moodle")
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()

        title = self.driver.title
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert "Log in to the site | Mount Orange School" in title

    def test_teacher_login_fail_2(self):
        self.driver.get("https://school.moodledemo.net/?lang=en")
        self.driver.find_element(By.XPATH, "//*[@id=\"usernavigation\"]/div[5]/div/span/a").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        time.sleep(2)
        # self.driver.find_element(By.ID, "password").send_keys("moodle")
        # time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()

        title = self.driver.title
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert "Log in to the site | Mount Orange School" in title

    def test_teacher_login_fail_3(self):
        self.driver.get("https://school.moodledemo.net/?lang=en")
        self.driver.find_element(By.XPATH, "//*[@id=\"usernavigation\"]/div[5]/div/span/a").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(1)
        # self.driver.find_element(By.ID, "username").send_keys("teacher")
        # time.sleep(2)
        # self.driver.find_element(By.ID, "password").send_keys("moodle")
        # time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()

        title = self.driver.title
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert "Log in to the site | Mount Orange School" in title

    def test_teacher_logout(self):
        self.driver.get("https://school.moodledemo.net/?lang=en")
        wait_element = WebDriverWait(self.driver, 10)

        wait_element.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"usernavigation\"]/div[5]/div/span/a")))
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id=\"usernavigation\"]/div[5]/div/span/a").click()

        wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-container")))
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()

        wait_element.until(EC.element_to_be_clickable((By.ID, "username")))
        time.sleep(2)
        self.driver.find_element(By.ID, "username").send_keys("teacher")

        wait_element.until(EC.element_to_be_clickable((By.ID, "password")))
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys("moodle")

        wait_element.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()

        wait_element.until(EC.element_to_be_clickable((By.ID, "user-menu-toggle")))
        time.sleep(2)
        self.driver.find_element(By.ID, "user-menu-toggle").click()

        wait_element.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"carousel-item-main\"]/a[9]")))
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id=\"carousel-item-main\"]/a[9]").click()

        wait_element.until(EC.title_contains("Home"))
        time.sleep(2)
        title = self.driver.title
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert "Home | Mount Orange School" in title
