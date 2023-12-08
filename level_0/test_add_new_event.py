import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


# level 0 - hard code data vào từng test case, không lấy data bên ngoài vào
# test add new event
class TestAddNewEventLevel0:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()

    def teardown_method(self):
        self.driver.quit()
        print('\n')

    def test_add_new_event_success(self):
        """test-case"""
        self.driver.get("https://school.moodledemo.net/my/")
        wait_element = WebDriverWait(self.driver, 10)

        # login
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a').click()

        wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-container")))
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()

        wait_element.until(EC.element_to_be_clickable((By.ID, "username")))
        time.sleep(2)
        self.driver.find_element(By.ID, "username").send_keys("teacher")    # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "password")))
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys("moodle")     # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()

        # navigate to Dashboard page
        wait_element.until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a")))
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//li[2]/a").click()

        # click New event button
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".float-sm-right").click()
        time.sleep(2)

        # enter Even title
        self.driver.find_element(By.XPATH, '//*[@id="id_name"]').send_keys('test_title_add')    # title
        time.sleep(2)

        # choose day
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_day"]')
        select = Select(select_element)
        select.select_by_visible_text('1')   # data
        time.sleep(2)

        # choose month
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_month"]')
        select = Select(select_element)
        select.select_by_visible_text('November')  # data
        time.sleep(2)

        # choose year
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_year"]')
        select = Select(select_element)
        select.select_by_visible_text('2023')  # data
        time.sleep(2)

        # choose hour
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_hour"]')
        select = Select(select_element)
        select.select_by_visible_text('15')  # data
        time.sleep(2)

        # choose minute
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_minute"]')
        select = Select(select_element)
        select.select_by_visible_text('30')  # data
        time.sleep(2)

        # choose type
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_eventtype"]')
        select = Select(select_element)
        select.select_by_visible_text('User')  # data
        time.sleep(2)

        # click Save button
        self.driver.find_element(By.XPATH, "//button[contains(., 'Save')]").click()
        time.sleep(2)

        try:
            # get error text
            self.driver.find_element(By.XPATH, "//*[@role='document' and @tabindex='-1']")
            print('add new event')
            # ketQuaMongDoi so sanh voi ketQuaChayThucTe
            actual_result = True
            assert True is actual_result
        except NoSuchElementException:
            self.driver.find_element(By.XPATH, "//*[@role='document' and @tabindex='0']")
            print('empty title -> not add')
            # ketQuaMongDoi so sanh voi ketQuaChayThucTe
            actual_result = False
            assert False is actual_result

    # @pytest.mark.skip(reason="no way of currently testing this")
    def test_add_new_event_fail_1(self):
        """test-case"""
        self.driver.get("https://school.moodledemo.net/my/")    # data
        wait_element = WebDriverWait(self.driver, 10)

        # login
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="usernavigation"]/div[5]/div/span/a').click()

        wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-container")))
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()

        wait_element.until(EC.element_to_be_clickable((By.ID, "username")))
        time.sleep(2)
        self.driver.find_element(By.ID, "username").send_keys("teacher")    # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "password")))
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys("moodle")     # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()

        # navigate to Dashboard page
        wait_element.until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a")))
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//li[2]/a").click()

        # click New event button
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".float-sm-right").click()
        time.sleep(2)

        # enter Even title
        self.driver.find_element(By.XPATH, '//*[@id="id_name"]').send_keys('')    # empty title
        time.sleep(2)

        # choose day
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_day"]')
        select = Select(select_element)
        select.select_by_visible_text('1')   # data
        time.sleep(2)

        # choose month
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_month"]')
        select = Select(select_element)
        select.select_by_visible_text('November')  # data
        time.sleep(2)

        # choose year
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_year"]')
        select = Select(select_element)
        select.select_by_visible_text('2023')  # data
        time.sleep(2)

        # choose hour
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_hour"]')
        select = Select(select_element)
        select.select_by_visible_text('15')  # data
        time.sleep(2)

        # choose minute
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_minute"]')
        select = Select(select_element)
        select.select_by_visible_text('30')  # data
        time.sleep(2)

        # choose type
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_eventtype"]')
        select = Select(select_element)
        select.select_by_visible_text('User')  # data
        time.sleep(2)

        # click Save button
        self.driver.find_element(By.XPATH, "//button[contains(., 'Save')]").click()
        time.sleep(2)

        try:
            # get error text
            self.driver.find_element(By.XPATH, "//*[@role='document' and @tabindex='-1']")
            print('add new event')
            # ketQuaMongDoi so sanh voi ketQuaChayThucTe
            actual_result = True
            assert True is actual_result
        except NoSuchElementException:
            self.driver.find_element(By.XPATH, "//*[@role='document' and @tabindex='0']")
            print('empty title -> not add')
            # ketQuaMongDoi so sanh voi ketQuaChayThucTe
            actual_result = False
            assert False is actual_result

