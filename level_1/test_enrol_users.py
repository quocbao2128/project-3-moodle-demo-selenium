import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from flaky import flaky
import read_write_excel as rwe


# level 1 - test case nhận data dưới dạng tham số truyền vào
# test enrol users
class TestEnrolUsersLevel1:
    def setup_method(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--lang=en-GB")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.delete_all_cookies()
        print('\n')

    def teardown_method(self):
        self.driver.quit()
        print('\n')

    # @pytest.mark.parametrize được sử dụng để chạy lặp lại test case, data có n dòng thì test case chạy n lần.
    # @flaky được sử dụng để chạy lại test case nếu fail, vì ứng dụng Moodle demo hoạt động không ổn định.
    # (Ứng dụng hoạt động không ổn định có thể trả về kết quả khác nhau khi chạy trên cùng 1 dòng trong data.)
    # Test case sẽ chạy tối đa 2 lần (max_runs), yêu cầu tối thiểu phải pass 1 lần (min_passes) với mỗi dòng trong data.
    @flaky(max_runs=2, min_passes=1)
    @pytest.mark.parametrize('function, url, user_name, password, course_index, select_users, assign_role, expected_result',
                             rwe.read_from_excel(r'../test_data.xlsx', 'enrol_users'))
    def test_enrol_users(self, function, url, user_name, password, course_index, select_users, assign_role, expected_result):
        """test-case"""
        self.driver.get(url)    # data
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
        self.driver.find_element(By.ID, "username").send_keys(user_name)  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "password")))
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(password)  # data

        wait_element.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
        time.sleep(2)
        self.driver.find_element(By.ID, "loginbtn").click()

        # choose a course
        wait_element.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="page-container-0"]/div/div/div[{str(course_index)}]/a')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, f'//*[@id="page-container-0"]/div/div/div[{str(course_index)}]/a').click()      # data

        # click participants tab
        wait_element.until(EC.element_to_be_clickable((By.XPATH, "//*//li[@data-key='participants']")))
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*//li[@data-key='participants']").click()

        # click Enrol users button
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="enrolusersbutton-1"]')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="enrolusersbutton-1"]').click()

        # select users
        if select_users == 'select':
            time.sleep(3)
            button = self.driver.find_element(By.XPATH, '//*[@id="fitem_id_userlist"]//div[2]//div[3]//span')
            self.driver.execute_script("arguments[0].click();", button)

            wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fitem_id_userlist"]//div[@data-fieldtype="autocomplete"]//ul//li[3]')))
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="fitem_id_userlist"]//div[@data-fieldtype="autocomplete"]//ul//li[3]').click()
        elif select_users == 'not select':
            pass

        # click outside to close autocomplete
        wait_element.until(EC.element_to_be_clickable((By.XPATH, "//h3[contains(text(), 'Enrolment options')]")))
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//h3[contains(text(), 'Enrolment options')]").click()

        # select cohorts
        time.sleep(2)
        button = self.driver.find_element(By.XPATH, '//*[@id="fitem_id_cohortlist"]//div[2]//div[3]//span')
        self.driver.execute_script("arguments[0].click();", button)

        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fitem_id_cohortlist"]//ul//li[5]')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="fitem_id_cohortlist"]//ul//li[5]').click()

        wait_element.until(EC.element_to_be_clickable((By.XPATH, "//h3[contains(text(), 'Enrolment options')]")))
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//h3[contains(text(), 'Enrolment options')]").click()

        # assign role
        time.sleep(2)
        select_element = self.driver.find_element(By.XPATH, '//*[@id="id_roletoassign"]')
        select = Select(select_element)
        select.select_by_visible_text(assign_role)  # data
        time.sleep(2)

        # click enrol selected users and cohorts button
        wait_element.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="modal-footer"]//button[@data-action="save"]')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@class="modal-footer"]//button[@data-action="save"]').click()

        # get number of users enrolled
        num_user_enrolled = wait_element.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "toast-message")]'))).text
        time.sleep(3)
        print('\n', num_user_enrolled)

        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert expected_result in num_user_enrolled

