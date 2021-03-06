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

    def getFornecedorEspecifico(self, db:Session, CNPJ_fornecedor:str):
        resultado = db.query(fornecedor).filter(fornecedor.CNPJ_fornecedor == CNPJ_fornecedor).first()
        if resultado is None:
            resultado = []
        return resultado

    def createFornecedor(self, db:Session, Fornecedor:fornecedorSchema):
      try:
        _fornecedor = fornecedor(CNPJ_fornecedor=Fornecedor.CNPJ_fornecedor,nome_fornecedor=Fornecedor.nome_fornecedor)
        db.add(_fornecedor)
        db.commit()
        db.refresh(_fornecedor)
        return True
      except:
        return False

    def removeFornecedor(self,db:Session, CNPJ_fornecedor:str):
      try:
        _fornecedor = self.getFornecedorEspecifico(db,CNPJ_fornecedor)
        db.delete(_fornecedor)
        db.commit()
        return True
      except:
        return False

    def updateFornecedor(self,db:Session, CNPJ_fornecedor:str, nome_fornecedor: str):
      try:
        _fornecedor= self.getFornecedorEspecifico(db, CNPJ_fornecedor)
        _fornecedor.nome_fornecedor = nome_fornecedor
        db.commit()
        db.refresh(_fornecedor)
        return True
      except:
        return False