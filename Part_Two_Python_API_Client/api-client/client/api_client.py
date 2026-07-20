import requests


class ApiClient:
    """Simple client for the Onsetto API."""

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def login(self, email: str, password: str) -> str:
        response = self.session.post(
            f"{self.base_url}/auth/token", json={"email": email, "password": password}
        )

        response.raise_for_status()

        return response.json()["mfa_token"]

    def verify_mfa(self, mfa_token: str) -> None:
        response = self.session.post(
            f"{self.base_url}/auth/mfa/verify",
            json={"mfa_token": mfa_token, "code": "1234"},
        )

        response.raise_for_status()

        token = response.json()["access_token"]

        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def update_banking(self, routing_number: str, account_number: str) -> dict:
        response = self.session.put(
            f"{self.base_url}/account/banking",
            json={"routing_number": routing_number, "account_number": account_number},
        )

        response.raise_for_status()

        return response.json()

    def update_payment(
        self,
        cardholder_name: str,
        card_number: str,
        exp_month: int,
        exp_year: int,
        cvc: str,
    ) -> dict:

        response = self.session.put(
            f"{self.base_url}/account/payment",
            json={
                "cardholder_name": cardholder_name,
                "card_number": card_number,
                "exp_month": exp_month,
                "exp_year": exp_year,
                "cvc": cvc,
            },
        )

        response.raise_for_status()

        return response.json()
