from fastapi import FastAPI
from app.routes.example_router import example_router
from app.routes.client_router import client_router
from app.config import engine
import app.model as model

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

app.include_router(example_router)
app.include_router(client_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello")
def hello():
    return {"message": "hello, world!"}
