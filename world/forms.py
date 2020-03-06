from django.forms import ModelForm

from data.models import Country

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ('name', 'iso_code', 'continent_id')