from django.conf.urls.defaults import patterns, include, url
from gmap.views import showmap, markers, gmap_search

urlpatterns = patterns('', 
    url(r'^markers.js$', markers),
    url(r'^search/?', gmap_search, name="gmap_search"),
    url(r'^(?P<address>.*)$', showmap, name="show map"),
)
