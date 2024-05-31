from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Library():

    def explicit_wait_by_id(self, driver, locator):
        element_locator = (By.ID, locator)
        wait = (WebDriverWait(driver, 20).until(EC.presence_of_element_located(element_locator)))
        assert wait.is_displayed()

    def explicit_wait_by_xpath(self, driver, locator):
        element_locator = (By.XPATH, locator)
        wait = (WebDriverWait(driver, 10).until(EC.presence_of_element_located(element_locator)))
        assert wait.is_displayed()


