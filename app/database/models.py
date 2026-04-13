from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    phone = Column(String(15), nullable=False)
    age = Column(Integer)
    active = Column(Boolean, nullable=False)

    vehicles = relationship("Vehicle", back_populates="user")
    
class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    color = Column(String(25))
    active = Column(Boolean, nullable=False)

    type = Column(String(50))

    user = relationship("User", back_populates="vehicles")

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "vehicle",
    }


class Car(Vehicle):
    __tablename__ = "cars"

    id = Column(Integer, ForeignKey("vehicles.id"), primary_key=True)
    plate = Column(String(30), nullable=False)
    capacity = Column(Integer)
    electrical = Column(Boolean)

    __mapper_args__ = {
        "polymorphic_identity": "car",
    }
    
class Bike(Vehicle):
    __tablename__ = "bikes"

    id = Column(Integer, ForeignKey("vehicles.id"), primary_key=True)
    basket = Column(Boolean)
    type_id = Column(Integer, ForeignKey("types.id"), nullable=False)

    bike_type = relationship("Type")

    __mapper_args__ = {
        "polymorphic_identity": "bike",
    }
class Type(Base):
    __tablename__ = "types"

    id = Column(Integer, primary_key=True)
    description = Column(String(150), nullable=False)