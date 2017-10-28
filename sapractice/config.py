
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///:memory:', echo=True)
create_session = scoped_session(sessionmaker(bind=engine, autoflush=False))
base = declarative_base(bind=engine)
metadata = base.metadata
