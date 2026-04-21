from datetime import datetime, timedelta, timezone

from sqlalchemy import select

from app.database.session import SessionDep
from fastapi import APIRouter, HTTPException, status
from app.database.models import User as UserModel
from app.models.User import UserCreate, UserUpdate
from passlib.context import CryptContext
from app.services.utils import is_user_valid
import jwt
from app.config import jwt_settings


router = APIRouter()
password_context = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"])


@router.post("/create")
async def create_user(user: UserCreate, session: SessionDep):
    
    await is_user_valid(user, session)
    
    password_hash = password_context.hash(user.password)
    print(password_hash)
    new_user = UserModel(
        name=user.name,
        email=user.email,
        phone=user.phone,
        age=user.age,
        password=password_hash,
        active=True
    )
    print(type(new_user))
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return new_user


@router.get("/user")
async def get_user(id: int, session: SessionDep):
    user = await session.get(UserModel, id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user

@router.put("/user/{id}")
async def update_user(id: int, data: UserUpdate, session: SessionDep):

    user = await session.get(UserModel, id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(user, key, value)

    await session.commit()
    await session.refresh(user)

    return user

@router.delete("/{id}")
async def delete_user(id: int, session: SessionDep):

    user = await session.get(UserModel, id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    await session.delete(user)
    await session.commit()

    return {"detail": "Usuario borrado correctamente"}

@router.post("/login")
async def login(email: str, password: str, session: SessionDep):
    user = await session.execute(select(UserModel).where(UserModel.email == email))
    user = user.scalar_one_or_none()

    if not user or not password_context.verify(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )
    token = jwt.encode({
        "user_id": user.id, 
        "email": user.email,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)}
        ,key=jwt_settings.JWT_SECRET_KEY, algorithm="HS256")
    return {"access_token": token}