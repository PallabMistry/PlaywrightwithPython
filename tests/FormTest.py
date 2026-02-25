from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    page.get_by_label('name').fill('Pallab')
    page.get_by_label('email').fill('Pallab@gmail.com')
    page.get_by_label('gender').click()
    page.get_by_label('mobile').fill('980756432')
    

    browser.close()


