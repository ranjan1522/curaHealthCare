from commonLib import Library
from main_setup import *
from selenium import webdriver
from selenium.webdriver.common.by import By


class Appointment_Process():
    def __init__(self, driver):
        #super().__init__()
        #self.driver = BaseClass.get_driver()
        self.driver = driver
        self.commonLib = Library()

    def verify_appointment_page(self):
        try:
            expected_message = "Make Appointment"
            appointment_heading =  self.driver.find_element(By.XPATH, "//h2[contains(text(),'Make Appointment')]")
            appointment_header_text = appointment_heading.text
            assert appointment_header_text == expected_message, f"Error in validation message, Expected Message: {expected_message}, but got Actual Message: {appointment_header_text} "
        except Exception as e:
            print(f"Verify Appointment Page Error: {e} ")

    def verify_webpage_element(self):
        try:
            facility_element = self.driver.find_element(By.XPATH, "//*[@id='appointment']/div/div/form/div[1]/label")
            health_program_element = self.driver.find_element(By.XPATH, "//*[@id='appointment']/div/div/form/div[3]/label")
            vist_date_element = self.driver.find_element(By.XPATH, "//*[@id='appointment']/div/div/form/div[4]/label")
            comment_element = self.driver.find_element(By.XPATH, "//*[@id='appointment']/div/div/form/div[5]/label")
            assert facility_element.text == 'Facility'
            assert health_program_element.text == 'Healthcare Program'
            assert vist_date_element.text == 'Visit Date (Required)'
            assert comment_element.text == 'Comment'
        except Exception as e:
            print(f"Appointment Page element Error: {e} ")

