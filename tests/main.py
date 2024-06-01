from selenium import webdriver
from change_password import Change_password
from login_page import Login_page

def main():
    driver = webdriver.Chrome()
    try:
        login = Login_page(driver)
        login.authentication(login_name, login_password)q\\
    
    # запускаем тест проверки функционала изменения пароля
    # тестовые данные
    user_current_password = 'RT*ei!P0/*'
    user_new_password = "RT*ei!P1/*"
    # запуск теста

    test_change_password = Change_password(driver)
    test_change_password.change_password(user_current_password, user_new_password)
    
    driver.quit()
main()