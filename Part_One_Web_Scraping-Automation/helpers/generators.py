"""Generator helper utilities."""

import random
import string
from datetime import datetime


class Generators:
    """Helper methods for generating random test data."""

    @staticmethod
    def generate_mfa_code() -> str:
        """Generate a random 4-digit MFA code."""
        return f"{random.randint(0, 9999):04d}"

    @staticmethod
    def routing_number() -> str:
        """Generate a random 9-digit routing number."""
        return "".join(random.choices(string.digits, k=9))

    @staticmethod
    def account_number(length: int = 12) -> str:
        """Generate a random account number (4-17 digits)."""

        if length < 4 or length > 17:
            raise ValueError("Account number must be 4-17 digits.")

        return "".join(random.choices(string.digits, k=length))

    @staticmethod
    def card_holder() -> str:
        """Generate a sample card holder name."""

        first = random.choice([
            "John", "Jane", "Robert", "Emily",
            "Chris", "Sarah", "Michael", "Lisa"
        ])

        last = random.choice([
            "Smith", "Johnson", "Brown",
            "Miller", "Wilson", "Davis"
        ])

        return f"{first} {last}"

    @staticmethod
    def future_expiration():
        """Generate a valid future expiration."""

        year = datetime.now().year + random.randint(1, 5)
        month = random.randint(1, 12)

        return f"{month:02}", str(year)

    @staticmethod
    def cvc(length: int = 3) -> str:
        """Generate a CVC."""

        return "".join(random.choices(string.digits, k=length))
    
    @staticmethod
    def card_number() -> str:
        """Generate a sample credit card number."""
        return random.choice([
            "4111111111111111",   # Visa
            "5555555555554444",   # Mastercard
            "378282246310005",    # American Express
            "6011111111111117"    # Discover
        ])