from app.api.user import get_user
from app.database.session import SessionDep
from fastapi import APIRouter, HTTPException, status
from app.models.Vehicle import VehicleCreate
from app.database.models import Vehicle, User



router = APIRouter()    

@router.post("/")
async def create_vehicle(user_id: int, data: VehicleCreate, session: SessionDep):

    user = await session.get(User, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    vehicle = Vehicle(
        color=data.color,
        active=True,
        user_id=user_id   # 👈 mejor que pasar el objeto entero
    )

    session.add(vehicle)
    await session.commit()
    await session.refresh(vehicle)

    return vehicle


@router.get("/{id}")
async def get_vehicle(id: int, session: SessionDep):
    vehicle = await session.get(Vehicle, id)
    if not vehicle:
        raise HTTPException(404, "Vehicle not found")
    return vehicle


@router.delete("/{id}")
async def delete_vehicle(id: int, session: SessionDep):
    vehicle = await session.get(Vehicle, id)
    if not vehicle:
        raise HTTPException(404, "Vehicle not found")

    await session.delete(vehicle)
    await session.commit()

    return {"detail": "Vehicle deleted"}