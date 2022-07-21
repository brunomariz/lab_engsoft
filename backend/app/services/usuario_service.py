from sqlalchemy.orm import Session
from app.schemas import usuarioSchema
import pandas as pd
import json 
from app.services._base import BaseService
from app.config import Sessionlocal
from app.model import usuario
from app.config import engine
#from app.config import conn

class usuarioService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def getUsuarios(self, db:Session, skip:int=0, limit:int=100):
        resultado=db.query(usuario).offset(skip).limit(limit).all()
        return resultado
        # json.dumps([obj.toDict() for obj in resultado])

    def getUsuarioEspecifico(self, db:Session, login:str):
        resultado = db.query(usuario).filter(usuario.login == login).first()
        if resultado is None:
            resultado = []
        return resultado

    def createUsuario(self, db:Session, Usuario:usuarioSchema):
      try:
        _usuario = usuario(login=Usuario.login,senha=Usuario.senha,eh_admin=Usuario.eh_admin)
        db.add(_usuario)
        db.commit()
        db.refresh(_usuario)
        return True
      except:
        return False

    def removeUsuario(self,db:Session, login:str):
      try:
        _usuario = self.getUsuarioEspecifico(db,login)
        db.delete(_usuario)
        db.commit()
        return True
      except:
        return False

    def updateUsuario(self,db:Session, login:str, senha: str):
      try:
        _usuario= self.getusuarioEspecifico(db, login)
        _usuario.senha=senha
        db.commit()
        db.refresh(_usuario)
        return True
      except:
        return False
      
    def verifyUsuario(self,db:Session,login:str,senha:str):
      try:
        _usuario= self.getusuarioEspecifico(db, login)
        if _usuario.senha == senha:
          return True
        return False
      except:
        return False