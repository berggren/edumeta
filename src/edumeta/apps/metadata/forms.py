from django.forms import ModelForm
from apps.metadata.models import Location, Institution, Contact

class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        exclude = ('contact', 'location', 'type')

class LocationForm(ModelForm):
    class Meta:
        model = Location

class ContactForm(ModelForm):
    class Meta:
        model = Contact
