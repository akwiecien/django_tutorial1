from django.shortcuts import render

from data.models import Continent, Country, City, CityStatusQuerySet

# Create your views here.
def home(request):

    continents = list(Continent.objects.all())
    countries = list(Country.objects.all())
    cities = list(City.objects.all())

    capitols = City.objects.get_capitol_cities()

    return render(request, "world/home.html",
        {
            'continents_amount': Continent.objects.count(),
            'countries_amount': Country.objects.count(),
            'cities_amount': City.objects.count(),
            'continents': continents,
            'countries': countries,
            'cities': cities,
            'capitols': capitols
        })