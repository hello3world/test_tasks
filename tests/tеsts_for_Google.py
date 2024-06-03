import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def read_credentials(file_path):
    credentials = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            credentials[key] = value
    return credentials

# Вход в Google Почту
def login(email, password):
    # вход в google почтку
    driver = webdriver.Chrome()  # или другой драйвер, который вы используете
    driver.get("https://mail.google.com/")

    # Ввод email
    input_enter_email = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@type="email"]'))
    )
    input_enter_email.send_keys(email)
    input_enter_email.send_keys(Keys.RETURN)

    # Ожидание загрузки следующей страницы и ввода пароля
    input_enter_password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//input[@type="password"]'))
    )
    input_enter_password.send_keys(password)
    input_enter_password.send_keys(Keys.RETURN)

# Изменение пароля
def change_password(new_password):
    wait = WebDriverWait(driver, 10)

    driver.get("https://myaccount.google.com/security")

    password_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[@aria-label="Пароль"]')))
    password_link.click()

    new_password_field = wait.until(
        EC.presence_of_element_located((By.NAME, "password")))
    new_password_field.send_keys(new_password)
    confirm_password_field = driver.find_element(By.NAME,
                                                 "confirmation_password")
    confirm_password_field.send_keys(new_password)
    button_change = driver.find_element(By.XPATH, '//button[@type="submit"]')
    time.sleep(60)
    button_change.click()

# Изменение имени и фамилии
def change_name(first_name, last_name):
    driver.get("https://myaccount.google.com/personal-info")
    wait = WebDriverWait(driver, 10)
    name_link = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//a[@data-nav-type="5"]')))
    name_link.click()
    button_edit = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-index="0"]')))
    button_edit.click()
    first_name_field = wait.until(
        EC.presence_of_element_located((By.ID, "i6")))
    first_name_field.clear()
    first_name_field.send_keys(first_name)

    last_name_field = wait.until(
        EC.presence_of_element_located((By.ID, "i11")))
    last_name_field.clear()
    last_name_field.send_keys(last_name)

    buttons = driver.find_elements(By.XPATH, '//button')
    button_save = buttons[6]
    button_save.click()

# Сохранение данных в таблицу
def save_data_to_table(email, password, first_name, last_name, birthdate,
                       recovery_email):
    data = {
        "Email": [email],
        "Password": [password],
        "First Name": [first_name],
        "Last Name": [last_name],
        "Birthdate": [birthdate],
        "Recovery Email": [recovery_email]
    }

    df = pd.DataFrame(data)
    df.to_csv("user_data.csv", index=False)

def main():
    try:
        credentials = read_credentials('credentials_for_Google.txt')
        email = credentials["mail_name"]
        password = credentials["mail_name"]
        new_password = credentials["new_password"]
        first_name = credentials["first_name"]
        last_name = credentials["last_name"]
        birthdate = credentials["birthdate"]
        recovery_email = credentials["recovery_email"]
        print(
            "1 - Вход в Google почту:\n 2 - Изменение пароля\n 3 - Изменение имени и фамилии\n 4 - Сохранение данных в таблицу")
        number_test = input("Введите номер теста:")
        if number_test == '1':
            # запускаем тест проверки входа
            login(email, password)
            print("test login is passed successfully")
        elif number_test == '2':
            # запускаем тест на изменение пароля
            login(email, password)
            change_password(new_password)
            print("test change password is passed successfully")
        elif number_test == '3':
            # запускаем тест на имени и фамилии
            login(email, password)
            change_name(first_name, last_name)
            print("test change_name is passed successfully")
        elif number_test == '4':
            # запускаем тест на сохранение данных в таблице
            login(email, password)
            save_data_to_table(email, password, first_name, last_name,
                               birthdate, recovery_email)
            print("test save data is passed successfully")
        time.sleep(3)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()