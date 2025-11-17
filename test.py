from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # headless=False shows the browser
    page = browser.new_page()

    # Open Playwright website
    page.goto("https://playwright.dev/")
    print("Page Title:", page.title())

    # Click on "Get Started"
    page.click("text=Get started")

    # Print the new URL
    print("New URL:", page.url)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
