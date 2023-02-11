from selenium import webdriver
import time
import datetime
#from selenium.webdriver.common.by import By

teraz=datetime.datetime.now()
# print(teraz)
# print(type(teraz))
screenshot='screenshot'+teraz.strftime('%H:%M:%S')+'.png'
print(screenshot)

driver=webdriver.Chrome()
driver.get("http://www.saucedemo.com/")
print("Nazwa strony:",driver.title)

try:
    username_box=driver.find_element('id','user-namesdsd')
    username_box.click()
    username_box.send_keys('standard_user')
except:
    driver.get_screenshot_as_file(screenshot)


password_box=driver.find_element('id','password')
login_box=driver.find_element('id','login-button')



password_box.click()
password_box.send_keys('secret_sauce')

login_box.click()

driver.get_screenshot_as_file(screenshot)

time.sleep(60)


# button_1_accept= driver.find_element('id',"L2AGLb")
# button_1_accept.click()
# print(button_1_accept)
# pole_Szukaj=driver.find_element('name','q')
# pole_Szukaj.send_keys('Czy jutro jest niedziela handlowa')
# szukaj=driver.find_element('name','btnK')
# szukaj.submit()
# time.sleep(60)
# driver.quit()