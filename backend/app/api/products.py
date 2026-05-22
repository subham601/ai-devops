from fastapi import APIRouter

from app.services.catalog import get_products

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("")
def list_products():
    return {"items": [p.model_dump() for p in get_products()]}

