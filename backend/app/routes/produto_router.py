from fastapi import APIRouter, HTTPException, Path, Depends
from app.config import Sessionlocal
from sqlalchemy.orm import Session
from app.schemas import produtoSchema, requestProduto,requestQuantidadeProduto, requestPromocaoProduto, requestPrecoProduto ,responseProduto
from app.controllers.produto_controller import ProdutoController
from app.services.produto_service import ProdutoService


produto_router = APIRouter(prefix="/produto")

produto_controller = ProdutoController(service=ProdutoService)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        pass
    db.close()


@produto_router.get("/")
async def get_produtos():
    return produto_controller.getProdutos(Sessionlocal())

@produto_router.get("/produto/")
async def get_produto_by_codigo(codigo : int):
    return produto_controller.getPrduto_byCodigo(Sessionlocal(), codigo)

@produto_router.post("/create/")
async def criar_produto(produto : requestProduto):
    return 200 if produto_controller.createProduto(Sessionlocal(), produto) else 400

@produto_router.delete("/remove/")
async def delete_produto(codigo: int):
    return 200 if produto_controller.remove_produto(Sessionlocal(), codigo) else 400

@produto_router.patch("/updateQuantidade/")
async def setQuantidade(request : requestQuantidadeProduto):
    return 200 if produto_controller.setQuantidadeProduto(Sessionlocal(), request) else 400

@produto_router.patch("/updatePromocao/")
async def setPromocao(request : requestQuantidadeProduto):
    return 200 if produto_controller.setPromocaoProduto(Sessionlocal(), request) else 400

@produto_router.patch("/updatePreco/")
async def setPreco(request : requestPrecoProduto):
    return 200 if produto_controller.setPrecoProduto(Sessionlocal(), request) else 400