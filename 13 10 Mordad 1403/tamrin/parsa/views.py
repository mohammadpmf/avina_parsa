from django.shortcuts import render


def show_parsas_homepage(request):
    context = {
        'name': 'Parsa',
        'middle_name': 'Pourmohammadi',
        'last_name': 'Fallah',
        'age': 12,
        'my_favorite_car': 'Tesla',
    }
    return render(request, 'parsa.html', context)