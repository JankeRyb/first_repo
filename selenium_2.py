from selenium import webdriver
import time
#from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("http://www.saucedemo.com/")
print("Nazwa strony:",driver.title)

time.sleep(3)


# button_1_accept= driver.find_element('id',"L2AGLb")
# button_1_accept.click()
# print(button_1_accept)
# pole_Szukaj=driver.find_element('name','q')
# pole_Szukaj.send_keys('Czy jutro jest niedziela handlowa')
# szukaj=driver.find_element('name','btnK')
# szukaj.submit()
# time.sleep(60)
# driver.quit()