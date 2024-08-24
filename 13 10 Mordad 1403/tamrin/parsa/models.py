from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=255)
    production_year = models.DateField()
    color = models.CharField(max_length=255)
    number_of_gears = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.color} {self.brand}"