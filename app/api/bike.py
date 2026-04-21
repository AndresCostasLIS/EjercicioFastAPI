# app/api/bike.py

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from app.database.session import SessionDep
from app.database.models import Bike, User
from app.models.Bike import BikeCreate
from sqlalchemy import select
from app.api.core.security import  oauth2_scheme

router = APIRouter()


# CREATE
@router.post("/")
async def create_bike(data: BikeCreate, session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]):

    user = await session.get(User, data.user_id)
    if not user:
        raise HTTPException(404, "User not found")

    bike = Bike(
        basket=data.basket,
        type_id=data.type_id,
        user_id=data.user_id,
        color=data.color,
        active=True
    )

    session.add(bike)
    await session.commit()
    await session.refresh(bike)

    return bike


# GET BY ID
@router.get("/{id}")
async def get_bike(id: int, session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]):

    bike = await session.get(Bike, id)
    if not bike:
        raise HTTPException(404, "Bike not found")

    return bike


# DELETE
@router.delete("/{id}")
async def delete_bike(id: int, session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]):

    bike = await session.get(Bike, id)
    if not bike:
        raise HTTPException(404, "Bike not found")

    await session.delete(bike)
    await session.commit()

    return {"detail": "Bike deleted"}

@router.get("/")
async def get_bikes(session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]):

    result = await session.execute(select(Bike))
    cars = result.scalars().all()

    return cars