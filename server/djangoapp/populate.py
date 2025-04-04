def initiate():
    print("Populate not implemented. Add data manually")
from .models import CarMake, CarModel
from datetime import date

def initiate():
    car_make_data = [
        {"name": "Nissan", "description": "Great Japanese cars"},
        {"name": "Mercedes", "description": "Luxury German cars"},
        {"name": "Audi", "description": "High-performance German cars"},
        {"name": "Kia", "description": "Affordable Korean cars"},
        {"name": "Toyota", "description": "Reliable Japanese cars"},
    ]

    car_make_instances = [CarMake.objects.create(**data) for data in car_make_data]

    car_model_data = [
        {"name": "Pathfinder", "car_type": "SUV", "year": date(2023, 1, 1), "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "A-Class", "car_type": "Sedan", "year": date(2023, 1, 1), "car_make": car_make_instances[1], "dealer_id": 2},
    ]

    for data in car_model_data:
        CarModel.objects.create(**data)
