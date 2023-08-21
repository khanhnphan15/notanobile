from django.contrib import admin
# import your models here
from .models import Meal, Photo, Reservation, AboutUs, Chef

# Register your models here
admin.site.register(Meal)
admin.site.register(Photo)
admin.site.register(Reservation)
admin.site.register(AboutUs)
admin.site.register(Chef)
