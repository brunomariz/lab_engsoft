from app.services._base import BaseService


class BaseController:
    def __init__(self, service=BaseService()) -> None:
        self.service = service

    def index(self):
        return self.service.index()
