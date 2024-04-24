from django.urls import path, include
from apps.booking.views import home_page, sign_up_page, login_page

app_name = 'router'

urlpatterns = [
    path('', home_page, name = "home"),
    path('sign-up/', sign_up_page, name = 'Sign up page'),
    path('login/', login_page, name = 'Login'),
    path('sign-up/', sign_up_page, name = 'Sign up page'),
    path('login/', login_page, name = 'Login'),
    path('hotels/', include('apps.booking.urls')),
]