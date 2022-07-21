from fastapi import FastAPI
from app.routes.example_router import example_router
from app.routes.client_router import client_router
from app.routes.fornecedor_router import fornecedor_router
from app.routes.funcionario_router import funcionario_router
from app.routes.salario_router import salario_router
from app.routes.produto_router import produto_router
from app.routes.compra_router import compra_router
from app.routes.usuario_router import usuario_router
from app.routes.venda_router import venda_router
from app.config import engine
import app.model as model
import uvicorn

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

app.include_router(example_router)
app.include_router(client_router)
app.include_router(fornecedor_router)
app.include_router(funcionario_router)
app.include_router(salario_router)
app.include_router(venda_router)
app.include_router(usuario_router)
app.include_router(produto_router)
app.include_router(compra_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello")
def hello():
    return {"message": "hello, world!"}

