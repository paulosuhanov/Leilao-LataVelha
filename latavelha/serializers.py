from pydantic import BaseModel, validator
from datetime import datetime
from fastapi import HTTPException, status


class CarOut(BaseModel):
    id: int
    marca: str
    model: str
    year: int
    price: float
    cat: str
    desc: str
    date_create: datetime


class CarIn(BaseModel):
    marca: str
    model: str
    year: int
    price: float
    cat: str
    desc: str
    
    @validator("price")
    def validate_price(cls, v, field):
        if v < 1.00 or v > 100000000.00:
            raise HTTPException(
                detail=f"{field.name} deve ser entre 1.00 e 100M",
                status_code=status.HTTP400_BAD_REQUEST,
            )
        return v

    @validator("year")
    def validate_year(cls, v):
        if v < 1800 or v > 2022:
            raise HTTPException(
                detail=f"O Ano deve ser entre 1800 e 2022",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return v


class UserOut(BaseModel):
    id:int
    name: str
    year: int
    username: str
    password: str
    date_create: datetime


class UserIn(BaseModel):
    name: str
    year: int
    username: str
    password: str

    @validator("year")
    def validate_year(cls, v):
        if v < 1900 or v > 2022:
            raise HTTPExpection(
                detail=f"O Ano deve ser entre 1800 e 2022",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return v