
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
create_session = sessionmaker(bind=engine, autoflush=False)
base = declarative_base(bind=engine)
metadata = base.metadata
