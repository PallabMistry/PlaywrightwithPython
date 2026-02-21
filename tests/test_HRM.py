import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("link", name="English").click()
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("orange hr")
    page.get_by_text("OrangeHRMFruitSee more").click()
    # page.locator("iframe[name=\"a-4232vcv4ov5a\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
    # page.locator("iframe[name=\"c-4232vcv4ov5a\"]").content_frame.locator(".rc-imageselect-tile").first.click()
    # page.locator("iframe[name=\"c-4232vcv4ov5a\"]").content_frame.locator("td:nth-child(2)").first.click()
    # page.locator("iframe[name=\"c-4232vcv4ov5a\"]").content_frame.locator("td:nth-child(3)").first.click()
    # page.locator("iframe[name=\"c-4232vcv4ov5a\"]").content_frame.locator("td:nth-child(2)").first.click()
    # page.locator("iframe[name=\"c-4232vcv4ov5a\"]").content_frame.get_by_role("button", name="Verify").click()
    # page.get_by_role("link", name="OrangeHRM: Human Resources").click()
    # page.get_by_role("navigation").get_by_role("link", name="OrangeHRM Logo").click()
    # page.locator("#navbarNav").get_by_role("button", name="Contact Sales").click()
    # page.get_by_role("textbox", name="Full Name").click()
    # page.get_by_role("textbox", name="Full Name").fill("pallab")
    # page.get_by_role("textbox", name="Phone Number").click()
    # page.get_by_role("textbox", name="Phone Number").fill("0193333333")
    # page.get_by_role("textbox", name="Email").click()
    # page.get_by_role("textbox", name="Email").fill("ex@mail.com")
    # page.get_by_label("Country").select_option("Bangladesh")
    # page.get_by_label("No Of Employees").select_option("11 - 50")
    # page.get_by_role("textbox", name="Job title").click()
    # page.get_by_role("textbox", name="Job title").fill("SQA")
    # page.get_by_role("textbox", name="Your Message").click()
    # page.get_by_role("textbox", name="Your Message").fill("i love too.")
    # page.locator("iframe[name=\"a-skwg156id1cf\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
 