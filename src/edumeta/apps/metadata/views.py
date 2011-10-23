from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import *
from forms import *

@login_required
def index(request):
    form = InstitutionForm()
    location_form = LocationForm()
    institutions = request.user.profile.institution.all()
    return render_to_response("metadata/index.html", {'form': form, 'institutions': institutions, 'location_form': location_form}, RequestContext(request))

@login_required
def institution(request, id=None):
    if id:
        institution = Institution.objects.get(pk=id)
        form = InstitutionForm(instance=institution)
    else:
        form = InstitutionForm()
    if request.method == "POST":
        if id:
            institution = Institution.objects.get(pk=id)
            form = InstitutionForm(request.POST, instance=institution)
        else:
            form = InstitutionForm(request.POST)
        if form.is_valid():
            institution = form.save()
            profile = request.user.profile
            institution.userprofile_set.add(profile)
            return HttpResponseRedirect("/")
    return render_to_response("metadata/institution.html", {'form': form, 'institution': institution}, RequestContext(request))

@login_required
def location(request, id=None):
    if id:
        location = Location.objects.get(pk=id)
        form = LocationForm(instance=location)
    else:
        form = LocationForm()
    if request.method == "POST":
        if id:
            location = Location.objects.get(pk=id)
            form = LocationForm(request.POST, instance=location)
        else:
            form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save()
            institution = Institution.objects.get(pk=1)
            location.institution_set.add(institution)
            return HttpResponseRedirect("/")
    return render_to_response("metadata/location.html", {'form': form, 'location': location}, RequestContext(request))
