from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Change_password:
    def __init__(self, driver):
        self.driver = driver

    def change_password(self, current_password, new_password):
        self.driver.get('https://x.com/settings/password')
        time.sleep(10)

        current_password_input = self.driver.find_element(By.XPATH, '//input[@name = "current_password"]')
        current_password_input.send_keys(current_password)

        new_password_input = self.driver.find_element(By.XPATH, '//input[@name = "new_password"]')
        new_password_input.send_keys(new_password)

        confirm_password_input = self.driver.find_element(By.XPATH, '//input[@name = "password_confirmation"]')
        confirm_password_input.send_keys(new_password)

        save_button = self.driver.find_element(By.XPATH,
                                      '//button[@data-testid="settingsDetailSave"]')
        save_button.click()
        print("Test -change_password- is completed succesfully")
        time.sleep(2)

