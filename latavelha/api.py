from typing import List

from fastapi import FastAPI, Request
from fastapi.middleware.wsgi import WSGIMiddleware

from flask import Flask, render_template, jsonify, request

from latavelha.core import get_cars_from_database, get_users_from_database
from latavelha.database import get_session
from latavelha.models import Car, User
from latavelha.serializers import CarIn, CarOut, UserIn, UserOut


# init FastAPI APP
api = FastAPI(title="Leilão Lata Velha")
flask_app = Flask(__name__, template_folder="../latavelha/app/templates")

api.mount("/leilao", WSGIMiddleware(flask_app))


# Flask Section
@flask_app.route("/")
def index():
    # Renderiza página inicial
    return render_template("index.html")


@flask_app.route("/sales")
def sales():
    # Renderiza página de venda
    return render_template("sales.html")


@flask_app.route("/sales/new")
def register_sale():
    return render_template("sales-new.html")


@flask_app.route("/sales/create", methods=["POST"])
def new_product():
    # Lógica para criar produtos
    nameproduct = request.form["input-nameproduct"]
    priceproduct = request.form["input-price"]
    categoryproduct = request.form["select-category"]
    datelimitproduct = request.form["input-datelimit"]
    return jsonify(
        {"status": 200, "text": f"{nameproduct} create successfully"}
    )


@flask_app.route("/sales/<id>")
def sale(id):
    # Renderiza página de cada produto em leilão
    return jsonify({"status": 200, "text": "Product is here!"})


@flask_app.route("/user/login")
def login_user():
    # Renderiza página de login de usuário
    return render_template("login.html")


@flask_app.route("/user/auth", methods=["POST"])
def do_login():
    # Lógica para logar usuário
    user = request.form["input-username"]
    return jsonify({"status": 200, "text": f"{user} login successfully"})


@flask_app.route("/user/register")
def register_user():
    # Renderiza página de registro de usuário
    return render_template("/user/register.html")


@flask_app.route("/user/new", methods=["POST"])
def new_user():
    user = request.form["input-username"]
    # Lógica para registro de usuário
    return jsonify({"status": 200, "text": f"{user} register successfully"})


# Section FastAPI
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
