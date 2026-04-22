# app/api/type.py

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from app.database.session import SessionDep
from app.database.models import Type
from app.models.Type import TypeCreate, TypeResponse
from app.api.core.security import  oauth2_scheme
router = APIRouter()


# CREATE
@router.post("/", response_model=TypeResponse)
async def create_type(data: TypeCreate, session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]):

    type_obj = Type(description=data.description)

    session.add(type_obj)
    await session.commit()
    await session.refresh(type_obj)

    return type_obj


# GET BY ID
@router.get("/{id}", response_model=TypeResponse)
async def get_type(id: int, session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]):

    type_obj = await session.get(Type, id)
    if not type_obj:
        raise HTTPException(404, "Type not found")

    return type_obj


# UPDATE
@router.put("/{id}", response_model=TypeResponse)
async def update_type(id: int, data: TypeCreate, session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]):

    type_obj = await session.get(Type, id)
    if not type_obj:
        raise HTTPException(404, "Type not found")

    type_obj.description = data.description

    await session.commit()
    await session.refresh(type_obj)

    return type_obj


# DELETE
@router.delete("/{id}")
async def delete_type(id: int, session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]):

    type_obj = await session.get(Type, id)
    if not type_obj:
        raise HTTPException(404, "Type not found")

    await session.delete(type_obj)
    await session.commit()

    return {"detail": "Type deleted"}