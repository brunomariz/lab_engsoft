from app.services._base import BaseService


class ClientService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def list_clientes(self):
        return {"method": "example additional method"}


