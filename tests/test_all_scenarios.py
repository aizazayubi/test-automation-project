import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage

@pytest.mark.parametrize("username,password,expected", [
    ("aizaz", "admin123", True),   # positive login
    ("wronguser", "wrongpass", False)  # negative login
])
def test_login(page, username, password, expected):
    page.goto("https://www.demoblaze.com/")
    login = LoginPage(page)
    login.open_login_modal()
    page.wait_for_selector("input#loginusername")
    login.login(username, password)

    if expected:
        page.wait_for_selector("#nameofuser", timeout=5000)
        assert "Welcome" in page.locator("#nameofuser").inner_text()
    else:
        # Negative scenario: modal should stay visible
        assert page.locator("input#loginusername").is_visible()

def test_add_to_cart_valid(page):
    page.goto("https://www.demoblaze.com/")
    login = LoginPage(page)
    login.open_login_modal()
    page.wait_for_selector("input#loginusername")
    login.login("aizaz", "admin123")
    page.wait_for_selector("#nameofuser")

    home = HomePage(page)
    home.select_product("Samsung galaxy s6")

    cart = CartPage(page)
    cart.add_to_cart()

    page.goto("https://www.demoblaze.com/cart.html")
    page.wait_for_selector("tr.success")
    assert page.locator("tr.success").is_visible()

def test_add_to_cart_invalid(page):
    page.goto("https://www.demoblaze.com/")
    # Try selecting a product that does not exist
    home = HomePage(page)
    with pytest.raises(Exception):
        home.select_product("NonExistentProduct")

def test_login_add_product_logout(page):
    page.goto("https://www.demoblaze.com/")
    login = LoginPage(page)
    login.open_login_modal()
    page.wait_for_selector("input#loginusername")
    login.login("aizaz", "admin123")
    page.wait_for_selector("#nameofuser")

    home = HomePage(page)
    home.select_product("Samsung galaxy s6")

    cart = CartPage(page)
    cart.add_to_cart()

    home.logout()
    page.wait_for_selector("a#login2")
    assert page.locator("a#login2").is_visible()
