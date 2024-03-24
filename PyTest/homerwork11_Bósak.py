import pytest

def test_start_engine(new_car):
    assert new_car.start_engine() == "Engine started."

def test_stop_engine(new_car):
    new_car.start_engine()
    assert new_car.stop_engine() == "Engine stopped."

def test_drive_within_limit(new_car):
    new_car.start_engine()
    assert new_car.drive(50) == "Driving 50 miles."

def test_drive_beyond_limit(new_car):
    new_car.start_engine()
    assert new_car.drive(150) == "The miles limit has been exceeded"

def test_drive_when_off(new_car):
    assert new_car.drive(50) == "Cannot drive. Engine is off."

def test_drive_negative_miles(new_car):
    new_car.start_engine()
    assert new_car.drive(-50) == "Driving -50 miles."  # Negative miles allowed

def test_clear_miles(car_with_miles):
    assert car_with_miles.miles_limit == 150  # Check initial miles remaining
    car_with_miles.drive(100)  # Drive more miles
    assert car_with_miles.miles_limit == 50  # Check remaining miles after driving