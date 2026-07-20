from playwright.sync_api import Page
from helpers.logger import Logger


class AppPage:
    """Page object for the main application navigation and user actions."""

    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.instructions_link = page.get_by_role("link", name="Instructions")
        self.marketplace_link = page.get_by_role("link", name="Marketplace")
        self.orders_link = page.get_by_role("link", name="Orders")
        self.account_link = page.get_by_role("link", name="Account")
        self.api_docs_link = page.get_by_role("link", name="API Docs")

        self.logout_btn = self.page.get_by_role("button", name="logout")

    def go_to_marketplace(self):
        """Navigate to the marketplace page."""
        self.marketplace_link.click()

    def go_to_orders(self):
        """Navigate to the orders page."""
        self.orders_link.click()

    def go_to_account(self):
        """Navigate to the account page."""
        self.account_link.click()

    def go_to_api_docs(self):
        """Navigate to the API docs page."""
        self.api_docs_link.click()

    def go_to_instructions(self):
        """Navigate to the instructions page."""
        self.instructions_link.click()

    def verify_logged_in_user(self, username: str):
        """Verify that the expected user is logged in."""
        is_user_valid = self.page.get_by_text(username, exact=True).is_visible()

        is_login_visible = self.logout_btn.is_visible()

        if is_user_valid and is_login_visible:
            Logger.success("Correct user is logged in.")
            return True

        Logger.error("Correct user is not logged in.")
        return False

    def logout(self):
        """Log out of the application by clicking the logout button."""
        Logger.info("Logging out...")
        self.logout_btn.click()