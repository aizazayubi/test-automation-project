from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage

def test_full_flow(page):
    page.goto("https://www.demoblaze.com/")

    # LOGIN
    login = LoginPage(page)
    login.open_login_modal()
    page.wait_for_selector("input#loginusername")
    login.login("aizaz", "admin123")
    page.wait_for_selector("#nameofuser")  # wait for welcome text
    assert "Welcome" in page.locator("#nameofuser").inner_text()

    # SELECT PRODUCT AND ADD TO CART
    home = HomePage(page)
    home.select_product("Samsung galaxy s6")  # change product name as needed

    cart = CartPage(page)
    cart.add_to_cart()

    # OPTIONAL: go to cart page to verify
    page.goto("https://www.demoblaze.com/cart.html")
    page.wait_for_selector("tr.success")  # ensures product row is visible

    # LOG OUT
    home.logout()
    page.wait_for_selector("a#login2")  # login button appears again
