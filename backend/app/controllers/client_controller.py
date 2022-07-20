from app.controllers._base import BaseController
from app.services.cliente_service import ClientService


class ClientController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(ClientService())

    def get_clientes(self):
        return self.service.list_clientes()
