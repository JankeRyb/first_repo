from selenium import webdriver
from selenium_funkcje import make_screenshot
from selenium4_klasa import LoginPage
import time


def test_login_page():
    driver=webdriver.Chrome()
    page=LoginPage(driver,'user-name','password','login-button')
    page.open()
    page.enter_username('standard_user')
    page.enter_password('secret_sauce')
    page.click_login_button()
    time.sleep(1)
    try:
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', make_screenshot(driver)
    finally:
        driver.quit()