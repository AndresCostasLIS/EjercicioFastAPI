
from app.api import user
from fastapi import FastAPI

app = FastAPI(titile= "Ejercicio API")

app.include_router(user.router, prefix="/user", tags=["user"])