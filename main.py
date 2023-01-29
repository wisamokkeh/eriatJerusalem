import time

import pytest
from selenium import webdriver
from allure_commons.types import AttachmentType
import allure
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from check_err import  check_err


class ConfirmationForStructurePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://jeronlineforms.jerusalem.muni.il/ConfirmationForStructure"
        self.first_name_label = 'שם פרטי'
        self.last_name_label = 'שם משפחה'
        self.id_label = 'מספר ת.ז.'
        self.phone_label = 'cellphone'
        self.email_label = 'דוא"ל'
        self.first_name_locator = {
                                    'By': By.XPATH,
                                    'Value': f"//label[contains(text(),'{self.first_name_label}')]/following-sibling::input"
                                    }
        self.last_name_locator = {
                                    'By': By.XPATH,
                                    'Value': f"//label[contains(text(),'{self.last_name_label}')]/following-sibling::input"
                                    }
        self.id_locator = {
                                    'By': By.XPATH,
                                    'Value': f"//label[contains(text(),'{self.id_label}')]/following-sibling::input"
                                    }
        self.phone_locator = {
                                    'By': By.XPATH,
                                    'Value': f"//input[@id='{self.phone_label}']"
                                    }
        self.email_locator = {
                                    'By': By.XPATH,
                                    'Value': f"//label[contains(text(),'{self.email_label}')]/following-sibling::input"
                                    }

        self.three_dig_phone_locator= {
                                        'By' : By.XPATH,
                                        'Value': f"//input[@id='{self.phone_label}']/following-sibling::p-dropdown"
                                    }


    def visit(self):
        self.driver.get(self.url)
        self.first_name_field = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.first_name_locator['By'], self.first_name_locator['Value'])))
        self.last_name_field = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.last_name_locator['By'], self.last_name_locator['Value'])))
        self.id_field = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.id_locator['By'], self.id_locator['Value'])))
        self.phone_field = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.phone_locator['By'], self.phone_locator['Value'])))
        self.email_field = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.email_locator['By'], self.email_locator['Value'])))
        self.three_dig_field = self.driver.find_element(self.three_dig_phone_locator['By'] , self.three_dig_phone_locator['Value'])



    def fill_form(self, first_name, last_name, id, phone, email ):
        self.first_name_field.send_keys(first_name)
        self.last_name_field.send_keys(last_name)
        self.id_field.send_keys(id)
        self.phone_field.send_keys(phone)
        self.email_field.send_keys(email)
        #self.three_dig.send_keys(threeDig)

    def get_first_name_value(self):
        return self.first_name_field.get_attribute('value')

    def get_last_name_value(self):
        return self.last_name_field.get_attribute('value')

    def get_id_label(self):
        return self.id_field.get_attribute('value')

    def get_phone_label(self):
        return self.phone_field.get_attribute('value')

    def get_email_label(self):
        return self.email_field.get_attribute('value')



    def get_three_dig_label(self):
        # drop_btn = self.phone_field.find_element(by=By.XPATH, value='//div[@aria-haspopup="listbox"]')
        # drop_btn_open = drop_btn.get_attribute('aria-expanded')
        # if drop_btn_open in ('false' , None):
        #     drop_btn.click()
        self.three_dig_field = self.driver.find_element(self.three_dig_phone_locator['By'] , self.three_dig_phone_locator['Value'])
        # phone = self.phone_field.find_element(by=By.XPATH, value=f'.//li[@aria-label="{three_dig}"]')
        # phone.click()
        self.three_dig_field.click()
        time.sleep(5)

    def click_three_digits(self,three_digits):
        self.driver.find_element(By.XPATH,f"//li[@aria-label='{three_digits}']").click()



@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()



# def test_form_submission(driver):
#     confirmation_page = ConfirmationForStructurePage(driver)
#     confirmation_page.visit()
#     confirmation_page.fill_form("ווסאם", "עוקה", "315222111", "524075877", "w@w.com")
#     confirmation_page.get_three_dig_label()
#     confirmation_page.click_three_digits("054")
#
#     # check that the form was submitted successfully
#     assert "ווסאם" in confirmation_page.get_first_name_value()
#
#     # add a screenshot to the Allure report
#     allure.attach("screenshot", driver.get_screenshot_as_png(), AttachmentType.PNG)

def test_form_submission2(driver):
    confirmation_page = ConfirmationForStructurePage(driver)
    confirmation_page.visit()
    test = check_err(driver)
    confirmation_page.fill_form("יי", "עוקה", "315456848", "524075877", "w@w.com")
    confirmation_page.get_three_dig_label()
    confirmation_page.click_three_digits("054")
    # check that the form was submitted successfully
    assert test.check()
    # add a screenshot to the Allure report
    allure.attach("screenshot", driver.get_screenshot_as_png(), AttachmentType.PNG)

def test_form_submission3(driver):
    confirmation_page = ConfirmationForStructurePage(driver)
    confirmation_page.visit()
    test = check_err(driver)
    confirmation_page.fill_form("יי", "עוקה", "315456", "524075877", "w@w.com")
    confirmation_page.get_three_dig_label()
    confirmation_page.click_three_digits("054")
    # check that the form was submitted successfully
    assert test.check()
    # add a screenshot to the Allure report
    allure.attach("screenshot", driver.get_screenshot_as_png(), AttachmentType.PNG)


def test_form_submission2(driver):
    confirmation_page = ConfirmationForStructurePage(driver)
    confirmation_page.visit()
    test = check_err(driver)
    confirmation_page.fill_form("ss", "עוקה", "315456848", "524075877", "w@w.com")
    confirmation_page.get_three_dig_label()
    confirmation_page.click_three_digits("054")
    # check that the form was submitted successfully
    assert test.check()
    # add a screenshot to the Allure report
    allure.attach("screenshot", driver.get_screenshot_as_png(), AttachmentType.PNG)

def test_form_submission4(driver):
    confirmation_page = ConfirmationForStructurePage(driver)
    confirmation_page.visit()
    test = check_err(driver)
    confirmation_page.fill_form("גג", "עוקה", "315456848", "524075877", "w@w.com")
    confirmation_page.get_three_dig_label()
    confirmation_page.click_three_digits("054")
    # check that the form was submitted successfully
    assert test.check()
    # add a screenshot to the Allure report
    allure.attach("screenshot", driver.get_screenshot_as_png(), AttachmentType.PNG)