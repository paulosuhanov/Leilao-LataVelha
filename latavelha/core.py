from typing import List

from sqlmodel import select

from latavelha.database import get_session
from latavelha.models import Car, User


def add_car_to_database(
    marca: str,
    model: str,
    year: int,
    price: float,
    cat: str,
    desc: str,
) -> bool:
    with get_session() as session:
        car = Car(
            marca=marca,
            model=model,
            year=year,
            price=price,
            cat=cat,
            desc=desc,
        )
        session.add(car)
        session.commit()
    return True


def get_cars_from_database() -> List[Car]:
    with get_session() as session:
        sql = select(Car)
        return list(session.exec(sql))


def add_user_to_database(
    name: str, year: int, username: str, password: str
) -> bool:
    with get_session() as session:
        user = User(name=name, year=year, username=username, password=password)
        session.add(user)
        session.commit()
    return True


def get_users_from_database() -> List[User]:
    with get_session() as session:
        sql = select(User)
        return list(session.exec(sql))
