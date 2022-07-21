from fastapi.routing import APIRouter
from app.controllers.example_controller import ExampleController

example_router = APIRouter(prefix="/example")

example_controller = ExampleController()

@example_router.get("/")
async def get_example():
    return example_controller.index()

@example_router.get("/additional_method")
async def get_example_additional_method():
    return example_controller.example_additional_method()
