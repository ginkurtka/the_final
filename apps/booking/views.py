from django.shortcuts import render,redirect
from .forms import BookingForm

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
    
def create_booking(request):
    rooms = Room.objects.filter(available=True)  # dоступные комнаты
    hotels = Hotel.objects.all()  #все отели

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()  #  брони
            return redirect('router:booking:all_booking')
    else:
        form = BookingForm()

    context = {
        "form": form,
        "rooms": rooms,
        "hotels": hotels,
    }
    return render(request, 'booking/create_booking.html', context)

# def create_booking(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.user_id = request.user.id  # если пользователь уже аутентифицирован
#             booking.save()
#             return redirect('booking_success')
#     else:
#         form = BookingForm()
#     return render(request, 'booking/create_booking.html', {'form': form})
