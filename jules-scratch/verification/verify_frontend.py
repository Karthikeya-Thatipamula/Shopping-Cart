from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto('http://127.0.0.1:5001/')
    page.fill('#username', 'testuser')
    page.fill('#password', 'testpassword')
    page.click('#register-btn')
    page.on('dialog', lambda dialog: dialog.accept())
    page.click('#login-btn')
    page.on('dialog', lambda dialog: dialog.accept())
    page.click('.product button')
    page.wait_for_selector('#cart-items li')
    page.screenshot(path='jules-scratch/verification/verification.png')
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
