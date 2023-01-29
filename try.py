import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


class drwesh():
    def __init__(self,browser,label,testValue):
        self.browser = browser
        self.label = label
        self.testValue = testValue
        self.fillForm()


    def getPath(self):
        try:
            a=self.browser.find_element(By.XPATH, f"//label[contains(text(),'{self.label}')]/following-sibling::input")

            return a
        except:

            self.last_name_field = WebDriverWait(self.browser, 30).until(
                EC.presence_of_element_located((By.ID, f"{self.label}")))

            return self.last_name_field

    def fillForm(self):
        self.getPath().send_keys(self.testValue)



browser = webdriver.Chrome()
browser.get("https://jeronlineforms.jerusalem.muni.il/ConfirmationForStructure")
drwesh(browser,'שם פרטי','דרוויש')
drwesh(browser, "cellphone" , "524075877")

time.sleep(4)

