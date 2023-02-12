from selenium import webdriver
from selenium_funkcje import make_screenshot
from selenium4_klasa import LoginPage
import time
import pytest

@pytest.mark.parametrize('uzytkownik',['standard_user','standard_user2'])

def test_login_page(uzytkownik):
    driver=webdriver.Chrome()
    page=LoginPage(driver)
    page.open()
    page.enter_username(uzytkownik)
    page.enter_password('secret_sauce')
    page.click_login_button()
    time.sleep(1)
    try:
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', make_screenshot(driver)
    finally:
        driver.quit()