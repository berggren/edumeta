from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from tastypie.api import Api
from api import InstitutionResource, LocationResource, ContactResource, PublicLocationResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(InstitutionResource())
v1_api.register(ContactResource())
v1_api.register(LocationResource())
v1_api.register(PublicLocationResource())

urlpatterns = patterns('',
    (r'^$',                             'apps.metadata.views.index'),
    (r'^location/add$',                 'apps.metadata.views.location'),
    (r'^location/(?P<id>[0-9]+)$',      'apps.metadata.views.location'),
    (r'^institution/add$',              'apps.metadata.views.institution'),
    (r'^institution/(?P<id>[0-9]+)$',   'apps.metadata.views.institution'),
    (r'^contact/add$',                  'apps.metadata.views.contact'),
    (r'^contact/(?P<id>[0-9]+)$',       'apps.metadata.views.contact'),
    (r'^developer/api',                 'django.views.generic.simple.direct_to_template', {'template': 'api.html'}),
    (r'^api/',                          include(v1_api.urls)),

    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', login,       {'template_name': "login.html"}),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jbn/stuff/work/code/edumeta/meta/static', 'show_indexes': True}),
)
