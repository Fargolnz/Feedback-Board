from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .database import Base
from .database import engine
from .routes import router

from . import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

app.include_router(router)