from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.resources import ModelResource
from apps.metadata.models import Institution, Location

class HeaderApiKeyAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        username = request.META.get('HTTP_X_EDUMETA_USERNAME') or request.GET.get('username')
        api_key = request.META.get('HTTP_X_EDUMETA_API_KEY') or request.GET.get('api_key')
        if not username or not api_key:
            return self._unauthorized()
        try:
            user = User.objects.get(username=username)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()
        request.user = user
        return self.get_key(user, api_key)

class EdumetaAuthorization(Authorization):
    def is_authorized(self, request, object=None):
        return True
    def apply_limits(self, request, object_list):
        ol = []
        institutions = request.user.profile.institution.all()
        for object in object_list:
            try:
                if object.institution in institutions:
                    ol.append(object)
            except AttributeError:
                if object in institutions:
                    ol.append(object)
        return ol

class InstitutionResource(ModelResource):
    class Meta:
        queryset = Institution.objects.all()
        resource_name = 'institution'
        allowed_methods = ['get']
        excludes = ['id', 'time_updated', 'time_created']
        authentication = HeaderApiKeyAuthentication()
        authorization = EdumetaAuthorization()
        def get_object_list(self, request):
            return request.user.institutions.all()

class LocationResource(ModelResource):
    institution = fields.ForeignKey(InstitutionResource, 'institution', full=False)
    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
        allowed_methods = ['get', 'post', 'put', 'patch']
        authentication = HeaderApiKeyAuthentication()
        authorization = EdumetaAuthorization()