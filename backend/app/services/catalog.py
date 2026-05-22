from app.models import Product


def get_products() -> list[Product]:
    # Static in-memory catalog
    return [
        Product(
            id=1,
            name="Wireless Headphones",
            description="Bluetooth headphones with deep bass and 30h battery.",
            price=59.99,
        ),
        Product(
            id=2,
            name="Smart Watch",
            description="Health tracking, notifications, and 7-day battery.",
            price=79.0,
        ),
        Product(
            id=3,
            name="Mechanical Keyboard",
            description="Hot-swappable switches, RGB backlight, and USB-C.",
            price=89.5,
        ),
        Product(
            id=4,
            name="USB-C Hub",
            description="7-in-1 hub with HDMI, SD, and fast data transfer.",
            price=24.99,
        ),
    ]

