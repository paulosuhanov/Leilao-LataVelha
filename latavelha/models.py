from datetime import datetime
from typing import Optional

from pydantic import validator
from sqlmodel import Field, SQLModel


class Car(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    marca: str
    model: str
    year: int
    price: float
    cat: str
    desc: str
    date_create: datetime = Field(default_factory=datetime.now)

    @validator("price")
    def validate_price(cls, v, field):
        if v < 1.00 or v > 100000000.00:
            raise RuntimeError("{field.name} deve ser entre 1.00 e 100M")
        return v

    @validator("year")
    def validate_year(cls, v):
        if v < 1800 or v > 2022:
            raise RuntimeError("O Ano deve ser entre 1800 e 2022")
        return v


class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    year: int
    username: str
    password: str
    date_create: datetime = Field(default_factory=datetime.now)

    @validator("year")
    def validate_year(cls, v):
        if v < 1900 or v > 2022:
            raise RuntimeError("O Ano deve ser entre 1800 e 2022")
        return v
