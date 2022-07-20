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