from django.db import models

# Create your models here.

CITY_STATUS = (
    ('C', 'Capitol'),
    ('R', 'Regular')
)

class Continent(models.Model):
    id = models.IntegerField(primary_key=True)
    iso_code = models.CharField(max_length=3)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Country(models.Model):
    continent_id = models.ForeignKey(Continent, models.CASCADE)

    id = models.IntegerField(primary_key=True)
    iso_code = models.CharField(max_length=3)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class City(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=1, default='R', choices=CITY_STATUS)

    def __str__(self):
        return self.name

