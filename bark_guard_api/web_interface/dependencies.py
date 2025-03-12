import secrets
from datetime import datetime, timezone
from fastapi import HTTPException, status
import jwt
from jwt import PyJWTError
import secrets

SECRET_KEY = secrets.token_hex(16)  # TODO store value in the .env file
ALGORITHM = "HS256"
TOKEN_EXPIRATION_TIME = 3600


def create_jwt(user_id: int) -> str:
    """
    This function is used to create jwt token.

    :param user_id: the id of the user

    :return: JWT token
    """
    payload = {"sub": user_id, "iat": datetime.now(timezone.utc)}
    token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    return token


def verify_jwt(token: str) -> int:
    """
    This function is used to check if token is valid.

    :param token: token to check

    :return: user id
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: int = payload.get("sub")
        token_creation_time = payload.get("iat")
        if not username or not token_creation_time:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid.")
        if datetime.now(timezone.utc) > token_creation_time + TOKEN_EXPIRATION_TIME:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is expired.")
        return username
    except PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")

