from playwright.sync_api import Page, expect
from helpers.logger import Logger


class LoginPage:
    """Page object for the login and MFA screens."""

    def __init__(self, page: Page):
        # Save the Playwright Page object
        self.page = page

        # Login
        self.signin_btn = page.get_by_role("button", name="Sign in").nth(0)
        self.username_txt = page.locator("#email")
        self.password_txt = page.locator("#password")
        self.error_toast = page.get_by_text("Invalid login credentials")
        self.mfa_message = page.get_by_text(
            "Enter the 4-digit code provided with your credentials"
        )

        # MFA
        self.mfa_input = page.locator("[data-input-otp='true']")
        self.verify_btn = self.page.get_by_role("button", name="Verify")

    def login(self, username, password):
        """Log in using the provided username and password."""
        Logger.info(f"Logging in with username: {username}")
        self.username_txt.fill(username)
        self.password_txt.fill(password)
        self.signin_btn.click()

    def has_invalid_login(self):
        """Return True if an invalid login error message is visible."""
        Logger.info("Checking for invalid login credentials...")
        Logger.info(
            f"Invalid login credentials message is visible: {self.error_toast.is_visible()}"
        )
        return self.page.get_by_text("Invalid login credentials").is_visible()

    def verify_login_page(self):
        """Verify that the login page is displayed by checking the URL."""
        Logger.section("Login Details")
        Logger.info("Verifying that the login page is displayed...")
        expect(self.page).to_have_url("https://marketplace.dev-challenge.com/login")

    def verify_mfa_page(self):
        """Verify that the MFA page is displayed with the expected message."""
        expect(self.mfa_message).to_be_visible()
        if self.mfa_message.is_visible():
            Logger.success("MFA page is displayed with the correct message.")
            return True
        else:
            Logger.error("MFA page is not displayed or the message is incorrect.")
            return False

    def submit_mfa(self, code):
        """Submit the MFA code on the MFA verification page."""
        if not code.isdigit() or len(code) != 4:
            raise ValueError("MFA code must be exactly 4 digits.")
        Logger.info("MFA page verification successful. Submitting MFA code...")
        self.mfa_input.fill(code)
        self.verify_btn.click()
