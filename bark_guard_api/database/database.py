import os

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

_Base = declarative_base()

"""The database will be replaced with Postgres hosted on the Docker."""
_engine = create_engine(f"sqlite:///{os.path.join(os.path.dirname(os.path.realpath(__file__)), 'database.db')}", echo=False)  # echo=True --> debug purposes
_Base.metadata.create_all(bind=_engine)
_Session = sessionmaker(bind=_engine)

db_session = _Session()
