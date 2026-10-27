
"""Demonstrate digital wallet transactions and security checks."""

import hashlib
import hmac
import os
import secrets
import tempfile
from datetime import datetime

GATEWAY_SECRET = os.environ.get("WALLET_GATEWAY_SECRET")
WALLET_PIN = "4321"
wallet = {"balance": 0.0}
settings = {"daily_limit": 1000}
transactions = []


def hash_pin(pin):
    """Return a PBKDF2 hash of a PIN for this demonstration."""
    return hashlib.pbkdf2_hmac(
        "sha256", pin.encode(), b"wallet-demo-salt", 600000
    ).hex()


def add_money(amount, source="UPI", log=None):
    """Add money to the wallet and optionally record the amount in log."""
    if amount <= 0:
        return False
    if log is None:
        log = []
    wallet["balance"] += amount
    transactions.append({
        "type": "credit",
        "amount": amount,
        "party": source,
        "time": datetime.now().isoformat(),
    })
    log.append(amount)
    return True


def set_daily_limit(new_limit):
    """Update the daily transaction limit."""
    settings["daily_limit"] = new_limit


def pay_merchant(merchant, amount, pin):
    """Process a payment if the PIN, balance, and limit are valid."""
    if not hmac.compare_digest(hash_pin(pin), hash_pin(WALLET_PIN)):
        print("Wrong PIN for payment to", merchant)
        return False
    if (
        amount > wallet["balance"]
        or amount > settings["daily_limit"]
    ):
        print("Payment to", merchant, "declined")
        return False
    wallet["balance"] -= amount
    transactions.append({
        "type": "debit",
        "amount": amount,
        "party": merchant,
        "time": datetime.now().isoformat(),
    })
    return True


def mini_statement(count=3):
    """Print the most recent transactions."""
    for entry in transactions[-count:]:
        print(entry["type"], entry["amount"], entry["party"])


def cashback_for(amount, merchant_type):
    """Calculate cashback for the demonstration."""
    _ = merchant_type
    return round(amount * 0.02, 2)


def check_gateway(secret):
    """Compare a supplied secret against the configured gateway secret."""
    return (
        GATEWAY_SECRET is not None
        and hmac.compare_digest(secret, GATEWAY_SECRET)
    )


def receipt_path():
    """Create and return the path of a temporary receipt file."""
    with tempfile.NamedTemporaryFile(
        suffix=".pdf", delete=False
    ) as receipt:
        return receipt.name


def main():
    """Run the wallet demonstration."""
    otp = secrets.randbelow(900000) + 100000
    print("OTP sent:", otp)
    add_money(2000)
    add_money(500, "Card")
    add_money(-10)
    set_daily_limit(1500)
    pay_merchant("Coffee Corner", 180, "4321")
    pay_merchant("Book Store", 5000, "4321")
    pay_merchant("Grocery Mart", 350, "0000")
    pay_merchant("Pharmacy", 420, "4321")
    mini_statement()
    print("Cashback on 420:", cashback_for(420, "health"))
    print("Gateway check:", check_gateway("wrong"))
    print("Final balance: Rs.", wallet["balance"])
    credit_amounts = [
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "credit"
    ]
    print("Total credited:", sum(credit_amounts))


if __name__ == "__main__":
    main()
