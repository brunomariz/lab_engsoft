from fastapi import FastAPI
from app.routes.example_router import example_router

app = FastAPI()

app.include_router(example_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello")
def hello():
    return {"message": "hello, world!"}
