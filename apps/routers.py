from django.urls import path, include
from apps.booking.views import home_page, sign_up_page, login_page

urlpatterns = [
    path('', home_page, name = "home"),
    path('sign-up/', sign_up_page, name = 'Sign up page'),
    path('login/', login_page, name = 'Login'),
    path('hotels/', include('apps.booking.urls')),
]