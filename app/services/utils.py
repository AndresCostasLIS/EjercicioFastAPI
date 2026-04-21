
from app.database.session import SessionDep
from app.models.User import UserCreate
from app.database.models import User as UserModel
from fastapi import HTTPException, status
from sqlalchemy import select



async def is_user_valid(user: UserCreate, session: SessionDep):
    result = await session.execute(
        select(UserModel).where(UserModel.email == user.email)
    )
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo ya está en uso"
    )