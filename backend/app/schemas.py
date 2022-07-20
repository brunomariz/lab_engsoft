from optparse import Option
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class clienteSchema(BaseModel):
    CPF_cliente: str=None
    nome_cliente: Optional[str]=None

    class config:
        orm_mode = True

class requestCliente(BaseModel):
    parameter: clienteSchema = Field(...)

class responseCliente(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class funcionarioSchema(BaseModel):
    CPF_funcionario: str=None
    nome_funcionario: Optional[str]=None

    class config:
        orm_mode = True

class requestfuncionario(BaseModel):
    parameter: funcionarioSchema = Field(...)

class responsefuncionario(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

class fornecedorSchema(BaseModel):
    CNPJ_fornecedor: str=None
    nome_fornecedor: Optional[str]=None

    class config:
        orm_mode = True

class requestfornecedor(BaseModel):
    parameter: fornecedorSchema = Field(...)

class responsefornecedor(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]