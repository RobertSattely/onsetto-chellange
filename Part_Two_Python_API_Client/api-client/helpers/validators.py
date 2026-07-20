"""Validation helper utilities."""


class Validators:
    """Collection of validation helpers."""

    @staticmethod
    def luhn_check(card_number: str) -> bool:
        """Validate a credit card number using the Luhn algorithm."""

        total = 0
        reverse_digits = card_number[::-1]

        for index, digit in enumerate(reverse_digits):
            n = int(digit)

            if index % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9

            total += n

        return total % 10 == 0
