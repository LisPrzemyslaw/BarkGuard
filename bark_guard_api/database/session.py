from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from bark_guard_api.database import DATABASE_URL, _Base
from bark_guard_api.database.tables import tables # noqa

"""The database will be replaced with Postgres hosted on the Docker."""
############################
# Constants, do not change!
############################
_engine = create_engine(DATABASE_URL, echo=False)  # echo=True --> debug purposes
_Base.metadata.create_all(bind=_engine, checkfirst=True)
_Session = sessionmaker(bind=_engine)
############################################
# db_session, to be used in the application
############################################
db_session = _Session()
