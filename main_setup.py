from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BaseClass:

    def __init__(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("https://katalon-demo-cura.herokuapp.com/")
        self.driver.maximize_window()

    def get_driver(self):
        return self.driver