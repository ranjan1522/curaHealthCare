import time

from selenium.webdriver.common.by import By
from main_setup import BaseClass
from commonLib import Library

class AppointmentButton():
    def __init__(self, driver):
       # super().__init__()
        self.driver = driver
        self.commonLib = Library()

    def button_click(self):
        try:
            appointment_button = self.driver.find_element(By.ID, "btn-make-appointment")
            self.commonLib.explicit_wait_by_id(self.driver, "btn-make-appointment")
            appointment_button.click()
        except Exception as e:
            print(f"Appointment Exception Error: {e}")
        time.sleep(10)
