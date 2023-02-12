class LoginPage:
    def __init__(self, driver,user='user-name',password='password',login_button='login-button'):
        self.driver=driver
        self.username_field=user
        self.password_field=password
        self.login_button=login_button

    def open(self,web="http://www.saucedemo.com/"):
        self.driver.get(web)

    def enter_username(self, username_tresc):
        field=self.driver.find_element('id',self.username_field)
        field.clear()
        field.send_keys(username_tresc)

    def enter_password(self,password_tresc):
        field = self.driver.find_element('id', self.password_field)
        field.clear()
        field.send_keys(password_tresc)

    def click_login_button(self):
        button=self.driver.find_element('id',self.login_button)
        button.click()



