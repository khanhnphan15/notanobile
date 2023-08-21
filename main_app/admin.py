from django.contrib import admin
# import your models here
from .models import Meal, Photo, Reservation, AboutUs, Why_Choose_Us, Chef

# Register your models here
admin.site.register(Meal)
admin.site.register(Photo)
admin.site.register(Reservation)
admin.site.register(AboutUs)
admin.site.register(Why_Choose_Us)
admin.site.register(Chef)
