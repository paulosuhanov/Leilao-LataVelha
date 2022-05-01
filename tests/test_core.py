from latavelha.core import get_cars_from_database, get_users_from_database
from latavelha.core import add_car_to_database, add_user_to_database


def test_add_car_to_database():
    assert add_car_to_database("Chevrolet", "Onix", 2020, 50111.0, "Popular", "Carro Semi-Novo")


def test_get_cars_from_database():
    add_car_to_database("Chevrolet", "Onix", 2020, 50111.0, "Popular", "Carro Semi-Novo")
    results = get_cars_from_database()
    assert len(results) > 0


def test_add_user_to_database():
    assert add_user_to_database("Joaquim", 2019, "joaquim", "123")


def test_get_users_from_database():
    add_user_to_database("Joaquim", 2019, "joaquim", "123")
    results = get_users_from_database()
    assert len(results) > 0
