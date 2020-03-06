from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from data.models import Continent, Country, City, CityTypesQuerySet
from .forms import CountryForm

# Create your views here.

@login_required
def home(request):
    # if not request.user.is_authenticated:
    #     return redirect('world_home')
    
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

@login_required
def add_country(request):
    if request.method == "POST":
        country = CountryForm(data=request.POST)
        if country.is_valid():
            country.save()
            return redirect('world_home')
    else:
        country_form = CountryForm()
    return render(request, "world/add_country.html", {'form': country_form})