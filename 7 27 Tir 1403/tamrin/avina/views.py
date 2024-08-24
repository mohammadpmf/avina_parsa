from django.shortcuts import render


def show_avinas_homepage(request):
    context = {
        'name': 'Avina',
        'last_name': 'Pourmohammadi Fallah',
        'age': 14,
        'favorite_color': 'blue',
    }
    return render(request, 'index.html', context)