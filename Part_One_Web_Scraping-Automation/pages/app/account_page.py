from datetime import datetime

from playwright.sync_api import Page, expect

from helpers.logger import Logger
from helpers.validators import Validators
from helpers.screenshot import Screenshot

class AccountPage:
    """Page object for account management including banking details and payment methods."""

    def __init__(self, page: Page):
        # Save the Playwright Page object
        self.page = page

        # Account Page banking details
        self.banking_details = {
            "routing": page.locator("#bank-routing"),
            "account": page.locator("#bank-account"),
            "save": page.locator("#bank-save"),
        }

        # Account Page payment method details
        self.payment_method = {
            "holder": page.locator("#card-holder"),
            "number": page.locator("#card-number"),
            "exp_month": page.locator("#card-exp-month"),
            "exp_year": page.locator("#card-exp-year"),
            "cvc": page.locator("#card-cvc"),
            "save": page.locator("#card-save"),
        }

        self.saved_bank_info = page.get_by_test_id("bank-saved-info").locator("p").first
        self.saved_payment_info = page.get_by_test_id("payment-saved-info").locator("p").first

    def verify_account_page(self):
        """
        Verify that the account page is displayed with correct URL.
        """
        Logger.info("Verifying that the account page is displayed...")
        expect(self.page).to_have_url(
            "https://marketplace.dev-challenge.com/app/account"
        )
    
    def add_banking_details(self, routing: str, account: str):
        """
        Add banking details to the account with routing and account number validation.
        
        Args:
            routing: Bank routing number (must be 9 digits)
            account: Bank account number (4-17 digits)
        """
        Logger.section("Banking Details")

        Logger.info("Validating routing number...")

        if not routing.isdigit() or len(routing) != 9:
            raise ValueError("Routing number must be exactly 9 digits.")

        Logger.success("Routing number is valid.")

        Logger.info("Validating account number...")

        if not account.isdigit() or not 4 <= len(account) <= 17:
            raise ValueError("Account number must be between 4 and 17 digits.")

        Logger.success("Account number is valid.")

        Logger.info("Entering routing number...")
        self.banking_details["routing"].fill(routing)

        Logger.info("Entering account number...")
        self.banking_details["account"].fill(account)
        
        Screenshot.capture(
                self.page,
                "banking_details_before_save"
            )
        
        Logger.info("Saving banking details...")

        # Use the locator from the banking_details mapping
        self.banking_details["save"].click()

        Logger.success("Banking details submitted.\n")
        
        expect(self.saved_bank_info).to_contain_text(routing[-4:])
        expect(self.saved_bank_info).to_contain_text(account[-4:])
        
        self.verify_saved_banking_details(
            routing,
            account
        )
        
        Screenshot.capture(
            self.page,
            "banking_details_saved"
        )
      
    def add_payment_method(self, holder: str, card_number: str, exp_month: str, exp_year: str, cvc: str):
        """
        Add a payment method to the account with card details validation.
        
        Args:
            holder: Card holder name
            card_number: Credit card number
            exp_month: Expiration month
            exp_year: Expiration year
            cvc: Card verification code
        """
        Logger.section("Payment Method")

        Logger.info("Validating card holder...")

        if not holder.strip():
            raise ValueError("Card holder name is required.")

        Logger.success("Card holder valid.")

        card_number = card_number.replace(" ", "")

        Logger.info("Validating card number...")

        if not Validators.luhn_check(card_number):
            raise ValueError("Card number failed Luhn validation.")

        Logger.success("Card number valid.")

        Logger.info("Validating expiration...")

        month = int(exp_month)
        year = int(exp_year)

        current = datetime.now()

        if month < 1 or month > 12:
            raise ValueError("Invalid expiration month.")

        if year < current.year:
            raise ValueError("Card has expired.")

        if year == current.year and month < current.month:
            raise ValueError("Card has expired.")

        Logger.success("Expiration date valid.")

        Logger.info("Validating CVC...")

        if not cvc.isdigit() or len(cvc) not in (3, 4):
            raise ValueError("CVC must be 3 or 4 digits.")

        Logger.success("CVC valid.")

        Logger.info("Entering card holder...")
        self.payment_method["holder"].fill(holder)

        Logger.info("Entering card number...")
        self.payment_method["number"].fill(card_number)

        Logger.info("Entering expiration month...")
        self.payment_method["exp_month"].fill(exp_month)

        Logger.info("Entering expiration year...")
        self.payment_method["exp_year"].fill(exp_year)

        Logger.info("Entering CVC...")
        self.payment_method["cvc"].fill(cvc)

        Logger.info("Saving payment method...")
        
        Screenshot.capture(
            self.page,
            "payment_method_before_save"
        )
        self.payment_method["save"].click()
        
        expect(self.saved_payment_info).to_contain_text(card_number[-4:])
        expect(self.saved_payment_info).to_contain_text(f"{int(exp_month)}/{exp_year}")
       
        self.verify_saved_payment_method(
            card_number,
            exp_month,
            exp_year
        )
        Screenshot.capture(
            self.page,
            "payment_method_saved"
        )
        Logger.success("Payment method submitted.\n")

    def verify_saved_banking_details(self, routing: str, account: str):
        """
        Verify that the saved banking details match the provided routing and account numbers.
        
        """
        Logger.info("Verifying saved banking details...")

        expect(self.saved_bank_info).to_be_visible()

        text = self.saved_bank_info.text_content().strip()

        Logger.info(f"Saved text: {text}")

        expected_routing = routing[-4:]
        expected_account = account[-4:]

        if f"Routing: •••••{expected_routing}" not in text:
            raise ValueError(
                f"Routing mismatch.\nExpected ending: {expected_routing}\nActual: {text}"
            )

        saved_account = text.split("Account:")[1].strip()

        if not saved_account.endswith(expected_account):
            raise ValueError(
                f"Account mismatch.\nExpected ending: {expected_account}\nActual: {saved_account}"
            )

        Logger.success("Banking details verified successfully.")

    def verify_saved_payment_method(self,card_number: str,exp_month: str,exp_year: str):
        """
        Verify that the saved payment method details match the provided card number
        and expiration date.
        """

        Logger.info("Verifying saved payment method details...")

        expect(self.saved_payment_info).to_be_visible()

        text = self.saved_payment_info.text_content().strip()

        Logger.info(f"Saved text: {text}")

        expected_card = card_number[-4:]

        if expected_card not in text:
            raise ValueError(
                f"Card number mismatch.\nExpected ending: {expected_card}\nActual: {text}"
            )

        saved_exp = text.split("Expires")[1].strip()

        expected_exp = f"{int(exp_month)}/{exp_year}"


        if saved_exp != expected_exp:
            raise ValueError(
                f"Expiration mismatch.\nExpected: {expected_exp}\nActual: {saved_exp}"
            )

        Logger.success("Payment method verified successfully.")