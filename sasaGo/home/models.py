from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

SERVICE_TYPE = (
    ('motoboy', 'Motoboy'),
    ('mintruck', 'Min Truck'),
    ('tuck', 'Truck')
)

ICON_LABEL_CHOICE=(
    ('motorcycle', 'motorcycle'),
    ('shuttle-van', 'shuttle-van'),
    ('truck-moving', 'truck-moving')
)


class Vehicle(models.Model):
    vehicle_type = models.CharField(choices=SERVICE_TYPE, max_length=20)
    icon_label = models.CharField(max_length=20, choices=ICON_LABEL_CHOICE,null =True)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        verbose_name = 'Vehicles'

    def __str__(self):
        return str(self.vehicle_type)


class BookedVehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        verbose_name_plural = 'Booked Vehicles'

    def __str__(self):
        return str(self.vehicle.vehicle_type)


class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booked_by')
    vehicle = models.ManyToManyField(Vehicle, related_name='List_booking', )

    class Meta:
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return str(self.vehicle.user)

