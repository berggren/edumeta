__author__ = 'jbn'

from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.resources import ModelResource
from tastypie.utils import trailing_slash
from apps.metadata.models import Institution, Location

class InstitutionResource(ModelResource):
    class Meta:
        queryset = Institution.objects.all()
        resource_name = 'institution'
        allowed_methods = ['get']
        #authorization = Authorization()
        #authentication = ApiKeyAuthentication()

class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
        allowed_methods = ['get']
        #authorization = Authorization()
        #authentication = ApiKeyAuthentication()
