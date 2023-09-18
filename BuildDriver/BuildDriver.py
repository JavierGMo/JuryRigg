from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class BuidDriver:
    def __init__(self) -> None:
        print("Init selenium...")
        self._driver = webdriver.Chrome()
        print("Opened selenium...")
    def getDriver(self):
        return self._driver
    def webDriverWait(self):
        print("Waiting for document ready...")
        WebDriverWait(driver=self._driver, timeout=10).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        print("Document ready...")
    def close(self):
        self._driver.close()
