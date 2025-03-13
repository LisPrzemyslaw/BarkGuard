from __future__ import annotations
import hashlib

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from bark_guard_api.database import _Base


class Subscription(_Base):
    __tablename__ = "subscription"

    subscription_id = Column("subscription_id", Integer, primary_key=True, autoincrement=True)
    plan = Column("plan", String)
    user_id = Column("user_id", Integer, ForeignKey("user.user_id"), unique=True)
    user = relationship("User", back_populates="subscription")

    def __init__(self, plan: str):
        self.plan = plan


class User(_Base):
    __tablename__ = "user"

    user_id = Column("user_id", Integer, primary_key=True, autoincrement=True)
    email = Column("email", String)
    password = Column("password", String)
    subscription = relationship(Subscription, back_populates="user", uselist=False)

    def __init__(self, email: str, password: str, subscription: Subscription) -> None:
        self.email = email
        self.password = self.__encode_password(password)
        self.subscription_id = subscription

    @staticmethod
    def __encode_password(password: str) -> str:
        """
        This function is used to encode password

        :param password: original given password

        :return: hashed password
        """
        password_bytes = password.encode("utf-8")
        hasher = hashlib.sha256()
        hasher.update(password_bytes)
        hashed_password = hasher.hexdigest()
        return hashed_password

    def verify_password(self, password: str) -> bool:
        """
        This function is used to verify if password is proper

        :param password: given password

        :return: boolean if password is the same as in database
        """
        return self.__encode_password(password) == self.password

    def __repr__(self):
        return f"<User {self.user_id}, email={self.email}>"
