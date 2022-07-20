from sqlalchemy.orm import Session
from app.model import cliente
from app.schemas import clienteSchema
import pandas as pd

def getClientes(db:Session, skip:int=0, limit:int=100):
    resultado=db.query(cliente).offset(skip).limit(limit).all()
    # pd.Dataframe(resultado.__dict__)
    # {col.name: getattr(resultado, col.name)for col in resultado.__table__.columns}
    return resultado

def getClienteEspecifico(db:Session, CPF_cliente:str):
    return db.query(cliente).filter(cliente.CPF_cliente == CPF_cliente).first()

def create_cliente(db:Session, Cliente:clienteSchema):
    _cliente = cliente(nome_cliente=Cliente.nome_cliente)
    db.add(_cliente)
    db.commit()
    db.refresh(_cliente)
    return _cliente

def remove_cliente(db:Session, CPF_cliente:str):
    _cliente = getClienteEspecifico(db,CPF_cliente)
    db.delete(_cliente)
    db.commit()

def update_cliente(db:Session, CPF_cliente:str, nome_cliente: str):
    _cliente= getClienteEspecifico(db, CPF_cliente)
    _cliente.nome_cliente = nome_cliente
    db.commit()
    db.refresh(_cliente)
    return _cliente