from django.forms import ModelForm
from apps.metadata.models import Location, Institution, Contact
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        exclude = ('contact', 'location', 'type')

class LocationForm(ModelForm):
    class Meta:
        model = Location
    def clean_latitude(self):
	value = self.cleaned_data.get('latitude','')
	try: 
		lat = float(value)
	except ValueError as e: raise ValidationError(_('Invalid latitude'))
	if lat < 55 or lat > 71:
		raise ValidationError(_('Invalid latitude value. Between 55-71'))
	return value
    def clean_longitude(self):
        value = self.cleaned_data.get('longitude','')
        try: 
                lon = float(value)
        except ValueError as e: raise ValidationError(_('Invalid longitude'))
        if lon < 10 or lon > 25:
                raise ValidationError(_('Invalid longitude value. Between 10-25'))
	return value
			
class ContactForm(ModelForm):
    class Meta:
        model = Contact
