from commonLib import Library
from main_setup import *
from selenium.webdriver.common.by import By

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
        self.comment_message = "Comments"

    def verify_appointment_page(self):
        try:

            appointment_heading =  self.driver.find_element(By.XPATH, "//h2[contains(text(),'Make Appointment')]")
            appointment_header_text = appointment_heading.text
            assert appointment_header_text == self.appointment_header_message, f"Error in validation message, Expected Message: {self.appointment_header_message}, but got Actual Message: {appointment_header_text} "
        except Exception as e:
            self.driver.get_screenshot_as_file('appointment_heading.png')
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
            self.driver.get_screenshot_as_file('webpage_element.png')
            print(f"Appointment Page element Error: {e} ")
            raise