from fastapi import APIRouter
from app.models.User import User, UserCreate


router = APIRouter()

@router.post("/create")
def create_user(user: UserCreate):
    new_user = user.create_user()
    return {
        "detail": "User created",
        "user_id": new_user.id,
        "user": new_user
    }
    
@router.get("/{user_id}")
def get_user(user_id: int):
    # user = user.get_user()
    # return user
    pass