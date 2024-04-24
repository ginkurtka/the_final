from django.urls import path, include
from apps.booking.views import home_page, sign_up_page, login_page

app_name = 'router'

urlpatterns = [
    path('', home_page, name = "home"),
    path("user/", include('apps.user.urls')),
    path('hotels/', include('apps.booking.urls')),
]