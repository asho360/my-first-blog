from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase

import time
MAX_WAIT = 10

class CVVistorTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title_of_blog(self):
        self.browser.get(self.live_server_url)
        self.assertIn("Ashleigh's blog", self.browser.title)

        self.fail('Finsih the test!')


