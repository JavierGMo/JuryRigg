import os
from dotenv import load_dotenv

class Config:
    def __init__(self) -> None:
        load_dotenv()
        self.__cflPage = os.getenv('CFL_PAGE')
        self.__emailTest = os.getenv('EMAIL_TEST')
        self.__passwordTest = os.getenv('PASSWORD_TEST')
    
    def getCFLPage(self):
        return self.__cflPage
    def getEmailTest(self):
        return self.__emailTest
    def getPasswordTest(self):
        return self.__passwordTest
