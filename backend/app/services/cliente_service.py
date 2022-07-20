from app.services._base import BaseService
from app.config import Sessionlocal
from app.model import cliente


class ClientService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def list_clientes(self):
        return Sessionlocal.query(cliente)
        #return {"method": "example additional method"}


