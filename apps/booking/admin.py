from django.contrib import admin
from apps.booking.models import Hotel


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass
