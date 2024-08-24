from django.shortcuts import render


def show_all_foods(request):
    list_of_foods = ['pizza', 'pasta', 'eggs']
    manager = "Parsa"
    context = {
        'modir': manager,
        'list_of_foods': list_of_foods,
    }
    return render(request, 'restaurant.html', context)