from pathlib import Path

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
# When running in Docker we expect /app/frontend to exist.
# When running tests locally, that path may not exist, so we guard the mount.
frontend_dir = Path("/app/frontend")
if frontend_dir.exists():
    # Keep line lengths under common style limits (flake8).
    app.mount(
        "/",
        StaticFiles(directory=str(frontend_dir), html=True),
        name="frontend",
    )

