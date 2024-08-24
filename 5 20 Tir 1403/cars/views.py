from django.shortcuts import render, HttpResponse


def show_benz(request):
    return HttpResponse("""
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWYotwtF4YfIX4ZXb-MZqMzqGtMAsSb1CijQ&s">
""")


def show_bmw(request):
    return HttpResponse("This is BMW Page")


def hello_toyota(request):
    return render(request, "toyota.html")