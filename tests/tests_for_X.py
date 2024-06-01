from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Login_page:
    def __init__(self, driver):
        self.driver = driver

    def authentication(self, mail_name, login_name, password):
        self.driver.get('https://x.com/settings/password')
        time.sleep(5)
        # поле логина
        mail_name_field = self.driver.find_element(By.XPATH, '//input[@name="text"]')
        mail_name_field.send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        mail_name_field.send_keys(Keys.DELETE)
        time.sleep(2)
        mail_name_field.send_keys(mail_name)
        # кнопка для входа
        buttons = self.driver.find_elements(By.XPATH, '//button')
        buttons[3].click()
        time.sleep(3)
        login_name_field = self.driver.find_element(By.XPATH, '//input[@data-testid="ocfEnterTextTextInput"]')
        login_name_field.send_keys(login_name)
        time.sleep(3)
        button_login = self.driver.find_element(By.XPATH, '//button[@data-testid="ocfEnterTextNextButton"]')
        button_login.click()
        time.sleep(3)
        current_password_input = self.driver.find_element(By.XPATH,
                                                          '//input[@name = "password"]')
        current_password_input.send_keys(Keys.CONTROL, 'a')
        time.sleep(3)
        current_password_input.send_keys(Keys.DELETE)
        time.sleep(3)
        current_password_input.send_keys(password)
        time.sleep(3)
        button_password = self.driver.find_element(By.XPATH,
                                                 '//button[@data-testid = "LoginForm_Login_Button"]')
        button_password.click()
        time.sleep(10)
class Change_password:
    def __init__(self, driver):
        self.driver = driver

    def change_password(self, current_password, new_password):
        current_password_input = self.driver.find_element(By.XPATH, '//input[@name = "current_password"]')
        current_password_input.send_keys(current_password)
        time.sleep(2)
        new_password_input = self.driver.find_element(By.XPATH, '//input[@name = "new_password"]')
        new_password_input.send_keys(new_password)
        time.sleep(2)
        confirm_password_input = self.driver.find_element(By.XPATH, '//input[@name = "password_confirmation"]')
        confirm_password_input.send_keys(new_password)
        time.sleep(2)
        save_button = self.driver.find_element(By.XPATH,
                                      '//button[@data-testid="settingsDetailSave"]')
        save_button.click()
        print("Test -change_password- is completed succesfully")
        time.sleep(2)

def main():
    driver = webdriver.Chrome()
    mail_name = input("Enter e-mail: ")
    login_name = input("Enter login_name: ")
    password = input("Enter password: ")
    login = Login_page(driver)
    login.authentication(mail_name, login_name, password)
    # запускаем тест проверки функционала изменения пароля
    # тестовые данные
    user_current_password = input("Enter user_current_password: ")
    user_new_password = input("Enter user_new_password: ")
    # запуск теста
    test_change_password = Change_password(driver)
    test_change_password.change_password(user_current_password, user_new_password)
    driver.quit()

if __name__ == "__main__":
    main()