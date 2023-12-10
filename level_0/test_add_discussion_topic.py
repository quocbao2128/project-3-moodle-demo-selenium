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
class TestAddTopicnLevel0:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()

    def teardown_method(self):
        self.driver.quit()
        print('\n')

    def test_adding_topic_success(self):
        #Login
        self.driver.get("https://school.moodledemo.net/login/index.php?lang=en")
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        self.driver.find_element(By.ID, "password").send_keys("moodle")
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(1)

        # Access forum and click add topic
        self.driver.get("https://school.moodledemo.net/mod/forum/view.php?f=81")
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
        time.sleep(1)

        # Input title
        self.driver.find_element(By.ID, "id_subject").send_keys("topic name")
        time.sleep(1)
        
        # Input message
        self.driver.switch_to.frame('id_message_ifr')
        self.driver.find_element(By.ID, "tinymce").send_keys("topic message")
        self.driver.switch_to.default_content()

        # Click btn submit
        self.driver.find_element(By.ID, "id_submitbutton").click()
        time.sleep(2)

        # Diff result
        messages = self.driver.find_element(By.CSS_SELECTOR, ".alert-success")
        assert "Your post was successfully added." in messages.text

    def test_adding_topic_fail_not_login(self):
        # Access forum and click add topic
        self.driver.get("https://school.moodledemo.net/mod/forum/view.php?f=81")
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
        time.sleep(1)

        # Diff result
        messages = self.driver.find_element(By.ID, "modal-body")
        expectedMessages= ["Only logged in users can post to this forum.", "Xin lỗi, khách không được phép đăng bài." ]
        assert any(messages.text in e for e in expectedMessages)

    def test_adding_topic_fail_not_fill_required(self):
        #Login
        self.driver.get("https://school.moodledemo.net/login/index.php?lang=en")
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        self.driver.find_element(By.ID, "password").send_keys("moodle")
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(1)

        # Access forum and click add topic
        self.driver.get("https://school.moodledemo.net/mod/forum/view.php?f=81")
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
        time.sleep(1)

        # Click btn submit
        self.driver.find_element(By.ID, "id_submitbutton").click()
        time.sleep(2)

        # Diff result
        messages = self.driver.find_element(By.ID, "id_error_subject")
        assert "Required" in messages.text
