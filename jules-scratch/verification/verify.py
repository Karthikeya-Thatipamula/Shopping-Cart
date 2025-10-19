
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:5001")

    # Register
    page.fill("#username", "testuser")
    page.fill("#password", "password")
    page.click("#register-btn")
    page.wait_for_selector(".notification.show")
    page.screenshot(path="jules-scratch/verification/register.png")

    # Login
    page.fill("#username", "testuser")
    page.fill("#password", "password")
    page.click("#login-btn")
    page.wait_for_selector("#user-info")
    page.screenshot(path="jules-scratch/verification/login.png")

    # Add to cart
    page.click(".product button")
    page.wait_for_selector(".cart-item-controls")
    page.screenshot(path="jules-scratch/verification/add_to_cart.png")

    # Increase quantity
    page.click(".quantity-increase")
    page.wait_for_timeout(500) # Wait for the UI to update
    page.screenshot(path="jules-scratch/verification/increase_quantity.png")

    # Remove from cart
    page.click(".remove-item")
    page.wait_for_timeout(500) # Wait for the UI to update
    page.screenshot(path="jules-scratch/verification/remove_from_cart.png")

    # Logout
    page.click("#logout-btn")
    page.wait_for_selector("#login-form")
    page.screenshot(path="jules-scratch/verification/logout.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
