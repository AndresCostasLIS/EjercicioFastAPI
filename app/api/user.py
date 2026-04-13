from fastapi import APIRouter, HTTPException, status
from app.models.User import User, UserCreate


router = APIRouter()

@router.post("/create")
async def create_user(user: UserCreate):
    new_user = user.create_user()
    return {
        "detail": "User created",
        "user_id": new_user.id,
        "user": new_user
    }
    
@router.get("/user", response_model=User)
async def get_user(id:int, session: SessionDep):
    user = await session.get(User, id)
    if user is None:
        raise HTTPException(
            status_code= status.HT
        )
    