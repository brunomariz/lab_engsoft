from app.services._base import BaseService


class ExampleService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def example_additional_method(self):
        return {"method": "example additional method"}
