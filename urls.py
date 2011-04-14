from django.conf.urls.defaults import patterns, include, url

from gmap.views import showmap

urlpatterns = patterns('', 
    url(r'^(?P<zipcode>\d*)$', showmap, name="show map"),
)
