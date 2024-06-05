import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from commonLib import Library

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.commonLib = Library()

    def copy_paste(self, first_locator, second_locator):
        try:
            first_element_locator = self.driver.find_element(By.XPATH, first_locator)
            first_element_locator.send_keys(Keys.CONTROL, "a")
            first_element_locator.send_keys(Keys.CONTROL, "c")
            second_element_locator = self.driver.find_element(By.XPATH, second_locator)
            second_element_locator.send_keys(Keys.CONTROL, "v")
        except Exception as e:
            print(f"Copy and Paste Exception Error: {e}")
            raise

    def enter_usename(self):
        try:
            self.copy_paste("//input[@aria-describedby='demo_username_label'][@placeholder='Username']", "//input[@id='txt-username'][@placeholder='Username']")
        except Exception as e:
            print(f"UserName Exception Error: {e}")
            raise

    def enter_password(self):
        try:
            self.copy_paste("//*[@id='login']/div/div/div[2]/form/div[1]/div[2]/div/div/input","//*[@id='txt-password']")
        except Exception as e:
            print(f"Password Exception Error: {e}")
            raise

    def click_login_button(self):
        try:
            login_button = self.driver.find_element(By.ID, "btn-login")
            self.commonLib.explicit_wait_by_id(self.driver, "btn-login")
            login_button.click()
        except Exception as e:
            print(f"Login Button Exception Error: {e}")
            raise