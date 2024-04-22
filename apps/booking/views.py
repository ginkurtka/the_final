from django.shortcuts import render,redirect
from apps.booking.models import (
    Hotel,
    Review,
    Room,
    Booking,
)

def home_page(request):
    return redirect('/hotels')

def login_page(request):
    return render(
        request=request,
        template_name='login.html',
        # context=context
    )

def sign_up_page(request):
    return render(
        request=request,
        template_name='sign-up.html',
        # context=context
    )

def get_all_hotels(request):
    hotel = Hotel.objects.all()
    
    context = {
        'hotels': hotel
    }
    return render(
        request=request,
        template_name='booking/all_hotels.html',
        context=context
    )
    
    def create_new_booking(request):
        users = User.objects.all()
        room = Room.objects.all()
        hotel = Hotel.objects.all()
        
        if request.method == 'POST':
            return render(
                request=request,
                template_name='booking/create_booking.html',
            )
        return render(
            request=request,
            template_name='booking/create_booking.html',
        )