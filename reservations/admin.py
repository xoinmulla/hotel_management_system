from django.contrib import admin
from .models import Hotel, Room, Reservations, Rating

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Reservations)
admin.site.register(Rating)
