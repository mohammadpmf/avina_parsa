from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_parsas_homepage),
]
