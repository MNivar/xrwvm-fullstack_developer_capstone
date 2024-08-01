from django.contrib import admin
from .models import CarModel, CarMake

# Register your models here.


# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['name', 'description']


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'type', 'year', 'car_make']
    inlines = [CarModelInline]


# Register models here
admin.site.register(CarModel)
admin.site.register(CarMake)
