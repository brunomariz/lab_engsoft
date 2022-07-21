from sqlalchemy.orm import Session
from app.schemas import vendaSchema
import pandas as pd
import json 
from app.services._base import BaseService
from app.config import Sessionlocal
from app.model import venda
from app.config import engine
#from app.config import conn

class vendaService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def getVendas(self, db:Session, skip:int=0, limit:int=100):
        resultado=db.query(venda).offset(skip).limit(limit).all()
        return resultado
        # json.dumps([obj.toDict() for obj in resultado])

    def getVendaEspecifico(self, db:Session, id_venda:str):
        resultado = db.query(venda).filter(venda.id_venda == id_venda).first()
        if resultado is None:
            resultado = []
        return resultado

    def createVenda(self, db:Session, Venda:vendaSchema):
      try:
        _venda = venda(id_venda=Venda.id_venda,nome_venda=Venda.nome_venda, venda_fixo=Venda.venda_fixo,data_admissao=Venda.data_admissao,eh_gerente=Venda.eh_gerente,comissao_venda=Venda.comissao_venda)
        db.add(_venda)
        db.commit()
        db.refresh(_venda)
        return True
      except:
        return False

    def removeVenda(self,db:Session, id_venda:str):
      try:
        _venda = self.getvendaEspecifico(db,id_venda)
        db.delete(_venda)
        db.commit()
        return True
      except:
        return False

    def updateVenda(self,db:Session, id_venda, data_venda,valor_por_item,quantidade_venda):
      try:
        _venda= self.getvendaEspecifico(db, id_venda)
        _venda.data_venda = data_venda
        _venda.valor_por_item=valor_por_item
        _venda.quantidade_venda=quantidade_venda
        db.commit()
        db.refresh(_venda)
        return True
      except:
        return False