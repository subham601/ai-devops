from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.auth import router as auth_router
from app.api.cart import router as cart_router
from app.api.products import router as products_router


app = FastAPI(title="Ecommerce Demo")

# API
app.include_router(auth_router)
app.include_router(products_router)
app.include_router(cart_router)

# Frontend (served by backend)
app.mount("/", StaticFiles(directory="/app/frontend", html=True), name="frontend")

