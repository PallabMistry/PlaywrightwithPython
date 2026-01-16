from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open website
    page.goto("https://example.com")

    # Take screenshot
    page.screenshot(path="example_screenshot.png", full_page=True)

    # Close browser
    browser.close()
