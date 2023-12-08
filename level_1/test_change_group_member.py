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
# test enrol users
class TestEnrolUsersLevel1:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()

    def teardown_method(self):
        self.driver.quit()
        print('\n')
    @pytest.mark.parametrize('function, url, user_name, password, GROUP, XPATH1, XPATH2, ACTION, RESULT1, RESULT2',
                             rwe.read_from_excel(r'../test_data.xlsx', 'change_group_member'))
    def test_change_member_auto(self,function, url, user_name, password, GROUP, XPATH1, XPATH2, ACTION, RESULT1, RESULT2):
        """test-case"""
        self.driver.get(url)    # data
        wait_element = WebDriverWait(self.driver, 5)

        # login
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a')))
        self.driver.find_element(By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a').click()

        wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-container")))
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()

        wait_element.until(EC.element_to_be_clickable((By.ID, "username")))
        self.driver.find_element(By.ID, "username").send_keys(user_name)  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "password")))
        self.driver.find_element(By.ID, "password").send_keys(password)  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
        self.driver.find_element(By.ID, "loginbtn").click()

        # to predetermined group selection path
        self.driver.get("https://school.moodledemo.net/group/index.php?id=72&group=0")
        wait_element = WebDriverWait(self.driver, 5)
        
        # Choose group
        dropdown = self.driver.find_element(By.ID, "groups")
        dropdown.find_element(By.XPATH, GROUP).click()
        
        # Choose member to change
        self.driver.find_element(By.ID, "showaddmembersform").click()
        if XPATH2 == '':
            dropdown = self.driver.find_element(By.ID, "addselect")
            prev1=dropdown.find_element(By.XPATH, XPATH1)
            prev1_value=prev1.get_attribute('value')
            prev1.click()
            time.sleep(2)
        else:
            dropdown = self.driver.find_element(By.ID, "addselect")
            prev1=dropdown.find_element(By.XPATH, XPATH1)
            prev1_value=prev1.get_attribute('value')
            prev1.click()
            time.sleep(2)
                
            dropdown = self.driver.find_element(By.ID, "addselect")
            prev2=dropdown.find_element(By.XPATH, XPATH2)
            prev2_value=prev2.get_attribute('value')
            prev2.click()
            time.sleep(2)
        self.driver.find_element(By.ID, ACTION).click()
        time.sleep(2)
        
        #assert with value before change
        if RESULT2 == '':
            result1 = self.driver.find_element(By.XPATH, RESULT1)
            assert result1.get_attribute('value') == prev1_value
        else:
            result1 = self.driver.find_element(By.XPATH, RESULT1).get_attribute('value')
            result2 = self.driver.find_element(By.XPATH, RESULT2).get_attribute('value')
            assert result1==prev1_value and result2==prev2_value
            