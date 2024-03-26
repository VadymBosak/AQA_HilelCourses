import pytest
from car import Car

@pytest.fixture
def new_car_with_started_engine(new_car):
    new_car.start_engine()
    return new_car

@pytest.mark.parametrize('miles', [0, 1, 50, 99, 100])
def test_drive_within_limit(new_car_with_started_engine, miles):
    assert new_car_with_started_engine.drive(miles) == f"Driving {miles} miles."

def test_drive_beyond_limit(new_car_with_started_engine):
    assert new_car_with_started_engine.drive(101) == "The miles limit has been exceeded"
