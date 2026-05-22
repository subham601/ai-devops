from fastapi import APIRouter, HTTPException

from app.core.security import create_access_token
from app.models import LoginRequest, LoginResponse
from app.services.auth import USERS, USER_PASSWORDS

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest):
    email = payload.email
    password = payload.password

    if email not in USERS or USER_PASSWORDS.get(email) != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user = USERS[email]
    token = create_access_token(subject=user.id, extra={"email": user.email})
    return LoginResponse(access_token=token)

