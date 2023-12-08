import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import read_write_excel as rwe


# level 1 - test case nhận data dưới dạng tham số truyền vào
# test add new event
class TestAddNewEventLevel1:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()

    def teardown_method(self):
        self.driver.quit()
        print('\n')

    # @pytest.mark.parametrize được sử dụng để chạy test case, data có n dòng thì test case chạy n lần.
    @pytest.mark.parametrize('function, url, user_name, password, event_title, date, ttype, expected_result',
                             rwe.read_from_excel(r'../test_data.xlsx', 'add_new_event'))
    def test_add_new_event(self, function, url, user_name, password, event_title, date, ttype, expected_result):
        """test-case"""
        date = date.split('-')

        self.driver.get(url)
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
        self.driver.find_element(By.ID, "username").send_keys(user_name)

        wait_element.until(EC.element_to_be_clickable((By.ID, "password")))
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(password)

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
        self.driver.find_element(By.XPATH, '//*[@id="id_name"]').send_keys(event_title)  # title
        time.sleep(2)

        # choose day
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_day"]')
        select = Select(select_element)
        select.select_by_visible_text(str(int(date[0])))  # data
        time.sleep(2)

        # choose month
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_month"]')
        select = Select(select_element)
        select.select_by_visible_text(date[1])  # data
        time.sleep(2)

        # choose year
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_year"]')
        select = Select(select_element)
        select.select_by_visible_text(date[2])  # data
        time.sleep(2)

        # choose hour
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_hour"]')
        select = Select(select_element)
        select.select_by_visible_text(date[3])  # data
        time.sleep(2)

        # choose minute
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_timestart_minute"]')
        select = Select(select_element)
        select.select_by_visible_text(date[4])  # data
        time.sleep(2)

        # choose type
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_eventtype"]')
        select = Select(select_element)
        select.select_by_visible_text(ttype)  # data
        time.sleep(2)

        # click Save button
        self.driver.find_element(By.XPATH, "//button[contains(., 'Save')]").click()
        time.sleep(2)

        try:
            # get error text
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@role='document' and @tabindex='-1']")
            actual_result = 'Add'
            print('add new event')
        except NoSuchElementException:
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@role='document' and @tabindex='0']")
            actual_result = 'Not add'
            print('empty title -> not add')
        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert expected_result in actual_result
