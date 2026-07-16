from playwright.sync_api import Page, expect
from helpers.logger import Logger

class HomePage:
    """Page object model for the home page."""

    def __init__(self, page: Page):
        # Save the Playwright Page object
        self.page = page

        # Locators
        self.login_btn = page.get_by_role("button", name="Log in").nth(0)

    def open_home_page(self):
        """Navigate to the home page."""
        Logger.info("Opening the home page...")
        self.page.goto("https://marketplace.dev-challenge.com/")

    def click_login(self):
        """Click the login button on the home page."""
        Logger.info("Clicking the login button...")
        self.login_btn.click()
        