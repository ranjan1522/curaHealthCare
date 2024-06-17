from selenium.webdriver.support.select import Select
from commonLib import Library
from main_setup import *
from selenium.webdriver.common.by import By
from pytest_html_reporter import attach

class Appointment_Process():

    def __init__(self, driver):
        #super().__init__()
        #self.driver = BaseClass.get_driver()
        self.driver = driver
        self.commonLib = Library()

        # Validation Messages
        self.appointment_header_message = "Make Appointment"
        self.facility_message = "Facility"
        self.health_program_message = "Healthcare Program"
        self.vist_date_message = "Visit Date (Required)"
        self.comment_message = "Comment"
    def verify_appointment_page(self):
        try:
            self.commonLib.explicit_wait_by_xpath(self.driver, "//h2[contains(text(),'Make Appointment')]")
            appointment_heading =  self.driver.find_element(By.XPATH, "//h2[contains(text(),'Make Appointment')]")
            appointment_header_text = appointment_heading.text
            assert appointment_header_text == self.appointment_header_message, f"Error in validation message, Expected Message: {self.appointment_header_message}, but got Actual Message: {appointment_header_text} "
        except Exception as e:
            attach(data=self.driver.get_screenshot_as_png())
            print(f"Verify Appointment Page Error: {e} ")
            raise

    def verify_webpage_element(self):
        try:
            facility_element = self.driver.find_element(By.XPATH, "//*[@id='appointment']/div/div/form/div[1]/label")
            health_program_element = self.driver.find_element(By.XPATH, "//*[@id='appointment']/div/div/form/div[3]/label")
            vist_date_element = self.driver.find_element(By.XPATH, "//*[@id='appointment']/div/div/form/div[4]/label")
            comment_element = self.driver.find_element(By.XPATH, "//*[@id='appointment']/div/div/form/div[5]/label")
            assert facility_element.text == self.facility_message, f"Actual Value: {facility_element.text} does not match with Expected Value: {self.facility_message}"
            assert health_program_element.text == self.health_program_message, f"Actual Value: {health_program_element.text} does not match with Expected Value: {self.health_program_message}"
            assert vist_date_element.text == self.vist_date_message, f"Actual Value: {vist_date_element.text} does not match with Expected Value: {self.vist_date_message}"
            assert comment_element.text == self.comment_message, f"Actual Value: {comment_element.text} does not match with Expected Value: {self.comment_message}"
        except Exception as e:
            attach(data=self.driver.get_screenshot_as_png())
            print(f"Appointment Page element Error: {e} ")
            raise

    def select_facility_option(self):
        try:
            self.commonLib.explicit_wait_by_id(self.driver, "combo_facility")
            select = Select(self.driver.find_element(By.ID, "combo_facility"))
            select.select_by_value("Hongkong CURA Healthcare Center")
        except Exception as e:
            attach(data=self.driver.get_screenshot_as_png())
            print(f"Facility drop down element Error: {e} ")
            raise

    def select_checkbox(self):
        try:
            self.commonLib.explicit_wait_by_id(self.driver, "chk_hospotal_readmission")
            select_check_box = self.driver.find_element(By.ID, "chk_hospotal_readmission")
            select_check_box.click()
        except Exception as e:
            attach(data=self.driver.get_screenshot_as_png())
            print(f"Select checkbox error: {e}")
            raise

    def select_health_radio_button(self):
        try:
            radio_value = 'medicaid'
            radio_locator = f"//*[@id='radio_program_{radio_value}']"
            self.commonLib.explicit_wait_by_xpath(self.driver, radio_locator)
            health_radio_button = self.driver.find_element(By.XPATH, radio_locator)
            health_radio_button.click()
        except Exception as e:
            attach(data=self.driver.get_screenshot_as_png())
            print(f"Radio button error: {e}")
            raise

    def select_calendar(self):
        try:
            day_value = 22
            date_picker = f"//td[@class = 'day' and text()='{day_value}']"
            date_picker_locator = self.driver.find_element(By.XPATH, "//*[@id='appointment']/div/div/form/div[4]/div/div/div/span")
            date_picker_locator.click()
            self.commonLib.explicit_wait_by_xpath(self.driver, date_picker)
            date_selection = self.driver.find_element(By.XPATH, date_picker)
            date_selection.click()
        except Exception as e:
            attach(data=self.driver.get_screenshot_as_png())
            print(f"Calendar error: {e}")
            raise

    def appointmnet_comment(self):
        try:
            self.commonLib.explicit_wait_by_id(self.driver, "txt_comment")
            comment_locator = self.driver.find_element(By.ID, "txt_comment")
            comment_locator.send_keys("Testing purpose")
        except Exception as e:
            attach(data=self.driver.get_screenshot_as_png())
            print(f"Comment Error: {e}")
            raise

    def click_on_book_appointment_button(self):
        try:
            self.commonLib.explicit_wait_by_id(self.driver, "btn-book-appointment")
            book_appointment_button = self.driver.find_element(By.ID, "btn-book-appointment")
            book_appointment_button.click()
        except Exception as e:
            attach(data=self.driver.get_screenshot_as_png())
            print(f"book Appointment Error: {e}")
            raise