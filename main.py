from contextlib import asynccontextmanager
from app.api import user
from fastapi import FastAPI
from app.database.session import create_db_tables

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    await create_db_tables()
    yield

app = FastAPI(lifespan= lifespan_handler,)

app.include_router(user.router, prefix="/user", tags=["user"])