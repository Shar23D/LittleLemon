import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Booking(models.Model):
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], default=1)
    reservation_date = models.DateField(default=datetime.date.today)
    def default_reservation_time():
        return datetime.datetime.now().time()
    reservation_time = models.TimeField(default=default_reservation_time)    
    comment = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    menu_item = models.TextField(max_length=1000, default="")

    def __str__(self) -> str:
        return self.name