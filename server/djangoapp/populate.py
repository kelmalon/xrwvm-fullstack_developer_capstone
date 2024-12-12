from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {
            "name": "NISSAN",
            "description": "Great cars. Japanese technology",
            "country": "Japan",
            "website": "https://www.nissanusa.com/",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "Mercedes",
            "description": "Great cars. German technology",
            "country": "Germany", "website": "https://www.mbusa.com/en/home",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "Audi",
            "description": "Great cars. German technology",
            "country": "Germany",
            "website": "https://www.audiusa.com/us/web/en.html",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "Kia",
            "description": "Great cars. Korean technology",
            "country": "South Korea",
            "website": "https://www.kia.com/us/en",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "Toyota",
            "description": "Great cars. Japanese technology",
            "country": "Japan",
            "website": "https://www.toyota.com/",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
    ]

    car_make_instances = []

    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(
            name=data['name'],
            description=data['description'],
            country=data['country'],
            website=data['website'],
            created_at=data['created_at'],
            updated_last=data['updated_last']
        ))

    car_model_data = [
        {
            "name": "Pathfinder",
            "dealer_id": 1,
            "vehicle_type": "SUV",
            "model_year": 2023,
            "make": car_make_instances[0],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "Qashqai",
            "dealer_id": 1,
            "vehicle_type": "SUV",
            "model_year": 2023,
            "make": car_make_instances[0],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "XTRAIL",
            "dealer_id": 1,
            "vehicle_type": "SUV",
            "model_year": 2023,
            "make": car_make_instances[0],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "A-Class",
            "dealer_id": 1,
            "vehicle_type": "SUV",
            "model_year": 2023,
            "make": car_make_instances[1],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "C-Class",
            "dealer_id": 1,
            "vehicle_type": "SUV",
            "model_year": 2023,
            "make": car_make_instances[1],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "E-Class",
            "dealer_id": 1,
            "vehicle_type": "SUV",
            "model_year": 2023,
            "make": car_make_instances[1],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "A4",
            "dealer_id": 1,
            "vehicle_type": "SUV",
            "model_year": 2023,
            "make": car_make_instances[2],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "A5",
            "dealer_id": 1,
            "vehicle_type": "SUV",
            "model_year": 2023,
            "make": car_make_instances[2],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "A6",
            "dealer_id": 1,
            "vehicle_type": "SUV",
            "model_year": 2023,
            "make": car_make_instances[2],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "Sorrento",
            "dealer_id": 1,
            "vehicle_type": "SUV",
            "model_year": 2023,
            "make": car_make_instances[3],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "Carnival",
            "dealer_id": 1,
            "vehicle_type": "SUV",
            "model_year": 2023,
            "make": car_make_instances[3],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "Cerato",
            "dealer_id": 1,
            "vehicle_type": "Sedan",
            "model_year": 2023,
            "make": car_make_instances[3],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "Corolla",
            "dealer_id": 1,
            "vehicle_type": "Sedan",
            "model_year": 2023,
            "make": car_make_instances[4],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "Camry",
            "dealer_id": 1,
            "vehicle_type": "Sedan",
            "model_year": 2023,
            "make": car_make_instances[4],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        },
        {
            "name": "Kluger",
            "dealer_id": 1,
            "vehicle_type": "SUV",
            "model_year": 2023,
            "make": car_make_instances[4],
            "engine_type": "Gasoline",
            "created_at": "2024-12-10 15:30:00",
            "updated_last": "2024-12-10 15:47:00"
        }
        # Add more CarModel instances as needed
    ]
    
    car_model_instances = []

    for data in car_model_data:
        car_model_instances.append(CarModel.objects.create(
            name=data['name'],
            make=data['make'],
            dealer_id=data['dealer_id'],
            vehicle_type=data['vehicle_type'],
            model_year=data['model_year'],
            engine_type=data['engine_type'],
            created_at=data['created_at'],
            updated_last=data['updated_last']
        ))
