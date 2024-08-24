from django.db import models


class Customer(models.Model):
    first_name  = models.CharField(max_length=225)
    last_name   = models.CharField(max_length=225)
    birth_date  = models.DateField()
    country     = models.CharField(max_length=225)
    city        = models.CharField(max_length=225)
    postal_code = models.CharField(max_length=225)
    number      = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
       return f"{self.name}"


class Order(models.Model):
    customer=models.ForeignKey(to=Customer, on_delete=models.PROTECT)
    product =models.ForeignKey(to=Product, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Customer: {self.customer}. Product: {self.product}"


class Comment(models.Model):
    pass
    # product =
    # author =
    # email =
    # datetime_created =
    # datetime_modified =
