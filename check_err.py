from selenium.webdriver.common.by import By
class check_err:
    def __init__(self,driver):
        self.driver = driver


    def check(self):


        try:
            self.allert_locator = {
                'By': By.XPATH,
                'Value': '//div[@class="field-errors ng-star-inserted"]'
            }
            self.allert_field = self.driver.find_element(self.allert_locator['By'], self.allert_locator['Value'])
            return False, print("value is invalid")
        except:
            return True, print("value is valid")