from typer.testing import CliRunner

from latavelha.cli import main

runner = CliRunner()

def test_add_car():
    result = runner.invoke(
        main, [
            'add-car',
            'Honda',
            'Civic',
            '--year=2013',
            '--price=5000.00',
            '--cat="Sedan"',
            '--desc="Carro em ótimo estado"'
        ]
    )
    assert result.exit_code == 0
    assert "Add Car to Database" in result.stdout


def test_add_user():
    result1 = runner.invoke(
        main, [
            'add-user',
            '"José Maria"',
            '--year=1975',
            '--username="jose.maria"',
            '--password="12333"'
        ]
    )
    assert result1.exit_code == 0
    assert "Add User to Database" in result1.stdout

def test_get_cars():
    pass

def test_get_users():
    pass
