from django.contrib import admin
from reservationApp.models import Location, Bus, Schedule, Booking
admin.site.register(Location)
admin.site.register(Bus)
admin.site.register(Schedule)
admin.site.register(Booking)
