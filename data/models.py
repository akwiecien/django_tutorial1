from django.db import models

# Create your models here.

CITY_TYPES = (
    ('C', 'Capitol'),
    ('R', 'Regular')
)

class CityTypesQuerySet(models.QuerySet):
    def get_capitol_cities(self):
        return self.filter(models.Q(type='C'))
    
class Continent(models.Model):
    id = models.AutoField(primary_key=True)
    iso_code = models.CharField(max_length=3)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Country(models.Model):
    continent_id = models.ForeignKey(Continent, models.CASCADE)

    id = models.AutoField(primary_key=True)
    iso_code = models.CharField(max_length=3, verbose_name="ISO Code", help_text="ISO 3166-1 alfa-3 standard")
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class City(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=1, default='R', choices=CITY_TYPES, verbose_name='Typ', help_text="capitol or regular")

    objects = CityTypesQuerySet.as_manager()

    def __str__(self):
        return self.name
