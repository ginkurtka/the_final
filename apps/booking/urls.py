from django.urls import path
from apps.booking.views import get_all_hotels

urlpatterns = [
    path('', get_all_hotels),
]