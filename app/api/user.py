from app.database.session import SessionDep
from fastapi import APIRouter, HTTPException, status
from app.models.User import UserCreate, User, UserUpdate



router = APIRouter()

@router.post("/create")
async def create_user(user: UserCreate, session: SessionDep):
    
    new_user = User(**user.model_dump(), active=True)

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return new_user


@router.get("/user")
async def get_user(id: int, session: SessionDep):
    user = await session.get(User, id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user

@router.put("/user/{id}")
async def update_user(id: int, data: UserUpdate, session: SessionDep):

    user = await session.get(User, id)

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

    user = await session.get(User, id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    await session.delete(user)
    await session.commit()

    return {"detail": "Usuario borrado correctamente"}

