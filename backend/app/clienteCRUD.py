from sqlalchemy.orm import Session
from model import cliente
from schemas import clienteSchema
import pandas as pd
from app.services._base import BaseService
from app.config import Sessionlocal
from app.model import cliente



class ClientService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def getClientes(self,db:Session, skip:int=0, limit:int=100):
        resultado=db.query(cliente).offset(skip).limit(limit).all()
        
        return pd.from_sql(resultado).to_dict('records')

    def getClienteEspecifico(self,db:Session, CPF_cliente:str):
        resultado = db.query(cliente).filter(cliente.CPF_cliente == CPF_cliente).first()
        return pd.from_sql(resultado).to_dict('records')

    def create_cliente(self,db:Session, Cliente:clienteSchema):
        _cliente = cliente(nome_cliente=Cliente.nome_cliente)
        db.add(_cliente)
        db.commit()
        db.refresh(_cliente)
        return pd.from_sql(_cliente).to_dict('records')

    def remove_cliente(self,db:Session, CPF_cliente:str):
        _cliente = self.getClienteEspecifico(db,CPF_cliente)
        db.delete(_cliente)
        db.commit()
        return pd.from_sql(_cliente).to_dict('records')

    def update_cliente(self,db:Session, CPF_cliente:str, nome_cliente: str):
        _cliente= self.getClienteEspecifico(db, CPF_cliente)
        _cliente.nome_cliente = nome_cliente
        db.commit()
        db.refresh(_cliente)
        return pd.from_sql(_cliente).to_dict('records')