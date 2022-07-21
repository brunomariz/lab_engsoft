from fastapi import APIRouter, HTTPException, Path, Depends
from app.config import Sessionlocal
from sqlalchemy.orm import Session
from app.schemas import salarioSchema, requestSalario, responseSalario
from app.controllers.salario_controller import salarioController
from app.services.salario_service import salarioService

salario_router = APIRouter(prefix="/salario")

salario_controller = salarioController(service=salarioService)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        pass
    db.close()

@salario_router.get("/")
async def get_salarios():
    return salario_controller.get_salarios(Sessionlocal())

@salario_router.get("/salario")
async def search_salario(request:requestSalario):
    return salario_controller.get_salarioEspecifico(Sessionlocal(),request)

@salario_router.post("/create")
async def create_salario(request:requestSalario):
    return salario_controller.create_salario(Sessionlocal(), request)

@salario_router.post("/remove")
async def remove_salario(request:requestSalario):
    return salario_controller.remove_salario(Sessionlocal(), request)

@salario_router.post("/update")
async def update_salario(request:requestSalario):
    return salario_controller.update_salario(Sessionlocal(), request)

# @salario_router.post("/create")
# async def create_salarioe(request:requestsalarioeget_db)):
#     return salario_controller.create_salarioe(db, request)
