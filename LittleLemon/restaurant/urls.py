from django.urls import path
from .views import home , menu, bookings

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('book/', bookings, name='bookings'),
]