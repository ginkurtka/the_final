from django.shortcuts import render
from apps.booking.models import Hotel

def home_page(request):
    return render(
        request=request,
        template_name='main.html',
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