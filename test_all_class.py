from Appointment_button import AppointmentButton
from Logout import Logout
from appointment_confirmation import appointment_confirmation
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
        appointment_process_instance.select_facility_option()
        appointment_process_instance.select_checkbox()
        appointment_process_instance.select_health_radio_button()
        appointment_process_instance.select_calendar()
        appointment_process_instance.appointmnet_comment()
        appointment_process_instance.click_on_book_appointment_button()

    def test_appointment_confirmation(self):
        appointment_confirmation_instance = appointment_confirmation(self.driver)
        appointment_confirmation_instance.verify_confirmation_url()
        appointment_confirmation_instance.verify_first_heading()
        appointment_confirmation_instance.verify_second_heading()
        appointment_confirmation_instance.verify_all_web_element()
        appointment_confirmation_instance.verify_submitted_element()

    def test_logout(self):
        logout_instance = Logout(self.driver)
        logout_instance.click_on_menu()
        logout_instance.click_on_logout()