from django.contrib import admin
from apps.booking.models import (
    Hotel,
    Room,
    Review,
    Booking)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass