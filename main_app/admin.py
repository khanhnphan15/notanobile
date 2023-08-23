from django.contrib import admin
# import your models here
from .models import Meal, Category, Photo, Reservation, AboutUs, Why_Choose_Us, Chef, Wine

# Register your models here
admin.site.register(Meal)
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Reservation)
admin.site.register(AboutUs)
admin.site.register(Why_Choose_Us)
admin.site.register(Chef)
admin.site.register(Wine)
