from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class CartItemIn(BaseModel):
    product_id: int
    quantity: int


class CartItem(BaseModel):
    product_id: int
    quantity: int
    name: str
    price: float


class CartOut(BaseModel):
    items: List[CartItem]
    total: float

