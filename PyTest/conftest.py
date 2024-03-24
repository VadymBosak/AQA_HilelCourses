import pytest
from car import Car

@pytest.fixture
def new_car():
    car = Car("Toyota", "Camry", miles_limit=100)
    yield car

@pytest.fixture
def car_with_miles():
    car = Car("Honda", "Accord", miles_limit=200)
    car.drive(50)
    yield car
