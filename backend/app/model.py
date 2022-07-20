from sqlalchemy import Column, Integer, String, VARCHAR
from config import Base

class cliente(Base):
    __tablename__ = 'Cliente'
    CPF_cliente=Column(str, primary_key=True)
    nome_cliente=Column(str)