import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os


class Test_Base:
    url = "https://www.accuweather.com/"
    max_wait = 10
    @pytest.fixture(autouse= True)
    def setup(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            service = Service(), options = chrome_options  # initializing Chrome webdriver
        )

        self.wait = WebDriverWait(self.driver, self.max_wait)  # initialize webdriver wait

        self.driver.get(self.url)  # opens url

        yield

        self.driver.quit() # teardown

