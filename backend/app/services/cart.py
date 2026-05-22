from dataclasses import dataclass
from typing import Dict

from app.models import CartItem
from app.services.catalog import get_products


PRODUCTS_BY_ID = {p.id: p for p in get_products()}


@dataclass
class CartState:
    # product_id -> quantity
    items: Dict[int, int]


_CARTS: Dict[str, CartState] = {}


def get_cart_for_user(user_id: str) -> CartState:
    if user_id not in _CARTS:
        _CARTS[user_id] = CartState(items={})
    return _CARTS[user_id]


def cart_add(user_id: str, product_id: int, quantity: int) -> None:
    if product_id not in PRODUCTS_BY_ID:
        raise ValueError("Unknown product")
    if quantity <= 0:
        # treat non-positive as removal
        cart_remove(user_id, product_id)
        return

    cart = get_cart_for_user(user_id)
    cart.items[product_id] = quantity


def cart_remove(user_id: str, product_id: int) -> None:
    cart = get_cart_for_user(user_id)
    cart.items.pop(product_id, None)


def cart_items(user_id: str) -> list[CartItem]:
    cart = get_cart_for_user(user_id)
    items: list[CartItem] = []
    for pid, qty in cart.items.items():
        p = PRODUCTS_BY_ID[pid]
        items.append(
            CartItem(
                product_id=pid,
                quantity=qty,
                name=p.name,
                price=p.price,
            )
        )
    return items


def cart_total(user_id: str) -> float:
    items = cart_items(user_id)
    return sum(i.price * i.quantity for i in items)

