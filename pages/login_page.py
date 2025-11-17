from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_button_header = page.locator("a#login2")
        self.username_input = page.locator("input#loginusername")
        self.password_input = page.locator("input#loginpassword")
        self.login_submit = page.locator("button:has-text('Log in')")

    def open_login_modal(self):
        self.login_button_header.click()

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_submit.click()
