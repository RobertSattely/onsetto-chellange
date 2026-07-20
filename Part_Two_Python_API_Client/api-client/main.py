from client.api_client import ApiClient
from helpers.generators import Generators
from helpers.logger import Logger
from helpers.validators import Validators
import config


def main():
    try:
        client = ApiClient(config.BASE_URL)

        Logger.info("Authenticating...")
        mfa_token = client.login(config.EMAIL, config.PASSWORD)

        Logger.info("Verifying MFA...")
        client.verify_mfa(mfa_token)

        Logger.info("Updating banking information...")
        banking = client.update_banking(
            Generators.routing_number(),
            Generators.account_number()
        )

        Logger.success(
            f"Banking updated: "
            f"{banking['routing_masked']} | "
            f"{banking['account_masked']}"
        )

        Logger.info("Updating payment method...")

        card_number = Generators.card_number()

        if not Validators.luhn_check(card_number):
            Logger.error("Generated an invalid credit card number.")
            return

        exp_month, exp_year = Generators.future_expiration()

        payment = client.update_payment(
            "Test User",
            card_number,
            exp_month,
            exp_year,
            Generators.cvc()
        )

        Logger.success(
            f"Payment updated: "
            f"{payment['card_brand']} ending in "
            f"{payment['last4']}"
        )

    except Exception as ex:
        Logger.error(str(ex))


if __name__ == "__main__":
    main()