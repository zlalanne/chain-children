from django.conf.urls import patterns, include, url
from chain_children.views import hello

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# Examples:
# url(r'^$', 'chain_children.views.home', name='home'),
# url(r'^chain_children/', include('chain_children.foo.urls')),

# Add the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
# Add the next line to enable the admin:
# url(r'^admin/', include(admin.site.urls)),

urlpatterns = patterns('', ('^hello/$', hello))
