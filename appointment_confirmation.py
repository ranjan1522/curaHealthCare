from commonLib import Library
from main_setup import *
from selenium.webdriver.common.by import By
from pytest_html_reporter import attach
class appointment_confirmation(BaseClass):
        def __init__(self, driver):
         #super().__init__()
         #self.driver = BaseClass.get_driver()
         self.driver = driver
         self.commonLib = Library()

        def verify_confirmation_url(self):
            try:
                confirmation_page_url = self.driver.current_url
                assert confirmation_page_url == "https://katalon-demo-cura.herokuapp.com/appointment.php#summary", "Confirmation page url is wrong"
            except Exception as e:
                attach(data=self.driver.get_screenshot_as_png())
                print(f"Exception in Confirmation page url: {e}")
                raise

        def verify_first_heading(self):
            try:
                first_heading = self.driver.find_element(By.XPATH, "//*[@id='summary']/div/div/div[1]/h2")
                assert first_heading.text == 'Appointment Confirmation', "Confirmation page first heading is wrong"
            except Exception as e:
                attach(data=self.driver.get_screenshot_as_png())
                print(f"First heading error occurs: {e} ")
                raise

        def verify_second_heading(self):
            try:
                second_heading = self.driver.find_element(By.XPATH, "//*[@id='summary']/div/div/div[1]/p")
                assert second_heading.text == "Please be informed that your appointment has been booked as following:", "Second heading mismatch"
            except Exception as e:
                attach(data=self.driver.get_screenshot_as_png())
                print(f"Second Heading error: {e}")
                raise

        def verify_submitted_element(self):
            try:
                facility_value = self.driver.find_element(By.ID, "facility")
                hospital_readmission_value = self.driver.find_element(By.ID, "hospital_readmission")
                program_value = self.driver.find_element(By.ID, "program")
                visit_date_value = self.driver.find_element(By.ID, "visit_date")
                comment_value = self.driver.find_element(By.ID, "comment")

                # asserting the element
                assert facility_value.text == 'Hongkong CURA Healthcare Center', "Facility Value mismatch"
                assert hospital_readmission_value.text == 'Yes', "Hospital Readmission Value mismatch"
                assert program_value.text == 'Medicaid', "Program Value mismatch"
                assert visit_date_value.text == '22/06/2024', "Visit Date Value mismatch"
                assert comment_value.text == 'Testing purpose', "Comment Value mismatch"
            except Exception as e:
                attach(data=self.driver.get_screenshot_as_png())
                print(f"Submitted value error: {e}")
                raise

        def verify_all_web_element(self):
            try:
                facility_element = self.driver.find_element(By.XPATH, "//label[@for='facility']")
                hospital_readmission_element = self.driver.find_element(By.XPATH, "//label[@for='hospital_readmission']")
                program_element = self.driver.find_element(By.XPATH, "//label[@for='program']")
                visit_date_element = self.driver.find_element(By.XPATH, "//label[@for='visit_date']")
                comment_element = self.driver.find_element(By.XPATH, "//label[@for='comment']")

                # asserting the element
                assert facility_element.text == 'Facility', "Facility Text Value mismatch"
                assert hospital_readmission_element.text == 'Apply for hospital readmission', "Apply for hospital readmission Text mismatch"
                assert program_element.text == 'Healthcare Program', "Healthcare Program Text  mismatch"
                assert visit_date_element.text == 'Visit Date', "Visit Date Text  mismatch"
                assert comment_element.text == 'Comment', "Comment Text  mismatch"
            except Exception as e:
                attach(data=self.driver.get_screenshot_as_png())
                print(f"Web page Element error: {e}")
                raise






