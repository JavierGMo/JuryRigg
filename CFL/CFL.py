from BuildDriver.BuildDriver import BuidDriver
from selenium.webdriver.common.by import By
import re
import time
from Art.Art import Art

class CFL:
    def __init__(self, cflPage: str, emailTest: str, passwordTest: str) -> None:
        Art.printArt()
        self._buildDriver = BuidDriver()
        self._driver = self._buildDriver.getDriver()
        self.cflPage = cflPage
        self.emailTest = emailTest
        self.passwordTest = passwordTest
    def run(self):
        print("Opening page...")
        self._driver.get(self.cflPage)
        # self.assertTitle()
        self.openSession()
        self._buildDriver.close()
        print("Closed page...")
    def assertTitle(self):
        print("Asserting title to CFL...")
        assert "Operations - CFL" in self._driver.title
    def openSession(self):
        email = self._driver.find_element(By.ID, "email")
        password = self._driver.find_element(By.ID, "password")
        buttonLogin = self._driver.find_element(By.XPATH, '//button[@type="submit"]')
        email.send_keys(self.emailTest)
        password.send_keys(self.passwordTest)
        buttonLogin.click()
        self._buildDriver.webDriverWait()
        print("Waiting for CFL page...")
        time.sleep(3)
        otp = self.getMailAtYup()
        fieldsForOTP = self._driver.find_elements(By.XPATH, '//input[@type="tel"]')
        continueButton = self._driver.find_element(By.XPATH, '//button[@type="submit"]')
        print("Getting into CFL, wait, please ...")
        print("fields")
        if len(fieldsForOTP) == 0:
            raise Exception("There aren't inputs")
        if len(fieldsForOTP) != 6:
            raise Exception("You could get error :s")
        print(f"How much inputs: {len(fieldsForOTP)}")
        for index, field in enumerate(fieldsForOTP):
            field.send_keys(otp[index])
        print("Send your OTP, wait, please ...")
        continueButton.click()
        time.sleep(10)
    def __openYupMail(self):
        print("Going to yup mail...")
        self._driver.execute_script("window.open('https://yopmail.com/es/')")
        self._driver.switch_to.window(self._driver.window_handles[1])
        print(f"Tab for yup: {self._driver.window_handles[1]}")
        print("At to yup mail...")
    def __gettingSessingYupMail(self):
        print("Putting mail for test...")
        emailInput = self._driver.find_element(By.ID, "login")
        btnForCreatingSession = self._driver.find_element(By.XPATH, '//button[@title="Revisa el correo @yopmail.com"]') # //button[@title="Revisa el correo @yopmail.com"] | //input[@type="submit"]
        print("Button")
        emailInput.send_keys("test-robert-ops+1@yopmail.com") # any email :p
        btnForCreatingSession.click()
    def __finishedOTP(self, text: str) -> str:
        foundOTP = re.search(r'[0-9]{0,3}-[0-9]{0,3}', text)
        groupOTP = foundOTP.group()
        print(f"Your OTP: {groupOTP}")
        splittedOTP = groupOTP.split('-')
        joinedOTP = "".join(splittedOTP)
        return joinedOTP
    def __gettingOTP(self):
        print("Refreshing YUP mail...")
        refreshingButton = self._driver.find_element(By.ID, "refresh")
        refreshingButton.click()
        print("Waiting for refreshing at yup...")
        time.sleep(3)
        emailsContainer = self._driver.find_element(By.ID, 'wminboxmain')
        print("Getting mails...")
        emailsIframe = emailsContainer.find_element(By.ID, 'ifinbox')
        print("Frame")
        self._driver.switch_to.frame(emailsIframe)
        emailsHTML = self._driver.find_element(By.TAG_NAME, 'html')
        emailsBody = emailsHTML.find_element(By.TAG_NAME, 'body')
        emailsDiv = emailsBody.find_element(By.CLASS_NAME, 'mctn')
        emails = emailsDiv.find_elements(By.CLASS_NAME, 'm')
        print("Waiting for getting mail...")
        if len(emails) == 0:
            raise Exception("There aren't emails")
        currentEmail = emails[0]
        buttonShortTextOTPEmail = currentEmail.find_element(By.CLASS_NAME, 'lm')
        divShortTextOTPEmail = buttonShortTextOTPEmail.find_element(By.CLASS_NAME, 'lms')
        textMail = divShortTextOTPEmail.text
        self._driver.switch_to.default_content()
        print(f"I'm OTP's text: {textMail}")
        return self.__finishedOTP(textMail)
    def __closingYUP(self):
        self._driver.close()
        self._driver.switch_to.window(self._driver.window_handles[0])
        print("Closed yup page...")
    def getMailAtYup(self):
        otp = ''
        self.__openYupMail()
        self.__gettingSessingYupMail()
        otp = self.__gettingOTP()
        self.__closingYUP()
        return otp
    def stepsInDashboard(self):
        pass
