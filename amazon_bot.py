from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import re
import time


class AmazonBot(object):
    
    def __init__(self, items):
        self.amazon_url = "https://www.amazon.com/"
        self.items = items

        self.profile = webdriver.FirefoxProfile()
        self.options = Options()
        self.driver = webdriver.Firefox(firefox_profile=self.profile, firefox_options=self.options, executable_path=r'C:Users\timpa\Documents\geckodriver.exe')

        self.driver.get(self.amazon_url)
    
    def search_items(self):

        urls = []
        prices = []
        names = []

        for item in self.items:
            print(f"Searching for {item}.")

            self.driver.get(self.amazon_url)

            search_input = self.driver.find_element_by_id("twotabsearchtextbox")
            search_input.send_keys(item)

            time.sleep(5)

            search_button = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input')
            search_button.click()

            time.sleep(5)

items = ["toothpaste"]
amazon_bot = AmazonBot(items)
amazon_bot.search_items()


