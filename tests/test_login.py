from pages.login_page import LoginPage

def test_login_success(page):
    page.goto("https://www.demoblaze.com/")
    login = LoginPage(page)

    # Open login modal
    login.open_login_modal()
    page.wait_for_selector("input#loginusername")  # wait until modal appears

    # Login with your credentials
    login.login("aizaz", "admin123")

    # Wait until the welcome text shows up
    page.wait_for_selector("#nameofuser", timeout=5000)
    welcome_text = page.locator("#nameofuser").inner_text()

    print("Welcome text:", welcome_text)  # debug
    assert "Welcome" in welcome_text
