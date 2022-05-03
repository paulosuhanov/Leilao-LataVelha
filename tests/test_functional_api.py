from fastapi.testclient import TestClient
from latavelha.api import api


client = TestClient(api)


def test_add_car_via_api():
    response = client.post(
        "/api/v1/cars",
        json={
            "marca": "Ford",
            "model": "Fusion",
            "year": 2010,
            "price": 50000.00,
            "cat": "Sedan",
            "desc": "Carro com baixa Kilometragem",
        },
    )
    assert response.status_code == 200
    result = response.json()
    assert result["model"] == "Fusion"
    assert result["id"] == 1


def test_add_user_via_api():
    response = client.post(
        "/api/v1/users", json={
            "name": "José Maria",
            "year": 1975,
            "username": "jose.maria",
            "password": "pass",
        },
    )
    assert response.status_code == 200
    result = response.json()
    assert result["username"] == "jose.maria"
    assert result["id"] == 1

def test_list_cars():
    response = client.get("/api/v1/cars")
    assert response.status_code == 200
    result = response.json()
    assert len(result) == 0

def test_list_users():
    response = client.get("/api/v1/users")
    assert response.status_code == 200
    result = response.json()
    assert len(result) == 0
