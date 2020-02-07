import os

# decorator to cache funtion results
from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@lru_cache(maxsize=32)
def engine(db_url=None):
    db_url = db_url or os.getenv("DB_URL")
    if not db_url:
        raise ValueError("Database URL is required")
    return create_engine(db_url)


def get_connection(db_url=None):
    """returns a connection from an engine"""
    return engine(db_url).connect()


@lru_cache(maxsize=32)
def session_class(db_url=None):
    return sessionmaker(bind=engine(db_url))


try:
    Session = session_class()
except:
    pass
