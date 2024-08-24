from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    # last_name
    # birth_date
    # country
    # city
    # postal_code
    # number
