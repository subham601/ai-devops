from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: str
    email: str


# Demo user store (in-memory)
USERS: dict[str, User] = {
    "demo@example.com": User(id="u1", email="demo@example.com")
}

# Demo password (plain text for demo simplicity)
USER_PASSWORDS: dict[str, str] = {
    # Keep in sync with backend/tests/test_auth_and_cart.py
    "demo@example.com": "demo123"
}

