from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title

class Reservation(models.Model):
    name = models.CharField(max_length=255)
    reservation_date = models.DateField()
    reservation_slot = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.reservation_date}"