from importlib.resources import path
from typing import List

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from latavelha.core import get_cars_from_database, get_users_from_database
from latavelha.database import get_session
from latavelha.models import Car, User
from latavelha.serializers import CarIn, CarOut, UserIn, UserOut

api = FastAPI(title="Leilão Lata Velha")


templates = Jinja2Templates(directory="./templates")


@api.get("/")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})

# @api.get("/", response_class=FileResponse)
# def index():
#     path1 = '/latavelha/templates/index.html'
#     return FileResponse(path1)


@api.get("/api/v1/cars", response_model=List[CarOut])
async def list_cars():
    cars = get_cars_from_database()
    return cars


@api.get("/api/v1/users", response_model=List[UserOut])
async def list_users():
    users = get_users_from_database()
    return users


@api.post("/api/v1/cars", response_model=CarOut)
async def add_car(car_in: CarIn):
    car = Car(**car_in.dict())
    with get_session() as session:
        session.add(car)
        session.commit()
        session.refresh(car)
    return car


@api.post("/api/v1/users", response_model=UserOut)
async def add_user(user_in: UserIn):
    user = User(**user_in.dict())
    with get_session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return user
