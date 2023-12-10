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

    def test_create_group_all_complete(self):
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
        self.driver.get('https://school.moodledemo.net/group/index.php?id=72')
        wait_element = WebDriverWait(self.driver, 5)
        
        # click Create group
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="showcreateorphangroupform"]').click()
        
        # add Group name
        wait_element.until(EC.element_to_be_clickable((By.ID, "id_name")))
        time.sleep(2)
        self.driver.find_element(By.ID, "id_name").send_keys("a") 
        
        # add Group ID number
        wait_element.until(EC.element_to_be_clickable((By.ID, "id_idnumber")))
        time.sleep(2)
        self.driver.find_element(By.ID, "id_idnumber").send_keys("a") 
        
        # add Group 
        time.sleep(2)
        self.driver.switch_to.frame(0)
        wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "html")))
        self.driver.find_element(By.CSS_SELECTOR, "html").click()
        element = self.driver.find_element(By.ID, "tinymce")
        time.sleep(2)
        innertext='a'
        #script='if(arguments[0].contentEditable === \'true\') {arguments[0].innerText = \'<p>' + innertext + '</p>\'}'
        #print(script)
        element.send_keys("a") 
        #self.driver.execute_script(script, element)
        self.driver.switch_to.default_content()
        time.sleep(2)
        
        # add Enrolment key
        #wait_element.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"yui_3_18_1_1_1701847506480_164\"]/a[1]/span/span/em")))
        #self.driver.find_element(By.XPATH, "//*[@id=\"page-group-group\"]").click()
        #wait_element.until(EC.element_to_be_clickable((By.ID, "id_enrolmentkey")))
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "em").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"id_enrolmentkey\"]").send_keys("a")
        
        # choose Group membership visibility
        time.sleep(2)
        wait_element.until(EC.element_to_be_clickable((By.ID, "id_visibility")))
        self.driver.find_element(By.ID, "id_visibility").click()
        dropdown = self.driver.find_element(By.ID, "id_visibility")
        option='Only visible to members'
        XPATH = '//option[. = \'' + option + '\']'
        wait_element.until(EC.element_to_be_clickable((By.XPATH, XPATH)))
        dropdown.find_element(By.XPATH, XPATH).click()
        
        # choose Group messaging
        time.sleep(2)
        wait_element.until(EC.element_to_be_clickable((By.ID, "id_enablemessaging")))
        self.driver.find_element(By.ID, "id_enablemessaging").click()
        dropdown = self.driver.find_element(By.ID, "id_enablemessaging")
        option = 'Yes'
        XPATH1 = '//option[. = \'' + option + '\']'
        wait_element.until(EC.element_to_be_clickable((By.XPATH, XPATH1)))
        dropdown.find_element(By.XPATH, XPATH1).click()
        
        # choose Image source
        
        # Submit
        time.sleep(2)
        wait_element.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        self.driver.find_element(By.ID, "id_submitbutton").click()
        
        # get title
        get_url= self.driver.current_url

        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert 'index.php' in get_url

    def test_delete_group(self):
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
        
        # Choose delete
        self.driver.find_element(By.ID, "deletegroup").click()
        XPATH1='/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/div/div[3]/div/div[2]/form/button'
        self.driver.find_element(By.XPATH, XPATH1).click()
        time.sleep(2)
        
        #assert with value before change
        RESULT='/html/body/div[2]/div[4]/div/div[3]/div/section/div/form/div/div/div[1]/div[1]/select/option[1]'
        result = self.driver.find_element(By.XPATH, RESULT)
        assert result.get_attribute('value') == '57'




    def test_create_group_missing_ID_name_failed(self):
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
        self.driver.get('https://school.moodledemo.net/group/index.php?id=72')
        wait_element = WebDriverWait(self.driver, 5)
        
        # click Create group
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="showcreateorphangroupform"]').click()
        
        # add Group name
        wait_element.until(EC.element_to_be_clickable((By.ID, "id_name")))
        time.sleep(2)
        self.driver.find_element(By.ID, "id_name").send_keys("") 
        
        # add Group ID number
        wait_element.until(EC.element_to_be_clickable((By.ID, "id_idnumber")))
        time.sleep(2)
        self.driver.find_element(By.ID, "id_idnumber").send_keys("") 
        
        # add Group 
        time.sleep(2)
        self.driver.switch_to.frame(0)
        wait_element.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "html")))
        self.driver.find_element(By.CSS_SELECTOR, "html").click()
        element = self.driver.find_element(By.ID, "tinymce")
        time.sleep(2)
        innertext='a'
        #script='if(arguments[0].contentEditable === \'true\') {arguments[0].innerText = \'<p>' + innertext + '</p>\'}'
        #print(script)
        element.send_keys("a") 
        #self.driver.execute_script(script, element)
        self.driver.switch_to.default_content()
        time.sleep(2)
        
        # add Enrolment key
        #wait_element.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"yui_3_18_1_1_1701847506480_164\"]/a[1]/span/span/em")))
        #self.driver.find_element(By.XPATH, "//*[@id=\"page-group-group\"]").click()
        #wait_element.until(EC.element_to_be_clickable((By.ID, "id_enrolmentkey")))
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "em").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"id_enrolmentkey\"]").send_keys("a")
        
        # choose Group membership visibility
        time.sleep(2)
        wait_element.until(EC.element_to_be_clickable((By.ID, "id_visibility")))
        self.driver.find_element(By.ID, "id_visibility").click()
        dropdown = self.driver.find_element(By.ID, "id_visibility")
        option='Only visible to members'
        XPATH = '//option[. = \'' + option + '\']'
        wait_element.until(EC.element_to_be_clickable((By.XPATH, XPATH)))
        dropdown.find_element(By.XPATH, XPATH).click()
        
        # choose Group messaging
        time.sleep(2)
        wait_element.until(EC.element_to_be_clickable((By.ID, "id_enablemessaging")))
        self.driver.find_element(By.ID, "id_enablemessaging").click()
        dropdown = self.driver.find_element(By.ID, "id_enablemessaging")
        option = 'Yes'
        XPATH1 = '//option[. = \'' + option + '\']'
        wait_element.until(EC.element_to_be_clickable((By.XPATH, XPATH1)))
        dropdown.find_element(By.XPATH, XPATH1).click()
        
        # choose Image source
        
        # Submit
        time.sleep(2)
        wait_element.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        self.driver.find_element(By.ID, "id_submitbutton").click()
        
        # get title
        get_url= self.driver.current_url

        # ketQuaMongDoi so sanh voi ketQuaChayThucTe
        assert 'group.php' in get_url
