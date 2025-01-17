from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://postgres:password!@localhost:5432/fast'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocomit=False, autoflush=False, bind=engine)

Base = declarative_base()