from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.config import settings

engine = create_async_engine(settings.POSTGRES_URL, echo=True)

SessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def create_db_tables():
    async with engine.begin() as conn:
        from app.database.models import Base  # IMPORTANTE
        await conn.run_sync(Base.metadata.create_all)
        
async def get_session():
    async with SessionLocal() as session:
        yield session
        
SessionDep = Annotated[AsyncSession, Depends(get_session)]