import typer
from typing import Optional
from latavelha.core import add_car_to_database, add_user_to_database
from latavelha.core import get_cars_from_database, get_users_from_database
from rich.table import Table
from rich.console import Console

main = typer.Typer(help="Leilão Lata Velha Application")

console = Console()


@main.command("add-car")
def add_car(
    marca: str,
    model: str,
    year: int = typer.Option(...),
    price: float = typer.Option(...),
    cat: str = typer.Option(...),
    desc: str = typer.Option(...),
):
    """Adds a new car to database."""
    if add_car_to_database(marca, model, year, price, cat, desc):
        print(f'Add Car to Database')
    else:
        print(f'Não foi adicionado o carro a Base de Dados')
        
@main.command("list-cars")
def list_cars(model: Optional[str] = None):
    """lists cars in database."""
    cars = get_cars_from_database()
    table = Table(title="Lista dos Carros")
    headers = ["id", "marca", "model", "year", "price", "cat", "desc", "date_create"]
    for header in headers:
        table.add_column(header, style="green")
    for car in cars:
        values = [str(getattr(car, header)) for header in headers]
        table.add_row(*values)
    console.print(table)


@main.command("add-user")
def add_user(
    name: str,
    year: int = typer.Option(...),
    username: str = typer.Option(...),
    password: str = typer.Option(...),
):
    """Adds a new user to database."""
    if add_user_to_database(name, year, username, password):
            print(f'Add User to Database')
    else:
        print(f'Não foi adicionado o usuário a Base de Dados')


@main.command("list-users")
def list_users(name: Optional[str] = None):
    """lists users in database."""
    users = get_users_from_database()
    table = Table(title="Lista dos Usuários")
    headers = ["id", "name", "year", "username", "date_create"]
    for header in headers:
        table.add_column(header, style="yellow")
    for user in users:
        values = [str(getattr(user, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
