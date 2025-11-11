import secrets
import string


def generate_transaction_id(length: int = 12) -> str:
    """Generate a secure random alphanumeric transaction ID"""
    alphabet = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))
