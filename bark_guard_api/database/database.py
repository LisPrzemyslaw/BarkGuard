import os
import hashlib

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, create_engine

_Base = declarative_base()


class User(_Base):
    __tablename__ = "user"

    user_id = Column("user_id", Integer, primary_key=True)
    email = Column("email", String)
    password = Column("password", String)

    def __init__(self, user_id: int, email: str, password: str) -> None:
        self.user_id = user_id
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


"""The database will be replaced with Postgres hosted on the Docker."""
_engine = create_engine(f"sqlite:///{os.path.join(os.path.dirname(os.path.realpath(__file__)), 'database.db')}", echo=False)  # echo=True --> debug purposes
_Base.metadata.create_all(bind=_engine)
_Session = sessionmaker(bind=_engine)

db_session = _Session()
