from fastapi import APIRouter, HTTPException, status
from bark_guard_api.web_interface.models.models import UserRequest
from bark_guard_api.database.session import db_session
from bark_guard_api.database.tables.tables import User, Subscription
from bark_guard_api.web_interface.dependencies import create_jwt

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/register")
def register(user_request: UserRequest) -> dict:
    """
    This function is used to register user

    :param user_request: user request

    :return: jwt token
    """
    if db_session.query(User).filter(User.email == user_request.email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists.")
    user = User(user_request.email, user_request.password, Subscription("FREE"))  # TODO make some other plans
    db_session.add(user)
    db_session.commit()
    return {"access_token": create_jwt(user.user_id), "token_type": "bearer"}


@router.post("/login")
def login(user_request: UserRequest) -> dict:
    """
    This function is used to log in user and return jwt token.

    :param user_request: user request

    :return: jwt token
    """
    user = db_session.query(User).filter(User.email == user_request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found.")
    if not user.verify_password(user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password.")
    return {"access_token": create_jwt(user.user_id), "token_type": "bearer"}
