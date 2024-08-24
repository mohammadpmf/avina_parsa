from django.db import models
from django.conf import settings


class BlogPost(models.Model):
    CHOICES = (
        ('pu', 'Published'),
        ('dr', 'Draft'),
        ('de', 'Deleted'),
    )

    author            = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title             = models.CharField(max_length=225)
    description       = models.TextField(max_length=10000)
    status            = models.CharField(max_length=225, choices=CHOICES)
    datetime_created  = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    likes             = models.PositiveIntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return f"{self.title} Author: {self.author}"
