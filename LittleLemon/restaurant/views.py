from django.shortcuts import render
from .models import MenuItem

def home(request):
    return render(request, 'index.html')

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html', {'items': items})

def bookings(request):
    return render(request, 'book.html')