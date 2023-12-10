import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


# level 0 - hard code data vào từng test case, không lấy data bên ngoài vào
# test enrol users
class TestEnrolUsersLevel0:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()

    def teardown_method(self):
        self.driver.quit()
        print('\n')

    def test_add_1_member(self):
        """test-case"""
        self.driver.get("https://school.moodledemo.net/my/courses.php")    # data
        wait_element = WebDriverWait(self.driver, 5)

        # login
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a')))
        self.driver.find_element(By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a').click()

        wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-container")))
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()

        wait_element.until(EC.element_to_be_clickable((By.ID, "username")))
        self.driver.find_element(By.ID, "username").send_keys("teacher")  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "password")))
        self.driver.find_element(By.ID, "password").send_keys("moodle")  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
        self.driver.find_element(By.ID, "loginbtn").click()

        # to predetermined group selection path
        self.driver.get("https://school.moodledemo.net/group/index.php?id=72&group=0")
        wait_element = WebDriverWait(self.driver, 5)
        
        # Choose group
        dropdown = self.driver.find_element(By.ID, "groups")
        XPATH='/html/body/div[2]/div[4]/div/div[3]/div/section/div/form/div/div/div[1]/div[1]/select/option[1]'
        dropdown.find_element(By.XPATH, XPATH).click()
        
        # Choose member to add
        self.driver.find_element(By.ID, "showaddmembersform").click()
        dropdown = self.driver.find_element(By.ID, "addselect")
        XPATH='/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/form/div/table/tbody/tr[1]/td[3]/div/select/optgroup/option[1]'
        prev=dropdown.find_element(By.XPATH, XPATH)
        prev_value=prev.get_attribute('value')
        prev.click()
        time.sleep(2)
        self.driver.find_element(By.ID, "add").click()
        time.sleep(2)
        
        #assert with value before change
        XPATH='/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/form/div/table/tbody/tr[1]/td[1]/div/select/optgroup[2]/option[5]'
        result = self.driver.find_element(By.XPATH, XPATH)
        assert result.get_attribute('value') == prev_value
        

    def test_remove_1_member(self):
        """test-case"""
        self.driver.get("https://school.moodledemo.net/my/courses.php")    # data
        wait_element = WebDriverWait(self.driver, 5)

        # login
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a')))
        self.driver.find_element(By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a').click()

        wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-container")))
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()

        wait_element.until(EC.element_to_be_clickable((By.ID, "username")))
        self.driver.find_element(By.ID, "username").send_keys("teacher")  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "password")))
        self.driver.find_element(By.ID, "password").send_keys("moodle")  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
        self.driver.find_element(By.ID, "loginbtn").click()

        # to predetermined group selection path
        self.driver.get("https://school.moodledemo.net/group/index.php?id=72&group=0")
        wait_element = WebDriverWait(self.driver, 5)
        
        # Choose group
        dropdown = self.driver.find_element(By.ID, "groups")
        XPATH='/html/body/div[2]/div[4]/div/div[3]/div/section/div/form/div/div/div[1]/div[1]/select/option[1]'
        dropdown.find_element(By.XPATH, XPATH).click()
        
        # Choose member to remove
        self.driver.find_element(By.ID, "showaddmembersform").click()
        dropdown = self.driver.find_element(By.ID, "addselect")
        XPATH='/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/form/div/table/tbody/tr[1]/td[1]/div/select/optgroup[2]/option[5]'
        prev=dropdown.find_element(By.XPATH, XPATH)
        prev_value=prev.get_attribute('value')
        prev.click()
        time.sleep(2)
        self.driver.find_element(By.ID, "remove").click()
        time.sleep(2)
        
        #assert with value before change
        XPATH='/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/form/div/table/tbody/tr[1]/td[3]/div/select/optgroup/option[1]'
        result = self.driver.find_element(By.XPATH, XPATH)
        assert result.get_attribute('value') == prev_value
        
        
    def test_add_2_member(self):
        """test-case"""
        self.driver.get("https://school.moodledemo.net/my/courses.php")    # data
        wait_element = WebDriverWait(self.driver, 5)

        # login
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a')))
        self.driver.find_element(By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a').click()

        wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-container")))
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()

        wait_element.until(EC.element_to_be_clickable((By.ID, "username")))
        self.driver.find_element(By.ID, "username").send_keys("teacher")  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "password")))
        self.driver.find_element(By.ID, "password").send_keys("moodle")  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
        self.driver.find_element(By.ID, "loginbtn").click()

        # to predetermined group selection path
        self.driver.get("https://school.moodledemo.net/group/index.php?id=72&group=0")
        wait_element = WebDriverWait(self.driver, 5)
        
        # Choose group
        dropdown = self.driver.find_element(By.ID, "groups")
        XPATH='/html/body/div[2]/div[4]/div/div[3]/div/section/div/form/div/div/div[1]/div[1]/select/option[1]'
        dropdown.find_element(By.XPATH, XPATH).click()
        
        # choose 2 member to add
        self.driver.find_element(By.ID, "showaddmembersform").click()
        dropdown = self.driver.find_element(By.ID, "addselect")
        XPATH1='/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/form/div/table/tbody/tr[1]/td[3]/div/select/optgroup/option[1]'
        prev1=dropdown.find_element(By.XPATH, XPATH1)
        prev1_value=prev1.get_attribute('value')
        prev1.click()
        time.sleep(2)
        dropdown = self.driver.find_element(By.ID, "addselect")
        XPATH2='/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/form/div/table/tbody/tr[1]/td[3]/div/select/optgroup/option[2]'
        prev2=dropdown.find_element(By.XPATH, XPATH2)
        prev2_value=prev2.get_attribute('value')
        prev2.click()
        time.sleep(2)
        self.driver.find_element(By.ID, "add").click()
        time.sleep(2)

        
        #assert with value before change
        XPATH1='/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/form/div/table/tbody/tr[1]/td[1]/div/select/optgroup[2]/option[5]'
        result1 = self.driver.find_element(By.XPATH, XPATH1).get_attribute('value')
        XPATH2='/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/form/div/table/tbody/tr[1]/td[1]/div/select/optgroup[2]/option[6]'
        result2 = self.driver.find_element(By.XPATH, XPATH2).get_attribute('value')
        assert result1==prev1_value and result2==prev2_value    
        
            
    def test_remove_2_member(self):
        """test-case"""
        self.driver.get("https://school.moodledemo.net/my/courses.php")    # data
        wait_element = WebDriverWait(self.driver, 5)

        # login
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a')))
        self.driver.find_element(By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a').click()

        wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-container")))
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()

        wait_element.until(EC.element_to_be_clickable((By.ID, "username")))
        self.driver.find_element(By.ID, "username").send_keys("teacher")  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "password")))
        self.driver.find_element(By.ID, "password").send_keys("moodle")  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
        self.driver.find_element(By.ID, "loginbtn").click()

        # to predetermined group selection path
        self.driver.get("https://school.moodledemo.net/group/index.php?id=72&group=0")
        wait_element = WebDriverWait(self.driver, 5)
        
        # Choose group
        dropdown = self.driver.find_element(By.ID, "groups")
        XPATH='/html/body/div[2]/div[4]/div/div[3]/div/section/div/form/div/div/div[1]/div[1]/select/option[1]'
        dropdown.find_element(By.XPATH, XPATH).click()
        
        # choose 2 member to remove
        self.driver.find_element(By.ID, "showaddmembersform").click()
        dropdown = self.driver.find_element(By.ID, "addselect")
        XPATH1='/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/form/div/table/tbody/tr[1]/td[1]/div/select/optgroup[2]/option[5]'
        prev1=dropdown.find_element(By.XPATH, XPATH1)
        prev1_value=prev1.get_attribute('value')
        prev1.click()
        time.sleep(2)
        dropdown = self.driver.find_element(By.ID, "addselect")
        XPATH2='/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/form/div/table/tbody/tr[1]/td[1]/div/select/optgroup[2]/option[6]'
        prev2=dropdown.find_element(By.XPATH, XPATH2)
        prev2_value=prev2.get_attribute('value')
        prev2.click()
        time.sleep(2)
        self.driver.find_element(By.ID, "remove").click()
        time.sleep(2)

        
        #assert with value before change
        XPATH1='/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/form/div/table/tbody/tr[1]/td[3]/div/select/optgroup/option[1]'
        result1 = self.driver.find_element(By.XPATH, XPATH1).get_attribute('value')
        XPATH2='/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/form/div/table/tbody/tr[1]/td[3]/div/select/optgroup/option[2]'
        result2 = self.driver.find_element(By.XPATH, XPATH2).get_attribute('value')
        assert result1==prev1_value and result2==prev2_value