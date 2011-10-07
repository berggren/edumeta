from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import *
from forms import *

def metadata(request):
    institution_form = InstitutionForm()
    location_form = LocationForm()
    institution = Institution.objects.get(pk=1)
    return render_to_response("metadata/index.html", {'institution_form': institution_form, 'location_form': location_form, 'institution': institution}, RequestContext(request))
