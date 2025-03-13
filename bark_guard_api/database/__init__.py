import os

from sqlalchemy.orm import declarative_base

DATABASE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'database.db')
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
_Base = declarative_base()
