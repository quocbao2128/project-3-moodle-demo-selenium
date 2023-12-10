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
class TestAddTopicLevel1:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()

    def teardown_method(self):
        self.driver.quit()
        print('\n')

    def add_topic(self, name, user_name, password, topic_name, topic_message):
        print(name)
        try:
            #Login
            self.driver.get("https://school.moodledemo.net/login/index.php?lang=en")
            time.sleep(1)
            self.driver.find_element(By.ID, "username").send_keys(user_name)
            self.driver.find_element(By.ID, "password").send_keys(password)
            self.driver.find_element(By.ID, "loginbtn").click()
            time.sleep(1)

            # Access forum and click add topic
            self.driver.get("https://school.moodledemo.net/mod/forum/view.php?f=81")
            time.sleep(3)
            self.driver.find_element(By.LINK_TEXT, "Add discussion topic").click()
            time.sleep(2)

            # Input title
            self.driver.find_element(By.ID, "id_subject").send_keys(topic_name)
            time.sleep(2)
            
            # Input message
            self.driver.switch_to.frame('id_message_ifr')
            self.driver.find_element(By.ID, "tinymce").send_keys(topic_message)
            self.driver.switch_to.default_content()

            # Click btn submit
            self.driver.find_element(By.ID, "id_submitbutton").click()
            time.sleep(2)

            # Diff result
            messages = self.driver.find_element(By.CSS_SELECTOR, ".alert-success")
            return messages.text
        except:
            return "error happen"

    # @pytest.mark.parametrize 
    @pytest.mark.parametrize('function, name, user_name, password, topic_name, topic_message, expected_result',
                             rwe.read_from_excel(r'../test_data.xlsx', 'teacher_add_topic'))
    def test_func_add_topic(self, function, name, user_name, password, topic_name, topic_message, expected_result):
        expected = expected_result.split('|')[0]
        actual = self.add_topic( name, user_name, password, topic_name, topic_message).split('|')[0]

        # DIFF
        assert expected in actual

