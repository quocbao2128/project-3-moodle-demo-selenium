import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from flaky import flaky

# level 0 - hard code data vào từng test case, không lấy data bên ngoài vào
# test enrol users
class TestEnrolUsersLevel0:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()

    def teardown_method(self):
        self.driver.quit()
        print('\n')

    # @flaky được sử dụng để chạy lại test case nếu fail, vì ứng dụng Moodle demo hoạt động không ổn định.
    # (Ứng dụng hoạt động không ổn định có thể trả về kết quả khác nhau khi chạy trên cùng 1 dòng trong data.)
    # Test case sẽ chạy tối đa 2 lần (max_runs), yêu cầu tối thiểu phải pass 1 lần (min_passes) với mỗi dòng trong data.
    @flaky(max_runs=2, min_passes=1)
    def test_enrol_users_select_users(self):
        """test-case"""
        self.driver.get("https://school.moodledemo.net/my/courses.php")    # data
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
        self.driver.find_element(By.ID, "username").send_keys("teacher")  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "password")))
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys("moodle")  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()

        # choose a course
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-container-0"]/div/div/div[2]/a')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="page-container-0"]/div/div/div[2]/a').click()

        # click participants tab
        wait_element.until(EC.element_to_be_clickable((By.XPATH, "//*//li[@data-key='participants']")))
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*//li[@data-key='participants']").click()

        # click Enrol users button
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="enrolusersbutton-1"]')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="enrolusersbutton-1"]').click()

        # select users
        time.sleep(2)
        button = self.driver.find_element(By.XPATH, '//*[@id="fitem_id_userlist"]//div[2]//div[3]//span')
        self.driver.execute_script("arguments[0].click();", button)

        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fitem_id_userlist"]//div[@data-fieldtype="autocomplete"]//ul//li[3]')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="fitem_id_userlist"]//div[@data-fieldtype="autocomplete"]//ul//li[3]').click()

        # select cohorts
        time.sleep(2)
        button = self.driver.find_element(By.XPATH, '//*[@id="fitem_id_cohortlist"]//div[2]//div[3]//span')
        self.driver.execute_script("arguments[0].click();", button)

        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fitem_id_cohortlist"]//ul//li[5]')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="fitem_id_cohortlist"]//ul//li[5]').click()

        # assign role
        time.sleep(2)
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_roletoassign"]')
        select = Select(select_element)
        select.select_by_visible_text('Student')  # data
        time.sleep(2)

        # click enrol selected users and cohorts button
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="modal-footer"]//button[@data-action="save"]')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@class="modal-footer"]//button[@data-action="save"]').click()

        # get number of users enrolled
        num_user_enrolled = wait_element.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "toast-message")]'))).text
        time.sleep(3)
        print(num_user_enrolled)

        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert num_user_enrolled in "1 enrolled users"

    def test_enrol_users_not_select_users(self):
        self.driver.get("https://school.moodledemo.net/my/courses.php")    # data
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
        self.driver.find_element(By.ID, "username").send_keys("teacher")  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "password")))
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys("moodle")  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()

        # choose a course
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-container-0"]/div/div/div[2]/a')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="page-container-0"]/div/div/div[2]/a').click()

        # click participants tab
        wait_element.until(EC.element_to_be_clickable((By.XPATH, "//*//li[@data-key='participants']")))
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*//li[@data-key='participants']").click()

        # click Enrol users button
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="enrolusersbutton-1"]')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="enrolusersbutton-1"]').click()

        # select users
        # time.sleep(2)
        # button = self.driver.find_element(By.XPATH, '//*[@id="fitem_id_userlist"]//div[2]//div[3]//span')
        # self.driver.execute_script("arguments[0].click();", button)
        #
        # wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fitem_id_userlist"]//div[@data-fieldtype="autocomplete"]//ul//li[3]')))
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, '//*[@id="fitem_id_userlist"]//div[@data-fieldtype="autocomplete"]//ul//li[3]').click()

        # select cohorts
        time.sleep(2)
        button = self.driver.find_element(By.XPATH, '//*[@id="fitem_id_cohortlist"]//div[2]//div[3]//span')
        self.driver.execute_script("arguments[0].click();", button)

        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fitem_id_cohortlist"]//ul//li[5]')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="fitem_id_cohortlist"]//ul//li[5]').click()

        # assign role
        time.sleep(2)
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_roletoassign"]')
        select = Select(select_element)
        select.select_by_visible_text('Student')  # data
        time.sleep(2)

        # click enrol selected users and cohorts button
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="modal-footer"]//button[@data-action="save"]')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@class="modal-footer"]//button[@data-action="save"]').click()

        # get number of users enrolled
        num_user_enrolled = wait_element.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "toast-message")]'))).text
        time.sleep(3)
        print(num_user_enrolled)

        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert num_user_enrolled in "0 enrolled users"

