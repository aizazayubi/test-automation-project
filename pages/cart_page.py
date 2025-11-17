from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def add_to_cart(self):
        self.page.locator("a:has-text('Add to cart')").click()
        self.page.on("dialog", lambda dialog: dialog.accept())
