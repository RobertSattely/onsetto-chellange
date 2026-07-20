import sys
from playwright.sync_api import sync_playwright
from helpers.logger import Logger
from helpers.generators import Generators
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.app_page import AppPage
from pages.app.account_page import AccountPage
from dotenv import load_dotenv
import os

load_dotenv()

Logger.info("Initializing Playwright...")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])

    username = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    bank_routing = Generators.routing_number()
    account_number = Generators.account_number()

    holder = Generators.card_holder()
    card_number = Generators.card_number()
    exp_month, exp_year = Generators.future_expiration()
    cvc = Generators.cvc()

    page = browser.new_page(no_viewport=True)
    Logger.info("Navigating to the home page...")
    home = HomePage(page)
    login = LoginPage(page)
    app = AppPage(page)
    account = AccountPage(page)

    home.open_home_page()
    home.click_login()
    login.verify_login_page()
    login.login(username, password)
    login.has_invalid_login()

    if login.verify_mfa_page():
        code = Generators.generate_mfa_code()
        login.submit_mfa(code)
    else:
        Logger.error("MFA page verification failed.")

    if not app.verify_logged_in_user(username):
        Logger.error("Failed to verify logged-in user.")
        app.logout()
        browser.close()
        sys.exit("Login failed: expected user not found.")

    Logger.info("Navigating to the Account page...")
    app.go_to_account()

    account.verify_account_page()

    account.add_banking_details(bank_routing, account_number)

    account.add_payment_method(holder, card_number, exp_month, exp_year, cvc)

    browser.close()
