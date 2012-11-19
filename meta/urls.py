from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from tastypie.api import Api
from api_v1 import InstitutionResource as InstitutionResource_v1
from api_v1 import LocationResource as LocationResource_v1
from api_v1 import ContactResource as ContactResource_v1
from api_v1 import PublicLocationResource as PublicLocationResource_v1

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(InstitutionResource_v1())
v1_api.register(ContactResource_v1())
v1_api.register(LocationResource_v1())
v1_api.register(PublicLocationResource_v1())

urlpatterns = patterns('',
    (r'^$',                                 'apps.metadata.views.index'),
    (r'^institution$',                      'apps.metadata.views.institution'),
    (r'^location/add$',                     'apps.metadata.views.location'),
    (r'^location/(?P<id>[0-9]+)/delete$',   'apps.metadata.views.delete_location'),
    (r'^location/(?P<id>[0-9]+)$',          'apps.metadata.views.location'),
    (r'^institution/add$',                  'apps.metadata.views.institution'),
    (r'^institution/(?P<id>[0-9]+)$',       'apps.metadata.views.edit_institution'),
    (r'^contact/add$',                      'apps.metadata.views.contact'),
    (r'^contact/(?P<id>[0-9]+)$',           'apps.metadata.views.contact'),
    (r'^contact/(?P<id>[0-9]+)/delete$',    'apps.metadata.views.delete_contact'),
    (r'^institution.xml$',                  'apps.metadata.views.metadata'),
    (r'^developer/api',                     'django.views.generic.simple.direct_to_template', {'template': 'api.html'}),
    (r'^embed',                             'django.views.generic.simple.direct_to_template', {'template': 'embed.html'}),
    (r'^api/',                              include(v1_api.urls)),
    url(r'^admin/',                         include(admin.site.urls)),
    (r'^accounts/login-federated/$',        'apps.auth.views.saml_login'),
    (r'^accounts/logout/$',                 'apps.auth.views.saml_logout'),
    (r'^site_media/(?P<path>.*)$',          'django.views.static.serve', {'document_root': '/home/jbn/stuff/work/code/edumeta/meta/static', 'show_indexes': True}),
)
