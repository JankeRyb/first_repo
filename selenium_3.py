from selenium import webdriver
import time
import datetime
from selenium.webdriver.support import expected_conditions as excon
from selenium.webdriver.support.wait import WebDriverWait
from selenium_funkcje import make_screenshot
from selenium.common.exceptions import TimeoutException

def czekaj_na_id(element_id):
    #element_id='login-button'
    timeout=10
    timeout_message=f'Element o id {element_id} nie pojawil sie w czasie {timeout} s.'

    lokalizator = ('id',element_id) #szukanie po id konkretnej wartosci
    znaleziono = excon.visibility_of_element_located(lokalizator)  #patyk do dźgania strony xD
    #obiekt bedzie pytany czy jest OK a odpowiedź bedzie zależeć od tego czy element jest widoczny
    oczekiwator=WebDriverWait(driver, timeout)
    return oczekiwator.until(znaleziono,timeout_message)

opcje=webdriver.ChromeOptions()
opcje.add_argument('headless')
driver=webdriver.Chrome(options=opcje)

driver.get("http://www.saucedemo.com/")
try:
    login_button=czekaj_na_id("login-button")
except TimeoutException:
    print('Nie znaleziono')
else:
    print('Znaleziono')
    print(login_button)
finally:
    make_screenshot(driver)
    time.sleep(2)
    driver.quit()


make_screenshot(driver)
time.sleep(2)
driver.quit()

