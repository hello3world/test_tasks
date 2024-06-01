import string
import random

from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_page:
    def __init__(self, driver):
        self.driver = driver

    def authentication(self, number_test, mail_name, login_name, password):
        if number_test == '1':
            self.driver.get('https://x.com/settings/password')
        elif number_test == '3':
            self.driver.get('https://x.com/home')
            time.sleep(8)
            wait = WebDriverWait(self.driver, 10)
            button = wait.until(EC.presence_of_element_located(
                (By.XPATH, '//a[@data-testid="loginButton"]')))
            button.click()
        time.sleep(5)
        # поле логина
        mail_name_field = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="text"]')))
        mail_name_field.send_keys(Keys.CONTROL, 'a')
        time.sleep(5)
        mail_name_field.send_keys(Keys.DELETE)
        time.sleep(5)
        mail_name_field.send_keys(mail_name)
        # кнопка для входа
        button = self.driver.find_element(By.XPATH,
                                          '//span[contains(text(), "Далее")]')
        button.click()
        time.sleep(3)
        login_name_field = self.driver.find_element(By.XPATH,
                                                    '//input[@data-testid="ocfEnterTextTextInput"]')
        login_name_field.send_keys(login_name)
        time.sleep(3)
        button_login = self.driver.find_element(By.XPATH,
                                                '//button[@data-testid="ocfEnterTextNextButton"]')
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
        current_password_input = self.driver.find_element(By.XPATH,
                                                          '//input[@name = "current_password"]')
        current_password_input.send_keys(current_password)
        time.sleep(2)
        new_password_input = self.driver.find_element(By.XPATH,
                                                      '//input[@name = "new_password"]')
        new_password_input.send_keys(new_password)
        time.sleep(2)
        confirm_password_input = self.driver.find_element(By.XPATH,
                                                          '//input[@name = "password_confirmation"]')
        confirm_password_input.send_keys(new_password)
        time.sleep(2)
        save_button = self.driver.find_element(By.XPATH,
                                               '//button[@data-testid="settingsDetailSave"]')
        save_button.click()
        print("Test -change_password- is completed succesfully")
        time.sleep(2)


class XPost:
    def __init__(self, driver):
        self.driver = driver

    def random_tweet(self, tweet_text):
        tweet_box = self.driver.find_element(By.XPATH,
                                             '//div[@data-testid="tweetTextarea_0"]')
        tweet_box.send_keys(tweet_text)
        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH,
                                                '//button[@data-testid="tweetButtonInline"]')
        tweet_button.click()
        print("Tweet posted successfully")
        time.sleep(2)


def read_credentials(file_path):
    credentials = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            credentials[key] = value
    return credentials


def main():
    driver = webdriver.Chrome()
    credentials = read_credentials('credentials.txt')

    mail_name = credentials['mail_name']
    login_name = credentials['login_name']
    password = credentials['password']
    user_current_password = credentials['user_current_password']
    user_new_password = credentials['user_new_password']
    print("1 - проверка смены пароля: \n 3 - проверка добавления нового поста")
    number_test = input("Введите номер теста:")
    login = Login_page(driver)
    login.authentication(number_test, mail_name, login_name, password)
    if number_test == '1':
        # запускаем тест проверки функционала изменения пароля
        test_change_password = Change_password(driver)
        test_change_password.change_password(user_current_password,
                                             user_new_password)
    elif number_test == '3':
        def generate_random_text():
            return ''.join(
                random.choices(string.ascii_letters + string.digits, k=280))

        tweet_text = generate_random_text()
        twitter_bot = XPost(driver)
        twitter_bot.random_tweet(tweet_text)
        time.sleep(5)


if __name__ == "__main__":
    main()
