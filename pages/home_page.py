from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def select_product(self, product_name: str):
        self.page.locator(f"a:has-text('{product_name}')").click()

    def logout(self):
        self.page.locator("a#logout2").click()
