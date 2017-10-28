
from os.path import abspath, join, dirname, exists
from os import mkdir

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

HERE = dirname(__file__)
DATA_DIRECTORY = abspath(join(HERE, '../data'))

if not exists(DATA_DIRECTORY):
    mkdir(DATA_DIRECTORY)

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine(f'sqlite:///{DATA_DIRECTORY}/quiz.sqlite', echo=True)
create_session = scoped_session(sessionmaker(bind=engine, autoflush=False))
base = declarative_base(bind=engine)
metadata = base.metadata
