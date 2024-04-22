from django.urls import path
from .views import get_all_hotels, create_booking

app_name = "booking"

urlpatterns = [
    path('', get_all_hotels, name = "all_booking"),
    path('create/', create_booking , name ='create_booking')
]