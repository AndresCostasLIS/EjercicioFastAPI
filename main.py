from contextlib import asynccontextmanager
from app.api import user, vehicle, car, bike, type
from fastapi import FastAPI
from app.database.session import create_db_tables

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    await create_db_tables()
    yield

app = FastAPI(lifespan= lifespan_handler,)

app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(vehicle.router, prefix="/vehicle", tags=["vehicle"])
app.include_router(car.router, prefix="/car", tags=["car"])
app.include_router(bike.router, prefix="/bike", tags=["bike"])
app.include_router(type.router, prefix="/type", tags=["type"])