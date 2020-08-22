import time
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


    def test_content_of_cv(self):
        #The user finds Ashleigh's cool blog
        self.browser.get(self.live_server_url)

        #They notice the title and the CV link
        self.assertIn("Ashleigh's blog", self.browser.title)
        self.browser.get(self.live_server_url + '/cv/')
        time.sleep(5)
        self.browser.get(self.live_server_url + '/cv/edit_cv')
        time.sleep(5)


