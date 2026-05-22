from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.security import decode_token
from app.models import CartItemIn, CartOut
from app.services.cart import cart_add, cart_items, cart_remove, cart_total

router = APIRouter(prefix="/api/cart", tags=["cart"])
security = HTTPBearer(auto_error=False)


def require_user_id(
    creds: HTTPAuthorizationCredentials | None = Depends(security),
) -> str:
    if creds is None or not creds.credentials:
        raise HTTPException(status_code=401, detail="Missing token")

    try:
        data = decode_token(creds.credentials)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

    user_id = data.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token payload")
    return str(user_id)


@router.get("", response_model=CartOut)
def get_cart(user_id: str = Depends(require_user_id)):
    items = cart_items(user_id)
    return CartOut(items=items, total=cart_total(user_id))


@router.post("/items")
def add_item(
    item: CartItemIn, user_id: str = Depends(require_user_id)
):
    try:
        cart_add(user_id, item.product_id, item.quantity)
    except ValueError:
        raise HTTPException(status_code=400, detail="Unknown product")
    return {"ok": True}


@router.delete("/items/{product_id}")
def delete_item(product_id: int, user_id: str = Depends(require_user_id)):
    cart_remove(user_id, product_id)
    return {"ok": True}

