from django.conf.urls.defaults import patterns, include, url

from gmap.views import showmap, markers

urlpatterns = patterns('', 
    url(r'^markers.js/$', markers),
    url(r'^(?P<zipcode>\d*)$', showmap, name="show map"),
)
