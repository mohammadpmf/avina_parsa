from django.shortcuts import render, HttpResponse


def show_lego(request):
    return render(request, 'lego.html')