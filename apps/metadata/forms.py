from django.forms import ModelForm
from apps.metadata.models import *

class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        exclude = ('contact', 'location')

class LocationForm(ModelForm):
    class Meta:
        model = Location
