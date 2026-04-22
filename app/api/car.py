from app.api.user import get_user
from app.database.session import SessionDep
from fastapi import APIRouter, Depends, HTTPException
from app.models.Car import CarCreate
from app.database.models import Car, User
from sqlalchemy import select
from typing import Annotated
from app.api.core.security import oauth2_scheme


router = APIRouter()    

@router.post("/car")
async def create_car(data: CarCreate, session: SessionDep,token: Annotated[str, Depends(oauth2_scheme)]):

    # comprobar usuario
    user = await session.get(User, data.user_id)
    if not user:
        raise HTTPException(404, "User not found")

    car = Car(
        user_id=data.user_id,
        color=data.color,
        active=True,
        plate=data.plate,
        capacity=data.capacity,
        electrical=data.electrical
    )

    session.add(car)
    await session.commit()
    await session.refresh(car)

    return car

@router.get("/{id}")
async def get_car(id: int, session: SessionDep,token: Annotated[str, Depends(oauth2_scheme)]):

    car = await session.get(Car, id)

    if not car:
        raise HTTPException(404, "Car not found")

    return car

@router.put("/{id}")
async def update_car(id: int, data: CarCreate, session: SessionDep,token: Annotated[str, Depends(oauth2_scheme)]):

    car = await session.get(Car, id)

    if not car:
        raise HTTPException(404, "Car not found")

    # actualizar campos
    car.color = data.color
    car.plate = data.plate
    car.capacity = data.capacity
    car.electrical = data.electrical
    car.active = data.active

    await session.commit()
    await session.refresh(car)

    return car


@router.delete("/{id}")
async def delete_car(id: int, session: SessionDep,token: Annotated[str, Depends(oauth2_scheme)]):

    car = await session.get(Car, id)

    if not car:
        raise HTTPException(404, "Car not found")

    await session.delete(car)
    await session.commit()

    return {"detail": "Car deleted"}


@router.get("/")
async def get_cars(session: SessionDep,token: Annotated[str, Depends(oauth2_scheme)]):

    result = await session.execute(select(Car))
    cars = result.scalars().all()

    return cars