from fastapi import APIRouter, HTTPException, Path, Depends
from app.config import Sessionlocal
from sqlalchemy.orm import Session
from app.schemas import usuarioSchema, requestUsuario, responseUsuario
from app.controllers.usuario_controller import usuarioController
from app.services.usuario_service import usuarioService


usuario_router = APIRouter(prefix="/usuarios")

usuario_controller = usuarioController(service=usuarioService)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        pass
    db.close()

@usuario_router.get("/")
async def get_usuarios():
    return usuario_controller.get_usuarios(Sessionlocal())

@usuario_router.get("/usuarios")
async def search_usuario(request:requestUsuario):
    return usuario_controller.get_usuarioEspecifico(Sessionlocal(),request)

@usuario_router.post("/create")
async def create_usuario(request:requestUsuario):
    return usuario_controller.create_usuarios(Sessionlocal(), request)

@usuario_router.post("/remove")
async def remove_usuario(request:requestUsuario):
    return usuario_controller.remove_usuarios(Sessionlocal(), request)

@usuario_router.post("/update")
async def update_usuario(request:requestUsuario):
    return usuario_controller.update_usuarios(Sessionlocal(), request)

@usuario_router.post("/login")
async def verify_usuario(request:requestUsuario):
    return usuario_controller.verify_usuario(Sessionlocal(), request)