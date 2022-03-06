from django.contrib import admin
from .models import Customer, Status, Advertisement, Broadcast, Rating

admin.site.register(Customer)
admin.site.register(Status)
admin.site.register(Advertisement)
admin.site.register(Broadcast)
admin.site.register(Rating)