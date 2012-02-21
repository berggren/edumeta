from django.forms import ModelForm
from apps.metadata.models import Location, Institution

class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        exclude = ('contact', 'location')

class LocationForm(ModelForm):
    class Meta:
        model = Location
        #exclude = ('institution')
