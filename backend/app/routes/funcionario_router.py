from fastapi import APIRouter, HTTPException, Path, Depends
from app.config import Sessionlocal
from sqlalchemy.orm import Session
from app.schemas import funcionarioSchema, requestFuncionario, responseFuncionario
from app.controllers.funcionario_controller import funcionarioController
from app.services.funcionario_service import funcionarioService

funcionario_router = APIRouter(prefix="/funcionario")

funcionario_controller = funcionarioController(service=funcionarioService)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        pass
    db.close()

@funcionario_router.get("/")
async def get_funcionarios():
    return funcionario_controller.get_funcionarios(Sessionlocal())

@funcionario_router.post("/funcionario")
async def search_funcionario(request:requestFuncionario):
    return funcionario_controller.get_funcionarioEspecifico(Sessionlocal(),request)

@funcionario_router.post("/create")
async def create_funcionario(request:requestFuncionario):
    return funcionario_controller.create_funcionario(Sessionlocal(), request)

@funcionario_router.post("/remove")
async def delete_funcionario(request:requestFuncionario):
    return funcionario_controller.remove_funcionario(Sessionlocal(), request)

@funcionario_router.post("/update")
async def update_funcionario(request:requestFuncionario):
    return funcionario_controller.update_funcionario(Sessionlocal(), request)