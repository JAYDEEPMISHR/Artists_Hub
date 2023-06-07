from django.contrib import admin
from .models import User,Video,Photo,Booking

# Register your models here.

admin.site.register(User)
admin.site.register(Video)
admin.site.register(Photo)
admin.site.register(Booking)

