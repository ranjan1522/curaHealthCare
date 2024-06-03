from Appointment_button import AppointmentButton
from login_page import *
from main_setup import BaseClass
from appointment_process import *
import pytest

class TestBaseClass:

    base = BaseClass()
    driver = base.get_driver()

    def test_click_apointment_button(self):
        appointment_button_instance = AppointmentButton(self.driver)
        appointment_button_instance.button_click()

    def test_login_process_button(self):
        login_instance = LoginPage(self.driver)
        login_instance.enter_usename()
        login_instance.enter_password()
        login_instance.click_login_button()

    def test_appointment_process_button(self):
        appointment_process_instance = Appointment_Process(self.driver)
        appointment_process_instance.verify_appointment_page()
        appointment_process_instance.verify_webpage_element()