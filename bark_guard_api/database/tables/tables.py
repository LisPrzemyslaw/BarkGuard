import hashlib

from sqlalchemy import Column, Integer, String
from bark_guard_api.database.database import _Base


class User(_Base):
    __tablename__ = "user"

    user_id = Column("user_id", Integer, primary_key=True, autoincrement=True)
    email = Column("email", String)
    password = Column("password", String)

    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = self.__encode_password(password)

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
