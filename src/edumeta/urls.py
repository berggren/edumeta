from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'apps.metadata.views.metadata'),
    # Examples:
    # url(r'^$', 'edumeta.views.home', name='home'),
    # url(r'^edumeta/', include('edumeta.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/login/$', login,       {'template_name': "login.html"}),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jbn/stuff/work/code/edumeta/src/edumeta/static', 'show_indexes': True}),
)
