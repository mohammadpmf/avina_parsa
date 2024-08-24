from django.shortcuts import render

from .models import Customer

def show_avinas_homepage(request):
    customers = Customer.objects.all()
    context = {
        'name': 'Avina',
        'last_name': 'Pourmohammadi Fallah',
        'age': 14,
        'favorite_color': 'blue',
        'customers': customers,
    }
    return render(request, 'index.html', context)