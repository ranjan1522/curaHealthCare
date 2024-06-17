from allure_commons._allure import attach

from main_setup import BaseClass
from selenium.webdriver.common.by import By
from commonLib import *

class Logout():
    def __init__(self, driver):
        #super().__init__()
        #self.driver = BaseClass.get_driver()
        self.driver = driver
        self.commonLib = Library()


    def click_on_menu(self):
        try:
            self.commonLib.explicit_wait_by_xpath(self.driver, "//*[@id='menu-toggle']/i")
            menu_element = self.driver.find_element(By.XPATH, "//*[@id='menu-toggle']/i")
            menu_element.click()
        except Exception as e:
            attach(data=self.driver.get_screenshot_as_png())
            print(f"Menu item error: {e}")
            raise

    def click_on_logout(self):
        try:
            self.commonLib.explicit_wait_by_xpath(self.driver, "//a[@href='authenticate.php?logout']")
            logout_element = self.driver.find_element(By.XPATH, "//a[@href='authenticate.php?logout']")
            logout_element.click()
        except Exception as e:
            attach(data=self.driver.get_screenshot_as_png())
            print(f"Logout error: {e}")
            raise