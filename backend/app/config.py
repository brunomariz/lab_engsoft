from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

POSTGRE_URL = "postgresql://aluno:secret@localhost:5543/lab_engsoft"

engine = create_engine(POSTGRE_URL)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()