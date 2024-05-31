from Appointment_button import AppointmentButton
from login_page import *
from main_setup import BaseClass

class TestBaseClass:


    def test_click_apointment_button(self):
        base = BaseClass()
        driver = base.get_driver()

        appointment_button_instance = AppointmentButton(driver)
        appointment_button_instance.button_click()

        login_instance = LoginPage(driver)
        login_instance.enter_usename()
        login_instance.enter_password()
        login_instance.click_login_button()
