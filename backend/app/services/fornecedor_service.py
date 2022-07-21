from sqlalchemy.orm import Session
from app.schemas import fornecedorSchema
import pandas as pd
import json 
from app.services._base import BaseService
from app.config import Sessionlocal
from app.model import fornecedor
from app.config import engine
#from app.config import conn

class fornecedorService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def getFornecedores(self, db:Session, skip:int=0, limit:int=100):
        resultado=db.query(fornecedor).offset(skip).limit(limit).all()
        return resultado
        # json.dumps([obj.toDict() for obj in resultado])

    def getFornecedorEspecifico(self, db:Session, CPF_fornecedor:str):
        resultado = db.query(fornecedor).filter(fornecedor.CPF_fornecedor == CPF_fornecedor).first()
        if resultado is None:
            resultado = []
        return resultado

    def createFornecedor(self, db:Session, Fornecedor:fornecedorSchema):
        _fornecedor = fornecedor(nome_fornecedor=Fornecedor.nome_fornecedor)
        db.add(_fornecedor)
        db.commit()
        db.refresh(_fornecedor)
        return _fornecedor

    def removeFornecedor(self,db:Session, CPF_fornecedor:str):
        _fornecedor = self.getFornecedorEspecifico(db,CPF_fornecedor)
        db.delete(_fornecedor)
        db.commit()
        return _fornecedor

    def updateFornecedor(self,db:Session, CPF_fornecedor:str, nome_fornecedor: str):
        _fornecedor= self.getFornecedorEspecifico(db, CPF_fornecedor)
        _fornecedor.nome_fornecedor = nome_fornecedor
        db.commit()
        db.refresh(_fornecedor)
        return _fornecedor