from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context
from django.contrib.auth.decorators import login_required
from models import *
from forms import *

def index(request):
    institutions = Institution.objects.all()
    locations = Location.objects.all()
    ap_no = Location.objects.all().aggregate(Sum('ap_no'))['ap_no__sum']
    ap_no_v6 = Location.objects.filter(ipv6=True).aggregate(Sum('ap_no'))['ap_no__sum']
    return render_to_response("index.html", {'institutions': institutions, 'locations': locations, 'ap_no': ap_no,'ap_no_v6_p':float(ap_no_v6)/float(ap_no)*100}, RequestContext(request))

@login_required
def institution(request):
    form = InstitutionForm()
    institutions = request.user.profile.institution.all()
    location_form = LocationForm()
    location_form.fields["institution"].queryset = institutions
    contact_form = ContactForm()
    contact_form.fields["institution"].queryset = institutions
    return render_to_response("metadata/institution.html", {'form': form, 'institutions': institutions, 'location_form': location_form, 'contact_form': contact_form}, RequestContext(request))

@login_required
def edit_institution(request, id=None):
    if id:
        institution = Institution.objects.get(pk=id)
        form = InstitutionForm(instance=institution)
        if not institution in request.user.profile.institution.all():
            raise PermissionDenied
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
    return render_to_response("metadata/edit_institution.html", {'form': form, 'institution': institution}, RequestContext(request))

@login_required
def contact(request, id=None):
    institutions = request.user.profile.institution.all()
    if id:
        contact = Contact.objects.get(pk=id)
        form = ContactForm(instance=contact)
        form.fields["institution"].queryset = institutions
        if not contact.institution in request.user.profile.institution.all():
            raise PermissionDenied
    else:
        form = ContactForm()
        form.fields["institution"].queryset = institutions
    if request.method == "POST":
        if id:
            contact = Contact.objects.get(pk=id)
            form = ContactForm(request.POST, instance=contact)
            if not contact.institution in request.user.profile.institution.all():
                raise PermissionDenied
        else:
            form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/institution")
    return render_to_response("metadata/contact.html", {'form': form, 'contact': contact}, RequestContext(request))

@login_required
def location(request, id=None):
    institutions = request.user.profile.institution.all()
    if id:
        location = Location.objects.get(pk=id)
        form = LocationForm(instance=location)
        form.fields["institution"].queryset = institutions
        if not location.institution in request.user.profile.institution.all():
            raise PermissionDenied
    else:
        form = LocationForm()
        form.fields["institution"].queryset = institutions
    if request.method == "POST":
        if id:
            location = Location.objects.get(pk=id)
            form = LocationForm(request.POST, instance=location)
            if not location.institution in request.user.profile.institution.all():
                raise PermissionDenied
        else:
            form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/institution")
    return render_to_response("metadata/location.html", {'form': form, 'location': location}, RequestContext(request))

@login_required
def delete_location(request, id=None):
    location = Location.objects.get(pk=id)
    if not location.institution in request.user.profile.institution.all():
        raise PermissionDenied
    location.delete()
    return HttpResponseRedirect('/institution')

@login_required
def delete_contact(request, id=None):
    contact = Contact.objects.get(pk=id)
    if not contact.institution in request.user.profile.institution.all():
        raise PermissionDenied
    contact.delete()
    return HttpResponseRedirect('/institution')

def metadata(request):
    institutions = Institution.objects.all()
    t = loader.get_template("metadata/metadata.xml")
    c = Context({"institutions": institutions})
    return HttpResponse(t.render(c), mimetype="text/xml")
