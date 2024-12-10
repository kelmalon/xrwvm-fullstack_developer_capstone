# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    country = models.CharField(max_length=100)
    website = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_last = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Country: {self.country}, Website: {self.website}, Created At: {self.created_at}, Updated Last: {self.updated_last}, Description: {self.description})"

class CarModel(models.Model):
    TYPE_CHOICES = {
        ('Hatchback', 'Hatchback'),
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Station Wagon', 'Station Wagon'),
        ('Van', 'Van')
    }
    ENGINE_CHOICES = {
        ('Gasoline', 'Gasoline'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric')
    }
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100,choices=TYPE_CHOICES)
    model_year = models.IntegerField()
    engine_type = models.CharField(max_length=100,choices=ENGINE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_last = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Make: {self.make}, DealerID: {self.dealer_id}, VehicleType: {self.vehicle_type}, ModelYear: {self.model_year}, EngineType: {self.engine_type}, CreatedAt: {self.created_at}, UpdatedLast: {self.updated_last})"


# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
