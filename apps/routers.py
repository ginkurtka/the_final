from django.urls import path, include
from apps.booking.views import home_page

urlpatterns = [
    path('', home_page, name = "home"),
    path('hotels/', include('apps.booking.urls')),
]