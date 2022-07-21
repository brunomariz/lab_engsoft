from fastapi import APIRouter, HTTPException, Path, Depends
from app.config import Sessionlocal
from sqlalchemy.orm import Session
from app.schemas import usuarioSchema, requestUsuarios, responseUsuarios
from app.controllers.usuario_controller import usuariosController
from app.services.usuario_service import usuariosService


usuarios_router = APIRouter(prefix="/usuarios")

usuarios_controller = usuariosController(service=usuariosService)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        pass
    db.close()

@usuarios_router.get("/")
async def get_usuarios():
    return usuarios_controller.get_usuarios(Sessionlocal())

@usuarios_router.get("/usuarios")
async def search_usuarios(request:requestUsuarios):
    return usuarios_controller.get_usuarioEspecifico(Sessionlocal(),request)

@usuarios_router.post("/create")
async def create_usuarios(request:requestUsuarios):
    return usuarios_controller.create_usuarios(Sessionlocal(), request)

@usuarios_router.post("/remove")
async def create_usuarios(request:requestUsuarios):
    return usuarios_controller.remove_usuarios(Sessionlocal(), request)

@usuarios_router.post("/update")
async def update_usuarios(request:requestUsuarios):
    return usuarios_controller.update_usuarios(Sessionlocal(), request)

# async def verify_usuarios(request:requestUsuarios):
#     return usuarios_controller.verify_usuarios(Sessionlocal(), request)

# @usuarios_router.post("/create")
# async def create_usuariose(request:requestusuarioseget_db)):
#     return usuarios_controller.create_usuariose(db, request)
