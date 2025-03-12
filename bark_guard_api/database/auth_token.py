import secrets
from datetime import datetime, timezone
import jwt
import secrets

SECRET_TOKEN = secrets.token_hex(16)  # TODO store value in the .env file
ALGORITHM = "HS256"


def create_jwt(user_id: int) -> str:
    payload = {"sub": user_id, "iat": datetime.now(timezone.utc)}
    token = jwt.encode(payload, SECRET_TOKEN, ALGORITHM)
    return token


def is_token_valid(token: str) -> bool:
    pass
