from app.controllers._base import BaseController
from sqlalchemy.orm import Session
from app.schemas import usuarioSchema, requestUsuario, responseUsuario
from app.services.usuario_service import usuarioService
import json

class usuarioController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(usuarioService())

    def get_usuarios(self,db:Session):
        return json.dumps([obj.toDict() for obj in self.service.getUsuarios(db)])

    def get_usuarioEspecifico(self,db:Session, request:requestUsuario):
        return json.dumps([(self.service.getUsuarioEspecifico(db, request.login)).toDict()])

    def create_usuario(self,db:Session, request:requestUsuario):
        if self.service.createUsuario(db, request):
            return responseUsuario("200","Ok","usuario criado com sucesso")
        return responseUsuario("400","Erro","Erro na criacao de usuario")

    def remove_usuario(self,db:Session, request:requestUsuario):
        if self.service.removeUsuario(db, request.login):
            return responseUsuario("200","Ok","usuario removido com sucesso")
        return responseUsuario("400","Erro","Erro na remocao de usuario")

    def update_usuario(self,db:Session, request:requestUsuario):
        if self.service.updateUsuario(db, request.login, request.senha, request.eh_admin):
            return responseUsuario("200","Ok","usuario atualizado com sucesso")
        return responseUsuario("400","Erro","Erro na atualizacao de usuario")
    
    def verify_usuario(self,db:Session, request:requestUsuario):
        if self.service.verifyUsuario(db, request.login, request.senha):
            return json.dumps([{"Usuario: ": f"{request.login}"}])
            # responseUsuario("200","Ok","Usuario permitido")
        return responseUsuario("400","Erro","Erro de autorizacao")