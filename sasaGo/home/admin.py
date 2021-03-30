from django.contrib import admin

# Register your models here.
from .models import Vehicle, BookedVehicle, Bookings

admin.site.register(Vehicle)
admin.site.register(BookedVehicle)
admin.site.register(Bookings)
