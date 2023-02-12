from selenium import webdriver
import time
import datetime
#from selenium.webdriver.common.by import By

def make_screenshot(driver):
    teraz=datetime.datetime.now()
    screenshot='screenshot'+teraz.strftime('_%H%M%S')+'.png' #tu nie moze byc dwukropkow
    driver.get_screenshot_as_file(screenshot)


driver=webdriver.Chrome()
driver.get("http://www.saucedemo.com/")
print("Nazwa strony:",driver.title)

try:
    username_box=driver.find_element('id','user-name')
    username_box.clear()
    username_box.send_keys('standard_user')
except:
    make_screenshot(driver)


password_box=driver.find_element('xpath','//*[@id="password"]')
password_box.clear()
login_box=driver.find_element('id','login-button')

password_box.click()
password_box.send_keys('secret_sauce')

login_box.click()

make_screenshot(driver)

time.sleep(10)