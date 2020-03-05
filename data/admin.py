from django.contrib import admin

from .models import Continent, Country, City

# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    list_editable = ('status',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'iso_code', 'name')

@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ('id', 'iso_code', 'name')
