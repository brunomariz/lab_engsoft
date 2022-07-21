from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from app.model import cliente
from app.schemas import clienteSchema, requestCliente
import pandas as pd
from app.services._base import BaseService
from app.config import Sessionlocal
from app.model import cliente
from app.config import engine
#from app.config import conn

class ClientService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def getClientes(self, db:Session, skip:int=0, limit:int=100):
        resultado=db.query(cliente).offset(skip).limit(limit).all()
        return resultado

    def getClienteEspecifico(self, db:Session, CPF_cliente:str, skip:int=0, limit:int=100):
        resultado = db.query(cliente).filter(cliente.CPF_cliente == CPF_cliente).first()
        if resultado is None:
            resultado = []
        return resultado

    def createCliente(self, db:Session, request:requestCliente):
        try:
            _cliente = cliente(CPF_cliente=request.CPF_cliente, nome_cliente=request.nome_cliente)
            db.add(_cliente)
            db.commit()
            db.refresh(_cliente)
            return True
        except:
            return False

    def removeCliente(self, db:Session, CPF_cliente:str):
        try:
            _cliente = self.getClienteEspecifico(db, CPF_cliente)
            db.delete(_cliente)
            db.commit()
            return True
        except:
            return False

    def updateCliente(self,db:Session, CPF_cliente:str, nome_cliente: str):
        try:
            _cliente= self.getClienteEspecifico(db, CPF_cliente)
            _cliente.nome_cliente = nome_cliente
            db.commit()
            db.refresh(_cliente)
            return True
        except:
            return False