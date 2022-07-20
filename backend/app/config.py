from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

POSTGRE_URL = "postgresql://iskndzepfsryoa:e8395b839a79f560f56c6e9ab3e6883b74284b107fa3c9092c0f1937ff1ae79c@ec2-54-87-179-4.compute-1.amazonaws.com:5432/d81on8fnotuumb"

engine = create_engine(POSTGRE_URL)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()