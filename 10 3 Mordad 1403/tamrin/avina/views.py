from django.shortcuts import render, get_object_or_404

from .models import Customer, Order

def show_avinas_homepage(request):
    customers = Customer.objects.all().order_by('-last_name', 'first_name')
    # customer = Customer.objects.get(last_name="Fallah")
    customer = get_object_or_404(Customer, last_name="Fallah", first_name="Parsa")
    orders = Order.objects.filter(customer=customer)
    context = {
        'name': 'Avina',
        'last_name': 'Pourmohammadi Fallah',
        'age': 14,
        'favorite_color': 'blue',
        'customers': customers,
        'orders': orders
    }
    return render(request, 'index.html', context)
