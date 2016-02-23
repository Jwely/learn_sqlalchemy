from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

import config        # local config file


def db_connect():
    """
    Performs database connection using database settings from config.py.
    Returns sqlalchemy engine instance
    """
    if not os.path.exists(config.DATABASE_PATH):
        print("Created db at {0}".format(config.DATABASE_URL))

    engine = create_engine(config.DATABASE_URL, echo=True)
    engine.connect()
    return engine


def db_session_start(engine=None):
    if engine is None:
        engine = db_connect()
    return sessionmaker(bind=engine)




class User(declarative_base()):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" \
               % (self.name, self.fullname, self.password)




if __name__ == "__main__":
    ses = db_session_start()
