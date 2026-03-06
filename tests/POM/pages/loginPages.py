class LoginPage:
    def __init__(self, page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("password")
        self._loginbtn = page.get_by_text('Login')

    def enter_username(self, u_name):
        self._username.clear()
        self._username.fill(u_name)

    def enter_password(self, p_word):
        self._password.clear()
        self._password.fill(p_word)   

    def click_login(self):
        self._loginbtn.click()

    def do_login(self, credential):
        self.enter_username(credential['username'])    
        self.enter_password(credential['password'])
        self.click_login()
        