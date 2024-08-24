from django.urls import path

from . import views

urlpatterns = [
    path('benz/', views.show_benz),
    path('bmw/', views.show_bmw),
    path('toyota/', views.hello_toyota),
]
